---
module: ma-building-eligibility
name: Class MA current building and site eligibility
description: The qualifying use history and location restrictions of the existing building and site for a Class MA change of use from commercial, business and service use to dwellinghouses.
entry-date: 2026-09-15
end-date: ''
fields:
  - field: use-two-years-plus
    required: true
  - field: has-location-restriction
    required: true
---

This module captures section 4a of the [Class MA application form, version ECAB 2024.1](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form064_england_en.pdf). The field definitions describe the qualifying uses and location restrictions.

The source form advises applicants not to continue with this application route and to seek advice from the local planning authority if:

- `use-two-years-plus` is false.
- `has-location-restriction` is true.
