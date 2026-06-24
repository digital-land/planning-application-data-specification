# Co-constraints

Co-constraints are conditional rules that say when a field applies or becomes required based on another value or context.

In the submission specification they are currently used in module and component field entries. They help make the specification explicit about conditional questions without relying only on prose notes.

## The principle

The specification should prefer explicit rules over implied meaning, so it is easier to review, implement and test.

If a condition affects whether a field is in scope or whether a response is required, it should be written as structured vocabulary where possible.

## Conditional intents

There are two main conditional intents.

| Intent | What it means | Current use |
| --- | --- | --- |
| `applies-if` | The field is in scope if the condition is satisfied. This usually means it should be presented to the user. | Currently used with `application-type`. |
| `required-if` | The field requires a response if the condition is satisfied. | Used for conditional requiredness based on answers or other values. |

At the moment, `applies-if` is used to say that a field only applies for one or more application types.

For example:

```yaml
- field: lbc-owners
  applies-if:
    application-type:
      in:
      - lbc
```

Most other conditional logic is expressed with `required-if`.

For example:

```yaml
fields:
- field: advice-sought
  required: true
- field: officer-name
  required-if:
  - field: advice-sought
    value: true
```

## Where conditions can point

A condition often refers to another field in the same module or component, but it does not have to.

Conditions can refer to values elsewhere in the submission where needed. Use an explicit path when the field is outside the current module.

For example:

```yaml
- field: contact-details
  required-if:
    - field: agent-details.agent.reference
      operator: not_empty
```

## Current condition patterns

These are the main patterns currently used.

| Pattern | Vocabulary | Meaning |
| --- | --- | --- |
| Field applies for an application type | `applies-if` + `application-type` + `in` | Field is in scope for one or more application types. |
| Answer equals a value | `required-if` + `field` + `value` | Field is required when another field has a specific value. |
| Answer is one of several values | `required-if` + `field` + `in` | Field is required when another field is one of a list of values. |
| Answer contains a value | `required-if` + `field` + `contains` | Field is required when a list or multi-value field contains a value. |
| Any condition is met | `required-if` + `any` | Field is required if at least one listed condition is satisfied. |
| All conditions are met | `required-if` + `all` | Field is required only if every listed condition is satisfied. |
| Unary operator check | `required-if` + `field` + `operator` | Field is required when a state check such as `empty` or `not_empty` is satisfied. |
| Literal comparison | `required-if` + `field` + `operator` + `value` | Field is required when another field compares with a literal value. |
| Field comparison | `required-if` + `field` + `operator` + `value-field` | Field is required when one field compares with another field. |

## Operators and operands

Operator conditions use the same flat condition structure as other `required-if`
conditions. The operator determines whether the condition needs a right-hand
operand.

- unary operators such as `empty` and `not_empty` do not take an operand
- binary operators take exactly one of `value` or `value-field`
- `value` contains a literal right-hand value
- `value-field` contains an explicit field path whose value is the right-hand value

For example, a field-to-field comparison is written as:

```yaml
- field: earlier-date-reason
  required-if:
    - field: pre-development-date
      operator: "<"
      value-field: submission-details.submitted-at
```

This means `earlier-date-reason` is required when `pre-development-date` is
less than `submission-details.submitted-at`.

The initial operator vocabulary used by submission co-constraints is:

| Operator | Type | Operand |
| --- | --- | --- |
| `empty` | Unary state check | None |
| `not_empty` | Unary state check | None |
| `<` | Binary comparison | Exactly one of `value` or `value-field` |

## Any and all

Use `any` and `all` when a rule depends on more than one condition.

- `any` means the field is required if at least one listed condition is met
- `all` means the field is required only if every listed condition is met

The specification should not rely on implied meaning when more than one condition is listed.

For example:

```yaml
fields:
- field: contamination-assessment
  required-if:
    - any:
      - field: is-contaminated-land
        value: true
      - field: is-suspected-contaminated-land
        value: true
      - field: proposed-use-contamination-risk
        value: true
```

And:

```yaml
fields:
- field: permission-not-obtained-details
  required-if:
    - all:
      - field: applicant-owns-land
        value: false
      - field: permission-obtained
        value: false
```

## Module, component and field scope

Application schemas decide which modules make up an application type. That is the composition layer of the specification.

Co-constraints are conditional rules inside that composition.

In practice:

- application schemas decide whether a module is part of an application type
- `applies-if` handles field-level variation when a shared module or component is used by multiple application types
- `required-if` handles answer-level logic once the relevant field or module is in scope

Whole modules are not currently put in or out of scope by an applicant answer. Instead, this is usually handled at field level. A module may include a leading question, and later fields in the same module become required only if the answer makes them relevant.

Components are represented through fields, so the same field-level rules can control when a component-shaped response is required.

## Open questions

This vocabulary is still being tightened.

Known open questions include:

- whether more complex conditions should eventually use a single expression language, such as JSONPath
- how much of the broader validation rule vocabulary should be formalised in the same way

These are future clean-up and tooling questions. The current direction is to keep the vocabulary minimal, explicit and testable.
