---
module: grounds-for-application
name: Grounds for application
description: |
  Grounds for a Certificate of Lawfulness of Proposed Works application,
  explaining why the certificate should be granted and why listed building
  consent is not required, with supporting documentary evidence
fields:
  - field: grounds-for-application
    required: true
  - field: documents
    required: true
rules:
  - description: "Grounds for application must be provided with clear reasoning"
    rule: "grounds-for-application.length > 0"
  - description: "At least one supporting document must be provided"
    rule: "documents.length >= 1"
  - description: "Documents must have valid reference and name"
    rule: "documents[].reference.length > 0 AND documents[].name.length > 0"
  - description: "Each document reference should be unique within the application"
    rule: "documents[].reference should be unique across application.documents[]"
entry-date: 2025-07-16
end-date: ''
---
