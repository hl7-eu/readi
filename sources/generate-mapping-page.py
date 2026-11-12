#!/usr/bin/env python3
"""Generate input/pagecontent/usdm2fhir-mapping.md from sources/USDM2FHIR_r4|r5|r6.csv.

sources/USDM2FHIR_notes.csv (Item, Notes, Highlight), matched on the R6 Item, gives the Notes column
and the cells highlighted by hand. Highlight is a space-separated list of cells (item, usdm, r4, r5,
r6, notes, or row for all of them), each optionally followed by :<colour> (yellow, the default,
orange or red), e.g. "row" or "r4 r5:orange". Highlighting by hand only adds colour to the cells
coloured automatically (yellow: to-be-specified, or no path in that FHIR version).

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
COLOURS = {  # background colours of the highlighted cells (legend text in LEGEND)
    "yellow": "background-color: #ffff99;",
    "orange": "background-color: #ffd8a8;",
    "red": "background-color: #ffb3b3;",
}
YELLOW = COLOURS["yellow"]
GREEN = "background-color: #e6f4e6;"   # hardcoded value in the JSONata
CELLS = ["item", "usdm", "r4", "r5", "r6", "notes"]
LEGEND = [
    ("yellow", "to be specified: no USDM source, no path in that FHIR version, or flagged by hand"),
    ("orange", "to be checked"),
    ("red", "known to be wrong"),
]

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
        "Intervention evidence variable type (dichotomous)": "Intervention evidence variable handling (boolean variable)",
    },
    "r5": {
        "Outcome measure name": "Outcome measurement name",
        "Outcome measure description": "Outcome measurement description",
        "Outcome measure reference": "Outcome measurement reference or display",
        "Outcome measure type": "Endpoint level",
        "primary purpose type": "purpose Intent",
        "Intervention evidence variable handling (dichotomous)": "Intervention evidence variable handling (boolean variable)",
    },
}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def load(v):
    with open(ROOT / f"sources/USDM2FHIR_{v}.csv", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows


def parse_highlight(text, item):
    """'r4 r5:orange' -> {"r4": yellow style, "r5": orange style}."""
    out = {}
    for token in text.split():
        cell, _, colour = token.lower().partition(":")
        colour = colour or "yellow"
        if colour not in COLOURS:
            sys.exit(f"notes: unknown colour {colour!r} for {item!r} (use {', '.join(COLOURS)})")
        if cell == "row":
            out.update({c: COLOURS[colour] for c in CELLS})
        elif cell in CELLS:
            out[cell] = COLOURS[colour]
        else:
            sys.exit(f"notes: unknown cell {cell!r} for {item!r} (use row, {', '.join(CELLS)})")
    return out


def load_notes(r6keys):
    """({R6 Item: note}, {R6 Item: {cell: style}}); several rows for the same Item are combined."""
    path = ROOT / "sources/USDM2FHIR_notes.csv"
    notes, highlights = {}, {}
    if not path.exists():
        return notes, highlights
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            k = norm(r["Item"])
            if k not in r6keys:
                sys.exit(f"notes: row not matched to R6: {r['Item']!r}")
            notes[k] = "; ".join(filter(None, [notes.get(k), norm(r.get("Notes") or "")]))
            highlights.setdefault(k, {}).update(parse_highlight(r.get("Highlight") or "", r["Item"]))
    return notes, highlights


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


def td(value, style="", span=1, extra="", path=False):
    attrs = (f' colspan="{span}"' if span > 1 else "") + (f' style="{style}"' if style else "")
    text = html.escape(value, quote=False)
    if path:  # long dotted paths: allow line breaks after each dot
        text = text.replace(".", ".<wbr/>")
    return f"<td{attrs}>{text}{extra}</td>"


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
    notes, highlights = load_notes(set(r6keys))

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
    legend = [f'<span style="{COLOURS[c]} padding: 0 0.5em;">{c}</span> {html.escape(text, quote=False)}'
              for c, text in LEGEND]
    legend.append(f'<span style="{GREEN} padding: 0 0.5em;">hardcoded value</span> '
                  "the JSONata expression returns a fixed value")
    out += ["<p>Cell colours: " + "; ".join(legend) + ".</p>", ""]
    counts = {}
    for cls, rows in sections.items():
        counts[cls] = len(rows)
        out += [f"### {cls}", "", '<div class="mapping-scroll">', '<table class="grid">',
                '<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/>'
                '<col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>', "<thead>",
                '<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th>'
                '<th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>',
                "<tr><th>R4</th><th>R5</th><th>R6</th></tr>", "</thead>", "<tbody>"]
        for r in rows:
            k = norm(r["Item"])
            usdm = f'{r["USDM class"].strip() or TBS}.{r["USDM attribute"].strip() or TBS}'
            vals = [fhir(by[v].get(k)) for v in ("r4", "r5", "r6")]
            manual = highlights.get(k, {})
            cells = []
            u_style = manual.get("usdm") or (YELLOW if TBS in usdm else "")
            u_extra = ""
            if TBS in usdm and is_hardcoded(r["USDM JSONata path"]):
                hv, cond = hardcoded_value(r["USDM JSONata path"])
                hv = html.escape(hv, quote=False)
                cond = f" ({html.escape(cond, quote=False)})" if cond else ""
                u_extra = f'<br/><span style="{GREEN}">hardcoded value: <code>{hv}</code>{cond}</span>'
            cells.append(td(norm(r["Item"]), manual.get("item", "")))
            cells.append(td(usdm, u_style, extra=u_extra, path=True))
            i = 0
            while i < 3:
                j = i
                while j + 1 < 3 and vals[j + 1] == vals[i]:
                    j += 1
                # a merged cell (same path in several versions) takes the first colour given by hand
                style = next((manual[f"r{4 + n}"] for n in range(i, j + 1) if f"r{4 + n}" in manual), "")
                if not style and (TBS in vals[i] or vals[i] == "—"):
                    style = YELLOW
                cells.append(td(vals[i], style, j - i + 1, path=True))
                i = j + 1
            cells.append(td(notes.get(k, ""), manual.get("notes", "")))
            out.append("<tr>" + "".join(cells) + "</tr>")
        out += ["</tbody>", "</table>", "</div>", ""]
    OUT.write_text("\n".join(out), encoding="utf-8")
    for c, n in counts.items():
        print(f"{c}: {n}")
    print("total:", sum(counts.values()))


main()
