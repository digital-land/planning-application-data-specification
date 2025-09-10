---
description: Details of the proposed advertisements such as their size and how they
  are made
end-date: ''
entry-date: 2025-07-17
fields:
- field: advertisements
  required: true
module: proposed-advert-details
name: Proposed advert details
notes: ''
rules:
- condition: advertisements is not empty
  rule: At least one advertisement entry must be provided
- condition: 'For each advertisement: illuminated != true OR illumination-method is
    not empty'
  rule: illumination-method is required when illuminated is true
- condition: 'For each advertisement: illuminated != true OR illuminance-level is
    provided'
  rule: illuminance-level is required when illuminated is true
- condition: 'For each advertisement: illuminated != true OR illumination-type is
    not empty'
  rule: illumination-type is required when illuminated is true
- condition: All height, width, depth, height-from-ground, symbol-height-max, max-projection
    values > 0
  rule: Dimensional values must be positive numbers
- condition: All illuminance-level values > 0
  rule: illuminance-level must be positive when provided
---