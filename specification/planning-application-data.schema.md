---
specification: planning-application-data
name: Planning application data
plural: Planning application data specifications
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
      - field: site
        description: the <a href="#reference">reference</a> for the related site
        dataset: site
      - field: received-date
        description: the date the planning authority received the application
      - field: planning-authority
        description: Identifier of the planning authority that received this planning application
      - field: development-scale
        description: the local planning authority's classification of a full or outline planning application by development scale
        applies-if:
          application-types:
            in:
              - full
              - outline-all
              - outline-some
      - field: planning-performance-agreement
        description: whether the application was subject to a Planning Performance Agreement
      - field: withdrawn-date
        description: the date the planning application was withdrawn
      - field: linked-applications
        description: references to earlier applications this application directly links to
      - field: document-url
        description: a URL to the completed application form
      - field: documentation-url
        description: the URL where supporting documents for the application can be accessed
  - dataset: planning-application-data
    name: planning application data
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the planning application data record
      - field: planning-application
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: submitted-data-uri
        description: the URI identifying the authoritative structured application data as first received by the planning authority
      - field: validated-data-uri
        description: the URI identifying the authoritative structured application data accepted through planning validation
  - dataset: site
    name: site
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the site
      - field: name
        description: Plain-language name for the site so it can be referenced in discussions and reports
      - field: address-text
        description: Plain-language address for the site, where one is available
      - field: postcode
        description: Postcode for the site, where one is available
      - field: description
        description: Plain-language description of the site, where this helps identify the land or buildings
      - field: geometry
        description: the boundary for the site
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
      - field: document-url
        description: the URL to the published section 106 agreement document
      - field: documentation-url
        description: the URL of the page where the section 106 agreement can be found
  - dataset: planning-application-document
    name: planning application document
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the document record
      - field: planning-application
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: document-url
        description: the URL to the document file
      - field: documentation-url
        description: the URL of the page where the document can be found
      - field: name
        description: Title or label used to identify the document
      - field: replaces
        description: Reference to an earlier document record replaced by this document
        dataset: planning-application-document
      - field: public-register-status
        description: Whether the document has been assessed as suitable for public availability on the planning register
  - dataset: planning-permission-timeline
    name: planning permission timeline
    fields:
      - field: reference
        description: the <a href="#reference">reference</a> for the timeline entry
      - field: planning-application
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: permission-process-event
        description: the type of event in the permission process
      - field: event-date
        description: the date the event occurred
      - field: notes
        description: Optional notes that provide additional context about the timeline event
---
