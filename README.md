# Planning application data specification

This repository contains data specifications used to exchange planning application data.

It is an initiative lead by the Ministry of Housing, Communities and Local Government (MHCLG) aiming to standardise what data is exchanged when a planning application is submitted.

The specification is made up of these elements:

* [Applications](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/application) - these define what is required for a given application type, for example, [Householder](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/hh.schema.md?plain=1)
* [Modules](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/module) - groupings of fields focused on a specific subject. For example, [agent details](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/module/agent-details.schema.md?plain=1)
* [Components](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/component) - resuable groups of fields, or substructures that are used by multiple modules. For example, [supporting documents](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/component/supporting-document.md?plain=1)
* [Fields](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/field) - these deine the specific fields, setting expectations for the field. For example, [decision date](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/field/decision-date.md?plain=1)
* [Codelists](https://github.com/digital-land/planning-application-data-specification/tree/main/specification/codelist) - these set the allowable values for a given field, for example, [parking space type](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/codelist/parking-space-type.schema.md?plain=1)


You can get involved by:

* raising and commenting on [issues](https://github.com/digital-land/planning-application-data-specification/issues)
* participating in [discussions](https://github.com/digital-land/planning-application-data-specification/discussions) around applications, modules and codelists

#### Background

More background can be found on the [planning application project page](https://design.planning.data.gov.uk/project/planning-applications).

## Application types

Below is the list of official application types (and their sub-types where applicable) that we are working through.

You can download a csv of [planning application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv) and [sub-types](http://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv).

| Application type | Sub type | Spec | Notes |
|---|---|---|---|
| [Advertising](https://github.com/digital-land/planning-application-data-specification/discussions/171) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/advertising.md) | |
| [Approval (discharge) of conditions](https://github.com/digital-land/planning-application-data-specification/discussions/173) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/approval-condition.md) | |
| [Consent under TPO](https://github.com/digital-land/planning-application-data-specification/discussions/220) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/consent-under-tpo.md) | |
| [Development relating to the onshore extraction of oil and gas](https://github.com/digital-land/planning-application-data-specification/discussions/176) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/extraction-oil-gas.md) | _A form of full planning with enough difference to warrant its own type_ |
| [Full planning permission](https://github.com/digital-land/planning-application-data-specification/discussions/167) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/full.md) | |
| [Hedgerow removal notice](https://github.com/digital-land/planning-application-data-specification/discussions/218) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/hedgerow-removal.md) | |
| [Householder planning application](https://github.com/digital-land/planning-application-data-specification/discussions/166) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/hh.md) | |
| Lawful development certificate | [Existing use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/182) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/ldc-ldc-existing-use.md) | |
| Lawful development certificate | [Prospective use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/181) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/ldc-ldc-prospective-use.md) | |
| Lawful development certificate | [Proposed work to a listed building](https://github.com/digital-land/planning-application-data-specification/discussions/180) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/ldc-ldc-proposed-work-lb.md) | |
| [Listed building consent](https://github.com/digital-land/planning-application-data-specification/discussions/170) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/lbc.md) | |
| [Non-material amendment](https://github.com/digital-land/planning-application-data-specification/discussions/174) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/non-material-amendment.md) | |
| [Notification of proposed works to trees in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/219) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/notice-trees-in-con-area.md) | |
| Outline planning | [All matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/179) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/outline-outline-all.md) | |
| Outline planning | [Some matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/178) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/outline-outline-some.md) | |
| [Permission in principle](https://github.com/digital-land/planning-application-data-specification/discussions/175) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/pip.md) | |
| [Planning permission for relevant demolition in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/169) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/demolition-con-area.md) | |
| Prior approval | [Larger Home Extension](https://github.com/digital-land/planning-application-data-specification/discussions/183) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/prior-approval-pa-extension.md) | |
| Prior approval | [Additional storeys](https://github.com/digital-land/planning-application-data-specification/discussions/184) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/prior-approval-pa-storey.md) | |
| [Removal/variation of conditions (S73)](https://github.com/digital-land/planning-application-data-specification/discussions/172) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/s73.md) | |
| [Reserved matters](https://github.com/digital-land/planning-application-data-specification/discussions/168) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/generated/info_model/application/reserved-matters.md) | |


## Contributing

It is important that these specifications work for the people (software vendors, planning officers, analysts, policy makers) that need them. For that to happen we need feedback, questions and contributions from the community.

You can comment on any of the items in this repository and we encourage you to help us work through the [issues](https://github.com/digital-land/planning-application-data-specification/issues).

