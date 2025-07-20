---
module: proposal-details
name: Description of the proposal
description: |
  Information about what development, works or change of use is being proposed
fields:
  - field: proposal-description
    applies-if:
      - application-type:
          in: ["advertising", "demolition-con-area", "full", "hh", "lbc", "outline"]
    required: true
  - field: reserved-matters
    applies-if:
      - application-type:
          in: ["outline", "reserved-matters"]
    required: true
  - field: related-application
    applies-if:
      - application-type:
          in: [reserved-matters]
    required: true
  - field: proposal-started
    applies-if:
      - application-type:
          in: ["advertising", "demolition-con-area", "full", "hh", "lbc", "outline"]
    required: true
  - field: proposal-started-date
    applies-if:
      - application-type:
          in: ["advertising", "demolition-con-area", "full", "hh", "lbc", "outline"]
    required-if:
      - field: proposal-started
        value: true
  - field: proposal-completed
    applies-if:
      - application-type:
          in: ["advertising", "demolition-con-area", "full", "hh", "lbc", "outline"]
    required: true
  - field: proposal-completed-date
    applies-if:
      - application-type:
          in: ["advertising", "demolition-con-area", "full", "hh", "lbc", "outline"]
    required-if:
      - field: proposal-completed
        value: true
  - field: pip-reference
    applies-if:
      - application-type:
          in: ["full"]
  - field: is-psi
    applies-if:
      - application-type:
          in: ["full"]
    required: true

rules:
  - rule: "proposal-description must be clear and concise"
  - rule: "proposal-started-date must not be in the future"
  - rule: "proposal-completed-date must be after proposal-started-date if both provided"
  - rule: "reserved-matters must be valid types from the codelist"
  - rule: "related-application reference must exist in authority records"
  - rule: "pip-reference must match an existing Planning in Principle application"
  - rule: "PSI projects must be checked against infrastructure improvement plans"
entry-date: 2025-06-12
end-date: ''
---
