---
application: cho-commercial-to-dwh
extends: prior-approval
name: 'Prior approval: Commercial, business and service use to dwellinghouses'
description: Prior approval for a change of use from Commercial, Business and Service use (Use Class E) to dwellinghouses (Use Class C3) under Class MA.
entry-date: 2026-09-17
start-date: ''
end-date: ''
legislation:
  - https://www.legislation.gov.uk/uksi/2015/596/schedule/2/part/3
fields:
  - field: submission-details
    required: true
modules:
  - module: agricultural-tenancy-consent
  - module: existing-building-premises
  - module: ma-building-eligibility
  - module: ma-proposal-eligibility
  - module: ma-works-impacts
rules:
  - rule: ma-works-impacts.fire-safety-impacts and a fire statement in submission-details.documents are required if the resulting building contains more than one dwellinghouse and is either at least 18 metres high or has at least 7 storeys.
  - rule: ma-works-impacts.conservation-area-impacts is required if the building is in a conservation area and the change of use affects all or part of the ground floor.
  - rule: ma-works-impacts.industrial-area-impacts is required if the building is in an area currently used for general or heavy industry, waste management, storage and distribution or a mix of these uses.
  - rule: ma-works-impacts.local-service-loss-impacts is required if the proposal involves the loss of services provided by a registered nursery or health centre.
  - rule: A site-specific flood risk assessment in submission-details.documents is required if the site is in Flood Zone 2 or 3 or an area with critical drainage problems.
  - rule: Written confirmations of consent from all relevant parties must be included in submission-details.documents if agricultural-tenancy-consent.agricultural-tenants and agricultural-tenancy-consent.tenancy-parties-consent are both true.
allow-additional-properties: true
---

This application definition covers the [Class MA application form, version ECAB 2024.1](https://ecab.planningportal.co.uk/uploads/appPDF/E2734Form064_england_en.pdf). It inherits applicant, agent, contact, site, checklist and declaration information from `prior-approval`. The inherited `conflict-of-interest` module is also retained, although it is not present in this paper form.
