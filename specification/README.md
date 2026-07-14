# Planning application data model – specification folder

This folder defines the **core data model** for planning application data.

It is intended for anyone working with the model in practice, including software suppliers implementing the specifications, local planning authorities using or testing them, policy and standards teams contributing to their development, and analysts or integrators who need to understand how planning data is structured.

It is used to support two specifications:

- **Planning application data specification** – the authoritative information that a planning authority creates and maintains through the planning permission process
- **Submission specification** – the information required to submit a valid planning application and get consistent data into the system

The planning application data specification describes the information that needs to be held and maintained. The submission specification provides a structured route for collecting the information needed when an application is made.

This README explains the different elements in this folder, how they fit together, and why they exist.

For a shorter primer on how the specification fits together and where to find fields, datatypes and codelists, see [how the specification fits together](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/how-the-specification-fits-together.md).

---

## Two specifications, two roles

The specifications have complementary roles:

- **Planning application data**: a local planning authority records and maintains authoritative information about an application through the planning permission process.
- **Submission**: an applicant provides information through a structured route when making an application.

The data model supports both roles.

### Planning application data specification

The planning application data specification defines:
- what information a planning authority should record and maintain about an application
- the authoritative records of the application, its progress, associated documents, decision and related obligations

It is **flat and relational**, because it represents linked records maintained through the planning permission process, without submission-time business logic.

### Submission specification

The submission specification defines:
- what information an applicant must provide
- how that information is grouped
- which modules and fields are required for different application types

It is **structured and nested**, because it mirrors how people think about completing an application and provides a route for getting consistent data into the system.

---

## What lives in this folder

```
specification/
  applications/
  modules/
  components/
  fields/
  datasets/
  codelists/
```

Each part plays a specific role.


### Applications (submission)

**Applications define what is required for a specific application type.**

For example: a full application, a householder application, or a listed building consent.

An application:
- brings together a set of modules
- defines fields are required, optional or not applicable
- represents the complete “shape” of a submission for that application type

An application here is **not** a planning application record.  
It is a **definition of requirements**, not a submitted case.


### Modules (submission)

**Modules group related fields around a subject.**

For example:
- site details
- applicant details
- ownership certificates

Modules:
- are used only by the submission specification
- act like sub-objects within an application
- mirror sections in traditional paper forms
- make large application definitions manageable and reusable

On the whole, you cannot add fields directly to an application.  
Fields must belong to a module so they are grouped, reusable and understandable.


### Components (submission)

**Components are reusable blocks of fields for use in submission forms.**

They capture patterns that appear repeatedly across the model.

For example:
- a person component
- an address component
- a contact details component

Components:
- are used by the submission specification
- promote consistency and reuse
- make repeated form structures easier to define

Think of components as the standard building blocks used everywhere.


### Fields (shared)

**Fields define individual pieces of data.**

A field describes:
- the name of the data item
- what it represents
- its type and constraints
- whether it uses a codelist

Fields are:
- reused across modules, components and datasets
- intentionally stable
- added to over time, with older fields potentially deprecated rather than removed

Fields should not exist in isolation.  
They are always used as part of an application, module, component or dataset.


### Datasets (planning application data)

**Datasets define tables of record.**

They represent real-world things in the planning process that need to be
**recorded, referenced and analysed**, regardless of how they were originally submitted.

For example:
- planning applications
- decisions
- planning conditions

Some datasets, such as planning applications and sites, exist before a decision is made. In the planning application data specification, they are treated as **authoritative records**, not user inputs.

Datasets:
- are used by the planning application data specification
- are flat and explicit
- remove submission-time structure and logic
- support publication, reporting and analysis

They describe *what exists and what happened*, not *how information was collected*.


### Codelists (shared)

**Codelists define the allowed values for certain fields.**

They ensure consistency where free text would make data unreliable.

For example:
- use classes
- decision outcomes (maybe)
- tenure types

Some codelists are:
- maintained locally for planning-permission-specific use (for example, yes-no-unknown)
- maintained elsewhere where they have wider utility, and referenced here (for example, use classes)

Using shared codelists across the submission and planning application data specifications ensures the same concepts mean the same thing throughout the process.

#### Codelist usage

When a codelist needs different valid subsets in different contexts, the preferred pattern is to keep one canonical codelist for the concepts and define context-specific allowed values in a separate usage table. 

See the [codelist usage pattern note](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/codelist-usage.md) and related [design decision](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/design-decisions/0010-separate-usage-for-codelist-subsets.md) for details.

---

## Why this model is structured this way

### Why not one big schema?

Because the specifications serve different purposes.

- The planning application data specification defines the authoritative information that a planning authority should record and maintain about an application and its progress.
- The submission specification defines the forms, structure and validation needed to collect good data when an application is made.

Forcing both into a single structure would mix the authoritative record with the form structure and validation needed to collect it.


### Why do the planning application data and submission models look different?

They answer different questions.

- Planning application data: *What information should we record and maintain about the application?*
- Submission: *What information do we need to ask for, and how should it be structured?*

More detail on this distinction is covered in [this explainer](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/difference-between-the-specifications.md).


### Why are some things modules and others datasets?

- **Datasets** record information that a planning authority needs to maintain
- **Modules** organise information people are asked to provide through a submission form

If something represents a thing that can exist, change state, or be referenced later, it belongs in a dataset.

### Why can’t I just add a field directly to an application?

Because fields need context.

Modules:
- group related information
- support reuse
- make requirements easier to understand and maintain

Adding fields directly to applications would quickly lead to duplication and inconsistency.


### Why is the same subject a module in one place and a dataset in another?

Some subjects appear in both submission modules and datasets in the planning application data specification. This is expected.

In the submission specification, a **module** groups related information that a user is asked to provide as part of an application. Its purpose is to support data entry and validation.

In the planning application data specification, a **dataset** records the enduring, authoritative version of that information as part of the planning record.

The difference is not about the subject itself, but about **when and why the data is being captured**:
- datasets record and maintain authoritative information that can be referenced, published or analysed later
- modules organise information at the point of submission

### Does the specification define validation rules or user interface behaviour?

The specification includes some **expressed rules**, but it does not fully codify validation logic (if you think it should then add to the [discussion](https://github.com/digital-land/planning-application-data-specification/issues/231)).

Rules are used to:
- describe important relationships between fields
- capture constraints that matter to the planning process
- make expectations explicit for implementers

For example, a module may state rules such as:
- a reference must match an entry defined elsewhere
- at least one contact method must be marked as primary

These rules describe **what must be true**, not **how systems must enforce it**.

Context-dependent rules are expected to be handled by validation logic outside the schema.  
For example, while the schema defines the fields that make up an address, a rule such as “a postcode is required if the site is in the UK” is currently enforced by application logic, not by the schema itself.

Similarly, the specification does not dictate whether something should be implemented as a checkbox, radio button or text input. Those decisions sit with individual systems, provided the resulting data meets the requirements of the model.

---

## Making changes to the model

Changes are made incrementally and deliberately, usually in response to:
- policy changes
- delivery needs identified by local authorities
- feedback from suppliers and the wider community

Most changes involve adding or refining fields, modules or datasets rather than restructuring the model. Existing elements are kept stable where possible, with new requirements introduced alongside them.

---

## In summary

- Applications define **what is required**
- Modules organise **how information is grouped**
- Components provide **reusable building blocks**
- Fields define **individual data points**
- Datasets record **authoritative information**
- Codelists keep answers **consistent**

Together, these elements form a clear, extensible data model that supports both recording and maintaining planning application information, and collecting good data when an application is made, without prescribing how systems must be built.
