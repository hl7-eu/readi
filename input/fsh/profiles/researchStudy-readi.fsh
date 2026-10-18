Profile: ResearchStudyReadi
Parent: ResearchStudy
Id: researchStudy-readi
Title: "ResearchStudy (READI)"
Description: "This profile describes a clinical study (e.g. a clinical trial) for the scope of the READI project."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI clinical study"
* . ^definition = "A clinical study (e.g. a clinical trial) described for the scope of the READI project."
* identifier 1..
  * ^short = "Study identifier (e.g. EU CT number, NCT number)"
* title 1..
  * ^short = "Study title"
* focus ^short = "Drug, device, condition or other focus of the study"
* condition ^short = "Condition(s) being studied"
* enrollment only Reference(GroupReadi)
  * ^short = "Inclusion and exclusion criteria (study population)"
* site ^short = "Facility where the study is conducted"
