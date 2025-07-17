---
module: desc-your-proposal
name: Description of your proposal
description: |
  Details about your proposal including related planning permissions, 
  development status, and condition information
fields:
  - field: related-application
    description: Details of the related planning permission
    applies-if:
      application-type:
        in: ["s73", "approval-condition", "non-material-amendment"]
    required: true
  - field: condition-numbers
    applies-if:
      application-type:
        in: ["s73", "approval-condition"]
  - field: original-application-type
    applies-if:
      application-type:
        in: ["non-material-amendment"]
  - field: is-householder-development
    applies-if:
      application-type:
        in: ["non-material-amendment"]
  - field: has-development-started
    applies-if:
      application-type:
        in: ["s73", "approval-condition"]
    required: true
  - field: development-start-date
    applies-if:
      application-type:
        in: ["s73", "approval-condition"]
    required-if:
      - field: has-development-started
        value: true
  - field: has-development-completed
    applies-if:
      application-type:
        in: ["s73", "approval-condition"]
    required: true
  - field: development-completed-date
    applies-if:
      application-type:
        in: ["s73", "approval-condition"]
    required-if:
      - field: has-development-completed
        value: true
rules:
  - rule: "start-date is required when development-started is true"
  - rule: "completion-date is required when development-completed is true"
  - rule: "decision-date must be before the application submission date"
  - rule: "reference-number must match the decision letter"
  - rule: "proposal-description must match the decision letter"
  - rule: "Module applies to s73, approval-condition, and non-material-amendment application types"
entry-date: 2025-06-26
end-date: ''
---
