# Householder planning application

A simplified process for applications to alter or enlarge a single house (but not a flat), including works within the boundary/garden

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Access and rights of way](#access-and-rights-of-way)
* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Biodiversity net gain](#biodiversity-net-gain)
* [Checklist](#checklist)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Materials](#materials)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration)
* [Parking arrangements](#parking-arrangements)
* [Pre-application advice](#pre-application-advice)
* [Description of the proposal](#description-of-the-proposal)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)
* [Trees and hedges information](#trees-and-hedges-information)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


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


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MAY | 
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
url | URL | A URL pointing to the stored file for previously uploaded or hosted files | MAY | 
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded useful for identifying and preserving the file | MUST | 
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

## Access and rights of way

Information about changes to access arrangements and public rights of way


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | New or altered vehicle access | Is a new or altered vehicle access proposed to/from the public highway | MUST | Select from the **rights-of-way-answers** enum |
| new-altered-pedestrian | New or altered pedestrian access | Is a new or altered pedestrian access proposed to/from the public highway | MUST | Select from the **rights-of-way-answers** enum |
| change-right-of-way | Change to right of way | Will the proposal change public rights of way (diversion/extinguishment/creation) | MUST | Select from the **rights-of-way-answers** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY |  |


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- All fields must use values from rights-of-way-answers codelist
- If new-altered-vehicle is yes, details must be provided in highways module
- If change-right-of-way is yes, separate rights of way order may be needed
- If temp-right-of-way is yes, details of temporary diversions must be provided

## Agent contact details

Contact details of the agent acting on behalf of the applicant


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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

## Biodiversity net gain

Information about biodiversity net gain requirements for the development,
including pre-development biodiversity value, habitat loss details, and
supporting documentation


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| bng-exempt | Biodiversity gain exemption | Statement whether the biodiversity gain condition will apply if permission is granted. Householder applicants need to confirm the biodiversity gain condition does not apply. | MUST |  |

**Validation rules**

- application-type == 'hh' REQUIRES only bng-exempt field
- bng-condition-applies == false REQUIRES bng-condition-exemption-reasons.length >= 1
- bng-condition-applies == true REQUIRES bng-details
- application-type == 'hh' RECOMMENDS bng-exempt == false
- bng-condition-exemption-reasons[].exemption-type must be from bng-exemption-type codelist
- bng-details.pre-development-date <= application-submission-date OR earlier-date-reason provided
- bng-details.habitat-loss-after-2020 == true REQUIRES bng-details.habitat-loss-details
- bng-details.irreplaceable-habitats == true REQUIRES bng-details.irreplaceable-habitats-details

## Checklist

Identifies the national requirement types that apply to this application type


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| national-req-types | National requirement types[] | List of the document types required for the given application type | MUST |  |

**Validation rules**

- All values must be from the national-requirement-type codelist
- Values must be valid for the current application type

## Conflict of interest

Information about any conflicts of interest between the applicant/agent and the planning authority,
including relationships with staff or elected members


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Conflict to declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared | MUST |  |
| conflict-person-name | Conflict person name | Name of the individual with the conflict of interest that matches one of the names provided in applicants/agent section | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |
| conflict-details | Conflict details | Details of the conflict of interest including name, role and how the individual is related to the planning authority | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |

**Validation rules**

- conflict-person-name must match a name provided in applicants or agent sections

## Declaration

Declaration by the applicant or agent confirming the accuracy of the information provided


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| name | Name | A name of a person | MUST |  |
| declaration-confirmed | Declaration confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | MUST |  |
| declaration-date | Declaration date | The date the declaration was made | MUST |  |

**Validation rules**

- name must match one of the named individuals in the application
- declaration-date must be in YYYY-MM-DD format
- declaration-date must not be in the future

## Materials

Information about the materials used in the development, including both existing and proposed materials


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| building-elements | Building elements[]{} | Details of materials for a specific building element such as walls, roof, windows or doors | MUST |  |
| additional-material-information | Additional material information | Additional context or details about the materials to be used in the development | MUST |  |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY | Rule: is a MUST if `additional-material-information` is `True` |


**Building element model**

field | name | description | required | notes
-- | -- | -- | -- | --
building-element-type | Building element type | The part of building the materials relate to, such as walls, roofs, windows, or doors | MUST | Select from the **building-element-type** enum
existing-materials | Existing materials | Description of the materials currently used for this building element | MAY | 
proposed-materials | Proposed materials | Description of the materials proposed for this building element as part of the development | MAY | 
materials-not-applicable | Materials not applicable | Indicates this building element is not relevant to the application | MAY | 
materials-not-known | Materials not known | Indicates the materials for this building element are not yet known | MAY | 


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- Each building-element must have a unique building-element-type
- At least one of: existing-materials, proposed-materials, materials-not-applicable or materials-not-known must be provided for each building-element
- materials-not-applicable cannot be true if existing-materials or proposed-materials is provided
- materials-not-known cannot be true if existing-materials or proposed-materials is provided
- supporting-documents must reference valid documents in the application

## Ownership certificates and agricultural land declaration

Information about ownership of the site and/or property for development, including agricultural tenants and notification requirements.


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| sole-owner | Sole owner | Is the applicant the sole owner of the land? | MUST |  |
| agricultural-tenants | Agricultural tenants | Are there any agricultural tenants on the land? | MUST |  |
| owners-and-tenants | Owners and tenants[]{} | List of known owners and agricultural tenants | MAY |  |
| steps-taken | Steps taken | Description of steps taken to identify unknown owners or tenants | MAY |  |
| newspaper-notices | Newspaper notices[]{} | Details of notices published in papers | MAY |  |
| ownership-cert-option | Ownership certificate type | The type of ownership certificate based on ownership and tenancy status | MAY | Select from the **ownership-cert-type** enum |
| applicant-signature | Applicant signature | Digital signature of the applicant | MAY |  |
| agent-signature | Agent signature | Digital signature of the agent (if applicable) | MAY |  |
| signature-date | Signature date | Date when the ownership certificate was signed | MAY |  |


**Notified person model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Detail to help identify a person | MAY | 
notice-date | Notice date | Date when notice was served to an owner or tenant | MAY | 


**Newspaper notice model**

field | name | description | required | notes
-- | -- | -- | -- | --
newspaper-name | Newspaper name | Name of the newspaper where the ownership notice was published | MUST | 
publication-date | Publication date | Date when the ownership notice was published in the newspaper | MUST | 


**Person obj model**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 



## Parking arrangements

Information about how the proposed development affects existing parking arrangements


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-existing-parking-affected | Existing parking affected | Will the proposed works affect existing car parking arrangements | MUST |  |
| description | Description | A description of how the proposed works will affect existing car parking arrangements | MAY | Rule: is a MUST if `is-existing-parking-affected` is `True` |



## Pre-application advice

Information about any pre-application advice sought from the planning authority


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Description of the proposal

Information about what development, works or change of use is being proposed


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposal-description | Proposal description | A description of what is being proposed, including the development, works, or change of use | MUST |  |
| proposal-started | Proposal started | Has any work on the proposal already been started | MUST |  |
| proposal-started-date | Proposal start date | The date when work on the proposal started, in YYYY-MM-DD format | MAY | Rule: is a MUST if `proposal-started` is `True` |
| proposal-completed | Proposal completed | Has any work on the proposal already been completed | MUST |  |
| proposal-completed-date | Proposal completion date | The date when work on the proposal was completed, in YYYY-MM-DD format | MAY | Rule: is a MUST if `proposal-completed` is `True` |

**Validation rules**

- proposal-description must be clear and concise
- proposal-started-date must not be in the future
- proposal-completed-date must be after proposal-started-date if both provided
- reserved-matters must be valid types from the codelist
- related-application reference must exist in authority records
- pip-reference must match an existing Planning in Principle application
- PSI projects must be checked against infrastructure improvement plans

## Site details

Information about the location and extent of the site where development 
or works are proposed


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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

## Trees and hedges information

Information about trees and hedges on or adjacent to the development site, including any that pose risks or need to be removed


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| has-falling-trees-risk | Falling trees risk | Whether there are falling trees on-premises or adjacent premises that are a risk to the development | MUST |  |
| falling-trees-document | Falling trees document{} | Details of document showing location of trees that pose a risk to the development | MAY | Rule: is a MUST if `has-falling-trees-risk` is `True` |
| tree-removal | Tree removal | Whether trees or hedges need to be pruned or removed | MUST |  |
| tree-removal-plan | Tree removal plan{} | Details of document showing location of trees and hedges to be removed or pruned | MAY | Rule: is a MUST if `tree-removal` is `True` |


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- falling-trees-document reference must match a document in application.documents
- tree-removal-plan reference must match a document in application.documents

## Required codelists

This are the codelist required to support this specification:

- building-element-type
- user-role-type
- bng-exemption-type
- contact-priority