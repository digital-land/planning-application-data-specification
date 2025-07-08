---
module: related-proposals
name: Related proposals
description: |
  Information about related applications, previous proposals or demolitions for the site, including whether such proposals exist and details of any related applications
fields:
  - field: has-related-proposals
    required: true
  - field: related-proposals
    applies-if:
      field: has-related-proposals
      value: true
validation:
  - rule: "related-proposals must be provided when has-related-proposals is true"
  - rule: "decision-date is optional and only relevant if the related proposal has been decided"
entry-date: 2025-07-08
end-date: ''
---

This module captures information about any related applications, previous proposals, or demolitions that have affected the development site. The `has-related-proposals` field determines whether there are any such related matters, and when true, the `related-proposals` array provides details of each related application.

For each related proposal, applicants must provide:
- A reference number for the related proposal/application
- A description of what the related proposal involved
- An optional decision date (only if the proposal has been decided)

This information helps planning authorities understand the planning history of the site and any relevant context for assessing the current application.
