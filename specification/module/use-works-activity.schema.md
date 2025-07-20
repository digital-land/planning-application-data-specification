---
module: use-works-activity
name: Use works activity
description: Information about what the lawful development certificate is needed for and related use details
entry-date: 2025-07-17
end-date: ''
notes: ''
fields:
  - field: ldc-need
    required: true
  - field: use
    required-if:
      any:
        - field: ldc-need
          contains: existing-use
        - field: ldc-need
          contains: breach-con-existing-use
  - field: specified-use
    required-if:
      any:
        - field: use
          value: sui
        - field: use
          value: other
rules:
  - rule: "At least one ldc-need value must be provided"
    condition: "ldc-need is not empty"
  - rule: "use is required when ldc-need contains existing-use or breach-con-existing-use"
    condition: "If ldc-need contains 'existing-use' OR 'breach-con-existing-use', then use must be provided"
  - rule: "specified-use is required when use is sui or other"
    condition: "If use == 'sui' OR use == 'other', then specified-use must be provided"
---
