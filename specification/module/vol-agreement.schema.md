---
module: vol-agreement
name: Voluntary agreement
description: |
  Information about voluntary agreements related to extraction oil and gas applications, 
  including whether a draft agreement is included and summary details
fields:
  - field: draft-agreement-included
    required: true
  - field: agreement-summary
    required-if:
      - field: draft-agreement-included
        value: true
rules:
  - rule: "agreement-summary is required when draft-agreement-included is true"
  - rule: "Module only applies to extraction-oil-gas application types"
entry-date: 2025-06-26
end-date: ''
---
