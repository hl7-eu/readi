# USDM to FHIR mapping – open issues

Date: 2026-10-18

Source: `sources/USDM2FHIR-GC-notes.xlsx` (sheet "USDM2FHIR map"), as rendered in
`input/pagecontent/usdm2fhir-mapping.md`.

Context: the mapping is used to assign `^requirements` (USDM class.attribute) to the elements of the
R4 profiles (`ResearchStudyReadi`, `GroupReadi`, `EvidenceVariableReadi`). R5 elements are pre-adopted
through the cross-version extensions of `hl7.fhir.uv.xver-r5.r4` 0.1.0 (aliases in
`input/fsh/alias-extensions.fsh`).

## 1. Mapped elements with no R4 element and no R5 cross-version extension

No requirement could be assigned for these rows. Each is listed as a comment at the end of its profile.

| # | FHIR path in the sheet | USDM source | Issue | Possible resolution |
|---|---|---|---|---|
| 1.1 | Group.description | ExpectedResponse.label | R5 element, but `hl7.fhir.uv.xver-r5.r4` 0.1.0 has no extension for it | Use `Group.name`, or a local extension |
| 1.2 | Group.combinationMethod | to-be-specified.to-be-specified | Not an R5 element (later FHIR version) | Local extension, or an extension from a later xver package |
| 1.3 | Group.characteristic.description | EligibilityCriterionItem.to-be-specified; ExpectedResponse.description | Not an R5 element (later FHIR version) | As above, or `characteristic.code.text` |
| 1.4 | Group.characteristic.relativeTime.offsetRange.low/high.value/unit | ExpectedResponse.atTiming | Not an R5 element (later FHIR version) | As above, or `characteristic.period` |
| 1.5 | Group.characteristic.relativeTime.contextCode.coding.code/display/system | to-be-specified.to-be-specified | Not an R5 element (later FHIR version) | As above |
| 1.6 | ResearchStudy.purposeType.coding | InterventionalStudyDesign.intentTypes; InterventionalStudyDesign.subTypes | Not an R5 element | Probably `ResearchStudy.primaryPurposeType` (exists in R4) – fix the sheet |
| 1.7 | ResearchStudy.comparisonGroup.targetNumber | studyCohort.plannedEnrollmentNumber | Not an R5 element | Local extension on `ResearchStudy.arm` |
| 1.8 | ResearchStudy.label.language | StudyTitle.extension | R5 `ResearchStudy.label` has no `language` | Use the `translation` extension on the label value, or drop the row |
| 1.9 | ResearchStudy.identifier.codeableConcept.text | StudyIdentifier.to-be-specified | Not a FHIR element | Probably `ResearchStudy.identifier.type.text` – fix the sheet |

## 2. Mapping choices to be confirmed

| # | FHIR path in the sheet | Applied in the profile | Note |
|---|---|---|---|
| 2.1 | ResearchStudy.objective.outcomeMeasure.endpoint | `extension[outcomeMeasure].extension[reference]` | In R5 `outcomeMeasure` is a ResearchStudy-level element (not under `objective`) and has no `endpoint`; the link to the objective is lost |
| 2.2 | ResearchStudy.objective.outcomeMeasure.endpoint.display | `extension[outcomeMeasure].extension[reference].valueReference.display` | As above |
| 2.3 | ResearchStudy.objective.outcomeMeasure.type.coding | `extension[outcomeMeasure].extension[type].valueCodeableConcept.coding` | As above |
| 2.4 | ResearchStudy.comparisonGroup.name / description | `arm.name` / `arm.description` | R4 equivalent, as stated in the xver R5-to-R4 ConceptMap |
| 2.5 | ResearchStudy.recruitment.eligibility | `enrollment` | R4 equivalent, as stated in the xver R5-to-R4 ConceptMap |
| 2.6 | EvidenceVariable.classifier | `extension[classifier]` (R5 `EvidenceVariable.category`) | `classifier` is not in R4 or R5; the R5 `category` extension carries a name and a value rather than a single code |
| 2.7 | Group-all.* | `GroupReadi` | Both the overall eligibility group and the per-criterion groups are R4 `Group`; a single profile is used |

## 3. Gaps in the mapping sheet

| # | Issue |
|---|---|
| 3.1 | 17 rows have no USDM class (and attribute); in the page they are rendered as `to-be-specified.to-be-specified` and grouped under the class of the previous row, which is not always meaningful (e.g. `Group-all.id` under StudySite, `EvidenceVariable.*` under BiomedicalConcept) |
| 3.2 | All EvidenceVariable rows (id, name, title, description, classifier) have no USDM class/attribute, although the JSONata expressions show they come from `BiomedicalConcept` (id, name, label, description) |
| 3.3 | Location rows (id, name, type, address.country) have no profile yet |
| 3.4 | `BiomedicalConcept.code` is mapped only to `Group.characteristic.code.coding`; consider also `EvidenceVariable.characteristic.definitionCodeableConcept` |
| 3.5 | Nothing references `EvidenceVariableReadi` from `ResearchStudyReadi` (R4 has no `outcomeMeasure`; see 2.1) |
| 3.6 | Inconsistent class names: `studyCohort` vs `StudyArm`, `PlannedSex` vs `plannedAge`, `extension studyProgressStatus` |
| 3.7 | Non-atomic attribute: `startDate, endDate` |
| 3.8 | Duplicate rows (e.g. `StudyTitle.type` → `ResearchStudy.label.type.coding` appears twice) |
