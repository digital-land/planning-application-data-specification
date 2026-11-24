---
module: agri-excavation-works
name: Agricultural excavation or waste deposition
description: Details of proposed excavations or waste deposition for agricultural use.
entry-date: 2026-11-24
end-date: ''
fields:
  - field: proposed-works-area
    required: true
  - field: proposed-works-volume
    required: true
  - field: proposed-works-details
    description: Please provide a detailed description of the proposed works.
    required: true
  - field: prev-excavation-or-deposit
    required: true
  - field: previous-works-area
    applies-if:
      field: prev-excavation-or-deposit
      value: true
    required: true
  - field: holding-size
    required: true
  - field: holding-number
    required: true
  - field: excavation-depth-or-raising-height
    required: true
  - field: excavated-material-retained
    required: true
  - field: imported-waste-materials
  - field: affects-water
    required: true
  - field: water-impact-details
    applies-if:
      field: affects-water
      value: true
    required: true
---

This module captures section 4 of the [prior approval form for excavation or waste deposition for agriculture, ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form018_england_en.pdf).
