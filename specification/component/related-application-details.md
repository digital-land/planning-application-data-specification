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
          in: [non-material-amendment]
entry-date: 2025-06-12
end-date: ''
---
