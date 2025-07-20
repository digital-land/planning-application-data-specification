---
module: interest-details
name: Interest details
description: |
  Details of the applicant's interest in land or listed buildings and information about
  other interested parties including owners and persons with interests in the property
fields:
  - field: applicant-interest
    required: true
    datatype: enum
    codelist: applicant-interest-type
  - field: owner-details
    required-if:
      any:
        - field: applicant-interest
          value: lessee
        - field: applicant-interest
          value: occupier
  - field: interested-persons
    required-if:
      - field: applicant-interest
        value: none
  - field: applicant-owns-land
    required: true
  - field: permission-obtained
    required-if:
      - field: applicant-owns-land
        value: false
  - field: permission-not-obtained-details
    required-if:
      any:
        - field: applicant-owns-land
          value: false
        - field: permission-obtained
          value: false
rules:
  - description: "Owner details required for lessee or occupier interests"
    rule: "if applicant-interest is 'lessee' or 'occupier', then owner-details is required"
  - description: "Interested persons required when applicant has no interest"
    rule: "if applicant-interest is 'none', then interested-persons is required"
  - description: "Permission status required when applicant doesn't own land"
    rule: "if applicant-owns-land is false, then permission-obtained is required"
  - description: "Permission details required when not obtained"
    rule: "if applicant-owns-land is false and permission-obtained is false, then permission-not-obtained-details is required"
  - description: "Advertisement permission compliance"
    rule: "No advertisement to be displayed without permission of owner or person with interest entitled to grant permission"
entry-date: 2025-07-18
end-date: ''
---
