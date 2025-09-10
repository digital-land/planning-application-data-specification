---
description: Details of any other development proposals made for the site
end-date: ''
entry-date: 2025-07-08
fields:
- field: has-related-applications
  required: true
- field: related-applications
  required-if:
    field: has-related-applications
    value: true
module: related-applications
name: Related applications
rules:
- rule: related-applications must be provided when has-related-applications is true
- rule: decision-date is optional and only relevant if the related proposal has been
    decided
---

This module captures information about any related applications, previous proposals, or demolitions that have affected the development site. The `has-related-applications` field determines whether there are any such related matters, and when true, the `related-applications` array provides details of each related application.

For each related proposal, applicants must provide:
- A reference number for the related proposal/application
- A description of what the related proposal involved
- An optional decision date (only if the proposal has been decided)

This information helps planning authorities understand the planning history of the site and any relevant context for assessing the current application.