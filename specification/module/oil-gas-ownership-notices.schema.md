---
description: Ownership, agricultural tenant and public notice details for extraction of oil and gas applications
end-date: ''
entry-date: 2026-06-02
fields:
- field: owners-and-tenants
  description: Owners and agricultural tenants who were served notice
  required: true
- field: valid-posted-notices
  description: Notices posted in each parish or ward and displayed for the required period
  required: true
- field: invalid-posted-notices
  description: Notices that were posted but not displayed for the required period
- field: steps-taken
  description: Steps taken to protect or replace notices that were removed, obscured or defaced
  required-if:
  - field: invalid-posted-notices
    operator: not_empty
- field: newspaper-notices
  description: Newspaper notices published in the area where the land is situated
  required: true
- field: person-reference
  description: Declaration must be made by an applicant or agent making the application
  required: true
- field: declaration-confirmed
  required: true
- field: declaration-date
  required: true
module: oil-gas-ownership-notices
name: Oil and gas ownership and notices
rules:
- rule: valid-posted-notices and invalid-posted-notices must include at least one notice in every parish or ward where the application land is situated
- rule: steps-taken is required when `invalid-posted-notices` is provided
- rule: newspaper-notices.publication-date must not be earlier than 21 days before the application date
- rule: person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- rule: declaration-date must not be in the future
- rule: declaration-confirmed must be `true` for a submission to be valid
---

This module captures the ownership and public notice duties for applications involving development for the winning and working of oil and gas.

The structure is based on [Article 13 of the Town and Country Planning (Development Management Procedure) (England) Order 2015](https://www.legislation.gov.uk/uksi/2015/595/article/13), which requires notice to owners and agricultural tenants, site notices in each parish or ward where the land is situated and newspaper notice where relevant.
