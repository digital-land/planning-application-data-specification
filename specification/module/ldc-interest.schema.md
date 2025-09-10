---
description: Who had a say in whether the proposal should go ahead
end-date: ''
entry-date: 2025-01-17
fields:
- codelist: applicant-interest-type
  datatype: enum
  description: Applicant's interest in the listed building
  field: applicant-interest
  required: true
- description: Details of the owner if the applicant is a lessee or occupier
  field: owner-details
- description: Details of other interested persons in the listed building
  field: interested-persons
module: ldc-interest
name: LDC Interest
rules:
- rule: owner-details is required if applicant-interest is 'lessee' or 'occupier'
- rule: interested-persons is required if applicant-interest is 'none'
- rule: at least one of owner-details or interested-persons must be provided
---