---
module: declaration
name: Declaration
description: |
  Declaration by the applicant or agent confirming the accuracy of the information provided
fields:
  - field: name
    required: true
  - field: declaration-confirmed
    required: true
  - field: declaration-date
    required: true
rules:
  - rule: "name must match one of the named individuals in the application"
  - rule: "declaration-date must be in YYYY-MM-DD format"
  - rule: "declaration-date must not be in the future"
entry-date: 2025-06-12
end-date: ''
---
