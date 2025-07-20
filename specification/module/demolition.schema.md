---
module: demolition
name: Demolition
description: |
  Permission or prior approval that may be required to demolish a building, specifically for listed building consent applications
fields:
  - field: is-proposing-demolition
    description: Does the proposal include partial or total demolition of a listed building?
    required: true
  - field: is-total-demolition
    required-if:
      - field: is-proposing-demolition
        value: true
  - field: is-demolishing-building-in-curtilage
    required-if:
      - field: is-proposing-demolition
        value: true
  - field: is-partial-demolition
    required-if:
      - field: is-proposing-demolition
        value: true
  - field: listed-building-volume
    required-if:
      - field: is-partial-demolition
        value: true
  - field: demolition-volume
    required-if:
      - field: is-partial-demolition
        value: true
  - field: part-built-date
    required-if:
      - field: is-partial-demolition
        value: true
  - field: description
    description: Description of the building or part you are proposing to demolish
    required: true
  - field: reason
    description: Reason for demolition
    required: true
rules:
entry-date: 2025-06-30
end-date: ''
---
