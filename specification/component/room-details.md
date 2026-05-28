---
component: room-details
name: Room details
description: Details of room changes for hotels, residential institutions and hostels (C1, C2, C2A use classes)
entry-date: 2025-07-17
end-date: ''
notes: ''
fields:
  - field: use-class-accommodation
    required: true
  - field: use-other
    required-if:
    - field: use-class-accommodation
      value: other
      description: if use-class-accommodation == "other"
  - field: existing-rooms-lost
    required: true
  - field: total-rooms-proposed
    required: true
  - field: net-additional-rooms
    required: true
---

Room detail entries are only expected where the accommodation use class applies to the proposal.

Generated PDF or paper forms may still render "not applicable" controls for each possible option. That is presentation and capture logic, rather than a requirement for the canonical submission data model.
