---
description: Details of any hedgerows being removed as part of the development
end-date: ''
entry-date: 2025-07-17
fields:
- field: removal-reasons
  required: true
- field: plan-references
  required: true
- field: hedgerow-length
  required: true
- field: hedgerow-less-than-30-years
  required: true
- field: planting-evidence-attached
- field: interest-declaration
  required: true
module: hedgerow-removal
name: Hedgerow removal notice
rules:
- rule: hedgerow-length must be a positive number
- rule: planting-evidence-attached is required if hedgerow-less-than-30-years is true
- rule: plan-references should reference documents in application.documents
---