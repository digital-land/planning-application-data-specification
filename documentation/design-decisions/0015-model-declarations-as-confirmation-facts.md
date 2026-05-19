## Decision: Model declarations as confirmation facts, not digital signatures

**Date:** 2026-05-19  
**Status:** draft  

**Context:**  

Some legacy forms ask for a “digital signature” from the applicant or agent. In the current specification this appears in places such as the ownership certificates module as `applicant-signature` and `agent-signature` string fields.

This creates ambiguity. A “digital signature” could mean:

- a typed name shown in a signature box
- a formal electronic signature
- a cryptographic signature
- a declaration or confirmation action by a known person

For the planning application specification, the core need is usually not to capture a cryptographic signature. It is to know who made a declaration or confirmation, what they confirmed and when they did it.

This decision builds on [Decision: Link named individuals by reference, not name matching](./0014-link-named-individuals-by-reference.md). That linked decision covers the first part of the pattern: how to identify the applicant, agent or person who made the declaration. This decision covers the declaration or confirmation facts and how they should be presented.

The way this is presented can vary by output:

- digital HTML form: checkbox, confirmation button or declaration page
- generated PDF/paper form: signature-style box or name/date area

The data model should not force one presentation pattern.

**Decision:**  

We will model declarations and confirmations as:

- **who made it:** a reference to the person, applicant or agent record, following the named-individual reference pattern
- **what they confirmed:** an explicit boolean or event/action field
- **when they confirmed it:** a date or timestamp where needed

We will not model legacy “digital signature” fields as concatenated name strings unless there is a specific legal or policy requirement to capture a literal signature text.

Presentation is handled by form generation, not by the core data model. The same model may render as a checkbox or declaration page in HTML and as a signature-style box in a generated PDF or paper form.

**Rationale:**  

The identity-linking part of this pattern follows [Decision: Link named individuals by reference, not name matching](./0014-link-named-individuals-by-reference.md). The declaration pattern then records the explicit act of confirmation by that referenced person.

Using an explicit confirmation field:

- records the applicant or agent’s affirmative action
- supports validation rules such as `declaration-confirmed must be true`
- avoids relying on absence or inferred intent

Using a date or timestamp:

- records when the declaration or confirmation was made
- supports audit and submission review

**Consequences:**  

- Modules that contain declarations should use the same basic pattern rather than local signature strings.
- The model may need a way to record that a field group uses the declaration/confirmation pattern so generated forms can render it differently for digital and paper/PDF outputs.
- If that metadata is not added directly to the model now, the pattern should at least be recorded in documentation or a separate form-generation mapping.
- Modules that currently identify a declaring person by matching a name should be reviewed under the named-individual reference decision record.

**Where this pattern is used:**  

- `specification/module/declaration.schema.md`
- `specification/module/ownership-certs.schema.md`

**Alternatives considered:**  

- Keep `applicant-signature` and `agent-signature` as free text strings -> rejected because this duplicates person data and does not identify the signer robustly.
- Concatenate title, first name and last name -> rejected because it creates derived text, can drift from the source person record and adds no reliable evidence.
- Require formal electronic or cryptographic signatures -> rejected unless policy or legal advice says this is required, because it would add identity, security and implementation complexity beyond the current need.
- Leave this to each implementation -> rejected because it would create inconsistent payloads and make it harder to interpret declarations across services.
