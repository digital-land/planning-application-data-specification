---
description: Drawings approved as part of the original decision and drawings submitted with the reserved matters application
end-date: ''
entry-date: 2025-06-26
fields:
- field: approved-drawings
  required-if:
  - field: submitted-drawings-document
    operator: empty
- field: submitted-drawing-references
  required-if:
  - field: submitted-drawings-document
    operator: empty
- field: approved-drawings-document
  required-if:
  - field: submitted-drawing-references
    operator: empty
- field: submitted-drawings-document
  required-if:
  - field: submitted-drawing-references
    operator: empty
- field: reason
  description: Reasons for any changes to the original drawings
module: supporting-info
name: Supporting information
rules:
- rule: Provide approved-drawings and submitted-drawing-references, or approved-drawings-document and submitted-drawings-document, but do not mix the two routes
- rule: References must be unique within approved-drawings and submitted-drawing-references
- rule: approved-drawings-document and submitted-drawings-document references must match documents in submission-details.documents
---
