## Decision: Single document reference pattern for modules

**Date:** 2026-01-14  
**Status:** Proposed  

**Context:**  
- Multiple components/fields (`plans-document`/`plans-documents`, `supporting-document`/`supporting-documents`) captured document data, sometimes duplicating names already in `application.documents`.  
- Cross-references to `application.documents` were inconsistent; some modules re-collected `name`, creating ambiguity (see issues #286, #334, PP board item 345).  

**Decision:**  
- Use a single reference component (`supporting-document`) for all module-level document references (plans, drawings, supporting material). It holds only `reference`.  
- Use one list field (`supporting-documents`) wherever document references are needed; `plans-document`/`plans-documents` are deprecated and end-dated.  
- Module rules must enforce that every referenced `reference` exists in `application.documents`.  
- `application.documents` remains the source of truth for metadata and files (reference, name, description, document-types, uploaded-date, file).  
- Do not collect duplicate names/descriptions in module-level references.  

**Consequences:**  
- Examples and any remaining modules using `plans-documents`/`plans-document` must be updated to `supporting-documents` + `supporting-document`.  
- Validation rules focus on presence (where required) and cross-reference to `application.documents`; uniqueness is handled by the document list.  
- Downstream consumers can rely on a single reference pattern and on `application.documents` for display metadata and categorisation.  
