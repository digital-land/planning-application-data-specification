## Decision: Link named individuals by reference, not name matching

**Date:** 2026-05-19  
**Status:** Proposed

**Context:**  

Some current forms need to identify which applicant, agent or named person a statement relates to.

The current forms often do this by asking the user to provide a name.

We had modelled this in the specification by adding a name field and a rule that the name must match a name already provided elsewhere in the application. Examples include:

- `specification/module/declaration.schema.md`, where `name` must match one of the named individuals in the application
- `specification/module/conflict-of-interest.schema.md`, where `conflict-person-name` must match a name provided in applicants or agent sections

This is risky in a structured digital submission. Names are not stable identifiers. They can be duplicated, formatted differently, misspelt or changed between sections. Matching free text also pushes interpretation work onto receiving systems.

Generated PDF or paper forms may still need to show a name box because the user is completing a human-readable form. That is a presentation and capture concern.

**Decision:**  

Where the specification needs to link something to an applicant, agent or person already provided in the submission, it should use a reference to that record.

The specification should not rely on matching a free-text name to identify a person where a structured reference can be used.

Where a generated PDF or paper form captures a name, that text should be treated as display or paper-capture text. The authoritative structured link should still be the person, applicant or agent reference.

**Rationale:**  

Using references:

- avoids ambiguous matches where two people share the same or similar names
- avoids drift between a repeated name and the original applicant or agent details
- gives receiving systems a clearer validation rule because the referenced record either exists or does not
- keeps the data model focused on structured relationships rather than presentation text
- supports both digital services and generated paper/PDF forms without forcing them to use the same user interface

**Consequences:**  

- Form-generation tooling may need a way to know when a referenced person should be rendered as a name box in PDF/paper outputs.
- Where a legacy or paper-facing name field is retained, documentation should be clear that it is not the authoritative link between records.

**Where this pattern is used:**  

- Declaration: identify who made the declaration using a person, applicant or agent reference.
- Conflict of interest: identify who has the conflict using a person, applicant or agent reference rather than name matching.
- Ownership certificates: identify who made the certificate declaration using a person, applicant or agent reference.

**Alternatives considered:**  

- Match on free-text names -> rejected because it is ambiguous and creates work for implementers and receiving systems.
- Concatenate title, first name and last name -> rejected because it creates derived text, can drift from the source record and does not solve identity matching.
- Repeat the full person object in each module -> rejected because it duplicates data and creates the same drift problem in a larger form.
- Leave matching to implementers -> rejected because it would create inconsistent interpretation across services and LPAs.
