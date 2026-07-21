# Making changes to the specification

This guide explains how to make deliberate, traceable changes to the planning application data specification. It is for contributors changing the model, its supporting needs and justifications, or its documentation and examples.

## Principles for making a change

- Start with a user need, policy requirement, delivery problem or other clearly stated reason for the change. Do not add data only because it might be useful one day.
- Prefer reuse where the existing element has the same meaning. Do not reuse an element simply because it has a similar label or datatype.
- Keep the meaning of established elements stable. Where a proposed change would alter an element's meaning, prefer a new element or deliberately generalise it with the impact made clear.
- Make linked changes together. A change to a canonical field, codelist or dataset may require changes to its usages, justification, examples, generated outputs and documentation.
- Keep the model independent of a particular form, screen or supplier implementation. Capture the information that needs to be exchanged or maintained, rather than presentation details.
- Make the rationale reviewable. Record why the change exists and what need it helps meet.
- Make small, coherent changes that can be reviewed and tested independently.

## High-level workflow

1. Describe the problem and identify the relevant user need, or create one if needed.
2. Identify the kind of model change needed and check whether an existing element can be reused without changing its meaning.
3. Update the canonical definition and every relevant usage of it in the specification.
4. Update or add justifications, examples, documentation and generated outputs where they are affected.
5. Run `make checks`, review the generated and rendered outputs where relevant, and make the change available for review.

## Change types

- [Fields](#fields)
  - [Adding a field](#adding-a-field)
  - [Removing a field](#removing-a-field)
  - [Changing a field](#changing-a-field)
- Components (needs content)
- Modules (needs content)
- Datasets (needs content)
  - Adding a dataset (needs content)
  - Removing a dataset (needs content)
  - Changing a dataset (needs content)
  - Adding a field to a dataset
- Codelists (needs content)
- Codelist values (needs content)
- Application types (needs content)
- User needs (needs content)
- Justifications (needs content)

## Fields

Fields are canonical definitions of individual data points. They are reused in modules and datasets where their semantic meaning holds. See [Fields](fields.md) for the field model and reuse principles.

### Adding a field

1. Identify the user need or other reason for the information.
2. Search the existing fields and reuse one only if it describes the same real-world concept. If an existing field is too narrow but can safely be generalised, assess every current usage before changing it.
3. Add the canonical field definition in `specification/field/`. Give it a stable `field` reference, a concise `name`, a plain-language `description`, an appropriate `datatype`, cardinality and entry date.
4. Run `make checks`

### Removing a field


### Changing a field

First decide whether the proposed change preserves the field's meaning.

For a non-semantic change, such as clearer wording, a corrected datatype constraint or improved guidance:

1. Update the canonical field definition.
2. Review every usage to decide whether a context-specific override, description or validation rule also needs changing.
3. Update affected examples, documentation and justifications.
4. Run `make checks`

For a semantic change, such as changing what information the field represents:

1. ...

## Datasets

### Adding a field to a dataset

1. Check the field you want to add exists. If not, follow the steps in "Fields: Adding a field"
2. Identify which dataset you want to add the field to
3. Add the field to the `fields` property
4. If a more specific description than the canonical field description is needed, include that in the entry too
5. Include any other overrides if they are absolutely necessary
6. Then look for specifications and views where the dataset is used. For example decide if you want to include this field. If so, follow steps 1-4 and add. It is likely to be a copy and paste. The key specifications and views to check are [planning-application-data.schema.md](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/planning-application-data.schema.md) and [national-public-view.schema.md](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/national-public-view.schema.md)
7. Run `make checks` to confirm there are no issues