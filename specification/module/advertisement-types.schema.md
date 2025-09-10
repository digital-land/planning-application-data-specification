---
description: What type of advertisements are proposed and how many there will be.
end-date: ''
entry-date: 2025-07-08
fields:
- field: advertisement-proposal-description
  required: true
- field: advertisement-proposal-type
  required: true
module: advertisement-types
name: Advertisement types
rules:
- At least one advertisement-proposal-type entry must be provided
- advertisement-other-description is required when advertisement-type is 'other'
- advertisement-count must be a positive integer
---