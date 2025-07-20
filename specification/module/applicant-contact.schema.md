---
module: applicant-contact
name: Applicant contact details
description: |
  Contact details for the applicant or applicants, including email and phone numbers
fields:
  - field: applicant-reference
    required: true
  - field: contact-details
    required: true
rules:
  - rule: "applicant-reference must match a reference from the applicant details component"
  - rule: "At least one phone number must have contact-priority set to primary"
entry-date: 2025-06-16
end-date: ''
---
