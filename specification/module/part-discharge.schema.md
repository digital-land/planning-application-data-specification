---
module: part-discharge
name: Part discharge
description: |
  Information about whether the applicant is trying to discharge part of a condition
  and details about which part of the condition is being addressed
fields:
  - field: is-discharging-part
    required: true
  - field: discharging-part-details
    required-if:
      - field: discharging-part
        value: true
rules:
  - rule: "discharging-part-details is required when is-discharging-part is true"
  - rule: "discharging-part-details should specify which part of the condition is being addressed"
entry-date: 2025-07-07
end-date: ''
---
