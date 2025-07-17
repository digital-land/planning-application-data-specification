---
module: ldc-interest
name: LDC Interest
description: |
  Information about the applicant's interest in the listed building and details of other interested parties including owners and interested persons
fields:
  - field: applicant-interest
    description: Applicant's interest in the listed building
    datatype: enum
    codelist: applicant-interest-type
    required: true
  - field: owner-details
    description: Details of the owner if the applicant is a lessee or occupier
  - field: interested-persons
    description: Details of other interested persons in the listed building  
components:
  - component: ldc-owner-details
    description: Structure for owner details including person information and notification status
  - component: ldc-interested-person
    description: Structure for interested person details including person information, nature of interest, and notification status
rules:
  - rule: "owner-details is required if applicant-interest is 'lessee' or 'occupier'"
  - rule: "interested-persons is required if applicant-interest is 'none'"
  - rule: "at least one of owner-details or interested-persons must be provided"
entry-date: 2025-01-17
end-date: ''
---
