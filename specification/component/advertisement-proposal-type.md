---
component: advertisement-proposal-type
name: Advertisement proposal type
description: |
  Information about a specific type of advertisement including type, count, 
  and additional description if 'other' type is selected
fields:
  - field: advertisement-type
    required: true
  - field: advertisement-count
    required: true
  - field: advertisement-other-description
    required-if:
      - field: advertisement-type
        value: "other"
entry-date: 2025-07-08
end-date: ''
---
