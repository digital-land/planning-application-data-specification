---
component: advertisement
name: Advertisement
description: Details of a proposed advertisement including dimensions, materials, and illumination
entry-date: 2025-07-17
end-date: ''
note: ''
fields:
  - field: height-from-ground
  - field: height
  - field: width
  - field: depth
  - field: symbol-height-max
  - field: colour
  - field: materials
  - field: max-projection
  - field: illuminated
  - field: illumination-method
    required-if: 
      - field: illuminated
        value: true
  - field: illuminance-level
    required-if: 
      - field: illuminated
        value: true
  - field: illumination-type
    required-if: 
      - field: illuminated
        value: true
---
