---
module: proposal-details-inc-non-residential
name: Description of the proposed development including any non-residential development
description: |
  Details of proposed development with specific provision for capturing both residential 
  and non-residential elements, including dwelling numbers and non-residential use amounts
fields:
  - field: description
    required: true
    description: Description of proposed development including non-residential development
  - field: net-dwellings-min
    required: true
  - field: net-dwellings-max
    required: true
  - field: non-residential-use
    required: true
rules:
  - rule: "net-dwellings-max must be greater than or equal to net-dwellings-min"
  - rule: "Each non-residential-use entry must have either exact-value OR both min and max values"
  - rule: "For non-residential-use ranges, max must be greater than min"
  - rule: "non-residential-measurement-type must be from the non-res-measurement-type codelist"
entry-date: 2025-06-26
end-date: ''
---
