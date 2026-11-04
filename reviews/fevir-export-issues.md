# FEvIR "Copy FHIR values" export – open issues

Date: 2026-11-04

Source: the study Bundles exported from FEvIR with the **Copy FHIR values** function
(`sources/READI-sample-*.json`, copied unchanged to `examples/READI-sample-*.json`).

## Issues

| # | Issue | Evidence | Impact | Possible resolution |
|---|---|---|---|---|
| 1 | The exported JSON is not a valid FHIR resource: the root object has no `resourceType` property | All 10 samples start with `{ "id": …, "url": …, "type": …, "entry": [ … ] }`. The resources inside `entry[].resource` do have `resourceType` | The validator and other FHIR tools cannot recognise the file as a resource, so the samples cannot be validated or loaded as exported | FEvIR should output `"resourceType": "Bundle"` as the first property of the root object. Until then, add it by hand (or in `sources/fevir-sample-to-r4.py`) before using a sample |

Status of #1: fixed by hand in `examples/READI-sample-2.json` … `READI-sample-10.json`
(2026-11-04). `sources/READI-sample-*.json` are kept as exported. Still to be fixed in FEvIR.

Expected start of an exported Bundle:

```json
{
  "resourceType": "Bundle",
  "id": "…",
  …
}
```
