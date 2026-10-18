# USDM to FHIR mapping

## Indication

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| Indication.label | ResearchStudy.condition.text |
| Indication.codes | ResearchStudy.condition.coding |

## StudyIdentifier

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudyIdentifier.text | ResearchStudy.identifier.value |
| StudyIdentifier.to-be-specified | ResearchStudy.identifier.codeableConcept.text |
| StudyIdentifier.scope | ResearchStudy.identifier.assigner.display |
| StudyIdentifier.to-be-specified | ResearchStudy.identifier.system |
| to-be-specified.to-be-specified | ResearchStudy.identifier.use |

## StudyTitle

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudyTitle.text | ResearchStudy.label.value |
| StudyTitle.text | ResearchStudy.title |
| StudyTitle.type | ResearchStudy.label.type.coding |
| StudyTitle.extension | ResearchStudy.label.value |
| StudyTitle.type | ResearchStudy.label.type.coding |
| StudyTitle.extension | ResearchStudy.label.language |

## PopulationDefinition

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| PopulationDefinition.plannedAge | ResearchStudy.classifier.text |
| PopulationDefinition.plannedAge | ResearchStudy.classifier.text |
| PopulationDefinition.PlannedSex | ResearchStudy.classifier |

## StudyDesignPopulation

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudyDesignPopulation.PlannedSex | ResearchStudy.classifier |
| StudyDesignPopulation.includesHealthySubjects | ResearchStudy.classifier |
| StudyDesignPopulation.includesHealthySubjects | ResearchStudy.classifier |
| StudyDesignPopulation.plannedAge | ResearchStudy.classifier |
| StudyDesignPopulation.plannedAge | ResearchStudy.classifier |
| StudyDesignPopulation.plannedAge | ResearchStudy.classifier |

## Objective

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| Objective.text | ResearchStudy.objective.name |
| Objective.type | ResearchStudy.objective.type.coding.code |
| Objective.level | ResearchStudy.objective.type.coding.display |
| to-be-specified.to-be-specified | ResearchStudy.objective.type.coding.system |
| Objective.level | ResearchStudy.objective.type.coding.code |
| Objective.level | ResearchStudy.objective.type.coding.display |
| Objective.level | ResearchStudy.objective.type.coding.code |
| Objective.level | ResearchStudy.objective.type.coding.display |

## Endpoint

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| Endpoint.text | ResearchStudy.objective.outcomeMeasure.endpoint |
| Endpoint.to-be-specified | ResearchStudy.objective.outcomeMeasure.endpoint.display |
| Endpoint.level | ResearchStudy.objective.outcomeMeasure.type.coding |

## InterventionalStudyDesign

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| InterventionalStudyDesign.intentTypes | ResearchStudy.purposeType.coding |
| InterventionalStudyDesign.subTypes | ResearchStudy.purposeType.coding |

## StudyDesign

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudyDesign.studyPhase | ResearchStudy.phase.coding |

## extension studyProgressStatus

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| extension studyProgressStatus.state | ResearchStudy.progressStatus.state.coding |
| extension studyProgressStatus.isActual | ResearchStudy.progressStatus.actual |
| extension studyProgressStatus.startDate, endDate | ResearchStudy.progressStatus.period |

## StudyArm

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudyArm.label | ResearchStudy.comparisonGroup.name |
| StudyArm.description | ResearchStudy.comparisonGroup.description |

## studyCohort

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| studyCohort.label | ResearchStudy.comparisonGroup.name |
| studyCohort.description | ResearchStudy.comparisonGroup.description |
| studyCohort.plannedEnrollmentNumber | ResearchStudy.comparisonGroup.targetNumber |

## StudySite

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| StudySite.id | ResearchStudy.site |
| to-be-specified.to-be-specified | Location.id |
| StudySite.label | Location.name |
| to-be-specified.to-be-specified | Location.type |
| StudySite.country | Location.address.country |
| to-be-specified.to-be-specified | ResearchStudy.recruitment.eligibility |
| to-be-specified.to-be-specified | Group-all.id |
| to-be-specified.to-be-specified | Group-all.combinationMethod |

## EligibilityCriterionItem

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| EligibilityCriterionItem.to-be-specified | Group-all.characteristic.description |
| EligibilityCriterionItem.to-be-specified | Group-all.characteristic.code.text |

## EligibilityCriterion

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| EligibilityCriterion.category | Group-all.characteristic.exclude |
| to-be-specified.to-be-specified | Group-all.characteristic.valueReference.reference |
| EligibilityCriterion.category | Group.characteristic.exclude |

## ExpectedResponse

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| ExpectedResponse.atTiming | Group-all.characteristic.valueReference.type |
| ExpectedResponse.id | Group.id |
| to-be-specified.to-be-specified | Group.combinationMethod |
| ExpectedResponse.label | Group.description |
| ExpectedResponse.value | Group.characteristic.valueRange.low.value |
| ExpectedResponse.value | Group.characteristic.valueRange.low.unit |
| ExpectedResponse.value | Group.characteristic.valueRange.high.value |
| ExpectedResponse.value | Group.characteristic.valueRange.high.unit |
| ExpectedResponse.description | Group.characteristic.description |
| ExpectedResponse.codes | Group.characteristic.valueCodeableConcept.coding.code |
| ExpectedResponse.codes | Group.characteristic.valueCodeableConcept.coding.display |
| ExpectedResponse.codes | Group.characteristic.valueCodeableConcept.coding.system |
| ExpectedResponse.value | Group.characteristic.valueQuantity.value |
| ExpectedResponse.value | Group.characteristic.valueQuantity.unit |
| ExpectedResponse.atTiming | Group.characteristic.relativeTime.offsetRange.low.value |
| ExpectedResponse.atTiming | Group.characteristic.relativeTime.offsetRange.low.unit |
| ExpectedResponse.atTiming | Group.characteristic.relativeTime.offsetRange.high.value |
| ExpectedResponse.atTiming | Group.characteristic.relativeTime.offsetRange.high.unit |
| to-be-specified.to-be-specified | Group.characteristic.relativeTime.contextCode.coding.code |
| to-be-specified.to-be-specified | Group.characteristic.relativeTime.contextCode.coding.display |
| to-be-specified.to-be-specified | Group.characteristic.relativeTime.contextCode.coding.system |

## BiomedicalConcept

| USDM class.attribute | FHIR resourceType.path |
|---|---|
| BiomedicalConcept.code | Group.characteristic.code.coding |
| to-be-specified.to-be-specified | EvidenceVariable.id |
| to-be-specified.to-be-specified | EvidenceVariable.name |
| to-be-specified.to-be-specified | EvidenceVariable.title |
| to-be-specified.to-be-specified | EvidenceVariable.description |
| to-be-specified.to-be-specified | EvidenceVariable.classifier |
