---
module: cls-q-eligib
name: Class Q general eligibility
description: General agricultural unit, building, extension, access and location eligibility information for a Class Q change of use to dwellinghouses.
entry-date: '2026-10-18'
end-date: ''
fields:
- field: cls-q-current-agri-unit
  required: true
- field: cls-q-agri-pd-10-years
  required: true
- field: cls-q-dimensions-exceeded
  required: true
- field: cls-q-extension-exceeded
  required: true
- field: has-suitable-highway-access
  required: true
- field: cls-q-existing-space-capable
  required: true
- field: has-location-restriction
  description: Whether any part of the land, site or building is affected by a location restriction listed for Class Q.
  notes: Use the Class Q question and restriction list in the field body. The source form advises applicants answering Yes not to continue and to seek advice from the local planning authority.
  required: true
---

This module captures section 4a of the [Class Q application form, version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf). The field bodies preserve the source questions and their subconditions.

Applicants should not continue with this application route and should seek advice from the local planning authority if they answer:

- `true` to `cls-q-agri-pd-10-years`.
- `true` to `cls-q-dimensions-exceeded`.
- `yes` to `cls-q-extension-exceeded`.
- `false` to `has-suitable-highway-access`.
- `false` to `cls-q-existing-space-capable`.
- `true` to `has-location-restriction`.
