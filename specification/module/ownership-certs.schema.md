---
description: Who will be affected by the proposal and whether they have been notified,
  such as agricultural tenants
end-date: ''
entry-date: 2025-06-13
fields:
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: sole-owner
  required: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
  field: agricultural-tenants
  required: true
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
  field: owners-and-tenants
- applies-if:
    application-type:
      in:
      - lbc
  field: lbc-owners
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: steps-taken
  notes: Required for Certificate-C or Certificate-D
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: newspaper-notices
  notes: Required for Certificate-C or Certificate-D
- applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - lbc
      - s73
      - extraction-oil-gas
  field: ownership-cert-option
  notes: Certificate type determined by ownership and notification status
- field: person-reference
  description: Declaration must be made by an applicant or agent making the application
  required: true
- field: declaration-confirmed
  required: true
- field: declaration-date
  required: true
module: ownership-certs
name: Ownership certificates and agricultural land declaration
rules:
- rule: person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`
- rule: declaration-date must be in YYYY-MM-DD format
- rule: declaration-date must not be in the future
- rule: declaration-confirmed must be `true` for a submission to be valid
---
