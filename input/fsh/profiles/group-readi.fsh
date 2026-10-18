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
// Mapped elements without an R4 element or R5 cross-version extension (no requirement assigned):
// Group.combinationMethod <- USDM: to-be-specified.to-be-specified (not an R5 element)
// Group.characteristic.description <- USDM: EligibilityCriterionItem.to-be-specified; ExpectedResponse.description (not an R5 element)
// Group.description <- USDM: ExpectedResponse.label (R5 element, no extension in hl7.fhir.uv.xver-r5.r4 0.1.0)
// Group.characteristic.relativeTime.offsetRange.low.value <- USDM: ExpectedResponse.atTiming (not an R5 element)
// Group.characteristic.relativeTime.offsetRange.low.unit <- USDM: ExpectedResponse.atTiming (not an R5 element)
// Group.characteristic.relativeTime.offsetRange.high.value <- USDM: ExpectedResponse.atTiming (not an R5 element)
// Group.characteristic.relativeTime.offsetRange.high.unit <- USDM: ExpectedResponse.atTiming (not an R5 element)
// Group.characteristic.relativeTime.contextCode.coding.code <- USDM: to-be-specified.to-be-specified (not an R5 element)
// Group.characteristic.relativeTime.contextCode.coding.display <- USDM: to-be-specified.to-be-specified (not an R5 element)
// Group.characteristic.relativeTime.contextCode.coding.system <- USDM: to-be-specified.to-be-specified (not an R5 element)
