---
description: Why a Lawful Development Certificate is required regarding how the development
  site is being used, or specific works taking place on the site.
end-date: ''
entry-date: 2025-07-17
fields:
- field: ldc-need
  required: true
- field: use
  required-if:
    - any:
      - contains: existing-use
        field: ldc-need
      - contains: breach-con-existing-use
        field: ldc-need
- field: specified-use
  required-if:
    - any:
      - field: use
        value: sui
      - field: use
        value: other
module: use-works-activity
name: Use works activity
notes: ''
rules:
- condition: ldc-need is not empty
  rule: At least one ldc-need value must be provided
- condition: If ldc-need contains 'existing-use' OR 'breach-con-existing-use', then
    use must be provided
  rule: use is required when ldc-need contains existing-use or breach-con-existing-use
- condition: If use == 'sui' OR use == 'other', then specified-use must be provided
  rule: specified-use is required when use is sui or other
---
