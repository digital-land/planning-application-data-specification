---
# Using names in datasets

In general, datasets should include names for the things that people need to recognise. A name:

- makes an item easier for a person to identify;
- gives services a meaningful label to show on a screen; and
- helps people use a consistent term when discussing an item or entity.

This need is captured in [data-need-002](../user-needs/need/data-need-002.md): entities should be identifiable in plain language, without relying on technical references alone.

`reference` and `name` do different jobs. A reference identifies a record reliably for systems and relationships. A name is the human-readable label that services show when people need to recognise, choose or discuss that record.

[Justification just-0017](../user-needs/justification/just-0017.md) records the general intention to provide names, while noting that its current rule is too broad for relationship and event datasets.

## Rules of thumb

- Always use the `reference` to link records. Never use a name as an identifier or join key.
- Give a record a `name` when a person needs to recognise, select, search for or discuss the thing represented by the row.
- A name may change as the accepted or customary way of referring to the thing changes. Its reference remains stable. For example, application `206/1393/FUL` may initially be displayed as `206/1393/FUL` and later as `The old brewery site`.
- Where there is no useful plain-language label, repeat the reference as the name. This is preferable to inventing a label or leaving a display label unavailable.
- Do not copy a related record's name into a join or event record merely for display. A service should resolve the referenced record and display its current name. This avoids conflicting copies.
- Add a name to a relationship record only when the relationship is a recognisable thing in its own right, which users need to distinguish from other relationships. In that case the name describes the relationship, not either linked record.

Names are labels, not evidence of identity. They can be duplicated, changed, abbreviated or misspelt. The related decision on named people makes the same point for submission data: [link named individuals by reference](design-decisions/0014-link-named-individuals-by-reference.md).

## Examples for the decision-stage datasets

Where a dataset normally derives a display label, the examples below are labels a service could show, rather than values to store in a `name` field.

| Dataset | Possible name or display label |
| --- | --- |
| `planning-application` | `The old brewery site`<br>`206/1393/FUL` |
| `site` | `The old brewery site`<br>`Former Brown's Brewery` |
| `planning-application-document` | `Proposed plans, revision B`<br>`Design and access statement` |
| `decision-notice` | `206/1393/FUL — granted 14 May 2026`<br>`Decision notice for the old brewery site` |
| `section-106` | `Section 106 agreement for the old brewery site`<br>`S106/2026/042` |
| `planning-condition` | `Materials approval`<br>`Approved plans` |


## Designing and maintaining names

Use a short, intelligible label rather than a full description. Keep the full text, rationale or document contents in their appropriate fields.

When a name changes, update the label without changing the reference or any relationships to the record. If previous names are needed for search, audit or legal interpretation, model them explicitly as aliases with their own dates and source. Do not overload the single current `name` field to carry a history.

