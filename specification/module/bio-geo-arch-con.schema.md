---
description: Details of potential impacts to the biodiversity of the site, or any
  noteable archaeological or geological features.
end-date: ''
entry-date: 2025-07-08
fields:
- field: protected-species-impact
  required: true
- field: biodiversity-features-impact
  required: true
- field: geological-features-impact
  required: true
- applies-if:
    application-type:
      in:
      - extraction-oil-gas
  field: archaeological-features-impact
  required: true
module: bio-geo-arch-con
name: Biodiversity, geological and archaeological conservation
rules:
- All impact assessments must use values from the affect-area codelist or 'no'
- Archaeological features impact is only required for extraction-oil-gas applications
- Impact assessments should be based on ecological surveys and site assessments
---