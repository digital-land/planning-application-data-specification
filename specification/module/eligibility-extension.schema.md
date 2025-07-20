---
module: eligibility-extension
name: Eligibility extension
description: |
  Eligibility criteria for extension applications to determine if the proposal
  meets the requirements for the application type
fields:
  - field: is-single-storey-extension
    required: true
  - field: is-extension-height-over-4m
    required: true
  - field: is-dwelling-detached
    required: true
  - field: is-extension-beyond-rear-wall
    required: true
  - field: extension-length
    required: true
  - field: is-within-site-constraints
    required: true
  - field: site-constraints
    required-if:
      - field: is-within-site-constraints
        equals: true
rules:
  - description: "Application cannot proceed if extension is not single storey"
    rule: "if is-single-storey-extension == false then application is ineligible"
  - description: "Application cannot proceed if extension exceeds 4 metres in height"
    rule: "if is-extension-height-over-4m == true then application is ineligible"
  - description: "Application cannot proceed if dwelling is within restricted areas"
    rule: "if is-within-site-constraints == true then application is ineligible"
  - description: "site-constraints is required when is-within-site-constraints is true"
    rule: "if is-within-site-constraints == true then site-constraints is required"
  - description: "Extension length limits depend on attachment type and dwelling type"
    rule: "extension-length must comply with permitted development limits based on is-dwelling-detached value"
entry-date: 2025-07-10
end-date: ''
---
