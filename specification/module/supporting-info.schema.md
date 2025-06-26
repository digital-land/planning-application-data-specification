---
module: supporting-info
name: Supporting information
description: |
  Information to support the application, including details of approved 
  drawings being replaced by new drawings
fields:
  - field: replacement-drawings
    required: true
rules:
  - rule: "old-drawing-reference references must match existing approved drawing identifiers"
  - rule: "new-drawing-reference references must match documents in application.documents"
  - rule: "Each old-drawing-reference reference must be unique within replacement-drawings array"
entry-date: 2025-06-26
end-date: ''
---
