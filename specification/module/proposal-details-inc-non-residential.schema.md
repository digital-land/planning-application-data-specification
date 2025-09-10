---
description: Details of the residential and non-residential parts of the proposed
  development.
end-date: ''
entry-date: 2025-06-26
fields:
- description: Description of proposed development including non-residential development
  field: description
  required: true
- field: net-dwellings-min
  required: true
- field: net-dwellings-max
  required: true
- field: non-residential-use
  required: true
module: proposal-details-inc-non-residential
name: Description of the proposed development including any non-residential development
rules:
- rule: net-dwellings-max must be greater than or equal to net-dwellings-min
- rule: Each non-residential-use entry must have either exact-value OR both min and
    max values
- rule: For non-residential-use ranges, max must be greater than min
- rule: non-residential-measurement-type must be from the non-res-measurement-type
    codelist
---