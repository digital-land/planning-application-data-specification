---
description: Details of changes to non-residential floorspace in the proposed development.
end-date: ''
entry-date: 2025-07-17
fields:
- applies-if:
    application-type:
      in:
      - full
  field: non-residential-change
  required: true
- applies-if:
    application-type:
      in:
      - outline
  field: non-residential-change-outline
  required: true
- applies-if:
    application-type:
      in:
      - full
  field: floorspace-details
  required-if:
  - field: non-residential-change
    value: true
- applies-if:
    application-type:
      in:
      - outline
  field: floorspace-details-outline
  required-if:
  - field: non-residential-change-outline
    value: true
- applies-if:
    application-type:
      in:
      - full
  field: room-details
  required-if:
    condition: floorspace-details contains use-class in ["C1", "C2", "C2A", "other"]
- applies-if:
    application-type:
      in:
      - outline
  field: room-details-outline
  required-if:
    condition: floorspace-details contains use-class in ["C1", "C2", "C2A", "other"]
module: non-res-floorspace
name: Non residential floorspace
notes: ''
rules:
- condition: non-residential-change != true OR floorspace-details is not empty
  rule: floorspace-details is required when non-residential-change is true
- condition: If any floorspace-details.use-class in ['C1', 'C2', 'C2A', 'other'],
    then room-details must be provided
  rule: room-details is required when floorspace involves C1, C2, C2A, or other use
    classes
- condition: 'For each floorspace-details: use != ''other'' AND use != ''sui'' OR
    specified-use is not empty'
  rule: specified-use is required when use is other or sui generis
- condition: All existing-gross-floorspace, floorspace-lost, total-gross-proposed,
    net-additional-floorspace >= 0
  rule: All floorspace values must be 0 or positive
- condition: All existing-rooms-lost, total-rooms-proposed, net-additional-rooms >=
    0
  rule: All room values must be 0 or positive
- condition: 'For each floorspace-details: net-additional-floorspace == (total-gross-proposed
    - existing-gross-floorspace)'
  rule: net-additional-floorspace must equal total-gross-proposed minus existing-gross-floorspace
- condition: 'For each room-details: net-additional-rooms == (total-rooms-proposed
    - existing-rooms-lost)'
  rule: net-additional-rooms must equal total-rooms-proposed minus existing-rooms-lost
---