---
module: nm-amendment-details
name: Non-material amendment details
description: |
  Details of non-material amendments to planning applications including
  description of changes, document substitutions, and reasons for amendments
fields:
  - field: description
    description: Description of the non-material amendments the applicant seeks to make
    required: true
  - field: is-substituting-document
    required: true
  - field: replacement-documents
    required-if:
      - field: is-substituting-document
        value: true
  - field: reason
    description: Reason why applicant wants to make the amendment
    required: true
rules:
  - description: "Replacement documents must be provided when substituting documents"
    rule: "is-substituting-document == true REQUIRES replacement-documents.length >= 1"
  - description: "Each replacement document must have valid old and new document references"
    rule: "replacement-documents[].old-document.length > 0 AND replacement-documents[].new-document.length > 0"
  - description: "Old and new document references must be different"
    rule: "replacement-documents[].old-document != replacement-documents[].new-document"
  - description: "Description must provide clear details of the amendments"
    rule: "description.length > 10"
  - description: "Reason must provide clear justification for the amendment"
    rule: "reason.length > 5"
entry-date: 2025-07-15
end-date: ''
---
