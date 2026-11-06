Profile: GroupReadi
Parent: Group
Id: group-readi
Title: "Group (READI)"
Description: "This profile describes the population of a clinical study for the scope of the READI project, defined by its inclusion and exclusion criteria (characteristics)."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI study population"
* . ^definition = "The population of a clinical study, defined by its inclusion and exclusion criteria."
* type = #person
* actual ^short = "Descriptive (false) or actual (true) group"
* actual ^comment = "Set to false when the group only describes the eligibility criteria of the study population; set to true when the enrolled participants are listed as members."
* quantity ^short = "Number of participants"
* characteristic ^short = "Inclusion (exclude = false) or exclusion (exclude = true) criterion"
* characteristic.value[x] ^comment = "valueReference is used to point to a (contained) Group representing a nested combination of criteria."
* member.entity only Reference(Patient)
// Group.combinationMethod, Group.description, Group.characteristic.description and Group.characteristic.relativeTime
// are represented by READI extensions (see input/fsh/extensions/group-extensions.fsh).
// ---- modifierExtension[combinationMethod]
* modifierExtension contains GroupCombinationMethod named combinationMethod 0..1
* modifierExtension[combinationMethod] ^short = "How the characteristics are combined (all-of, any-of, ...)"
* modifierExtension[combinationMethod] ^comment = "When absent, all the characteristics apply (all-of), as defined by FHIR R4. Nested criteria (e.g. any-of within an all-of group) are represented by a characteristic whose valueReference points to another (contained) Group."
// ---- extension[description]
* extension contains GroupDescription named description 0..1
* extension[description] ^short = "Natural language description of the group (R5 Group.description)"
* characteristic.extension contains
    GroupCharacteristicDescription named description 0..1 and
    GroupCharacteristicRelativeTime named relativeTime 0..*
// ---- characteristic.extension[description]
* characteristic.extension[description] ^short = "Text of the criterion (R6 Group.characteristic.description)"
// ---- characteristic.extension[relativeTime]
* characteristic.extension[relativeTime] ^short = "When the criterion applies, relative to a reference event"
// ---- USDM requirements: every Group element used as a target in the R4 mapping (sources/USDM2FHIR_r4.csv) ----
// R5/R6 elements are given on the READI extension that represents them.
* id ^requirements = "USDM: StudyArm.id; to-be-specified.to-be-specified; ExpectedResponse.id"
* name ^requirements = "USDM: StudyArm.label"
* actual ^requirements = "USDM: to-be-specified.to-be-specified"
* code.text ^requirements = "USDM: StudyArm.type"
* extension[description] ^requirements = "USDM: StudyArm.description; ExpectedResponse.label"
* modifierExtension[combinationMethod] ^requirements = "USDM: to-be-specified.to-be-specified"
* characteristic.extension[description] ^requirements = "USDM: EligibilityCriterionItem.to-be-specified; ExpectedResponse.description"
* characteristic.code.text ^requirements = "USDM: to-be-specified.to-be-specified"
* characteristic.code.coding ^requirements = "USDM: BiomedicalConcept.code"
* characteristic.exclude ^requirements = "USDM: EligibilityCriterion.category; ExpectedResponse.category"
* characteristic.valueCodeableConcept.text ^requirements = "USDM: EligibilityCriterionItem.text"
* characteristic.valueCodeableConcept.coding ^requirements = "USDM: ExpectedResponse.codes"
* characteristic.valueQuantity ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueQuantity.code ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange.low.code ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange.high.code ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueReference.reference ^requirements = "USDM: Extension.to-be-specified; ExpResponseNode.childArray"
* characteristic.valueReference.type ^requirements = "USDM: ExpectedResponse.atTiming; ExpResponseNode.childArray"
// offsetRange (USDM: ExpectedResponse.atTiming) and contextCode (USDM: to-be-specified.to-be-specified;
// ExpectedResponse.atTiming): requirements set per sub-extension in GroupCharacteristicRelativeTime
* characteristic.extension[relativeTime] ^requirements = "USDM: ExpectedResponse.atTiming; to-be-specified.to-be-specified"
// Rows of the R4 mapping with no element in R4 Group or in GroupReadi:
// - status (USDM: to-be-specified.to-be-specified): not in R4 Group
// - characteristic.valueRange.low/high.isInclusive (USDM: ExpectedResponse.value): not in FHIR; the flag is removed by fhir_version.py
