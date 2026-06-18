# spec CLI

`spec.py` is the command line tool for exploring this repository.

Use it when you want to inspect the specification, check how specification elements are connected, or run the small set of project reports that are maintained with the repository.

Run commands from the repository root:

```bash
python spec.py --help
```

The CLI has three main command groups:

- `inspect` for the canonical specification model
- `report` for repository summaries and progress reports
- `analysis` for useful side datasets, such as the 2025 forms analysis

## Inspect the specification

Use `inspect` when you want to look up something in the canonical specification.

```bash
python spec.py inspect application full
python spec.py inspect application "hh;lbc"
python spec.py inspect module agent-details
python spec.py inspect component supporting-document
python spec.py inspect field application-type
python spec.py inspect codelist application-type
```

These commands print a readable summary of the selected item.

For example:

```bash
python spec.py inspect field application-type
```

shows the field name, datatype, whether it is required, cardinality and any descriptive notes held in the specification.

```bash
python spec.py inspect application full
```

shows the resolved application definition, including the modules used by that application.

For controlled combined applications, pass the combined application type as one argument:

```bash
python spec.py inspect application "hh;lbc"
```

This resolves the controlled combination from `specification/combined-application-types.csv`, prints `Combined: yes`, and shows the deduplicated module list derived from the member application types. Input order is normalised, so `"lbc;hh"` resolves to `"hh;lbc"`.

Only combinations that are active in `specification/combined-application-types.csv` can be resolved this way. Unknown combinations are rejected, and recognised but inactive combinations are not treated as available application definitions.

## Find where things are used

Use `inspect uses` for reverse lookups.

```bash
python spec.py inspect uses application full
python spec.py inspect uses application "hh;lbc"
python spec.py inspect uses module agent-details
python spec.py inspect uses field application-type
python spec.py inspect uses component address
```

The commands answer different relationship questions:

| Command | Use it to find |
| --- | --- |
| `inspect uses application <application_ref>` | modules used by a single or controlled combined application |
| `inspect uses module <module_ref>` | applications that use a module |
| `inspect uses field <field_ref>` | datasets, modules and components that include a field |
| `inspect uses component <component_ref>` | fields and modules that use a component |

`inspect uses module` includes active controlled combined application types when the combined application uses the module.

For example:

```bash
python spec.py inspect uses field description
```

prints the datasets, modules and components that directly include the `description` field:

```text
Field: description
Datasets: 3
- planning-application: Planning application
- planning-condition: Planning condition
- site: Site

Modules: 12
...

Components: 3
...
```

For component usage:

```bash
python spec.py inspect uses component applicant
```

prints the fields that reference the `applicant` component and the modules that use those fields:

```text
Component: applicant
Fields: 1
- applicants: Applicants

Modules: 1
- applicant-details: Applicant details
```

This uses the same package-backed component usage query as the Python API.

## Run repository reports

Use `report` for maintained summary views over the repository.

```bash
python spec.py report summary
python spec.py report summary --markdown
```

`report summary` prints counts for the main specification record types: applications, modules, fields, components, codelists, datasets and specifications.

The markdown option is useful when you want to write the summary into a document:

```bash
python spec.py report summary --markdown > issue-tracking/declarative-model-progress.md
```

## Check completeness

Use `report completeness` to inspect the completeness report based on the application volume CSV.

```bash
python spec.py report completeness
python spec.py report completeness summary
python spec.py report completeness summary --verbose
python spec.py report completeness scope
python spec.py report completeness scope --verbose
```

By default these commands use:

```text
bin/admin_data/2024-application-volumes.csv
```

You can pass a different CSV with `--input`:

```bash
python spec.py report completeness summary --input path/to/application-volumes.csv
```

`summary` reports volumes and the percentage covered by the specification.

`scope` reports which application types are treated as in scope or out of scope for the completeness calculation.

Add `--verbose` when you need the row-level lists behind the summary.

## Check decision-stage needs coverage

Use the decision report to see how many decision-stage needs are covered by justifications.

```bash
python spec.py report decision summary
python spec.py report decision summary --list
```

`--list` prints the covered need ids and the justification ids that cover them.

## Explore 2025 forms analysis

Use `analysis forms` to query the analysed 2025 form data.

This data is useful context, but it is not the canonical specification model. The commands are grouped under `analysis` to keep that distinction clear.

```bash
python spec.py analysis forms list full
python spec.py analysis forms urls full
python spec.py analysis forms show form-app-for-pp
python spec.py analysis forms for-module agent-details
python spec.py analysis forms modules form-app-for-pp
```

The forms commands answer these questions:

| Command | Use it to find |
| --- | --- |
| `analysis forms list <application_type>` | analysed 2025 forms that cover an application type or subtype |
| `analysis forms urls <application_type>` | matching form URLs for an application type or subtype |
| `analysis forms show <form_ref>` | core details for one analysed form |
| `analysis forms for-module <module_ref>` | analysed forms that include a module |
| `analysis forms modules <form_ref>` | analysed modules found in one form |

For combined forms, pass the combined application type as one argument:

```bash
python spec.py analysis forms urls "hh;lbc"
```

## Command reference

```text
python spec.py
  inspect
    application <application_ref>
    module <module_ref>
    component <component_ref>
    field <field_ref>
    codelist <codelist_ref>
    uses
      application <application_ref>
      module <module_ref>
      field <field_ref>
      component <component_ref>

  report
    summary [--markdown]
    completeness [--input <csv>] [--verbose]
    completeness summary [--input <csv>] [--verbose]
    completeness scope [--input <csv>] [--verbose]
    decision
      summary [--list]

  analysis
    forms
      list <application_type>
      urls <application_type>
      show <form_ref>
      for-module <module_ref>
      modules <form_ref>
```

You can also ask for help at any level:

```bash
python spec.py --help
python spec.py inspect --help
python spec.py inspect uses --help
python spec.py report completeness --help
python spec.py analysis forms --help
```
