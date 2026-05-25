# Applications

As we move from narrative specifications to declarative models, we need a consistent way to describe applications. 

The application interface defines the application, what legislation underpins it and what is required to submit an application of that type - including any specific fields for that application and the required modules.

A declarative definition of application types supports programmatic conformance checking, dynamic form generation, and structured communication between systems, while remaining implementation-agnostic.

## Benefits

Like [modules](module.md), applications benefit from being:

* **Explicit** it clearly states what is required
* **Reuse** of modules across applications types make the data more consistent
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

Some application types can be submitted together as a combined application. These combinations are not open-ended. They come from a controlled list of policy-approved combinations, and the specification derives the combined application from the member application types rather than maintaining a separate hand-written definition for each combination. See [decision record 0012](design-decisions/0012-use-a-controlled-list-for-combined-application-types.md).

Every application includes the `submission-details` field for information about the submitted payload itself, such as the submission reference, application types, planning authority, submitted time and uploaded documents. See [submission details](submission-details.md).

## Resolving application definitions

Some application definitions extend a broader parent application. For example, `outline-some` extends `outline`.

When building or validating a payload for a concrete application type, resolve the application definition before deciding the expected payload shape:

* start with the parent application's `fields` and `modules`
* add the child application's `fields` and `modules`
* de-duplicate repeated references
* treat the resulting field and module references as top-level payload properties

For `outline-some`, this means the payload includes the inherited `submission-details` field and inherited outline modules, plus the additional modules listed on `outline-some`.

The resulting JSON payload is keyed by field or module reference, for example:

```json
{
  "submission-details": {},
  "applicant-details": {},
  "proposal-details": {},
  "access-rights-of-way": {}
}
```

If the application definition has `allow-additional-properties: true`, the root payload may include extra top-level properties beyond the resolved field and module references.

**Attributes of module definitions**

* `application` -  unique identifier for the application (e.g. `hh`)
* `name`
* `description`
* `synonyms` - other names used for the application type
* `legislation` - provides a link for legal context
* `fields[]` - list of field references, currently including `submission-details`
* `modules` - a list of modules an applicant needs to complete
* `entry-date`
* `end-date` - for deprecating applications
* `rules`

**Applications should reference fields and modules by ID**
With the field and modules definitions defined elsewhere.

### Still to decide

* If `fields` and `modules` need to be separate lists. The `fields` list is always going to reference the `submission-details` field. And arguably the `modules` are top-level fields that break down into substructures. Our current thinking is:
  * Field components describe reusable data shapes — what structured data looks like.
  * Modules define reusable form sections — where and when that data is collected in an application.
  * The two work together: fields define structure, modules define context.
* Should the definition include other details that could be useful for submission and back-office systems, such as, details of the expected turn around times, so that these are also codified?
* how to handle `sub-types`. One option to handle them the same as applications. So for outline applications we'd have 2 application definitions: outline-all and outline-some that define the modules required for each. An alternative is to define an outline application  and use `extend` or `inheritance` to define the application

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
  - field: submission-details
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

* `fields` attribute must include `submission-details`
* each `field` of `fields` must be defined in the set of specification fields
* `modules` attribute must have 1 or more entries
* each `module` must be defined in the list of modules
* `legislation` attribute must not be empty
