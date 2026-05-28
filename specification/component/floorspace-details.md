---
component: floorspace-details
name: Floorspace details
description: Details of non-residential floorspace changes by use class including existing, lost, and proposed amounts
entry-date: '2025-07-17'
end-date: ''
notes: ''
fields:
  - field: use
    required: true
  - field: specified-use
    notes: should this be use-other?
    required-if:
      description: use == "other" OR use == "sui"
      any:
        - field: use
          contains: sui
        - field: use
          contains: other
  - field: existing-gross-floorspace
    required: true
  - field: floorspace-lost
    required: true
  - field: total-gross-proposed
    required: true
  - field: net-additional-floorspace
    required: true
---

Floorspace detail entries are only expected where the use class applies to the proposal.

Generated PDF or paper forms may still render "not applicable" controls for each possible option. That is presentation and capture logic, rather than a requirement for the canonical submission data model.
