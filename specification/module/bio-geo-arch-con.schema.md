---
module: bio-geo-arch-con
name: Biodiversity, geological and archaeological conservation
description: |
  Assessment of potential impacts on protected species, important habitats, 
  biodiversity features, geological features, and archaeological features
fields:
  - field: protected-species-impact
    required: true
  - field: biodiversity-features-impact
    required: true
  - field: geological-features-impact
    required: true
  - field: archaeological-features-impact
    required: true
    applies-if:
      - application-type:
          in: [extraction-oil-gas]
rules:
  - "All impact assessments must use values from the affect-area codelist or 'no'"
  - "Archaeological features impact is only required for extraction-oil-gas applications"
  - "Impact assessments should be based on ecological surveys and site assessments"
entry-date: 2025-07-08
end-date: ''
---
