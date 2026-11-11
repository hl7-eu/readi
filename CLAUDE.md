# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

The **HL7 Europe FHIR Implementation Guide (IG) for the IHI READI project** — *Building an Inclusive
Clinical Studies Ecosystem to Drive Health Equity in Europe*.

- Canonical: `http://hl7.eu/fhir/ig/readi` — package id `hl7.eu.fhir.readi`
- CI build: https://build.fhir.org/ig/hl7-eu/readi
- GitHub org: `hl7-eu`
- **FHIR version: R4 (4.0.1)**. Status: draft, version 0.1.0, FMM 0 on all artefacts.
- Authored in **FSH** (FHIR Shorthand), compiled with **SUSHI**, published with the **HL7 IG Publisher**.

### Project context

1. **READI data export in FHIR.** READI needs to export clinical-study data (studies, eligibility
   criteria, cohorts, endpoints, sites) in FHIR. This IG defines the profiles and the extensions needed
   for that. Because the data model is richer than R4, many elements are *pre-adopted* from R5/R6 via
   extensions.
2. **Extensions need an IG.** Extensions used by the profiles must be defined in, or imported from, an IG.
   Local extensions live in this repo (`input/fsh/extensions/`); external ones are imported as package
   dependencies (see below). **More IGs are expected to be added here as dependencies** — when that
   happens, update `sushi-config.yaml` (`dependencies`), `.github/workflows/validate-examples.yml`
   (`EXTRA_IGS`), `input/pagecontent/dependencies.md`, and add aliases in `input/fsh/alias-extensions.fsh`.
3. **Collaboration with CDISC: USDM → FHIR.** In parallel, the project transforms **CDISC USDM** (Unified
   Study Definitions Model) into FHIR. The mapping is documented on the page *USDM to FHIR Mapping* and
   drives the `^requirements` of the profile elements (format `USDM: <Class>.<attribute>`).
   <!-- TODO: add further notes about the CDISC collaboration here (contacts, USDM version, decisions). -->

## Repository layout

| Path                                         | Purpose                                                                                                                                                                                 |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `sushi-config.yaml`                          | IG definition: id, canonical, version, dependencies, pages, menu, parameters, resources (examples).                                                                                     |
| `ig.ini`                                     | IG Publisher entry point; uses the local template `#ig-template`.                                                                                                                       |
| `input/fsh/profiles/`                        | Profiles: `ResearchStudyReadi`, `GroupReadi`, `EvidenceVariableReadi`, `LocationReadi`, `BundleReadi`.                                                                                  |
| `input/fsh/extensions/`                      | Local extensions (`group-extensions.fsh`, `researchStudy-extensions.fsh`).                                                                                                              |
| `input/fsh/alias-extensions.fsh`             | Aliases (`$researchStudy-label-r5`, …) for the R5 cross-version extensions.                                                                                                             |
| `input/fsh/aliases.fsh`                      | Other aliases (code systems, etc.).                                                                                                                                                     |
| `input/fsh/rulesSet/`                        | Reusable RuleSets, e.g. `SetFmmAndStatusRule(fmm, status)`.                                                                                                                             |
| `input/fsh/{examples,models,terminologies}/` | Placeholders (`.gitkeep`) for FSH examples, logical models, terminology.                                                                                                                |
| `input/pagecontent/`                         | Narrative pages (Markdown). `usdm2fhir-mapping.md` is the big one (HTML tables).                                                                                                        |
| `input/ignoreWarnings.txt`                   | Suppressed IG Publisher QA messages — each must carry a justifying comment.                                                                                                             |
| `input/examples/`                            | JSON example included **in the IG build** (listed under `resources:` in `sushi-config.yaml`).                                                                                           |
| `examples/`                                  | Test instances for the **daily validation workflow only** — *not* read by the IG Publisher. See `examples/README.md`.                                                                   |
| `scripts/validation/report.py`               | Compares validator output with `baseline.json` and writes the Markdown report.                                                                                                          |
| `sources/`                                   | Source material: `USDM2FHIR-GC-notes.xlsx` (the mapping sheet), `READI-sample-1.json` (FEvIR sample, NCT01444456), `fevir-sample-to-r4.py` (converter), `regenerate-mapping-prompt.md`. |
| `reviews/usdm2fhir-mapping-issues.md`        | Open issues found while mapping (elements with no R4/R5 equivalent, choices to confirm).                                                                                                |
| `ig-template/`                               | Local IG template giving the IG the look of https://ihi-readi.org/ (based on `fhir.base.template`).                                                                                     |
| `_build.sh` / `_build.bat`                   | Standard IG Publisher bootstrap scripts.                                                                                                                                                |
| `runJekyll.bat`                              | Fast rebuild of narrative pages only (Windows; needs a prior full publisher run).                                                                                                       |

Generated and git-ignored: `fsh-generated/`, `output/`, `temp/`, `input-cache/`, `template/`.

## How the modelling works

### R5 elements in an R4 IG
FHIR R4 lacks many elements the data needs. The strategy, in order of preference:

1. Use the **R4 equivalent** when one exists (e.g. R5 `comparisonGroup` → R4 `arm`,
   `recruitment.eligibility` → `enrollment`, `purposeType` → `primaryPurposeType`).
2. Otherwise use the **R5 cross-version extension** from `hl7.fhir.uv.xver-r5.r4#0.1.0`
   (URL pattern `http://hl7.org/fhir/5.0/StructureDefinition/extension-<Resource>.<element>`), aliased in
   `alias-extensions.fsh` and added to the profile with `extension contains`.
3. Otherwise define a **local extension** in `input/fsh/extensions/` (e.g. `GroupCombinationMethod`
   pre-adopts R6 `Group.combinationMethod`; `GroupDescription` pre-adopts R5 `Group.description`).

Every local extension/profile uses `* insert SetFmmAndStatusRule (0, draft)`.

### Traceability to USDM
Elements are annotated with `^requirements = "USDM: <Class>.<attribute>"`. Keep this in sync with
`usdm2fhir-mapping.md`. Rows that could not be mapped are listed as comments at the end of each profile
and in `reviews/usdm2fhir-mapping-issues.md`.

### Profiles
- `ResearchStudyReadi` — the study. Eligibility → `enrollment` (Reference to `GroupReadi`); sites → `site`
  (Reference to `LocationReadi`); many R5 elements through extensions.
- `GroupReadi` — both the overall eligibility group and per-criterion/cohort groups (one profile, with
  extension rules per slice).
- `EvidenceVariableReadi` — endpoints (referenced from the `outcomeMeasure` extension).
- `LocationReadi` — trial sites.
- `BundleReadi` — `collection` Bundle sliced by resource type: 1 ResearchStudy, 0..* Group,
  EvidenceVariable, Location, Practitioner, PractitionerRole.

### The USDM mapping page
`input/pagecontent/usdm2fhir-mapping.md` is **generated from the CSVs**
`sources/USDM2FHIR_r4.csv`, `_r5.csv`, `_r6.csv` with `python3 sources/generate-mapping-page.py` (rules in
`sources/regenerate-mapping-prompt.md`). Do not hand-edit the tables; change the CSVs or the generator and
regenerate. Cells with `to-be-specified` are yellow, or light green when the JSONata returns a hardcoded value. Headings on the page start at `###` (the template renders
the page title as `h2`).

## Common commands

```bash
# Compile FSH only (fast feedback; output in fsh-generated/)
sushi .            # npx --yes fsh-sushi@3.21.0 .   (the version used in CI)

# Full IG build (downloads publisher into input-cache/ on first run; needs Java, Jekyll)
./_build.sh        # or _build.bat on Windows; menu: update the publisher / build

# Narrative pages only, after a full build (Windows)
runJekyll.bat usdm2fhir-mapping

# Regenerate the R4 sample from the FEvIR source
python sources/fevir-sample-to-r4.py sources/READI-sample-1.json input/examples/Bundle-readi-sample-1-r4.json
```

After changing `.fsh` files always run SUSHI and fix errors/warnings before finishing. After changing
profiles, check that `input/examples/` and `examples/` still validate.

## Examples and CI validation

Two example locations, deliberately separate:

- `input/examples/` — published in the IG (declared in `sushi-config.yaml` → `resources`). Currently
  `Bundle-readi-sample-1-r4.json` (study NCT01444456 / eAQUA), also copied in `examples/`.
- `examples/` — non-regression tests. `.github/workflows/validate-examples.yml` runs **daily at 05:00 UTC**
  (only if there was a new commit) and on manual dispatch: SUSHI → HL7 FHIR Java validator (pinned
  `VALIDATOR_VERSION`) → `scripts/validation/report.py` vs `scripts/validation/baseline.json`.
  - New errors not in the baseline fail the run; new warnings are only reported.
  - Files under an `invalid/` folder are negative tests and **must** produce an error.
  - To accept new results: run the workflow with `update_baseline`, download `baseline.json` from the
    artifact and commit it to `scripts/validation/baseline.json`.
  - Examples should declare their profile in `meta.profile`.

## Conventions and gotchas

- Language of the repo: **English** (code, comments, docs).
- Keep versions pinned in the workflow (`VALIDATOR_VERSION`, `SUSHI_VERSION`); bump deliberately and
  refresh the baseline.
- New pages: add the `.md` in `input/pagecontent/` **and** register it in `sushi-config.yaml` (`pages:` and,
  if needed, `menu:`).
- `ignoreWarnings.txt` entries need a justification comment. Known one: duplicate `metadata` anchor ids
  from the Group renderer when a Bundle holds several Groups.
- The IG is a draft: pages carry a `stu-note` warning; keep status `draft` / FMM 0 until agreed otherwise.
- Do not commit generated folders (`fsh-generated/`, `output/`, `temp/`, `input-cache/`).
- Commit/PR flow: work on a branch, open a PR to `master` (the repo uses PRs, e.g. the validation workflow
  came through PR #1).
