---
description: Details of any liquid waste produced by industial processes on the proposed
  site, and how it will be diposed of.
end-date: ''
entry-date: 2025-06-26
fields:
- field: is-disposal-required
  required: true
- description: describe the nature, volume and means of disposal of trade effluents
    or waste
  field: description
  required-if:
  - field: disposal-required
    value: true
module: trade-effluent
name: Trade effluent
notes: This module should be included in all applications including full permission.
  For example, full and full+lbc
rules:
- rule: description is required when disposal-required is true
- rule: Module applies to full, extraction-oil-gas, and outline application types
---