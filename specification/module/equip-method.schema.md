---
module: equip-method
name: Equipment and method
description: |
  Module for capturing information about equipment and methods to be used 
  in extraction operations, particularly for oil and gas applications
fields:
  - field: equipment-plan
    required: true
rules:
  - "Equipment-plan must include details of equipment types and specifications"
  - "For drilling operations, maximum height and type of drilling rig must be specified"
  - "This module is only applicable to extraction-oil-gas applications"
entry-date: 2025-07-08
end-date: ''
---
