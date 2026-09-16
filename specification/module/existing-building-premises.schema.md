---
module: existing-building-premises
name: Existing building premises
description: Addresses of flats and other premises within the existing building, supplied as a structured list or in supporting documents.
entry-date: 2026-09-16
end-date: ''
fields:
  - field: addresses
    description: Addresses of all flats and other premises within the existing building.
    required-if:
      - field: supporting-documents
        operator: empty
  - field: supporting-documents
    description: References to documents supplied with the application containing the complete list of addresses of flats and other premises within the existing building.
    required-if:
      - field: addresses
        operator: empty
rules:
  - rule: At least one of addresses or supporting-documents must contain one or more items.
  - rule: The complete list of addresses must be provided through at least one of these routes.
---

This module captures section 7 of the [Class MA application form, version ECAB 2024.1](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form064_england_en.pdf). It identifies premises within the existing building, rather than neighbouring premises.

Applicants can supply the complete list as structured addresses or as supporting documents referenced from the application document list. Either route is sufficient; both may be provided.
