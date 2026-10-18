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
