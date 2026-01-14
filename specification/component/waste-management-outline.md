---
component: waste-management-outline
name: Waste management
description: |
  Details of waste management facilities including type, capacity, and throughput information. Specifically for outline applications
fields:
  - field: waste-management-facility-type
    required: true
  - field: not-applicable
  - field: is-total-capacity-known
    required: true
  - field: total-capacity
    required-if:
     - all:
        - field: not-applicable
          value: false
        - field: is-total-capacity-known
          value: true
  - field: unit-type
    required-if:
      - all:
        - field: not-applicable
          value: false
        - field: is-total-capacity-known
          value: true
  - field: is-annual-throughput-known
    required: true
  - field: annual-throughput
    required-if:
      - all:
        - field: not-applicable
          value: false
        - field: is-annual-throughput-known
          value: true
  - field: unit-type
    codelist: waste-throughput-unit
    required-if:
      - all:
        - field: not-applicable
          value: false
        - field: is-annual-throughput-known
          value: true
entry-date: 2025-07-09
end-date: ''
---
