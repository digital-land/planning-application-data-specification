---
description: Who had a say in whether the proposal should go ahead
end-date: ''
entry-date: 2025-01-17
fields:
- field: applicant-interest-type
  required: true
- field: owner-details
  description: Details of the owner if the applicant is a lessee or occupier
  required-if:
  - field: applicant-interest-type
    in:
    - lessee
    - occupier
- field: interested-persons
  description: Details of other interested persons in the listed building
  required-if:
  - field: applicant-interest-type
    value: none
module: ldc-interest
name: LDC Interest
rules:
- rule: owner-details is required if applicant-interest-type is 'lessee' or 'occupier'
- rule: interested-persons is required if applicant-interest-type is 'none'
- rule: at least one of owner-details or interested-persons must be provided
---
