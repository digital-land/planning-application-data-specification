## Decision: Use a `parent` field for simple hierarchical codelists

**Date:** 2026-03-10  
**Status:** Proposed  

**Context:**  

Some codelists need a light parent-child hierarchy so related values are discoverable from one canonical source.  

For example, application type and subtype were previously split across two datasets, which required consumers to join datasets to resolve the full classification. This created integration overhead and ambiguity about where hierarchy should be interpreted.

We need a consistent way to represent simple hierarchies in codelists

**Decision:**  

- For simple hierarchical codelists, include a `parent` column in the canonical codelist CSV.  
- `parent` stores the `reference` of another row in the same codelist.  
- Root entries have a blank `parent`.  
- Child entries must provide a non-blank `parent`.  
- Pattern scope is intentionally one-level parent-child hierarchy (not deep trees).

**Rationale:**  

Using a dedicated `parent` field:
- keeps hierarchy metadata in one canonical codelist instead of splitting across datasets
- provides one consistent pattern across codelists that need simple hierarchy
- preserves stable references and existing code-based integrations
- avoids duplicating parent metadata in application schemas and payloads
- makes hierarchy machine-readable for validation and downstream consumers

This gives clear semantics with low implementation complexity and minimal disruption.

**Consequences:**  

- Codelists that use hierarchy must validate `parent` references against existing `reference` values in the same file.  
- Child rows require `parent`; root rows must leave `parent` blank.  
- Downstream code can treat codelist references as before, and optionally resolve hierarchy from codelist metadata when needed.

**Alternatives considered:**  

- Keep separate parent and child codelists and join them downstream -> rejected due to integration friction and ambiguous source of truth.  
- Introduce a graph/tree model with recursive parent chains -> rejected as unnecessary complexity for current use cases.
