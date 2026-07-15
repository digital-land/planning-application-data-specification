## Decision: Name the application record dataset `planning-application`

**Date:** 2025-12-18  
**Status:** Proposed

### Context 

The planning application data specification needs to include a dataset that represents planning applications.

A planning application is often referred to as an “application”, however, the word application could reasonably refer to other concepts, for example, an "application for designation of a neighbourhood forum".

The unqualified term "application" can describe several distinct kinds of request in the planning system, rather than this particular record.

This means using an unqualified name risks ambiguity as the specification expands.

### Decision 

A planning application is a request submitted to a planning authority for planning permission, consent, approval, a certificate or a related determination.

We will name the dataset `planning-application` rather than `application`.

### Rationale

Using a more specific dataset name:
- makes the scope and meaning of the dataset explicit
- avoids overloading the term “application” as the wider planning data model evolves
- reduces ambiguity for suppliers, analysts, and downstream users
- creates space for datasets for other kinds of application to be introduced later without renaming or breaking changes
- planning application data is reused across registers, reporting and other systems. Qualifying the dataset name ensures its meaning remains clear in those contexts.

This is a preventative design choice that improves clarity by maintaining context even when the data is used in other areas.

### Alternatives Considered

- Naming the dataset `application` → rejected due to ambiguity and risk of future collisions
