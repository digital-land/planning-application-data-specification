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
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the planning application
      - field: name
        requirement-level: SHOULD
        description: A plain-language label for the planning application so it can be identified without relying on its reference
      - field: description
        requirement-level: MUST
        description: the description of the proposed development
      - field: application-types
        requirement-level: MUST
        description: one or more codelist values describing the application type
      - field: site
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the related site
        dataset: site
      - field: received-date
        requirement-level: MUST
        description: the date the planning authority received the application
      - field: planning-authority
        requirement-level: MUST
        description: Identifier of the planning authority that received this planning application
      - field: officer-name
        name: Case officer
        description: Name of the planning officer responsible for handling the application
      - field: development-scale
        requirement-level: SHOULD
        description: the local planning authority's classification of a full or outline planning application by development scale
        applies-if:
          application-types:
            in:
              - full
              - outline-all
              - outline-some
      - field: planning-performance-agreement
        requirement-level: MUST
        description: whether the application was subject to a Planning Performance Agreement
      - field: withdrawn-date
        requirement-level: SHOULD
        description: the date the planning application was withdrawn
      - field: linked-applications
        requirement-level: MUST
        description: references to earlier applications this application directly links to
        dataset: planning-application
      - field: document-url
        requirement-level: SHOULD
        description: a URL to the completed application form
      - field: documentation-url
        requirement-level: MUST
        description: the URL where supporting documents for the application can be accessed
      - field: notes
        requirement-level: MAY
        description: Optional notes that provide additional context about the planning application
  - dataset: planning-application-data
    name: planning application data
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the planning application data record
      - field: planning-application
        requirement-level: MUST
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
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the site
      - field: name
        description: Plain-language name for the site so it can be referenced in discussions and reports
        requirement-level: SHOULD
      - field: address-text
        requirement-level: MUST
        description: Plain-language address or description that helps identify the site location
      - field: postcode
        requirement-level: SHOULD
        description: Postcode for the site, where one is available
      - field: uprns
        requirement-level: SHOULD
        description: UPRNs for existing properties and premises within the site boundary, where known
      - field: usrns
        requirement-level: SHOULD
        description: USRNs for streets associated with the site, where known
      - field: geometry
        requirement-level: MUST
        description: the boundary for the site
  - dataset: decision-notice
    name: decision notice
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the decision notice
      - field: planning-application
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: decision
        requirement-level: MUST
        description: the decision outcome for the planning application
      - field: decision-date
        requirement-level: MUST
        description: the date the decision notice was issued
      - field: organisation
        requirement-level: MUST
        description: the organisation issuing the decision notice
      - field: decision-maker
        requirement-level: MUST
        description: the category of person or body that formally made the decision
      - field: planning-officer-recommendation
        requirement-level: SHOULD
        description: the recommendation made by the planning officer for this application
      - field: document-url
        requirement-level: SHOULD
        description: the URL to the published decision notice
      - field: documentation-url
        requirement-level: MUST
        description: the URL of the page where the decision notice can be found
      - field: notes
        requirement-level: MAY
        description: Optional notes that provide additional context about the decision notice
  - dataset: planning-condition
    name: planning condition
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the planning condition
      - field: name
        description: a plain-language label for the condition
        requirement-level: SHOULD
      - field: description
        requirement-level: MUST
        description: the text of the condition that must be met
      - field: reason
        requirement-level: MUST
        description: an explanation of why the condition was imposed
      - field: organisation
        requirement-level: MUST
        description: the organisation responsible for this condition
  - dataset: decision-condition
    name: decision condition
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the decision condition
      - field: decision-notice
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the decision notice this condition is attached to
        dataset: decision-notice
      - field: planning-condition
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the linked planning condition record
        dataset: planning-condition
      - field: organisation
        description: the organisation responsible for this condition within the decision
      - field: requested-by
        description: identifier of the body requesting the condition
      - field: discharged-by
        requirement-level: MUST
        description: reference to the decision notice discharging the condition
        dataset: decision-notice
  - dataset: section-106
    name: section 106 agreement
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the section 106 agreement
      - field: name
        requirement-level: SHOULD
        description: Title or plain-language label for the section 106 agreement so it can be identified
      - field: decision-notice
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the decision notice tied to the section 106 agreement
        dataset: decision-notice
      - field: document-url
        requirement-level: SHOULD
        description: the URL to the published section 106 agreement document
      - field: documentation-url
        requirement-level: MUST
        description: the URL of the page where the section 106 agreement can be found
  - dataset: planning-application-document
    name: planning application document
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the document record
      - field: planning-application
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: document-url
        requirement-level: SHOULD
        description: the URL to the document file
      - field: documentation-url
        requirement-level: MUST
        description: the URL of the page where the document can be found
      - field: name
        requirement-level: MUST
        description: Title or label used to identify the document
      - field: replaces
        requirement-level: MUST
        description: Reference to an earlier document record replaced by this document
        dataset: planning-application-document
      - field: public-register-status
        requirement-level: MUST
        description: Whether the document has been assessed as suitable for public availability on the planning register
  - dataset: planning-permission-timeline
    name: planning permission timeline
    fields:
      - field: reference
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the timeline entry
      - field: planning-application
        requirement-level: MUST
        description: the <a href="#reference">reference</a> for the related planning application
        dataset: planning-application
      - field: permission-process-event
        requirement-level: MUST
        description: the type of event in the permission process
      - field: event-date
        requirement-level: MUST
        description: the date the event occurred
      - field: notes
        description: Optional notes that provide additional context about the timeline event
---
