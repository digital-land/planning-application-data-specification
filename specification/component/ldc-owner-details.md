---
component: ldc-owner-details
name: LDC Owner Details
description: |
  Details of property owners for Listed Building Consent applications including their personal information and whether they have been informed of the application
fields:
  - field: person
    description: Personal details of the property owner
    required: true
  - field: informed-of-application
    description: Whether the owner has been informed of the application
    required: true
rules:
  - rule: "person details must be complete for identification purposes"
  - rule: "informed-of-application must be specified for all owners"
entry-date: 2025-01-17
end-date: ''
---
