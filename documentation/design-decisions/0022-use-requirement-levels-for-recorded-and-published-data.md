## Decision: Use requirement levels for recorded and published planning application data

**Date:** 2026-09-02
**Status:** Proposed

### Context

The submission specification currently uses `required: true` and `required-if` on field usages. These rules tell a submission service when a field is absolutely necessary and whether an application can be accepted without it.

When `required` is absent, the field is currently treated as optional. This is implicit and does not distinguish between:

- information that must be provided;
- information that should be provided wherever reasonably possible; and
- information that is genuinely optional.

The planning application data specification and publication views need this distinction. They describe information an authority records through the planning process and information it publishes for particular uses. Whether information can legitimately be omitted may depend on whether the fact exists, whether it applies to the record, whether it can reasonably be obtained and whether it is appropriate for the particular view.

This nuance matters because treating every included field as mandatory would reject legitimate records or encourage invented, duplicated or placeholder values. Treating every field without `required: true` as equally optional would make the specification unclear and weaken expectations for useful data that should normally be provided.

Different layers also serve different needs. A field may be important in the authority's planning application record but excluded from an open view. A view may place a strong publication requirement on a field where it is necessary for that view to work. Requirement levels must therefore be stated for the particular field usage rather than inherited from the canonical field or another specification layer.

### Decision

Use separate mechanisms for submission requiredness and for the strength of requirements in planning application datasets and publication views.

#### Submission specifications

Submission application, module and component field usages will continue to use:

- `required: true` where a field is always necessary for an acceptable submission; and
- `required-if` where a field is necessary when a stated condition applies.

An absent `required` attribute means the field is not structurally required by that submission usage.

Submission field usages will not use `requirement-level`.

#### Planning application datasets and publication views

Dataset and view field usages will use `requirement-level` with one of these values:

| Level | Plain-English meaning | Conformance consequence |
|---|---|---|
| `MUST` | This information has to be provided. | Missing information is a conformance error. |
| `SHOULD` | Provide this information wherever reasonably possible. It may be omitted where there is a valid reason. | Missing information does not automatically make the record invalid. It may be reported so the publisher can review the omission. |
| `MAY` | This information is genuinely optional. | Missing information has no conformance consequence. |

Dataset and view field usages will not use `required`.

`requirement-level` states the strength of the requirement. It does not state whether the field applies to a particular record. Applicability and requirement strength are separate concepts. This decision does not introduce conditional applicability rules for datasets or views. Add those later only where a specific field needs a rule that can be tested from the data.

The repository will define the controlled `MUST`, `SHOULD` and `MAY` values locally. Their meanings will remain consistent with their ordinary use in standards, while the project documentation will define how they apply to this specification.

#### Requirements are specific to each layer

Each dataset and view will state its own requirement level based on the need it serves.

- A dataset requirement describes what an authority is expected to record.
- A National Public View requirement describes what it is expected to publish in that view.
- Another view may set a different level for the same field because it serves a different need.

Levels will not inherit silently between datasets and views. Identical levels at different layers are separate, explicit decisions.

#### Transition

Existing dataset and view field usages do not yet have requirement levels. During backfilling:

- an absent `requirement-level` will continue to have the same conformance effect as an optional field;
- the specification viewer will display `Not specified`, not `MAY`; and
- only an explicit `MAY` will mean that genuine optionality has been considered and decided.

### Rationale

Keeping `required` for submissions gives submission services a direct rule for determining whether an application contains information that is absolutely necessary. It also retains the existing structured mechanism for conditional submission questions.

Using requirement levels for datasets and views makes their expectations explicit. `MUST`, `SHOULD` and `MAY` communicate distinctions that a boolean cannot represent, while their conformance consequences allow future checking and reporting even where the specification does not generate JSON Schema.

Keeping the mechanisms in separate contexts avoids two attributes making the same claim on one field usage. It also keeps the language appropriate to the different tasks: accepting a submitted application, maintaining a planning application record and publishing a defined view of that record.

Stating levels independently at each layer prevents an implementation from assuming that information collected or held must automatically be made public. It also prevents a weaker publication requirement from changing what should be held in the underlying planning application record.

### Consequences

- The repository must define a local controlled requirement-level vocabulary containing `MUST`, `SHOULD` and `MAY`.
- Dataset and view field-usage models must support `requirement-level`.
- Integrity checks must reject unrecognised levels and the use of `required` in dataset or view field usages.
- Integrity checks must reject `requirement-level` in submission field usages.
- The specification viewer and other generated outputs must show the requirement level for each usage.
- Missing levels must be shown as `Not specified` during the transition.
- Documentation must explain the difference between submission requiredness, requirement level, applicability, inclusion and cardinality.
- Checking actual planning application data against the levels is not part of the first implementation. Future checking can treat missing `MUST` data as an error, report missing `SHOULD` data for review and accept missing `MAY` data.
- Each dataset and view will need its field usages reviewed and backfilled deliberately.

### Initial application to `site.name`

Set `site.name` to `SHOULD` independently in:

- the `site` dataset, because a meaningful name should normally be recorded where one exists; and
- the National Public View, because a meaningful recorded name should normally be published to help people recognise and discuss the site.

Separate field-usage guidance will explain that publishers must not invent a site name or duplicate the full address merely to populate the field. Omission is legitimate where no meaningful site name exists.

### Alternatives considered

- Continue treating absence of `required: true` as optional everywhere -> rejected because it cannot distinguish expected information from genuinely optional information.
- Use `required` throughout all specifications -> rejected because a boolean cannot express `SHOULD` and would overload a submission acceptance rule with recording and publication policy.
- Use `requirement-level` alongside `required` in submission specifications -> rejected because it would create two mechanisms expressing the strength of the same submission requirement and allow contradictory combinations.
- Define one requirement level on the canonical field and inherit it everywhere -> rejected because requiredness depends on the use of the field and the needs served by the dataset or view.
- Treat missing levels as explicit `MAY` during migration -> rejected because this would make an incomplete backfill appear to be a deliberate decision.

### Not included in this decision

- A general mechanism for conditional applicability in datasets and views. Add one later only where a concrete field requires it.
- A requirement for publishers to record or submit a formal explanation whenever a `SHOULD` field is omitted.
- Tooling that checks actual planning application data against requirement levels.
- Generating JSON Schema or another machine-readable conformance schema for planning application datasets and publication views.
