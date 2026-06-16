## Decision: Keep form generation details separate from structured data

**Date:** 2026-05-21  
**Status:** Proposed

**Context:**  

The planning application specification is used to describe the structured data expected from a planning application submission.

The same schema information may also support validation, HTML form generation, generated PDFs and API contracts. These uses need a shared understanding of the submission structure, but they do not all need the same presentation controls.

For example, a paper form may need a "not applicable" box for each possible option because a blank box is ambiguous on paper. In structured data, absence of a repeated item can sometimes be a clear enough signal that the item does not apply, provided the specification says so.

This is related to [ADR 0013: When to use explicit not applicable fields](0013-when-to-use-explicit-not-applicable-fields.md), but the question here is broader: whether form-generation needs should drive the canonical data model.

**Decision:**  

The specification should model the structured data outcome first.

Form-generation metadata, hints and structures should be kept separate from the canonical data model unless they describe information that must be captured as submission data.

Generated HTML, PDF or paper forms may include controls, labels or layout structures that are not themselves fields in the canonical submission data model. Those output-specific details should sit in a form-generation layer or mapping.

**Consequences:**  

- Where absence of data means "not applicable", the relevant module or component should say so explicitly.
- A field should remain in the data model where the applicant's explicit answer is itself needed to interpret the submission.
- Form-generation tooling may render the same data model differently for HTML, generated PDF and paper outputs.

**Alternatives considered:**  

- Model every form-generation control as submission data -> rejected because it mixes presentation mechanics with the canonical data model and can add unnecessary burden.
- Exclude all form-generation considerations from this repository -> rejected for now because the specification still needs to explain enough for consistent implementation.
