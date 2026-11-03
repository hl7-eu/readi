Extension: QuantityCdiscUnit
Id: quantity-cdisc-unit
Title: "Quantity CDISC Unit"
Description: "The unit of a Quantity as a CDISC Controlled Terminology concept (system http://www.cdisc.org), for units that cannot be expressed in UCUM."
Context: Quantity
* insert SetFmmAndStatusRule (0, draft)
* value[x] only Coding
* valueCoding 1..
* valueCoding.system = "http://www.cdisc.org" (exactly)
* valueCoding.code 1..
* valueCoding ^requirements = "USDM: ExpectedResponse.value"
