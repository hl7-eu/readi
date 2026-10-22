<div class="stu-note" markdown="1">
This mapping is a work in progress: it has not been validated yet and may change at any time.
</div>

### Indication

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Condition label</td><td>Indication.label</td><td colspan="3">ResearchStudy.condition.text</td><td></td></tr>
<tr><td>Condition code</td><td>Indication.codes</td><td colspan="3">ResearchStudy.condition.coding</td><td></td></tr>
</tbody>
</table>

### StudyIdentifier

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Identifier</td><td>StudyIdentifier.text</td><td colspan="3">ResearchStudy.identifier.value</td><td></td></tr>
<tr><td style="background-color: #ffff99;">Study Identifier FHIR type</td><td style="background-color: #ffff99;">StudyIdentifier.to-be-specified</td><td colspan="3" style="background-color: #ffff99;">ResearchStudy.identifier.codeableConcept.text</td><td style="background-color: #ffff99;">ResearchStudy.identifier has not a codeableConcept</td></tr>
<tr><td>Study Identifier Organization</td><td>StudyIdentifier.scope</td><td colspan="3">ResearchStudy.identifier.assigner.display</td><td></td></tr>
<tr><td>NCT identifier system</td><td style="background-color: #ffff99;">StudyIdentifier.to-be-specified</td><td colspan="3">ResearchStudy.identifier.system</td><td></td></tr>
<tr><td>Identifier use</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">ResearchStudy.identifier.use</td><td></td></tr>
</tbody>
</table>

### StudyTitle

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study titles</td><td>StudyTitle.text</td><td>ResearchStudy.extension:label.extension:value.valueString</td><td colspan="2">ResearchStudy.label.value</td><td></td></tr>
<tr><td>Official title</td><td>StudyTitle.text</td><td colspan="3">ResearchStudy.title</td><td></td></tr>
<tr><td>Title type</td><td>StudyTitle.type</td><td>ResearchStudy.extension:label.extension:type.valueCodeableConcept.coding</td><td colspan="2">ResearchStudy.label.type.coding</td><td></td></tr>
<tr><td>Translated titles</td><td>StudyTitle.extension</td><td>ResearchStudy.extension:label.extension:value.valueString</td><td colspan="2">ResearchStudy.label.value</td><td></td></tr>
<tr><td>Translated title type</td><td>StudyTitle.type</td><td>ResearchStudy.extension:label.extension:type.valueCodeableConcept.coding</td><td colspan="2">ResearchStudy.label.type.coding</td><td></td></tr>
<tr><td>Translated title language</td><td>StudyTitle.extension</td><td colspan="2" style="background-color: #ffff99;">—</td><td>ResearchStudy.label.language</td><td>R5 preadoption ?</td></tr>
</tbody>
</table>

### PopulationDefinition

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td style="background-color: #ffff99;">Minimum Age text</td><td>PopulationDefinition.plannedAge</td><td>ResearchStudy.extension:classifier.valueCodeableConcept.text</td><td colspan="2">ResearchStudy.classifier.text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td style="background-color: #ffff99;">Maximum Age text</td><td>PopulationDefinition.plannedAge</td><td>ResearchStudy.extension:classifier.valueCodeableConcept.text</td><td colspan="2">ResearchStudy.classifier.text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td>Includes females code (cohort definitions not included)</td><td>PopulationDefinition.PlannedSex</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td>Why is this coded, while the planned age is not?</td></tr>
</tbody>
</table>

### StudyDesignPopulation

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Includes males code (cohort definitions not included)</td><td>StudyDesignPopulation.PlannedSex</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
<tr><td>no healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.includesHealthySubjects</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
<tr><td>healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.includesHealthySubjects</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 0-17 (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 18-64 (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 65 and older (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td>ResearchStudy.extension:classifier.valueCodeableConcept</td><td colspan="2">ResearchStudy.classifier</td><td></td></tr>
</tbody>
</table>

<div class="alert alert-info" markdown="1">
PopulationDefinition and StudyDesignPopulation seem to contain the same kind of information: please check.
</div>

### Objective

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Objective text</td><td>Objective.text</td><td colspan="3">ResearchStudy.objective.name</td><td></td></tr>
<tr><td>Objective primary level</td><td>Objective.type</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td></td></tr>
<tr><td>Objective primary level</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td style="background-color: #ffff99;">Clarify whether these are new objectives or a new coding of the same objective (I believe the former, but please confirm).</td></tr>
<tr><td>Objective codeSystem FHIR</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">ResearchStudy.objective.type.coding.system</td><td></td></tr>
<tr><td>Objective secondary level</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td></td></tr>
<tr><td>Objective secondary level</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td></td></tr>
<tr><td>Objective exploratory level</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td></td></tr>
<tr><td>Objective exploratory level</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td></td></tr>
</tbody>
</table>

### Endpoint

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Outcome measurement reference or display</td><td>Endpoint.text</td><td>ResearchStudy.extension:outcomeMeasure.extension:reference.valueReference</td><td>ResearchStudy.outcomeMeasure.reference</td><td>ResearchStudy.objective.outcomeMeasure.endpoint</td><td style="background-color: #ffff99;">The attribute is Endpoint.text, which seems to be a textual element and not a reference: to be checked.</td></tr>
<tr><td>Outcome measurement display</td><td style="background-color: #ffff99;">Endpoint.to-be-specified</td><td>ResearchStudy.extension:outcomeMeasure.extension:reference.valueReference.display</td><td>ResearchStudy.outcomeMeasure.reference.display</td><td>ResearchStudy.objective.outcomeMeasure.endpoint.display</td><td></td></tr>
<tr><td>Endpoint level</td><td>Endpoint.level</td><td>ResearchStudy.extension:outcomeMeasure.extension:type.valueCodeableConcept.coding</td><td>ResearchStudy.outcomeMeasure.type.coding</td><td>ResearchStudy.objective.outcomeMeasure.type.coding</td><td></td></tr>
</tbody>
</table>

### InterventionalStudyDesign

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>purpose Intent</td><td>InterventionalStudyDesign.intentTypes</td><td colspan="2">ResearchStudy.primaryPurposeType.coding</td><td>ResearchStudy.purposeType.coding</td><td></td></tr>
<tr><td>purpose SubType</td><td>InterventionalStudyDesign.subTypes</td><td colspan="2">ResearchStudy.primaryPurposeType.coding</td><td>ResearchStudy.purposeType.coding</td><td></td></tr>
</tbody>
</table>

### StudyDesign

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Phase</td><td>StudyDesign.studyPhase</td><td colspan="3">ResearchStudy.phase.coding</td><td></td></tr>
</tbody>
</table>

### extension studyProgressStatus

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>progress status</td><td>extension studyProgressStatus.state</td><td>ResearchStudy.extension:progressStatus.extension:state.valueCodeableConcept.coding</td><td colspan="2">ResearchStudy.progressStatus.state.coding</td><td></td></tr>
<tr><td>progress status actual</td><td>extension studyProgressStatus.isActual</td><td>ResearchStudy.extension:progressStatus.extension:actual.valueBoolean</td><td colspan="2">ResearchStudy.progressStatus.actual</td><td></td></tr>
<tr><td>progress status period</td><td>extension studyProgressStatus.startDate, endDate</td><td>ResearchStudy.extension:progressStatus.extension:period.valuePeriod</td><td colspan="2">ResearchStudy.progressStatus.period</td><td></td></tr>
</tbody>
</table>

### StudyArm

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Arm name</td><td>StudyArm.label</td><td>ResearchStudy.arm.name</td><td colspan="2">ResearchStudy.comparisonGroup.name</td><td>In R4 the lement is called arm</td></tr>
<tr><td>Arm description</td><td>StudyArm.description</td><td>ResearchStudy.arm.description</td><td colspan="2">ResearchStudy.comparisonGroup.description</td><td></td></tr>
</tbody>
</table>

### studyCohort

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Cohort name</td><td>studyCohort.label</td><td>ResearchStudy.arm.name</td><td colspan="2">ResearchStudy.comparisonGroup.name</td><td>Cohort are not described in the Group ?</td></tr>
<tr><td>Cohort description</td><td>studyCohort.description</td><td>ResearchStudy.arm.description</td><td colspan="2">ResearchStudy.comparisonGroup.description</td><td></td></tr>
<tr><td>Cohort planned number</td><td>studyCohort.plannedEnrollmentNumber</td><td>ResearchStudy.arm.extension:targetNumber.valueUnsignedInt</td><td style="background-color: #ffff99;">—</td><td>ResearchStudy.comparisonGroup.targetNumber</td><td>This element is not in not present neither in the R4 arm nor in the R5 comparisonGroup; R4: READI local extension researchStudy-arm-targetNumber (ResearchStudyArmTargetNumber).</td></tr>
</tbody>
</table>

### StudySite

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>location reference</td><td>StudySite.id</td><td colspan="3">ResearchStudy.site</td><td></td></tr>
<tr><td>location id</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">Location.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>site name</td><td>StudySite.label</td><td colspan="3">Location.name</td><td></td></tr>
<tr><td>site type</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">Location.type</td><td></td></tr>
<tr><td>site country</td><td>StudySite.country</td><td colspan="3">Location.address.country</td><td></td></tr>
<tr><td>Reference to group of criteria</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td>ResearchStudy.enrollment</td><td colspan="2">ResearchStudy.recruitment.eligibility</td><td>This element in R4 is enrollment</td></tr>
<tr><td>Eligibility overall list id</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">Group-all.id</td><td>The Resource is Group; Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>combination method general</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group-all.combinationMethod</td><td>Not able to find this element in R4 or R5 Group</td></tr>
</tbody>
</table>

### EligibilityCriterionItem

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Eligibility criteria text</td><td style="background-color: #ffff99;">EligibilityCriterionItem.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group-all.characteristic.description</td><td></td></tr>
<tr><td>Eligibility criteria code</td><td style="background-color: #ffff99;">EligibilityCriterionItem.to-be-specified</td><td colspan="3">Group-all.characteristic.code.text</td><td></td></tr>
</tbody>
</table>

### EligibilityCriterion

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Exclusion criterion true/false?</td><td>EligibilityCriterion.category</td><td colspan="3">Group-all.characteristic.exclude</td><td></td></tr>
<tr><td>Group references</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">Group-all.characteristic.valueReference.reference</td><td>It should be right .. But to be sure that it refers to a Group that full fill a specific caracthersitic</td></tr>
<tr><td>Exclusion criterion true or false?</td><td>EligibilityCriterion.category</td><td colspan="3">Group.characteristic.exclude</td><td></td></tr>
</tbody>
</table>

### ExpectedResponse

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Node reference indication</td><td>ExpectedResponse.atTiming</td><td colspan="3">Group-all.characteristic.valueReference.type</td><td>It is OK if type is fixed to “Group”</td></tr>
<tr><td>eligibility criteria subgroup referenced id</td><td>ExpectedResponse.id</td><td colspan="3">Group.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>eligibility criteria - response combination method</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.combinationMethod</td><td>Not able to find this element in R4 or R5 Group</td></tr>
<tr><td>expected response label (set to &quot;Node&quot; for combinations)</td><td>ExpectedResponse.label</td><td>Group.extension:description</td><td colspan="2">Group.description</td><td>Not sure to have understood what is about</td></tr>
<tr><td>expected response min value</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueRange.low.value</td><td></td></tr>
<tr><td>expected response min value unit</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueRange.low.unit</td><td></td></tr>
<tr><td>expected response max value - single response</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueRange.high.value</td><td></td></tr>
<tr><td>expected response max value unit</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueRange.high.unit</td><td></td></tr>
<tr><td>expected response description</td><td>ExpectedResponse.description</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.description</td><td></td></tr>
<tr><td>Expected response value code</td><td>ExpectedResponse.codes</td><td colspan="3">Group.characteristic.valueCodeableConcept.coding.code</td><td></td></tr>
<tr><td>Expected response value decode</td><td>ExpectedResponse.codes</td><td colspan="3">Group.characteristic.valueCodeableConcept.coding.display</td><td></td></tr>
<tr><td>Expected response value codeSystem</td><td>ExpectedResponse.codes</td><td colspan="3">Group.characteristic.valueCodeableConcept.coding.system</td><td></td></tr>
<tr><td>expected response quantity - single response</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueQuantity.value</td><td></td></tr>
<tr><td>expected response unit</td><td>ExpectedResponse.value</td><td colspan="3">Group.characteristic.valueQuantity.unit</td><td></td></tr>
<tr><td>Group low timing range</td><td>ExpectedResponse.atTiming</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.offsetRange.low.value</td><td>Not sure to have understood what is about; relativeTime is not a subelment of characteristic in HFIR R4 / R5</td></tr>
<tr><td>Group low timing unit</td><td>ExpectedResponse.atTiming</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.offsetRange.low.unit</td><td></td></tr>
<tr><td>Group high timing range</td><td>ExpectedResponse.atTiming</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.offsetRange.high.value</td><td></td></tr>
<tr><td>Group high timing unit</td><td>ExpectedResponse.atTiming</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.offsetRange.high.unit</td><td></td></tr>
<tr><td>relative time context code</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.contextCode.coding.code</td><td></td></tr>
<tr><td>relative time context display</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.contextCode.coding.display</td><td></td></tr>
<tr><td>relative time context system</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>Group.characteristic.relativeTime.contextCode.coding.system</td><td></td></tr>
</tbody>
</table>

### BiomedicalConcept

<table class="grid" style="width: 90%;">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Loinc Code of assessment</td><td>BiomedicalConcept.code</td><td colspan="3">Group.characteristic.code.coding</td><td>Not sure about its meaning..</td></tr>
<tr><td>Evidence variable id</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>Evidence variable name</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.name</td><td></td></tr>
<tr><td>Evidence variable title</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.title</td><td></td></tr>
<tr><td>Evidence variable description</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.description</td><td></td></tr>
<tr><td>Evidence classifier (note that questionnaires should get another code / not taken care of yet)</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2" style="background-color: #ffff99;">—</td><td>EvidenceVariable.classifier</td><td>Not able to find it in R4 or R5; This has been introdcued in R6</td></tr>
</tbody>
</table>
