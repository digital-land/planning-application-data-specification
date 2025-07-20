---
module: vehicle-parking
name: Vehicle parking
description: |
  Detailed information about parking spaces by vehicle type, including existing 
  and proposed counts with net change calculations
fields:
  - field: parking-spaces
    required: true
entry-date: 2025-07-08
end-date: ''
rules:
  - description: "vehicle-type-other is required when parking-space-type is 'other'"
    rule: "if parking-space-type == 'other' then vehicle-type-other is required"
  - description: "Numeric fields must be 0 or positive"
    rule: "total-existing >= 0 AND total-proposed >= 0 AND (unknown-proposed is empty OR unknown-proposed >= 0)"
  - description: "difference-in-spaces should equal total-proposed minus total-existing"
    rule: "difference-in-spaces == (total-proposed - total-existing)"
---
