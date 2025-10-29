# Advertising

An application for all types of advertisements and signs

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Advertisement location](#advertisement-location)
* [Advert period](#advert-period)
* [Advertisement types](#advertisement-types)
* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Checklist](#checklist)
* [Community consultation](#community-consultation)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Interest details](#interest-details)
* [Pre-application advice](#pre-application-advice)
* [Proposed advert details](#proposed-advert-details)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)

### Codelists

* [Advertisement type](#advertisement-type)
* [Contact priority](#contact-priority)
* [Illumination type](#illumination-type)
* [User role type](#user-role-type)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


**Application fields module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-subtype** enum |
| planning-authority | Planning authority | The reference of the planning authority the application has been submitted to, e.g. local-authority:CMD | MUST |  |
| submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format | MUST |  |
| modules | Modules[] | List of required modules for this application that can be used to validate the application | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MUST |  |
| fee | Fee{} | The fee payable for the application including amounts and transaction details | MAY |  |


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

## Advertisement location

Where the advertisement being applied to be built will be located

**Advertisement location module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-advert-in-place | Is advert in place | Whether the advertisement is already in place | MUST |  |
| advert-placed-date | Advert placed date | Date when the advertisement was placed (YYYY-MM-DD format) | MAY | Rule: is a MUST if `is-advert-in-place` is `True` |
| is-replacement-advert | Is replacement advert | Whether this is a replacement advertisement | MUST |  |
| document-reference | Document reference[]{} | References to documents detailing the proposed alterations | MAY | Rule: is a MUST if `is-advert-in-place` is `True`. Rule: is a MUST if `is-replacement-advert` is `True` |
| is-advert-overhanging | Is advert overhanging | Whether the advertisement will project over a footpath or other public highway | MUST |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 

**Validation rules**

- if is-advert-in-place == true then advert-placed-date is required
- if (is-advert-in-place == true OR is-replacement-advert == true) then document-reference is required

## Advert period

How long the proposed advertisement will be shown.

**Advert period module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advert-start-date | Advert start date | The start of the time period that consent to advertisement is sought | MUST |  |
| advert-end-date | Advert end date | The end of the time period that consent to advertisement is sought | MUST |  |

**Validation rules**

- advert-start-date must be a valid date in YYYY-MM-DD format
- advert-end-date must be a valid date in YYYY-MM-DD format
- advert-end-date must be after advert-start-date

## Advertisement types

What type of advertisements are proposed and how many there will be.

**Advertisement types module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advertisement-proposal-description | Advertisement proposal description | Description of the advertisement proposal | MUST |  |
| advertisement-proposal-type | Advertisement proposal type[]{} | Expected to provide counts for each advertisement type | MUST |  |


**Advertisement proposal type component**

field | name | description | required | notes
-- | -- | -- | -- | --
advertisement-type | Advertisement type | One of the advertisement-types or other | MUST | Select from the **advertisement-type** enum
advertisement-count | Advertisement count | Number of this type of advertisement | MUST | 
advertisement-other-description | Advertisement other description | Details required if other advertisement type is selected | MAY | Rule: is a MUST if `advertisement-type` is `other`

**Validation rules**

- At least one advertisement-proposal-type entry must be provided
- advertisement-other-description is required when advertisement-type is 'other'
- advertisement-count must be a positive integer

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

## Community consultation

What community consultation activities have taken place as part of the application

**Community consultation module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| have-consulted | Have consulted | Whether community consultation has been carried out | MUST |  |
| description | Description | Provide details of the community consultation | MAY | Rule: is a MUST if `have-consulted` is `True` |

**Validation rules**

- Description is required when have-consulted is true
- Description should provide details of the consultation activities undertaken

## Conflict of interest

Details of any conflict of interest that may exist between the applicant and planning authority.

**Conflict of interest module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Conflict to declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared | MUST |  |
| conflict-person-name | Conflict person name | Name of the individual with the conflict of interest that matches one of the names provided in applicants/agent section | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |
| conflict-details | Conflict details | Details of the conflict of interest including name, role and how the individual is related to the planning authority | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |

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

## Interest details

Names and contact details for all parties with an interest in the proposed develpoment.

**Interest details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| applicant-interest | Applicant interest | Description of the applicant's interest in the land | MUST |  |
| owner-details | Owner details[]{} | Details of property owners including their personal information and notification status | MAY |  |
| interested-persons | Interested persons[]{} | Details of persons with an interest in the property including their personal information, nature of interest, and notification status | MAY | Rule: is a MUST if `applicant-interest` is `none` |
| applicant-owns-land | Applicant owns land | True or False indicating whether the applicant owns the land where the advertisement will be displayed | MUST |  |
| permission-obtained | Permission obtained | True or False indicating whether permission of the owner for the display of an advertisement has been obtained | MAY | Rule: is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Permission not obtained details | Details explaining why permission from the land owner has not been obtained for the advertisement display | MAY |  |


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
- No advertisement to be displayed without permission of owner or person with interest entitled to grant permission

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



## Proposed advert details

Details of the proposed advertisements such as their size and how they are made

**Proposed advert details module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advertisements | Advertisements[]{} | Structured data about each proposed advertisement | MUST |  |


**Advertisement component**

field | name | description | required | notes
-- | -- | -- | -- | --
height-from-ground | Height from ground | Height, in metres, from ground to the base of the advertisement | MAY | in metres
height | Height | Height, in metres, of dimensions of advertisement | MAY | in metres
width | Width | Width of dimensions of advertisement | MAY | in metres
depth | Depth | Depth, in metres, of dimensions of advertisement | MAY | in metres
symbol-height-max | Symbol height max | Maximum height, in metres, of any individual letters or symbols | MAY | 
colour | Colour | Colour of proposed sign | MAY | 
materials | Materials | Materials of proposed sign | MAY | 
max-projection | Max projection | Maximum projection, in metres, of the advertisement from the face of the building | MAY | 
illuminated | Illuminated | Will the sign(s) be illuminated? | MAY | 
illumination-method | Illumination method | Method of illumination for the advertisement | MAY | Rule: is a MUST if `illuminated` is `True`
illuminance-level | Illuminance level | Level of illuminance for the advertisement | MAY | Rule: is a MUST if `illuminated` is `True`. Unit: cd/m2
illumination-type | Illumination type | Type of illumination (static or intermittent) | MAY | Select from the **illumination-type** enum. Rule: is a MUST if `illuminated` is `True`

**Validation rules**

- At least one advertisement entry must be provided
- illumination-method is required when illuminated is true
- illuminance-level is required when illuminated is true
- illumination-type is required when illuminated is true
- Dimensional values must be positive numbers
- illuminance-level must be positive when provided

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

## Required codelists

Below are the codelists required to support this specification:

### Advertisement type

| reference | name | description |
| --- | --- | --- |
| fascia | Fascia |  |
| projecting-hanging | Projecting or hanging sign |  |
| hoarding | Hoarding |  |
| other | Other |  |

### Contact priority

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

### Illumination type

| reference | name | description |
| --- | --- | --- |
| static | Static | Illumination is constant and does not change or flash. |
| intermittent | Intermittent | Illumination switches on and off or flashes at intervals. |

### User role type

| reference | name | description |
| --- | --- | --- |
| agent | Agent | A professional agent working for the applicant |
| proxy | Proxy | An individual working on behalf of the applicant but not in a professional capacity |
