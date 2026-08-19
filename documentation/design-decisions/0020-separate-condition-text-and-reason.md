## Decision: Record condition text and reason separately

**Date:** 2026-08-18  
**Status:** Proposed

### Context

Planning decision notices commonly present a condition as two related but distinct pieces of information:

- the condition text, which states what must be done or restricted; and
- the reason, which explains why the condition was imposed.

For example:

> The development must be carried out in accordance with the approved plans.
>
> **Reason:** For the avoidance of doubt and in the interests of proper planning.

Some planning systems store or render both parts in one text field. However, evidence shows that a combined source value may still contain a clearly labelled reason, often introduced by `Reason:`. This is an implementation characteristic and does not make the two pieces of information semantically equivalent.

This decision responds to [user need `dd-need-036`](../../user-needs/need/dd-need-036.md): applicants and developers need to see the reasons behind each condition so they can understand why it was imposed and how it relates to policy or the proposal. [Justification `just-0019`](../../user-needs/justification/just-0019.md) records how the current specification satisfies that need.

### Decision

Record the condition text and reason as separate data items.

The condition text records the requirement that must be met. The reason records the justification for imposing that condition. It does not record a reason for refusing the planning application.

### Rationale

Keeping the two values separate:

- answers two different questions: what is required, and why it is required;
- makes the justification for a condition visible and supports scrutiny of whether it is necessary, relevant, enforceable and reasonable;
- supports search and analysis of requirements and their policy or site-specific justifications independently;
- allows common condition wording to be compared or reused without assuming that its justification is identical in every case; and
- reflects the explicit condition-and-reason structure commonly presented in decision notices.

Both values may contain standard and case-specific material. Condition wording may include application-specific plans, dates or substitutions. A reason may use a standard rationale, cite local policy or explain a particular impact of the development. Separating them does not imply that one is always reusable and the other is always bespoke.

### Consequences

- Publishers should map a reliably labelled reason separately even where a source system stores condition text and reason together.
- Publishers should not copy the same combined text into both fields. If the boundary cannot be identified reliably, they should report the reason as unavailable rather than invent a split.
- The exact text and reason issued with a decision must remain recoverable as authoritative information.

### Alternatives considered

- Store condition text and reason as one value -> rejected because it combines the requirement with its justification, limiting reuse, scrutiny and analysis even when the source document clearly distinguishes them.
- Treat the reason as unstructured supporting documentation only -> rejected because reasons are routinely presented as part of the issued condition and have value as structured data.

### Unresolved questions

This decision establishes the semantic separation only. It does not settle whether either value should ultimately be held on `planning-condition`, `decision-condition` or another future representation of an imposed condition.

For now, `description` and `reason` remain on `planning-condition`. Further work will establish whether `planning-condition` represents a reusable clause or an exact condition as imposed through a particular decision, and whether the reason justifies a general clause or its use in that particular case.
