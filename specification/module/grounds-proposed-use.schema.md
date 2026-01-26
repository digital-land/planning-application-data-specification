---
description: What the new site will be used for
end-date: ''
entry-date: 2025-07-17
fields:
- description: State proposed use class
  field: use
- field: specified-use
  required-if:
    - any:
      - field: use
        value: sui
      - field: use
        value: other
- field: operation-type
  required: true
- field: temporary-details
- field: reason
  required: true
module: grounds-proposed-use
name: Grounds for proposed use
rules:
- rule: specified-use is required if use is 'sui' or 'other'
- rule: temporary-details is required if operation-type is 'temporary'
---
