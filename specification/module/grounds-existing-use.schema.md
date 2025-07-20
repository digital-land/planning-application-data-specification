---
module: grounds-existing-use
name: Grounds for application (information about the existing use(s))
description: |
  Information about the existing or last use of the site to support 
  a lawful development certificate application, including lawful justification,
  use classification, and supporting documentary evidence
fields:
  - field: use-lawful-reason
    required: true
  - field: documents
    required: false
  - field: use
    required: false
  - field: specified-use
    required-if:
      - field: use
        value: "sui"
      - field: use
        value: "other"
rules:
  - description: "Use lawful reason must be provided to justify the existing use"
    rule: "use-lawful-reason.length > 0"
  - description: "Specified use must be provided when use is 'sui' or 'other'"
    rule: "use IN ['sui', 'other'] REQUIRES specified-use.length > 0"
  - description: "Documents must have valid reference and name when provided"
    rule: "documents[].reference.length > 0 AND documents[].name.length > 0"
  - description: "Each document reference should be unique within the application"
    rule: "documents[].reference should be unique across application.documents[]"
entry-date: 2025-06-26
end-date: ''
---
