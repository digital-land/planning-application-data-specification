## Decision: Name the application record dataset `planning-application`

**Date:** 2025-12-18  
**Status:** Under review  

**Context:**  
While publishing the decision stage specification incrementally, we needed to introduce a dataset representing the application record associated with a decision.  

The generic term “application” may be widely used across the planning system and could reasonably refer to multiple concepts. “application” is more of a category, than a single thing. 

Using an unqualified name risks ambiguity as the specification expands.

**Decision:**  
We will name the dataset `planning-application` rather than `application`.

**Rationale:**  
Using a more specific dataset name:
- makes the scope and meaning of the dataset explicit
- avoids overloading the term “application” as the wider planning data model evolves
- reduces ambiguity for suppliers, analysts, and downstream users
- creates space for other application-type datasets to be introduced later without renaming or breaking changes
- decision data travels. Submission data is contextual. So we qualify the dataset name early to avoid collisions once it’s used outside the submission flow.

This is a preventative design choice that improves clarity and long-term maintainability with minimal additional complexity.

**Alternatives Considered:**  
- Naming the dataset `application` → rejected due to ambiguity and risk of future collisions
