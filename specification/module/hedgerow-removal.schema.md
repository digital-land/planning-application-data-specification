---
description: Details of any hedgerows being removed as part of the development
end-date: ''
entry-date: 2025-07-17
fields:
- field: removal-reasons
  required: true
- field: supporting-documents
  description: References to plans or drawings showing the stretches of hedgerow to be removed
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
- rule: each document in supporting-documents must have a `reference` that matches
    a document in application.documents
---
