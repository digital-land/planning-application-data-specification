# Planning application data specification

This repository contains the data specifications that define how planning application data should be structured.

It is an initiative led by the Ministry of Housing, Communities and Local Government aiming to standardise and increase the value of planning application data.

To find out more about the background to the project, visit the [planning application project page](https://design.planning.data.gov.uk/project/planning-applications).

### What the specification covers

The specification covers what needs to be:

* **submitted** - it defines what information is needed for each type of planning application and how it should be structured
* **recorded about the application** - it defines everything a planning authority must record about a planning application, including the application itself, how it has been processed and the decisions made
* **made available as open data** - it defines what data can and must be made available as open data for the benefit of others

See [which application types are currently in scope](documentation/application-scope.md).

### The data model

The [specification](https://github.com/digital-land/planning-application-data-specification/tree/main/specification) is made up of these elements:

* [applications](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/application) - these define what is required for a given application type, for example '[householder](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/hh.schema.md?plain=1)'. See [which application types are in scope](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/application-scope.md).
* [modules](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/module) - groupings of fields focused on a specific subject. For example '[agent details](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/agent-details.schema.md?plain=1)'
* [components](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/component) - reusable groups of fields, or substructures that are used by multiple modules. For example '[supporting documents](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/component/supporting-document.md?plain=1)'
* [fields](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field) - these define the specific fields, setting expectations for the field. For example '[decision date](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/decision-date.md?plain=1)'
* [codelists](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/codelist) - these set the allowable values for a given field, for example '[parking space type](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/codelist/parking-space-type.schema.md?plain=1)'
* [datasets](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/dataset) - these cover how the submitted and recorded information should be structured, for example '[site](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/dataset/site.schema.md?plain=1)'

There is more information on how the specification is structured in the [/documentation folder](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation).

#### Other ways to access the specification

The canonical specification in this repository is used to generate the following outputs:

* [a specification viewer](https://digital-land.github.io/planning-application-data-specification/) for an easier way to view and explore the specification
* [compiled markdown representations of each application type](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/info_model/application) showing what is expected to be submitted for each application type
* [spreadsheets for each application type](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/spreadsheet) so that people can use those to perform analysis tasks
* [JSON schemas](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/json-schema/applications) for each application type, which can be used to build services

If you are new to the repository, start with [how the specification fits together](https://github.com/digital-land/planning-application-data-specification/blob/main/documentation/how-the-specification-fits-together.md).

---

## CLI

`spec.py` is a command line tool for exploring this repository.

Use it when you want to inspect the specification, check how specification elements are connected, or run the small set of project reports that are maintained with the repository.

Run commands from the repository root:

```bash
python spec.py --help
```

The CLI has three main command groups:

- `inspect` for the canonical specification model
- `report` for repository summaries and progress reports
- `analysis` for useful side datasets, such as the 2025 forms analysis

For usage examples and the command reference, see [spec CLI](documentation/spec-cli.md).

---

## We need your help

It is important that these specifications work for everyone who needs them, such as software vendors, planning officers, analysts and policymakers. For that to happen we need your feedback, questions and contributions.

You can comment on any of the items in this repository and we encourage you to help us work through outstanding [issues](https://github.com/digital-land/planning-application-data-specification/issues).

You can get involved by:

* raising and commenting on [issues](https://github.com/digital-land/planning-application-data-specification/issues)
* participating in [discussions](https://github.com/digital-land/planning-application-data-specification/discussions) around applications, modules and codelists
* joining the regular community sessions, the date of the next event can be found on the [project page](https://design.planning.data.gov.uk/project/planning-applications)

### Maintaining a CHANGELOG

We maintain a [CHANGELOG](CHANGELOG.md) using [git-chglog](https://github.com/git-chglog/git-chglog). This groups commits by type and into releases. Types are configurable and set in [.chglog/config.yml](.chglog/config.yml). Releases are handled by `git tag`.

If you make a PR with a number of commits (following [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)) and want to update the CHANGELOG, run

```
git tag -a v{version_number} -m "{release description}"
# then
git-chglog -o CHANGELOG.md
```
