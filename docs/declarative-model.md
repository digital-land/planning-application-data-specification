# Declarative model

Declarative models support the implementation and adoption of the specification(s).

They make the structure of the data explicit, helping systems interpret, validate, and exchange planning application data more easily — without replacing the more accessible, narrative forms of the specification.

## What is a declarative model?

A declarative model is a structured, machine-readable way of describing data fields, substructures and modules. Rather than writing code or building technical tools, they describe:

* what data is needed
* what shape it takes
* how it can be validated
* where and when each field and module is used

For fields this includes standard attributes like field names, descriptions, datatypes, cardinality, and validation rules.

For modules, this includes which fields they use, when they are required, and the rules that govern their use.

We are not going beyond this - a declarative model will not define protocols, APIs, or prescribe specific formats like JSON or XML. They are about structure, not execution.

## Why we need a declarative model

Our existing human-readable specifications or information models, have served us well during design and consultation. But to manage, validate, and eventually mandate them, we now need to express them more formally.

This declarative layer becomes the shared foundation that different tools, systems, and organisations can work from, without ambiguity or translation overhead.

### Beenfits of a declarative model

For MHCLG (as administrators of the specification):

* makes the structure of the specification explicit and composed of discrete, well-defined parts, enabling better reuse and iteration
* easier to track changes
* enables automated validation 
* simplifies feedback resolution
* can be versioned and maintained as structured, living documentation
* provides a single source of truth to derive multiple outputs (human-readable docs, tests, schemas)

For service builders and the wider community

* clear, consistent model to build against
* enables automated validation of data against the spec
* reduces the effort needed to interpret the spec manually
* makes it easier to build conforming systems regardless of tech stack
* supports the development of shared tools and validators
* keeps the spec implementation-agnostic, but usable
* creates a shared, unambiguous expectation of what data constitutes a planning application which reduces the need for bespoke, one-off integrations between systems in the ecosystem

## Next steps

This model is being introduced gradually, and we’re keeping it lightweight by design. We’ll publish it alongside the existing human-readable specs and welcome input on versioning, extension, and validation patterns as it evolves.

--

## Parts of the declarative model


* fields - are the small elements of the model, they define individual data points
  * fields can reference a component
* components are reusable substructures or data shapes made up of, for example, an address or a person
  * they group fields into logical, structured units
* modules are a collection of fields and/or components that appear together as a section of an application form.
  * they define which data is required in a given context
* applications - the different types of planning applications that people can submit to ask for permission to do something
  * each application specifies the modules that must be completed to allow a planning authority to assess the proposal

If **fields** are the building blocks (bricks), and **components** are grouped blocks (walls), then **modules** are the rooms – they determine where and how those walls are arranged.  
**Applications** are the full building – the complete structure made from those rooms, shaped according to purpose.
