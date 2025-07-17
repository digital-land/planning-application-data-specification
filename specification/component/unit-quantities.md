---
component: unit-quantities
name: Unit quantities
description: |
  Structure for defining quantities of units, either as unknown or broken down by bedroom count
fields:
  - field: units-unknown
    required: true
  - field: units-per-bedroom-no
    required-if:
      - field: units-unknown
        value: false
  - field: total-units
entry-date: 2025-07-17
end-date: ''
---
