---
reference: air-quality-assessment
name: Air Quality Assessment
description: >
  An assessment of the impact on air quality around the development and during the construction phase.
synonyms: []
requirement-type: document
source: "National Planning Policy Framework (NPPF), paras 110, 119"
entry-date: 2025-03-30
end-date: ''
required-if:
  all:
    - application-type:
        in: [full, outline, reserved-matters]
    - any:
        - condition:
            field: dwelling-count
            operator: ">="
            value: 10
            description: Development proposes 10 or more residential units.
        - condition:
            field: site-area-residential
            operator: ">="
            value: 0.5
            description: Site area for residential development is 0.5 hectares or more.
        - condition:
            field: site-area-non-residential
            operator: ">="
            value: 1
            description: Site area for non-residential development is 1 hectare or more.
        - condition:
            field: floorspace-non-residential
            operator: ">="
            value: 1000
            description: Non-residential floorspace is 1,000 square metres or more.
---
