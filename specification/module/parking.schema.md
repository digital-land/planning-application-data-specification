---
module: parking
name: Parking arrangements
description: |
  Information about how the proposed development affects existing parking arrangements
fields:
  - field: is-existing-parking-affected
    required: true
  - field: description
    description: A description of how the proposed works will affect existing car parking arrangements
    required-if:
      - field: is-existing-parking-affected
        value: true
entry-date: 2025-06-12
end-date: ''
---
