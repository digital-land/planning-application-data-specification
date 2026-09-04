---
reference: decision-notice-decision-maker
dataset: decision-notice
field: decision-maker
---

### How to use it

Use this field to record the category of person or body that formally made the decision. Use a value from the `decision-maker` codelist.

Do not use the name of an individual officer. Do not use an organisation identifier: record the organisation that issued the notice in `organisation`.

### Examples

| Situation | `organisation` | `decision-maker` |
| --- | --- | --- |
| A planning officer makes the decision under delegated powers | `local-authority:RDB` | `planning-officer` |
| A planning committee makes the decision | `local-authority:RDB` | `committee` |
| A Planning Inspector makes the decision | `government-organisation:EA39` | `planning-inspector` |

For an LPA decision, `organisation` identifies the planning authority that issued the notice. `decision-maker` distinguishes a decision made by an officer under delegated powers from one made by the planning committee.

For an appeal decision made by a Planning Inspector, `organisation` identifies the Planning Inspectorate and `decision-maker` is `planning-inspector`.
