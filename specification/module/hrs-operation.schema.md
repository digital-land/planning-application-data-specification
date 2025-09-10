---
description: Proposed operating hours if the proposed development is intended for
  non-residential use.
end-date: ''
entry-date: 2025-07-16
fields:
- applies-if:
    application-type:
      in:
      - full
      - outline
      - extraction-oil-gas
  field: hours-of-operation
  required: true
- applies-if:
    application-type:
      in:
      - extraction-oil-gas
  field: additional-information
module: hrs-operation
name: Hours of operation
notes: ''
rules:
- condition: hours-of-operation is not empty
  rule: At least one hours-of-operation entry must be provided
- condition: 'For each hours-of-operation: operational-times is not empty OR hours-not-known
    == true'
  rule: Either operational-times or hours-not-known must be provided within each hours-of-operation
    entry
- condition: 'For each hours-of-operation: use != ''other'' OR use-other is not empty'
  rule: use-other is required when use is 'other'
- condition: 'For each operational-times: closed == true OR time-ranges is not empty'
  rule: time-ranges is required when not closed
- condition: All open-time and close-time values match pattern '^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
  rule: open-time and close-time must be in HH:MM format
- condition: 'For each time-range: close-time > open-time'
  rule: close-time must be after open-time within same time range
---