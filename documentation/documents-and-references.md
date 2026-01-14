---
title: Documents and references
---

## Core model

- `application.documents` is the single source of truth for uploaded files. It uses the `document` component with:
  - `reference` (required, unique per application)
  - `name` (required)
  - `description` (optional)
  - `document-types` (required; codelist-driven categorisation)
  - `uploaded-date` (required)
  - `file` (required; see file component)

## Referencing documents in modules

- Modules should only collect references to existing `application.documents`, not duplicate document metadata (name/description).
- Reference component: `supporting-document` (used for both plans/drawings and other supporting material) and it only carries a required `reference`.
- Use the `supporting-documents` field wherever a list of document references is needed. The older `plans-documents` field/component is deprecated.
- Rules in modules must ensure every referenced `reference` exists in `application.documents`. Use the pattern: `each document in <field> must have a reference that matches a document in application.documents`.
- Avoid collecting additional names in modules; the display name comes from the document list.

## Replacement flow

- Use the `replacement-document` component (fields: `old-document`, `new-document`) for substitutions.
- Validation should ensure:
  - `old-document` and `new-document` are provided and differ.
  - Both references exist in `application.documents` (new documents must be in the submitted list).

## Validation expectations

- `reference` values in `application.documents` must be unique and stable for the submission.
- Module-level checks cover:
  - Presence (e.g. at least one plan in `supporting-documents` where required).
  - Cross-reference to `application.documents`.
- Do not repeat name/description validation in referencing fields; rely on `application.documents` for those.

## Example flow

1. Applicant uploads documents, populating `application.documents` with reference/name/description/document-types/uploaded-date/file.
2. Module fields (e.g. `supporting-documents`) capture only the `reference` for the relevant items.
3. Validation checks that the referenced documents exist and that any module-specific presence rules are met. Replace documents (if applicable) via `replacement-documents` using `old-document`/`new-document` references.
