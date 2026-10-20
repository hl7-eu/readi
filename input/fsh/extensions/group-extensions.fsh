Extension: GroupCombinationMethod
Id: group-combinationMethod
Title: "Group Combination Method"
Description: "How the characteristics of the Group are combined (e.g. all of, any of) to determine membership. It pre-adopts the FHIR R6 Group.combinationMethod element, not available in FHIR R4 or R5."
Context: Group
* insert SetFmmAndStatusRule (0, draft)
* . ^isModifier = true
* . ^isModifierReason = "In FHIR R4 all the characteristics of a Group must be true for an entity to be a member of the group; a combination method other than all-of (e.g. any-of) changes this meaning."
* value[x] only code
* valueCode 1..
* valueCode from http://hl7.org/fhir/uv/xver/ValueSet/R5-characteristic-combination-for-R4 (required)
  * ^short = "all-of | any-of | at-least | at-most | statistical | net-effect | dataset"
* valueCode ^requirements = "USDM: to-be-specified.to-be-specified"

Extension: GroupDescription
Id: group-description
Title: "Group Description"
Description: "A natural language description of the Group. It pre-adopts the FHIR R5 Group.description element, not covered by the R5 cross-version extensions for R4."
Context: Group
* insert SetFmmAndStatusRule (0, draft)
* value[x] only markdown
* valueMarkdown 1..
* valueMarkdown ^requirements = "USDM: ExpectedResponse.label"

Extension: GroupCharacteristicDescription
Id: group-characteristic-description
Title: "Group Characteristic Description"
Description: "A natural language description of a Group characteristic (e.g. the text of an eligibility criterion). It pre-adopts the FHIR R6 Group.characteristic.description element."
Context: Group.characteristic
* insert SetFmmAndStatusRule (0, draft)
* value[x] only markdown
* valueMarkdown 1..
* valueMarkdown ^requirements = "USDM: EligibilityCriterionItem.to-be-specified; ExpectedResponse.description"

Extension: GroupCharacteristicRelativeTime
Id: group-characteristic-relativeTime
Title: "Group Characteristic Relative Time"
Description: "The time when the characteristic applies, relative to a reference event (e.g. at enrollment in the study)."
Context: Group.characteristic
* insert SetFmmAndStatusRule (0, draft)
* extension contains
    contextCode 1..1 and
    offsetRange 0..1
* extension[contextCode] ^short = "The reference event (e.g. enrollment in clinical trial)"
* extension[contextCode].value[x] only CodeableConcept
* extension[contextCode].valueCodeableConcept ^requirements = "USDM: to-be-specified.to-be-specified"
* extension[offsetRange] ^short = "Offset from the reference event"
* extension[offsetRange].value[x] only Range
* extension[offsetRange].valueRange ^requirements = "USDM: ExpectedResponse.atTiming"
