# Planning Requirements

As part of moving from narrative guidance to structured, testable models, we want to define planning requirements (also known as **information requirements**) in a consistent, machine-readable format.

PLanning requirements are the documents, statements or data artefacts that must be submitted as part of a planning application, such as, flood risk assessments, affordable housing statements, or site plans.

## Structure

Each planning requirement is represented by a `.md` file in the `/planning-requirement` directory. These files define the standardised set of planning requirements used nationally or across multiple contexts.

Each file includes:

* `reference` – a unique identifier for the requirement (e.g. `air-quality-assessment`)
* `name` – human-readable title
* `description` – explanation of the requirement
* `synonyms` – list of alternative names (if applicable)
* `document-type` – category of document (e.g. statement, report)
* `source` – legal or policy source, such as legislation or NPPF paragraph references
* `entry-date` – when this requirement was introduced
* `end-date` – for deprecating or superseded requirements
* `required-if` – a declarative block describing the conditions under which this requirement is triggered (optional)

### Example: `/planning-requirement/air-quality-assessment.md`

```yaml
dataset: planning-requirement
reference: air-quality-assessment
name: Air Quality Assessment
description: >
  An assessment of the impact on air quality around the development and during the construction phase.
source: "National Planning Policy Framework (NPPF), paras 110, 119"
required-if:
  all:
    - application-type:
        in: [full, outline, reserved-matters]
    - any:
        - condition:
            field: dwelling-count
            operator: ">="
            value: 10
            description: Development proposes 10 or more residential units.
        - condition:
            field: site-area-residential
            operator: ">="
            value: 0.5
            description: Site area for residential development is 0.5 hectares or more.
        - condition:
            field: site-area-non-residential
            operator: ">="
            value: 1
            description: Site area for non-residential development is 1 hectare or more.
        - condition:
            field: floorspace-non-residential
            operator: ">="
            value: 1000
            description: Non-residential floorspace is 1,000 square metres or more.
```

## Local Area Requirements

Where a requirement is only applicable in a specific local authority (e.g. Camden), the conditions that trigger that requirement are stored in a separate directory for that authority.

For example, Camden’s local condition for when an **Affordable Housing Statement** is required would live at:

```
/planning-requirement/
  └── CMD/
       └── affordable-housing-statement.md
```

This avoids bloating the core definition with hundreds of divergent local rules. Instead:

* The defined requirement lives in `/planning-requirement/affordable-housing-statement.md`
* Camden’s local condition lives in `/planning-requirement/CMD/`

The local file defines a `required-if` block based on Camden-specific thresholds and conditions (e.g. number of dwellings, shared housing, student schemes, etc).

For example, for Camden specific affordable housing statement

```yaml
reference: affordable-housing-statement
local-authority: CMD
required-if:
  any:
    - all:
        - condition:
            field: dwelling-count
            operator: ">="
            value: 1
            description: The proposal includes at least one new dwelling.
        - condition:
            field: housing-floorspace
            operator: ">="
            value: 100
            description: The total new housing floorspace is at least 100 square metres.
    - condition:
        field: housing-type
        value: student
        description: The proposal includes student accommodation.
    - condition:
        field: housing-type
        value: shared
        description: The proposal includes shared housing.
    - condition:
        field: housing-type
        value: older-people
        description: The proposal includes housing for older people.
```

## Benefits

### For planning authorities and policymakers:

* Clear list of defined planning requirements
* Ability to track how and when requirements are triggered
* Easier to maintain a consistent national/local distinction
* The model allows authorities to document their requirements before codifying them

### For planning system developers and integrators:

* Machine-readable rules for validation and eligibility checks
* No need to hardcode validation logic for each LPA
* Clarity on where requirements come from and how they apply

## Design Decisions

* **Planning requirements are declared once centrally** in `/planning-requirement/`
* **Local authority rules are stored in subfolders** using local authority codes (e.g. `CMD` for Camden)
* `required-if` blocks are used to describe triggering logic in a structured format
* Requirements reference field conditions (e.g. `dwelling-count`, `housing-type`, `application-type`) that are aligned with the specification field list

#### Still to decided

* Is it useful to classify planning-requirements by `document-type`
* Do local area requirement files need place to add associated policies?
* Should we include common conditions in reusable blocks? For example, major development
```yaml
major-development:
  description: A standard definition of major development for residential or non-residential proposals.
  any:
    - condition:
        type: dwelling-count
        operator: ">="
        value: 10
    - condition:
        type: site-area-residential
        operator: ">="
        value: 0.5
    - condition:
        type: site-area-non-residential
        operator: ">="
        value: 1
    - condition:
        type: floorspace-non-residential
        operator: ">="
        value: 1000
```

## Validation and Integrity Checks

Validation logic should enforce the following:

* ✅ Local area requirements **must reference a planning requirement that exists** in `/planning-requirement/`
* ✅ Any `field` used in a condition **should exist in the specification’s field list** (alignment pending)
* ✅ `application-type` filters should only be included when the requirement is **not universal**
* ✅ Values for `application-type` and `application-sub-type` must **match the standardised list** of application types and subtypes
