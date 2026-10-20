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
* member.entity only Reference(Patient)
* modifierExtension contains GroupCombinationMethod named combinationMethod 0..1
* modifierExtension[combinationMethod] ^short = "How the characteristics are combined (all-of, any-of, ...)"
* modifierExtension[combinationMethod] ^comment = "When absent, all the characteristics apply (all-of), as defined by FHIR R4. Nested criteria (e.g. any-of within an all-of group) are represented by a characteristic whose valueReference points to another (contained) Group."
* extension contains GroupDescription named description 0..1
* extension[description] ^short = "Natural language description of the group (R5 Group.description)"
* characteristic.extension contains
    GroupCharacteristicDescription named description 0..1 and
    GroupCharacteristicRelativeTime named relativeTime 0..*
* characteristic.extension[description] ^short = "Text of the criterion (R6 Group.characteristic.description)"
* characteristic.extension[relativeTime] ^short = "When the criterion applies, relative to a reference event"
* characteristic.value[x] ^comment = "valueReference is used to point to a (contained) Group representing a nested combination of criteria."
// ---- USDM requirements (generated from usdm2fhir-mapping.md) ----
* id ^requirements = "USDM: to-be-specified.to-be-specified; ExpectedResponse.id"
* characteristic.code.text ^requirements = "USDM: EligibilityCriterionItem.to-be-specified"
* characteristic.exclude ^requirements = "USDM: EligibilityCriterion.category"
* characteristic.valueReference.reference ^requirements = "USDM: to-be-specified.to-be-specified"
* characteristic.valueReference.type ^requirements = "USDM: ExpectedResponse.atTiming"
* characteristic.valueRange.low.value ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange.low.unit ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange.high.value ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueRange.high.unit ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueCodeableConcept.coding.code ^requirements = "USDM: ExpectedResponse.codes"
* characteristic.valueCodeableConcept.coding.display ^requirements = "USDM: ExpectedResponse.codes"
* characteristic.valueCodeableConcept.coding.system ^requirements = "USDM: ExpectedResponse.codes"
* characteristic.valueQuantity.value ^requirements = "USDM: ExpectedResponse.value"
* characteristic.valueQuantity.unit ^requirements = "USDM: ExpectedResponse.value"
* characteristic.code.coding ^requirements = "USDM: BiomedicalConcept.code"
* modifierExtension[combinationMethod] ^requirements = "USDM: to-be-specified.to-be-specified"
* extension[description] ^requirements = "USDM: ExpectedResponse.label"
* characteristic.extension[description] ^requirements = "USDM: EligibilityCriterionItem.to-be-specified; ExpectedResponse.description"
* characteristic.extension[relativeTime] ^requirements = "USDM: ExpectedResponse.atTiming"
// Group.combinationMethod, Group.description, Group.characteristic.description and Group.characteristic.relativeTime
// are represented by READI extensions (see input/fsh/extensions/group-extensions.fsh).
