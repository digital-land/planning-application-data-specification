---
description: Telephone number and email address of the applicant.
end-date: ''
entry-date: 2025-06-16
fields:
- field: applicant-reference
  required: true
- field: contact-details
  required: true
module: applicant-contact
name: Applicant contact details
rules:
- rule: applicant-reference must match a reference from the applicant details component
- rule: At least one phone number must have contact-priority set to primary
---