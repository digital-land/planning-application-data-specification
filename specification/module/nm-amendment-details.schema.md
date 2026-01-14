---
description: Details of changes being requested to plans after permission has already
  been granted.
end-date: ''
entry-date: 2025-07-15
fields:
- description: Description of the non-material amendments the applicant seeks to make
  field: description
  required: true
- field: is-substituting-document
  required: true
- field: replacement-documents
  required-if:
  - field: is-substituting-document
    value: true
- description: Reason why applicant wants to make the amendment
  field: reason
  required: true
module: nm-amendment-details
name: Non-material amendment details
rules:
- description: Replacement documents must be provided when substituting documents
  rule: is-substituting-document == true REQUIRES replacement-documents.length >=
    1
- description: Each replacement document must have valid old and new document references
  rule: replacement-documents[].old-document.length > 0 AND replacement-documents[].new-document.length
    > 0
- description: Old and new document references must be different
  rule: replacement-documents[].old-document != replacement-documents[].new-document
- description: Old and new document references must match documents uploaded with the application
  rule: each document in replacement-documents must have `old-document` and `new-document`
    that match a document in application.documents
- description: Description must provide clear details of the amendments
  rule: description.length > 10
- description: Reason must provide clear justification for the amendment
  rule: reason.length > 5
---
