---
description: Names and contact details for all parties with an interest in the proposed
  develpoment.
end-date: ''
entry-date: 2025-07-18
fields:
- codelist: applicant-interest-type
  datatype: enum
  field: applicant-interest
  required: true
- field: owner-details
  required-if:
    - any:
      - field: applicant-interest
        value: lessee
      - field: applicant-interest
        value: occupier
- field: interested-persons
  required-if:
  - field: applicant-interest
    value: none
module: interest-details
name: Interest details
rules:
- description: Owner details required for lessee or occupier interests
  rule: if applicant-interest is 'lessee' or 'occupier', then owner-details is required
- description: Interested persons required when applicant has no interest
  rule: if applicant-interest is 'none', then interested-persons is required
- description: Permission status required when applicant doesn't own land
  rule: if applicant-owns-land is false, then permission-obtained is required
- description: Permission details required when not obtained
  rule: if applicant-owns-land is false and permission-obtained is false, then permission-not-obtained-details
    is required
---
