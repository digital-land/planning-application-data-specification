# Larger Home Extension

Planning application for extension

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Adjacent premises](#adjacent-premises)
* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Checklist](#checklist)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Description of proposed works](#description-of-proposed-works)
* [Eligibility extension](#eligibility-extension)
* [Site details](#site-details)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-sub-type** enum |
| planning-authority | Planning authority | The reference of the planning authority the application has been submitted to, e.g. local-authority:CMD | MUST |  |
| submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format | MUST |  |
| modules | Modules[] | List of required modules for this application that can be used to validate the application | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MUST |  |
| fee | Fee{} | The fee payable for the application including amounts and transaction details | MAY |  |


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | A name of a person | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**Fee model**

field | name | description | required | notes
-- | -- | -- | -- | --
amount | Amount | The total amount due for the application fee | MUST | 
amount-paid | Amount paid | The amount paid towards the application fee | MUST | 
transactions | Transactions[] | References to payments or financial transactions related to this application | MAY | 


**File model**

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

## Adjacent premises

Information about addresses of properties adjacent to the development site


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for the adjoining properties | MUST |  |


**Address model**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 
uprn | UPRN | Unique Property Reference Number | MAY | 

**Validation rules**

- At least one address must be provided
- Each address must have address-text as minimum requirement
- UPRN should be provided where known for accurate property identification

## Agent contact details

Contact details of the agent acting on behalf of the applicant


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| agent-reference | Agent reference | A reference to an agent object | MUST |  |
| contact-details | Contact details{} | A structured object containing contact information for an individual. This component is required for planning in principle (PiP) applications and optional for other application types. Contains email and phone contact information. | MUST |  |


**Contact details model**

field | name | description | required | notes
-- | -- | -- | -- | --
email | Email | The email address that can be used for electronic correspondence with the individual | MUST | 
phone-numbers | Phone number(s)[]{} | One or more telephone numbers to contact individual | MUST | 


**Phone number model**

field | name | description | required | notes
-- | -- | -- | -- | --
number | Phone number | A phone number | MAY | 
contact-priority | Contact priority | The priority of a number | MAY | Select from the **contact-priority** enum



## Agent details

Details of the agent acting on behalf of the applicant


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| agent | agent{} | Details of the agent | MAY |  |


**Agent obj model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
person | Person{} | Detail to help identify a person | MUST | 
company | Company | The name of a company (that the agent works for) | MAY | 
user-role | User role | The role of the named individual. Agent or proxy | MAY | Select from the **user-role-type** enum


**Person obj model**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 



## Applicant contact details

Contact details for the applicant or applicants, including email and phone numbers


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-reference | Applicant reference | Reference to match contact details to a named individual from the applicant details component | MUST |  |
| contact-details | Contact details{} | A structured object containing contact information for an individual. This component is required for planning in principle (PiP) applications and optional for other application types. Contains email and phone contact information. | MUST |  |


**Contact details model**

field | name | description | required | notes
-- | -- | -- | -- | --
email | Email | The email address that can be used for electronic correspondence with the individual | MUST | 
phone-numbers | Phone number(s)[]{} | One or more telephone numbers to contact individual | MUST | 


**Phone number model**

field | name | description | required | notes
-- | -- | -- | -- | --
number | Phone number | A phone number | MAY | 
contact-priority | Contact priority | The priority of a number | MAY | Select from the **contact-priority** enum

**Validation rules**

- applicant-reference must match a reference from the applicant details component
- At least one phone number must have contact-priority set to primary

## Applicant details

Details about the applicants for the planning application,
including their personal information and contact details


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicants | Applicants[]{} |  | MUST |  |


**Applicant model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
person | Person{} | Detail to help identify a person | MUST | 


**Person obj model**

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

Identifies the national requirement types that apply to this application type


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| national-req-types | National requirement types[] | List of the document types required for the given application type | MUST |  |

**Validation rules**

- All values must be from the national-requirement-type codelist
- Values must be valid for the current application type

## Conflict of interest

Information about any conflicts of interest between the applicant/agent and the planning authority,
including relationships with staff or elected members


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |

**Validation rules**

- conflict-person-name must match a name provided in applicants or agent sections

## Declaration

Declaration by the applicant or agent confirming the accuracy of the information provided


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| name | Name | A name of a person | MUST |  |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | MUST |  |
| declaration-date | Declaration date | The date the declaration was made | MUST |  |

**Validation rules**

- name must match one of the named individuals in the application
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future

## Description of proposed works

Description of proposed development works including extension measurements
and detailed work specifications for planning applications


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposed-works-details | Proposed works details | Description of the proposed works including detailed explanation of the work | MUST |  |
| extension-depth | Extension depth | How far the extension extends beyond the rear wall, measured externally in metres | MUST |  |
| max-extension-height | Maximum extension height | Maximum height of the extension, measured externally from natural ground level in metres | MUST |  |
| eaves-height | Eaves height | Height at the eaves of the extension, measured externally from natural ground level in metres | MUST |  |

**Validation rules**

- extension-depth > 0 AND max-extension-height > 0 AND eaves-height > 0
- eaves-height <= max-extension-height
- extension-depth measurement taken from external face of existing rear wall
- max-extension-height and eaves-height measured from natural ground level
- proposed-works-details.length > 10

## Eligibility extension

Eligibility criteria for extension applications to determine if the proposal
meets the requirements for the application type


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-single-storey-extension | Single storey extension | Will the extension be a single storey | MUST |  |
| is-extension-height-over-4m | Extension height over 4m | Will the extension exceed 4 metres in height | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached | MUST |  |
| is-extension-beyond-rear-wall | Extension beyond rear wall | Will the extension extend beyond the rear wall of the original dwelling | MUST |  |
| extension-length | Extension length | Length of rear extension in metres | MUST |  |
| is-within-site-constraints | Within site constraints | Is the dwellinghouse within any restricted area | MUST |  |
| site-constraints | Site constraints[] | List of specific site constraints that restrict development | MAY | Select from the **designation** enum |

**Validation rules**

- if is-single-storey-extension == false then application is ineligible
- if is-extension-height-over-4m == true then application is ineligible
- if is-within-site-constraints == true then application is ineligible
- if is-within-site-constraints == true then site-constraints is required
- extension-length must comply with permitted development limits based on is-dwelling-detached value

## Site details

Information about the location and extent of the site where development 
or works are proposed


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-locations | Site locations[]{} | Details of the sites where development or works are proposed | MUST |  |


**Site location model**

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

- At least one site-location must be provided for tree works applications
- Exactly one site-location for all other applications types
- If easting is provided, northing must also be provided and vice versa
- If latitude is provided, longitude must also be provided and vice versa
- Site boundary must be valid GeoJSON
- UPRNs must be valid format
- Post code must be valid UK format
