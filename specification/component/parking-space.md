---
component: parking-space
name: Parking space
description: |
  Information about parking spaces by vehicle type, including existing
  and proposed counts with net change calculations
fields:
  - field: parking-space-type
    required: true
  - field: vehicle-type-other
    required-if:
      - field: parking-space-type
        value: "other"
  - field: total-existing
    required: true
  - field: total-proposed
    required: true
  - field: unknown-proposed
    applies-if:
      application-type:
        in: ["outline-some"]
  - field: difference-in-spaces
    required: true
entry-date: 2025-07-08
end-date: ''
---
