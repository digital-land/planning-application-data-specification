---
module: desc-existing-use
name: Description of existing use
description: |
  Information about the existing uses of the development site, including 
  use classes and which parts of the land they relate to
fields:
  - field: existing-use-details
    required: true
rules:
  - description: "At least one existing use must be provided"
    rule: "existing-use-details must contain at least one item"
  - description: "use-details is required when use is 'sui' or 'other'"
    rule: "if use == 'sui' OR use == 'other' then use-details is required"
entry-date: 2025-07-09
end-date: ''
---
