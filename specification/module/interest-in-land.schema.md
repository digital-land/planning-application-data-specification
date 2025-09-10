---
description: Whether the applicant owns or has permission to use the land where the
  proposed advertisement will be placed
end-date: ''
entry-date: 2025-07-08
fields:
- field: applicant-owns-land
  required: true
- field: permission-obtained
  required-if:
    field: applicant-owns-land
    value: false
- field: permission-not-obtained-details
  required-if:
    field: permission-obtained
    value: false
module: interest-in-land
name: Interest in land
rules:
- rule: permission-obtained must be provided when applicant-owns-land is false
- rule: permission-not-obtained-details must be provided when applicant-owns-land
    is false and permission-obtained is false
---

This module captures information about the applicant's legal interest in the land where an advertisement will be displayed. It determines whether the applicant owns the land, and if not, whether they have obtained permission from the land owner.

The conditional logic ensures that:
- If the applicant does not own the land, they must indicate whether permission has been obtained
- If permission has not been obtained, details must be provided explaining the circumstances

This information helps planning authorities understand the legal basis for the proposed advertisement and whether appropriate permissions are in place.