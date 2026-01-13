---
dataset: national-planning-requirement
name: National planning requirement
plural: National planning requirements
description: >
  A dataset that maps national planning requirements to specific types and sub-types
  of planning applications. This is used to determine which documents are required
  under national regulations depending on the application context.
fields:
  - field: reference
    description: A unique reference identifier for the national planning requirement entry
  - field: application-type
    description: The high-level type of application (e.g. full, outline, reserved-matters)
    dataset: planning-application-type
  - field: application-sub-type
    description: A more specific sub-type of application, if applicable.
  - field: planning-requirement
    description: The identifier for the related planning requirement (e.g. site-plan, biodiversity-survey-report).
  - field: entry-date
    description: The date this record was added to the dataset (ISO 8601 format).
  - field: start-date
    description: The effective date from which this requirement applies (if different from entry-date).
  - field: end-date
    description: The date on which this requirement ceased to apply, if applicable.
---
