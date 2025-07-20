---
module: trees-ownership
name: Trees ownership
description: |
  Information about ownership of trees affected by the proposed works
fields:
  - field: is-applicant-owner
    description: Whether the applicant owns the trees affected by the proposed works
    required: true
    applies-if:
      application-type:
        in: [notice-trees-in-con-area, consent-under-tpo]
  - field: owner
    description: Details of the tree owner when applicant is not the owner
    applies-if:
      application-type:
        in: [notice-trees-in-con-area, consent-under-tpo]
    required-if:
      - field: is-applicant-owner
        value: false
rules:
  - rule: "owner details required when is-applicant-owner is false"
entry-date: 2025-06-30
end-date: ''
---
