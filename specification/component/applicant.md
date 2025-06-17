---
component: applicant
name: Applicant
description: |
  Details of an individual applicant for the planning application,
  including their personal information and contact details
fields:
  - field: reference
    required: true
  - field: person
    required: true
    component: person
  - field: contact-details
    component: contact-details
    required-if:
      - application-type:
          in: [pip]
entry-date: 2025-06-16
end-date: ''
---
