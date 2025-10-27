---
component: room-details-outline
name: Room details
description: Details of room changes for hotels, residential institutions and hostels (C1, C2, C2A use classes)
entry-date: 2025-08-28
end-date: ''
note: 'Used solely for outline applications'
fields:
  - field: use-class-accommodation
    required: true
  - field: use-other
    required-if:
    - field: use-class-accommodation
      value: other
      description: if use-class-accommodation == "other"
  - field: not-applicable
  - field: is-existing-rooms-lost-known
  - field: existing-rooms-lost
    required-if:
      - field: not-applicable
        value: false
      - field: is-existing-rooms-lost-known
        value: true
  - field: is-total-rooms-proposed-known
  - field: total-rooms-proposed
    required-if:
      - field: not-applicable
        value: false
      - field: is-total-rooms-proposed-known
        value: true
  - field: net-additional-rooms
    required: true
---
