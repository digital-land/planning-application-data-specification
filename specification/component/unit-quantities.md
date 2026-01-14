---
component: unit-quantities
name: Unit quantities
description: |
  Structure for defining quantities of units, either as unknown or broken down by bedroom count
fields:
  - applies-if:
      application-type:
        in:
        - full
        - outline
        - outline-all
        - outline-some
        - technical-details-consent
    field: units-unknown
    required: true
  - field: units-per-bedroom-no
    required-if:
      - any:
        - field: units-unknown
          value: false
        - application-type:
            in:
              - ldc-existing-use
  - field: total-units
entry-date: 2025-07-17
end-date: ''
---
