## Decision: Name the decision notice dataset `decision-notice`

**Date:** 2026-01-09  
**Status:** Under review  

**Context:**  

While publishing the decision stage specification, a dataset was introduced to represent the outcome of a planning application and the information formally issued by the authority.  

This dataset was initially named `decision`. However, the term “decision” is already used within the model to represent the outcome itself (e.g. granted, refused, withdrawn), and the dataset captures more than just that outcome. It represents the decision notice as a whole, including the information published on the notice and referenced by other decision-stage datasets.

Using the same term for both the dataset and a core field introduces ambiguity and creates naming conflicts when establishing references between datasets.

**Decision:**  
We will rename the dataset from `decision` to `decision-notice`.

**Rationale:**  
The dataset represents the decision notice, not just the decision outcome. The decision itself is one attribute of that notice, alongside other published information. Naming the dataset `decision-notice`:
- reflects the real-world artefact being modelled
- avoids overloading the term “decision” at both dataset and field level
- enables a clear and consistent field naming model (e.g. `decision: granted`)
- allows other datasets (e.g. decision-conditions) to reference the notice explicitly using a `decision-notice` identifier  

For example:
- the decision notice dataset can include a `decision` field to capture the outcome
- datasets such as `decision-condition` can reference the notice via a `decision-notice` field (e.g. `decision-notice: dec-001201`)

This improves clarity, supports clean referencing, and reduces the risk of confusion as the decision-stage model expands and is reused more widely.

**Alternatives Considered:**  
- Keeping the dataset named `decision` → rejected due to ambiguity and naming conflicts with the decision outcome field.  
- Renaming the decision outcome field instead → rejected as the field name is clear, well-understood, and already semantically correct.  
- Introducing compound or overloaded field names (e.g. `decision-reference`) → rejected as it obscures meaning rather than clarifying it.
