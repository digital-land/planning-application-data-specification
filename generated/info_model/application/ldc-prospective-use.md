# LDC Proposed Use

Prospective use of the site

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
* [Grounds for application (information about the existing use(s))](#grounds-for-application-(information-about-the-existing-use(s)))
* [Grounds for proposed use](#grounds-for-proposed-use)
* [Interest details](#interest-details)
* [Pre-application advice](#pre-application-advice)
* [Proposal details LDC](#proposal-details-ldc)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)

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

## Grounds for application (information about the existing use(s))

Information about the existing or last use of the site to support 
a lawful development certificate application, including lawful justification,
use classification, and supporting documentary evidence


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| use-lawful-reason | Use lawful reason | Explanation of why the existing or last use is considered lawful, 
providing justification for a lawful development certificate application
 | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MAY |  |
| use | Use | A use class or type of use | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other` |


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | A name of a person | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


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

- use-lawful-reason.length > 0
- use IN ['sui', 'other'] REQUIRES specified-use.length > 0
- documents[].reference.length > 0 AND documents[].name.length > 0
- documents[].reference should be unique across application.documents[]

## Grounds for proposed use

Information about the proposed use class, operation type, and supporting reasoning for lawful development certificate applications


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| use | Use | State proposed use class | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY |  |
| operation-type | Operation type | Whether the proposed use is temporary or permanent | MUST | Select from the **operation-type** enum |
| temporary-details | Temporary details | Details of temporary use including duration and specific arrangements | MAY |  |
| reason | Reason | A textual reason | MUST |  |

**Validation rules**

- specified-use is required if use is 'sui' or 'other'
- temporary-details is required if operation-type is 'temporary'

## Interest details

Details of the applicant's interest in land or listed buildings and information about
other interested parties including owners and persons with interests in the property


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-interest | Applicant interest | Description of the applicant's interest in the land | MUST |  |
| owner-details | Owner details[]{} | Details of property owners including their personal information and notification status | MAY |  |
| interested-persons | Interested persons[]{} | Details of persons with an interest in the property including their personal information, nature of interest, and notification status | MAY | Rule: is a MUST if `applicant-interest` is `none` |
| applicant-owns-land | Applicant owns land | True or False indicating whether the applicant owns the land where the advertisement will be displayed | MUST |  |
| permission-obtained | Permission obtained | True or False indicating whether permission of the owner for the display of an advertisement has been obtained | MAY | Rule: is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Permission not obtained details | Details explaining why permission from the land owner has not been obtained for the advertisement display | MAY |  |


**LDC Owner Details model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the property owner | MUST | 
informed-of-application | Informed of application | Whether the owner has been informed of the application | MUST | 


**LDC Interested Person model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal details of the interested person | MUST | 
nature-of-interest | Nature of interest | Description of the nature of a person's interest in the property | MUST | 
informed-of-application | Informed of application | Whether the person has been informed of the application | MUST | 
reason-not-informed | Reason not informed | Reason why a person was not informed of the application | MAY | 


**Person obj model**

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

Information about any pre-application advice sought from the planning authority


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Proposal details LDC

Details of the proposal for lawful development certificate applications

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposal-incl-building-operations | Proposal incl building operations | Does the proposal include building operations? | MUST | For lawful development certificate for proposed work |
| proposal-building-operations-description | Proposal building operations description | Description of the building operations included in the proposal | MAY | Rule: is a MUST if `proposal-incl-building-operations` is `True` |
| proposal-incl-change-of-use | Proposal incl change of use | Does the proposal include a change of use? | MUST |  |
| proposal-change-of-use-description | Proposal change of use description | Description of the change of use included in the proposal | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True`. Required if proposal-incl-change-of-use is true |
| proposal-existing-use-description | Proposal existing use description | Description of the existing use before the proposed change of use | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-existing-use-stop-date | Proposal existing use stop date | Date when the existing use stopped or will stop | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-started | Proposal started | Has any work on the proposal already been started | MUST |  |

**Validation rules**

- proposal-building-operations-description is required when proposal-incl-building-operations is true
- proposal-change-of-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date must be in YYYY-MM-DD format

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

## Site Visit Details

Details needed to support a site visit by the planning authority


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| can-be-seen-from | Site seen from public area | Can site be seen from a public road, public footpath, bridleway or other public land | MUST |  |
| contact-type | Site visit contact type | Indicates who the authority should contact to arrange a site visit | MUST | Select from the **site-visit-contact-type** enum |
| contact-reference | Contact reference | The reference of the applicant or agent who should be contacted for site visits | MAY |  |
| other-contact | Other site visit contact{} | Details of specifically named contact for site visits | MAY | Rule: is a MUST if `contact-type` is `other` |


**Other contact model**

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

