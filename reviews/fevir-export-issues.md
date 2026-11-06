# FEvIR "Copy FHIR values" export – open issues

Date: 2026-11-04

Source: the study Bundles exported from FEvIR with the **Copy FHIR values** function
(`sources/READI-sample-*.json`, copied unchanged to `examples/READI-sample-*.json`).

## Issues

| # | Issue                                                                                          | Evidence                                                                                                                                     | Impact                                                                                                                               | Possible resolution                                                                                                                                                               |
|---|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 | The exported JSON is not a valid FHIR resource: the root object has no `resourceType` property | All 10 samples start with `{ "id": …, "url": …, "type": …, "entry": [ … ] }`. The resources inside `entry[].resource` do have `resourceType` | The validator and other FHIR tools cannot recognise the file as a resource, so the samples cannot be validated or loaded as exported | FEvIR should output `"resourceType": "Bundle"` as the first property of the root object. Until then, add it by hand (or in `sources/fevir-sample-to-r4.py`) before using a sample |

Status of #1: still to be fixed in FEvIR. `sources/READI-sample-*.json` are kept as exported; the
converter (`sources/fevir-sample-to-r4.py`) does not depend on the missing `resourceType`.

Expected start of an exported Bundle:

```json
{
  "resourceType": "Bundle",
  "id": "…",
  …
}
```

## Validation of the exported samples against FHIR R4

Run: [Validate examples #11](https://github.com/hl7-eu/readi/actions/runs/41886890245)
(2026-11-04, commit `aef588d`, validator 7.0.4, tx.fhir.org), on the 9 exported samples
`examples/READI-sample-2.json` … `READI-sample-10.json` (with only #1 fixed).

Totals: 2,005 errors, 450 warnings, 639 information messages. Errors per sample range from 39
(sample 8) to 493 (sample 7). `Bundle-readi-sample-1-r4.json`, converted with
`sources/fevir-sample-to-r4.py`, has no errors.

Each sample is a `Bundle` with one `ResearchStudy` (Locations, Groups, EvidenceVariables,
Practitioners and nested ResearchStudies as contained resources) and one `Group`.
"Count" is the number of errors or warnings across the 9 samples; "Samples" is how many of
the 9 have them. Validator message ids are shown in brackets.

### 2. Defects in the export, whatever the target FHIR version

| #    | Issue                                                                                                                                          |     Count |      Samples | Validator message                                                      | Possible resolution                                                                           |
|------|------------------------------------------------------------------------------------------------------------------------------------------------|----------:|-------------:|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| 2.1  | *`Bundle.type` is `Collection` instead of the code `collection`                                                                                |        18 |            9 | `Terminology_TX_NoValid_16`, `UNABLE_TO_INFER_CODESYSTEM`              | Export the code in lower case                                                                 |
| 2.2  | *Ids with invalid characters: `_` in the Bundle and entry ids (`fake_b_…`, `fake_r_…`, `fake_g_…`)                                             |        41 |            9 | `Resource_RES_ID_Malformed_Chars`                                      | Use only `A-Z a-z 0-9 - .`                                                                    |
| 2.3  | *Ids longer than 64 characters (up to 77), e.g. `NCT07203378-other-whole-body-resistance-training-and-aerobic-exercise`                        |        81 |            5 | `Resource_RES_ID_Malformed_Length`                                     | Shorten the generated ids (e.g. hash or counter)                                              |
| 2.4  | *Local references that do not resolve to a contained resource (`site` → `#…-Location-…-ResearchStudy`)                                         | 107 + 107 |            4 | `Reference_REF_CantResolve`, `ref-1`                                   | Make sure every `#id` points to a contained resource                                          |
| 2.5  | Contained resources not referenced from anywhere in the container                                                                              |       131 |            7 | `CONTAINED_ORPHAN_DOM3` (dom-3)                                        | Reference them (e.g. EvidenceVariables from the outcome measures) or drop them                |
| 2.6  | `meta.versionId` / `meta.lastUpdated` in contained resources                                                                                   |         9 |            9 | `dom-4`                                                                | Strip `meta` from contained resources                                                         |
| 2.7  | *Code system given as a name instead of a URI, e.g. `Medical Subject Headings (NLM)`                                                           |    12 + 3 |            4 | `Type_Specific_Checks_DT_URI_WS`, `Terminology_TX_System_Relative`     | Use the canonical URI (`http://terminology.hl7.org/CodeSystem/MSH`, `http://snomed.info/sct`) |
| 2.8  | *Empty arrays (e.g. `Group.characteristic: []`)                                                                                                |        29 |            9 | `invalid`                                                              | Omit empty properties                                                                         |
| 2.9  | *Extension with an `example.org` URL used as a **modifier** extension: `https://example.org/fhir/StructureDefinition/group-combination-method` |   54 + 54 |            9 | `Extension_EXT_Unknown_NotHere`, `TYPE_SPECIFIC_CHECKS_DT_URL_EXAMPLE` | Use a published extension (in R4: the READI extension or the R5 cross-version one)            |
| 2.10 | *`meta.profile` contains a web page, `http://hl7.org/fhir/R4/researchstudy.html`                                                               |         – |            – | (profile not found)                                                    | Remove it, or use the canonical URL of a profile                                              |
| 2.11 | *Age range `0 Month` – `120 Year`: the validator compares only the values, so `rng-2` (low < high) fails                                       |         1 | 1 (sample 8) | `rng-2`                                                                | Use the same unit for low and high                                                            |

### 3. R5/R6 content that does not exist in R4

The export follows the R6 ballot (e.g. `ValueSet group-type|6.0.0-ballot2`) and the EBM IG,
so much of it is not R4. This is expected and is what `sources/fevir-sample-to-r4.py` converts.
It shows that the export cannot be used as an R4 READI instance as it is.

| #   | Issue                                                                                                                                                                                                                                                                                                                                                                                   |        Count | Samples | Validator message                                                                                       |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|--------:|---------------------------------------------------------------------------------------------------------|
| 3.1 | *Elements not in R4: `title` (219), `characteristic.description` (105), `progressStatus` (80), `status` and `membership` on Group (24 each), `description` (18 + 8), `url` on Bundle and resources (9 + 18), `objective.description` (16), `handling` and `classifier` (15 each), `name` / `title` / `descriptionSummary` / `studyDesign` on ResearchStudy (8–9 each), and a few others |          587 |       9 | `structure` (Unrecognized property)                                                                     |
| 3.2 | *Values whose type changed since R4 (`name` on contained resources, `phase`, `characteristic`)                                                                                                                                                                                                                                                                                          |           29 |       – | `invalid`                                                                                               |
| 3.3 | `ResearchStudy.status` missing (required in R4; the export carries the status elsewhere)                                                                                                                                                                                                                                                                                                |          133 |       9 | `Validation_VAL_Profile_Minimum`                                                                        |
| 3.4 | *`ResearchStudy.site` references contained ResearchStudy resources (EBM `research-study-site` pattern); R4 allows only `Location`                                                                                                                                                                                                                                                       |     187 + 80 |       9 | `Reference_REF_WrongTarget`, `Reference_REF_BadTargetType`                                              |
| 3.5 | R4 extension `researchStudy-studyRegistration` (5.4.0) used with the R5/EBM structure: unknown sub-extension `state`, required `activity` missing, unknown code `overall-study`                                                                                                                                                                                                         | 91 + 74 + 18 |       9 | `Extension_EXT_SubExtension_Invalid`, `Validation_VAL_Profile_Minimum_SLICE`, `Unknown_Code_in_Version` |
| 3.6 | R5 cross-version extension `ResearchStudy.outcomeMeasure` with a `string` where R4 needs `markdown`                                                                                                                                                                                                                                                                                     |          114 |       8 | `Extension_PROF_Type`                                                                                   |

### 4. Definitions the validator cannot find

| #   | Issue                                                                                                                                                                                                                                                             |                    Count | Samples | Validator message                                                                                                |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------:|--------:|------------------------------------------------------------------------------------------------------------------|
| 4.1 | EBM IG resources not published at their canonical URL: CodeSystem `http://hl7.org/fhir/uv/ebm/CodeSystem/study-registry-period` (an error when used as a URL value), profiles `…/ebm/StructureDefinition/study-registry-record` and `…/research-study-site` (404) | 74 errors + 218 warnings |       9 | `Type_Specific_Checks_DT_URL_Resolve`, `not-found`, `UNKNOWN_CODESYSTEM`, `VALIDATION_VAL_PROFILE_UNKNOWN_ERROR` |
| 4.2 | FEvIR code systems such as `https://fevir.net/resources/CodeSystem/419455` cannot be resolved                                                                                                                                                                     |               (warnings) |       – | `UNKNOWN_CODESYSTEM`                                                                                             |

### 5. Warnings and information messages (not blocking)

- Codes from R5 code systems (e.g. `research-study-registration-activity`) in R4 `ResearchStudyStatus` bindings: 145 warnings (`Terminology_TX_NoValid_2_CC`).
- Several matching profiles for references to contained Practitioners (R4 and R5 cross-version profile): 48 warnings (`Reference_REF_MultipleMatches`).
- R6 ValueSet `group-type|6.0.0-ballot2` not found: 24 warnings.
- No narrative (dom-6, 18), `Identifier.type` without a code (15).
- Information only: bindings without a source (361), profile matching details (180), canonical URLs not resolved (98).

## Conversion of the samples to R4 (READI profiles)

Date: 2026-11-04

All 10 samples are converted with `sources/fevir-sample-to-r4.py` into
`examples/Bundle-readi-sample-<n>-r4.json` (BundleReadi); the raw exports were removed from `examples/`.
Local validation (validator 7.0.4, tx.fhir.org): **0 errors** in all 10. The remaining warnings come from
the source data (FEvIR code system `419455`, registration-activity codes in `progressStatus`, identifier
types with text only, an NCI code unknown to the validator) or from validator ambiguities (contained
Practitioners matching both the R4 and the R5 cross-version profile).

How the R5/R6 content is represented:

| FEvIR (R5/R6/EBM)                              | R4 Bundle                                                                                                                                                                                                                                           |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ResearchStudy                                  | ResearchStudyReadi; R5 elements in the R5 cross-version extensions (`label`, `classifier`, `progressStatus`, `outcomeMeasure`, `associatedParty`, `recruitment.targetNumber`, `studyDesign`, `descriptionSummary`, `name`, `objective.description`) |
| `title` missing (sample 8)                     | First label, by title type (official, scientific, …)                                                                                                                                                                                                |
| `status` (in `progressStatus`)                 | R5 status mapped to R4 (`recruiting` → `active`, …); from the site status when the study has none (sample 8)                                                                                                                                        |
| *`overall-study` progress state                | `ResearchStudy.period`; state recoded as `active` with text "Overall study"                                                                                                                                                                         |
| Label `language`                               | R4 `language` extension on the label value                                                                                                                                                                                                          |
| Endpoints (`outcomeMeasure`)                   | One EvidenceVariableReadi entry each, referenced from `outcomeMeasure.reference`                                                                                                                                                                    |
| Contained interventions (EvidenceVariable)     | EvidenceVariableReadi entries; `classifier` → R5 `EvidenceVariable.category`; `handling` (boolean) → `type = dichotomous`                                                                                                                           |
| Eligibility criteria Group                     | GroupReadi entry; nested criteria contained in it; READI extensions for `combinationMethod`, `description`, `characteristic.description`, `characteristic.relativeTime`                                                                             |
| Cohorts (comparison groups)                    | GroupReadi entries, referenced from `arm` with the READI `researchStudy-arm-eligibility` extension; group `code` → `arm.type`                                                                                                                       |
| *Sites (EBM per-site ResearchStudy → Location) | LocationReadi entries referenced from `ResearchStudy.site`                                                                                                                                                                                          |
| Practitioner / PractitionerRole (contacts)     | Kept contained when referenced from `associatedParty.party`; R5 `PractitionerRole.contact` → `practitioner.display` and `telecom`                                                                                                                   |
| Age range `artifact-useContext`                | Kept; months converted to years when low and high use different units                                                                                                                                                                               |

Dropped (no R4 or READI equivalent, or not needed):

- the EBM `researchStudy-studyRegistration` extension (registry periods, duplicating `progressStatus`);
- the per-site ResearchStudy wrappers, i.e. the **status of each site**;
- unreferenced contained resources: Locations that are not sites (sponsor and vendors in sample 9) and one
  PractitionerRole (sample 9);
- the FEvIR `url` of the resources and of the Bundle, `meta.lastUpdated` and the EBM `meta.profile`;
- the summary eligibility Group entry (its text is the description of the eligibility criteria Group).
