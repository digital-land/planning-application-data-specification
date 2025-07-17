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
      - condition: 
          field: use
          other: other
  - field: operational-times
    required-if:
      - condition: 
          field: hours-not-known
          value: true
  - field: hours-not-known
    required-if:
      - condition: 
          field: operational-times
          is: empty
---
