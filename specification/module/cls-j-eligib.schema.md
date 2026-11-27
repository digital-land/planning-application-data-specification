---
module: cls-j-eligib
name: Class J non-domestic roof solar eligibility
description: Roof projection, edge distance, generation capacity and location eligibility information for roof-mounted solar photovoltaic equipment on non-domestic buildings.
entry-date: 2026-11-26
end-date: ''
fields:
  - field: roof-pv-exceeds-proj
    required: true
  - field: roof-pv-within-edge
    required: true
  - field: roof-pv-less-50kw
    required: true
  - field: has-location-restriction
    description: Whether the solar photovoltaic equipment would be installed on any part of the roof of a building that is a scheduled monument (or the site contains one), or a listed building (or within the curtilage of a listed building).
    notes: Use the Class J question and advice in this module body.
    required: true
---

Source: section 4 of the [prior approval form for roof-mounted solar PV on non-domestic buildings, version ECAB 2023](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form052_england_en.pdf).

The new field bodies preserve their source questions and describe the source advice for implementers. These statements record the significance of answers, not a requirement for software to block submission.

For `has-location-restriction`, use the following question and advice:

Would the solar photovoltaic equipment be installed on any part of the roof of a building that is:

- a scheduled monument (or the site contains one);
- a listed building (or within the curtilage of a listed building).

Yes / No

If any answers to the above are yes (true), the proposal will exceed the limits set by legislation. In this circumstance, the application should not continue and applicant should seek advice from the Local Planning Authority on the best course of action.
