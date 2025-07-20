---
module: eligibility-related-works
name: Eligibility related works
description: |
  Eligibility criteria for engineering works related to prior approval applications,
  specifically relating to external support structures and curtilage extensions
fields:
  - field: external-support-required
    required: true
rules:
  - description: "External support impacts prior approval applicability"
    rule: "external-support-required == true may affect prior approval eligibility"
entry-date: 2025-07-18
end-date: ''
---
