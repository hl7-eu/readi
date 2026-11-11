Profile: BundleReadi
Parent: Bundle
Id: bundle-readi
Title: "Bundle (READI)"
Description: "This profile describes a collection of the resources that describe a clinical study for the scope of the READI project: the study, its eligibility criteria and cohorts, its endpoints, its sites and the people referenced as contacts."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI clinical study collection"
* . ^definition = "A collection of the resources describing a clinical study (e.g. a clinical trial) for the scope of the READI project."
* type = #collection
* entry 1..
* entry ^slicing.discriminator.type = #type
* entry ^slicing.discriminator.path = "resource"
* entry ^slicing.rules = #open
* entry ^slicing.description = "Slicing based on the type of the entry resource"
* entry contains
    researchStudy 1..1 and
    group 0..* and
    evidenceVariable 0..* and
    location 0..* and
    practitioner 0..* and
    practitionerRole 0..*
* entry[researchStudy] ^short = "The clinical study"
* entry[researchStudy].resource 1..
* entry[researchStudy].resource only ResearchStudyReadi
* entry[group] ^short = "Eligibility criteria, cohorts and expected responses"
* entry[group].resource 1..
* entry[group].resource only GroupReadi
* entry[evidenceVariable] ^short = "Endpoints (outcome measures) of the study"
* entry[evidenceVariable].resource 1..
* entry[evidenceVariable].resource only EvidenceVariableReadi
* entry[location] ^short = "Sites where the study is conducted"
* entry[location].resource 1..
* entry[location].resource only LocationReadi
* entry[practitioner] ^short = "People referenced by the study (e.g. central contacts), via ResearchStudy.associatedParty"
* entry[practitioner].resource 1..
* entry[practitioner].resource only Practitioner
* entry[practitionerRole] ^short = "Roles of the people referenced by the study, via ResearchStudy.associatedParty"
* entry[practitionerRole].resource 1..
* entry[practitionerRole].resource only PractitionerRole
