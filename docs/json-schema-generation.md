# JSON Schema generation

## Overview

This document outlines the approach for generating JSON Schema definitions from the existing markdown based planning application data specifications.

The goal is to create schemas that can be used to validate JSON payloads representing planning applications of specific types.

The main aim for this piece of work was to:

**"Combine the various 'separate modules & components' of the current declarative models into a 'composite for the whole specification payload.'**

### Note
**A major part missing in this work is sample application JSON data. This would have made testing the generation of JSON schema much easier
and sustainable.** 

An attempt to use LLMs was made to generate sample application, but the result was a mixed bag and required a fair bit of manual reworking.

In the end only one example application was created [example-hh-payload-minimal.json](../specification/example/example-hh-payload-minimal.json)

It should be a high priority to create sample application payloads for each application type.

## Key design decision: One schema per application type

A key design decision in this architecture is to generate one self-contained JSON schema for each individual application type, rather than a single 
monolithic schema to 
validate all possible payloads.

**This approach is a starting point and can be changed based on future based on feedback**.

While the planning application data model allows a payload to represent multiple application types simultaneously (via the `application-types` array), 
a single, all encompassing schema may require a number of nested `if/then` logic conditions to handle every possible combination of application types.
The alternative approach of a single schema hasn't been tested given the time available but may be worth exploring at some point if required.

The chosen approach promotes separation of concerns. Each schema is stand alone and the trade-off in taking this approach is that it would require
validation orchestration.

To restate this, the approach is to have:

1.  **Schemas as rules to apply for each application type:** Each generated schema (e.g., `hh.json`, `lbc.json`) acts as a complete, focused, and 
    more readable set of constraints for a single application type. It defines exactly which modules and fields are required for that specific type.

2.  **Validation orchestration:** The responsibility for handling multi-type applications is placed on the consuming application (the "validator").
    A validator should be implemented with the following logic:

    * Inspect the `application-types` array in the incoming JSON payload. 
    * For each type listed in the array, validate the entire payload against **each** of the relevant JSON schemas.

A payload is only considered valid if it successfully validates against all the schemas it declares an interest in. This ensures that a combined 
"Householder" and "Listed Building Consent" application, for example, contains all the required modules and fields for both types.
**See the section below for an example validation script.**

This modular architecture ensures the schemas themselves remain simpler and maintainable while providing the necessary building blocks for developers 
to implement robust and flexible validation logic.

#### Example validation orchestration script

To illustrate how validation could be done for multi type planning applications an example script has been added to this
repository and can be found here [bin/example_validator.py](../bin/example_validator.py)

To use this script check out this repository and set up the required tools (create a python virtual env, activate it and run `make init`).

Then you can run:

```
 bin/example_validator.py --payload [path to application json ] --schema-dir [path to schema director]
```
So a real example you can run is:

```
bin/example_validator.py --payload specification/example/example-hh-payload-minimal.json --schema-dir generated/json-schema/applications
```


## Future enhancements, questions and considerations
1. Create a complete set of correct sample application types for testing.
2. How could/should the rules lists from the markdown schemas be incorporated into JSON schema?
3. Would a single schema be a better approach?
4. Publication of schemas. Github urls, release branch, tags for stable Github urls?
5. Versioning options, version number in url, version in output file name, convention for latest, Github tags, directory based versioning?

## JSON Schema version

**Reason for using JSON Schema Draft-07** for maximum compatibility across validation tooling. While Draft 2020-12 is the latest standard, Draft-07 has:

- **Widespread tooling support**: Supported by many JSON Schema validation libraries
- **Sufficient features**: Includes all validation constructs used in this project (`if/then/else`, `definitions`, etc.)

The generated schemas use Draft-07 syntax (`definitions` instead of `$defs`, etc.) to ensure they work reliably across different validation environments.

## Current architecture

### Specification structure
The current specification is organized as a hierarchical structure:

```
Application (hh, full, lbc, etc.)
├── Application-level Fields (application, etc.)
│   └── Components (e.g., application core data)
└── Modules (agent-details, proposal-details, etc.)
    ├── Fields (with conditional logic)
    └── Components (reusable field groups)
```

### Key components

#### 1. **Applications** (`specification/application/*.schema.md`)
- Define application types (householder, full planning, listed building consent, etc.)
- Include application-level fields (typically core application data like reference, submission-date)
- Reference modules for specific functional areas
- Include application-specific metadata (legislation, synonyms, dates)

#### 2. **Modules** (`specification/module/*.schema.md`) 
- Group related fields by subject area (e.g., agent-details, proposal-details)
- Support conditional field inclusion (`applies-if`, `required-if`)
- Include validation rules in human-readable format

#### 3. **Fields** (`specification/field/*.md`)
- Define individual data elements with:
  - **Datatype**: `string`, `number`, `boolean`, `enum`, `object`
  - **Cardinality**: `1` (single) or `n` (array)
  - **Component reference**: Links to reusable components
  - **Codelist reference**: Links to enumerated values

#### 4. **Components** (`specification/component/*.md`)
- Reusable field groupings (e.g., supporting-document, address)
- Can be referenced by fields with `datatype: object`
- 
#### 5. **Codelists** (`specification/codelist/*.schema.md` + `data/codelist/*.csv`)
- Enumerated values for dropdown/select fields
- CSV data with reference, name, description columns

## JSON Schema generation requirements

### Schema structure

**Inline Definitions**: The current implementation uses inline definitions within each application schema file. 
All component and module definitions are included in the `"definitions"` section of each application's JSON Schema file.

**Rationale**:
- **Self-contained**: Each schema file works independently without external dependencies
- **Validation reliability**: No risk of broken references

**Future Considerations**: The approach could be adapted to generate separate component/module schema files referenced via relative file paths or URLs if needed.

### Core mapping

#### Datatype mapping
```
# Field specification → JSON Schema
string → {"type": "string"}
number → {"type": "number"}
boolean → {"type": "boolean"}
enum → {"type": "string", "enum": [values from CSV]}
object → {"type": "object", "$ref": "#/definitions/ComponentName"}
```

#### Cardinality mapping
```
# Cardinality → JSON Schema
cardinality: "1" → field definition
cardinality: "n" → {"type": "array", "items": field_definition}
```

#### Module mapping
```
module: tpo
name: Tree preservation order details
fields:
- field: tpo-reference        # cardinality: n, datatype: string
- field: tpo-provided-by      # cardinality: 1, datatype: enum
```
Maps to application property and definition:
```
{
  "properties": {
    "tpo": {"$ref": "#/definitions/tpo"}
  },
  "definitions": {
    "tpo": {
      "type": "object",
      "properties": {
        "tpo-reference": {
          "type": "array",
          "items": {"type": "string"}
        },
        "tpo-provided-by": {
          "type": "string",
          "enum": ["applicant", "system"]
        }
      }
    }
  }
}
```

####  Component mapping
```
# Field with component reference
field: documents
datatype: object
component: document
cardinality: n
```
Maps to:
```
{
  "documents": {
    "type": "array",
    "items": {"$ref": "#/definitions/document"}
  }
}
```

#### Codelist mapping
```
# Field with enumeration
field: foul-sewage-disposal-types  
datatype: enum
codelist: foul-sewage-disposal-type
cardinality: n
```
Maps to:
```
{
  "foul-sewage-disposal-types": {
    "type": "array", 
    "items": {
      "type": "string",
      "enum": ["mains-sewer", "cess-pit", "septic-tank", "package-treatment", "other"]
    }
  }
}
```
With the values for the enum read from the corresponding csv in (data/codelist/*.csv) directory.
 
#### Conditional logic mapping
The module specifications include complex conditional logic that is handled differently depending on the condition type

There are two main types of conditionals in the markdown schemas. 

1. `required-if` conditions
2. `applies-if` conditions

Both are converted to JSON Schema `if/then/else` constructs. Some are simple `if/then/else` constructs. The conditions
evaluated within the `if` may in turn be combined using `allOf` or `anyOf`constructs resulting in logical and|or semantics.

#### **1. Simple `required-if` (single condition)**
Example from: [specification/component/operational-times.md](../specification/component/operational-times.md)
```
- field: time-ranges
  required-if:
    - field: closed
      value: false
```
Maps to:
```
{
  "if": {"properties": {"closed": {"const": false}}},
  "then": {"required": ["time-ranges"]}
}
```

#### **2. `allOf` pattern (multiple 'AND' conditions)**
Example from: [specification/component/floorspace-details-outline.md](../specification/component/floorspace-details-outline.md)
```
- field: floorspace-lost
  required-if:
    - field: not-applicable
      value: false
    - field: is-floorspace-lost-known
      value: true
```
Maps to:
```
{
  "if": {
    "allOf": [
      {"properties": {"not-applicable": {"const": false}}},
      {"properties": {"is-floorspace-lost-known": {"const": true}}}
    ]
  },
  "then": {"required": ["floorspace-lost"]}
}
```

#### **3. `anyOf` pattern (multiple 'OR' conditions)**
Example from: [specification/component/floorspace-details-outline.md](../specification/component/floorspace-details-outline.md)
```
- field: specified-use
  required-if:
    any:
      - field: use
        contains: sui
      - field: use
        contains: other
```
Maps to:
```
{
  "if": {
    "anyOf": [
      {"properties": {"use": {"pattern": "sui"}}},
      {"properties": {"use": {"pattern": "other"}}}
    ]
  },
  "then": {"required": ["specified-use"]}
}
```

#### **4. `applies-if` (Field inclusion by application type)**
Example from: [specification/component/tree-details.md](../specification/component/tree-details.md)
```
- field: replanting-description
  applies-if:
    application-type:
      in: [consent-under-tpo]
```
**Field only included** in schemas where the application type matches. Only appears in `consent-under-tpo.json`,
in the `properties` list and of course in the `definitions`. It's excluded from all other application type schemas.


### Schema architecture

#### 1. **Application level schema**
Each application type gets its own self-contained JSON Schema file matching the specification filenames:
- `generated/json-schema/applications/hh.json` (householder)
- `generated/json-schema/applications/full.json` (full planning)
- `generated/json-schema/applications/lbc.json` (listed building consent)
- `generated/json-schema/applications/advertising.json`
- `generated/json-schema/applications/approval-condition.json`
- etc. (24 total application schemas)

#### 2. **Inline definitions**
All modules and components are treated uniformly as properties with inline definitions:

```
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "$id": "hh.json",
  "properties": {
    "agent-details": {"$ref": "#/definitions/agent-details"},
    "proposal-details": {"$ref": "#/definitions/proposal-details"},
    "supporting-document": {"$ref": "#/definitions/supporting-document"},
    "application": {"$ref": "#/definitions/application"}
  },
  "definitions": {
    "agent-details": {
      "type": "object",
      "properties": {...}
    },
    "proposal-details": {
      "type": "object",
      "properties": {...}
    },
    "supporting-document": {
      "type": "object",
      "properties": {...}
    },
    "application": {
      "type": "object",
      "properties": {...}
    }
  }
}
```

**Key architectural decisions:**
- **Self-contained schemas**: Each application schema includes all necessary definitions inline
- **Unified treatment**: Modules and components are both treated as properties with `$ref` pointers to inline definitions
- **No external dependencies**: Each schema file works independently without requiring external references


### Technical implementation details

#### Generator script

The script for generation of json is [bin/generate_json_schema.py](bin/generate_json_schema.py)

#### Output structure
```
generated/
└── json-schema/
    └── applications/
        ├── hh.json
        ├── full.json
        ├── lbc.json
        ├── advertising.json
        └── ... (all application types)
```

Each application JSON Schema file contains:
- Main application `properties` with references to items in `defintions` list
- Inline module definitions in `definitions` section
- Inline component definitions in `definitions` section

#### Integration with existing workflow
- Generator script added to `Makefile`: `json-schemas` target

### Implementation scope

**Initial focus**: Direct technical mapping of specification elements to JSON Schema:
- Field datatypes (`string`, `number`, `boolean`, `enum`, `object`)
- Cardinality constraints (`1` vs `n` for arrays)
- Module and Component references via `$ref` with definitions
- Application level fields (core application data)
- Module and Component inclusion with (`applies-if`, `required-if`)

**Future scope**: Complex validation rules from module `rules:` sections would require additional analysis and are not included in the initial implementation.

### Deliverables
1. **JSON Schema generation script** (`bin/generate_json_schema.py`) - ✅ Complete
2. **Generated schema files** (`generated/json-schema/applications/*.json`) - ✅ Complete (24 schemas)
3. **Integration with build process** (Makefile targets) - ✅ Complete
4. **Sample application json files for householder, full and outline** - [❌] Incomplete
5. **Sample vaidation script using jsonschema (Python)** - ✅ Complete

### File paths and data sources

**Specification loading:**
- `bin/loader.py:load_specification_model()` → Returns complete model
- `bin/models.py` → Dataclass definitions
- Uses `frontmatter` library to parse YAML headers

**Data sources:**
- Applications: `specification/application/*.schema.md`
- Modules: `specification/module/*.schema.md` 
- Fields: `specification/field/*.md`
- Components: `specification/component/*.md`
- Codelists: `specification/codelist/*.schema.md` + `data/codelist/*.csv`

The current generation approach leverages the existing structured specification model and provides the basis for JSON Schema generation 
while maintaining the integrity and conditional logic present in the current markdown based specifications.


