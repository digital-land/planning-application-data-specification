---
description: What development, works or change of use is proposed
end-date: ''
entry-date: 2025-06-12
fields:
- applies-if:
    application-type:
      in:
      - advertising
      - demolition-con-area
      - full
      - hh
      - lbc
      - outline
  field: proposal-description
  required: true
- applies-if:
    application-type:
      in:
      - outline
      - reserved-matters
  field: reserved-matters
  required: true
- applies-if:
    application-type:
      in:
      - reserved-matters
  field: related-application
  required: true
- applies-if:
    application-type:
      in:
      - advertising
      - demolition-con-area
      - full
      - hh
      - lbc
      - outline
  field: proposal-started
  required: true
- applies-if:
    application-type:
      in:
      - advertising
      - demolition-con-area
      - full
      - hh
      - lbc
      - outline
  field: proposal-started-date
  required-if:
  - field: proposal-started
    value: true
- applies-if:
    application-type:
      in:
      - advertising
      - demolition-con-area
      - full
      - hh
      - lbc
      - outline
  field: proposal-completed
  required: true
- applies-if:
    application-type:
      in:
      - advertising
      - demolition-con-area
      - full
      - hh
      - lbc
      - outline
  field: proposal-completed-date
  required-if:
  - field: proposal-completed
    value: true
- applies-if:
    application-type:
      in:
      - full
  field: pip-reference
- applies-if:
    application-type:
      in:
      - full
  field: is-psi
  required: true
module: proposal-details
name: Description of the proposal
rules:
- rule: proposal-description must be clear and concise
- rule: proposal-started-date must not be in the future
- rule: proposal-completed-date must be after proposal-started-date if both provided
- rule: reserved-matters must be valid types from the codelist
- rule: related-application reference must exist in authority records
- rule: pip-reference must match an existing Planning in Principle application
- rule: PSI projects must be checked against infrastructure improvement plans
---