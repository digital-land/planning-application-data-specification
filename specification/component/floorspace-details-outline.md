---
component: floorspace-details-outline
name: Floorspace details
description: Details of non-residential floorspace changes by use class including existing, lost, and proposed amounts. Specifically for outline applications
entry-date: '2025-07-17'
end-date: ''
note: ''
fields:
  - field: use
    required: true
  - field: specified-use
    note: should this be use-other?
    required-if:
      description: use == "other" OR use == "sui"
      any:
        - field: use
          contains: sui
        - field: use
          contains: other
  - field: not-applicable
  - field: existing-gross-floorspace
    required: true
  - field: is-floorspace-lost-known
  - field: floorspace-lost
    required-if:
      - field: not-applicable
        value: false
      - field: is-floorspace-lost-known
        value: true
  - field: is-total-gross-proposed-known
  - field: total-gross-proposed
    required-if:
      - field: not-applicable
        value: false
      - field: is-total-gross-proposed-known
        value: true
  - field: net-additional-floorspace
    required: true
---
