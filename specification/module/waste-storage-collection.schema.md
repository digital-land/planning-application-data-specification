---
module: waste-storage-collection
name: Waste storage and collection
description: |
  Information about waste storage and recycling arrangements for developments, 
  including whether waste storage areas are needed and details of recycling provisions
fields:
  - field: needs-waste-storage-area
    required: true
    applies-if:
      application-type:
        in: ['full']
  - field: needs-waste-storage-area-outline
    required: true
    applies-if:
      application-type:
        in: ['outline']
  - field: waste-storage-area-details
    applies-if:
      field: needs-waste-storage-area
      value: true
  - field: separate-recycling-arrangements
    required: true
    applies-if:
      application-type:
        in: ['full']
  - field: separate-recycling-arrangements
    required: true
    applies-if:
      application-type:
        in: ['outline']
  - field: separate-recycling-arrangements-details
    applies-if:
      field: separate-recycling-arrangements
      value: true
rules:
  - rule: "waste-storage-area-details must be provided when needs-waste-storage-area is true"
  - rule: "separate-recycling-arrangements-details must be provided when separate-recycling-arrangements is true"
entry-date: 2025-07-08
end-date: ''
---

This module captures information about waste management provisions for new developments. It covers two main aspects:

**Waste Storage Areas**: Whether the development requires dedicated waste storage areas and if so, details about their design, location, size, and access arrangements.

**Recycling Arrangements**: Whether the development includes separate recycling provisions and if so, details about the types of materials to be recycled, collection methods, and storage facilities.

This information helps planning authorities assess whether adequate waste management infrastructure is being provided and whether it meets local waste management policies and requirements.
