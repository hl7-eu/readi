Extension: ResearchStudyArmTargetNumber
Id: researchStudy-arm-targetNumber
Title: "ResearchStudy Comparison Group Target Number"
Description: "Estimated number of participants to be enrolled in the comparison group (arm or cohort) of the study. It pre-adopts the FHIR R6 ResearchStudy.comparisonGroup.targetNumber element, not available in FHIR R5."
Context: ResearchStudy.comparisonGroup
* insert SetFmmAndStatusRule (0, draft)
* value[x] only unsignedInt
* valueUnsignedInt 1..
* valueUnsignedInt ^requirements = "USDM: studyCohort.plannedEnrollmentNumber"

Extension: ResearchStudyArmEligibility
Id: researchStudy-arm-eligibility
Title: "ResearchStudy Comparison Group Eligibility"
Description: "Reference to the Group holding the eligibility criteria that apply to the comparison group (arm or cohort) of the study. It pre-adopts the FHIR R6 ResearchStudy.comparisonGroup.eligibility element, not available in FHIR R5."
Context: ResearchStudy.comparisonGroup
* insert SetFmmAndStatusRule (0, draft)
* value[x] only Reference(GroupReadi)
* valueReference 1..
* valueReference ^requirements = "USDM: StudyCohort.to-be-specified"
