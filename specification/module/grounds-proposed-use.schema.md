---
module: grounds-proposed-use
name: Grounds for proposed use
description: |
  Information about the proposed use class, operation type, and supporting reasoning for lawful development certificate applications
fields:
  - field: use
    description: State proposed use class
  - field: specified-use
    required-if:
      any:
        - field: use
          value: sui
        - field: use
          value: other
  - field: operation-type
    required: true
  - field: temporary-details
  - field: reason
    required: true
rules:
  - rule: "specified-use is required if use is 'sui' or 'other'"
  - rule: "temporary-details is required if operation-type is 'temporary'"
entry-date: 2025-07-17
end-date: ''
---
