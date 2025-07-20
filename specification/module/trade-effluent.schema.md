---
module: trade-effluent
name: Trade effluent
description: |
  Information about the disposal of trade effluents or waste, including whether 
  disposal is required and details about the nature, volume and means of disposal
fields:
  - field: is-disposal-required
    required: true
  - field: description
    description: describe the nature, volume and means of disposal of trade effluents or waste
    required-if:
      - field: disposal-required
        value: true
rules:
  - rule: "description is required when disposal-required is true"
  - rule: "Module applies to full, extraction-oil-gas, and outline application types"
entry-date: 2025-06-26
end-date: ''
notes: This module should be included in all applications including full permission. For example, full and full+lbc
---
