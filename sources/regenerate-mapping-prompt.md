# Prompt to regenerate the USDM to FHIR mapping page

Copy the text below into a Claude Code chat opened in this repository to rebuild
`input/pagecontent/usdm2fhir-mapping.md` from `sources/USDM2FHIR-GC-notes.xlsx`.

---

Read the Excel file `sources/USDM2FHIR-GC-notes.xlsx`, sheet "USDM2FHIR map", columns
"USDM class", "USDM attribute", "FHIR resourceType" and "FHIR path", and (re)write the page
`input/pagecontent/usdm2fhir-mapping.md` following these rules:

1. Skip rows where all four columns are empty.
2. Each row becomes a line in a two-column table:
   - first column "USDM class.attribute" = `<USDM class>.<USDM attribute>`
   - second column "FHIR resourceType.path" = `<FHIR resourceType>.<FHIR path>`
3. If "USDM attribute" is empty, use `to-be-specified` as attribute.
   If "USDM class" is empty, use `to-be-specified` as class (giving `to-be-specified.to-be-specified`
   when both are empty).
4. Organize the page per USDM class: one `## <USDM class>` section per class, each with its own table,
   sections ordered by the first appearance of the class in the sheet. All rows of the same class
   (exact name, even if not contiguous in the sheet) go in the same table, in sheet order.
5. Rows with an empty "USDM class" are added to the table of the class of the previous row in the sheet.
6. Keep the values as they are in the sheet (no case normalization, no de-duplication).
7. Start the page with the heading `# USDM to FHIR mapping`.

Report the number of rows per class and the total.
