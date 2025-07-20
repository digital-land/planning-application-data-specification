---
module: proposal-details-ldc
name: Proposal details LDC
description: Details of the proposal for lawful development certificate applications
entry-date: 2025-07-17
end-date: ''
notes: ''
fields:
  - field: proposal-incl-building-operations
    required: true
  - field: proposal-building-operations-description
    required-if:
      - field: proposal-incl-building-operations
        value: true
  - field: proposal-incl-change-of-use
    required: true
  - field: proposal-change-of-use-description
    required-if:
      - field: proposal-incl-change-of-use
        value: true
  - field: proposal-existing-use-description
    required-if:
      - field: proposal-incl-change-of-use
        value: true
  - field: proposal-existing-use-stop-date
    required-if:
      - field: proposal-incl-change-of-use
        value: true
  - field: proposal-started
    required: true
rules:
  - rule: "proposal-building-operations-description is required when proposal-incl-building-operations is true"
    condition: "proposal-incl-building-operations != true OR proposal-building-operations-description is not empty"
  - rule: "proposal-change-of-use-description is required when proposal-incl-change-of-use is true"
    condition: "proposal-incl-change-of-use != true OR proposal-change-of-use-description is not empty"
  - rule: "proposal-existing-use-description is required when proposal-incl-change-of-use is true"
    condition: "proposal-incl-change-of-use != true OR proposal-existing-use-description is not empty"
  - rule: "proposal-existing-use-stop-date is required when proposal-incl-change-of-use is true"
    condition: "proposal-incl-change-of-use != true OR proposal-existing-use-stop-date is not empty"
  - rule: "proposal-existing-use-stop-date must be in YYYY-MM-DD format"
    condition: "proposal-existing-use-stop-date matches pattern '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'"
---
