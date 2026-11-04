"""Convert a FEvIR (R5/R6-style) READI study bundle into an R4 Bundle conformant to the READI profiles.

Usage: python fevir-sample-to-r4.py <input.json> <output.json> [bundle-id]

The FEvIR export ("Copy FHIR values") is a Bundle with a ResearchStudy (everything else contained)
and a summary eligibility Group. The R4 Bundle (BundleReadi) has:

- the ResearchStudy (ResearchStudyReadi); R5 elements without an R4 counterpart go to the R5
  cross-version extensions (hl7.fhir.uv.xver-r5.r4) or to the READI extensions;
- one EvidenceVariable (EvidenceVariableReadi) per endpoint (outcomeMeasure) and per intervention;
- the eligibility criteria and the cohorts as Groups (GroupReadi), with the nested criteria contained
  in the eligibility criteria Group;
- the sites as Locations (LocationReadi).

Invalid ids, unresolvable references and non-URI code systems are fixed. Dropped content (no R4 or
READI equivalent): the EBM studyRegistration extension, the per-site ResearchStudy wrappers (site
status), unreferenced contained resources, the FEvIR url and the summary eligibility Group entry.
"""
import json
import re
import sys

READI = "http://hl7.eu/fhir/ig/readi/StructureDefinition/"
R5 = "http://hl7.org/fhir/5.0/StructureDefinition/extension-"
BASE = "https://example.org/fhir/"
LANGUAGE = "http://hl7.org/fhir/StructureDefinition/language"

SYSTEMS = {  # FEvIR system names / non R4 URIs -> canonical URIs
    "Medical Subject Headings (NLM)": "http://terminology.hl7.org/CodeSystem/MSH",
    "Systematic Nomenclature of Medicine - Clinical Terms (IHTSDO)": "http://snomed.info/sct",
    "Nebraska Lexicon (UNMC)": "https://www.unmc.edu/nebraska-lexicon",
    "https://fevir.net/sevco": "http://hl7.org/fhir/study-design",
    "http://terminology.hl7.org/CodeSystem/research-study-party-role": "http://hl7.org/fhir/research-study-party-role",
    "http://terminology.hl7.org/CodeSystem/research-study-status": "http://hl7.org/fhir/research-study-status",
}
SEVCO_DISPLAY = {"SEVCO:01001": "Interventional research", "SEVCO:01002": "Observational research"}

# R5 research-study-status -> R4 ResearchStudy.status
R4_STATUS = {
    "active": "active", "recruiting": "active", "enrolling-by-invitation": "active",
    "not-yet-recruiting": "approved", "active-but-not-recruiting": "closed-to-accrual",
    "suspended": "temporarily-closed-to-accrual", "terminated": "administratively-completed",
    "administratively-completed": "administratively-completed", "approved": "approved",
    "closed-to-accrual": "closed-to-accrual", "completed": "completed", "disapproved": "disapproved",
    "in-review": "in-review", "withdrawn": "withdrawn",
    "temporarily-closed-to-accrual": "temporarily-closed-to-accrual",
}
TITLE_TYPES = ["official", "scientific", "acronym", "short-title", "plain-language"]


def copy(x):
    return json.loads(json.dumps(x))


def safe_id(text, fallback):
    """A valid R4 id (A-Z a-z 0-9 - ., max 64) from text, or the fallback when too long."""
    out = re.sub(r"[^A-Za-z0-9\-.]+", "-", text).strip("-")
    return out if 0 < len(out) <= 64 else fallback


def computable_name(text):
    """A name usable by machines (evv-0: starts with an upper-case letter, then letters, digits, _)."""
    out = re.sub(r"[^A-Za-z0-9_]+", "", text)
    if not out[:1].isalpha():
        out = "Study" + out
    return out[0].upper() + out[1:]


def fix_cc(cc):
    """Return a copy of a CodeableConcept with fixed code systems."""
    cc = copy(cc)
    for c in cc.get("coding", []):
        c["system"] = SYSTEMS.get(c.get("system"), c.get("system"))
        if c["system"] == "http://hl7.org/fhir/study-design" and c.get("code") in SEVCO_DISPLAY:
            c["display"] = SEVCO_DISPLAY[c["code"]]
        if c["system"] == "http://hl7.org/fhir/research-study-party-role":
            c["display"] = c["code"]  # R5 displays are the codes
    # SNOMED CT extension concepts (partition identifier "10", e.g. UK edition) are not in the
    # International Edition: kept as text only
    national = [c for c in cc.get("coding", [])
                if c["system"] == "http://snomed.info/sct" and c.get("code", "")[-3:-1] == "10"]
    for c in national:
        cc["coding"].remove(c)
        cc.setdefault("text", c.get("display"))
    if not cc.get("coding"):
        cc.pop("coding", None)
    return cc


def ext(url, **value):
    (k, v), = value.items()
    return {"url": url, k: v}


def split_time_frame(text):
    """'Title [Time Frame: xxx]' -> ('Title', 'xxx')."""
    m = re.match(r"^(.*?)\s*\[Time Frame:\s*(.*)\]\s*$", text, re.S)
    return (m.group(1).strip(), m.group(2).strip()) if m else (text.strip(), None)


def fix_range_units(rng):
    """rng-2 compares values only: put low and high in the same unit (months -> years)."""
    low, high = rng.get("low", {}), rng.get("high", {})
    if low.get("unit") and high.get("unit") and low["unit"] != high["unit"]:
        if low["unit"].lower().startswith("month") and high["unit"].lower().startswith("year"):
            low["value"] = round(low["value"] / 12, 2)
            low["unit"] = high["unit"]


def convert_group(g, id_map):
    """R5/R6 Group (eligibility criteria, criteria node or cohort) -> R4 GroupReadi."""
    out = {"resourceType": "Group", "id": id_map[g["id"]], "meta": {"profile": [READI + "group-readi"]}}
    for m in g.get("modifierExtension", []):
        if m["url"].endswith("group-combination-method"):
            out["modifierExtension"] = [ext(READI + "group-combinationMethod", valueCode=m["valueCode"])]
    if g.get("description"):
        out["extension"] = [ext(READI + "group-description", valueMarkdown=g["description"])]
    if g.get("status"):
        out["active"] = g["status"] == "active"
    out["type"] = "person"
    out["actual"] = g.get("membership") == "enumerated"
    if g.get("code"):
        out["code"] = fix_cc(g["code"])
    if g.get("title"):
        out["name"] = g["title"].strip()
    chars = []
    for ch in g.get("characteristic", []):
        c = {}
        exts = []
        if ch.get("description"):
            exts.append(ext(READI + "group-characteristic-description", valueMarkdown=ch["description"]))
        for e in ch.get("extension", []):
            if e["url"].endswith("characteristic-relative-time"):
                parts = []
                for s in e["extension"]:
                    if s["url"] == "contextCode":
                        parts.append(ext("contextCode", valueCodeableConcept=fix_cc(s["valueCodeableConcept"])))
                    elif s["url"] == "offsetRange":
                        parts.append(ext("offsetRange", valueRange=s["valueRange"]))
                exts.append({"extension": parts, "url": READI + "group-characteristic-relativeTime"})
        if exts:
            c["extension"] = exts
        c["code"] = fix_cc(ch["code"])
        for k, v in ch.items():
            if k.startswith("value"):
                if k == "valueReference":
                    v = dict(v, reference="#" + id_map[v["reference"][1:]])
                elif k == "valueCodeableConcept":
                    v = fix_cc(v)
                c[k] = v
        c["exclude"] = ch.get("exclude", False)
        chars.append(c)
    if chars:
        out["characteristic"] = chars
    return out


def convert_practitioner(c, new_id):
    out = {"resourceType": c["resourceType"], "id": new_id}
    if c["resourceType"] == "Practitioner":
        out.update({k: c[k] for k in ("name", "telecom") if c.get(k)})
        return out
    # PractitionerRole: R5 contact -> R4 practitioner (display) and telecom
    contact = (c.get("contact") or [{}])[0]
    if c.get("practitioner"):
        out["practitioner"] = c["practitioner"]
    elif contact.get("name"):
        out["practitioner"] = {"display": contact["name"][0].get("text")}
    if c.get("organization"):
        out["organization"] = c["organization"]
    if c.get("code"):
        out["code"] = [fix_cc(x) for x in c["code"]]
    if contact.get("telecom"):
        out["telecom"] = contact["telecom"]
    return out


def convert_evidence_variable(c, new_id):
    """A contained R5 EvidenceVariable (an intervention) -> EvidenceVariableReadi."""
    name = c.get("name")
    if isinstance(name, list):  # FEvIR exports name as [{"text": ...}]
        name = name[0].get("text") if name else None
    ev = {"resourceType": "EvidenceVariable", "id": new_id, "meta": {"profile": [READI + "evidenceVariable-readi"]}}
    exts = []
    for cl in c.get("classifier", []):
        text = cl.get("text", "")
        label, _, value = text.partition(":")
        if value:  # "Intervention Type: .DRUG"
            exts.append({"extension": [ext("name", valueString=label.strip()),
                                       ext("value", valueCodeableConcept={"text": value.strip().lstrip(".")})],
                         "url": R5 + "EvidenceVariable.category"})
        else:
            exts.append({"extension": [ext("value", valueCodeableConcept=fix_cc(cl))],
                         "url": R5 + "EvidenceVariable.category"})
    if exts:
        ev["extension"] = exts
    ev["name"] = computable_name(name or c.get("title") or new_id)
    if c.get("title"):
        ev["title"] = c["title"]
    ev["status"] = c.get("status", "active")
    if c.get("description"):
        ev["description"] = c["description"]
    ev["characteristic"] = [{"definitionCodeableConcept": {"text": c.get("title") or ev["name"]}}]
    handling = json.dumps(c.get("handling", {}))
    if "boolean" in handling or "dichotomous" in handling:
        ev["type"] = "dichotomous"
    elif "continuous" in handling:
        ev["type"] = "continuous"
    return ev


def convert(src, bundle_id):
    rs = next(e["resource"] for e in src["entry"] if e["resource"]["resourceType"] == "ResearchStudy")
    study_id = safe_id(rs["identifier"][0]["value"], "study")
    prefix = study_id.lower()
    contained_by_id = {c["id"]: c for c in rs.get("contained", [])}

    # ---- sites: ResearchStudy.site -> per-site ResearchStudy wrapper (EBM) -> Location
    site_locations = []
    for s in rs.get("site", []):
        target = s["reference"].lstrip("#")
        wrapper = contained_by_id.get(target)
        if wrapper and wrapper["resourceType"] == "ResearchStudy":
            target = wrapper["site"][0]["reference"].lstrip("#")
        elif target not in contained_by_id:
            target = target.removesuffix("-ResearchStudy")
        loc = contained_by_id.get(target)
        if loc and loc["resourceType"] == "Location" and loc not in site_locations:
            site_locations.append(loc)

    # ---- new valid ids
    # The eligibility criteria and the cohorts become Bundle entries; the nested criteria nodes stay
    # contained in the eligibility criteria Group.
    id_map, nodes, standalone, people, interventions = {}, [], [], [], []
    for n, loc in enumerate(site_locations, 1):
        id_map[loc["id"]] = "%s-site-%d" % (prefix, n)
    for c in rs.get("contained", []):
        t = c["resourceType"]
        if t == "Group":
            if c["id"] == "eligibility-criteria":
                id_map[c["id"]] = prefix + "-eligibility-criteria"
                standalone.append(c)
            elif "comparison-group" in c["id"]:
                id_map[c["id"]] = prefix + "-cohort-" + str(int(c["id"].rsplit("-", 1)[1]) + 1)
                standalone.append(c)
            else:
                id_map[c["id"]] = "criteria-node-%d" % (len(nodes) + 1)
                nodes.append(c)
        elif t in ("Practitioner", "PractitionerRole"):
            id_map[c["id"]] = safe_id(c["id"], "%s-%d" % (t.lower(), len(people) + 1))
            people.append(c)
        elif t == "EvidenceVariable":
            n = len(interventions) + 1
            id_map[c["id"]] = safe_id(c["id"], "%s-intervention-%d" % (prefix, n))
            interventions.append(c)
    standalone_ids = {id_map[g["id"]] for g in standalone}

    def ref(old):
        new = id_map[old.lstrip("#")]
        return "Group/" + new if new in standalone_ids else "#" + new

    groups = [convert_group(g, id_map) for g in standalone]
    for g in groups:
        if g["id"].endswith("-eligibility-criteria") and nodes:
            g["contained"] = [convert_group(n, id_map) for n in nodes]
            g_keys = ["resourceType", "id", "meta", "contained"]
            g.update({k: g.pop(k) for k in list(g) if k not in g_keys})  # keep R4 element order

    locations = []
    for loc in site_locations:
        r4 = {"resourceType": "Location", "id": id_map[loc["id"]], "meta": {"profile": [READI + "location-readi"]},
              "name": loc["title"]}
        if loc.get("address"):
            r4["address"] = loc["address"]
        if "position" in loc:
            r4["position"] = loc["position"]
        locations.append(r4)

    # ---- endpoints -> EvidenceVariable
    evs, outcome_exts, levels = [], [], {}
    for e in [x for x in rs["extension"] if x["url"] == R5 + "ResearchStudy.outcomeMeasure"]:
        parts = {s["url"]: s for s in e["extension"]}
        if "endpoint" in parts:
            text = parts["endpoint"]["valueReference"]["display"]
        else:
            text = parts["description"]["valueString"]
        title, time_frame = split_time_frame(text)
        type_cc = fix_cc(parts["type"]["valueCodeableConcept"])
        level = type_cc.get("coding", [{}])[0].get("code", "other")
        levels[level] = n = levels.get(level, 0) + 1
        ev_id = "%s-%s-endpoint-%d" % (prefix, level, n)
        ev = {
            "resourceType": "EvidenceVariable",
            "id": ev_id,
            "meta": {"profile": [READI + "evidenceVariable-readi"]},
            "name": computable_name("%s%sEndpoint%d" % (study_id, level.capitalize(), n)),
            "title": title,
            "status": "active",
            "description": text,
            "characteristic": [{"definitionCodeableConcept": {"text": title}}],
        }
        endpoint_name = parts.get("name", {}).get("valueString", "")
        if "_" in endpoint_name:  # Endpoint_<uuid>
            ev["identifier"] = [{"system": "urn:ietf:rfc:3986",
                                 "value": "urn:uuid:" + endpoint_name.split("_", 1)[1]}]
            ev = {k: ev[k] for k in ("resourceType", "id", "meta", "identifier", "name", "title", "status",
                                     "description", "characteristic")}
        if time_frame:
            ev["characteristic"][0]["description"] = "Time frame: " + time_frame
        evs.append(ev)
        outcome_exts.append({"extension": [
            ext("name", valueString=title),
            ext("type", valueCodeableConcept=type_cc),
            ext("description", valueMarkdown=text),
            ext("reference", valueReference={"reference": "EvidenceVariable/" + ev_id, "display": title}),
        ], "url": R5 + "ResearchStudy.outcomeMeasure"})
    evs += [convert_evidence_variable(c, id_map[c["id"]]) for c in interventions]

    # ---- ResearchStudy extensions
    exts, status, period, title = [], None, None, rs.get("title")
    for e in [x for x in rs["extension"] if x["url"] == R5 + "ResearchStudy.label"]:
        parts = []
        lang = None
        for s in e["extension"]:
            if s["url"] == "language":
                lang = s.get("valueCode")
            else:
                parts.append(ext(s["url"], valueCodeableConcept=fix_cc(s["valueCodeableConcept"]))
                             if "valueCodeableConcept" in s else copy(s))
        if lang:  # R5 label has no language: R4 language extension on the value
            for s in parts:
                if s["url"] == "value":
                    s["_valueString"] = {"extension": [ext(LANGUAGE, valueCode=lang)]}
        exts.append({"extension": parts, "url": e["url"]})
    if not title:  # R4 (and READI) require a title: first label, by title type
        labels = [({s["url"]: s for s in e["extension"]}) for e in exts]
        labels = [(p["type"]["valueCodeableConcept"].get("coding", [{}])[0].get("code"), p["value"]["valueString"])
                  for p in labels if "type" in p and "value" in p]
        labels.sort(key=lambda x: TITLE_TYPES.index(x[0]) if x[0] in TITLE_TYPES else 99)
        title = labels[0][1] if labels else rs.get("name")
    exts += [e for e in rs["extension"] if e["url"] == R5 + "ResearchStudy.classifier"]
    for e in rs["extension"]:
        if e["url"] == R5 + "ResearchStudy.progressStatus":
            e = copy(e)
            for s in e["extension"]:
                if s["url"] == "state":
                    s["valueCodeableConcept"] = fix_cc(s["valueCodeableConcept"])
                    code = s["valueCodeableConcept"]["coding"][0]
                    if code["code"] == "overall-study":
                        period = period or next((p["valuePeriod"] for p in e["extension"] if p["url"] == "period"), None)
                        # not a code of these code systems: overall study period = study active
                        s["valueCodeableConcept"] = {"coding": [{
                            "system": "http://hl7.org/fhir/research-study-status", "code": "active",
                            "display": "Active"}], "text": "Overall study"}
                    elif code["system"] == "http://hl7.org/fhir/research-study-status":
                        status = status or R4_STATUS.get(code["code"])
                        if code["code"] not in R4_STATUS.values():  # R5-only code: R4 equivalent, R5 as text
                            s["valueCodeableConcept"] = {"coding": [dict(code, code=R4_STATUS[code["code"]],
                                                                         display=R4_STATUS[code["code"]].capitalize())],
                                                         "text": code.get("display", code["code"])}
            exts.append(e)
    exts += outcome_exts
    sponsor = None
    for e in rs["extension"]:
        if e["url"] == R5 + "ResearchStudy.associatedParty":
            parts = []
            for s in e["extension"]:
                if s["url"] == "classifier" and s["valueCodeableConcept"].get("text", "").lower() == "industry":
                    s = ext("classifier", valueCodeableConcept={"coding": [{
                        "system": "http://hl7.org/fhir/research-study-party-organization-type",
                        "code": "industry", "display": "Industry"}], "text": s["valueCodeableConcept"]["text"]})
                elif "valueCodeableConcept" in s:
                    s = ext(s["url"], valueCodeableConcept=fix_cc(s["valueCodeableConcept"]))
                elif "reference" in s.get("valueReference", {}):
                    s = ext(s["url"], valueReference=dict(s["valueReference"], reference=ref(s["valueReference"]["reference"])))
                parts.append(s)
            exts.append({"extension": parts, "url": e["url"]})
            role = next((s["valueCodeableConcept"]["coding"][0]["code"] for s in parts if s["url"] == "role"), None)
            if role == "lead-sponsor":
                sponsor = next(s["valueString"] for s in parts if s["url"] == "name")
    exts += [e for e in rs["extension"] if e["url"] == R5 + "ResearchStudy.recruitment.targetNumber"]
    exts += [ext(R5 + "ResearchStudy.studyDesign", valueCodeableConcept=fix_cc(sd)) for sd in rs.get("studyDesign", [])]
    if rs.get("descriptionSummary"):
        exts.append(ext(R5 + "ResearchStudy.descriptionSummary", valueMarkdown=rs["descriptionSummary"]))
    if rs.get("name"):
        exts.append(ext(R5 + "ResearchStudy.name", valueString=rs["name"]))
    # age range: R4 artifact-useContext extension (hl7.fhir.uv.extensions.r4)
    for e in rs["extension"]:
        if e["url"] == "http://hl7.org/fhir/StructureDefinition/artifact-useContext":
            e = copy(e)
            if "valueRange" in e["valueUsageContext"]:
                fix_range_units(e["valueUsageContext"]["valueRange"])
            exts.append(e)
    # researchStudy-studyRegistration (EBM registry periods) duplicates progressStatus: dropped
    if not status:  # no study status: the status of the sites (EBM per-site ResearchStudy), if any
        site_states = [p["state"]["coding"][0]["code"] for c in rs.get("contained", [])
                       if c["resourceType"] == "ResearchStudy" for p in c.get("progressStatus", [])]
        status = next((R4_STATUS[s] for s in site_states if s in R4_STATUS), None)

    # ---- contained: the people referenced from associatedParty
    referenced = set(re.findall(r'"reference": "#([^"]+)"', json.dumps(exts)))
    contained = [convert_practitioner(c, id_map[c["id"]]) for c in people if id_map[c["id"]] in referenced]

    study = {"resourceType": "ResearchStudy", "id": study_id, "meta": {"profile": [READI + "researchStudy-readi"]}}
    if contained:
        study["contained"] = contained
    study.update({
        "extension": exts,
        "identifier": rs["identifier"],
        "title": title,
        "status": status or "completed",
    })
    if rs.get("primaryPurposeType"):
        study["primaryPurposeType"] = fix_cc(rs["primaryPurposeType"])
    if rs.get("phase"):
        study["phase"] = fix_cc(rs["phase"][0] if isinstance(rs["phase"], list) else rs["phase"])
    if rs.get("condition"):
        study["condition"] = [fix_cc(c) for c in rs["condition"]]
    if rs.get("description"):
        study["description"] = rs["description"]
    study["enrollment"] = [dict(r, reference=ref(r["reference"])) for r in rs.get("enrollment", [])]
    if period:
        study["period"] = period
    if sponsor:
        study["sponsor"] = {"display": sponsor}
    if locations:
        study["site"] = [{"reference": "Location/" + l["id"], "display": l["name"]} for l in locations]
    cohorts = {g["id"]: g for g in groups}
    arms = []
    for a in rs.get("arm", []):
        arm = {}
        for e in a.get("extension", []):
            if e["url"].endswith("comparison-group-eligibility"):
                vr = e["valueReference"]
                arm["extension"] = [ext(READI + "researchStudy-arm-eligibility", valueReference={
                    "reference": ref(vr["reference"]), "display": vr.get("display")})]
                cohort = cohorts.get(ref(vr["reference"]).split("/")[-1], {})
                if cohort.get("code"):
                    arm["type"] = cohort["code"]
        arm["name"] = a["name"]
        if a.get("description"):
            arm["description"] = a["description"]
        arm = {k: arm[k] for k in ("extension", "name", "type", "description") if k in arm}
        arms.append(arm)
    if arms:
        study["arm"] = arms
    objectives = []
    for o in rs.get("objective", []):
        obj = {}
        if o.get("description"):
            obj["extension"] = [ext(R5 + "ResearchStudy.objective.description", valueMarkdown=o["description"])]
        obj.update({k: v for k, v in o.items() if k in ("name", "_name")})
        if o.get("type"):
            obj["type"] = fix_cc(o["type"])
        objectives.append(obj)
    if objectives:
        study["objective"] = objectives

    entries = [{"fullUrl": BASE + "ResearchStudy/" + study_id, "resource": study}]
    entries += [{"fullUrl": BASE + "EvidenceVariable/" + ev["id"], "resource": ev} for ev in evs]
    entries += [{"fullUrl": BASE + "Group/" + g["id"], "resource": g} for g in groups]
    entries += [{"fullUrl": BASE + "Location/" + l["id"], "resource": l} for l in locations]
    return {"resourceType": "Bundle", "id": bundle_id, "meta": {"profile": [READI + "bundle-readi"]},
            "type": "collection", "entry": entries}


if __name__ == "__main__":
    src = json.load(open(sys.argv[1], encoding="utf-8"))
    out = convert(src, sys.argv[3] if len(sys.argv) > 3 else "readi-sample-1-r4")
    with open(sys.argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
