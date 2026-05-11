---
description: 
end-date: ''
entry-date: 2026-05-11
module: agri-forest-dev-elig
name: 
fields:
  - field: agri-unit-area
    required: true
  - field: land-parcel-area
    required: true
  - field: agri-start-date
    required: true
  - field: is-necessary-for-agri
    required: true
  - field: details
    description: Explanation of why the proposed development is reasonably necessary for the purposes of agriculture.
    required-if:
    - field: is-necessary-for-agri
      value: true
  - field: is-designed-agri
    required: true
  - field: design-details
    description: |
      Explanation of why the proposed development is designed for the purposes of agriculture.
    required-if:
    - field: is-designed-agri
      value: true
  - field: dwelling-alteration
    required: true
  - field: away-from-road
    required: true
  - field: close-to-aerodrome
    required: true
  - field: proposed-height
    description: Height of the proposed agricultural or forestry development in metres
    required: true
  - field: affects-heritage
    required: true
  - field: heritage-nature-impact-details
    required-if:
    - field: affects-heritage
      value: true
---
