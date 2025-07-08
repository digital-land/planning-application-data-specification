---
module: community-consultation
name: Community consultation
description: |
  Information about community consultation activities carried out in relation to the planning application
fields:
  - field: have-consulted
    required: true
  - field: description
    description: Provide details of the community consultation
    required-if:
      - field: have-consulted
        value: true
rules:
  - "Description is required when have-consulted is true"
  - "Description should provide details of the consultation activities undertaken"
entry-date: 2025-07-08
end-date: ''
---
