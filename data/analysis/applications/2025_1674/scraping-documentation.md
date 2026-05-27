# Scraping documentation: 2025/1674

## Source

- Planning authority: Hackney
- Application reference: `2025/1674`
- Planning Portal reference: `PP-14191823`
- Source form: `sources/application_form.pdf`
- Associated document list: user-provided screenshot in the Codex conversation

## Application type

The form title is `Application for Planning Permission; Listed Building Consent for alterations, extension or demolition of a listed building`.

The inferrence is its a combined application type `full;lbc`, which resolves to 36 expected modules.


## Document list handling

The document list was transcribed from the public access document view. It includes visible document names, portal document types and dates. The site shows Download buttons, but not direct download URLs or file bytes, so extracted document records do not include base64 content and have blank `file.url` values.

Every row in `documents.json` has `provision_source`:

- `submission`: 27 rows, treated as submitted with the application and copied into `submission-details.documents`
- `additional-request`: 18 rows, kept in `documents.json` but excluded from the assembled submission payload
- `planning-authority`: 2 rows, `DNF-Full Planning Granted Final` and `Officer Report`, kept in `documents.json` but excluded from the assembled submission payload

The classification rule for this pass was: 2025-07-24 rows are treated as original submission documents; later applicant-supplied drawing/document rows are treated as `additional-request`; authority-created decision and officer report rows are treated as `planning-authority`.

## Generated and normalised values

- `site-area.site-area-in-hectares` was converted from 169.10 square metres to 0.01691 hectares (TO CHECK).
- `submission-details.application-types` is `["full", "lbc"]`.
- Dates from the form and document list were normalised to ISO dates where full dates were available.
- Document references were generated from visible names or aligned to visible drawing numbers where the site showed them directly.
- `documents.json.provision_source` controls which documents are copied into the assembled submission payload.
- GLA-specific planning questions were preserved under `additional-properties.gla-planning-data` where no clear module field was available.

## Cross-checks

The document-reference cross-check script was run after creating `documents.json`. Supporting-document references in `foul-sewage` and `materials` resolved to document references in `documents.json`.

For `lb-alter`, the applicant's drawing references from the form are preserved as the extracted values. The visible document-list directly supports only some of those references, so unresolved references are kept as review points rather than replaced with inferred portal-document slugs.

## Review risks

- The document-list may not include all available documents (TO FOLLOW UP).
- Download URLs and base64 file content are absent because they were not available.
- Several document names are generic or generated, for example `A:906 1`, so document type mappings need human review.
- Some drawing references in the form are grouped or partially different from the visible document-list names. `lb-alter.json` preserves the form references and does not force all of them to portal-document names.
- The extraction includes blank or note-bearing module files where the combined specification expects a module but the PDF does not expose a clear corresponding section.
