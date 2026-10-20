Profile: LocationReadi
Parent: Location
Id: location-readi
Title: "Location (READI)"
Description: "This profile describes a site (facility) where a clinical study is conducted for the scope of the READI project. It is derived from the USDM StudySite."
* insert SetFmmAndStatusRule (0, draft)
* . ^short = "READI study site"
* . ^definition = "A site (facility) where a clinical study is conducted, derived from a USDM StudySite."
* id ^short = "Logical id of the site (USDM StudySite.id)"
* id ^comment = "The USDM to FHIR transformation sets it to the StudySite.id, used also to reference the site from ResearchStudy.site."
* name 1..
  * ^short = "Name of the site (USDM StudySite.label)"
* type ^short = "Type of site"
* type ^comment = "The USDM to FHIR transformation currently sets a fixed \"location\" value: a code from the extensible ServiceDeliveryLocationRoleType value set (or another agreed code) is still to be specified."
* address ^short = "Address of the site"
* address.country ^short = "Country of the site (USDM StudySite.country)"
* address.country ^comment = "ISO 3166 2 or 3 letter code (USDM StudySite.country.code)."
* position ^short = "Geographical coordinates of the site"
// ---- USDM requirements (generated from usdm2fhir-mapping.md) ----
* id ^requirements = "USDM: to-be-specified.to-be-specified"
* name ^requirements = "USDM: StudySite.label"
* type ^requirements = "USDM: to-be-specified.to-be-specified"
* address.country ^requirements = "USDM: StudySite.country"
