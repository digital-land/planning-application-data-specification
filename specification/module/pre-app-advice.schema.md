---
description: Details of pre-application advice previously received from the planning authority
end-date: ''
entry-date: 2025-06-12
fields:
- field: advice-sought
  required: true
- field: officer-name
  required-if:
  - field: advice-sought
    value: true
- field: reference
  required-if:
  - field: advice-sought
    value: true
- field: advice-date
  required-if:
  - field: advice-sought
    value: true
- field: advice-summary
  required-if:
  - field: advice-sought
    value: true
module: pre-app-advice
name: Pre-application advice
---

Is `advice-summary` required if the applicant provides a reference to a document they have uploaded?
