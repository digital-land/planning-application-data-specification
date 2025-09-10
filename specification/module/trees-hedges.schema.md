---
description: Details of trees and/or hedges that will be affected by the proposed
  development
end-date: ''
entry-date: 2025-06-12
fields:
- applies-if:
    application-type:
      in:
      - full;outline-some;extraction-oil-gas
  field: trees-on-site
  required: true
- applies-if:
    application-type:
      in:
      - full;outline-some;extraction-oil-gas
  field: trees-on-adj-land
  required: true
- applies-if:
    application-type:
      in:
      - hh
  field: has-falling-trees-risk
  required: true
- applies-if:
    application-type:
      in:
      - hh
  field: falling-trees-document
  required-if:
  - field: has-falling-trees-risk
    value: true
- applies-if:
    application-type:
      in:
      - hh
  field: tree-removal
  required: true
- applies-if:
    application-type:
      in:
      - hh
  field: tree-removal-plan
  required-if:
  - field: tree-removal
    value: true
module: trees-hedges
name: Trees and hedges information
rules:
- rule: falling-trees-document reference must match a document in application.documents
- rule: tree-removal-plan reference must match a document in application.documents
---