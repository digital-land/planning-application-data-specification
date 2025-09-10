---
description: Any additional information which will help with the planning application
end-date: ''
entry-date: 2025-06-26
fields:
- field: replacement-drawings
  required: true
module: supporting-info
name: Supporting information
rules:
- rule: old-drawing-reference references must match existing approved drawing identifiers
- rule: new-drawing-reference references must match documents in application.documents
- rule: Each old-drawing-reference reference must be unique within replacement-drawings
    array
---