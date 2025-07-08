---
module: con-remove-vary
name: Condition removal or variation
description: |
  Information about why applicant wishes planning condition(s) to be removed or changed,
  and how the condition should vary for s73 applications
fields:
  - field: reason
    description: The reason why the applicant wishes condition(s) to be removed or changed
    required: true
  - field: condition-change
rules:
  - "Reason must explain why the applicant wishes condition(s) to be removed or changed"
  - "Condition change should specify how the condition should vary if modification is sought"
entry-date: 2025-07-08
end-date: ''
---
