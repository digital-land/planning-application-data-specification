# Planning application data specification

This repository contains data specifications used to submit planning application data.

It is an initiative led by the Ministry of Housing, Communities and Local Government aiming to standardise the data you provide when a planning application is submitted.

The [specification](https://github.com/digital-land/planning-application-data-specification/tree/main/specification) is made up of these elements:

* [applications](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/application) - these define what is required for a given application type, for example '[householder](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/hh.schema.md?plain=1)'
* [modules](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/module) - groupings of fields focused on a specific subject. For example '[agent details](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/agent-details.schema.md?plain=1)'
* [components](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/component) - resuable groups of fields, or substructures that are used by multiple modules. For example '[supporting documents](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/component/supporting-document.md?plain=1)'
* [fields](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field) - these define the specific fields, setting expectations for the field. For example '[decision date](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/decision-date.md?plain=1)'
* [codelists](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/codelist) - these set the allowable values for a given field, for example '[parking space type](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/codelist/parking-space-type.schema.md?plain=1)'

These elements are then used to generate the following outputs

* [information models](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/info_model/module) for each module
* [compiled specifications](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/info_model/application) for each application type and sub-type
* a [spreadsheet](https://github.com/digital-land/planning-application-data-specification/tree/main/generated/spreadsheet) view of each application type

## CLI

The main command line entry point is [spec.py](spec.py).

### Find and query

Find applications that use a module

```bash
python spec.py find applications-with-module <module_ref>
```

Find modules used by an application

```bash
python spec.py find modules-in-application <application_ref>
```

Find where a field is used

```bash
python spec.py find field-usage <field_ref>
```

Find where a component is used

```bash
python spec.py find component-usage <component_ref>
```

### Decision-stage summary

Summarise decision-stage needs coverage

```bash
python spec.py decision summary
```

List covered needs as well

```bash
python spec.py decision summary --list
```

### 2025 forms analysis

Return matching 2025 form URLs for an application type or subtype

```bash
python spec.py form-url <application_type>
```

List matching 2025 forms for an application type or subtype

```bash
python spec.py forms <application_type>
```

Show core details for a 2025 form by reference

```bash
python spec.py form <form_ref>
```

List analysed 2025 forms that include a module

```bash
python spec.py module-forms <module_ref>
```

These form commands use the analysed 2025 forms data under `data/analysis/`. They are not derived from the canonical specification model.

### Completeness reporting

Print the completeness summary

```bash
python spec.py completeness summary
```

Print the completeness summary with row-level detail

```bash
python spec.py completeness summary --verbose
```

Print the in-scope and out-of-scope split

```bash
python spec.py completeness scope
```

You can get involved by:

* raising and commenting on [issues](https://github.com/digital-land/planning-application-data-specification/issues)
* participating in [discussions](https://github.com/digital-land/planning-application-data-specification/discussions) around applications, modules and codelists

#### More information

To find out more about the background of the the project you can visit the [planning application project page](https://design.planning.data.gov.uk/project/planning-applications).

For help with the terminology used on this page, visit our [glossary of terms](https://standards.planning-data.dev/terms/).

## Application types

Below is the list of official application types that we have produced specifications for. Where a more specific classification is needed, the canonical [application type codelist](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv) now uses a light parent/child hierarchy in a single dataset.

We are prioritising the application types that lead to housing delivery.

#### Applications affecting housing delivery

| Application type | Child type |
|---|---|
| [Approval (discharge) of conditions](https://github.com/digital-land/planning-application-data-specification/discussions/173) | | 
| [Full planning permission](https://github.com/digital-land/planning-application-data-specification/discussions/167) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/full.md) | |
| [Householder planning application](https://github.com/digital-land/planning-application-data-specification/discussions/166) | | 
| Lawful development certificate | [Existing use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/182) | |
| Lawful development certificate | [Prospective use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/181) ||
| Lawful development certificate | [Proposed work to a listed building](https://github.com/digital-land/planning-application-data-specification/discussions/180) | |
| [Listed building consent](https://github.com/digital-land/planning-application-data-specification/discussions/170) | |
| [Non-material amendment](https://github.com/digital-land/planning-application-data-specification/discussions/174) |  |
| Outline planning | [All matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/179) ||
| Outline planning | [Some matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/178) | |
| [Permission in principle](https://github.com/digital-land/planning-application-data-specification/discussions/175) |  |
| [Planning permission for relevant demolition in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/169) | |
| Prior approval | [Larger Home Extension](https://github.com/digital-land/planning-application-data-specification/discussions/183) | |
| Prior approval | [Additional storeys](https://github.com/digital-land/planning-application-data-specification/discussions/184) | |
| [Removal/variation of conditions (S73)](https://github.com/digital-land/planning-application-data-specification/discussions/172) |  |
| [Reserved matters](https://github.com/digital-land/planning-application-data-specification/discussions/168) | |
| [Technical details consent](https://github.com/digital-land/planning-application-data-specification/discussions/343) | |

#### Other applications in scope

| Application type | Child type |
|---|---|
| [Advertising](https://github.com/digital-land/planning-application-data-specification/discussions/171) | | 
| [Consent under TPO](https://github.com/digital-land/planning-application-data-specification/discussions/220) | |
| [Development relating to the onshore extraction of oil and gas](https://github.com/digital-land/planning-application-data-specification/discussions/176) | |
| [Hedgerow removal notice](https://github.com/digital-land/planning-application-data-specification/discussions/218) | |
| [Notification of proposed works to trees in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/219) | |

#### Applications not in scope

The application types we have not yet included in these specifications are

* Additional environmental approval to extend the duration of a planning permission
* Certificate of alternative appropriate development 
* Change of use planning application 
* Circular 14/90 Overhead lines 
* Footpath diversion
* Hazardous Substances Consent 
* Land Drainage Consent 
* Mineral extraction or associated development 
* Mineral planning applications 
* Modification of conditions relating to construction working hours 
* Modification or discharge of a Section 106 planning obligation 
* Nationally Significant Infrastructure Projects (NSIPs) 
* Public Service Infrastructure applications 
* Regulation 3 planning application
* Regulation 4 planning application 
* Review of mineral permission (ROMP) 
* Transport and works act order 
* Waste development 

## We need your help

It is important that these specifications work for everyone that needs them (such as software vendors, planning officers, analysts and policymakers). For that to happen we need yor feedback, questions and contributions.

You can comment on any of the items in this repository and we encourage you to help us work through outstanding [issues](https://github.com/digital-land/planning-application-data-specification/issues).

### Maintaining a CHANGELOG

We maintain a [CHANGELOG](CHANGELOG.md) using [git-chglog](https://github.com/git-chglog/git-chglog). This groups commits by type and into releases. Types are configurable and set in [.chglog/config.yml](.chglog/config.yml). Releases are handled by `git tag`.

If you have made a number of commits (following [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)) and want to update the CHANGELOG, run

```
git tag -a v{version_number} -m "{release description}"
# then
git-chglog -o CHANGELOG.md
```
