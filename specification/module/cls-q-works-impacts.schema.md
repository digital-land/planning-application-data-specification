---
module: cls-q-works-impacts
name: Class Q works, impacts and risks
description: Proposed development, building works and impact and risk details for prior approval of agricultural buildings to dwellinghouses.
entry-date: '2026-10-20'
end-date: ''
fields:
- field: proposal-description
  description: Description of the proposed development, including the siting and location of the building or buildings.
  required: true
- field: natural-light-details
  required: true
- field: buildings-extended
  required: true
- field: impact-on-amenity
  description: Details of any impact of the proposed extension on the amenity of adjoining premises.
  required: true
  applies-if:
    field: buildings-extended
    value: true
- field: cls-q-building-works-required
  required: true
- field: design-details
  description: Details of the design and external appearance of the buildings for the associated building works or other operations, including partial demolition.
  required: true
  applies-if:
    field: cls-q-building-works-required
    value: true
- field: transport-impacts
  description: Details of transport and highways impacts of the proposed development and how they will be mitigated.
  required: true
- field: noise-impacts
  required: true
- field: contamination-risks
  required: true
- field: flooding-risks
  required: true
---

This module captures section 7 of the [prior approval application form for agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf), on pages 5 to 7. The field bodies preserve the source questions.

On page 6, “If yes” introduces the adjoining-amenity question immediately after the extension question. It separately introduces the design and external appearance question after the question about required building works or other operations. Each follow-up is applicable and required only when its preceding answer is true. The remaining eight answers have no conditional qualifier and are required.
