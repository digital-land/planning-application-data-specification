# Applications

_Note: how we define applications is still being worked on_

As we move from narrative specifications to declarative models, we need a consistent way to describe applications. 

The pplication interface defines the application, what legislation underpins it and what is required to submit an application of that type - including any specific fields for that application and the required modules.


## Benefits

Like [modules](module.md), applications benefit from being:

* **Explicit** it clearly states what is required
* **Reuse** of modules across applications types make the data mmore consistent
* **Testable** can drive conformance checks and interface expectations
* **Supports validation and guidance** generation for applicants and services


Breaking that down some of the benefits include:

For MHCLG and admins:

* reusable, explicit module definitions
* easier validation, and documentation
* more consistent data
* clarity of what is required

For suppliers and community:

* clear contract of what’s required, and when
* easier to validate payloads against requirements
* helps everyone "speak the same language" when it comes to data

## Decision made

**Applications should be defined by MHCLG**
Each application is defined in legislation and MHCLG should use that to define what is required to be submitted for the application

**Attributes of module definitions**

* `application` -  unique identifier for the application (e.g. `hh`)
* `name`
* `description`
* `synonyms` - other names used for the application type
* `legislation` - a link to the legislation that defines the application type
* `fields[]` - list of field references
* `modules` - a list of modules an applicant needs to complete
* `entry-date`
* `end-date` - for deprecating applications
* `rules`

**Applications should reference fields and modules by ID**
With the field and modules definitions defined elsewhere.

### Still to decide

* If we need `fields` and `modules` need to be separate lists. The `fields` list is always going to reference the `application` field. And arguably the `modules` are top-level fields that break down into substructures
* Should the definition include other details that could be useful for submission and back-office systems, such as, details of the expected turn around times, so that these are also codified?

### Examples

The `hh` application
```yaml
---
application: hh
name: Householder planning application
description: A simplified process for applications to alter or enlarge a single house (but not a flat), including works within the boundary/garden
synonyms: []
legislation:
  - https://www.legislation.gov.uk/ukpga/1990/8/section/62
notes: ''
entry-date: 2025-01-07
start-date: ''
end-date: ''
fields:
  - field: application
    required: true
modules:
  - module: access-rights-of-way
  - module: agent-contact
  - module: agent-details
  - module: applicant-contact
  - module: applicant-details
  - module: bng
  - module: checklist
  - module: conflict-of-interest
  - module: declaration
  - module: materials
  - module: ownership-certs
  - module: parking
  - module: pre-app-advice
  - module: proposal-details
  - module: site-details
  - module: site-visit
  - module: trees-hedges
---
```

### Validation rules for module (or component) definitions

* `fields` attribute must have `application`
* each `field` of `fields` must be defined in the set of specification fields
* `modules` attribute must have 1 or more entries
* each `module` must be defined in the list of modules
* `legislation` attribute must not be empty
