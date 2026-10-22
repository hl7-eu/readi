# Prompt to regenerate the USDM to FHIR mapping page

Copy the text below into a Claude Code chat opened in this repository to rebuild
`input/pagecontent/usdm2fhir-mapping.md` from `sources/USDM2FHIR-GC-notes.xlsx`.

---

Read the Excel file `sources/USDM2FHIR-GC-notes.xlsx`, sheet "USDM2FHIR map", columns "Item",
"USDM class", "USDM attribute", "FHIR resourceType" and "FHIR path", plus the cell comments of each row,
and (re)write the page `input/pagecontent/usdm2fhir-mapping.md` following these rules.

### Rows and grouping

1. Skip rows where the four USDM and FHIR columns are all empty.
2. The Item of a row is the "Item" column, with white space (including line breaks) collapsed to single
   spaces. Several rows can share the same USDM value and FHIR path: the Item tells them apart (e.g.
   "Minimum Age text" and "Maximum Age text").
3. The USDM value of a row is `<USDM class>.<USDM attribute>`. If "USDM attribute" is empty, use
   `to-be-specified` as attribute. If "USDM class" is empty, use `to-be-specified` as class (giving
   `to-be-specified.to-be-specified` when both are empty).
4. The FHIR path of a row in the sheet is `<FHIR resourceType>.<FHIR path>`.
5. Organize the page per USDM class: one `### <USDM class>` section per class, each with its own table,
   sections ordered by the first appearance of the class in the sheet. All rows of the same class
   (exact name, even if not contiguous in the sheet) go in the same table, in sheet order.
6. Rows with an empty "USDM class" are added to the table of the class of the previous row in the sheet.
7. Keep the values as they are in the sheet (no case normalization, no de-duplication).

### FHIR version columns

The FHIR paths in the sheet are aligned to FHIR R6. Validate the paths against the core
StructureDefinitions in the local FHIR package cache (`~/.fhir/packages`): `hl7.fhir.r4.core#4.0.1`,
`hl7.fhir.r5.core#5.0.0`, and `hl7.fhir.r6.core` (if it is not in the cache, download the latest version
listed at `https://packages2.fhir.org/packages/hl7.fhir.r6.core` into a scratch directory; 6.0.0-snapshot1
was used last time). A path is valid when each step is an element of the resource, or of the datatype of
the previous element (choice elements as `value<Type>`, e.g. `valueReference`). Treat the `Group-all`
resourceType as `Group` when validating, but write it as `Group-all` in the page.

8. **R6** = the sheet path.
9. **R5** = the sheet path with these renames (longest prefix first), if valid in R5; otherwise `—`:
   - `ResearchStudy.objective.outcomeMeasure.endpoint` → `ResearchStudy.outcomeMeasure.reference`
   - `ResearchStudy.objective.outcomeMeasure` → `ResearchStudy.outcomeMeasure`
   - `ResearchStudy.purposeType` → `ResearchStudy.primaryPurposeType`
10. **R4** = the sheet path with these renames (longest prefix first), if valid in R4:
   - `ResearchStudy.purposeType` → `ResearchStudy.primaryPurposeType`
   - `ResearchStudy.comparisonGroup` → `ResearchStudy.arm`
   - `ResearchStudy.recruitment.eligibility` → `ResearchStudy.enrollment`

   Otherwise, if the R5 column has a path, the R5 element is pre-adopted in R4 through a cross-version
   extension: take the R5 path, keep the leading part valid in R4, and replace the first element not in R4
   with `extension:<element>`. Use the extension `ext-R5-<Resource>.<element>` of
   `hl7.fhir.uv.xver-r5.r4#0.1.0` for the rest of the path: when the next step is one of its
   sub-extensions write `.extension:<name>`. When the (sub-)extension reached has a single-type
   `value[x]`, always end with its value as `.value<Type>`, followed by the remaining steps if any. If no
   such extension exists in the package, append the remaining steps as they are. Examples:
   - `ResearchStudy.label.value` → `ResearchStudy.extension:label.extension:value.valueString`
   - `ResearchStudy.classifier` → `ResearchStudy.extension:classifier.valueCodeableConcept`
   - `ResearchStudy.progressStatus.actual` → `ResearchStudy.extension:progressStatus.extension:actual.valueBoolean`
   - `ResearchStudy.label.type.coding` → `ResearchStudy.extension:label.extension:type.valueCodeableConcept.coding`
   - `ResearchStudy.classifier.text` → `ResearchStudy.extension:classifier.valueCodeableConcept.text`
   - `Group.description` → `Group.extension:description` (no extension in the package)

   Otherwise (no R5 path either) use `—`.
11. If the sheet path is not valid in R6 either (e.g. `ResearchStudy.identifier.codeableConcept.text`),
    write it unchanged in all three columns.

### Notes column

12. Notes = the text of the cell comments on the row (any column), in column order. The comments are
    Excel threaded comments: drop the boilerplate up to and including `Commento:`, split the replies
    marked by `Rispondi:`, collapse white space, and join the parts with `; `. Keep the text as it is
    (no spelling fixes). Leave the cell empty when the row has no comments.

### Page layout

13. Do not add a page heading: the IG template already renders the page title (from `sushi-config.yaml`) as
    `h2`, and numbers the headings from it (`h2` = page number, `h3` = 2.1, 2.2, ...), so content headings
    start at `###`. Start the page with:

    ```html
    <div class="stu-note" markdown="1">
    This mapping is a work in progress: it has not been validated yet and may change at any time.
    </div>
    ```

14. Write each table in HTML (Markdown tables cannot merge cells), HTML-escaping the cell values:

    ```html
    <table class="grid" style="width: 90%;">
    <thead>
    <tr><th rowspan="2">Item</th><th rowspan="2">USDM class.attribute</th><th colspan="3">FHIR resourceType.path</th><th rowspan="2">Notes</th></tr>
    <tr><th>R4</th><th>R5</th><th>R6</th></tr>
    </thead>
    <tbody>
    <tr><td>item</td><td>USDM</td><td>R4</td><td>R5</td><td>R6</td><td>notes</td></tr>
    </tbody>
    </table>
    ```

15. Merge adjacent FHIR version cells with the same value (including `—`) into one cell with
    `colspan="2"` or `colspan="3"`: e.g. `<td colspan="3">ResearchStudy.condition.text</td>` when the path
    is the same in R4, R5 and R6, or `<td>—</td><td colspan="2">ResearchStudy.classifier</td>`.
16. Highlight with a yellow background (`style="background-color: #ffff99;"` on the `<td>`) the
    USDM and FHIR version cells whose value contains `to-be-specified` or is `—`, e.g.
    `<td style="background-color: #ffff99;">to-be-specified.to-be-specified</td>` or
    `<td colspan="2" style="background-color: #ffff99;">—</td>`.
17. Highlight with a yellow background all the cells of these rows (Item and Notes included), and use
    the given note instead of the cell comments:

    | FHIR path in the sheet | Note |
    |---|---|
    | `ResearchStudy.identifier.codeableConcept.text` | ResearchStudy.identifier has not a codeableConcept |

18. If the sheet has both the `PopulationDefinition` and the `StudyDesignPopulation` classes, add this
    info box right after the table of whichever of the two sections comes later on the page:

    ```html
    <div class="alert alert-info" markdown="1">
    PopulationDefinition and StudyDesignPopulation seem to contain the same kind of information: please check.
    </div>
    ```

Report the number of rows per class and the total, and list the rows whose R4 or R5 path differs from
the sheet path. To check the page without a full IG Publisher build, run `runJekyll.bat usdm2fhir-mapping`.
