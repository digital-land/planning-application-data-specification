---
description: |
  If making an 'outline' application, how waste will be managed on the development site
end-date: ''
entry-date: 2025-07-14
fields:
- field: site-activity-details
  required: true
- field: proposal-waste-management-outline
  required: true
- field: waste-management-outline
- field: waste-streams
module: processes-machinery-waste-outline
name: Processes machinery waste
notes: |
  If no waste management facility is applicable, the applicant answers that at section level.
  If waste management is applicable, they add one or more entries only for the facilities they need to describe.
  They should not be expected to work through the full codelist and mark each remaining facility not applicable.
rules:
- description: waste-management-outline must contain one or more applicable facility
    entries when proposal-waste-management-outline is true
  rule: if proposal-waste-management-outline == true then waste-management-outline
    is required
- description: waste-streams is required when proposal-waste-management-outline is
    true
  rule: if proposal-waste-management-outline == true then waste-streams is required
---
