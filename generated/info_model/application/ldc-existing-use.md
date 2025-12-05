# LDC Existing Use

Existing use of the site

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Checklist](#checklist)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Description of existing use](#description-of-existing-use)
* [Grounds for lawful development certificate](#grounds-for-lawful-development-certificate)
* [Information to support LDC](#information-to-support-ldc)
* [Interest details](#interest-details)
* [Pre-application advice](#pre-application-advice)
* [Residential units](#residential-units)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)
* [Use works activity](#use-works-activity)

### Codelists

* [Housing type](#housing-type)
* [Tenure type](#tenure-type)
* [Use class](#use-class)

## Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees

**Application fields module**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum
application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-subtype** enum
planning-authority | Planning authority | A reference of the planning authority the application has been submitted to, e.g. local-authority:CMD for London borough of Camden | MUST | Select from the **planning-authority** enum. Currently built by combining local-authority, development-corporation and national-park-authority datasets from planning.data.gov.uk
submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format | MUST | 
modules | Modules[] | List of required modules for this application that can be used to validate the application | MUST | 
documents | Documents[]{} | List of submitted documents with references and details | MUST | 
fee | Fee{} | The fee payable for the application including amounts and transaction details | MAY | 


**Document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | The name or title of the document | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**Fee component**

field | name | description | required | notes
-- | -- | -- | -- | --
amount | Amount | The total amount due for the application fee | MUST | 
amount-paid | Amount paid | The amount paid towards the application fee | MUST | 
transactions | Transactions[] | References to payments or financial transactions related to this application | MAY | 


**File component**

field | name | description | required | notes
-- | -- | -- | -- | --
url | URL | A URL pointing to the stored file | MAY | 
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded | MUST | 
mime-type | MIME type | The file's MIME type such as application/pdf or image/jpeg | MAY | 
checksum | Checksum | Hash of the file contents used for file validation and checking files have not been tampered with | MAY | 
file-size | File size | Size of the file in bytes that can be used to enforce limits | MAY | 

**Validation rules**

- reference must be a valid UUID format
- application-types must reference valid application type codelist values
- application-sub-type must reference valid application sub-type codelist values
- planning-authority must be a valid organisation reference
- modules must reference existing module definitions
- document references must be unique within the application
- file must contain either url or base64, but not both
- document-types must reference valid planning requirement codelist values

## Agent contact details

Name and contact information if an agent is being used.

**Agent contact details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| agent-reference | Agent reference | A reference to an agent object | MUST |  |
| contact-details | Contact details{} | A structured object containing contact information for an individual. This component is required for planning in principle (PiP) applications and optional for other application types. Contains email and phone contact information. | MUST |  |


**Contact details component**

field | name | description | required | notes
-- | -- | -- | -- | --
email | Email | The email address that can be used for electronic correspondence with the individual | MUST | 
phone-numbers | Phone number(s)[]{} | One or more telephone numbers to contact individual | MUST | 


**Phone number component**

field | name | description | required | notes
-- | -- | -- | -- | --
number | Phone number | A phone number | MAY | 
contact-priority | Contact priority | The priority of a number | MAY | Select from the **contact-priority** enum



## Agent details

Name and contact information if an agent is being used.

**Agent details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| agent | agent{} | Details of the agent | MAY |  |


**Agent obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
person | Person{} | Detail to help identify a person | MUST | 
company | Company | The name of a company (that the agent works for) | MAY | 
user-role | User role | The role of the named individual. Agent or proxy | MAY | Select from the **user-role-type** enum


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 



## Applicant contact details

Telephone number and email address of the applicant.

**Applicant contact details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| applicant-reference | Applicant reference | Reference to match contact details to a named individual from the applicant details component | MUST |  |
| contact-details | Contact details{} | A structured object containing contact information for an individual. This component is required for planning in principle (PiP) applications and optional for other application types. Contains email and phone contact information. | MUST |  |


**Contact details component**

field | name | description | required | notes
-- | -- | -- | -- | --
email | Email | The email address that can be used for electronic correspondence with the individual | MUST | 
phone-numbers | Phone number(s)[]{} | One or more telephone numbers to contact individual | MUST | 


**Phone number component**

field | name | description | required | notes
-- | -- | -- | -- | --
number | Phone number | A phone number | MAY | 
contact-priority | Contact priority | The priority of a number | MAY | Select from the **contact-priority** enum

**Validation rules**

- applicant-reference must match a reference from the applicant details component
- At least one phone number must have contact-priority set to primary

## Applicant details

Name and contact information for the parties making the application.

**Applicant details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| applicants | Applicants[]{} |  | MUST |  |


**Applicant component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
person | Person{} | Detail to help identify a person | MUST | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 

**Validation rules**

- At least one applicant must be provided
- Each applicant reference must be unique within the application

## Checklist

Checking whether all the requirements of the form have been met, such as proof of payment or supporting documentation.

**Checklist module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| national-req-types | National requirement types[] | List of the document types required for the given application type | MUST |  |

**Validation rules**

- All values must be from the national-requirement-type codelist
- Values must be valid for the current application type

## Conflict of interest

Details of any conflict of interest that may exist between the applicant and planning authority.

**Conflict of interest module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |

**Validation rules**

- conflict-person-name must match a name provided in applicants or agent sections

## Declaration

Signed and dated verification of the application's accuracy.

**Declaration module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| name | Name | A name of a person | MUST |  |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | MUST |  |
| declaration-date | Declaration date | The date the declaration was made | MUST |  |

**Validation rules**

- name must match one of the named individuals in the application
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future

## Description of existing use

How the development site is used, including use class information

**Description of existing use module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| existing-use-details | Existing use details[]{} | List of existing site uses and related land areas | MUST |  |


**Existing use detail component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-details | Use details | Further detail of the use | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`
land-part | Land part | Which part of the land the use relates to | MUST | 

**Validation rules**

- existing-use-details must contain at least one item
- if use == 'sui' OR use == 'other' then use-details is required

## Grounds for lawful development certificate

Evidence and explanations relating to a Lawful Development Certificate (LDC) application

**Grounds for lawful development certificate module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| grounds-pre-2024 | Grounds pre 2024[] | List of grounds pre 2024-04-25 under which the certificate is sought | MAY | Select from the **grounds-ldc-pre-apr-2024** enum |
| grounds-post-2024 | Grounds post 2024[] | List of grounds post 2024-04-25 under which the certificate is sought | MAY | Select from the **grounds-ldc-post-apr-2024** enum |
| other-details | Other details | Explanation if other ground is selected | MAY |  |
| supporting-applications | Supporting applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site | MAY |  |
| reason | Reason | A textual reason | MUST |  |


**Supporting applications component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference-number | Reference number | Reference number of the planning permission | MAY | 
condition-number | Condition number | Number of any condition being breached | MAY | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- grounds-pre-2024 is not empty OR grounds-post-2024 is not empty
- if grounds-pre-2024 contains 'other' OR grounds-post-2024 contains 'other' then other-details is required

## Information to support LDC

Supporting information required to make a Lawful Development Certificate application

**Information to support LDC module**

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

## Interest details

Names and contact details for all parties with an interest in the proposed develpoment.

**Interest details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| applicant-interest | Applicant interest | Description of the applicant's interest in the land | MUST |  |
| owner-details | Owner details[]{} | Details of property owners including their personal information and notification status | MAY |  |
| interested-persons | Interested persons[]{} | Details of persons with an interest in the property including their personal information, nature of interest, and notification status | MAY | Rule: is a MUST if `applicant-interest` is `none` |


**LDC Owner Details component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the property owner | MUST | 
informed-of-application | Informed of application | Whether the owner has been informed of the application | MUST | 


**LDC Interested Person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the interested person | MUST | 
nature-of-interest | Nature of interest | Description of the nature of a person's interest in the property | MUST | 
informed-of-application | Informed of application | Whether the person has been informed of the application | MUST | 
reason-not-informed | Reason not informed | Reason why a person was not informed of the application | MAY | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 

**Validation rules**

- if applicant-interest is 'lessee' or 'occupier', then owner-details is required
- if applicant-interest is 'none', then interested-persons is required
- if applicant-owns-land is false, then permission-obtained is required
- if applicant-owns-land is false and permission-obtained is false, then permission-not-obtained-details is required

## Pre-application advice

Details of pre-application advice previously received from the planning authority

**Pre-application advice module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Residential units

Details of the residential units that make up both the current and proposed development.

**Residential units module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| will-residential-units-change | Residential unit change | Proposal includes the gain, loss or change of use of residential units | MUST |  |
| residential-unit-summary | Residential unit summary[]{} | Breakdown of unit counts by tenure and housing type | MAY | Rule: is a MUST if `will-residential-units-change` is `True` |
| total-existing-units | Total existing units | The total number of existing units | MUST |  |
| total-proposed-units | Total proposed units | The total number of proposed units | MUST |  |
| net-change | Net change | Calculated net change in units | MUST |  |


**Residential unit summary component**

field | name | description | required | notes
-- | -- | -- | -- | --
tenure-type | Tenure type | Category of housing tenure | MUST | Select from the **tenure-type** enum
housing-type | Housing type | Type of housing | MUST | Select from the **housing-type** enum
existing-unit-breakdown | Existing unit breakdown[]{} | Number of existing units by bedroom count | MAY | 
proposed-unit-breakdown | Proposed unit breakdown[]{} | Number of proposed units by bedroom count | MAY | 


**Unit quantities component**

field | name | description | required | notes
-- | -- | -- | -- | --
units-unknown | Units unknown | Whether the number of units is unknown | MUST | 
units-per-bedroom-no | Units per bedroom number[]{} | Number of units broken down by bedroom count | MAY | Rule: is a MUST if `units-unknown` is `False`
total-units | Total units | Total number of units | MAY | 


**Bedroom count component**

field | name | description | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | No bedrooms unknown | Set to true when counting units where bedroom number is unknown | MUST | 
no-of-bedrooms | Number of bedrooms | The number of bedrooms in unit | MAY | Rule: is a MUST if `no-bedrooms-unknown` is `False`
units | Units | The number of units of that bedroom count | MUST | 

**Validation rules**

- residential-unit-summary is required when will-residential-units-change is true
- net-change is calculated as total-proposed-units minus total-existing-units
- if will-residential-units-change is true, at least one breakdown for existing and proposed is required (count could be unknown)

## Site details

Where the proposed development will be built.

**Site details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| site-locations | Site locations[]{} | Details of the sites where development or works are proposed | MUST |  |


**Site location component**

field | name | description | required | notes
-- | -- | -- | -- | --
site-boundary | Site boundary | Geometry of the site of the development, typically in GeoJSON format | MAY | 
address-text | Address Text | Flexible field for capturing addresses | MAY | 
postcode | Postcode | The postal code | MAY | 
easting | Easting | Easting coordinate in British National Grid (EPSG:27700) | MAY | 
northing | Northing | Northing coordinate in British National Grid (EPSG:27700) | MAY | 
latitude | Latitude | Latitude coordinate in WGS84 (EPSG:4326) | MAY | 
longitude | Longitude | Longitude coordinate in WGS84 (EPSG:4326) | MAY | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MAY | 
uprns | UPRNs[] | Unique Property Reference Numbers (UPRNs) for properties within the site boundary | MAY | 

**Validation rules**

- {'description': 'At least one site-location must be provided for tree works applications', 'field': 'site-locations', 'require': {'min': 1}, 'type': 'count-constraint', 'when': {'application-type': {'in': ['tree-works']}}}
- {'description': 'Exactly one site-location for all other applications types', 'field': 'site-locations', 'require': {'exact': 1}, 'type': 'count-constraint', 'when': {'application-type': {'not': ['tree-works']}}}
- If easting is provided, northing must also be provided and vice versa
- If latitude is provided, longitude must also be provided and vice versa
- Site boundary must be valid GeoJSON
- UPRNs must be valid format
- Post code must be valid UK format

## Site Visit Details

Information to help the planning authority arrange a site visit

**Site Visit Details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| can-be-seen-from | Site seen from public area | Can site be seen from a public road, public footpath, bridleway or other public land | MUST |  |
| contact-type | Site visit contact type | Indicates who the authority should contact to arrange a site visit | MUST | Select from the **site-visit-contact-type** enum |
| contact-reference | Contact reference | The reference of the applicant or agent who should be contacted for site visits | MAY |  |
| other-contact | Other site visit contact{} | Details of specifically named contact for site visits | MAY | Rule: is a MUST if `contact-type` is `other` |


**Other contact component**

field | name | description | required | notes
-- | -- | -- | -- | --
fullname | Full name | The complete name of a person | MUST | 
number | Phone number | A phone number | MUST | 
email | Email | The email address that can be used for electronic correspondence with the individual | MUST | 

**Validation rules**

- contact-reference must match agent-details.agent.reference details if contact-type is agent
- contact-reference must match one of the references in applicant-details.applicants if contact-type is applicant
- When contact-type is other, full contact details must be provided

## Use works activity

Why a Lawful Development Certificate is required regarding how the development site is being used, or specific works taking place on the site.

**Use works activity module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| ldc-need | LDC need[] | What is the lawful development certificate needed for? | MUST | Select from the **lawful-dev-cert-need** enum. At least one value must be provided |
| use | Use | A use class or type of use | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY |  |

**Validation rules**

- At least one ldc-need value must be provided
- use is required when ldc-need contains existing-use or breach-con-existing-use
- specified-use is required when use is sui or other

## Required codelists

Below are the codelists required to support this specification:

### Housing type

| reference | name | description |
| --- | --- | --- |
| houses | Houses | Detached |
| flats-maisonettes | Flats/Maisonettes | Self-contained apartments or maisonettes. |
| sheltered-housing | Sheltered Housing | Housing with support for older or disabled people. |
| bedsit-studio | Bedsit/Studio | Single-room living spaces. |
| cluster-flats | Cluster Flats | Flats with shared communal areas. |
| other | Other | Any other housing type not listed. |
| live-work-units | Live-Work Units | Properties combining residential and workspace. |
| unknown | Unknown | When the type of housing is uncertain. |

### Tenure type

| reference | name | description | application-types |
| --- | --- | --- | --- |
| market-housing | Market Housing | Private housing for sale or rent. | ldc;full;outline |
| social-rented | Social Rented Housing | Public/social housing at below-market rents. | ldc |
| intermediate-housing | Intermediate Housing | Housing with rents or ownership costs between social housing and market housing. | ldc |
| key-worker-housing | Key Worker Housing | Housing for essential workers (e.g. teachers |  NHS staff). |
| affordable-rent | Social |  Affordable |  or Intermediate Rent |
| home-ownership | Affordable Home Ownership | Shared ownership or similar schemes. | full;outline |
| starter-homes | Starter Homes | Discounted homes for first-time buyers. | full;outline |
| custom-build | Self-Build and Custom Build | Homes built or commissioned by individuals. | full;outline |

### Use class

| reference | name | description | notes | entry-date | start-date | end-date |
| --- | --- | --- | --- | --- | --- | --- |
| b2 | B2 – General Industrial | Industrial uses not falling within Class E. |  | 2025-10-27 |  |  |
| b8 | B8 – Storage and Distribution | Warehousing and storage. |  | 2025-10-27 |  |  |
| c1 | C1 – Hotels | Includes hotels, boarding houses, and guest houses. |  | 2025-10-27 |  |  |
| c2 | C2 – Residential Institutions | Care homes, hospitals, and boarding schools. |  | 2025-10-27 |  |  |
| c2a | C2A – Secure Residential Institutions | Prisons, young offender institutions. |  | 2025-10-27 |  |  |
| c3 | C3 – Dwellinghouses | Sole or main residence used by people forming a single household. |  | 2025-10-27 |  |  |
| c4 | C4 – Houses in multiple occupation | Defined in the Housing Act 2004 (with the exclusion of converted block of flats). |  | 2025-10-27 |  |  |
| e-a | E(a) – Retail (other than hot food) | Shops and other retail services. |  | 2025-10-27 |  |  |
| e-b | E(b) – Food and Drink | Premises mostly for on-site consumption. |  | 2025-10-27 |  |  |
| e-c-i | E(c)(i) – Financial Services | Banks, building societies, and credit unions. |  | 2025-10-27 |  |  |
| e-c-ii | E(c)(ii) – Professional Services | Non-health/medical services (e.g., accountants, solicitors). |  | 2025-10-27 |  |  |
| e-c-iii | E(c)(iii) – Any Other Service | Non-retail services to the public. |  | 2025-10-27 |  |  |
| e-d | E(d) – Indoor Sports and Recreation | Excludes motorised or firearms activities. |  | 2025-10-27 |  |  |
| e-e | E(e) – Medical or Health Services | Clinics and health centres. |  | 2025-10-27 |  |  |
| e-f | E(f) – Creche, Day Nursery | Facilities for childcare. |  | 2025-10-27 |  |  |
| e-g-i | E(g)(i) – Office | For operational or administrative functions. |  | 2025-10-27 |  |  |
| e-g-ii | E(g)(ii) – Research and Development | Development of products or processes. |  | 2025-10-27 |  |  |
| e-g-iii | E(g)(iii) – Industrial Process | Processes that can operate within a residential area. |  | 2025-10-27 |  |  |
| f1-a | F1(a) – Education | Schools, colleges, and training centres. |  | 2025-10-27 |  |  |
| f1-b | F1(b) – Display of Works of Art | Galleries (excluding commercial galleries). |  | 2025-10-27 |  |  |
| f1-c | F1(c) – Museum | Non-commercial museums. |  | 2025-10-27 |  |  |
| f1-d | F1(d) – Public Library | Libraries open to the public. |  | 2025-10-27 |  |  |
| f1-e | F1(e) – Public Hall/Exhibition Hall | Community spaces for events. |  | 2025-10-27 |  |  |
| f1-f | F1(f) – Public Worship/Religious Instruction | Churches, mosques, synagogues. |  | 2025-10-27 |  |  |
| f1-g | F1(g) – Law Court | Court facilities. |  | 2025-10-27 |  |  |
| f2-a | F2(a) – Local Community Shop | Shop under 280 sqm with no similar facility nearby. |  | 2025-10-27 |  |  |
| f2-b | F2(b) – Community Hall | Halls for local community use. |  | 2025-10-27 |  |  |
| f2-c | F2(c) – Outdoor Sport/Recreation | Excludes motorised sports. |  | 2025-10-27 |  |  |
| f2-d | F2(d) – Indoor/Outdoor Swimming Pool | Includes skating rinks. |  | 2025-10-27 |  |  |
| sui | Sui generis | Uses that do not fall within any defined use class and are considered unique. For example, theatres, nightclubs, scrap yards and mineral extraction |  | 2025-10-27 |  |  |
| other | Other (Please Specify) | Free text required if selected. |  | 2025-10-27 |  |  |
