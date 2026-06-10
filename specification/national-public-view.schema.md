---
specification: national-public-view
specification-profile: national-public-view
name: National public view
plural: national public view specifications
specification-status: working-draft
consideration: planning-applications-decisions
start-date: ''
end-date: ''
entry-date: 2026-06-10
github-discussion: ''
datasets:
  - dataset: planning-application
    name: planning application
    fields:
      - field: reference
        description: the reference used for the planning application, for example 2025/1674
      - field: description
        description: the description of the proposed development
      - field: application-types
        description: one or more application types that the application covers
      - field: site
        description: the reference to the related site
        dataset: site
      - field: received-date
        description: the date the planning authority received the application
      - field: development-scale
        description: the local planning authority's classification of a full or outline planning application by development scale, where applicable. Either major or minor
      - field: planning-performance-agreement
        description: whether the application was subject to a Planning Performance Agreement
      - field: withdrawn-date
        description: the date the planning application was withdrawn
      - field: linked-applications
        description: references to earlier applications this application directly links to
        dataset: planning-application
      - field: document-url
        description: a URL to the completed application form published by the planning authority, where available
      - field: documentation-url
        description: a URL to the planning authority page where the completed application form or supporting application information can be accessed, where available
  - dataset: site
    name: site
    fields:
      - field: reference
        description: the reference for the site
      - field: name
        description: a plain-language name for the site so it can be referenced in discussions and reports
      - field: address-text
        description: the address for the site, where one is available
      - field: postcode
        description: postcode for the site, where one is available
      - field: description
        description: a plain-language description of the site, where this helps identify the land or buildings
      - field: site-boundary
        description: the boundary geometry for the site
  - dataset: decision-notice
    name: decision notice
    fields:
      - field: reference
        description: the reference for the decision notice
      - field: planning-application
        description: the reference for the planning application the decision notice is for
        dataset: planning-application
      - field: decision
        description: the decision outcome for the planning application
      - field: decision-date
        description: the date the decision notice was issued
      - field: organisation
        description: the organisation issuing the decision notice
      - field: decision-maker
        description: who made the decision
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
        description: a reference for the planning condition
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
        description: the reference for the decision condition
      - field: decision-notice
        description: the reference for the decision notice this condition is attached to
        dataset: decision-notice
      - field: planning-condition
        description: the reference for the linked planning condition record
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
        description: the reference for the section 106 agreement
      - field: decision-notice
        description: the reference for the decision notice tied to the section 106 agreement
        dataset: decision-notice
      - field: document-url
        description: the URL to the published section 106 agreement document
      - field: documentation-url
        description: the URL of the page where the section 106 agreement can be found
  - dataset: planning-application-document
    name: planning application document
    record-inclusion:
      field: public-register-status
      include-values:
        - publish
    fields:
      - field: reference
        description: the reference for the document record
      - field: planning-application
        description: the reference for the related planning application
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
  - dataset: planning-permission-timeline
    name: planning permission timeline
    record-inclusion:
      field: permission-process-event
      include-values:
        codelist: permission-process-event
    fields:
      - field: reference
        description: the reference for the timeline entry
      - field: planning-application
        description: the reference for the related planning application
        dataset: planning-application
      - field: permission-process-event
        description: the type of event in the permission process
      - field: event-date
        description: the date the event occurred
---

The national public view is an explicit extraction from the wider planning
application data standard. Datasets, records and fields are included only where
this schema says they are included.

The publication boundary and rationale for excluded decision-stage fields are
documented in [National public view](../documentation/national-public-view.md).
