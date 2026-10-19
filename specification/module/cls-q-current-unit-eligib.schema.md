---
module: cls-q-current-unit-eligib
name: Class Q current agricultural unit eligibility
description: Agricultural unit membership history for a prior approval change of use from agricultural buildings to dwellinghouses where the site is currently part of an established agricultural unit.
entry-date: 2026-10-19
end-date: ''
fields:
  - field: cls-q-unit-on-2023-07-24
    required-if:
      - field: cls-q-eligib.cls-q-current-agri-unit
        value: true
  - field: cls-q-unit-10-years
    required: true
    applies-if:
      field: cls-q-unit-on-2023-07-24
      value: false
---

This module captures section 4b of the [prior approval application form for agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf).

Complete this section only if the site is currently part of an established agricultural unit, recorded as `true` in `cls-q-eligib.cls-q-current-agri-unit`. If it is no longer part of an established agricultural unit, complete the former agricultural unit section instead.

Answer `cls-q-unit-10-years` only when `cls-q-unit-on-2023-07-24` is `false`. Preserve the source form's Yes, No and Not applicable options for that answer.

Applicants should not continue with this application route and should seek advice from the local planning authority if they answer:

- `false` to `cls-q-unit-on-2023-07-24` and `no` to `cls-q-unit-10-years`.
