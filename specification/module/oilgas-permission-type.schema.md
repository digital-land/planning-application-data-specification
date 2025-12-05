---
module: oilgas-permission-type
name: Oil and gas permission types
description: |
  Module for details about types of onshore oil and gas extraction permissions already received and applying for
fields:
  - field: oilgas-permission-types
    required: true
  - field: related-permissions
    require-if:
      - field: oilgas-permission-types
        in: 
          - renewal-unimplemented
          - renewal-temporary
          - extension-existing-site
          - variation-condition
          - romp-review
          - minerals-development
  - field: other-details
  - field: will-consolidate-permissions
    required: true
  - field: details
    description: Details about the consolidation or update of permissions
    required-if:
      - field: will-consolidate-permissions
        value: true
  - field: related-proposals
    description: Previous permissions for minerals development on the site (if any)
entry-date: 2025-09-09
end-date: ''
rules:
  rule: the field `oilgas-permission-types` must be one or more of the oilgas-permission-type codelist values
  rule: related-permissions is required if oilgas-permission-types includes any of `renewal-unimplemented`, `renewal-temporary`, `extension-existing-site` `variation-condition`, `romp-review` or `minerals-development`
  rule: if `will-consolidate-permissions` is true then `details` is required
---

