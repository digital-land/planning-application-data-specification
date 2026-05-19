---
description: Signed and dated verification of the application's accuracy.
end-date: ''
entry-date: 2025-06-12
fields:
- field: person-reference
  description: Declaration must be made by an applicant or agent making the application
  required: true
- field: declaration-confirmed
  required: true
- field: declaration-date
  required: true
module: declaration
name: Declaration
rules:
- rule: person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- rule: declaration-date must be in YYYY-MM-DD format
- rule: declaration-date must not be in the future
- rule: declaration-confirmed must be `true` for a submission to be valid
---
