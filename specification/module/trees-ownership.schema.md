---
description: Who owns any trees affected by the proposed development.
end-date: ''
entry-date: 2025-06-30
fields:
- applies-if:
    application-type:
      in:
      - notice-trees-in-con-area
      - consent-under-tpo
  description: Whether the applicant owns the trees affected by the proposed works
  field: is-applicant-owner
  required: true
- applies-if:
    application-type:
      in:
      - notice-trees-in-con-area
      - consent-under-tpo
  description: Details of the tree owner when applicant is not the owner
  field: owner
  required-if:
  - field: is-applicant-owner
    value: false
module: trees-ownership
name: Trees ownership
rules:
- rule: owner details required when is-applicant-owner is false
---