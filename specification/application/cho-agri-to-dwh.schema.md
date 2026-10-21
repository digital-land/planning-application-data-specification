---
application: cho-agri-to-dwh
extends: prior-approval
name: 'Prior approval: Agricultural or former agricultural buildings to dwellinghouses'
description: Prior approval for a change of use from agricultural or former agricultural buildings to dwellinghouses under Class Q, including associated building works.
entry-date: 2026-10-20
start-date: ''
end-date: ''
legislation:
  - https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/3
fields:
  - field: submission-details
    required: true
modules:
  - module: cls-q-agri-tenancies
  - module: cls-q-current-unit-eligib
  - module: cls-q-dwelling-limits
  - module: cls-q-eligib
  - module: cls-q-former-unit-eligib
  - module: cls-q-works-impacts
rules:
  - rule: Written confirmations from all relevant landlords and tenants consenting to the change of use must be included in submission-details.documents if cls-q-agri-tenancies.agricultural-tenants and cls-q-agri-tenancies.tenancy-parties-consent are both true.
  - rule: Written confirmations from all relevant landlords and tenants agreeing that the site is no longer required for any agricultural use must be included in submission-details.documents if cls-q-agri-tenancies.cls-q-tenancy-terminated and cls-q-agri-tenancies.cls-q-agri-use-not-required are both true.
  - rule: A site-specific flood risk assessment in submission-details.documents is required if the site is in Flood Zone 2 or 3 or an area with critical drainage problems.
allow-additional-properties: true
---

This application definition covers the [prior approval application form for agricultural or former agricultural buildings to dwellinghouses (Class Q), version ECAB 2024.2](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form044_england_en.pdf). It inherits applicant, agent, contact, site, checklist and declaration information from `prior-approval`. The inherited `conflict-of-interest` module is retained, although it is not present in this paper form.
