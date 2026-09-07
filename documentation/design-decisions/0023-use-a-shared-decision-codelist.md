## Decision: Use a shared decision codelist

**Date:** 2026-09-07
**Status:** Proposed

### Context

The decision outcome and formal planning officer recommendation were free-text fields. Different values for the same outcome make it harder to compare recommendations with decisions. Supplier feedback also showed that the recommendation's purpose needed clarification.

### Decision

Use one [decision codelist](../../data/codelist/decision.csv) for `decision-notice.decision` and `decision-notice.planning-officer-recommendation`. Its initial values are `grant` and `refuse`.

The recommendation records the formal recommendation presented to the planning committee. Omit it where no such recommendation exists, including where one has not yet been made. Do not use an empty string or placeholder values such as `pending`, `none` or `not-applicable`.

### Rationale

Sharing the vocabulary allows users to compare the recommended outcome with the final outcome without translating between different lists.

A grant with conditions is still a grant. Related condition records identify the conditions imposed, so a separate `grant-with-conditions` value would duplicate information.

`defer` concerns postponing consideration rather than granting or refusing the application. It is not included in this outcome codelist.

Withdrawal is a separate fact about the application. Its representation is outside this decision and must not be introduced as a decision outcome simply because a source system stores it alongside decisions.

This distinction is also reflected in [national planning application statistics](https://www.gov.uk/government/statistics/planning-applications-in-england-january-to-march-2026/planning-applications-in-england-january-to-march-2026-statistical-release), which account separately for decisions made and applications withdrawn when reporting applications remaining on hand.

### Consequences

- Both fields use datatype `enum` and reference the same codelist.
- Guidance and examples use `grant` and `refuse` consistently.
- Publishers map equivalent local outcome labels to these values.
- The initial list can be extended where evidenced application outcomes require it. It is not a claim that all possible outcomes have already been modelled.

Related work: [issue 341](https://github.com/digital-land/planning-data-design/issues/341).
