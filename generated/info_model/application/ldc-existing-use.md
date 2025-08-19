# LDC Existing Use

Existing use of the site

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Description of existing use](#description-of-existing-use)
* [Use works activity](#use-works-activity)
* [Grounds for lawful development certificate](#grounds-for-lawful-development-certificate)
* [Information to support LDC](#information-to-support-ldc)
* [Residential units](#residential-units)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |

## Description of existing use

Information about the existing uses of the development site, including 
use classes and which parts of the land they relate to


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| existing-use-details | Existing use details[]{} | List of existing site uses and related land areas | MUST |  |


**Existing use detail model**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-details | Use details | Further detail of the use | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`
land-part | Land part | Which part of the land the use relates to | MUST | 

**Validation rules**

- existing-use-details must contain at least one item
- if use == 'sui' OR use == 'other' then use-details is required

## Use works activity

Information about what the lawful development certificate is needed for and related use details

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| ldc-need | LDC need[] | What is the lawful development certificate needed for? | MUST | Select from the **lawful-development-need** enum. At least one value must be provided |
| use | Use | A use class or type of use | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY |  |

**Validation rules**

- At least one ldc-need value must be provided
- use is required when ldc-need contains existing-use or breach-con-existing-use
- specified-use is required when use is sui or other

## Grounds for lawful development certificate

Grounds on which a lawful development certificate is being sought,
including supporting evidence and explanations


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| grounds-pre-2024 | Grounds pre 2024[] | List of grounds pre 2024-04-25 under which the certificate is sought | MAY | Select from the **grounds-ldc-pre-apr-2024** enum |
| grounds-post-2024 | Grounds post 2024[] | List of grounds post 2024-04-25 under which the certificate is sought | MAY | Select from the **grounds-ldc-post-apr-2024** enum |
| other-details | Other details | Explanation if other ground is selected | MAY |  |
| supporting-applications | Supporting applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site | MAY |  |
| reason | Reason | A textual reason | MUST |  |


**Supporting applications model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference-number | Reference number | Reference number of the planning permission | MAY | 
condition-number | Condition number | Number of any condition being breached | MAY | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- grounds-pre-2024 is not empty OR grounds-post-2024 is not empty
- if grounds-pre-2024 contains 'other' OR grounds-post-2024 contains 'other' then other-details is required

## Information to support LDC

Information to support Lawful Development Certificate applications including
details of existing use, interruptions, and changes to support evidence of lawfulness


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| existing-use-start-date | Existing use start date | Date when the existing use of the land or building commenced, in YYYY-MM-DD format | MUST |  |
| has-existing-use-interrupted | Existing use interrupted | Indicating whether the existing use has been interrupted since it commenced | MUST |  |
| interruption-details | Interruption details | Details of any interruption to the existing use including dates and circumstances | MAY | Rule: is a MUST if `has-existing-use-interrupted` is `True` |
| has-existing-use-changed | Existing use change | Indicate whether there has been any change in the existing use since it commenced | MUST |  |
| existing-use-change-details | Existing use change details | Details of any changes to the existing use including nature of changes and dates | MAY | Rule: is a MUST if `has-existing-use-changed` is `True` |

**Validation rules**

- existing-use-start-date matches YYYY-MM-DD format
- existing-use-start-date <= current_date
- has-existing-use-interrupted == true REQUIRES interruption-details.length > 0
- has-existing-use-changed== true REQUIRES existing-use-change-details.length > 0
- interruption-details must specify dates and nature of interruption when provided
- existing-use-change-details must specify dates and nature of changes when provided

## Residential units

Information about residential units including existing and proposed unit counts, 
with detailed breakdowns by tenure and housing type


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| will-residential-units-change | Residential unit change | Proposal includes the gain, loss or change of use of residential units | MUST |  |
| residential-unit-summary | Residential unit summary[]{} | Breakdown of unit counts by tenure and housing type | MAY | Rule: is a MUST if `will-residential-units-change` is `True` |
| total-existing-units | Total existing units | The total number of existing units | MUST |  |
| total-proposed-units | Total proposed units | The total number of proposed units | MUST |  |
| net-change | Net change | Calculated net change in units | MUST |  |


**Residential unit summary model**

field | name | description | required | notes
-- | -- | -- | -- | --
tenure-type | Tenure type | Category of housing tenure | MUST | Select from the **tenure-type** enum
housing-type | Housing type | Type of housing | MUST | Select from the **housing-type** enum
existing-unit-breakdown | Existing unit breakdown[]{} | Number of existing units by bedroom count | MAY | 
proposed-unit-breakdown | Proposed unit breakdown[]{} | Number of proposed units by bedroom count | MAY | 


**Unit quantities model**

field | name | description | required | notes
-- | -- | -- | -- | --
units-unknown | Units unknown | Whether the number of units is unknown | MUST | 
units-per-bedroom-no | Units per bedroom number[]{} | Number of units broken down by bedroom count | MAY | Rule: is a MUST if `units-unknown` is `False`
total-units | Total units | Total number of units | MAY | 


**Bedroom count model**

field | name | description | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | No bedrooms unknown | Set to true when counting units where bedroom number is unknown | MUST | 
no-of-bedrooms | Number of bedrooms | The number of bedrooms in unit | MAY | Rule: is a MUST if `no-bedrooms-unknown` is `False`
units | Units | The number of units of that bedroom count | MUST | 

**Validation rules**

- residential-unit-summary is required when will-residential-units-change is true
- net-change is calculated as total-proposed-units minus total-existing-units
- if will-residential-units-change is true, at least one breakdown for existing and proposed is required (count could be unknown)

## Required codelists

This are the codelist required to support this specification:

- tenure-type
- use-class
- housing-type