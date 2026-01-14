---
component: supporting-document
name: Supporting document
description: |
  Reference to a supporting document already listed in application.documents
fields:
  - field: reference
    required: true
  - field: details
    applies-if:
      application-type:
        in: ["pip"]
entry-date: 2025-06-12
end-date: ''
rules:
- rule: reference must match a document reference in application.documents
---
