---
module: proposed-advert-details
name: Proposed advert details
description: Details of proposed advertisements including dimensions, materials, and illumination specifications
entry-date: 2025-07-17
end-date: ''
notes: ''
fields:
  - field: advertisements
    required: true
rules:
  - rule: "At least one advertisement entry must be provided"
    condition: "advertisements is not empty"
  - rule: "illumination-method is required when illuminated is true"
    condition: "For each advertisement: illuminated != true OR illumination-method is not empty"
  - rule: "illuminance-level is required when illuminated is true"
    condition: "For each advertisement: illuminated != true OR illuminance-level is provided"
  - rule: "illumination-type is required when illuminated is true"
    condition: "For each advertisement: illuminated != true OR illumination-type is not empty"
  - rule: "Dimensional values must be positive numbers"
    condition: "All height, width, depth, height-from-ground, symbol-height-max, max-projection values > 0"
  - rule: "illuminance-level must be positive when provided"
    condition: "All illuminance-level values > 0"
---
