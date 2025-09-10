---
description: Signed and dated verification of the application's accuracy.
end-date: ''
entry-date: 2025-06-12
fields:
- field: name
  required: true
- field: declaration-confirmed
  required: true
- field: declaration-date
  required: true
module: declaration
name: Declaration
rules:
- rule: name must match one of the named individuals in the application
- rule: declaration-date must be in YYYY-MM-DD format
- rule: declaration-date must not be in the future
---