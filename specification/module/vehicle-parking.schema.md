---
description: Details of current parking facilities at the site and any changes that
  would be made by the proposed development.
end-date: ''
entry-date: 2025-07-08
fields:
- field: parking-spaces
  required: true
module: vehicle-parking
name: Vehicle parking
rules:
- description: vehicle-type-other is required when parking-space-type is 'other'
  rule: if parking-space-type == 'other' then vehicle-type-other is required
- description: Numeric fields must be 0 or positive
  rule: total-existing >= 0 AND total-proposed >= 0 AND (unknown-proposed is empty
    OR unknown-proposed >= 0)
- description: difference-in-spaces should equal total-proposed minus total-existing
  rule: difference-in-spaces == (total-proposed - total-existing)
---