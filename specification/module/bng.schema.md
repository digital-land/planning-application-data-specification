---
description: How any natural habitats on the development site will be improved by
  the proposed works.
end-date: ''
entry-date: 2025-06-16
fields:
- field: bng-exempt
  applies-if:
    application-type:
      in:
      - hh
  required: true
- field: bng-condition-applies
  applies-if:
    application-type:
      in:
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
  required: true
- field: bng-condition-exemption-reasons
  applies-if:
    application-type:
      in:
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
  required-if:
  - field: bng-condition-applies
    value: false
- field: bng-details
  applies-if:
    all:
    - application-type:
        in:
        - full
        - technical-details-consent
        - outline
        - demolition-con-area
    - field: bng-condition-applies
      value: true
  required: true
module: bng
name: Biodiversity net gain
rules:
- description: For householder applications, only bng-exempt field is required
  rule: application-type == 'hh' REQUIRES only bng-exempt field
- description: Exemption reasons must be provided when BNG condition does not apply
  rule: bng-condition-applies == false REQUIRES bng-condition-exemption-reasons.length
    >= 1
- description: BNG details must be provided when in scope and must not be provided otherwise
  rule: BNG details are required when their applies-if condition is satisfied and are forbidden otherwise
- description: BNG exempt must be false for householder applications (confirming exemption)
  rule: application-type == 'hh' RECOMMENDS bng-exempt == false
- description: Exemption type must be from valid enumeration
  rule: bng-condition-exemption-reasons[].exemption-type must be from bng-exemption-type
    codelist
- description: A pre-development date earlier than submission must be justified
  rule: bng-details.pre-development-date < submission-details.submitted-at REQUIRES
    bng-details.earlier-date-reason
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
