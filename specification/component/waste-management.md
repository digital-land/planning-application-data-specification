---
component: waste-management
name: Waste management
description: |
  Details of waste management facilities including type, capacity, and throughput information
fields:
  - field: type
    required: true
  - field: not-applicable
  - field: is-total-capacity-known
    required: true
    applies-if:
      - application-type:
        in: [outline]
  - field: total-capacity
    required-if:
      - field: not-applicable
        value: false
      - field: is-total-capacity-known
        value: true
        applies-if:
          - application-type:
            in: [outline]
  - field: is-annual-throughput-known
    required: true
    applies-if:
      - application-type:
        in: [outline]
  - field: annual-throughput
    required-if:
      - field: not-applicable
        value: false
      - field: is-annual-throughput-known
        value: true
        applies-if:
          - application-type:
            in: [outline]
entry-date: 2025-07-09
end-date: ''
---
