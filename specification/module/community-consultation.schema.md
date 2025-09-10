---
description: What community consultation activities have taken place as part of the
  application
end-date: ''
entry-date: 2025-07-08
fields:
- field: have-consulted
  required: true
- description: Provide details of the community consultation
  field: description
  required-if:
  - field: have-consulted
    value: true
module: community-consultation
name: Community consultation
rules:
- Description is required when have-consulted is true
- Description should provide details of the consultation activities undertaken
---