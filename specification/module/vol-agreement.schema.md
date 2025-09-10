---
description: Details of any voluntary agreements made as part of an oil and gas extraction
  application.
end-date: ''
entry-date: 2025-06-26
fields:
- field: draft-agreement-included
  required: true
- field: agreement-summary
  required-if:
  - field: draft-agreement-included
    value: true
module: vol-agreement
name: Voluntary agreement
rules:
- rule: agreement-summary is required when draft-agreement-included is true
- rule: Module only applies to extraction-oil-gas application types
---