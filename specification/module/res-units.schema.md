---
description: Details of the residential units that make up both the current and proposed
  development.
end-date: ''
entry-date: 2025-07-17
fields:
- field: will-residential-units-change
  required: true
- field: residential-unit-summary
  required-if:
  - field: will-residential-units-change
    value: true
- field: total-existing-units
  required: true
- field: total-proposed-units
  required: true
- field: net-change
  required: true
implementation: For the paper forms, for space reasons, we need to limit the bedroom
  counts to 1, 2, 3, 4+
module: res-units
name: Residential units
rules:
- rule: residential-unit-summary is required when will-residential-units-change is
    true
- rule: net-change is calculated as total-proposed-units minus total-existing-units
- rule: if will-residential-units-change is true, at least one breakdown for existing
    and proposed is required (count could be unknown)
---