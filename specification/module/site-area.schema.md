---
description: How big the site is including relevant measurements
end-date: ''
entry-date: 2025-07-02
fields:
- field: site-area-in-hectares
  required: true
- field: site-area-provided-by
module: site-area
name: Site area
notes: site-area-in-hectares should ideally be calculated from site boundary
rules:
- rule: site-area-in-hectares must be a positive number
- rule: Authority can use site-area-provided-by to determine if calculation verification
    is needed
- rule: site-area-in-hectares is measured in hectares
---