---
component: waste-management-outline
name: Waste management
description: |
  Details of applicable waste management facilities including type, capacity, and throughput information. Specifically for outline applications.
fields:
  - field: waste-management-facility-type
    required: true
  - field: is-total-capacity-known
    required: true
  - field: total-capacity
    required-if:
      - field: is-total-capacity-known
        value: true
  - field: unit-type
    required-if:
      - field: is-total-capacity-known
        value: true
  - field: is-annual-throughput-known
    required: true
  - field: annual-throughput
    required-if:
      - field: is-annual-throughput-known
        value: true
  - field: unit-type
    codelist: waste-throughput-unit
    required-if:
      - field: is-annual-throughput-known
        value: true
entry-date: 2025-07-09
end-date: ''
notes: Applicants should only include entries for facilities that are relevant to the proposal.
---
