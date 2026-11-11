<div class="stu-note" markdown="1">
This mapping is a work in progress: it has not been validated yet and may change at any time.
</div>

<p>Cell colours: <span style="background-color: #ffff99; padding: 0 0.5em;">yellow</span> to be specified: no USDM source, no path in that FHIR version, or flagged by hand; <span style="background-color: #ffd8a8; padding: 0 0.5em;">orange</span> to be checked; <span style="background-color: #ffb3b3; padding: 0 0.5em;">red</span> known to be wrong; <span style="background-color: #e6f4e6; padding: 0 0.5em;">hardcoded value</span> the JSONata expression returns a fixed value.</p>

### Indication

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Condition label</td><td>Indication.label</td><td colspan="3">ResearchStudy.condition.text</td><td></td></tr>
<tr><td>Condition code</td><td>Indication.codes</td><td colspan="3">ResearchStudy.condition.coding</td><td></td></tr>
</tbody>
</table>
</div>

### StudyIdentifier

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Identifier</td><td>StudyIdentifier.text</td><td colspan="3">ResearchStudy.identifier.value</td><td></td></tr>
<tr><td>Study Identifier FHIR type</td><td style="background-color: #ffff99;">StudyIdentifier.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"study identifier"</code></span></td><td colspan="3">ResearchStudy.identifier.type.text</td><td>ResearchStudy.identifier has not a codeableConcept</td></tr>
<tr><td>Study Identifier Organization</td><td>StudyIdentifier.scope</td><td colspan="3">ResearchStudy.identifier.assigner.display</td><td></td></tr>
<tr><td>NCT identifier system</td><td style="background-color: #ffff99;">StudyIdentifier.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://terminology.hl7.org/NamingSystem/ClinicalTrials-Gov"</code> (only when $substring(text,0,3)="NCT")</span></td><td colspan="3">ResearchStudy.identifier.system</td><td></td></tr>
<tr><td>Identifier use</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"official"</code></span></td><td colspan="3">ResearchStudy.identifier.use</td><td></td></tr>
</tbody>
</table>
</div>

### StudyTitle

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study titles</td><td>StudyTitle.text</td><td colspan="3">ResearchStudy.label.value</td><td></td></tr>
<tr><td>Official title</td><td>StudyTitle.text</td><td colspan="3">ResearchStudy.title</td><td></td></tr>
<tr><td>Title type</td><td>StudyTitle.type</td><td colspan="3">ResearchStudy.label.type.coding</td><td></td></tr>
<tr><td>Translated titles</td><td>StudyTitle.extension</td><td colspan="3">ResearchStudy.label.value</td><td></td></tr>
<tr><td>Translated title type</td><td>StudyTitle.type</td><td colspan="3">ResearchStudy.label.type.coding</td><td></td></tr>
<tr><td>Translated title language</td><td>StudyTitle.extension</td><td colspan="3">ResearchStudy.label.language</td><td>R5 preadoption ?</td></tr>
<tr><td>Eligibility display (official or short title)</td><td>StudyTitle.text</td><td>ResearchStudy.enrollment.display</td><td colspan="2">ResearchStudy.recruitment.eligibility.display</td><td></td></tr>
</tbody>
</table>
</div>

### Study

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study description</td><td>Study.description</td><td colspan="3">ResearchStudy.description</td><td></td></tr>
</tbody>
</table>
</div>

### StudyDesignPopulation

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Minimum Age text</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.classifier.text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td>Maximum Age text</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.classifier.text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td>Includes females code (cohort definitions not included)</td><td>StudyDesignPopulation.PlannedSex</td><td colspan="3">ResearchStudy.classifier</td><td>Why is this coded, while the planned age is not?</td></tr>
<tr><td>Includes males code (cohort definitions not included)</td><td>StudyDesignPopulation.PlannedSex</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>no healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.includesHealthySubjects</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.includesHealthySubjects</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 0-17 (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 18-64 (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>age category 65 and older (Only based on population and year unit)</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>Planned enrollment number (first comparison group only — R6 replacement for recruitment.targetNumber)</td><td>StudyDesignPopulation.plannedEnrollmentNumber</td><td colspan="2" style="background-color: #ffff99;">—</td><td>ResearchStudy.comparisonGroup.targetNumber</td><td>This element is not in not present neither in the R4 arm nor in the R5 comparisonGroup; R4: READI local extension researchStudy-arm-targetNumber (ResearchStudyArmTargetNumber).</td></tr>
<tr><td>Planned enrollment number</td><td>StudyDesignPopulation.plannedEnrollmentNumber</td><td>ResearchStudy.extension</td><td colspan="2">ResearchStudy.recruitment.targetNumber</td><td></td></tr>
<tr><td>Eligibility overall list id</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"eligibility-criteria"</code> (for id "eligibility-criteria")</span></td><td colspan="3" style="background-color: #ffd8a8;">Group.id</td><td>The Resource is Group; Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>combination method general</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"all-of"</code> (for id "eligibility-criteria")</span></td><td>Group.extension:combinationMethod</td><td colspan="2">Group.combinationMethod</td><td>Not able to find this element in R4 or R5 Group. To be decided: in GroupReadi the READI extension group-combinationMethod is a modifierExtension (modifierExtension:combinationMethod); shall it stay a modifierExtension, as it is now, or become an extension?</td></tr>
<tr><td>Study Population Source (population description free text)</td><td>StudyDesignPopulation.description</td><td colspan="3">ResearchStudy.classifier</td><td></td></tr>
<tr><td>Extension age range (artifact-useContext from plannedAge)</td><td>StudyDesignPopulation.plannedAge</td><td colspan="3">ResearchStudy.extension</td><td></td></tr>
</tbody>
</table>
</div>

### Objective

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Objective text</td><td>Objective.text</td><td colspan="3">ResearchStudy.objective.name</td><td></td></tr>
<tr><td>Translated objective name</td><td>Objective.extension</td><td colspan="3">ResearchStudy.objective._name.extension</td><td></td></tr>
<tr><td>Objective primary level (code)</td><td>Objective.type</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td>Clarify whether these are new objectives or a new coding of the same objective (I believe the former, but please confirm).</td></tr>
<tr><td>Objective primary level (display)</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td></td></tr>
<tr><td>Objective codeSystem FHIR</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://terminology.hl7.org/CodeSystem/research-study-objective-type"</code></span></td><td colspan="3">ResearchStudy.objective.type.coding.system</td><td></td></tr>
<tr><td>Objective secondary level (code)</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td></td></tr>
<tr><td>Objective secondary level (display)</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td></td></tr>
<tr><td>Objective exploratory level (code)</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.code</td><td></td></tr>
<tr><td>Objective exploratory level (display)</td><td>Objective.level</td><td colspan="3">ResearchStudy.objective.type.coding.display</td><td></td></tr>
</tbody>
</table>
</div>

### Endpoint

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Outcome measurement name</td><td>Endpoint.text</td><td colspan="2">ResearchStudy.outcomeMeasure.name</td><td>ResearchStudy.objective.outcomeMeasure.name</td><td></td></tr>
<tr><td>Outcome measurement description</td><td>Endpoint.description</td><td colspan="2">ResearchStudy.outcomeMeasure.description</td><td>ResearchStudy.objective.outcomeMeasure.description</td><td></td></tr>
<tr><td>Outcome measurement reference or display</td><td>Endpoint.forAssessment (extension)</td><td colspan="2">ResearchStudy.outcomeMeasure.reference</td><td>ResearchStudy.objective.outcomeMeasure.endpoint</td><td>The attribute is Endpoint.text, which seems to be a textual element and not a reference: to be checked.</td></tr>
<tr><td>Endpoint level</td><td>Endpoint.level</td><td colspan="2">ResearchStudy.outcomeMeasure.type.coding</td><td>ResearchStudy.objective.outcomeMeasure.type.coding</td><td></td></tr>
</tbody>
</table>
</div>

### InterventionalStudyDesign

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>purpose Intent</td><td>InterventionalStudyDesign.intentTypes</td><td colspan="2">ResearchStudy.primaryPurposeType.coding</td><td>ResearchStudy.purposeType.coding</td><td></td></tr>
<tr><td>purpose SubType</td><td>InterventionalStudyDesign.subTypes</td><td colspan="2" style="background-color: #ffff99;">—</td><td>ResearchStudy.purposeType.coding</td><td></td></tr>
</tbody>
</table>
</div>

### StudyDesign

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Phase</td><td>StudyDesign.studyPhase</td><td colspan="3">ResearchStudy.phase.coding</td><td></td></tr>
<tr><td>Study Phase text</td><td>StudyDesign.studyPhase</td><td colspan="3">ResearchStudy.phase.text</td><td></td></tr>
<tr><td>Study Design type (from studyType)</td><td>StudyDesign.studyType</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
<tr><td>Study Design cohort design (from intervention model)</td><td>StudyDesign.model</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
<tr><td>Study Design observational model (from observational model)</td><td>StudyDesign.model</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
<tr><td>Study Design allocation (randomized/non-randomized characteristic)</td><td>StudyDesign.characteristics</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
</tbody>
</table>
</div>

### extension studyProgressStatus

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>progress status</td><td>extension studyProgressStatus.state</td><td>ResearchStudy.extension</td><td colspan="2">ResearchStudy.progressStatus.state.coding</td><td></td></tr>
<tr><td>progress status actual</td><td>extension studyProgressStatus.isActual</td><td style="background-color: #ffff99;">—</td><td colspan="2">ResearchStudy.progressStatus.actual</td><td></td></tr>
<tr><td>progress status period</td><td>extension studyProgressStatus.startDate, endDate</td><td style="background-color: #ffff99;">—</td><td colspan="2">ResearchStudy.progressStatus.period</td><td></td></tr>
</tbody>
</table>
</div>

### StudyArm

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Arm name</td><td>StudyArm.label</td><td>ResearchStudy.arm.name</td><td colspan="2">ResearchStudy.comparisonGroup.name</td><td>In R4 the element is called arm</td></tr>
<tr><td>Arm description</td><td>StudyArm.description</td><td>ResearchStudy.arm.description</td><td colspan="2">ResearchStudy.comparisonGroup.description</td><td></td></tr>
<tr><td>Arm type</td><td>StudyArm.type</td><td>ResearchStudy.arm.type.coding</td><td colspan="2">ResearchStudy.comparisonGroup.type.coding</td><td></td></tr>
<tr><td>Arm eligibility (reference to the arm Group)</td><td>StudyArm.id</td><td>ResearchStudy.arm.eligibility</td><td colspan="2">ResearchStudy.comparisonGroup.eligibility</td><td></td></tr>
<tr><td>Arm eligibility group id</td><td>StudyArm.id</td><td colspan="3" style="background-color: #ffd8a8;">Group.id</td><td></td></tr>
<tr><td>Arm eligibility group title</td><td>StudyArm.label</td><td>Group.name</td><td colspan="2">Group.title</td><td>R4: Group.name, the R4 equivalent of R5 Group.title</td></tr>
<tr><td>Arm eligibility group status</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"active"</code></span></td><td colspan="3">Group.status</td><td></td></tr>
<tr><td>Arm eligibility group membership</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"conceptual"</code></span></td><td>Group.actual</td><td colspan="2">Group.membership</td><td>R4: Group.actual, the R4 equivalent of R5 Group.membership (conceptual = false, enumerated = true). Should we instead pre-adopt the R5 element Group.membership (R5 cross-version extension) to facilitate the cross-version transformation?</td></tr>
<tr><td>Arm eligibility group type (code.text)</td><td>StudyArm.type</td><td colspan="3">Group.code.text</td><td>Is StudyArm.type a string ?</td></tr>
<tr><td>Arm eligibility group description</td><td>StudyArm.description</td><td>Group.extension:description</td><td colspan="2">Group.description</td><td></td></tr>
</tbody>
</table>
</div>

### studyCohort

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Cohort name</td><td>studyCohort.label</td><td>ResearchStudy.arm.name</td><td colspan="2">ResearchStudy.comparisonGroup.name</td><td>Cohort are not described in the Group ?</td></tr>
<tr><td>Cohort description</td><td>studyCohort.description</td><td>ResearchStudy.arm.description</td><td colspan="2">ResearchStudy.comparisonGroup.description</td><td></td></tr>
</tbody>
</table>
</div>

### StudySite

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>location reference</td><td>StudySite.id</td><td colspan="3">ResearchStudy.site</td><td></td></tr>
<tr><td>location id</td><td>StudySite.id</td><td colspan="3" style="background-color: #ffd8a8;">Location.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>location identifier</td><td>StudySite.id</td><td colspan="3">Location.identifier.value</td><td></td></tr>
<tr><td>site name</td><td>StudySite.label</td><td colspan="3">Location.name</td><td></td></tr>
<tr><td>site type</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"code": "DX", "display": "Diagnostics or therapeutics unit", "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"}</code></span></td><td colspan="3">Location.type.coding</td><td></td></tr>
<tr><td>site country</td><td>StudySite.country</td><td colspan="3">Location.address.country</td><td></td></tr>
</tbody>
</table>
</div>

### Address

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>site city</td><td>Address.city</td><td colspan="3">Location.address.city</td><td></td></tr>
<tr><td>site state</td><td>Address.state</td><td colspan="3">Location.address.state</td><td></td></tr>
<tr><td>site postal code</td><td>Address.postalCode</td><td colspan="3">Location.address.postalCode</td><td></td></tr>
<tr><td>Reference to group of criteria</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"reference": "#eligibility-criteria", "type":"Group"}</code> (for id "eligibility-criteria")</span></td><td>ResearchStudy.enrollment</td><td colspan="2">ResearchStudy.recruitment.eligibility</td><td>This element in R4 is enrollment</td></tr>
</tbody>
</table>
</div>

### EligibilityCriterionItem

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Eligibility criteria text</td><td style="background-color: #ffff99;">EligibilityCriterionItem.to-be-specified</td><td>Group.characteristic.extension:description</td><td colspan="2">Group.characteristic.description</td><td>Where do you get this data from? Do you really need this row?</td></tr>
<tr><td>Eligibility criteria code</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"Defined by CodeableConcept"</code></span></td><td colspan="3">Group.characteristic.code.text</td><td>Not clear what it means: hardcoded value "Defined by CodeableConcept".</td></tr>
<tr><td>Eligibility criteria valueCodeableConcept text</td><td>EligibilityCriterionItem.text</td><td colspan="3">Group.characteristic.valueCodeableConcept.text</td><td>Could not this be the Eligibility criteria text?</td></tr>
</tbody>
</table>
</div>

### EligibilityCriterion

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Exclusion criterion true/false?</td><td>EligibilityCriterion.category</td><td colspan="3">Group.characteristic.exclude</td><td></td></tr>
</tbody>
</table>
</div>

### Extension

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td style="background-color: #ffd8a8;">Group references</td><td style="background-color: #ffd8a8;">Extension.to-be-specified</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueReference.reference</td><td style="background-color: #ffd8a8;">It should be right .. But to be sure that it refers to a Group that full fill a specific caracthersitic. Which characteristic code is used for the valueReference? How is it used?</td></tr>
</tbody>
</table>
</div>

### ExpectedResponse

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Node reference indication</td><td>ExpectedResponse.atTiming</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueReference.type</td><td>Please clarify which kind of code (characteristic.code) is used to distinguish among all these different kinds of characteristics (range, code, quantity, reference, ...).</td></tr>
<tr><td>expected response range - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange</td><td></td></tr>
<tr><td>Expected response value code - direct</td><td>ExpectedResponse.codes</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueCodeableConcept.coding</td><td></td></tr>
<tr><td>expected response quantity - single response - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity</td><td></td></tr>
<tr><td>Group timing range - direct</td><td>ExpectedResponse.atTiming</td><td colspan="2">Group.characteristic.extension:relativeTime.extension:offsetRange.valueRange</td><td>Group.characteristic.relativeTime.offsetRange</td><td></td></tr>
<tr><td>Group timing context - direct</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="2">Group.characteristic.extension:relativeTime.extension:contextCode.valueCodeableConcept.coding</td><td>Group.characteristic.relativeTime.contextCode.coding</td><td></td></tr>
<tr><td>expected response min value unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.code</td><td></td></tr>
<tr><td>expected response min value unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueRange.low.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response min value is inclusive (flag, removed by fhir_version.py) - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.isInclusive</td><td></td></tr>
<tr><td>expected response max value unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.code</td><td></td></tr>
<tr><td>expected response max value unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueRange.high.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response max value is inclusive (flag, removed by fhir_version.py) - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.isInclusive</td><td></td></tr>
<tr><td>expected response unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity.code</td><td></td></tr>
<tr><td>expected response unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueQuantity.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>eligibility criteria subgroup referenced id</td><td>ExpectedResponse.id</td><td colspan="3" style="background-color: #ffd8a8;">Group.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>eligibility criteria - response combination method</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td>Group.extension:combinationMethod</td><td colspan="2">Group.combinationMethod</td><td>Not able to find this element in R4 or R5 Group. To be decided: in GroupReadi the READI extension group-combinationMethod is a modifierExtension (modifierExtension:combinationMethod); shall it stay a modifierExtension, as it is now, or become an extension?</td></tr>
<tr><td>expected response label (set to "Node" for combinations)</td><td>ExpectedResponse.label</td><td>Group.extension:description</td><td colspan="2">Group.description</td><td>Not sure to have understood what is about</td></tr>
<tr><td>expected response range</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange</td><td></td></tr>
<tr><td>expected response description - node</td><td>ExpectedResponse.description</td><td>Group.characteristic.extension:description</td><td colspan="2">Group.characteristic.description</td><td></td></tr>
<tr><td>Expected response value code - via nodes</td><td>ExpectedResponse.codes</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueCodeableConcept.coding</td><td></td></tr>
<tr><td>expected response quantity response - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity</td><td></td></tr>
<tr><td>Group timing range - node</td><td>ExpectedResponse.atTiming</td><td colspan="2">Group.characteristic.extension:relativeTime.extension:offsetRange.valueRange</td><td>Group.characteristic.relativeTime.offsetRange</td><td></td></tr>
<tr><td>Group timing context - nodes</td><td>ExpectedResponse.atTiming</td><td colspan="2">Group.characteristic.extension:relativeTime.extension:contextCode.valueCodeableConcept.coding</td><td>Group.characteristic.relativeTime.contextCode.coding</td><td></td></tr>
<tr><td>Exclusion criterion true or false?</td><td>ExpectedResponse.category</td><td colspan="3">Group.characteristic.exclude</td><td></td></tr>
<tr><td>expected response min value unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.code</td><td></td></tr>
<tr><td>expected response min value unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueRange.low.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response min value is inclusive (flag, removed by fhir_version.py) - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.low.isInclusive</td><td></td></tr>
<tr><td>expected response max value unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.code</td><td></td></tr>
<tr><td>expected response max value unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueRange.high.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response max value is inclusive (flag, removed by fhir_version.py) - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueRange.high.isInclusive</td><td></td></tr>
<tr><td>expected response unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.value</td><td colspan="3" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity.code</td><td></td></tr>
<tr><td>expected response unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.value</td><td style="background-color: #ffb3b3;">Group.characteristic.valueQuantity.extension:quantity-translation.valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.characteristic.valueQuantity.standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
</tbody>
</table>
</div>

### BiomedicalConcept

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Loinc Code of assessment - direct</td><td>BiomedicalConcept.code</td><td colspan="3">Group.characteristic.code.coding</td><td></td></tr>
<tr><td>Loinc Code of assessment</td><td>BiomedicalConcept.code</td><td colspan="3">Group.characteristic.code.coding</td><td>Not sure about its meaning..</td></tr>
</tbody>
</table>
</div>

### ExpResponseNode

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>sub-node reference (nested Group) - via nodes</td><td>ExpResponseNode.childArray</td><td colspan="3">Group.characteristic.valueReference.reference</td><td></td></tr>
<tr><td>sub-node reference type - via nodes</td><td>ExpResponseNode.childArray</td><td colspan="3">Group.characteristic.valueReference.type</td><td></td></tr>
<tr><td>Evidence variable id</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3" style="background-color: #ffd8a8;">EvidenceVariable.id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>Evidence variable name</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.name</td><td></td></tr>
<tr><td>Evidence variable status</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.status</td><td></td></tr>
<tr><td>Evidence variable title</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.title</td><td></td></tr>
<tr><td>Evidence variable description</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.description</td><td></td></tr>
<tr><td>Evidence classifier (note that questionnaires should get another code / not taken care of yet)</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified</td><td colspan="3">EvidenceVariable.classifier</td><td>Not able to find it in R4 or R5; This has been introdcued in R6</td></tr>
</tbody>
</table>
</div>

### StudyRole

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Design masking (masked roles → SEVCO blinding codes)</td><td>StudyRole.masking</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
<tr><td>Associated party name — lead-sponsor (organization label)</td><td>StudyRole.label</td><td colspan="3">ResearchStudy.associatedParty.name</td><td></td></tr>
<tr><td>Associated party name — co-sponsor (organization label)</td><td>StudyRole.label</td><td colspan="3">ResearchStudy.associatedParty.name</td><td></td></tr>
<tr><td>Associated party reference (points to contained PractitionerRole)</td><td>StudyRole.id</td><td colspan="3">ResearchStudy.associatedParty.party.reference</td><td></td></tr>
<tr><td>Associated party reference type</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"PractitionerRole"</code> (only when code.code = "EXT0003")</span></td><td colspan="3">ResearchStudy.associatedParty.party.type</td><td></td></tr>
<tr><td>Contained PractitionerRole id</td><td>StudyRole.id</td><td colspan="3" style="background-color: #ffd8a8;">PractitionerRole.id</td><td></td></tr>
<tr><td>Contained PractitionerRole organization display (role label)</td><td>StudyRole.label</td><td colspan="3">PractitionerRole.organization.display</td><td></td></tr>
<tr><td>Associated party reference — primary-investigator (points to contained PractitionerRole)</td><td>StudyRole.id</td><td colspan="3">ResearchStudy.associatedParty.party.reference</td><td></td></tr>
<tr><td>Associated party reference type — primary-investigator</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"PractitionerRole"</code> (only when code.code = "C19924")</span></td><td colspan="3">ResearchStudy.associatedParty.party.type</td><td></td></tr>
<tr><td>Contained PractitionerRole id — primary-investigator</td><td>StudyRole.id</td><td colspan="3" style="background-color: #ffd8a8;">PractitionerRole.id</td><td></td></tr>
<tr><td>Contained PractitionerRole organization display — primary-investigator (role label)</td><td>StudyRole.label</td><td colspan="3">PractitionerRole.organization.display</td><td></td></tr>
<tr><td>Associated party name — collaborator (organization label)</td><td>StudyRole.label</td><td colspan="3">ResearchStudy.associatedParty.name</td><td></td></tr>
</tbody>
</table>
</div>

### StudyVersion

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Design masking (open label — no masked role found)</td><td>StudyVersion.roles</td><td colspan="3">ResearchStudy.studyDesign</td><td></td></tr>
</tbody>
</table>
</div>

### Code

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Associated party role code — lead-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.role.coding.code</td><td></td></tr>
<tr><td>Associated party role display — lead-sponsor</td><td>Code.decode</td><td colspan="3">ResearchStudy.associatedParty.role.coding.display</td><td></td></tr>
<tr><td>Associated party role system — lead-sponsor</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C70793")</span></td><td colspan="3">ResearchStudy.associatedParty.role.coding.system</td><td></td></tr>
<tr><td>Associated party organization type system — lead-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.system</td><td></td></tr>
<tr><td>Associated party organization type code — lead-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.code</td><td></td></tr>
<tr><td>Associated party organization type display — lead-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.display</td><td></td></tr>
<tr><td>Associated party role code — co-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.role.coding.code</td><td></td></tr>
<tr><td>Associated party role display — co-sponsor</td><td>Code.decode</td><td colspan="3">ResearchStudy.associatedParty.role.coding.display</td><td></td></tr>
<tr><td>Associated party role system — co-sponsor</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C215669")</span></td><td colspan="3">ResearchStudy.associatedParty.role.coding.system</td><td></td></tr>
<tr><td>Associated party organization type system — co-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.system</td><td></td></tr>
<tr><td>Associated party organization type code — co-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.code</td><td></td></tr>
<tr><td>Associated party organization type display — co-sponsor</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.classifier.coding.display</td><td></td></tr>
<tr><td>Associated party role code</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.role.coding.code</td><td></td></tr>
<tr><td>Associated party role display</td><td>Code.decode</td><td colspan="3">ResearchStudy.associatedParty.role.coding.display</td><td></td></tr>
<tr><td>Associated party role system</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "EXT0003")</span></td><td colspan="3">ResearchStudy.associatedParty.role.coding.system</td><td></td></tr>
<tr><td>Associated party role code — primary-investigator</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.role.coding.code</td><td></td></tr>
<tr><td>Associated party role display — primary-investigator</td><td>Code.decode</td><td colspan="3">ResearchStudy.associatedParty.role.coding.display</td><td></td></tr>
<tr><td>Associated party role system — primary-investigator</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C19924")</span></td><td colspan="3">ResearchStudy.associatedParty.role.coding.system</td><td></td></tr>
<tr><td>Associated party role code — collaborator</td><td>Code.code</td><td colspan="3">ResearchStudy.associatedParty.role.coding.code</td><td></td></tr>
<tr><td>Associated party role display — collaborator</td><td>Code.decode</td><td colspan="3">ResearchStudy.associatedParty.role.coding.display</td><td></td></tr>
<tr><td>Associated party role system — collaborator</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "EXT0004")</span></td><td colspan="3">ResearchStudy.associatedParty.role.coding.system</td><td></td></tr>
</tbody>
</table>
</div>

### AssignedPerson

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Associated party name (assigned person)</td><td>AssignedPerson.text</td><td colspan="3">ResearchStudy.associatedParty.name</td><td></td></tr>
<tr><td>Contained PractitionerRole code text (assigned person job title)</td><td>AssignedPerson.jobTitle</td><td colspan="3">PractitionerRole.code.text</td><td></td></tr>
<tr><td>Contained PractitionerRole practitioner display (assigned person name)</td><td>AssignedPerson.text</td><td colspan="3">PractitionerRole.practitioner.display</td><td></td></tr>
<tr><td>Associated party name — primary-investigator (assigned person)</td><td>AssignedPerson.text</td><td colspan="3">ResearchStudy.associatedParty.name</td><td></td></tr>
<tr><td>Contained PractitionerRole code text — primary-investigator (job title)</td><td>AssignedPerson.jobTitle</td><td colspan="3">PractitionerRole.code.text</td><td></td></tr>
<tr><td>Contained PractitionerRole practitioner display — primary-investigator (assigned person name)</td><td>AssignedPerson.text</td><td colspan="3">PractitionerRole.practitioner.display</td><td></td></tr>
</tbody>
</table>
</div>

### StudyIntervention

<div class="mapping-scroll">
<table class="grid">
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Intervention evidence variable id</td><td>StudyIntervention.id</td><td colspan="3" style="background-color: #ffd8a8;">EvidenceVariable.id</td><td></td></tr>
<tr><td>Intervention evidence variable meta profile</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/uv/ebm/StructureDefinition/variable-definition"</code></span></td><td colspan="3">EvidenceVariable.meta.profile</td><td></td></tr>
<tr><td>Intervention evidence variable name</td><td>StudyIntervention.label</td><td colspan="3">EvidenceVariable.name</td><td></td></tr>
<tr><td>Intervention evidence variable title</td><td>StudyIntervention.label</td><td colspan="3">EvidenceVariable.title</td><td></td></tr>
<tr><td>Intervention evidence variable status</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"active"</code></span></td><td colspan="3">EvidenceVariable.status</td><td></td></tr>
<tr><td>Intervention evidence variable handling (boolean variable)</td><td style="background-color: #ffff99;">to-be-specified.to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"coding": { "code": "STATO:0000724", "system": "https://fevir.net/sevco", "display": "boolean variable" }}</code></span></td><td>EvidenceVariable.type</td><td colspan="2">EvidenceVariable.handling</td><td></td></tr>
<tr><td>Intervention evidence variable classifier (intervention type)</td><td>StudyIntervention.type</td><td colspan="3">EvidenceVariable.classifier</td><td></td></tr>
<tr><td>Intervention evidence variable description</td><td>StudyIntervention.description</td><td colspan="3">EvidenceVariable.description</td><td></td></tr>
</tbody>
</table>
</div>
