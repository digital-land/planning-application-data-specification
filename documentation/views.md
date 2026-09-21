# Creating views

A view defines a specific cut of existing specification data for a stated purpose and set of user needs. For example, the national public view selects the information to publish openly from the wider planning application data specification. Other views may serve different purposes; being a view does not itself mean the information is public.

A view selects existing data; changing its structure would need an explicit transformation model. Views configure the use of existing datasets and fields rather than introduce new data-model elements.

## What a view can define

A view lets you:

- Select datasets and fields that already exist in the specification.
- Set a requirement level for each selected field, independently of its requirement in the underlying dataset.
- Filter which records from a selected dataset are included, using rules expressed as `record-inclusion` in the view file.
- Override field names and descriptions where wording specific to the view's purpose is useful (do this cautiously)

Field selection controls which properties appear; record filters control which records appear. 
For example, the national public view includes planning application document records only when their `public-register-status` is `publish`. A document with another status, or no status, is excluded entirely, even if it contains fields selected by the view. 

Without a record-inclusion rule, all records from the selected dataset are included, with only the selected fields.

## Start with the purpose

Before creating a view, explain who needs this cut of the data, what they will use it for and why an existing view does not meet that need. Link to the relevant user needs (or objective). Choose datasets, fields and any record-inclusion rules to serve that purpose.

The [national public view schema](../specification/national-public-view.schema.md) is the existing example. Its [output and record-inclusion guidance](required-national-public-view-output-and-rules-for-deriving-it.md) explains how its selection is expressed. View definitions currently use a `specification` reference ending in `-view` in a root-level specification schema file. The package and integrity checks use this convention to distinguish views from other specification profiles.

The package provides a [view-resolution interface](../planning_application_specification/README.md#resolving-views). Integrity checks and package loading of a view share validation for selected references, duplicate selections, prohibited structural overrides, requirement levels and record-filter shapes. They do not execute record filters or establish that codelist profile selections meet the view's user needs.

## Explicit selection and order

- Include only datasets explicitly listed in the view file, in their authored order.
- Within each selected dataset, include only fields explicitly listed for that dataset in the view file, in their authored order.
- Fields omitted from the view stay excluded even when they exist in the underlying dataset.
- Select fields from the underlying dataset definition. Define new data-model elements in the underlying specification before selecting them in a view.
- Use record-inclusion rules when the purpose requires a subset of records. See the existing output guidance for supported rule shapes.

## Field properties and overrides

`name` and `description` are optional field-usage overrides in a view file. Resolve each using this precedence:

1. The view's override, if supplied.
2. The dataset's field-usage override, if supplied.
3. The base field definition.

Omit an override when the existing wording is suitable. Clarify the selected data's meaning for the view's purpose without changing the underlying meaning of the field.

Datatype and cardinality come from the resolved dataset field. Do not override them in a view file. Restructuring records, converting datatypes or changing cardinality requires a separately defined transformation model; it is outside the current view model.

Set `requirement-level` independently for each selected field in the view. It does not inherit from the dataset: a requirement to record information is distinct from a requirement to publish it. Omission means unspecified, not optional or inherited. Follow [Required fields and requirement levels](requirement-levels.md).

## Review a view

Check that its selection supports the stated needs, that every selected field belongs to its underlying dataset and that its descriptions preserve the field's meaning. For a publication view, review whether the selected records and fields are appropriate for that audience. Keep selection separate from transformation, and document any unresolved rules before implementing them.
