"""Convert a FEvIR (R5/R6-style) READI study bundle into an R4 Bundle conformant to the READI profiles.

Usage: python fevir-sample-to-r4.py <input.json> <output.json> [bundle-id]

- R5 elements without an R4 counterpart are moved to the R5 cross-version extensions
  (hl7.fhir.uv.xver-r5.r4) or to the READI extensions (Group combinationMethod, description,
  characteristic description and relative time).
- Endpoints (outcomeMeasure) become EvidenceVariable resources, referenced from
  outcomeMeasure.reference.
- Invalid ids, unresolvable references and non-URI code systems are fixed.
"""
import json
import re
import sys

READI = "http://hl7.eu/fhir/ig/readi/StructureDefinition/"
R5 = "http://hl7.org/fhir/5.0/StructureDefinition/extension-"
BASE = "https://example.org/fhir/"

SYSTEMS = {  # FEvIR system names / non R4 URIs -> canonical URIs
    "Medical Subject Headings (NLM)": "http://terminology.hl7.org/CodeSystem/MSH",
    "Systematic Nomenclature of Medicine - Clinical Terms (IHTSDO)": "http://snomed.info/sct",
    "https://fevir.net/sevco": "http://hl7.org/fhir/study-design",
    "http://terminology.hl7.org/CodeSystem/research-study-party-role": "http://hl7.org/fhir/research-study-party-role",
    "http://terminology.hl7.org/CodeSystem/research-study-status": "http://hl7.org/fhir/research-study-status",
}

SEVCO_DISPLAY = {"SEVCO:01001": "Interventional research", "SEVCO:01002": "Observational research"}


def fix_cc(cc):
    """Return a copy of a CodeableConcept with fixed code systems."""
    cc = json.loads(json.dumps(cc))
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


def sub(url, **value):
    return ext(url, **value)


def split_time_frame(text):
    """'Title [Time Frame: xxx]' -> ('Title', 'xxx')."""
    m = re.match(r"^(.*?)\s*\[Time Frame:\s*(.*)\]\s*$", text, re.S)
    return (m.group(1).strip(), m.group(2).strip()) if m else (text.strip(), None)


def convert_group(g, id_map):
    """R5/R6 Group (eligibility criteria, criteria node or cohort) -> R4 GroupReadi."""
    out = {"resourceType": "Group", "id": id_map[g["id"]], "meta": {"profile": [READI + "group-readi"]}}
    for m in g.get("modifierExtension", []):
        if m["url"].endswith("group-combination-method"):
            out["modifierExtension"] = [ext(READI + "group-combinationMethod", valueCode=m["valueCode"])]
    if g.get("description"):
        out["extension"] = [ext(READI + "group-description", valueMarkdown=g["description"])]
    out["type"] = g.get("type", "person")
    out["actual"] = g.get("membership") == "enumerated"
    if g.get("code"):
        out["code"] = g["code"]
    if g.get("title"):
        out["name"] = g["title"]
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
                        parts.append(sub("contextCode", valueCodeableConcept=s["valueCodeableConcept"]))
                    elif s["url"] == "offsetRange":
                        parts.append(sub("offsetRange", valueRange=s["valueRange"]))
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


def convert(src, bundle_id):
    rs = next(e["resource"] for e in src["entry"] if e["resource"]["resourceType"] == "ResearchStudy")
    study_id = rs["identifier"][0]["value"]

    # ---- contained resources: new valid ids
    # The eligibility criteria and the cohorts become Bundle entries; the nested criteria nodes stay
    # contained in the eligibility criteria Group, the sites in the ResearchStudy.
    id_map, nodes, standalone, locations = {}, [], [], []
    prefix = study_id.lower()
    for c in rs.get("contained", []):
        if c["resourceType"] == "Location":
            id_map[c["id"]] = "loc-%03d" % (len(locations) + 1)
            locations.append(c)
        elif c["resourceType"] == "Group":
            if c["id"] == "eligibility-criteria":
                id_map[c["id"]] = prefix + "-eligibility-criteria"
                standalone.append(c)
            elif "comparison-group" in c["id"]:
                id_map[c["id"]] = prefix + "-cohort-" + str(int(c["id"].rsplit("-", 1)[1]) + 1)
                standalone.append(c)
            else:
                id_map[c["id"]] = "criteria-node-%d" % (len(nodes) + 1)
                nodes.append(c)
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

    contained = []
    for loc in locations:
        r4 = {"resourceType": "Location", "id": id_map[loc["id"]], "name": loc["title"], "address": loc["address"]}
        if "position" in loc:
            r4["position"] = loc["position"]
        contained.append(r4)

    # ---- endpoints -> EvidenceVariable
    evs, outcome_exts = [], []
    for e in [x for x in rs["extension"] if x["url"] == R5 + "ResearchStudy.outcomeMeasure"]:
        parts = {s["url"]: s for s in e["extension"]}
        text = parts["endpoint"]["valueReference"]["display"]
        title, time_frame = split_time_frame(text)
        level = parts["type"]["valueCodeableConcept"]["coding"][0]["code"]
        n = sum(1 for v in evs if v["_level"] == level) + 1
        ev_id = "%s-%s-endpoint-%d" % (study_id.lower(), level, n)
        ev = {
            "resourceType": "EvidenceVariable",
            "id": ev_id,
            "meta": {"profile": [READI + "evidenceVariable-readi"]},
            "identifier": [{"system": "urn:ietf:rfc:3986",
                            "value": "urn:uuid:" + parts["name"]["valueString"].split("_", 1)[1]}],
            "name": "%s%sEndpoint%d" % (study_id, level.capitalize(), n),
            "title": title,
            "status": "active",
            "description": text,
            "characteristic": [{"definitionCodeableConcept": {"text": title}}],
            "_level": level,
        }
        if time_frame:
            ev["characteristic"][0]["description"] = "Time frame: " + time_frame
        evs.append(ev)
        outcome_exts.append({"extension": [
            sub("name", valueString=title),
            sub("type", valueCodeableConcept=fix_cc(parts["type"]["valueCodeableConcept"])),
            sub("description", valueMarkdown=text),
            sub("reference", valueReference={"reference": "EvidenceVariable/" + ev_id, "display": title}),
        ], "url": R5 + "ResearchStudy.outcomeMeasure"})

    # ---- ResearchStudy extensions
    exts, status, period_start = [], None, None
    for e in rs["extension"]:
        u = e["url"]
        if u == R5 + "ResearchStudy.label":
            exts.append(e)
    exts += [e for e in rs["extension"] if e["url"] == R5 + "ResearchStudy.classifier"]
    for e in rs["extension"]:
        if e["url"] == R5 + "ResearchStudy.progressStatus":
            e = json.loads(json.dumps(e))
            for s in e["extension"]:
                if s["url"] == "state":
                    s["valueCodeableConcept"] = fix_cc(s["valueCodeableConcept"])
                    code = s["valueCodeableConcept"]["coding"][0]
                    if code["system"] == "http://hl7.org/fhir/research-study-status":
                        status = code["code"]
                    if code["code"] == "overall-study":
                        period_start = next((p["valuePeriod"].get("start") for p in e["extension"]
                                             if p["url"] == "period"), None)
                        # not a research-study-registration-activity code: overall study period = study active
                        s["valueCodeableConcept"] = {"coding": [{
                            "system": "http://hl7.org/fhir/research-study-status", "code": "active",
                            "display": "Active"}], "text": "Overall study"}
            exts.append(e)
    exts += outcome_exts
    sponsor = None
    for e in rs["extension"]:
        if e["url"] == R5 + "ResearchStudy.associatedParty":
            parts = []
            for s in e["extension"]:
                if s["url"] == "classifier" and s["valueCodeableConcept"].get("text", "").lower() == "industry":
                    s = sub("classifier", valueCodeableConcept={"coding": [{
                        "system": "http://hl7.org/fhir/research-study-party-organization-type",
                        "code": "industry", "display": "Industry"}], "text": s["valueCodeableConcept"]["text"]})
                elif "valueCodeableConcept" in s:
                    s = sub(s["url"], valueCodeableConcept=fix_cc(s["valueCodeableConcept"]))
                parts.append(s)
            exts.append({"extension": parts, "url": e["url"]})
            role = next((s["valueCodeableConcept"]["coding"][0]["code"] for s in parts if s["url"] == "role"), None)
            if role == "lead-sponsor":
                sponsor = next(s["valueString"] for s in parts if s["url"] == "name")
    exts += [e for e in rs["extension"] if e["url"] == R5 + "ResearchStudy.recruitment.targetNumber"]
    exts += [ext(R5 + "ResearchStudy.studyDesign", valueCodeableConcept=fix_cc(sd)) for sd in rs.get("studyDesign", [])]
    if rs.get("descriptionSummary"):
        exts.append(ext(R5 + "ResearchStudy.descriptionSummary", valueMarkdown=rs["descriptionSummary"]))
    # age range: R4 artifact-useContext extension (hl7.fhir.uv.extensions.r4)
    exts += [e for e in rs["extension"] if e["url"] == "http://hl7.org/fhir/StructureDefinition/artifact-useContext"]
    # researchStudy-studyRegistration duplicates progressStatus: dropped

    study = {
        "resourceType": "ResearchStudy",
        "id": study_id,
        "meta": {"profile": [READI + "researchStudy-readi"]},
        "contained": contained,
        "extension": exts,
        "identifier": rs["identifier"],
        "title": rs["title"],
        "status": status or "completed",
        "condition": [fix_cc(c) for c in rs.get("condition", [])],
        "description": rs.get("description"),
        "enrollment": [dict(r, reference=ref(r["reference"])) for r in rs.get("enrollment", [])],
    }
    if period_start:
        study["period"] = {"start": period_start}
    if sponsor:
        study["sponsor"] = {"display": sponsor}
    study["site"] = [{"reference": "#" + id_map[l["id"]], "type": "Location", "display": l["title"]} for l in locations]
    arms = []
    for a in rs.get("arm", []):
        arm = {}
        for e in a.get("extension", []):
            if e["url"].endswith("comparison-group-eligibility"):
                vr = e["valueReference"]
                arm["extension"] = [ext(R5 + "ResearchStudy.comparisonGroup.observedGroup", valueReference={
                    "reference": ref(vr["reference"]), "display": vr.get("display")})]
        arm["name"] = a["name"]
        if a.get("description"):
            arm["description"] = a["description"]
        arms.append(arm)
    if arms:
        study["arm"] = arms
    study["objective"] = [{k: v for k, v in o.items() if k in ("name", "type")} for o in rs.get("objective", [])]

    entries = [{"fullUrl": BASE + "ResearchStudy/" + study_id, "resource": study}]
    for ev in evs:
        del ev["_level"]
        entries.append({"fullUrl": BASE + "EvidenceVariable/" + ev["id"], "resource": ev})
    for g in groups:
        entries.append({"fullUrl": BASE + "Group/" + g["id"], "resource": g})
    return {"resourceType": "Bundle", "id": bundle_id, "type": "collection", "entry": entries}


if __name__ == "__main__":
    src = json.load(open(sys.argv[1], encoding="utf-8"))
    out = convert(src, sys.argv[3] if len(sys.argv) > 3 else "readi-sample-1-r4")
    with open(sys.argv[2], "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
