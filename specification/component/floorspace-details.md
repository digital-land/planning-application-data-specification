---
component: floorspace-details
name: Floorspace details
description: Details of non-residential floorspace changes by use class including existing, lost, and proposed amounts
entry-date: 2025-07-17
end-date: ''
note: ''
fields:
  - field: use
    required: true
  - field: specified-use
    note: should this be use-other?
    required-if:
      any:
        - field: use
          contains: sui
        - field: use
          contains: other
    condition: use == "other" OR use == "sui"
  - field: existing-gross-floorspace
    required: true
  - field: floorspace-lost
    required: true
  - field: total-gross-proposed
    required: true
  - field: net-additional-floorspace
    required: true
---
