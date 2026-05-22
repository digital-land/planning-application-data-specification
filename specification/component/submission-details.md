---
component: submission-details
name: Submission details
description: |
  Details about the submitted payload, including reference information,
  application types, specification profile, destination, documents, and fees
fields:
  - field: submission-reference
    required: true
  - field: application-types
    required: true
  - field: specification-profile
    required: true
  - field: planning-authority
    required: true
  - field: submitted-at
    required: true
  - field: created-at
    required: true
  - field: documents
    required: true
  - field: fee
validation:
  - rule: "submission-reference must identify the submitted payload"
  - rule: "application-types must reference valid application type codelist values"
  - rule: "specification-profile must reference a valid specification profile codelist value"
  - rule: "planning-authority must be a valid organisation reference"
  - rule: "document references must be unique within the submission"
  - rule: "file must contain base64-content"
  - rule: "document-types must reference valid planning requirement codelist values"
entry-date: 2025-06-20
end-date: ''
---
