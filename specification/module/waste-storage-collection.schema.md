---
description: Any waste storage or recycling arrangements are in place, such as waste
  storage areas
end-date: ''
entry-date: 2025-07-08
fields:
- applies-if:
    application-type:
      in:
      - full
  field: needs-waste-storage-area
  required: true
- applies-if:
    application-type:
      in:
      - outline
  field: needs-waste-storage-area-outline
  required: true
- field: waste-storage-area-details
  required-if:
    - field: needs-waste-storage-area
      value: true
- applies-if:
    application-type:
      in:
      - full
  field: separate-recycling-arrangements
  required: true
- applies-if:
    application-type:
      in:
      - outline
  field: separate-recycling-arrangements-outline
  required: true
- field: separate-recycling-arrangements-details
  required-if:
    - field: separate-recycling-arrangements
      value: true
module: waste-storage-collection
name: Waste storage and collection
rules:
- rule: waste-storage-area-details must be provided when needs-waste-storage-area
    is true
- rule: separate-recycling-arrangements-details must be provided when separate-recycling-arrangements
    is true
---

This module captures information about waste management provisions for new developments. It covers two main aspects:

**Waste Storage Areas**: Whether the development requires dedicated waste storage areas and if so, details about their design, location, size, and access arrangements.

**Recycling Arrangements**: Whether the development includes separate recycling provisions and if so, details about the types of materials to be recycled, collection methods, and storage facilities.

This information helps planning authorities assess whether adequate waste management infrastructure is being provided and whether it meets local waste management policies and requirements.
