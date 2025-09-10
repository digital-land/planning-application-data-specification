---
description: How the proposed development may affect nearby amenities, air traffic,
  defence assets or protected views.
end-date: ''
entry-date: 2025-07-14
fields:
- description: Description of proposed development including details of proposed work
    and external appearance
  field: description
  required: true
- field: dwellinghouse-height
  required: true
- field: proposed-height
  required: true
- field: impact-on-amenity
  required: true
- field: air-traffic-defence-impacts
  required: true
- field: protected-view-impact
  required: true
module: desc-work-impacts-risks
name: Description of work impacts and risks
rules:
- description: Height measurements must be in metres and positive values
  rule: dwellinghouse-height > 0 AND proposed-height > 0
- description: Proposed height should typically be greater than existing height for
    additional storeys
  rule: proposed-height >= dwellinghouse-height (advisory)
- description: Impact assessments must include mitigation measures where applicable
  rule: impact-on-amenity must include mitigation details where impacts identified
- description: Air traffic and defence impacts must include mitigation measures where
    applicable
  rule: air-traffic-defence-impacts must include mitigation details where impacts
    identified
---