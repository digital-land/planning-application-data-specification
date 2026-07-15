## Decision: Do not duplicate dates across decision-stage datasets

**Date:** 2026-05-28  
**Status:** Proposed

### Context

The specification has datasets that record the main facts and characteristics about a planning application and its decision.

Some of those facts are dated events that change the application’s state. For example:

- `planning-application.received-date` records when the planning authority received the application and is when the statutory time period for a planning authority to validate an application begins
- `decision-notice.decision-date` records when the decision was made and decision notice issued, and carries legal significance

The specification also has `planning-permission-timeline`, which records dated events in the processing of a planning application.

There is some crossover here and a decision needs to be made about where to store certain dates.

If the same date is recorded both as a primary dataset field and as a timeline event, the specification duplicates the same fact in two places. That creates scope for conflicting values and uncertainty about which record is authoritative.

### Decision

Each fact has one canonical home. 

Keep a date on the dataset whose record it describes when it is a core property of that record. 

Use `planning-permission-timeline` for process events that need their own record, can recur or need event-specific context.

Do not store the same fact in both places.

### Rationale

Keeping core dates on the dataset that owns the record:

- means key state of the item can be understood using a single dataset. For example, any planning application record with a `withdrawn-date` can be considered withdrawn
- reduces the risk of the same date being recorded differently in two places
- keeps process events in the timeline and fundamental record properties on their owning datasets
- still allows services to display a combined timeline by deriving it from multiple datasets where needed

### Consequences

- `application-received` should not be a `permission-process-event` because `received-date` is already recorded on `planning-application`.
- `decision-date` should remain on `decision-notice` and should not be duplicated as a timeline event.
- `withdrawn-date` should be recorded on `planning-application` and should not be duplicated as a timeline event, because withdrawal is a fundamental fact about the application rather than a repeatable process event.
- a complete chronological timeline will need to be treated as a derived view. It may combine dates and events from `planning-application`, `planning-permission-timeline`, `decision-notice` and other decision-stage datasets without duplicating those facts in the canonical datasets.
- `application-submitted` remains a `permission-process-event`. It records submission by the applicant, which is distinct from receipt by the planning authority recorded in received-date.

### Alternatives considered

- Duplicate first-class dates in `planning-permission-timeline` -> rejected because it creates two authoritative-looking places for the same fact, increasing the risk of conflicting values without improving the canonical data model.
- Remove first-class dates from their owning datasets and model all dates only as events -> rejected because dates such as `received-date` and `decision-date` are fundamental properties of their records and should be easy to find.
