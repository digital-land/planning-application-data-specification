---
description: Details of any demolition that needs to take place as part of the development
  proposal.
end-date: ''
entry-date: 2025-06-30
fields:
- description: Does the proposal include partial or total demolition of a listed building?
  field: is-proposing-demolition
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
- description: Description of the building or part you are proposing to demolish
  field: description
  required: true
- description: Reason for demolition
  field: reason
  required: true
module: demolition
name: Demolition
rules: null
---