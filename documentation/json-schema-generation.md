# JSON Schema generation

## Overview

This document outlines the approach for generating JSON Schema definitions from the existing markdown based planning application data specifications.

The goal is to create schemas that can be used to validate JSON payloads representing planning applications of specific types.

The main aim for this piece of work was to:

**"Combine the various 'separate modules & components' of the current declarative models into a 'composite for the whole specification payload.'**

### Examples

The [application type examples](../specification/example/application-type/) currently cover six application types. They are useful for checking the generated schemas, but do not yet cover every application type or every conditional rule.

## Application schemas and combined applications

The generator produces one self-contained JSON Schema for each authored application type. Each schema describes that type's resolved fields and modules. It sets `additionalProperties: false` at the payload root, so unknown top-level names fail validation. The optional `additional-data` field is a defined top-level property whose object contents remain open. The checked-in generated schemas must be rebuilt to reflect this change. See [Applications](application.md) for the submission rule.

A combined application is derived from an approved combination of member application types. Its payload contains the merged fields and modules of those types. Do not validate the entire combined payload separately against each member's JSON Schema: each closed schema would reject fields or modules belonging only to the other member. The package can [resolve a combined application definition](../planning_application_specification/README.md#combined-applications), but the current generator does not publish a combined JSON Schema. A validator needs a schema or equivalent validation contract built from that resolved combination.

The historical [example validator](../bin/example_validator.py) still loops through single-type schemas for a multi-type payload. It does not implement this combined-application rule and should not be used to validate a combined submission against the current closed-root schemas.

## Future enhancements, questions and considerations
1. Extend the sample payloads to cover all application types and relevant conditions.
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
├── Submission-level fields (submission-details, additional-data)
│   └── Components where a field has a defined structure
└── Modules (agent-details, proposal-details, etc.)
    ├── Fields (with conditional logic)
    └── Components (reusable field groups)
```

### Key components

#### 1. **Applications** (`specification/application/*.schema.md`)
- Define application types (householder, full planning, listed building consent, etc.)
- Include submission-level fields, such as `submission-details` and optional `additional-data`
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
  - **Component reference**: Links to reusable components for structured object fields
  - **Open object**: `allow-additional-properties: true` permits any properties within an object field without a component
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
object with component → {"$ref": "#/definitions/ComponentName"}
object with allow-additional-properties: true → {"type": "object", "additionalProperties": true}
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

### Co-constraint coverage

The specification supports structured co-constraints such as `applies-if` and
`required-if`. The JSON Schema generator currently emits only a subset of these
rules.

Known gaps include `required-if` operators such as `not_empty`, field-to-field
comparisons, grouped `all` conditions and dotted paths that refer outside the
current object. `applies-if` checks are resolved through the package model, so
application types that use `extends` inherit parent application type conditions.

Until those gaps are implemented, generated schemas may be conservative. For
example, a generated schema may require a field unconditionally even where the
source specification says it is conditionally required. This is preferable to
silently accepting invalid data, but it means generated schemas should not yet
be treated as a complete expression of all co-constraints.

See [Co-constraints](co-constraints.md) for the current coverage matrix.

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

Supported conditions are converted to JSON Schema `if/then/else` constructs. Some are simple `if/then/else` constructs. The conditions
evaluated within the `if` may in turn be combined using `allOf` or `anyOf` constructs resulting in logical and/or semantics.

The generator supports value-based `required-if` conditions and `operator: empty`, including missing properties and empty strings, arrays, objects or null values. It does not generate rules for other operator conditions such as `not_empty` or field-to-field comparisons using `value-field`. JSON Schema Draft 7 cannot
portably compare the values of two fields, so these conditions remain part of
the source specification but are not enforced by the generated JSON Schema.

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
- etc. (one schema per authored application type)

#### 2. **Inline definitions**
Modules and submission-level fields become root properties. Structured fields and modules can reference inline definitions. An open object field such as `additional-data` has no component definition:

```
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "$id": "hh.json",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "agent-details": {"$ref": "#/definitions/agent-details"},
    "proposal-details": {"$ref": "#/definitions/proposal-details"},
    "submission-details": {"$ref": "#/definitions/submission-details"},
    "additional-data": {"type": "object", "additionalProperties": true}
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
    "submission-details": {
      "type": "object",
      "properties": {...}
    }
  }
}
```

**Key architectural decisions:**
- **Self-contained schemas**: Each application schema includes all necessary definitions inline
- **Defined root properties**: Only resolved application fields and modules are allowed at the payload root
- **No external dependencies**: Each schema file works independently without requiring external references


### Technical implementation details

#### Generator script

The generator is [bin/generate_json_schema.py](../bin/generate_json_schema.py).

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
- Main application `properties` for its resolved fields and modules, with `additionalProperties: false` at the root
- Inline module definitions in `definitions` section
- Inline component definitions in `definitions` section

#### Integration with existing workflow
- Run the `jsonschema` target in the `Makefile` to regenerate the schemas

### Implementation scope

**Initial focus**: Direct technical mapping of specification elements to JSON Schema:
- Field datatypes (`string`, `number`, `boolean`, `enum`, `object`)
- Cardinality constraints (`1` vs `n` for arrays)
- Module and Component references via `$ref` with definitions
- Submission-level fields, including the optional open `additional-data` object
- Module and Component inclusion with (`applies-if`, `required-if`)

**Future scope**: Complex validation rules from module `rules:` sections would require additional analysis and are not included in the initial implementation.

### Deliverables
1. **JSON Schema generation script** (`bin/generate_json_schema.py`) - ✅ Complete
2. **Generated schema files** (`generated/json-schema/applications/*.json`) - rebuild after specification changes
3. **Integration with build process** (Makefile targets) - ✅ Complete
4. **Sample application JSON files** - six canonical application type examples; broader coverage remains to be done
5. **Sample validation script using jsonschema (Python)** - historical example; does not validate combined applications against their resolved definition

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

### Deferred support: conditional listed building grades

The module model supports answer-based `applies-if` conditions. The generator does not yet translate all conditional rules. In particular, generated schemas cannot yet be relied on to validate the rule that a listed building grade is required only when `listed-building-grade-known` is `true`. See [co-constraint coverage](co-constraints.md#json-schema-generator-coverage) for the outstanding work.

Support for this conditional grade requirement in generated schemas is tracked in [issue #420](https://github.com/digital-land/planning-application-data-specification/issues/420).
