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
* condition ^short = "Condition(s) being studied"
* recruitment.eligibility only Reference(GroupReadi)
  * ^short = "Inclusion and exclusion criteria (study population)"
* site only Reference(LocationReadi)
  * ^short = "Facility where the study is conducted"
* label ^short = "Additional names for the study"
* classifier ^short = "Classification for the study"
* progressStatus ^short = "Status of study with time for that status"
* outcomeMeasure ^short = "A variable measured during the study"
* outcomeMeasure.reference only Reference(EvidenceVariableReadi)
* comparisonGroup.observedGroup only Reference(GroupReadi)
// ---- comparisonGroup.extension[targetNumber]
* comparisonGroup.extension contains ResearchStudyArmTargetNumber named targetNumber 0..1
* comparisonGroup.extension[targetNumber] ^short = "Estimated number of participants to be enrolled in the comparison group (R6 ResearchStudy.comparisonGroup.targetNumber)"
// ---- comparisonGroup.extension[eligibility]
* comparisonGroup.extension contains ResearchStudyArmEligibility named eligibility 0..1
* comparisonGroup.extension[eligibility] ^short = "Group with the eligibility criteria of the comparison group (R6 ResearchStudy.comparisonGroup.eligibility)"
// ---- USDM requirements (generated from usdm2fhir-mapping.md) ----
* condition.text ^requirements = "USDM: Indication.label"
* condition.coding ^requirements = "USDM: Indication.codes"
* identifier.value ^requirements = "USDM: StudyIdentifier.text"
* identifier.assigner.display ^requirements = "USDM: StudyIdentifier.scope"
* identifier.system ^requirements = "USDM: StudyIdentifier.to-be-specified"
* identifier.use ^requirements = "USDM: to-be-specified.to-be-specified"
* title ^requirements = "USDM: StudyTitle.text"
* label.value ^requirements = "USDM: StudyTitle.text; StudyTitle.extension"
* label.type.coding ^requirements = "USDM: StudyTitle.type"
* classifier ^requirements = "USDM: PopulationDefinition.PlannedSex; StudyDesignPopulation.PlannedSex; StudyDesignPopulation.includesHealthySubjects; StudyDesignPopulation.plannedAge"
* classifier.text ^requirements = "USDM: PopulationDefinition.plannedAge"
* progressStatus.state.coding ^requirements = "USDM: extension studyProgressStatus.state"
* progressStatus.actual ^requirements = "USDM: extension studyProgressStatus.isActual"
* progressStatus.period ^requirements = "USDM: extension studyProgressStatus.startDate, endDate"
* outcomeMeasure.type.coding ^requirements = "USDM: Endpoint.level"
* outcomeMeasure.reference ^requirements = "USDM: Endpoint.text"
* outcomeMeasure.reference.display ^requirements = "USDM: Endpoint.to-be-specified"
* objective.name ^requirements = "USDM: Objective.text"
* objective.type.coding.code ^requirements = "USDM: Objective.type; Objective.level"
* objective.type.coding.display ^requirements = "USDM: Objective.level"
* objective.type.coding.system ^requirements = "USDM: to-be-specified.to-be-specified"
* phase.coding ^requirements = "USDM: StudyDesign.studyPhase"
* comparisonGroup.name ^requirements = "USDM: StudyArm.label; studyCohort.label"
* comparisonGroup.description ^requirements = "USDM: StudyArm.description; studyCohort.description"
* site ^requirements = "USDM: StudySite.id"
* recruitment.eligibility ^requirements = "USDM: to-be-specified.to-be-specified"
* recruitment.targetNumber ^requirements = "USDM: StudyDesignPopulation.plannedEnrollmentNumber"
// Mapped elements without an R5 element (no requirement assigned):
// ResearchStudy.identifier.codeableConcept.text <- USDM: StudyIdentifier.to-be-specified (not a FHIR element (identifier.type.text?))
// ResearchStudy.label.language <- USDM: StudyTitle.extension (R5 ResearchStudy.label has no language)
// ResearchStudy.purposeType.coding <- USDM: InterventionalStudyDesign.intentTypes; InterventionalStudyDesign.subTypes (R6 element; R5 has primaryPurposeType)
