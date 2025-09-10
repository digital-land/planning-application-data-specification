---
description: If making an 'outline' application, how waste will be managed on the
  development site
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
rules:
- description: waste-management-outline is required when proposal-waste-management-outline
    is true
  rule: if proposal-waste-management-outline == true then waste-management-outline
    is required
- description: waste-streams is required when proposal-waste-management-outline is
    true
  rule: if proposal-waste-management-outline == true then waste-streams is required
---