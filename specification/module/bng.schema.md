---
module: bng
name: Biodiversity net gain
description: |
  Information about biodiversity net gain requirements for the development,
  including pre-development biodiversity value, habitat loss details, and
  supporting documentation
fields:
  - field: bng-exempt
    applies-if:
      - application-type:
          in: [hh]
    required: true
  - field: bng-condition-applies
    applies-if:
      - application-type:
          in: [full, outline, demolition-con-area]
    required: true
  - field: bng-condition-exemption-reason
    required-if:
      - field: bng-condition-applies
        value: false
    applies-if:
      - application-type:
          in: [full, outline, demolition-con-area]
  - field: bng-details
    required-if:
      - field: bng-condition-applies
        value: true
    applies-if:
      - application-type:
          in: [full, outline, demolition-con-area]
entry-date: 2025-06-16
end-date: ''
---

**Planning requirement documents**

* Completed biodiversity metric tool - Shows pre-development value and loss if applicable (REQUIRED)
* Habitat plan - Plan showing onsite habitats at the relevant date (REQUIRED)
* Irreplaceable habitat plan - Plan showing onsite irreplaceable habitats (REQUIRED If irreplaceable-habitats = Yes)
