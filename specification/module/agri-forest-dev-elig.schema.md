---
description: |
  Information needed to assess agricultural unit, land parcel, agricultural purpose and wider site constraints
end-date: ''
entry-date: 2026-05-11
module: agri-forest-dev-elig
name: Agricultural and forestry development eligibility
fields:
  - field: agri-unit-area
    required: true
  - field: area-unit
    description: Unit of measurement for the total area of the entire agricultural unit, either square metres or hectares.
    required: true
  - field: land-parcel-area
    required: true
  - field: agri-use-years
    required: true
  - field: agri-use-months
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
  - field: height-applicable
    applies-if:
      application-type:
        in:
        - pa-road-agri-forest
        - pa-excavate-agri
    required: true
  - field: proposed-height
    description: Height of the proposed agricultural or forestry development in metres
    applies-if:
      any:
      - application-type:
          in:
          - pa-build-agri-forest
      - field: height-applicable
        value: true
    required: true
  - field: affects-heritage
    description: Would the proposed development affect an ancient monument, archaeological site or listed building or would it be within a Site of Special Scientific Interest or a local nature reserve?
    required: true
  - field: heritage-nature-impact-details
    required-if:
    - field: affects-heritage
      value: true
---

This module follows section 5, Agricultural and Forestry Developments, of the prior approval forms for [agricultural or forestry buildings](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form016_england_en.pdf), [private roads for agricultural or forestry use](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form017_england_en.pdf) and [excavation or waste deposit for agriculture](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form018_england_en.pdf).

The building form requires a height in metres. The road and excavation forms also offer Not applicable, represented by the height-applicable answer.
