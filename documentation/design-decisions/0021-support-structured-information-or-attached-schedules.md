## Decision: Support structured information or attached schedules

**Date:** 2026-08-27  
**Status:** Proposed

**Context:**  
Planning application forms sometimes allow applicants to provide structured information directly on the form or refer to an attached document containing the same information. Applicants commonly respond with wording such as "see attached schedule" rather than transcribing a long list.

The supporting information section of the reserved matters form asks for:

- drawings approved as part of the original decision, including drawing names and reference numbers
- drawing numbers submitted with the reserved matters application
- reasons for changes to the original drawings, where applicable

Hackney applications `2012/2584` and `20/00482/REM` provide examples of applicants referring to attached decision notices or drawing schedules instead of entering the drawing lists on the form. The extracted submission for `2012/2584` also shows that the current `replacement-drawings` structure cannot represent this response faithfully.

The current model assumes one-to-one relationships between old and new drawings. The form does not establish that every submitted drawing replaces one approved drawing, and the approved and submitted drawing sets may contain different numbers of entries.

**Decision:**  
The `supporting-info` module will support two alternative ways of providing the section:

- references to an attached decision notice and submitted drawing schedule
- structured approved drawing details and submitted drawing references

Applicants must use one route for the whole section. They must not mix the two routes or be required to provide both representations.

The attached-document route is:

```json
"supporting-info": {
  "approved-drawings-document": {
    "reference": "abc"
  },
  "submitted-drawings-document": {
    "reference": "xyz"
  }
}
```

The structured route is:

```json
"supporting-info": {
  "approved-drawings": [
    {
      "reference": "abc",
      "name": "A title"
    }
  ],
  "submitted-drawing-references": [
    "abc",
    "thsh",
    "ths"
  ]
}
```

Reciprocal `required-if` co-constraints using `operator: empty` will make both structured fields required when the document route is empty, and make both document fields required when the structured route is empty. Module rules will prevent fields from the two routes being mixed.

An attached decision notice or drawing schedule must be included in `submission-details.documents` using the existing `document` component. Its `reference` must be stable and unique within the submission, and its `name` must be a concise human-readable title describing the uploaded document. Suitable examples are:

- reference `doc-approved-drawings`, name `Outline decision notice and approved drawings schedule`
- reference `doc-submitted-drawings`, name `Submitted drawings schedule`

These reference values are illustrative. Submitting systems remain responsible for generating unique document references.

The `supporting-info` module will refer to these documents using the existing `supporting-document` component. It will store only the document `reference`; it will not repeat the document name, description or file metadata.

The attached-document route will only be introduced where application evidence shows that the form and application process already allow the information to be supplied in an attachment. This decision does not generally allow structured questions to be replaced by arbitrary documents.

The existing `replacement-drawings`, `replacement-drawing`, `old-drawing-reference` and `new-drawing-reference` elements will be deleted when the module is migrated. They are not used by another source module and describe a replacement relationship that is not supported by the form evidence. Their examples and extracted test data will be updated at the same time. Generated outputs will be refreshed through the normal generation workflow.

**Rationale:**  
Supporting both routes reflects how applicants already complete these forms while preserving structured data where it is supplied directly. Referencing an uploaded schedule avoids unnecessary transcription and keeps the application record complete and stable.

Using the existing `document` and `supporting-document` components follows the established single document-reference pattern. It keeps document metadata in one place and gives modules a consistent way to identify supporting files.

Separating approved and submitted drawing information avoids inventing one-to-one replacement relationships. Requiring one complete route for the section also prevents partially structured payloads that would be difficult to interpret consistently.

**Consequences:**  

- New fields are needed for `approved-drawings`, `submitted-drawing-references`, `approved-drawings-document` and `submitted-drawings-document`.
- The `supporting-info` module will use reciprocal `empty` co-constraints and exclusivity rules.
- JSON Schema generation will need support for `operator: empty` before the alternative routes can be represented accurately in generated schemas.
- Uploaded schedules and decision notices must appear in `submission-details.documents` and contain complete file metadata.
- Integration examples must use document references that resolve to documents in the same payload.
- The reserved matters example based on Hackney `2012/2584` must be updated to use the new model.

**Alternatives considered:**  

- Require structured drawing lists only -> rejected because real applications show that applicants are permitted to provide the information in attached schedules or decision notices.
- Accept attached schedules only -> rejected because it would remove structured information where applicants provide drawing details directly.
- Require both structured lists and attached schedules -> rejected because it duplicates applicant effort and creates two potentially inconsistent representations.
- Retain `replacement-drawings` -> rejected because the form requests two independent drawing sets and does not establish one-to-one replacement relationships.
