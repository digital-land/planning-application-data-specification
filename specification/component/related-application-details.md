---
component: related-application-details
name: Related application details
description: |
  Details about a related application including its reference, description and decision date
fields:
  - field: reference
    description: The reference for the related application
    required: true
  - field: description
    description: A description of the related application
    required: true
  - field: decision-date
    required-if:
      - application-type:
          in: ['non-material-amendment']
  - field: eia-application
    applies-if:
      application-type:
        in:
          - reserved-matters
    required: true
  - field: environmental-statement-submitted
    applies-if:
      application-type:
        in:
          - reserved-matters
    required-if:
      - field: eia-application
        value: true
entry-date: 2025-06-12
end-date: ''
---
