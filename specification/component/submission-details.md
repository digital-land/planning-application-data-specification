---
component: submission-details
name: Submission details
description: |
  Details about the submitted payload, including reference information,
  application types, specification profile, destination, modules, documents, and fees
fields:
  - field: reference
    required: true
  - field: application-types
    required: true
  - field: specification-profile
    required: true
  - field: planning-authority
    required: true
  - field: submission-date
    required: true
  - field: modules
    required: true
  - field: documents
    required: true
  - field: fee
validation:
  - rule: "reference must be a valid UUID format"
  - rule: "application-types must reference valid application type codelist values"
  - rule: "specification-profile must reference a valid specification profile codelist value"
  - rule: "planning-authority must be a valid organisation reference"
  - rule: "modules must reference existing module definitions"
  - rule: "document references must be unique within the submission"
  - rule: "file must contain base64-content"
  - rule: "document-types must reference valid planning requirement codelist values"
entry-date: 2025-06-20
end-date: ''
---
