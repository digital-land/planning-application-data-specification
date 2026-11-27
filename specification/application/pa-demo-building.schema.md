---
application: pa-demo-building
extends: prior-approval
name: 'Prior approval: Demolition of buildings'
description: Prior approval for the demolition of buildings.
notes: Class B (demolition of buildings)
entry-date: 2026-11-27
start-date: ''
end-date: ''
legislation:
  - https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/11
fields:
  - field: submission-details
    required: true
  - field: additional-data
modules:
  - module: demolition-works
  - module: pre-app-advice
  - module: site-visit
allow-additional-properties: false
---

This definition covers the [prior approval form for demolition of buildings, version ECAB 2019.1 RP](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form022_england_en.pdf).
