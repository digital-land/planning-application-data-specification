---
description: Whether certain eligibility criteria has been met and the right people
  notified
end-date: ''
entry-date: 2025-07-18
fields:
- field: applicant-land-interest
  required: true
- field: ownership-notification
- field: notified-persons
  required-if:
  - field: ownership-notification
    value: true
module: eligibility
name: Eligibility
rules:
- description: Applicant must have land interest to proceed
  rule: applicant-land-interest == true (required for application to proceed)
- description: Ownership notification required for partial land interest
  rule: if applicant-land-interest == 'partial', then ownership-notification is required
- description: Notified persons required when notification given
  rule: if ownership-notification == 'yes', then notified-persons must be provided
- description: Application cannot proceed without proper notification
  rule: if ownership-notification == 'no', application cannot proceed without valid
    justification
---