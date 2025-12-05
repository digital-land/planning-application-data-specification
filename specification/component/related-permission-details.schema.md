---
component: related-permission-details
name: Related permission-details
description: |
  Details about a related permission including the reference of the original application, type and decision date, and an option condition number/reference if varying
fields:
  - field: reference
    description: The reference for the related application that permission was received for
    required: true
  - field: oilgas-permission-type
    required: true
  - field: decision-date
    required: true
  - field: condition-number
    required-if:
      - field: oilgas-permission-type
        value: variation-condition
entry-date: 2025-12-05
end-date: ''
---
