---
module: cls-q-former-unit-eligib
name: Class Q former agricultural unit eligibility
description: Agricultural unit membership history and subsequent use for a prior approval change of use from agricultural buildings to dwellinghouses where the site was formerly part of an established agricultural unit.
entry-date: 2026-10-20
end-date: ''
fields:
  - field: cls-q-unit-on-2023-07-24
    required-if:
      - field: cls-q-eligib.cls-q-current-agri-unit
        value: false
  - field: cls-q-ceased-10-years
    required: true
    applies-if:
      field: cls-q-unit-on-2023-07-24
      value: true
  - field: cls-q-non-agri-use
    required-if:
      - field: cls-q-eligib.cls-q-current-agri-unit
        value: false
---

This module captures the former established agricultural unit section on page 3 of the [prior approval application form for agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf). The form's navigation calls this section 4c, although its printed heading repeats 4b.

The source form states: “This question should only be completed if the site was formerly part of an established agricultural unit.” Section 4a directs applicants answering No to the current agricultural unit question to this section. Accordingly, the dated membership and subsequent-use answers are required when `cls-q-eligib.cls-q-current-agri-unit` is `false`. These requiredness conditions do not mechanically prohibit answers in the other branch.

The source's “If yes” instruction makes `cls-q-ceased-10-years` applicable and required only when `cls-q-unit-on-2023-07-24` is `true`. Preserve the source form's Yes, No and Not applicable options for that answer.

Applicants should not continue with this application route and should seek advice from the local planning authority if they answer:

- `no` to `cls-q-ceased-10-years`.
- `true` to `cls-q-non-agri-use`.
