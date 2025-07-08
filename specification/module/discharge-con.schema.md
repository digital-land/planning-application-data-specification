---
module: discharge-con
name: Discharge condition
description: |
  Module for capturing information about materials and details being submitted 
  for approval as part of discharging planning conditions
fields:
  - field: description-list
    required: true
    applies-if:
      - application-type:
          in: [approval-condition]
rules:
  - "Description-list must provide clear details of materials/details submitted for approval"
  - "This module is only applicable to approval-condition applications"
entry-date: 2025-07-08
end-date: ''
---
