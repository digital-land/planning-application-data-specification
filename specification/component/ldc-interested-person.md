---
component: ldc-interested-person
name: LDC Interested Person
description: |
  Details of persons with an interest in the property for Listed Building Consent applications including their personal information, nature of interest, and notification status
fields:
  - field: person
    description: Personal details of the interested person
    required: true
  - field: nature-of-interest
    required: true
  - field: informed-of-application
    required: true
  - field: reason-not-informed
rules:
  - rule: "person details must be complete for identification purposes"
  - rule: "nature-of-interest must be specified for all interested persons"
  - rule: "if informed-of-application is false, reason-not-informed should be provided"
entry-date: 2025-01-17
end-date: ''
---
