---
component: waste-management
name: Waste management
description: |
  Details of waste management facilities including type, capacity, and throughput information
fields:
  - field: waste-management-facility-type
    required: true
  - field: not-applicable
  - field: total-capacity
    required-if:
      - field: not-applicable
        value: false
  - field: annual-throughput
    required-if:
      - field: not-applicable
        value: false
entry-date: 2025-07-09
end-date: ''
---
