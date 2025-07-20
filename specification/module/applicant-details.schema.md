---
module: applicant-details
name: Applicant details
description: |
  Details about the applicants for the planning application,
  including their personal information and contact details
fields:
  - field: applicants
    required: true
    minimum-items: 1
rules:
  - rule: "At least one applicant must be provided"
  - rule: "Each applicant reference must be unique within the application"
entry-date: 2025-06-16
end-date: ''
---
