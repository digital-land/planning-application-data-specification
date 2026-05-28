---
component: room-details-outline
name: Room details
description: Details of room changes for hotels, residential institutions and hostels (C1, C2, C2A use classes)
entry-date: 2025-08-28
end-date: ''
notes: 'Used solely for outline applications'
fields:
  - field: use-class-accommodation
    required: true
  - field: use-other
    required-if:
    - field: use-class-accommodation
      value: other
      description: if use-class-accommodation == "other"
  - field: is-existing-rooms-lost-known
  - field: existing-rooms-lost
    required-if:
      - field: is-existing-rooms-lost-known
        value: true
  - field: is-total-rooms-proposed-known
  - field: total-rooms-proposed
    required-if:
      - field: is-total-rooms-proposed-known
        value: true
  - field: net-additional-rooms
    required: true
---

Room detail entries are only expected where the accommodation use class applies to the proposal.

Generated PDF or paper forms may still render "not applicable" controls for each possible option. That is presentation and capture logic, rather than a requirement for the canonical submission data model.
