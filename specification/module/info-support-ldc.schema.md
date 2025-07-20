---
module: info-support-ldc
name: Information to support LDC
description: |
  Information to support Lawful Development Certificate applications including
  details of existing use, interruptions, and changes to support evidence of lawfulness
fields:
  - field: existing-use-start-date
    required: true
  - field: has-existing-use-interrupted
    required: true
  - field: interruption-details
    required-if:
      - field: has-existing-use-interrupted
        value: true
  - field: has-existing-use-changed
    required: true
  - field: existing-use-change-details
    required-if:
      - field: has-existing-use-changed
        value: true
rules:
  - description: "Start date must be a valid date in YYYY-MM-DD format"
    rule: "existing-use-start-date matches YYYY-MM-DD format"
  - description: "Start date must be in the past"
    rule: "existing-use-start-date <= current_date"
  - description: "Interruption details must be provided when use has been interrupted"
    rule: "has-existing-use-interrupted == true REQUIRES interruption-details.length > 0"
  - description: "Use change details must be provided when use has changed"
    rule: "has-existing-use-changed== true REQUIRES existing-use-change-details.length > 0"
  - description: "Interruption details must include relevant dates and circumstances"
    rule: "interruption-details must specify dates and nature of interruption when provided"
  - description: "Use change details must include relevant dates and nature of changes"
    rule: "existing-use-change-details must specify dates and nature of changes when provided"
entry-date: 2025-07-15
end-date: ''
---
