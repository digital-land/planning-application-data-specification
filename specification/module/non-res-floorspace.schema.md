---
module: non-res-floorspace
name: Non residential floorspace
description: Information about non-residential floorspace changes including use class details and room counts for specific accommodation types
entry-date: 2025-07-17
end-date: ''
notes: ''
fields:
  - field: non-residential-change
    required: true
  - field: floorspace-details
    required-if:
      - field: non-residential-change
        value: true
  - field: room-details
    required-if:
      condition: floorspace-details contains use-class in ["C1", "C2", "C2A", "other"]
rules:
  - rule: "floorspace-details is required when non-residential-change is true"
    condition: "non-residential-change != true OR floorspace-details is not empty"
  - rule: "room-details is required when floorspace involves C1, C2, C2A, or other use classes"
    condition: "If any floorspace-details.use-class in ['C1', 'C2', 'C2A', 'other'], then room-details must be provided"
  - rule: "specified-use is required when use is other or sui generis"
    condition: "For each floorspace-details: use != 'other' AND use != 'sui' OR specified-use is not empty"
  - rule: "All floorspace values must be 0 or positive"
    condition: "All existing-gross-floorspace, floorspace-lost, total-gross-proposed, net-additional-floorspace >= 0"
  - rule: "All room values must be 0 or positive"
    condition: "All existing-rooms-lost, total-rooms-proposed, net-additional-rooms >= 0"
  - rule: "net-additional-floorspace must equal total-gross-proposed minus existing-gross-floorspace"
    condition: "For each floorspace-details: net-additional-floorspace == (total-gross-proposed - existing-gross-floorspace)"
  - rule: "net-additional-rooms must equal total-rooms-proposed minus existing-rooms-lost"
    condition: "For each room-details: net-additional-rooms == (total-rooms-proposed - existing-rooms-lost)"
---
