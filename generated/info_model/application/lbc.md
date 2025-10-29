# Listed building consent

An application for works for the demolition of a listed building or for its alteration or extension in any manner which would affect its character as a building of special architectural or historic interest

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Checklist](#checklist)
* [Community consultation](#community-consultation)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Demolition](#demolition)
* [Immunity from listing](#immunity-from-listing)
* [Listed building alterations](#listed-building-alterations)
* [Listed building grade](#listed-building-grade)
* [Materials](#materials)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration)
* [Pre-application advice](#pre-application-advice)
* [Description of the proposal](#description-of-the-proposal)
* [Related applications](#related-applications)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)

### Codelists

* [Building element type](#building-element-type)
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

## Demolition

Details of any demolition that needs to take place as part of the development proposal.

**Demolition module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-proposing-demolition | Is propsing demolition | Does the proposal include partial or total demolition of a listed building? | MUST |  |
| is-total-demolition | Is total demolition | Indicating whether the proposal involves total demolition of a listed building | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| is-demolishing-building-in-curtilage | Demolition building in curtilage | True or False indicating whether the proposal involves demolition of a building in the curtilage of a listed building | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| is-partial-demolition | Demolition part | True or False indicating whether the proposal involves partial demolition of a listed building | MAY | Rule: is a MUST if `is-proposing-demolition` is `True` |
| listed-building-volume | Listed building volume | Volume of listed building in cubic metres | MAY | Rule: is a MUST if `is-partial-demolition` is `True` |
| demolition-volume | Demolition volume | Volume of part to be demolished in cubic metres | MAY | Rule: is a MUST if `is-partial-demolition` is `True` |
| part-built-date | Part built date | The approximate date the part to be removed was built, in YYYY-MM-DD format. | MAY | Rule: is a MUST if `is-partial-demolition` is `True`. Approximate dates are allowed |
| description | Description | Description of the building or part you are proposing to demolish | MUST |  |
| reason | Reason | Reason for demolition | MUST |  |



## Immunity from listing

Whether the applicant has obtained a Certificate of Immunity (COI) meaning the building in question cannot be listed

**Immunity from listing module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| cert-of-immunity-sought | Certificate of immunity sought | Has a certificate of immunity been sought | MUST | Select from the **yes-no-unknown** enum |
| application-result | Application result | Provide the result of the application for a certificate of immunity | MAY |  |

**Validation rules**

- application-result is required when cert-of-immunity-sought is 'yes'

## Listed building alterations

Details of any changes being made to a listed building as part of development works

**Listed building alterations module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposal-alter-lb | Proposal alter listed building | True or False if proposal includes alterations to a listed building | MUST |  |
| proposal-alter-lb-types | Proposal alteration types[] | Select from a list of listed building alteration types, select all that apply | MAY | Select from the **lb-alteration-type** enum |
| document-reference | Document reference[]{} | References to documents detailing the proposed alterations | MAY |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 



## Listed building grade

The grade of any listed building affected by the proposed development.

**Listed building grade module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Listed building grade | The grade of the listed building, selected from the listed-building-grade codelist or "don't know" | MUST | Select from the **listed-building-grade** enum |
| listed-building | Listed building | Listed building reference for cross-referencing with listed building records | MAY |  |
| provided-by | Provided by | Source of the listed building grade information | MAY | Select from the **provided-by** enum |

**Validation rules**

- listed-building-grade must be selected from the listed-building-grade codelist or 'don't know'
- If listed-building is provided, it must reference a valid listed building

## Materials

What materials are being used for the proposed development

**Materials module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| building-elements | Building elements[]{} | Details of materials for a specific building element such as walls, roof, windows or doors | MUST |  |
| providing-additional-material-information | Providing additional material information | Is the applicant providing additional materials information on submitted plan(s)/drawing(s)/design and access statement? | MUST |  |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY | Rule: is a MUST if `providing-additional-material-information` is `True` |


**Building element component**

field | name | description | required | notes
-- | -- | -- | -- | --
building-element-type | Building element type | The part of building the materials relate to, such as walls, roofs, windows, or doors | MUST | Select from the **building-element-type** enum
existing-materials | Existing materials | Description of the materials currently used for this building element | MAY | 
proposed-materials | Proposed materials | Description of the materials proposed for this building element as part of the development | MAY | 
materials-not-applicable | Materials not applicable | Indicates this building element is not relevant to the application | MAY | 
materials-not-known | Materials not known | Indicates the materials for this building element are not yet known | MAY | 


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 

**Validation rules**

- Each building-element must have a unique building-element-type
- At least one of: existing-materials, proposed-materials, materials-not-applicable or materials-not-known must be provided for each building-element
- materials-not-applicable cannot be true if existing-materials or proposed-materials is provided
- materials-not-known cannot be true if existing-materials or proposed-materials is provided
- supporting-documents must reference valid documents in the application

## Ownership certificates and agricultural land declaration

Who will be affected by the proposal and whether they have been notified, such as agricultural tenants

**Ownership certificates and agricultural land declaration module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| sole-owner | Sole owner | Is the applicant the sole owner of the land? | MUST |  |
| lbc-owners | Owners of listed building[]{} | List of known owners | MAY |  |
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

Details of pre-application advice previously received from the planning authority

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

### Building element type

| reference | name | description | application-types | notes |
| --- | --- | --- | --- | --- |
| walls | Walls | A vertical construction that bounds or subdivides spaces | advertising;demolition-con-area;full;hh;outline | Referring to same thing as IfcWall |
| roof | Roof | A covering of the top part of a building, it protects the building against the effects of weather | advertising;demolition-con-area;full;hh;outline | Referring to same thing as IfcRoof |
| windows | Windows |  | advertising;demolition-con-area;full;hh;outline |  |
| doors | Doors |  | advertising;demolition-con-area;full;hh;outline |  |
| boundary-treatments | Boundary treatments |  | advertising;demolition-con-area;full;hh;lbc;outline |  |
| vehicle-access-hard-standings | Vehicle access and hard-standings |  | advertising;demolition-con-area;full;hh;lbc;outline |  |
| lighting | Lighting |  | advertising;demolition-con-area;full;hh;lbc;outline |  |
| external-walls | External walls |  | lbc |  |
| roof-covering | Roof covering |  | lbc |  |
| chimney | Chimney |  | lbc |  |
| external-doors | External doors |  | lbc |  |
| ceilings | Ceilings |  | lbc |  |
| internal-walls | Internal walls |  | lbc |  |
| floors | Floors |  | lbc |  |
| internal-doors | Internal doors |  | lbc |  |
| rainwater-goods | Rainwater goods |  | lbc |  |
| other | Other |  | lbc |  |

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
