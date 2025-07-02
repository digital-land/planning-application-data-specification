---
module: dev-type
name: Development type
description: |
  Information about oil and gas development applications including phases, 
  quantities, licensing, and environmental considerations
fields:
  - field: development-phase
    required: true
  - field: development-description
    required: true
  - field: quantity-cubic-metres
    required: true
  - field: permission-period-years
  - field: hydrocarbon-licence-block
    required: true
  - field: surface-site-area-hectares
  - field: site-hectares-provided-by
  - field: environmental-statement
    required: true
  - field: environmental-statement-reference
    required-if:
      - field: environmental-statement
        value: true
    description: Reference to the environmental statement document
rules:
  - rule: "development-phase must contain at least one value from development-phases codelist"
  - rule: "quantity-cubic-metres must be a positive number"
  - rule: "surface-site-area-hectares must be a positive number"
  - rule: "environmental-statement-reference is required when environmental-statement is true"
  - rule: "environmental-statement-reference must reference a valid document in the application"
  - rule: "hydrocarbon-licence-block typically follows format PEDL123"
entry-date: 2025-07-02
end-date: ''
---
