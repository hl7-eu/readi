Profile: EvidenceVariableReadi
Parent: EvidenceVariable
Id: evidenceVariable-readi
Title: "EvidenceVariable (READI)"
Description: "This profile describes a variable measured in a clinical study (e.g. the assessment related to a study endpoint) for the scope of the READI project. It is derived from the USDM BiomedicalConcept referenced by the endpoint."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI study variable"
* . ^definition = "A variable measured in a clinical study (e.g. the assessment related to a study endpoint), derived from a USDM BiomedicalConcept."
* name 1..
  * ^short = "Name of the variable (USDM BiomedicalConcept.name)"
* title ^short = "Label of the variable (USDM BiomedicalConcept.label)"
* description ^short = "Description of the variable (USDM BiomedicalConcept.description)"
* characteristic ^short = "What defines the variable (e.g. the USDM BiomedicalConcept code)"
* category ^short = "Classification of the variable (e.g. measurement)"
// ---- USDM requirements (generated from usdm2fhir-mapping.md) ----
* category ^requirements = "USDM: to-be-specified.to-be-specified"
* id ^requirements = "USDM: to-be-specified.to-be-specified"
* name ^requirements = "USDM: to-be-specified.to-be-specified"
* title ^requirements = "USDM: to-be-specified.to-be-specified"
* description ^requirements = "USDM: to-be-specified.to-be-specified"
