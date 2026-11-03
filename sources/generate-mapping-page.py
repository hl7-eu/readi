#!/usr/bin/env python3
"""Generate input/pagecontent/usdm2fhir-mapping.md from sources/USDM2FHIR_r4|r5|r6.csv.

Usage: python3 sources/generate-mapping-page.py
"""
import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "input/pagecontent/usdm2fhir-mapping.md"
TBS = "to-be-specified"
YELLOW = "background-color: #ffff99;"
GREEN = "background-color: #e6f4e6;"   # hardcoded value in the JSONata

# R4/R5 rows whose Item differs from the R6 one (R6 is the master order of the page).
ALIASES = {
    "r4": {
        "Outcome measure name": "Outcome measurement name",
        "Outcome measure description": "Outcome measurement description",
        "Outcome measure reference": "Outcome measurement reference or display",
        "Outcome measure type": "Endpoint level",
        "primary purpose type": "purpose Intent",
        "progress status extension (state, actual, period)": "progress status",
        "Extension target number (R4 replacement for recruitment.targetNumber)": "Planned enrollment number",
    },
    "r5": {
        "Outcome measure name": "Outcome measurement name",
        "Outcome measure description": "Outcome measurement description",
        "Outcome measure reference": "Outcome measurement reference or display",
        "Outcome measure type": "Endpoint level",
        "primary purpose type": "purpose Intent",
    },
}
YELLOW_ROW_PATHS = {"ResearchStudy.identifier.codeableConcept.text"}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def load(v):
    with open(ROOT / f"sources/USDM2FHIR_{v}.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows


def fhir(row):
    if row is None:
        return "—"
    v = (row["FHIR resourceType"] + "." + row["FHIR path"]).strip(".")
    return v or "—"


def is_hardcoded(jsonata):
    """True when the value produced by the JSONata expression is a literal (no data accessed)."""
    j = jsonata
    m = list(re.finditer(r"\{\s*id\s*:", j))
    tail = j[m[-1].start():] if m else j.strip()
    if not tail.startswith("{"):
        return False
    tail = re.sub(r'"[^"]*"', '""', tail)
    tail = re.sub(r"\bid\b|\btrue\b|\bfalse\b|\bnull\b", "", tail)
    return not re.search(r"[A-Za-z$@\[\]()&=]", tail)


def hardcoded_value(jsonata):
    """Describe the literal produced by a hardcoded JSONata expression.

    `<path>[filter].{id: <literal>}`  -> `<literal>` (+ `only when <filter>`)
    `{"<id>": <literal>}`             -> `<literal>` (+ `for id <id>`)
    """
    m = list(re.finditer(r"\{\s*id\s*:", jsonata))
    if m:
        v = norm(jsonata[m[-1].end():]).rstrip()
        v = v[:-1].rstrip() if v.endswith("}") else v
        filters = [norm(f) for f in re.findall(r"\[([^\]]*)\]", jsonata[:m[-1].start()])]
        return v, ("only when " + " and ".join(filters)) if filters else ""
    mo = re.match(r'^\s*\{\s*"([^"]+)"\s*:\s*(.*)\}\s*$', jsonata, re.S)
    if mo:
        return norm(mo.group(2)), f'for id "{mo.group(1)}"'
    return norm(jsonata), ""


def td(value, style="", span=1, extra=""):
    attrs = (f' colspan="{span}"' if span > 1 else "") + (f' style="{style}"' if style else "")
    return f"<td{attrs}>{html.escape(value, quote=False)}{extra}</td>"


def main():
    data = {v: load(v) for v in ("r4", "r5", "r6")}
    by = {}
    for v in ("r4", "r5"):
        d = {}
        for r in data[v]:
            key = ALIASES[v].get(r["Item"], r["Item"])
            d[norm(key)] = r
        by[v] = d
    by["r6"] = {norm(r["Item"]): r for r in data["r6"]}
    r6keys = [norm(r["Item"]) for r in data["r6"]]
    for v in ("r4", "r5"):
        extra = set(by[v]) - set(r6keys)
        if extra:
            sys.exit(f"{v}: rows not matched to R6: {sorted(extra)}")

    sections, current = {}, None
    for r in data["r6"]:
        cls = r["USDM class"].strip()
        if cls:
            current = cls
        if current is None:
            sys.exit("first row has no USDM class")
        sections.setdefault(current, []).append(r)

    out = ['<div class="stu-note" markdown="1">',
           "This mapping is a work in progress: it has not been validated yet and may change at any time.",
           "</div>", ""]
    counts = {}
    for cls, rows in sections.items():
        counts[cls] = len(rows)
        out += [f"### {cls}", "", '<div class="mapping-scroll">', '<table class="grid">', "<thead>",
                '<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th>'
                '<th colspan="3">FHIR resourceType.path</th></tr>',
                "<tr><th>R4</th><th>R5</th><th>R6</th></tr>", "</thead>", "<tbody>"]
        for r in rows:
            k = norm(r["Item"])
            usdm = f'{r["USDM class"].strip() or TBS}.{r["USDM attribute"].strip() or TBS}'
            vals = [fhir(by[v].get(k)) for v in ("r4", "r5", "r6")]
            row_yellow = vals[2] in YELLOW_ROW_PATHS
            cells = []
            u_style = YELLOW if (row_yellow or TBS in usdm) else ""
            u_extra = ""
            if TBS in usdm and is_hardcoded(r["USDM JSONata path"]):
                hv, cond = hardcoded_value(r["USDM JSONata path"])
                hv = html.escape(hv, quote=False)
                cond = f" ({html.escape(cond, quote=False)})" if cond else ""
                u_extra = f'<br/><span style="{GREEN}">hardcoded value: <code>{hv}</code>{cond}</span>'
            cells.append(td(norm(r["Item"]), YELLOW if row_yellow else ""))
            cells.append(td(usdm, u_style, extra=u_extra))
            i = 0
            while i < 3:
                j = i
                while j + 1 < 3 and vals[j + 1] == vals[i]:
                    j += 1
                bad = row_yellow or TBS in vals[i] or vals[i] == "—"
                cells.append(td(vals[i], YELLOW if bad else "", j - i + 1))
                i = j + 1
            out.append("<tr>" + "".join(cells) + "</tr>")
        out += ["</tbody>", "</table>", "</div>", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    for c, n in counts.items():
        print(f"{c}: {n}")
    print("total:", sum(counts.values()))


main()
