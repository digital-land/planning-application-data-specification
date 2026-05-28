# Needs and justifications

This folder separates what problem we are trying to solve from how the specification solves it.

•	Needs describe user or system problems in plain English.
•	Justifications explain why particular datasets or fields exist, by showing how they help meet one or more needs.

This keeps the specification focused on what data is required, while making the rationale explicit and reviewable.

## User needs

A need is a stable statement of a problem to be solved.

Needs:
	•	are written from the perspective of a user (for example a data consumer)
	•	describe outcomes, not solutions
	•	do not reference specific datasets or fields
	•	may overlap with other needs during discovery

Each need is stored as a single file in needs/ and given a unique ID.

---

## Justifications

Justifications

A justification records a claim that one or more elements of the specification help satisfy a need.

Justifications:
	•	link a need to concrete parts of the specification
	•	may reference a dataset, a field, or a combination of elements
	•	are separate from the specification itself
	•	can be proposed, reviewed, accepted, or retired

A single need may have multiple justifications.

#### What justifications are not

Justifications are:
	•	not implementation instructions
	•	not validation rules
	•	not guarantees of completeness

They exist to make the reasoning behind the specification visible and open to challenge.

---
### Ways a need can be justified

Justifications support a small number of clear patterns.

1. Single element (leaf)

A need is satisfied by a single dataset or field.

```
satisfied_by:
  dataset: decision-notice
  field: reference
```

Use this when one element on its own enables the user to meet the need.

2. Combination (allOf)

A need is satisfied only when multiple elements exist together.

```
satisfied_by:
  allOf:
    - dataset: decision-notice
      field: reference
    - dataset: decision-notice
      field: decision-date
```

Use this when the user cannot complete their task unless all listed elements are present.

3. Alternative ways (anyOf)

A need can be satisfied in more than one way.

```
satisfied_by:
  anyOf:
    - dataset: site
      field: uprn
    - dataset: site
      field: geometry
```

Use this sparingly. It is most useful where:
	•	legacy and new approaches coexist
	•	different producers support different capabilities

4. Combination with codelist requirements

Sometimes a need is only satisfied when a field exists **and** a specific value, or set of values, exists in a codelist.

Use this for controlled codelists where the values define standard reportable states, events, categories, obligations or decisions that affect public transparency, statutory or process accountability, validation, routing, eligibility or cross-authority comparison.

This is not required for every value in every codelist. It is for codelists where changing the vocabulary changes what the specification can recognise, compare or explain. For example, `permission-process-event` values define the planning process events that can be recorded consistently across authorities.

```
satisfied_by:
  allOf:
    - dataset: planning-permission-timeline
      field: permission-process-event
      codelist: permission-process-event
      includes:
        - found-invalid
    - dataset: planning-permission-timeline
      field: event-date

notes: >
  Need is met when the timeline can record that an application was found
  invalid and when that happened.
```

The codelist value is not justified in isolation. The justification should name the consuming dataset and field, plus enough companion fields to make the value useful. For timeline events, `event-date` is usually essential.

Use `includes` consistently, even for a single value. `includes` means these values must exist in the codelist vocabulary. It does not mean that a single data record must contain all those values at once.

A justification record should justify the need, not the codelist row. If one value satisfies the need, include one value. If the need requires a set of values, include the set. For example, a need to understand a consultation window may require both `consultation-start` and `consultation-end`.

The body of the justification should explain what would be lost if the value was absent from the controlled vocabulary.

Do not write needs that simply restate the existence of the code. A need must identify a real user task, policy or process accountability point, statutory milestone, interoperability requirement, or repeated cross-authority reporting use.

Use the existing `status`, `satisfaction` and `confidence` fields for these records. Use `satisfaction: partial` where the codelist value is useful but the current model does not fully meet the need.

If a need changes, review all justification records that refer to that need. That review may lead to model or codelist changes.

Codelist CSV columns such as `need` are convenience text for community review, not the canonical source of rationale. The canonical traceability belongs in `user-needs/justification/`. If a codelist has a `notes` property, it may say that the codelist is treated as a controlled codelist whose values should be justified through these records.

5. Rule (general requirement)

Some needs apply across many parts of the specification.

In these cases, a justification may record a rule rather than a specific instance.

```
satisfied_by:
  rule:
    applies_to: dataset
    requires:
      - field: reference
```

Rules express design intent or expectations (for example, “all datasets should have a reference”).
They do not assert that the rule is currently met everywhere.

Coverage and conformance can be checked separately.

---

## Reviewing and evolving needs

Needs and justifications are expected to evolve.
	•	Similar or overlapping needs may be merged or split over time.
	•	Justifications may change as the specification develops.
	•	Fields or datasets without an accepted justification should be reviewed.

This approach helps ensure the planning system becomes more data-rich for clear, documented reasons, not by accident.
