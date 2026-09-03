---
reference: planning-application-document-replaces
dataset: planning-application-document
field: replaces
---

### How to use it

Use `replaces` when a new document supersedes an earlier document for the same planning application.

Record the stable `reference` of the earlier document on the newer document record. Do not put the newer document's reference on the earlier record and do not use a filename or URL as the value.

Keep a separate record for each version. If a third version is published, it should replace the second version, forming a chain between the document records.

### Example

Document V1 is recorded first:

```json
{
  "reference": "document-001",
  "planning-application": "application-001",
  "name": "Proposed site plan V1",
  "document-url": "https://example.org/documents/site-plan-v1.pdf"
}
```

Document V2 is then published as its replacement:

```json
{
  "reference": "document-002",
  "planning-application": "application-001",
  "name": "Proposed site plan V2",
  "document-url": "https://example.org/documents/site-plan-v2.pdf",
  "replaces": "document-001"
}
```

`document-002` is the newer record, so its `replaces` field points to `document-001`.
