# Planning application data specification

This repository contains data specifications used to exchange planning application data.

It is an initiative lead by the Ministry of Housing, Communities and Local Governemnt (MHCLG) aiming to standardise what data is exchanged when a planning application is submitted.

The specification will consist of a number of "modules", one data specification per module, and will set out which modules are required for each application type.

This initiatives aims to improve the use, interoperability and consistency of planning application data that moves through the UK planning system.

#### Background

We started this initiative to create baseline planning application specifications that can be evolved over time, and to improve the use, interoperability and consistency of planning application data that flows through the UK planning system. For some background, you can check out our[ initial blog post](https://mhclgdigital.blog.gov.uk/2024/10/18/using-data-design-to-transform-the-planning-application-process-get-involved/) and a follow upblog post about the [first 2 events we held](https://mhclgdigital.blog.gov.uk/2024/12/06/digital-planning-developing-planning-applications-specifications-in-the-open/).

To support this work, we set up [an advisory group](https://design.planning.data.gov.uk/advisory-group) and have been sharing high-level updates through a [GitHub discussion](https://github.com/digital-land/data-standards-backlog/discussions/98). However, as the discussion has grown quite lengthy, we’ve decided to create this repository to help manage the issues more effectively, allow contributors to focus on them one at a time.


## Application types

Below is the list of official application types, and their sub-types where application that we are working through.

You can download a csv of [planning application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv) and [sub-types](http://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv).

| Application type | Sub type | Spec | Notes |
|---|---|---|---|
| [Advertising](https://github.com/digital-land/planning-application-data-specification/discussions/171) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/advertising.md) | |
| [Approval (discharge) of conditions](https://github.com/digital-land/planning-application-data-specification/discussions/173) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/approval-condition.md) | |
| [Consent under TPO](https://github.com/digital-land/planning-application-data-specification/discussions/220) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/consent-under-tpo.md) | |
| [Development relating to the onshore extraction of oil and gas](https://github.com/digital-land/planning-application-data-specification/discussions/176) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/extraction-oil-gas.md) | _A form of full planning with enough difference to warrant its own type_ |
| [Full planning permission](https://github.com/digital-land/planning-application-data-specification/discussions/167) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/full.md) | |
| [Hedgerow removal notice](https://github.com/digital-land/planning-application-data-specification/discussions/218) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/hedgerow-removal.md) | |
| [Householder planning application](https://github.com/digital-land/planning-application-data-specification/discussions/166) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/hh.md) | |
| Lawful development certificate | [Existing use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/182) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/ldc-ldc-existing-use.md) | |
| Lawful development certificate | [Prospective use of the site](https://github.com/digital-land/planning-application-data-specification/discussions/181) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/ldc-ldc-prospective-use.md) | |
| Lawful development certificate | [Proposed work to a listed building](https://github.com/digital-land/planning-application-data-specification/discussions/180) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/ldc-ldc-proposed-work-lb.md) | |
| [Listed building consent](https://github.com/digital-land/planning-application-data-specification/discussions/170) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/lbc.md) | |
| [Non-material amendment](https://github.com/digital-land/planning-application-data-specification/discussions/174) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/non-material-amendment.md) | |
| [Notification of proposed works to trees in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/219) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/notice-trees-in-con-area.md) | |
| Outline planning | [All matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/179) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/outline-outline-all.md) | |
| Outline planning | [Some matters reserved](https://github.com/digital-land/planning-application-data-specification/discussions/178) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/outline-outline-some.md) | |
| [Permission in principle](https://github.com/digital-land/planning-application-data-specification/discussions/175) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/pip.md) | |
| [Planning permission for relevant demolition in a conservation area](https://github.com/digital-land/planning-application-data-specification/discussions/169) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/demolition-con-area.md) | |
| Prior approval | [Larger Home Extension](https://github.com/digital-land/planning-application-data-specification/discussions/183) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/prior-approval-pa-extension.md) | |
| Prior approval | [Additional storeys](https://github.com/digital-land/planning-application-data-specification/discussions/184) | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/prior-approval-pa-storey.md) | |
| [Removal/variation of conditions (S73)](https://github.com/digital-land/planning-application-data-specification/discussions/172) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/s73.md) | |
| [Reserved matters](https://github.com/digital-land/planning-application-data-specification/discussions/168) | | [see spec](https://github.com/digital-land/planning-application-data-specification/blob/main/specification/application/reserved-matters.md) | |


## Contributing

It is important that these specifications work for the people (software vendors, planning officers, analysts, policy makers) that need them. For that to happen we need feedback, questions and contributions from the community.

You can comment on any of the items in this respository and we encourage you to help us work through the [issues](https://github.com/digital-land/planning-application-data-specification/issues).

