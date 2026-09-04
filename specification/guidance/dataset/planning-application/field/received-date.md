---
reference: planning-application-received-date
dataset: planning-application
field: received-date
---

### How to use it

Use this field to record the date the planning authority first received the application.

Do not replace it with the date the application was later validated or registered.

This date marks the start of the authority's end-to-end handling time.

Keep the original received date and record validation separately in the planning permission timeline using the defined events:

- `valid-from`: the date from which the authority treated the application as valid
- `invalid-from`: the date from which the authority treated the application as invalid
- `validation-completed`: the date the authority completed its validation check

These dates may differ. Keeping them separate makes it possible to distinguish time spent reaching validation from time spent determining the application.

For example:

```json
{
  "received-date": "2026-08-03"
}
```
