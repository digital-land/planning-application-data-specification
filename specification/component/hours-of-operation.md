---
component: hours-of-operation
name: Hours of operation
description: Hours of operation structure for non-residential use
entry-date: 2025-07-16
end-date: ''
note: ''
fields:
  - field: use
    required: true
  - field: use-other
    required-if:
      - field: use
        value: other
        description: required if `use` field is other
  - field: operational-times
    required-if:
      - field: hours-not-known
        value: true
        description: required if `hours-not-known` field is true
  - field: hours-not-known
    required-if:
      - field: operational-times
        is: empty
        description: required if `operational-times` field is empty
          
---
