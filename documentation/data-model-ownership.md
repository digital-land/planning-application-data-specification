# Ownership of data-model definitions

Fields, datasets, specifications and views have distinct responsibilities. Independently defined datasets are brought together by a specification, following the Digital Land pattern.

| Layer | Responsibility |
| --- | --- |
| Field | Define a reusable property and its default characteristics. |
| Dataset | Define a record: its fields, contextual descriptions, recording requirements and relationships to other records. |
| Specification | Assemble the related datasets that describe a subject or process, establishing their collective scope and a named entry point for people and machines. |
| View | Select existing datasets, fields and records for a specific purpose, with requirements appropriate to that purpose. |

A dataset can be understood independently and reused in another specification. The assembly identifies which datasets together constitute, for example, planning application data. It enables consumers to start at one definition and discover the related records making up that specification.

## Relationships belong in dataset definitions

A field usage's target dataset describes the relationship between records. For example, `discharged-by` in `decision-condition` refers to a `decision-notice` record:

```yaml
- field: discharged-by
  dataset: decision-notice
```

Declare this target on the field usage in the dataset definition so it is available independently of an assembly or viewer. A viewer can use the target to construct a link, but the relationship is part of the data model rather than presentation metadata.

## Current assembly files

The planning application data assembly currently repeats field lists, descriptions, requirements and some relationships from individual datasets. Relationship targets are retained in the assembly and also declared in the datasets. Keep those declarations consistent while both exist.

Whether to simplify duplicated field declarations, where to maintain field ordering and how to resolve assembly-level wording are deferred questions. This ownership model does not remove existing declarations or establish a new override API. See the [outstanding specification questions](../tmp/specification-questions-to-return-to.md#duplicated-field-declarations-in-specification-assemblies).

Views have a separate selection role. They do not change the structure of existing data; see [Creating views](views.md).
