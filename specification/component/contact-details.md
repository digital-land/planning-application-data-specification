---
component: contact-details
name: Contact details
description: |
  A substructure for recording contact details
fields:
  - field: email
    required: true
  - field: phone-numbers
    required: true
rules:
  - rule: At least one phone number must have `contact-priority` set to `primary`
    applies-to: phone-numbers
    condition:
      field: contact-priority
      equals: primary
      minimum-occurrences: 1
entry-date: 2025-05-30
end-date: ''
---
