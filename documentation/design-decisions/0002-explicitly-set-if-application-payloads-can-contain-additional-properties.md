## Decision: Put additional submission data in a named block

**Date:** 2025-12-16
**Updated:** 2026-10-28
**Status:** Proposed

**Context:**
Submission services may need to provide information that the national submission specification does not define, for example to meet a local requirement or support an integration. The original approach set `allow-additional-properties: true` on application definitions, allowing any extra property at the payload root.

That leaves extra information mixed with standard fields and modules. An extra name could conflict with a future standard name, and a misspelt optional standard name could pass validation without being recognised as the intended field or module.

**Decision:**
Set `allow-additional-properties: false` on application definitions. The root payload may contain only the fields and modules in its resolved application definition. Include an optional top-level `additional-data` field in current application definitions for information outside the national model.

The `additional-data` field has `datatype: object` and field-level `allow-additional-properties: true`. The national JSON Schema checks that its value is an object but does not constrain the properties or values within it. Standard fields and modules retain their existing validation rules.

**Rationale:**
The named block preserves room for local and supplier data while giving it a predictable location. Closing the root protects standard names and allows future top-level properties to be added deliberately. A field is appropriate because this is an optional property of the submission payload, not a form section with nationally defined questions.

**Consequences:**
Existing payloads with extra top-level properties must move those properties inside `additional-data` to validate against the revised schemas. Receiving systems should not assume that the national schema validates or gives meaning to the block's contents. Suppliers may group their entries under a stable supplier or service name to reduce clashes within the block.

**History:**
The 2025 decision introduced the application-level `allow-additional-properties` flag so openness would be explicit rather than relying on JSON Schema's default. This 2026 revision retains that flag but sets it to `false` and provides a named place for additional data. Restricting the block for individual application types, including inherited or combined types, is a separate future decision.
