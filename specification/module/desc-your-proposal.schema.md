---
description: Written description of the proposed development including any additional
  relevant details.
end-date: ''
entry-date: 2025-06-26
fields:
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
      - non-material-amendment
  description: Details of the related planning permission
  field: related-application
  required: true
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
  field: condition-numbers
- applies-if:
    application-type:
      in:
      - non-material-amendment
  field: original-application-type
- applies-if:
    application-type:
      in:
      - non-material-amendment
  field: is-householder-development
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
  field: has-development-started
  required: true
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
  field: development-start-date
  required-if:
  - field: has-development-started
    value: true
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
  field: has-development-completed
  required: true
- applies-if:
    application-type:
      in:
      - s73
      - approval-condition
  field: development-completed-date
  required-if:
  - field: has-development-completed
    value: true
module: desc-your-proposal
name: Description of your proposal
rules:
- rule: start-date is required when development-started is true
- rule: completion-date is required when development-completed is true
- rule: decision-date must be before the application submission date
- rule: reference-number must match the decision letter
- rule: proposal-description must match the decision letter
- rule: Module applies to s73, approval-condition, and non-material-amendment application
    types
---