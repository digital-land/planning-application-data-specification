---
module: hedgerow-removal
name: Hedgerow removal notice
description: |
  Information required for hedgerow removal notices including removal reasons, plans, length details, age considerations, and interest declarations
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
rules:
  - rule: "hedgerow-length must be a positive number"
  - rule: "planting-evidence-attached is required if hedgerow-less-than-30-years is true"
  - rule: "plan-references should reference documents in application.documents"
entry-date: 2025-07-17
end-date: ''
---
