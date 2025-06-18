---
module: trees-hedges
name: Trees and hedges information
description: |
  Information about trees and hedges on or adjacent to the development site, including any that pose risks or need to be removed
fields:
  - field: trees-on-site
    applies-if:
      application-type:
        in: [full;outline-some;extraction-oil-gas]
    required: true
  - field: trees-on-adj-land
    applies-if:
      application-type:
        in: [full;outline-some;extraction-oil-gas]
    required: true
  - field: has-falling-trees-risk
    applies-if:
      application-type:
        in: [hh]
    required: true
  - field: falling-trees-document
    applies-if:
      application-type:
        in: [hh]
    required-if:
      - field: has-falling-trees-risk
        value: true
  - field: tree-removal
    applies-if:
      application-type:
        in: [hh]
    required: true
  - field: tree-removal-plan
    applies-if:
      application-type:
        in: [hh]
    required-if:
      - field: tree-removal
        value: true
rules:
  - rule: "falling-trees-document reference must match a document in application.documents"
  - rule: "tree-removal-plan reference must match a document in application.documents"
entry-date: 2025-06-12
end-date: ''
---
