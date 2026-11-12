<div class="stu-note" markdown="1">
This mapping is a work in progress: it has not been validated yet and may change at any time.
</div>

<p>Cell colours: <span style="background-color: #ffff99; padding: 0 0.5em;">yellow</span> to be specified: no USDM source, no path in that FHIR version, or flagged by hand; <span style="background-color: #ffd8a8; padding: 0 0.5em;">orange</span> to be checked; <span style="background-color: #ffb3b3; padding: 0 0.5em;">red</span> known to be wrong; <span style="background-color: #e6f4e6; padding: 0 0.5em;">hardcoded value</span> the JSONata expression returns a fixed value.</p>

### Indication

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Condition label</td><td>Indication.<wbr/>label</td><td colspan="3">ResearchStudy.<wbr/>condition.<wbr/>text</td><td></td></tr>
<tr><td>Condition code</td><td>Indication.<wbr/>codes</td><td colspan="3">ResearchStudy.<wbr/>condition.<wbr/>coding</td><td></td></tr>
</tbody>
</table>
</div>

### StudyIdentifier

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Identifier</td><td>StudyIdentifier.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>identifier.<wbr/>value</td><td></td></tr>
<tr><td>Study Identifier FHIR type</td><td style="background-color: #ffff99;">StudyIdentifier.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"study identifier"</code></span></td><td colspan="3">ResearchStudy.<wbr/>identifier.<wbr/>type.<wbr/>text</td><td>ResearchStudy.identifier has not a codeableConcept</td></tr>
<tr><td>Study Identifier Organization</td><td>StudyIdentifier.<wbr/>scope</td><td colspan="3">ResearchStudy.<wbr/>identifier.<wbr/>assigner.<wbr/>display</td><td></td></tr>
<tr><td>NCT identifier system</td><td style="background-color: #ffff99;">StudyIdentifier.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://terminology.hl7.org/NamingSystem/ClinicalTrials-Gov"</code> (only when $substring(text,0,3)="NCT")</span></td><td colspan="3">ResearchStudy.<wbr/>identifier.<wbr/>system</td><td></td></tr>
<tr><td>Identifier use</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"official"</code></span></td><td colspan="3">ResearchStudy.<wbr/>identifier.<wbr/>use</td><td></td></tr>
</tbody>
</table>
</div>

### StudyTitle

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study titles</td><td>StudyTitle.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>label.<wbr/>value</td><td></td></tr>
<tr><td>Official title</td><td>StudyTitle.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>title</td><td></td></tr>
<tr><td>Title type</td><td>StudyTitle.<wbr/>type</td><td colspan="3">ResearchStudy.<wbr/>label.<wbr/>type.<wbr/>coding</td><td></td></tr>
<tr><td>Translated titles</td><td>StudyTitle.<wbr/>extension</td><td colspan="3">ResearchStudy.<wbr/>label.<wbr/>value</td><td></td></tr>
<tr><td>Translated title type</td><td>StudyTitle.<wbr/>type</td><td colspan="3">ResearchStudy.<wbr/>label.<wbr/>type.<wbr/>coding</td><td></td></tr>
<tr><td>Translated title language</td><td>StudyTitle.<wbr/>extension</td><td colspan="3">ResearchStudy.<wbr/>label.<wbr/>language</td><td>R5 preadoption ?</td></tr>
<tr><td>Eligibility display (official or short title)</td><td>StudyTitle.<wbr/>text</td><td>ResearchStudy.<wbr/>enrollment.<wbr/>display</td><td colspan="2">ResearchStudy.<wbr/>recruitment.<wbr/>eligibility.<wbr/>display</td><td></td></tr>
</tbody>
</table>
</div>

### Study

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study description</td><td>Study.<wbr/>description</td><td colspan="3">ResearchStudy.<wbr/>description</td><td></td></tr>
</tbody>
</table>
</div>

### StudyDesignPopulation

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Minimum Age text</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>classifier.<wbr/>text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td>Maximum Age text</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>classifier.<wbr/>text</td><td>Is PlannedAge a single string, or two strings for the minimum and the maximum age?</td></tr>
<tr><td>Includes females code (cohort definitions not included)</td><td>StudyDesignPopulation.<wbr/>PlannedSex</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td>Why is this coded, while the planned age is not?</td></tr>
<tr><td>Includes males code (cohort definitions not included)</td><td>StudyDesignPopulation.<wbr/>PlannedSex</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>no healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.<wbr/>includesHealthySubjects</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>healthy subjects code (cohort definitions not included)</td><td>StudyDesignPopulation.<wbr/>includesHealthySubjects</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>age category 0-17 (Only based on population and year unit)</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>age category 18-64 (Only based on population and year unit)</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>age category 65 and older (Only based on population and year unit)</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>Planned enrollment number (first comparison group only — R6 replacement for recruitment.targetNumber)</td><td>StudyDesignPopulation.<wbr/>plannedEnrollmentNumber</td><td colspan="2" style="background-color: #ffff99;">—</td><td>ResearchStudy.<wbr/>comparisonGroup.<wbr/>targetNumber</td><td>This element is not in not present neither in the R4 arm nor in the R5 comparisonGroup; R4: READI local extension researchStudy-arm-targetNumber (ResearchStudyArmTargetNumber).</td></tr>
<tr><td>Planned enrollment number</td><td>StudyDesignPopulation.<wbr/>plannedEnrollmentNumber</td><td>ResearchStudy.<wbr/>extension</td><td colspan="2">ResearchStudy.<wbr/>recruitment.<wbr/>targetNumber</td><td></td></tr>
<tr><td style="background-color: #ffd8a8;">Eligibility overall list id</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"eligibility-criteria"</code> (for id "eligibility-criteria")</span></td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>id</td><td>The Resource is Group; Is not an identifier (the id of the resource can change when you move the resource around…); Clarify how a resource id can be fixed</td></tr>
<tr><td>combination method general</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"all-of"</code> (for id "eligibility-criteria")</span></td><td>Group.<wbr/>extension:combinationMethod</td><td colspan="2">Group.<wbr/>combinationMethod</td><td>Not able to find this element in R4 or R5 Group. To be decided: in GroupReadi the READI extension group-combinationMethod is a modifierExtension (modifierExtension:combinationMethod); shall it stay a modifierExtension, as it is now, or become an extension?</td></tr>
<tr><td>Study Population Source (population description free text)</td><td>StudyDesignPopulation.<wbr/>description</td><td colspan="3">ResearchStudy.<wbr/>classifier</td><td></td></tr>
<tr><td>Extension age range (artifact-useContext from plannedAge)</td><td>StudyDesignPopulation.<wbr/>plannedAge</td><td colspan="3">ResearchStudy.<wbr/>extension</td><td></td></tr>
</tbody>
</table>
</div>

### Objective

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Objective text</td><td>Objective.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>name</td><td></td></tr>
<tr><td>Translated objective name</td><td>Objective.<wbr/>extension</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>_name.<wbr/>extension</td><td></td></tr>
<tr><td>Objective primary level (code)</td><td>Objective.<wbr/>type</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>code</td><td>Clarify whether these are new objectives or a new coding of the same objective (I believe the former, but please confirm).</td></tr>
<tr><td>Objective primary level (display)</td><td>Objective.<wbr/>level</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Objective codeSystem FHIR</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://terminology.hl7.org/CodeSystem/research-study-objective-type"</code></span></td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Objective secondary level (code)</td><td>Objective.<wbr/>level</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Objective secondary level (display)</td><td>Objective.<wbr/>level</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Objective exploratory level (code)</td><td>Objective.<wbr/>level</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Objective exploratory level (display)</td><td>Objective.<wbr/>level</td><td colspan="3">ResearchStudy.<wbr/>objective.<wbr/>type.<wbr/>coding.<wbr/>display</td><td></td></tr>
</tbody>
</table>
</div>

### Endpoint

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Outcome measurement name</td><td>Endpoint.<wbr/>text</td><td colspan="2">ResearchStudy.<wbr/>outcomeMeasure.<wbr/>name</td><td>ResearchStudy.<wbr/>objective.<wbr/>outcomeMeasure.<wbr/>name</td><td></td></tr>
<tr><td>Outcome measurement description</td><td>Endpoint.<wbr/>description</td><td colspan="2">ResearchStudy.<wbr/>outcomeMeasure.<wbr/>description</td><td>ResearchStudy.<wbr/>objective.<wbr/>outcomeMeasure.<wbr/>description</td><td></td></tr>
<tr><td>Outcome measurement reference or display</td><td>Endpoint.<wbr/>forAssessment (extension)</td><td colspan="2">ResearchStudy.<wbr/>outcomeMeasure.<wbr/>reference</td><td>ResearchStudy.<wbr/>objective.<wbr/>outcomeMeasure.<wbr/>endpoint</td><td>The attribute is Endpoint.text, which seems to be a textual element and not a reference: to be checked.</td></tr>
<tr><td>Endpoint level</td><td>Endpoint.<wbr/>level</td><td colspan="2">ResearchStudy.<wbr/>outcomeMeasure.<wbr/>type.<wbr/>coding</td><td>ResearchStudy.<wbr/>objective.<wbr/>outcomeMeasure.<wbr/>type.<wbr/>coding</td><td></td></tr>
</tbody>
</table>
</div>

### InterventionalStudyDesign

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>purpose Intent</td><td>InterventionalStudyDesign.<wbr/>intentTypes</td><td colspan="2">ResearchStudy.<wbr/>primaryPurposeType.<wbr/>coding</td><td>ResearchStudy.<wbr/>purposeType.<wbr/>coding</td><td></td></tr>
<tr><td>purpose SubType</td><td>InterventionalStudyDesign.<wbr/>subTypes</td><td colspan="2">ResearchStudy.<wbr/>primaryPurposeType.<wbr/>coding</td><td>ResearchStudy.<wbr/>purposeType.<wbr/>coding</td><td></td></tr>
</tbody>
</table>
</div>

### StudyDesign

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Phase</td><td>StudyDesign.<wbr/>studyPhase</td><td colspan="3">ResearchStudy.<wbr/>phase.<wbr/>coding</td><td></td></tr>
<tr><td>Study Phase text</td><td>StudyDesign.<wbr/>studyPhase</td><td colspan="3">ResearchStudy.<wbr/>phase.<wbr/>text</td><td></td></tr>
<tr><td>Study Design type (from studyType)</td><td>StudyDesign.<wbr/>studyType</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
<tr><td>Study Design cohort design (from intervention model)</td><td>StudyDesign.<wbr/>model</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
<tr><td>Study Design observational model (from observational model)</td><td>StudyDesign.<wbr/>model</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
<tr><td>Study Design allocation (randomized/non-randomized characteristic)</td><td>StudyDesign.<wbr/>characteristics</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
</tbody>
</table>
</div>

### extension studyProgressStatus

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>progress status</td><td>extension studyProgressStatus.<wbr/>state</td><td>ResearchStudy.<wbr/>extension:progressStatus.<wbr/>extension:state.<wbr/>valueCodeableConcept.<wbr/>coding</td><td colspan="2">ResearchStudy.<wbr/>progressStatus.<wbr/>state.<wbr/>coding</td><td></td></tr>
<tr><td>progress status actual</td><td>extension studyProgressStatus.<wbr/>isActual</td><td>ResearchStudy.<wbr/>extension:progressStatus.<wbr/>extension:actual.<wbr/>valueBoolean</td><td colspan="2">ResearchStudy.<wbr/>progressStatus.<wbr/>actual</td><td></td></tr>
<tr><td>progress status period</td><td>extension studyProgressStatus.<wbr/>startDate, endDate</td><td>ResearchStudy.<wbr/>extension:progressStatus.<wbr/>extension:period.<wbr/>valuePeriod</td><td colspan="2">ResearchStudy.<wbr/>progressStatus.<wbr/>period</td><td></td></tr>
</tbody>
</table>
</div>

### StudyArm

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Arm name</td><td>StudyArm.<wbr/>label</td><td>ResearchStudy.<wbr/>arm.<wbr/>name</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>name</td><td>In R4 the element is called arm</td></tr>
<tr><td>Arm description</td><td>StudyArm.<wbr/>description</td><td>ResearchStudy.<wbr/>arm.<wbr/>description</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>description</td><td></td></tr>
<tr><td>Arm type</td><td>StudyArm.<wbr/>type</td><td>ResearchStudy.<wbr/>arm.<wbr/>type.<wbr/>coding</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>type.<wbr/>coding</td><td></td></tr>
<tr><td>Arm eligibility (reference to the arm Group)</td><td>StudyArm.<wbr/>id</td><td>ResearchStudy.<wbr/>arm.<wbr/>eligibility</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>eligibility</td><td></td></tr>
<tr><td>Arm eligibility group id</td><td>StudyArm.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>id</td><td></td></tr>
<tr><td>Arm eligibility group title</td><td>StudyArm.<wbr/>label</td><td>Group.<wbr/>name</td><td colspan="2">Group.<wbr/>title</td><td>R4: Group.name, the R4 equivalent of R5 Group.title</td></tr>
<tr><td>Arm eligibility group status</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"active"</code></span></td><td colspan="3">Group.<wbr/>status</td><td></td></tr>
<tr><td>Arm eligibility group membership</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"conceptual"</code></span></td><td>Group.<wbr/>actual</td><td colspan="2">Group.<wbr/>membership</td><td>R4: Group.actual, the R4 equivalent of R5 Group.membership (conceptual = false, enumerated = true). Should we instead pre-adopt the R5 element Group.membership (R5 cross-version extension) to facilitate the cross-version transformation?</td></tr>
<tr><td>Arm eligibility group type (code.text)</td><td>StudyArm.<wbr/>type</td><td colspan="3">Group.<wbr/>code.<wbr/>text</td><td>Is StudyArm.type a string ?</td></tr>
<tr><td>Arm eligibility group description</td><td>StudyArm.<wbr/>description</td><td>Group.<wbr/>extension:description</td><td colspan="2">Group.<wbr/>description</td><td></td></tr>
</tbody>
</table>
</div>

### studyCohort

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Cohort name</td><td>studyCohort.<wbr/>label</td><td>ResearchStudy.<wbr/>arm.<wbr/>name</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>name</td><td>Cohort are not described in the Group ?</td></tr>
<tr><td>Cohort description</td><td>studyCohort.<wbr/>description</td><td>ResearchStudy.<wbr/>arm.<wbr/>description</td><td colspan="2">ResearchStudy.<wbr/>comparisonGroup.<wbr/>description</td><td></td></tr>
</tbody>
</table>
</div>

### StudySite

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>location reference</td><td>StudySite.<wbr/>id</td><td colspan="3">ResearchStudy.<wbr/>site</td><td></td></tr>
<tr><td>location id</td><td>StudySite.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">Location.<wbr/>id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>location identifier</td><td>StudySite.<wbr/>id</td><td colspan="3">Location.<wbr/>identifier.<wbr/>value</td><td></td></tr>
<tr><td>site name</td><td>StudySite.<wbr/>label</td><td colspan="3">Location.<wbr/>name</td><td></td></tr>
<tr><td>site type</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"code": "DX", "display": "Diagnostics or therapeutics unit", "system": "http://terminology.hl7.org/CodeSystem/v3-RoleCode"}</code></span></td><td colspan="3">Location.<wbr/>type.<wbr/>coding</td><td></td></tr>
<tr><td>site country</td><td>StudySite.<wbr/>country</td><td colspan="3">Location.<wbr/>address.<wbr/>country</td><td></td></tr>
</tbody>
</table>
</div>

### Address

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>site city</td><td>Address.<wbr/>city</td><td colspan="3">Location.<wbr/>address.<wbr/>city</td><td></td></tr>
<tr><td>site state</td><td>Address.<wbr/>state</td><td colspan="3">Location.<wbr/>address.<wbr/>state</td><td></td></tr>
<tr><td>site postal code</td><td>Address.<wbr/>postalCode</td><td colspan="3">Location.<wbr/>address.<wbr/>postalCode</td><td></td></tr>
<tr><td>Reference to group of criteria</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"reference": "#eligibility-criteria", "type":"Group"}</code> (for id "eligibility-criteria")</span></td><td>ResearchStudy.<wbr/>enrollment</td><td colspan="2">ResearchStudy.<wbr/>recruitment.<wbr/>eligibility</td><td>This element in R4 is enrollment</td></tr>
</tbody>
</table>
</div>

### EligibilityCriterionItem

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Eligibility criteria text</td><td style="background-color: #ffff99;">EligibilityCriterionItem.<wbr/>to-be-specified</td><td>Group.<wbr/>characteristic.<wbr/>extension:description</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>description</td><td>Where do you get this data from? Do you really need this row?</td></tr>
<tr><td>Eligibility criteria code</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"Defined by CodeableConcept"</code></span></td><td colspan="3">Group.<wbr/>characteristic.<wbr/>code.<wbr/>text</td><td>Not clear what it means: hardcoded value "Defined by CodeableConcept".</td></tr>
<tr><td>Eligibility criteria valueCodeableConcept text</td><td>EligibilityCriterionItem.<wbr/>text</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>valueCodeableConcept.<wbr/>text</td><td>Could not this be the Eligibility criteria text?</td></tr>
</tbody>
</table>
</div>

### EligibilityCriterion

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Exclusion criterion true/false?</td><td>EligibilityCriterion.<wbr/>category</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>exclude</td><td></td></tr>
</tbody>
</table>
</div>

### Extension

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td style="background-color: #ffd8a8;">Group references</td><td style="background-color: #ffd8a8;">Extension.<wbr/>to-be-specified</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueReference.<wbr/>reference</td><td style="background-color: #ffd8a8;">It should be right .. But to be sure that it refers to a Group that full fill a specific caracthersitic. Which characteristic code is used for the valueReference? How is it used?</td></tr>
</tbody>
</table>
</div>

### ExpectedResponse

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Node reference indication</td><td>ExpectedResponse.<wbr/>atTiming</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueReference.<wbr/>type</td><td>Please clarify which kind of code (characteristic.code) is used to distinguish among all these different kinds of characteristics (range, code, quantity, reference, ...).</td></tr>
<tr><td>expected response range - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange</td><td></td></tr>
<tr><td>Expected response value code - direct</td><td>ExpectedResponse.<wbr/>codes</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueCodeableConcept.<wbr/>coding</td><td></td></tr>
<tr><td>expected response quantity - single response - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity</td><td></td></tr>
<tr><td>Group timing range - direct</td><td>ExpectedResponse.<wbr/>atTiming</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>extension:relativeTime.<wbr/>extension:offsetRange.<wbr/>valueRange</td><td>Group.<wbr/>characteristic.<wbr/>relativeTime.<wbr/>offsetRange</td><td></td></tr>
<tr><td>Group timing context - direct</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>extension:relativeTime.<wbr/>extension:contextCode.<wbr/>valueCodeableConcept.<wbr/>coding</td><td>Group.<wbr/>characteristic.<wbr/>relativeTime.<wbr/>contextCode.<wbr/>coding</td><td></td></tr>
<tr><td>expected response min value unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>code</td><td></td></tr>
<tr><td>expected response min value unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response min value is inclusive (flag, removed by fhir_version.py) - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>isInclusive</td><td></td></tr>
<tr><td>expected response max value unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>code</td><td></td></tr>
<tr><td>expected response max value unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response max value is inclusive (flag, removed by fhir_version.py) - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>isInclusive</td><td></td></tr>
<tr><td>expected response unit code (UCUM, from standardCodeAliases) - direct</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>code</td><td></td></tr>
<tr><td>expected response unit standard code (NCI, moved to an extension by fhir_version.py) - direct</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>eligibility criteria subgroup referenced id</td><td>ExpectedResponse.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>eligibility criteria - response combination method</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td>Group.<wbr/>extension:combinationMethod</td><td colspan="2">Group.<wbr/>combinationMethod</td><td>Not able to find this element in R4 or R5 Group. To be decided: in GroupReadi the READI extension group-combinationMethod is a modifierExtension (modifierExtension:combinationMethod); shall it stay a modifierExtension, as it is now, or become an extension?</td></tr>
<tr><td>expected response label (set to "Node" for combinations)</td><td>ExpectedResponse.<wbr/>label</td><td>Group.<wbr/>extension:description</td><td colspan="2">Group.<wbr/>description</td><td>Not sure to have understood what is about</td></tr>
<tr><td>expected response range</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange</td><td></td></tr>
<tr><td>expected response description - node</td><td>ExpectedResponse.<wbr/>description</td><td>Group.<wbr/>characteristic.<wbr/>extension:description</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>description</td><td></td></tr>
<tr><td>Expected response value code - via nodes</td><td>ExpectedResponse.<wbr/>codes</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueCodeableConcept.<wbr/>coding</td><td></td></tr>
<tr><td>expected response quantity response - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity</td><td></td></tr>
<tr><td>Group timing range - node</td><td>ExpectedResponse.<wbr/>atTiming</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>extension:relativeTime.<wbr/>extension:offsetRange.<wbr/>valueRange</td><td>Group.<wbr/>characteristic.<wbr/>relativeTime.<wbr/>offsetRange</td><td></td></tr>
<tr><td>Group timing context - nodes</td><td>ExpectedResponse.<wbr/>atTiming</td><td colspan="2">Group.<wbr/>characteristic.<wbr/>extension:relativeTime.<wbr/>extension:contextCode.<wbr/>valueCodeableConcept.<wbr/>coding</td><td>Group.<wbr/>characteristic.<wbr/>relativeTime.<wbr/>contextCode.<wbr/>coding</td><td></td></tr>
<tr><td>Exclusion criterion true or false?</td><td>ExpectedResponse.<wbr/>category</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>exclude</td><td></td></tr>
<tr><td>expected response min value unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>code</td><td></td></tr>
<tr><td>expected response min value unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response min value is inclusive (flag, removed by fhir_version.py) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>low.<wbr/>isInclusive</td><td></td></tr>
<tr><td>expected response max value unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>code</td><td></td></tr>
<tr><td>expected response max value unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
<tr><td>expected response max value is inclusive (flag, removed by fhir_version.py) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueRange.<wbr/>high.<wbr/>isInclusive</td><td></td></tr>
<tr><td>expected response unit code (UCUM, from standardCodeAliases) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td colspan="3" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>code</td><td></td></tr>
<tr><td>expected response unit standard code (NCI, moved to an extension by fhir_version.py) - via nodes</td><td>ExpectedResponse.<wbr/>value</td><td style="background-color: #ffb3b3;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>extension:quantity-translation.<wbr/>valueQuantity</td><td colspan="2" style="background-color: #ffd8a8;">Group.<wbr/>characteristic.<wbr/>valueQuantity.<wbr/>standardCode</td><td>Not the right extension: use the standard extension instead of the local READI quantity-cdisc-unit (e.g. the core extension iso21090-PQ-translation).</td></tr>
</tbody>
</table>
</div>

### BiomedicalConcept

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Loinc Code of assessment - direct</td><td>BiomedicalConcept.<wbr/>code</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>code.<wbr/>coding</td><td></td></tr>
<tr><td>Loinc Code of assessment</td><td>BiomedicalConcept.<wbr/>code</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>code.<wbr/>coding</td><td>Not sure about its meaning..</td></tr>
</tbody>
</table>
</div>

### ExpResponseNode

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>sub-node reference (nested Group) - via nodes</td><td>ExpResponseNode.<wbr/>childArray</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>valueReference.<wbr/>reference</td><td></td></tr>
<tr><td>sub-node reference type - via nodes</td><td>ExpResponseNode.<wbr/>childArray</td><td colspan="3">Group.<wbr/>characteristic.<wbr/>valueReference.<wbr/>type</td><td></td></tr>
<tr><td>Evidence variable id</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3" style="background-color: #ffd8a8;">EvidenceVariable.<wbr/>id</td><td>Is not an identifier (the id of the resource can change when you move the resource around…)</td></tr>
<tr><td>Evidence variable name</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3">EvidenceVariable.<wbr/>name</td><td></td></tr>
<tr><td>Evidence variable status</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3">EvidenceVariable.<wbr/>status</td><td></td></tr>
<tr><td>Evidence variable title</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3">EvidenceVariable.<wbr/>title</td><td></td></tr>
<tr><td>Evidence variable description</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3">EvidenceVariable.<wbr/>description</td><td></td></tr>
<tr><td>Evidence classifier (note that questionnaires should get another code / not taken care of yet)</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified</td><td colspan="3">EvidenceVariable.<wbr/>classifier</td><td>Not able to find it in R4 or R5; This has been introdcued in R6</td></tr>
</tbody>
</table>
</div>

### StudyRole

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Design masking (masked roles → SEVCO blinding codes)</td><td>StudyRole.<wbr/>masking</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
<tr><td>Associated party name — lead-sponsor (organization label)</td><td>StudyRole.<wbr/>label</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>name</td><td></td></tr>
<tr><td>Associated party name — co-sponsor (organization label)</td><td>StudyRole.<wbr/>label</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>name</td><td></td></tr>
<tr><td>Associated party reference (points to contained PractitionerRole)</td><td>StudyRole.<wbr/>id</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>party.<wbr/>reference</td><td></td></tr>
<tr><td>Associated party reference type</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"PractitionerRole"</code> (only when code.code = "EXT0003")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>party.<wbr/>type</td><td></td></tr>
<tr><td>Contained PractitionerRole id</td><td>StudyRole.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">PractitionerRole.<wbr/>id</td><td></td></tr>
<tr><td>Contained PractitionerRole organization display (role label)</td><td>StudyRole.<wbr/>label</td><td colspan="3">PractitionerRole.<wbr/>organization.<wbr/>display</td><td></td></tr>
<tr><td>Associated party reference — primary-investigator (points to contained PractitionerRole)</td><td>StudyRole.<wbr/>id</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>party.<wbr/>reference</td><td></td></tr>
<tr><td>Associated party reference type — primary-investigator</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"PractitionerRole"</code> (only when code.code = "C19924")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>party.<wbr/>type</td><td></td></tr>
<tr><td>Contained PractitionerRole id — primary-investigator</td><td>StudyRole.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">PractitionerRole.<wbr/>id</td><td></td></tr>
<tr><td>Contained PractitionerRole organization display — primary-investigator (role label)</td><td>StudyRole.<wbr/>label</td><td colspan="3">PractitionerRole.<wbr/>organization.<wbr/>display</td><td></td></tr>
<tr><td>Associated party name — collaborator (organization label)</td><td>StudyRole.<wbr/>label</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>name</td><td></td></tr>
</tbody>
</table>
</div>

### StudyVersion

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Study Design masking (open label — no masked role found)</td><td>StudyVersion.<wbr/>roles</td><td colspan="3">ResearchStudy.<wbr/>studyDesign</td><td></td></tr>
</tbody>
</table>
</div>

### Code

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Associated party role code — lead-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party role display — lead-sponsor</td><td>Code.<wbr/>decode</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role system — lead-sponsor</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C70793")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party organization type system — lead-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party organization type code — lead-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party organization type display — lead-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role code — co-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party role display — co-sponsor</td><td>Code.<wbr/>decode</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role system — co-sponsor</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C215669")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party organization type system — co-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party organization type code — co-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party organization type display — co-sponsor</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>classifier.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role code</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party role display</td><td>Code.<wbr/>decode</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role system</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "EXT0003")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party role code — primary-investigator</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party role display — primary-investigator</td><td>Code.<wbr/>decode</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role system — primary-investigator</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "C19924")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>system</td><td></td></tr>
<tr><td>Associated party role code — collaborator</td><td>Code.<wbr/>code</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>code</td><td></td></tr>
<tr><td>Associated party role display — collaborator</td><td>Code.<wbr/>decode</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>display</td><td></td></tr>
<tr><td>Associated party role system — collaborator</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/research-study-party-role"</code> (only when code.code = "EXT0004")</span></td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>role.<wbr/>coding.<wbr/>system</td><td></td></tr>
</tbody>
</table>
</div>

### AssignedPerson

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Associated party name (assigned person)</td><td>AssignedPerson.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>name</td><td></td></tr>
<tr><td>Contained PractitionerRole code text (assigned person job title)</td><td>AssignedPerson.<wbr/>jobTitle</td><td colspan="3">PractitionerRole.<wbr/>code.<wbr/>text</td><td></td></tr>
<tr><td>Contained PractitionerRole practitioner display (assigned person name)</td><td>AssignedPerson.<wbr/>text</td><td colspan="3">PractitionerRole.<wbr/>practitioner.<wbr/>display</td><td></td></tr>
<tr><td>Associated party name — primary-investigator (assigned person)</td><td>AssignedPerson.<wbr/>text</td><td colspan="3">ResearchStudy.<wbr/>associatedParty.<wbr/>name</td><td></td></tr>
<tr><td>Contained PractitionerRole code text — primary-investigator (job title)</td><td>AssignedPerson.<wbr/>jobTitle</td><td colspan="3">PractitionerRole.<wbr/>code.<wbr/>text</td><td></td></tr>
<tr><td>Contained PractitionerRole practitioner display — primary-investigator (assigned person name)</td><td>AssignedPerson.<wbr/>text</td><td colspan="3">PractitionerRole.<wbr/>practitioner.<wbr/>display</td><td></td></tr>
</tbody>
</table>
</div>

### StudyIntervention

<div class="mapping-scroll">
<table class="grid">
<colgroup><col class="c-item"/><col class="c-usdm"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-fhir"/><col class="c-notes"/></colgroup>
<thead>
<tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
<tr><th>R4</th><th>R5</th><th>R6</th></tr>
</thead>
<tbody>
<tr><td>Intervention evidence variable id</td><td>StudyIntervention.<wbr/>id</td><td colspan="3" style="background-color: #ffd8a8;">EvidenceVariable.<wbr/>id</td><td></td></tr>
<tr><td>Intervention evidence variable meta profile</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"http://hl7.org/fhir/uv/ebm/StructureDefinition/variable-definition"</code></span></td><td colspan="3">EvidenceVariable.<wbr/>meta.<wbr/>profile</td><td></td></tr>
<tr><td>Intervention evidence variable name</td><td>StudyIntervention.<wbr/>label</td><td colspan="3">EvidenceVariable.<wbr/>name</td><td></td></tr>
<tr><td>Intervention evidence variable title</td><td>StudyIntervention.<wbr/>label</td><td colspan="3">EvidenceVariable.<wbr/>title</td><td></td></tr>
<tr><td>Intervention evidence variable status</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>"active"</code></span></td><td colspan="3">EvidenceVariable.<wbr/>status</td><td></td></tr>
<tr><td>Intervention evidence variable handling (boolean variable)</td><td style="background-color: #ffff99;">to-be-specified.<wbr/>to-be-specified<br/><span style="background-color: #e6f4e6;">hardcoded value: <code>{"coding": { "code": "STATO:0000724", "system": "https://fevir.net/sevco", "display": "boolean variable" }}</code></span></td><td>EvidenceVariable.<wbr/>type</td><td colspan="2">EvidenceVariable.<wbr/>handling</td><td></td></tr>
<tr><td>Intervention evidence variable classifier (intervention type)</td><td>StudyIntervention.<wbr/>type</td><td colspan="3">EvidenceVariable.<wbr/>classifier</td><td></td></tr>
<tr><td>Intervention evidence variable description</td><td>StudyIntervention.<wbr/>description</td><td colspan="3">EvidenceVariable.<wbr/>description</td><td></td></tr>
</tbody>
</table>
</div>
