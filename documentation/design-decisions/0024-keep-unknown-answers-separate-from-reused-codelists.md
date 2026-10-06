## Decision: Keep unknown answers separate from reused codelists

**Date:** 2026-10-06  
**Status:** Proposed

**Context:**

The specification reuses codelists maintained elsewhere. For example, the listed-building-grade codelist refers to an external dataset of listed building grades.

An applicant may not know which value applies. We need to record that answer without adding `unknown` to the source dataset or maintaining a separate copy of it. An unanswered question must not be treated as an explicit answer of “I don't know”.

**Decision:**

Keep externally maintained codelists unchanged. Where the specification needs an explicit unknown answer, record it in a separate field.

This preserves the meaning of the source dataset and lets the specification describe uncertainty separately.

For listed building grade, use a boolean flag to record that the grade is unknown. The applicant must supply either a valid grade or the unknown flag set to `true`. They must not supply both. Omitting both is not a valid answer where this information is required.

The module uses the boolean field `listed-building-grade-unknown` with `fixed-value: true`.

```json
{
  "listed-building-grade-unknown": true
}
```

When the applicant supplies a grade from the codelist, they must omit the unknown flag. 
A flag set to `false` alone does not answer the question.

| Grade | Unknown flag | Result |
| --- | --- | --- |
| Valid codelist value | Absent | Valid |
| Absent | `true` | Valid |
| Present | `true` | Invalid: contradictory answers |
| Absent | Absent | Invalid: unanswered |
| Absent | `false` | Invalid: no grade supplied |
| Present | `false` | Not the chosen representation: omit the flag when supplying a grade |

These requirements apply when the grade question is required. They do not make the module mandatory for application types that do not require it.

**Conditional rules:**

The module must state the requirement to supply exactly one of the two answers. Validation must check both completeness and contradictions.

The [co-constraint guidance](../co-constraints.md) now includes `operator: empty` under `applies-if`. Each answer applies only when the other is empty or missing and is required when in scope. Conditions are evaluated against the original payload, before requiredness. Supplied empty values must still satisfy the field constraints; they are not an alternative answer.

The unknown flag has `fixed-value: true`. This requires the supplied value to be the boolean `true`; it does not supply a default or make the field required by itself. See [module field attributes](../module.md).

The package exposes these constraints without evaluating submitted answers. JSON Schema generation is deferred and tracked in [issue #420](https://github.com/digital-land/planning-application-data-specification/issues/420). Until that work is complete, generated schemas do not fully enforce this pattern.

**Other answers outside a codelist:**

The same principle applies when an answer does not belong in the reused source dataset: model the additional information separately in the specification.

This does not prevent adding a meaningful answer to a codelist maintained by this specification. The [affected-area-type codelist](../../specification/codelist/affected-area-type.schema.md) includes `no` ("No likely impact") alongside the two affected locations. The [biodiversity, geological and archaeological conservation module](../../specification/module/bio-geo-arch-con.schema.md) needs each assessment to distinguish no likely impact from an impact at either location. Because we own that codelist, adding the answer there keeps the required fields and their validation consistent without introducing separate flags. `no` is an explicit assessment, not an unknown answer or a missing value.

However, “other” and “unknown” are different. An unknown flag does not represent a known value missing from a codelist. If a future requirement needs an “other” answer, define how to capture that value or its description and when it is allowed. This decision does not introduce a generic reason field or allow arbitrary values in the grade field.

**Interface design:**

The specification defines the submitted data and the rules it must meet. Software providers decide how to present the question and capture the answer. They could show grades and “I don't know” as choices within one question, then map the answer to the appropriate field.

This follows [ADR 0016: Keep form generation details separate from structured data](0016-keep-form-generation-details-separate-from-structured-data.md), which is currently marked Proposed. Separate data fields do not require separate questions or controls on screen.

**Consequences:**

- The source codelist remains reusable without local additions for submission-specific answers.
- Consumers can distinguish a supplied grade, an explicitly unknown grade and an unanswered question.
- Suppliers must apply the rule across both fields when validating submissions.
- Each use of this pattern must define its permitted combinations and whether an answer is required.
- This decision does not prevent adding needed answers to codelists owned by this specification, or changing those where `unknown` is already an intentional permitted answer, such as the pattern in [ADR 0001](0001-use-enum-for-yes-no-unknown.md).

**Alternatives considered:**

- Add `unknown` to the external codelist: would mix submission uncertainty with the source dataset's actual values and depend on its maintainer accepting the change.
- Maintain a local extended copy: would create another list to keep aligned with the source.
- Allow an extra string through prose alone: would leave the codelist and machine-readable validation incomplete.
- Infer unknown from a missing grade: would confuse an explicit answer with an unanswered question.
- Require a true/false unknown flag for every answer: fits the value-based `applies-if` pattern, but adds a redundant flag when the grade itself is supplied.
