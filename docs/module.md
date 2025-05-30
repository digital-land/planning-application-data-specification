# Modules

_Note: Exactly how we define modules is still being decided_

As we move from narrative specifications to declarative models, we need a consistent way to describe modules. 

Modules are the reusable groupings of fields that make up parts of a planning application.

The module interface/scheme should define how a module is structured, what fields it uses, and the conditions under which it applies.

## Benefits

Like fields, modules benefit from being:

* **Explicit** everyone knows what is required and when
* **Reused** used across different application types or contexts
* **Testable** can drive conformance checks and interface expectations


Breaking that down some of the benefits include:

For MHCLG and admins:

* reusable, explicit module definitions
* easier changelogs, validation, and documentation
* enables modular versioning and testing

For suppliers and community:

* clear contract of what’s required, and when
* easier to validate payloads against requirements
* reduces the need for hardcoded integration assumptions
* helps everyone "speak the same language" when it comes to data

## Decisions

**Modules should be defined centrally**
Each module has a canonical definition in a shared repository.

**Attributes of module definitions**

* `module` -  unique identifier for the module (e.g. `agent-details`)
* `name`
* `description`
* `fields[]` - List of field references
* `applies-if` - A condition or expression that determines when the module is used (not sure if this is the right place for it)
* `entry-date`
* `end-date` - for deprecating fields

Each field item will need include the requirement level and, probably, a level of conditionality (for example, required if field X is Y)

**Modules should reference fields by ID**
With the field definitions living elsewhere.

**Use of `applies-if`**
Use of `applies-if` allows conditional inclusion without bloating the model.

### Still to decide

* Should `applies-if` support complex conditions or be limited to simple key-value checks?
  Similarly is it bound to whats available in the module?
* Do we allow modules to override field data types or other structural elements?
  Leaning no, maybe better to create new fields.
* Should modules be allowed to reference other modules (i.e. support nesting or composition)?
  Again leaning towards no. Fields can have substructures so that is where the nesting happens
* What is missing? For example, field ordering?
  Model should be minimal so reluctant to introduce too much. No looking to encode UI layout reqs, data transfer methods, etc
* Should we include what is redactable at the model or field level?
* is a `rules` attribute enough to handle the validation rules for components and modules?


### Validation rules for module (or component) definitions

* `fields` attribute must have 1 or more entries
* each `field` of `fields` must be defined in the set of specification fields
