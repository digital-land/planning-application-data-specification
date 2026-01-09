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

4. Rule (general requirement)

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
