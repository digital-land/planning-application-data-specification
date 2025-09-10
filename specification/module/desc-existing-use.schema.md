---
description: How the development site is used, including use class information
end-date: ''
entry-date: 2025-07-09
fields:
- field: existing-use-details
  required: true
module: desc-existing-use
name: Description of existing use
rules:
- description: At least one existing use must be provided
  rule: existing-use-details must contain at least one item
- description: use-details is required when use is 'sui' or 'other'
  rule: if use == 'sui' OR use == 'other' then use-details is required
---