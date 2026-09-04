---
reference: planning-application-received-date
dataset: planning-application
field: received-date
---

### How to use it

Use this field to record the date the planning authority first received the application.

Do not replace it with the date the application was later validated or registered.

This date marks the start of the authority's end-to-end handling time.

Keep the original received date and record validation separately using the `found-valid` planning permission timeline event. This makes it possible to distinguish time spent reaching validation from time spent determining the application.

For example:

```json
{
  "received-date": "2026-08-03"
}
```
