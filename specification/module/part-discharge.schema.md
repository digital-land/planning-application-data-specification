---
description: Details of how the applicant is meeting a specific part of a set of conditions
  made by the planning authority.
end-date: ''
entry-date: 2025-07-07
fields:
- field: is-discharging-part
  required: true
- field: discharging-part-details
  required-if:
  - field: discharging-part
    value: true
module: part-discharge
name: Part discharge
rules:
- rule: discharging-part-details is required when is-discharging-part is true
- rule: discharging-part-details should specify which part of the condition is being
    addressed
---