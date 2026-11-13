#!/usr/bin/env python3
"""Refresh sources/READI-sample-N.json with the FHIR Bundles served by the READI engine.

Usage:
    python3 sources/update-readi-samples.py            # all samples (1-10)
    python3 sources/update-readi-samples.py 1 4 8      # only these samples
    python3 sources/update-readi-samples.py --dry-run  # fetch and report, write nothing

The API answers with a JSON-LD collection whose `member` array holds a single
Bundle; that Bundle (without the JSON-LD `@...` keys) is written to the sample file.

Usage: python3 sources/update-readi-samples.py
"""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://readi-engine.io/api/public/clinical_trials/fhir/es"
SOURCES = Path(__file__).resolve().parent

SAMPLES = {
    1: "NCT01444456",
    2: "NCT04077723",
    3: "NCT04710615",
    4: "NCT05841355",
    5: "NCT05160337",
    6: "NCT06422078",
    7: "NCT04436744",
    8: "2023-509661-21-00",
    9: "2024-512278-92-00",
    10: "NCT07203378",
    11: "NCT06509776",
    12: "NCT07577804",
    13: "NCT07301736",
    14: "NCT06521567",
}


def fetch(identifier):
    query = urllib.parse.urlencode({
        "page": 1,
        "itemsPerPage": 15,
        "entry.resource.identifier.value": identifier,
    })
    req = urllib.request.Request(f"{API}?{query}", headers={
        "Accept": "application/json",
        # the default Python-urllib agent is rejected (403) by the server
        "User-Agent": "curl/8.7.1",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)
    # application/json -> plain array; JSON-LD -> {"member": [...]}
    members = data if isinstance(data, list) else data.get("member")
    if not members:
        raise ValueError("empty response (no bundle returned)")
    if len(members) != 1:
        print(f"  warning: {len(members)} bundles returned, using the first", file=sys.stderr)
    return strip_jsonld(members[0])


def strip_jsonld(node):
    """Drop JSON-LD bookkeeping keys (@id, @type, @context) recursively."""
    if isinstance(node, dict):
        return {k: strip_jsonld(v) for k, v in node.items() if not k.startswith("@")}
    if isinstance(node, list):
        return [strip_jsonld(v) for v in node]
    return node


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("numbers", nargs="*", type=int, help="sample numbers (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="do not write files")
    args = parser.parse_args()

    numbers = args.numbers or sorted(SAMPLES)
    unknown = [n for n in numbers if n not in SAMPLES]
    if unknown:
        parser.error(f"unknown sample number(s): {unknown}")

    failed = []
    for n in numbers:
        identifier = SAMPLES[n]
        target = SOURCES / f"READI-sample-{n}.json"
        print(f"[{n}] {identifier} -> {target.name}")
        try:
            bundle = fetch(identifier)
        except (urllib.error.URLError, ValueError, json.JSONDecodeError) as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            failed.append(n)
            continue
        entries = len(bundle.get("entry", []))
        print(f"  {entries} entries")
        if not args.dry_run:
            target.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if failed:
        print(f"Failed: {failed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
