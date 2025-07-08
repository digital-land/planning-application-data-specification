---
module: advertisement-types
name: Advertisement types
description: |
  Module for capturing information about different types of advertisements 
  proposed, including their counts and descriptions
fields:
  - field: advertisement-proposal-description
    required: true
  - field: advertisement-proposal-type
    required: true
rules:
  - "At least one advertisement-proposal-type entry must be provided"
  - "advertisement-other-description is required when advertisement-type is 'other'"
  - "advertisement-count must be a positive integer"
entry-date: 2025-07-08
end-date: ''
---
