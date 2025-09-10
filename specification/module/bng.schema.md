---
description: How any natural habitats on the development site will be improved by
  the proposed works.
end-date: ''
entry-date: 2025-06-16
fields:
- applies-if:
    application-type:
      in:
      - hh
  field: bng-exempt
  required: true
- applies-if:
    application-type:
      in:
      - full
      - outline
      - demolition-con-area
  field: bng-condition-applies
  required: true
- applies-if:
    application-type:
      in:
      - full
      - outline
      - demolition-con-area
  field: bng-condition-exemption-reasons
  required-if:
  - field: bng-condition-applies
    value: false
- applies-if:
    application-type:
      in:
      - full
      - outline
      - demolition-con-area
  field: bng-details
  required-if:
  - field: bng-condition-applies
    value: true
module: bng
name: Biodiversity net gain
rules:
- description: For householder applications, only bng-exempt field is required
  rule: application-type == 'hh' REQUIRES only bng-exempt field
- description: Exemption reasons must be provided when BNG condition does not apply
  rule: bng-condition-applies == false REQUIRES bng-condition-exemption-reasons.length
    >= 1
- description: BNG details must be provided when BNG condition applies
  rule: bng-condition-applies == true REQUIRES bng-details
- description: BNG exempt must be false for householder applications (confirming exemption)
  rule: application-type == 'hh' RECOMMENDS bng-exempt == false
- description: Exemption type must be from valid enumeration
  rule: bng-condition-exemption-reasons[].exemption-type must be from bng-exemption-type
    codelist
- description: Pre-development date must align with application or be justified
  rule: bng-details.pre-development-date <= application-submission-date OR earlier-date-reason
    provided
- description: Habitat loss details required when habitat loss after 2020 is true
  rule: bng-details.habitat-loss-after-2020 == true REQUIRES bng-details.habitat-loss-details
- description: Irreplaceable habitat details required when irreplaceable habitats
    present
  rule: bng-details.irreplaceable-habitats == true REQUIRES bng-details.irreplaceable-habitats-details
---

**Planning requirement documents**

* Completed biodiversity metric tool - Shows pre-development value and loss if applicable (REQUIRED)
* Habitat plan - Plan showing onsite habitats at the relevant date (REQUIRED)
* Irreplaceable habitat plan - Plan showing onsite irreplaceable habitats (REQUIRED If irreplaceable-habitats = Yes)