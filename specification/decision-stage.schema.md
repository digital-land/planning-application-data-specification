---
specification: decision-stage
name: Decision stage
plural: decision stage specifications
specification-status: working-draft
consideration: planning-applications-decisions
start-date: ''
end-date: ''
entry-date: 2026-01-09
github-discussion: ''
datasets:
  - dataset: planning-application
    name: planning application
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the planning application
      - field: description
        description: the description of the proposed development
      - field: application-types
        description: one or more codelist values describing the application type
      - field: received-date
        description: the date the planning authority received the application
      - field: document-url
        description: a URL to the completed application form
      - field: documentation-url
        description: the URL where supporting documents for the application can be accessed
  - dataset: site
    name: site
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the site
  - dataset: decision-notice
    name: decision notice
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the decision notice
      - field: planning-application
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: decision
        description: the decision outcome for the planning application
      - field: decision-date
        description: the date the decision notice was issued
      - field: organisation
        description: the organisation issuing the decision notice
      - field: decision-maker
        description: who made the decision (planning authority, Planning Inspectorate, or Secretary of State)
      - field: planning-officer-recommendation
        description: the recommendation made by the planning officer for this application
      - field: document-url
        description: the URL to the published decision notice
      - field: documentation-url
        description: the URL of the page where the decision notice can be found
  - dataset: planning-condition
    name: planning condition
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the planning condition
      - field: name
        description: a plain-language label for the condition
      - field: description
        description: the text of the condition that must be met
      - field: reason
        description: an explanation of why the condition was imposed
      - field: organisation
        description: the organisation responsible for this condition
  - dataset: decision-condition
    name: decision condition
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the decision condition
      - field: decision-notice
        description: the <a href="#reference">reference</a> for the decision notice this condition is attached to
        dataset: decision-notice
      - field: planning-condition
        description: the <a href="#reference">reference</a> for the linked planning condition record
        dataset: planning-condition
      - field: organisation
        description: the organisation responsible for this condition within the decision
      - field: requested-by
        description: identifier of the body requesting the condition
      - field: discharged-by
        description: identifier of the body discharging the condition
  - dataset: section-106
    name: section 106 agreement
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the section 106 agreement
      - field: decision-notice
        description: the <a href="#reference">reference</a> for the decision notice tied to the section 106 agreement
        dataset: decision-notice
---
