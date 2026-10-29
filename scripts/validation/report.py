#!/usr/bin/env python3
"""Compare FHIR validator results for examples/ against a committed baseline.

Reads the output of `validator_cli.jar ... -output results.json` (a Bundle of
OperationOutcomes, or a single OperationOutcome), compares every issue with
the baseline and writes a Markdown report.

Exit code 1 when there is a regression:
  - a new error/fatal issue not present in the baseline, or
  - an example under an `invalid/` folder that no longer produces any error.

Usage:
  report.py results.json --baseline scripts/validation/baseline.json --report report.md
  report.py results.json --baseline scripts/validation/baseline.json --update-baseline
"""

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

EXT_FILE = "http://hl7.org/fhir/StructureDefinition/operationoutcome-file"
EXT_MSG_ID = "http://hl7.org/fhir/StructureDefinition/operationoutcome-message-id"
EXT_LINE = "http://hl7.org/fhir/StructureDefinition/operationoutcome-issue-line"

SEVERITIES = ["fatal", "error", "warning", "information"]
BLOCKING = {"fatal", "error"}


def ext_value(resource, url):
    for ext in resource.get("extension", []):
        if ext.get("url") == url:
            for key, value in ext.items():
                if key.startswith("value"):
                    return value
    return None


def normalise_path(path, root):
    path = Path(path)
    try:
        path = path.resolve().relative_to(root.resolve())
    except ValueError:
        pass
    return path.as_posix()


def load_results(results_file, root):
    """Return {file: [issue, ...]} from the validator output."""
    data = json.loads(Path(results_file).read_text(encoding="utf-8"))
    if data.get("resourceType") == "Bundle":
        outcomes = [e["resource"] for e in data.get("entry", [])]
    else:
        outcomes = [data]

    results = {}
    for oo in outcomes:
        file = normalise_path(ext_value(oo, EXT_FILE) or "unknown", root)
        issues = []
        for issue in oo.get("issue", []):
            text = issue.get("details", {}).get("text", "") or issue.get("diagnostics", "")
            # The validator reports a clean file as a single "All OK" information issue
            if issue.get("severity") == "information" and text == "All OK":
                continue
            where = (issue.get("expression") or issue.get("location") or [""])[0]
            issues.append({
                "severity": issue.get("severity", "error"),
                "id": ext_value(issue, EXT_MSG_ID) or issue.get("code", ""),
                "expression": where,
                "line": ext_value(issue, EXT_LINE),
                "text": text,
            })
        results[file] = issues
    return results


def key(issue):
    # Message text changes between validator releases; the message id and
    # location are stable enough to recognise the same issue across runs
    return (issue["severity"], issue["id"], issue["expression"])


def is_negative(file):
    return "invalid" in Path(file).parts


def compare(results, baseline):
    """Return per-file diff: {file: {"new": [...], "fixed": [...], "known": [...]}}."""
    diff = {}
    for file in sorted(set(results) | set(baseline)):
        current = results.get(file)
        expected = baseline.get(file, [])
        if current is None:
            diff[file] = {"removed": True, "new": [], "fixed": [], "known": []}
            continue
        remaining = Counter(key(i) for i in expected)
        new, known = [], []
        for issue in current:
            k = key(issue)
            if remaining[k] > 0:
                remaining[k] -= 1
                known.append(issue)
            else:
                new.append(issue)
        fixed = []
        for issue in expected:
            if remaining[key(issue)] > 0:
                remaining[key(issue)] -= 1
                fixed.append(issue)
        diff[file] = {"removed": False, "new": new, "fixed": fixed, "known": known}
    return diff


def counts(issues):
    c = Counter(i["severity"] for i in issues)
    return c["fatal"] + c["error"], c["warning"], c["information"]


def md_escape(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def issue_line(issue):
    loc = f"`{issue['expression']}`" if issue["expression"] else ""
    line = f" (line {issue['line']})" if issue.get("line") else ""
    return f"- **{issue['severity']}** {loc}{line}: {md_escape(issue['text'])} <sub>[{issue['id']}]</sub>"


def build_report(results, diff, baseline_files, context):
    lines = ["# READI examples – validation report", ""]
    for label, value in context.items():
        if value:
            lines.append(f"- **{label}:** {value}")
    lines.append("")

    regressions = []
    rows = []
    for file, d in diff.items():
        if d["removed"]:
            rows.append(f"| `{file}` | – | – | – | removed (still in baseline) | ⚪ |")
            continue
        errors, warnings, infos = counts(results[file])
        new_blocking = [i for i in d["new"] if i["severity"] in BLOCKING]
        negative = is_negative(file)
        if negative and errors == 0:
            status = "❌ expected to fail but is valid"
            regressions.append(file)
        elif new_blocking:
            status = "❌ new errors"
            regressions.append(file)
        elif d["new"]:
            status = "⚠️ new warnings"
        elif file not in baseline_files:
            status = "🆕 new example"
        elif d["fixed"]:
            status = "✅ improved"
        else:
            status = "✅ unchanged"
        delta = f"+{len(d['new'])} / -{len(d['fixed'])}"
        kind = "negative" if negative else "positive"
        rows.append(f"| `{file}` | {errors} | {warnings} | {infos} | {delta} | {status} ({kind}) |")

    total = len([d for d in diff.values() if not d["removed"]])
    if regressions:
        lines.append(f"**Result: ❌ {len(regressions)} of {total} examples regressed.**")
    else:
        lines.append(f"**Result: ✅ no regressions in {total} examples.**")
    lines += [
        "",
        "| Example | Errors | Warnings | Info | Δ vs baseline (new / fixed) | Status |",
        "|---|---:|---:|---:|---|---|",
        *rows,
        "",
    ]

    for title, bucket in (("New issues", "new"), ("Fixed issues (no longer reported)", "fixed")):
        section = [(f, d[bucket]) for f, d in diff.items() if d[bucket]]
        if not section:
            continue
        lines += [f"## {title}", ""]
        for file, issues in section:
            lines.append(f"### `{file}`")
            lines += [issue_line(i) for i in issues]
            lines.append("")

    known = [(f, d["known"]) for f, d in diff.items() if d["known"]]
    if known:
        lines += ["<details><summary>Known issues (accepted in the baseline)</summary>", ""]
        for file, issues in known:
            lines.append(f"**`{file}`**")
            lines += [issue_line(i) for i in issues]
            lines.append("")
        lines += ["</details>", ""]

    return "\n".join(lines), regressions


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", help="validator output (JSON)")
    parser.add_argument("--baseline", required=True, help="baseline JSON file")
    parser.add_argument("--report", help="Markdown report to write")
    parser.add_argument("--update-baseline", action="store_true", help="overwrite the baseline with these results")
    parser.add_argument("--root", default=".", help="repository root, used to make file paths relative")
    parser.add_argument("--context", action="append", default=[], metavar="LABEL=VALUE",
                        help="extra header lines for the report (repeatable)")
    args = parser.parse_args()

    root = Path(args.root)
    results = load_results(args.results, root)
    baseline_path = Path(args.baseline)

    if args.update_baseline:
        stored = {f: [{k: i[k] for k in ("severity", "id", "expression", "text")} for i in issues]
                  for f, issues in sorted(results.items())}
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(json.dumps(stored, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Baseline written to {baseline_path} ({len(stored)} examples)")

    baseline = json.loads(baseline_path.read_text(encoding="utf-8")) if baseline_path.exists() else {}
    diff = compare(results, baseline)
    context = dict(c.split("=", 1) for c in args.context if "=" in c)
    report, regressions = build_report(results, diff, set(baseline), context)

    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write(report + "\n")
    if not args.report and not summary:
        sys.stdout.reconfigure(encoding="utf-8")
        print(report)

    return 1 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
