---
description: Details of changes to non-residential floorspace in the proposed development.
end-date: ''
entry-date: 2025-07-17
fields:
- field: non-residential-change
  applies-if:
    application-type:
      in:
      - full
      - technical-details-consent
  required: true
- field: non-residential-change-outline
  applies-if:
    application-type:
      in:
      - outline
  required: true
- field: floorspace-details
  applies-if:
    application-type:
      in:
      - full
      - technical-details-consent
  required-if:
  - field: non-residential-change
    value: true
- field: floorspace-details-outline
  applies-if:
    application-type:
      in:
      - outline
  required-if:
  - field: non-residential-change-outline
    value: true
- field: room-details
  applies-if:
    application-type:
      in:
      - full
      - technical-details-consent
  required-if:
  - field: floorspace-details
    description: if floorspace-details contains an item where use is c1, c2, c2a or other
    contains:
      field: use
      in:
      - c1
      - c2
      - c2a
      - other
- field: room-details-outline
  applies-if:
    application-type:
      in:
      - outline
  required-if:
  - field: floorspace-details-outline
    description: if floorspace-details-outline contains an item where use is c1, c2, c2a or other
    contains:
      field: use
      in:
      - c1
      - c2
      - c2a
      - other
module: non-res-floorspace
name: Non residential floorspace
notes: ''
rules:
- condition: non-residential-change != true OR floorspace-details is not empty
  rule: floorspace-details is required when non-residential-change is true
- rule: room-details is required when floorspace-details involves C1, C2, C2A, or "other" use classes
- rule: room-details-outline is required when floorspace-details-outline involves C1, C2, C2A, or "other" use classes
- condition: 'For each floorspace-details: use != ''other'' AND use != ''sui'' OR
    specified-use is not empty'
  rule: specified-use is required when use is other or sui generis
- condition: floorspace-details.existing-gross-floorspace, floorspace-details.floorspace-lost and floorspace-details.total-gross-proposed values >= 0
  rule: Existing, lost and proposed floorspace values must be >= 0
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
