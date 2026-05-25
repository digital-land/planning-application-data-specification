# Scraping and extraction documentation: 2011/0734

## Source application

We found an existing application on Hackney Council's planning site:
[Hackney planning application 2011/0734](https://developmentandhousing.hackney.gov.uk/planning/index.html?fa=getApplication&id=21998)

The application reference used in the extraction is `2011/0734`.

We downloaded the completed application form from the planning site and copied it to:

`data/analysis/applications/2011_0734/sources/application_form.pdf`

The source PDF is a scanned 20-page document.

## Application type

We determined that the completed form is for `Outline Planning Permission with Some Matters Reserved`.

The application type reference used for the submission specification is:

`outline-some`

We cross-checked the expected data modules by running:

```bash
python spec.py inspect application outline-some
```

This returned 30 expected modules. We compared those modules with the visible sections in the completed form and recorded the status of each module in `extraction-report.md`.

## Section extraction order

We processed the main form sections in form order:

1. Applicant details and applicant contact details.
2. Agent details and agent contact details.
3. Proposal details.
4. Site details.
5. Pre-application advice.
6. Access, rights of way, waste storage and conflict of interest.
7. Materials and vehicle parking.
8. Foul sewage, flood risk, biodiversity/geological/archaeological conservation, existing use, trees and trade effluent.
9. Residential units and non-residential floorspace.
10. Employment, hours of operation, site area, processes/machinery/waste and hazardous substances.
11. Site visit details, ownership certificates and declaration.
12. Attached owner-list pages.
13. Portal document-list screenshot.

For each section, we checked the relevant module and field definitions under `specification/module/`, `specification/field/` and `specification/component/`, then created one JSON file per module.

## Interpretation and generated values

Some values had to be interpreted to fit the current specification.

- We generated stable person references such as `applicant-1` and `agent-1` so contact, conflict and declaration sections could link to the relevant person.
- We normalised visible dates to `YYYY-MM-DD`.
- We represented visibly blank scalar values as empty strings, and visibly absent repeated values as empty arrays.
- We preserved important form annotations in top-level module `notes` fields where the current module did not have a clear field for the content.
- We mapped legacy use-class labels such as `A1`, `A5`, `B1(a)`, `D1` and `D2` to current structured fields as far as possible, while retaining the historic labels in `specified-use` or `additional-properties`.
- We represented the legacy `4+` bedroom column as `no-of-bedrooms: 4`, and flagged it for human review.
- We treated `bng` and `checklist` as blocked modules because the current specification expects them, but the 2011 form does not visibly include matching sections.
- Where the current specification warrants a document reference but the form does not provide one, we may generate or retain a stable placeholder-style reference so links between sections can be tested. These generated or unresolved references are flagged in `extraction-report.md`.

## Owner-list extraction

Certificate B says to see the attached list. The owner-list attachment pages are rotated in the source PDF.

We used OCR on the rotated pages and checked the page images visually. We then populated `ownership-certs.owners-and-tenants` with 95 notified-person entries.

The owner-list transcription is OCR-assisted and should be checked by a human before final use. Names, dates and postcodes are the main risk areas.

## Document-list extraction

We created `documents.json` from the visible rows in the planning access site document list.

The standalone file includes all visible documents, including documents whose visible type is `Additional Information (Submitted By Applicants)`.

Each document entry has:

- `reference`
- `name`
- `description`
- `document-types`
- `uploaded-date`
- `file`

Those fields match the specification. We added an additional field:

- `provision_source`

to capture whether the document was provided on submission or later.

We classified rows as follows:

- `Additional Information (Submitted By Applicants)` rows are `additional-request`.
- All other visible document rows are `submission`.

The document list extraction produced:

| Classification | Count | Use |
| --- | ---: | --- |
| `submission` | 72 | Included in `submission-details.documents`. |
| `additional-request` | 12 | Kept in `documents.json`, excluded from `submission-details.documents`. |
| Total visible rows | 84 | Preserved in `documents.json`. |

When recreating `submission.json`, we include only documents with `provision_source: submission`. We remove `provision_source` from `submission-details.documents`, because it is extraction metadata rather than submitted application data.

## Supporting-document cross-check

After creating the document list, we cross-checked existing `supporting-documents.reference` values in module JSON files against document references and names using:

```bash
python .codex/skills/submission-data-extractor/scripts/check_document_references.py \
  --application-dir data/analysis/applications/2011_0734
```

The `materials` module uses `Design Code` as a supporting-document reference. The document list includes a document named `SD2_PT2_0.0_1.0 INTRODUCTION (THE DESIGN CODE)`, so we changed that document's `reference` to `Design Code`.

Other references remain unresolved or partial matches:

- `Regulatory Plan - 009`
- `P, D&A Statement`
- `P, D&A Statements including illustrative masterplan drawings`
- `Development Specification`

Those have been left as extracted from the form and flagged for human review in `extraction-report.md`.

## Output files

The main output files are:

- `extraction-report.md`
- `submission-details.json`
- `documents.json`
- `additional-properties.json`
- one JSON file per expected module
- `submission.json`

`submission.json` is assembled from the module JSON files, `submission-details.json` and `additional-properties.json`.

## Known risks and review points

- Some current-specification fields do not exist on the legacy 2011 form, so blanks, generated references or notes are used to preserve structure without inventing unsupported facts.
- The completed form contains some handwritten annotations, where they field an expected field we have included them, where they don't we've included the text in a `notes` field in the applicable module so that it is preserved.
- Some document references in the form are descriptive rather than exact document-list references.
- Some portal documents are classified as `additional-request` from the visible portal document type, but the webpage alone does not prove the timing or request history behind each document.
