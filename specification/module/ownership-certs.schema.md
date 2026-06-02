---
description: Who will be affected by the proposal and whether they have been notified,
  such as agricultural tenants
end-date: ''
entry-date: 2025-06-13
fields:
- field: sole-owner
  required: true
- field: agricultural-tenants
  applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
  required: true
- field: owners-and-tenants
  applies-if:
    application-type:
      in:
      - hh
      - full
      - technical-details-consent
      - outline
      - demolition-con-area
      - s73
      - extraction-oil-gas
- field: lbc-owners
  applies-if:
    application-type:
      in:
      - lbc
- field: ownership-cert-option
  notes: Certificate type determined by ownership and notification status
- field: steps-taken
  required-if:
    - description: Required for Certificate-C or Certificate-D
      field: ownership-cert-option
      in: 
      - certificate-c
      - certificate-d
- field: newspaper-notices
  required-if:
    - description: Required for Certificate-C or Certificate-D
      field: ownership-cert-option
      in: 
      - certificate-c
      - certificate-d
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
