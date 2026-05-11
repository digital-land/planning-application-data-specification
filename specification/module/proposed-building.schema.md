---
description: Agricultural or forestry building details
end-date: ''
entry-date: 2026-05-11
module: proposed-building
name: Agricultural or forestry building details
fields:
  - field: development-operation-types
    required: true
  - field: proposed-building-details
    required: true
  - field: building-wall-materials
    required: true
  - field: building-wall-colour
    required: true
  - field: building-roof-materials
    required: true
  - field: building-roof-colour
    required: true
  - field: has-agri-building-2-yrs
    required: true
  - field: agri-building-area
    required-if:
    - field: has-agri-building-2-yrs
      value: true
  - field: agri-building-distance
    required-if:
    - field: has-agri-building-2-yrs
      value: true
  - field: house-livestock
    required: true
  - field: livestock-building-400m
    required-if:
    - field: house-livestock
      value: true
  - field: exceeds-threshold
    required: true
  - field: related-work-distance
    required: true
  - field: engineering-operations-threshold
    required: true
  - field: within-scheduled-monument
    required: true
---
