Extension: ResearchStudyArmTargetNumber
Id: researchStudy-arm-targetNumber
Title: "ResearchStudy Arm Target Number"
Description: "Estimated number of participants to be enrolled in the arm (or cohort) of the study. It pre-adopts the FHIR R6 ResearchStudy.comparisonGroup.targetNumber element, not available in FHIR R4 or R5."
Context: ResearchStudy.arm
* insert SetFmmAndStatusRule (0, draft)
* value[x] only unsignedInt
* valueUnsignedInt 1..
* valueUnsignedInt ^requirements = "USDM: studyCohort.plannedEnrollmentNumber"
