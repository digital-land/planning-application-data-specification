# Permission in principle

An alternative way of getting planning permission for housing-led development which separates the consideration of matters of principle from the technical detail of the development

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
* [Description of the proposed development including any non-residential development](#description-of-the-proposed-development-including-any-non-residential-development)
* [Site details](#site-details)
* [Site information](#site-information)

### Codelists

* [Contact priority](#contact-priority)
* [Non-residential measurement type](#non-residential-measurement-type)
* [Provided by](#provided-by)
* [User role type](#user-role-type)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


**Application fields module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-sub-type** enum |
| planning-authority | Planning authority | The reference of the planning authority the application has been submitted to, e.g. local-authority:CMD | MUST |  |
| submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format | MUST |  |
| modules | Modules[] | List of required modules for this application that can be used to validate the application | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MUST |  |
| fee | Fee{} | The fee payable for the application including amounts and transaction details | MAY |  |


**Document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | A name of a person | MUST | 
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

Contact details of the agent acting on behalf of the applicant


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

Details of the agent acting on behalf of the applicant


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

Contact details for the applicant or applicants, including email and phone numbers


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

Details about the applicants for the planning application,
including their personal information and contact details


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

Identifies the national requirement types that apply to this application type


**Checklist module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| national-req-types | National requirement types[] | List of the document types required for the given application type | MUST |  |

**Validation rules**

- All values must be from the national-requirement-type codelist
- Values must be valid for the current application type

## Conflict of interest

Information about any conflicts of interest between the applicant/agent and the planning authority,
including relationships with staff or elected members


**Conflict of interest module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Conflict to declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared | MUST |  |
| conflict-person-name | Conflict person name | Name of the individual with the conflict of interest that matches one of the names provided in applicants/agent section | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |
| conflict-details | Conflict details | Details of the conflict of interest including name, role and how the individual is related to the planning authority | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |

**Validation rules**

- conflict-person-name must match a name provided in applicants or agent sections

## Declaration

Declaration by the applicant or agent confirming the accuracy of the information provided


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

## Description of the proposed development including any non-residential development

Details of proposed development with specific provision for capturing both residential 
and non-residential elements, including dwelling numbers and non-residential use amounts


**Description of the proposed development including any non-residential development module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| description | Description | Description of proposed development including non-residential development | MUST |  |
| net-dwellings-min | Net dwellings minimum | The minimum number of net additional dwellings proposed as part of the development, accounting for any existing dwellings lost and new dwellings created | MUST |  |
| net-dwellings-max | Net dwellings maximum | The maximum number of net additional dwellings proposed as part of the development, allowing for flexibility in the final housing numbers | MUST |  |
| non-residential-use | Non-residential use[]{} | The amount of non-residential use, which can be expressed as floorspace, site area, or both | MUST |  |


**Non-residential use component**

field | name | description | required | notes
-- | -- | -- | -- | --
non-residential-measurement-type | Non-residential measurement type | Type of measurement being provided (floorspace or site-area) | MUST | Select from the **non-residential-measurement-type** enum
exact-value | Exact value | Exact figure of non-residential use | MAY | 
min | Minimum value | Lower bound of non-residential use for ranges | MAY | 
max | Maximum value | Upper bound of non-residential use for ranges | MAY | 

**Validation rules**

- net-dwellings-max must be greater than or equal to net-dwellings-min
- Each non-residential-use entry must have either exact-value OR both min and max values
- For non-residential-use ranges, max must be greater than min
- non-residential-measurement-type must be from the non-res-measurement-type codelist

## Site details

Information about the location and extent of the site where development 
or works are proposed


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

- {'description': 'At least one site-location must be provided for tree works applications', 'type': 'count-constraint', 'field': 'site-locations', 'when': {'application-type': {'in': ['tree-works']}}, 'require': {'min': 1}}
- {'description': 'Exactly one site-location for all other applications types', 'type': 'count-constraint', 'field': 'site-locations', 'when': {'application-type': {'not': ['tree-works']}}, 'require': {'exact': 1}}
- If easting is provided, northing must also be provided and vice versa
- If latitude is provided, longitude must also be provided and vice versa
- Site boundary must be valid GeoJSON
- UPRNs must be valid format
- Post code must be valid UK format

## Site information

Additional information about the development site including area, 
existing use, constraints, and supporting documentation


**Site information module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| site-area | Site area{} | The total area of the site where development is proposed | MUST |  |
| existing-use | Existing use[]{} | Structured information on the current use of the site | MUST |  |
| known-constraints | Known constraints[] | A list of the known constraints affecting the site | MUST | Select from the **site-constraint** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY |  |


**Site area component**

field | name | description | required | notes
-- | -- | -- | -- | --
value | Value | Numeric value representing a measurement or quantity | MUST | 
unit | Unit | Unit of measurement for a value | MUST | 
provided-by | Provided by | Whether the information was provided by the applicant or calculated by the system | MAY | Select from the **provided-by** enum


**Existing use component**

field | name | description | required | notes
-- | -- | -- | -- | --
uses | Uses[]{} | List of applicable uses for a site or development | MUST | 
floorspace | Floorspace | Total floorspace for a use in square metres | MUST | 


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 


**Use component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`

**Validation rules**

- supporting-documents is required if known-constraints is not empty
- site-area value should ideally be calculated from site boundary
- site-area unit must be one of: m2, hectares
- provided-by must be one of: Applicant, System/Service
- use must reference valid use class or be 'other' or 'sui'
- specified-use is required if use is 'sui' or 'other'
- floorspace must be numeric value in m2

## Required codelists

Below are the codelists required to support this specification:

### Contact priority

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

### Non-residential measurement type

Source file not found: data/codelist/non-residential-measurement-type.csv

### Provided by

| reference | name | description |
| --- | --- | --- |
| applicant | Applicant | Information provided by the applicant |
| system | System/Service | Information calculated or determined by the system or external service |

### User role type

| reference | name | description |
| --- | --- | --- |
| agent | Agent | A professional agent working for the applicant |
| proxy | Proxy | An individual working on behalf of the applicant but not in a professional capacity |
