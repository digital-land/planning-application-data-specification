---
description: Why a Certificate of Lawfulness of Propose Works is being requested.
end-date: ''
entry-date: 2025-07-16
fields:
- field: grounds-for-application
  required: true
- field: supporting-documents
  required: true
module: grounds-for-application
name: Grounds for application
rules:
- description: Grounds for application must be provided with clear reasoning
  rule: grounds-for-application.length > 0
- description: At least one supporting document must be provided
  rule: supporting-documents.length >= 1
- description: Supporting documents must reference uploaded application documents
  rule: each document in supporting-documents must have a `reference` that matches a document in application.documents
---
