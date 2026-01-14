---
description: Supporting inforation for a Lawful Development Certificate application
  relating to how the site has most recently been used.
end-date: ''
entry-date: 2025-06-26
fields:
- field: use-lawful-reason
  required: true
- field: supporting-documents
  required: false
- field: use
  required: false
- field: specified-use
  required-if:
  - field: use
    value: sui
  - field: use
    value: other
module: grounds-existing-use
name: Grounds for application (information about the existing use(s))
rules:
- description: Use lawful reason must be provided to justify the existing use
  rule: use-lawful-reason.length > 0
- description: Specified use must be provided when use is 'sui' or 'other'
  rule: use IN ['sui', 'other'] REQUIRES specified-use.length > 0
- description: Supporting documents must reference uploaded application documents
  rule: each document in supporting-documents must have a `reference` that matches a document in application.documents
---
