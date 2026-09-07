---
reference: decision-condition-requested-by
dataset: decision-condition
field: requested-by
---

### How to use it

Use this field when a consultee or other body requested that the condition be imposed on the particular decision. Omit it where no separate requesting organisation is known.

The requesting organisation does not formally impose or discharge the condition. The planning authority issues the original decision and determines a later application to discharge the condition, taking further advice from the requesting body where required.

For example, where the Environment Agency requested a condition:

```json
{
  "reference": "decision-2026-0123-condition-01",
  "decision-notice": "decision-2026-0123",
  "planning-condition": "ENV01",
  "requested-by": "government-organisation:EA199"
}
```
