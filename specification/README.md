# Planning application data model – specification folder

This folder defines the **core data model** for planning application data.

It is used to support **two related but distinct specifications**:

- **Submission specification** – what information is required to submit a valid planning application
- **Decision specification** – what information must be recorded once a decision has been made

Together, these specifications describe **what data is required at different stages of the planning process**, without dictating how software systems must be built to collect or store it.

This README explains the different elements in this folder, how they fit together, and why they exist.

---

## Two stages, two models

The planning process has a clear split:

- **Input**: an applicant submits information to request permission
- **Output**: a local authority records what decision was made and why, and any associated artefacts

The data model reflects this.

### Submission specification (input)

The submission specification defines:
- what information an applicant must provide
- how that information is grouped
- which modules and fields are required for different application types

It is **structured and nested**, because it mirrors how people think about completing an application.

### Decision specification (output)

The decision specification defines:
- what information and artefacts must be recorded once a decision exists
- the authoritative record of decisions, conditions and outcomes

It is **flat and relational**, because it represents facts that have already happened, with submission-time business logic removed.

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


### Components (submission and decision)

**Components are reusable blocks of fields.**

They capture patterns that appear repeatedly across the model.

For example:
- a person component
- an address component
- a contact details component

Components:
- are shared by both submission and decision specifications
- promote consistency and reuse
- provide a common vocabulary across the model

Think of components as the standard building blocks used everywhere.


### Fields (submission and decision)

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


### Datasets (decision)

**Datasets define tables of record.**

They represent real-world things in the planning process that need to be
**recorded, referenced and analysed**, regardless of how they were originally submitted.

For example:
- planning applications
- decisions
- planning conditions

Some datasets (such as planning applications) **exist before a decision is made**,  
but in the decision specification they are treated as **authoritative records**, not user inputs.

Datasets:
- are used by the decision specification
- are flat and explicit
- remove submission-time structure and logic
- support publication, reporting and analysis

They describe *what exists and what happened*, not *how information was collected*.


### Codelists (submission and decision)

**Codelists define the allowed values for certain fields.**

They ensure consistency where free text would make data unreliable.

For example:
- use classes
- decision outcomes (maybe)
- tenure types

Some codelists are:
- maintained locally for planning-permission-specific use (for example, yes-no-unknown)
- maintained elsewhere where they have wider utility, and referenced here (for example, use classes)

Using shared codelists across submission and decision stages ensures the same concepts mean the same thing throughout the process.

---

## Why this model is structured this way

### Why not one big schema?

Because submission and decision data serve different purposes.

- Submission data supports user input and validation
- Decision data records authoritative outcomes

Forcing both into a single structure would make both harder to use.


### Why do submission and decision models look different?

They answer different questions.

- Submission: *What information do we need to ask for?*
- Decision: *What happened?*

More detail on this distinction is covered in [this explainer](https://github.com/digital-land/planning-application-data-specification/blob/main/docs/difference-between-submission-decision-specs.md).


### Why are some things modules and others datasets?

- **Modules** organise information people are asked to provide
- **Datasets** record facts that exist independently

If something represents a thing that can exist, change state, or be referenced later, it belongs in a dataset.

### Why can’t I just add a field directly to an application?

Because fields need context.

Modules:
- group related information
- support reuse
- make requirements easier to understand and maintain

Adding fields directly to applications would quickly lead to duplication and inconsistency.

---

## In summary

- Applications define **what is required**
- Modules organise **how information is grouped**
- Components provide **reusable building blocks**
- Fields define **individual data points**
- Datasets record **authoritative outcomes**
- Codelists keep answers **consistent**

Together, these elements form a clear, extensible data model that supports both submitting planning applications and recording planning decisions — without prescribing how systems must be built to do it.
