---
module: site-area
name: Site area
description: |
  Information about the size of the development site, including 
  the area measurement and source of the measurement
fields:
  - field: site-area-in-hectares
    required: true
  - field: site-area-provided-by
rules:
  - rule: "site-area-in-hectares must be a positive number"
  - rule: "Authority can use site-area-provided-by to determine if calculation verification is needed"
  - rule: "site-area-in-hectares is measured in hectares"
notes: "site-area-in-hectares should ideally be calculated from site boundary"
entry-date: 2025-07-02
end-date: ''
---
