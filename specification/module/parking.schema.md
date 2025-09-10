---
description: Details of any changes the proposed development would make to parking
  facilities.
end-date: ''
entry-date: 2025-06-12
fields:
- field: is-existing-parking-affected
  required: true
- description: A description of how the proposed works will affect existing car parking
    arrangements
  field: description
  required-if:
  - field: is-existing-parking-affected
    value: true
module: parking
name: Parking arrangements
---