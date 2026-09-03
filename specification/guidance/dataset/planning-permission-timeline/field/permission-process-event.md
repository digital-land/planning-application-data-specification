---
reference: planning-permission-timeline-permission-process-event
dataset: planning-permission-timeline
field: permission-process-event
---

### How to use it

Use this field only for the defined planning process milestones in the [`permission-process-event` codelist](https://github.com/digital-land/planning-application-data-specification/blob/main/data/codelist/permission-process-event.csv).

It is not intended to contain every action, contact or audit entry held in a case-management system.

For example, record the start of a consultation period:

```json
{
  "planning-application": "23/01234/FUL",
  "permission-process-event": "consultation-start",
  "event-date": "2026-08-12"
}
```

Record the end of that consultation period as a separate event:

```json
{
  "planning-application": "23/01234/FUL",
  "permission-process-event": "consultation-end",
  "event-date": "2026-09-09"
}
```

You do not need to, and are not expected to, create events for individual emails, telephone calls, case notes or site visits unless the activity is represented by a defined codelist value.
