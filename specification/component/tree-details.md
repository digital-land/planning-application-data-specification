---
component: tree-details
name: Tree details
description: |
  Detailed information about an individual tree including identification, 
  species and proposed works
fields:
  - field: reference
    description: Identifier for the tree, use the TPO identifier if applicable
    required: true
  - field: species
  - field: description-of-works
  - field: reason
    description: Explain the reason for the work
    applies-if:
      application-type:
        in: [consent-under-tpo]
  - field: replanting-description
    applies-if:
      application-type:
        in: [consent-under-tpo]
entry-date: 2025-06-30
end-date: ''
---
