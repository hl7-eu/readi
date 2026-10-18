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
* extension contains
    $researchStudy-label-r5 named label 0..* and
    $researchStudy-classifier-r5 named classifier 0..* and
    $researchStudy-progressStatus-r5 named progressStatus 0..* and
    $researchStudy-outcomeMeasure-r5 named outcomeMeasure 0..*
* extension[label] ^short = "Additional names for the study (R5 ResearchStudy.label)"
* extension[classifier] ^short = "Classification for the study (R5 ResearchStudy.classifier)"
* extension[progressStatus] ^short = "Status of study with time for that status (R5 ResearchStudy.progressStatus)"
* extension[outcomeMeasure] ^short = "A variable measured during the study (R5 ResearchStudy.outcomeMeasure)"
// ---- USDM requirements (generated from usdm2fhir-mapping.md) ----
* condition.text ^requirements = "USDM: Indication.label"
* condition.coding ^requirements = "USDM: Indication.codes"
* identifier.value ^requirements = "USDM: StudyIdentifier.text"
* identifier.assigner.display ^requirements = "USDM: StudyIdentifier.scope"
* identifier.system ^requirements = "USDM: StudyIdentifier.to-be-specified"
* identifier.use ^requirements = "USDM: to-be-specified.to-be-specified"
* extension[label].extension[value] ^requirements = "USDM: StudyTitle.text; StudyTitle.extension"
* title ^requirements = "USDM: StudyTitle.text"
* extension[label].extension[type].valueCodeableConcept.coding ^requirements = "USDM: StudyTitle.type"
* extension[classifier].valueCodeableConcept.text ^requirements = "USDM: PopulationDefinition.plannedAge"
* extension[classifier] ^requirements = "USDM: PopulationDefinition.PlannedSex; StudyDesignPopulation.PlannedSex; StudyDesignPopulation.includesHealthySubjects; StudyDesignPopulation.plannedAge"
* objective.name ^requirements = "USDM: Objective.text"
* objective.type.coding.code ^requirements = "USDM: Objective.type; Objective.level"
* objective.type.coding.display ^requirements = "USDM: Objective.level"
* objective.type.coding.system ^requirements = "USDM: to-be-specified.to-be-specified"
* extension[outcomeMeasure].extension[reference] ^requirements = "USDM: Endpoint.text"
* extension[outcomeMeasure].extension[reference].valueReference.display ^requirements = "USDM: Endpoint.to-be-specified"
* extension[outcomeMeasure].extension[type].valueCodeableConcept.coding ^requirements = "USDM: Endpoint.level"
* phase.coding ^requirements = "USDM: StudyDesign.studyPhase"
* extension[progressStatus].extension[state].valueCodeableConcept.coding ^requirements = "USDM: extension studyProgressStatus.state"
* extension[progressStatus].extension[actual] ^requirements = "USDM: extension studyProgressStatus.isActual"
* extension[progressStatus].extension[period] ^requirements = "USDM: extension studyProgressStatus.startDate, endDate"
* arm.name ^requirements = "USDM: StudyArm.label; studyCohort.label"
* arm.description ^requirements = "USDM: StudyArm.description; studyCohort.description"
* site ^requirements = "USDM: StudySite.id"
* enrollment ^requirements = "USDM: to-be-specified.to-be-specified"
// Mapped elements without an R4 element or R5 cross-version extension (no requirement assigned):
// ResearchStudy.identifier.codeableConcept.text <- USDM: StudyIdentifier.to-be-specified (not a FHIR element (identifier.type.text?))
// ResearchStudy.label.language <- USDM: StudyTitle.extension (R5 ResearchStudy.label has no language)
// ResearchStudy.purposeType.coding <- USDM: InterventionalStudyDesign.intentTypes; InterventionalStudyDesign.subTypes (not an R5 element (primaryPurposeType?))
// ResearchStudy.comparisonGroup.targetNumber <- USDM: studyCohort.plannedEnrollmentNumber (not an R5 element)
