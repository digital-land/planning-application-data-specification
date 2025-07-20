---
module: grounds-ldc
name: Grounds for lawful development certificate
description: |
  Grounds on which a lawful development certificate is being sought,
  including supporting evidence and explanations
fields:
  - field: grounds-pre-2024
  - field: grounds-post-2024
  - field: other-details
    required-if:
      - field: grounds-pre-2024
        contains: other
      - field: grounds-post-2024
        contains: other
  - field: supporting-applications
  - field: reason
    required: true
rules:
  - description: "At least one ground must be selected from either pre-2024 or post-2024 lists"
    rule: "grounds-pre-2024 is not empty OR grounds-post-2024 is not empty"
  - description: "other-details is required when 'other' is selected in any grounds list"
    rule: "if grounds-pre-2024 contains 'other' OR grounds-post-2024 contains 'other' then other-details is required"
entry-date: 2025-07-10
end-date: ''
---
