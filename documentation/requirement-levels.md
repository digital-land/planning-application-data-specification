# Required fields and requirement levels

The specifications use two mechanisms because they answer different questions:

- submission specifications use `required` and `required-if` as structural validation rules for a submission payload; and
- planning application datasets and publication views use `requirement-level` to express whether information `MUST`, `SHOULD` or `MAY` be recorded or published.

A submission rule determines whether the payload contains the information required by that submission specification. It does not determine whether the planning application is legally valid. A requirement level expresses a broader recording or publication expectation, including cases where information should normally be provided but may legitimately be unavailable or inapplicable.

The two mechanisms do not appear on the same field usage.

The rationale for this approach is recorded in [Decision 0022: Use requirement levels for recorded and published planning application data](design-decisions/0022-use-requirement-levels-for-recorded-and-published-data.md).

| Part of the specification | Mechanism | What it tells you |
|---|---|---|
| Submission application, module or component | `required` and `required-if` | Whether a field must be present in an acceptable submission |
| Planning application dataset | `requirement-level` | How strongly an authority is expected to record the field |
| Publication view | `requirement-level` | How strongly an authority is expected to publish the field in that view |

## Contents

- [Required fields in submission specifications](#required-fields-in-submission-specifications)
- [Requirement levels for recorded and published data](#requirement-levels-for-recorded-and-published-data)
- [How requirement levels relate to other data model concepts](#how-requirement-levels-relate-to-other-data-model-concepts)
- [Missing levels during the transition](#missing-levels-during-the-transition)
- [Authoring requirement levels](#authoring-requirement-levels)
- [Example: `site.name`](#example-sitename)

## Required fields in submission specifications

Submission specifications use `required` and `required-if` because a submitting service needs to know which information is necessary for an acceptable application.

### Always required

```yaml
- field: reference
  required: true
```

`required: true` means the field must be present in the submitted application. If it is absent, the submission does not conform to the specification.

### Required in stated circumstances

```yaml
- field: is-discharging-part
  required: true
- field: discharging-part-details
  required-if:
    - field: is-discharging-part
      value: true
```

In the [`part-discharge` module](../specification/module/part-discharge.schema.md), `is-discharging-part` is always required. `discharging-part-details` is required only when the applicant says they are discharging part of a condition. If the condition is not met, that field is not required by this rule.

### Optional in a submission

If neither `required` nor `required-if` is present, the submission structure does not require the field.

Submission field usages do not use `requirement-level`.

## Requirement levels for recorded and published data

Planning application datasets and publication views use requirement levels because a simple required-or-optional choice is not precise enough.

An authority may be expected to provide information in most cases even though a meaningful value does not exist, does not apply or cannot reasonably be obtained in every case. Treating such a field as mandatory can encourage invented values, duplicated information or placeholders. Treating it as entirely optional can weaken a valuable expectation and make avoidable omissions appear acceptable.

Requirement levels distinguish information that must be provided, information that should normally be provided and information that is genuinely optional.

### The requirement levels

| Level | What it means | What happens when the information is missing |
|---|---|---|
| `MUST` | You have to provide the information when the field applies. | The data does not conform to the requirement. This is an error. |
| `SHOULD` | You should provide the information wherever reasonably possible. You may omit it where there is a valid reason. | The omission does not automatically make the record invalid. It may be reported so the publisher can review it. |
| `MAY` | You can provide the information, but it is genuinely optional. | The omission is acceptable and does not produce an error or warning. |

`SHOULD` does not mean that a field is unimportant. It establishes a clear expectation while recognising that omission can be legitimate in particular circumstances.

Dataset and publication-view field usages do not use `required`.

### Requirement levels in datasets

A dataset requirement level says how strongly an authority is expected to record the field as part of its planning application data.

For example:

```yaml
- field: reference
  requirement-level: MUST
```

An application reference must be recorded because the application cannot otherwise be identified or linked reliably to its decisions, documents and events.

```yaml
- field: name
  requirement-level: SHOULD
```

A site name should be recorded where a meaningful name exists, but an authority should not invent one for an ordinary property that is already adequately identified by its address.

### Requirement levels in publication views

A publication view states how strongly an authority is expected to publish each included field for the needs served by that view.

The view makes its own decision. It does not inherit a requirement level automatically from the underlying dataset.

For example, `site.name` can be `SHOULD` in both the `site` dataset and the National Public View. These are separate requirements:

- the dataset says that a meaningful site name should be recorded; and
- the National Public View says that a meaningful recorded site name should normally be published.

A field could instead be `MUST` in an underlying dataset but `MAY`, or not included, in an open view. Recording information does not automatically mean it should be published openly.

---

## How requirement levels relate to other data model concepts

`requirement-level` only tells us how strongly information is expected to be recorded or published. It does not tell us whether the field applies to a particular record, whether it is included in a dataset or view, or how many values it can contain.

Those questions are handled by other parts of the specification. Keeping them separate prevents us using `MUST`, `SHOULD` or `MAY` to express several different rules at once.

| Concept | What it tells you |
|---|---|
| `required: true` | A field must be present in a submission. |
| `required-if` | A field must be present in a submission when a stated condition is met. |
| `requirement-level` | How strongly a field must be recorded or published. |
| Applicability | Whether the field is relevant to a particular record. |
| Inclusion in a dataset or view | Whether the field forms part of that dataset or output. |
| Cardinality | How many values the field can contain. |

### Requirement level and applicability

A `MUST` field that does not apply to a record should not require an invented value.

This specification does not yet define general conditional applicability rules for datasets and views. Add a rule later where a specific field needs one that can be tested from the data. Where applicability depends on judgement, field-usage guidance should explain when omission is legitimate.

For `site.name`, the specification uses `SHOULD` rather than a mechanical condition because deciding whether a site has a meaningful name requires judgement.

### Requirement level and inclusion

Listing a field in a dataset or view means it forms part of that structure. Inclusion alone does not state whether the field must be populated.

- included and `MUST`: provide it when applicable;
- included and `SHOULD`: normally provide it, but a justified omission is possible;
- included and `MAY`: provide it optionally; and
- not included: it is not part of that dataset or view.

### Requirement level and cardinality

Cardinality states how many values a field can contain.

- cardinality `1` means one value at most;
- cardinality `n` means the field can contain multiple values.

Cardinality does not say whether any value must be supplied. A field can have cardinality `1` and requirement level `MAY`, or cardinality `n` and requirement level `MUST`.

## Missing levels during the transition

Requirement levels will be added to existing dataset and view field usages progressively.

Until that work is complete:

- an absent level continues to behave like an optional field so existing data does not unexpectedly fail;
- the specification viewer shows `Not specified`; and
- an absent level is not presented as `MAY`, because `MAY` records a deliberate decision that the field is genuinely optional.

## Authoring requirement levels

When setting a level for a dataset or view field usage:

1. Identify the need served by the field in that particular dataset or view.
2. Decide whether the output can work reliably without the information.
3. Use `MUST` where the information is necessary and omission would prevent conformance with the need.
4. Use `SHOULD` where the information has clear value but a meaningful value may not exist, may not apply or may legitimately be unavailable.
5. Use `MAY` only where omission is acceptable without explanation.
6. State the level independently at every dataset and view layer. Do not assume inheritance.
7. Add field-usage guidance where implementers need to understand when a `SHOULD` value may be omitted.

## Example: `site.name`

`site.name` is `SHOULD` in both the `site` dataset and the National Public View.

Provide a short name where the site has a meaningful established or descriptive name, such as:

- `Former St Anne's Hospital`; or
- `Land north of High Street`.

Do not use `site.name` as another identifier and do not repeat the full address merely to populate it. It may be omitted where an ordinary address adequately identifies the site and there is no separate meaningful site name.

The following are not site names:

- the site record reference;
- a UPRN; or
- the complete postal address copied from `address-text`.
