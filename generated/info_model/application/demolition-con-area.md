# Planning permission for relevant demolition in a conservation area

An application for planning permission involving the demolition of any unlisted building or structure in a conservation area if permission is required

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Biodiversity net gain](#biodiversity-net-gain)
* [Checklist](#checklist)
* [Community consultation](#community-consultation)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Demolition reason](#demolition-reason)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration)
* [Pre-application advice](#pre-application-advice)
* [Description of the proposal](#description-of-the-proposal)
* [Related applications](#related-applications)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)

### Codelists

* [BNG exemption type](#bng-exemption-type)
* [Contact priority](#contact-priority)
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

## Biodiversity net gain

How any natural habitats on the development site will be improved by the proposed works.

**Biodiversity net gain module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| bng-condition-applies | Biodiversity gain condition applies | Does the applicant believe the Biodiversity Gain Condition applies to this application | MUST |  |
| bng-condition-exemption-reasons | Biodiversity gain condition exemption reason[]{} | Reasons why BNG does not apply, referencing exemptions or transitional arrangements | MAY | Rule: is a MUST if `bng-condition-applies` is `False` |
| bng-details | Biodiversity net gain details{} | Comprehensive details about biodiversity net gain assessment including pre-development value, habitat loss information, and supporting documentation | MAY | Rule: is a MUST if `bng-condition-applies` is `True` |


**BNG exemption reason component**

field | name | description | required | notes
-- | -- | -- | -- | --
exemption-type | Exemption type | The type of biodiversity gain exemption from the bng-exemption-type enum | MUST | Select from the **bng-exemption-type** enum
reason | Reason | The reason the exemption applies to this proposal | MUST | 


**Biodiversity net gain details component**

field | name | description | required | notes
-- | -- | -- | -- | --
pre-development-date | Pre development date | Date of pre-development biodiversity value calculation, must align with application or justified earlier date | MUST | 
pre-development-biodiversity-value | Pre development biodiversity value | Calculated biodiversity value in Habitat Biodiversity Units | MUST | 
earlier-date-reason | Earlier date reason | Reason for using a pre-development date that is earlier than the application submission | MAY | 
habitat-loss-after-2020 | Habitat loss after 2020 | Indicates whether there has been degradation of onsite habitat(s) after 30 Jan 2020 | MAY | 
habitat-loss-details | Habitat loss details{} | Details of habitat loss or degradation events | MAY | Rule: is a MUST if `habitat-loss-after-2020` is `True`
metric-publication-date | Metric publication date | Publication date of the biodiversity metric tool used for calculations | MUST | 
irreplaceable-habitats | Irreplaceable habitats | Indicates whether the site contains any irreplaceable habitats | MUST | 
irreplaceable-habitats-details | Irreplaceable habitats details | Description and references for any irreplaceable habitats identified on the site | MAY | Rule: is a MUST if `irreplaceable-habitats` is `True`
supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MUST | 


**Habitat loss details component**

field | name | description | required | notes
-- | -- | -- | -- | --
loss-date | Loss date | Date the activity causing habitat loss or degradation occurred | MUST | 
pre-loss-biodiversity-value | Pre loss biodiversity value | Biodiversity value immediately before habitat loss or degradation occurred, measured in Habitat Biodiversity Units | MUST | 
supporting-evidence | Supporting evidence | Description or reference to supporting documents for habitat loss or degradation evidence | MAY | 


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 

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

## Demolition reason

Why demolition is necessary at the development site

**Demolition reason module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| reason | Reason | Why is it necessary to demolish all or part of the building(s) and structure(s)? | MUST |  |



## Ownership certificates and agricultural land declaration

Who will be affected by the proposal and whether they have been notified, such as agricultural tenants

**Ownership certificates and agricultural land declaration module**

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


**Notified person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | details of the owner (or tenant when not a listed building consent application) | MAY | 
notice-date | Notice date | Date when notice was served | MAY | 


**Newspaper notice component**

field | name | description | required | notes
-- | -- | -- | -- | --
newspaper-name | Newspaper name | Name of the newspaper where notice was published | MUST | 
publication-date | Publication date | Date when the notice was published | MUST | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 



## Pre-application advice

Details of pre-application advice received from the planning authority

**Pre-application advice module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Description of the proposal

What development, works or change of use is proposed

**Description of the proposal module**

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

## Related applications

Details of any other development proposals made for the site

**Related applications module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| has-related-applications | Has related applications | Are there any related applications, previous proposals or demolitions for the site | MUST |  |
| related-applications | Related applications[]{} | List of related applications, previous proposals or demolitions for the site | MAY |  |


**Related application details component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST | 
description | Description | A description of the related application | MUST | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- related-applications must be provided when has-related-applications is true
- decision-date is optional and only relevant if the related proposal has been decided

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

### BNG exemption type

| reference | name | description | entry-date | end-date |
| --- | --- | --- | --- | --- |
| pre-commencement | Submitted before BNG commencement | Planning applications submitted before the Biodiversity Net Gain rules took effect (need to add the effective date) | 2025-07-15 |  |
| small-sites | Small sites exemption | Temporary exemption for non-major developments. | 2025-07-15 |  |
| de-minimis | De minimis exemption | Development below the minimum threshold for BNG requirements. | 2025-07-15 |  |
| self-build | Self-build and custom build | Self-build or custom build development projects. | 2025-07-15 |  |
| gain-site | Biodiversity gain site | Development of a registered biodiversity gain site. | 2025-07-15 |  |
| retrospective | Retrospective planning permission | Applications for retrospective planning permission. | 2025-07-15 |  |
| hs2 | High Speed Railway development | Development related to the High Speed Railway (HS2). | 2025-07-15 |  |

### Contact priority

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

### User role type

| reference | name | description |
| --- | --- | --- |
| agent | Agent | A professional agent working for the applicant |
| proxy | Proxy | An individual working on behalf of the applicant but not in a professional capacity |
