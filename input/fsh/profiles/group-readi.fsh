Profile: GroupReadi
Parent: Group
Id: group-readi
Title: "Group (READI)"
Description: "This profile describes the population of a clinical study for the scope of the READI project, defined by its inclusion and exclusion criteria (characteristics)."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI study population"
* . ^definition = "The population of a clinical study, defined by its inclusion and exclusion criteria."
* type = #person
* membership ^short = "definitional | conceptual | enumerated"
* membership ^comment = "Use conceptual (or definitional) when the group only describes the eligibility criteria of the study population; use enumerated when the enrolled participants are listed as members."
* quantity ^short = "Number of participants"
* characteristic ^short = "Inclusion (exclude = false) or exclusion (exclude = true) criterion"
* characteristic.value[x] ^comment = "valueReference is used to point to a (contained) Group representing a nested combination of criteria."
* member.entity only Reference(Patient)
// Group.combinationMethod, Group.characteristic.description and Group.characteristic.relativeTime
// (Group.description is native in FHIR R5)
// are represented by READI extensions (see input/fsh/extensions/group-extensions.fsh).
// ---- modifierExtension[combinationMethod]
* modifierExtension contains GroupCombinationMethod named combinationMethod 0..1
* modifierExtension[combinationMethod] ^short = "How the characteristics are combined (all-of, any-of, ...)"
* modifierExtension[combinationMethod] ^comment = "When absent, all the characteristics apply (all-of), as defined by FHIR R5. Nested criteria (e.g. any-of within an all-of group) are represented by a characteristic whose valueReference points to another (contained) Group."
* modifierExtension[combinationMethod] ^requirements = "USDM: to-be-specified.to-be-specified"
* description ^requirements = "USDM: ExpectedResponse.label"
* characteristic.extension contains
    GroupCharacteristicDescription named description 0..1 and
    GroupCharacteristicRelativeTime named relativeTime 0..*
// ---- characteristic.extension[description]
* characteristic.extension[description] ^short = "Text of the criterion (R6 Group.characteristic.description)"
* characteristic.extension[description] ^requirements = "USDM: EligibilityCriterionItem.to-be-specified; ExpectedResponse.description"
// ---- characteristic.extension[relativeTime]
* characteristic.extension[relativeTime] ^short = "When the criterion applies, relative to a reference event"
* characteristic.extension[relativeTime] ^requirements = "USDM: ExpectedResponse.atTiming"
// ---- characteristic.valueQuantity.extension[cdiscUnit]
* characteristic.valueQuantity.extension contains QuantityCdiscUnit named cdiscUnit 0..1
* characteristic.valueQuantity.extension[cdiscUnit] ^short = "Unit as a CDISC Controlled Terminology concept"
* characteristic.valueRange.low.extension contains QuantityCdiscUnit named cdiscUnit 0..1
* characteristic.valueRange.low.extension[cdiscUnit] ^short = "Unit as a CDISC Controlled Terminology concept"
* characteristic.valueRange.high.extension contains QuantityCdiscUnit named cdiscUnit 0..1
* characteristic.valueRange.high.extension[cdiscUnit] ^short = "Unit as a CDISC Controlled Terminology concept"
// ---- USDM requirements (generated from usdm2fhir-mapping.md; extension requirements are with the extension rules above) ----
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
