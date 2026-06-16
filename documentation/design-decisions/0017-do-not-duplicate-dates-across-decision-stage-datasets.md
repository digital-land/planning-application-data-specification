## Decision: Do not duplicate dates across decision-stage datasets

**Date:** 2026-05-28  
**Status:** Proposed

**Context:**  

The decision-stage specification has primary datasets that record the main facts about a planning application and its decision.

Some of those facts are dates. For example:

- `planning-application.received-date` records when the planning authority received the application
- `decision-notice.decision-date` records when the decision was made

The specification also has `planning-permission-timeline`, which records dated events in the processing of a planning application.

If the same date is recorded both as a primary dataset field and as a timeline event, the specification duplicates the same fact in two places. That creates scope for conflicting values and uncertainty about which record is authoritative.

**Decision:**  

The same date should not be modelled twice across decision-stage datasets.

Where a date is already recorded as a field on the dataset that owns the underlying record, it should not also be added as a `planning-permission-timeline` event for the same fact.

The `planning-permission-timeline` dataset should be used for process events where an event record is useful in its own right. This is especially relevant where events can happen more than once, need event-level context or are not already modelled as a first-class date on another dataset.

**Rationale:**  

Keeping core dates on the dataset that owns the record:

- makes the authoritative source clearer
- reduces the risk of the same date being recorded differently in two places
- keeps process events in the timeline and fundamental record properties on their owning datasets
- still allows services to display a combined timeline by deriving it from multiple datasets where needed

**Consequences:**  

- `application-received` should not be a `permission-process-event` because `received-date` is already recorded on `planning-application`.
- `decision-date` should remain on `decision-notice` and should not be duplicated as a timeline event.
- `withdrawn-date` should be recorded on `planning-application` and should not be duplicated as a timeline event, because withdrawal is a fundamental fact about the application rather than a repeatable process event.
- A complete chronological timeline should be treated as a derived view. It may combine dates and events from `planning-application`, `planning-permission-timeline`, `decision-notice` and other decision-stage datasets without duplicating those facts in the canonical datasets.
- `application-submitted` can remain as a `permission-process-event` because the decision-stage specification does not otherwise hold submitted date as a first-class field.

**Alternatives considered:**  

- Duplicate first-class dates in `planning-permission-timeline` -> rejected because it creates two authoritative-looking places for the same fact, increasing the risk of conflicting values without improving the canonical data model.
- Remove first-class dates from their owning datasets and model all dates only as events -> rejected because dates such as `received-date` and `decision-date` are fundamental properties of their records and should be easy to find.
