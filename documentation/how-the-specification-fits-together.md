# How the specification fits together

This note is a short primer on the structure of the planning application data specification and where to find the main pieces within it.

In particular, it explains:

- how applications, modules, fields and codelists relate to each other
- where to find field datatypes and formats
- where to find controlled vocabularies and the codelists linked to fields
- where to use the specification viewer and where to use the GitHub repository

The short version is:

- every field has a definition
- every field definition includes a datatype
- if a field uses a controlled list, the field definition names the codelist
- the codelist then defines the allowed values

## Start here

The easiest place to browse the specification is the viewer site:

- [Planning application data specification](https://digital-land.github.io/planning-application-data-specification/)
- [Submission specification](https://digital-land.github.io/planning-application-data-specification/submission/)
- [Decision specification](https://digital-land.github.io/planning-application-data-specification/decision-stage/)
- [Shared elements](https://digital-land.github.io/planning-application-data-specification/shared-elements/)
- [Fields](https://digital-land.github.io/planning-application-data-specification/fields/)
- [Codelists](https://digital-land.github.io/planning-application-data-specification/codelist/)

The underlying canonical files are in GitHub:

- [Repository root](https://github.com/digital-land/planning-application-data-specification)
- [Specification overview](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/README.md)
- [Fields folder](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field)
- [Codelists folder](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/codelist)

## How the parts fit together

At a high level the specification works like this:

- an application definition says what is needed for a given application type
- an application uses modules
- a module groups related fields
- a field defines an individual data item, including its datatype
- if the field is controlled, the field definition points to a codelist
- the codelist defines the allowed values

In other words:

`application -> module -> field -> datatype / codelist`

This is why the field definition is the key place to look when you want to know how a field is defined.

## Where to find the datatype or format for a field

Every field has a datatype defined in its field definition.

The easiest place to browse fields is:

- [Fields in the specification viewer](https://digital-land.github.io/planning-application-data-specification/fields/)

The canonical source files are here:

- [Field definition files in GitHub](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field)

For example, the field definition for `decision-date` shows the datatype directly:

```yaml
field: decision-date
datatype: string
description: The date when the decision was made, in YYYY-MM-DD format
```

Source:

- [decision-date field definition](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/decision-date.md)

So if the question is, "Where do I see the format or data type for this field?", the answer is: open the field definition and look for the `datatype` line and, where helpful, the description.

## Where to find which codelist applies to a field

If a field uses a controlled vocabulary, the field definition will show:

- `datatype: enum`
- `codelist: ...`

For example:

```yaml
field: application-type
datatype: enum
codelist: application-type
```

Source:

- [application-type field definition](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/application-type.md)

That tells you the field is an enum and that the relevant codelist is `application-type`.

You can then look up that codelist here:

- [Codelists in the specification viewer](https://digital-land.github.io/planning-application-data-specification/codelist/)
- [application-type codelist definition](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/codelist/application-type.schema.md)
- [application-type codelist values](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)

So if the question is, "Where do I see which code list applies to this field?", the answer is: open the field definition first. If it is an enum, the field definition will name the codelist.

## A second concrete example

The same pattern applies to other controlled fields. For example:

```yaml
field: contact-priority
datatype: enum
codelist: contact-priority
```

Source:

- [contact-priority field definition](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/contact-priority.md)
- [contact-priority codelist definition](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/codelist/contact-priority.schema.md)

## Where spreadsheets and compiled views fit in

The repository also includes generated views that are useful for browsing:

- [Compiled application views](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/info_model/application)
- [Spreadsheet views](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/spreadsheet)

These are useful reading views, but they are generated from the underlying specification files. If you need the exact datatype or the exact codelist link for a field, the canonical field definition is the most direct place to look.

For example:

- [Full planning permission compiled view](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/full.md)

## Short version you can reuse

If useful, you can send suppliers the following summary:

> Every field in the specification has a field definition. That definition shows the field datatype. If the field uses a controlled list, the same definition also names the codelist. The easiest way to browse these is via the specification viewer, especially the [fields](https://digital-land.github.io/planning-application-data-specification/fields/) and [codelists](https://digital-land.github.io/planning-application-data-specification/codelist/) sections. The underlying canonical files are in the GitHub repository under [`specification/field`](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field) and [`specification/codelist`](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/codelist).
