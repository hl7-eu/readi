# READI test examples

FHIR instances (`.json` / `.xml`) used for the daily non-regression validation
([.github/workflows/validate-examples.yml](../.github/workflows/validate-examples.yml)).
They are **not** part of the IG build: the IG Publisher does not read this folder.

## Conventions

- Put examples in any sub-folder, e.g. `examples/studies/…`, `examples/bundles/…`.
- Every instance should declare the READI profile it claims in `meta.profile`.
- Examples under a folder named `invalid/` (at any depth) are **negative tests**:
  they must produce at least one error. The run fails if one of them becomes valid.
- All other examples are **positive tests**.

## How the check works

Every day at 05:00 UTC, if something was pushed since the last run, GitHub Actions:

1. runs SUSHI to generate the current profiles (`fsh-generated/resources`);
2. validates every file here with the HL7 FHIR Java validator (pinned version);
3. compares the issues with [scripts/validation/baseline.json](../scripts/validation/baseline.json)
   and writes a report to the run summary (and the `validation-report-*` artifact,
   together with the validator's HTML output).

The run **fails** (and GitHub notifies by e-mail) when an error appears that is not
in the baseline, or when a negative example stops failing. New warnings are
reported but do not fail the run.

Issues are matched on severity + validator message id + FHIRPath location, so a
rewording of a message by a newer validator is not counted as a regression.

## Accepting the current results (refreshing the baseline)

After adding examples, or once a change in the results is understood and accepted:

1. Actions → *Validate examples* → *Run workflow* with **update_baseline** ticked;
2. download `baseline.json` from the run's artifact;
3. commit it as `scripts/validation/baseline.json`.

You can run the workflow manually at any time (Actions → *Validate examples* →
*Run workflow*).
