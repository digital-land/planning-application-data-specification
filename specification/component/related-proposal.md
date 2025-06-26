---
component: related-proposal
name: Related proposal
description: |
  Details about a related proposal including its reference, description and decision date
fields:
  - field: reference
    description: The reference for the related proposal/application
    required: true
  - field: description
    description: A description of the related proposal/application
    required: true
  - field: decision-date
    required-if:
      - application-type:
          in: [non-material-amendment]
entry-date: 2025-06-12
end-date: ''
---
