---
module: pre-app-advice
name: Pre-application advice
description: |
  Information about any pre-application advice sought from the planning authority
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
entry-date: 2025-06-12
end-date: ''
---

Is `advice-summary` required if the applicant provides a reference to a document they have uploaded?
