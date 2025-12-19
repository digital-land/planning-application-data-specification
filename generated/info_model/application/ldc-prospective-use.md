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

### Codelists

* [Planning requirement](#planning-requirement)

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

## Grounds for application (information about the existing use(s))

Supporting inforation for a Lawful Development Certificate application relating to how the site has most recently been used.

**Grounds for application (information about the existing use(s)) module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| use-lawful-reason | Use lawful reason | Explanation of why the existing or last use is considered lawful, 
providing justification for a lawful development certificate application
 | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MAY |  |
| use | Use | A use class or type of use | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other` |


**Document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | The name or title of the document | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**File component**

field | name | description | required | notes
-- | -- | -- | -- | --
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

What the new site will be used for

**Grounds for proposed use module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| use | Use | State proposed use class | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY |  |
| operation-type | Operation type | Whether the proposed use is temporary or permanent | MUST | Select from the **operation-type** enum |
| temporary-details | Temporary details | Details of temporary use including duration and specific arrangements | MAY |  |
| reason | Reason | A textual reason | MUST |  |

**Validation rules**

- specified-use is required if use is 'sui' or 'other'
- temporary-details is required if operation-type is 'temporary'

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



## Proposal details LDC

Details of why a Lawful Development Certificate is required.

**Proposal details LDC module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
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

### Planning requirement

| reference | name | description | synonyms | document-type | source | notes | entry-date | end-date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| acoustic-report | Acoustic report | A report measuring the noise environment for a new development or its effect within a proposed development | Noise impact assessment |  |  |  |  |  |
| affordable-housing-statement | Affordable housing statement | This statement should set out how the development scheme will comply with the local authority’s  affordable housing policy |  |  | National Planning Policy Framework (NPPF), paras 61-77 |  |  |  |
| air-quality-assessment | Air quality assessment (AQA) | An assessment of the impact on air quality around the development and during the construction phase |  |  | National Planning Policy Framework (NPPF), paras 110, 119 |  |  |  |
| arboriculturist-report | Arboricultural impact assessment | A supporting report from an arboriculturist for any proposed work on trees - providing detail on the conditions of the trees on or next to the development site | Arboricultural report;Tree report;Tree survey;Condition of Trees;Arboricultural implication assessment |  | National Planning Policy Framework (NPPF), paras 44, 136, 187, 193 |  |  |  |
| archaeological-assessment | Archaeological assessment | An evaluation to identify and assess the potential of an area to contain as-yet unrecorded archaeological sites |  |  |  |  |  |  |
| biodiversity-survey-report | Biodiversity survey and report | Information on biodiversity interests and protected species and any possible impacts on them from the development, plus details of any measures proposed to mitigate or compensate for the impacts | Biodiversity report;Biodiversity statement |  | The Environment Act 2021 National Planning Policy Framework (NPPF), paragraphs 187 - 195 National Planning Practice Guidance (NPPG), under the heading ‘Natural Environment’ |  |  |  |
| cil-form | Community infrastructure levy (CIL) form | A form that must be completed to determine whether the development is subject to a CIL payment |  |  |  |  |  |  |
| condition-of-trees | Condition of Trees | Written arboricultural advice |  |  |  | Covers if tree is diseased, at risk of breaking or falling |  |  |
| completed-app-form | Completed application form | The application form that must be completed for all planning applications, including the relevant sections and questions |  |  | Article 7 Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended)and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) |  | 2025-05-07 |  |
| daylight-sunlight-assessment | Daylight and sunlight assessment | An assessment to evaluate the potential impact of a proposed development on the amount of natural light received by surrounding properties |  |  |  |  |  |  |
| design-and-access-statement | Design and access statement | A report accompanying and supporting a planning application that explains how a proposed development is a suitable response to the site and its setting, and demonstrates that it can be adequately accessed by prospective users |  |  | Article 9, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| elevation-existing | Elevation - existing | What a building or structure currently looks like from the outside at a scale of 1:50 or 1:100 |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| elevation-proposed | Elevation - proposed | Showing how the building will look after work has been carried out at a scale of 1:50 or 1:100 |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| energy-statement | Energy statement | A detailed report about how a planned development will meet the energy efficiency standards set by the local planning authority |  |  |  |  |  |  |
| eia | Environmental Impact Assessment (EIA) |  |  |  |  | Required if the site exceeds certain thresholds or is near sensitive areas re onshore extraction of oil and gas |  | 2025-03-27 |
| environmental-statement | Environmental Statement | A statement setting out an assessment of the likely environmental effects of the proposed development - this is only required if the local planning authority deem the application to have environmental impacts after the Environmental Impact Assessment has been assessed |  |  | National Planning Policy Framework (NPPF), para 44 National Planning Practice Guidance (NPPG), paras 010 (Reference ID: 4-010-20170728), 034 (Reference ID: 4-034-20170728) and 035 (Reference ID: 4-035-20170728) Town and Country Planning (Environmental lmpact Assessment) Regulations 2017 | Required by Development relating to the onshore extraction of oil and gas applications |  |  |
| flood-risk-assessment | Flood risk assessment | An assessment of flood risk that needs to be completed if the proposed development is within a flood risk zone to show the potential impacts of the development on flooding and propose mitigation, such as SuDs |  |  | National Planning Policy Framework (NPPF), paras 44, 161-186 |  |  |  |
| floor-plan-existing | Floor plan - existing | Floor plans showing the building as it is now, usually at a scale of 1:100, but can be 1:50 if done to maintain consistency from the elevation drawings |  | Plans and drawings |  | general requirement |  |  |
| floor-plan-proposed | Floor plan - proposed | Floor plans showing the proposed changes to the building, usually at a scale of 1:100, but can be 1:50 if done to maintain consistency from the elevation drawings |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| heritage-impact-assessment | Heritage impact assessment | If the site is close to a heritage asset or conservation area a report is needed to assess the effect of the proposed development on the significance of the heritage |  |  |  |  |  |  |
| heritage-statement | Heritage statement | This statement describes a heritage asset, its significance and the proposed works that are being applied for |  |  | National Planning Policy Framework (NPPF), paras 202 - 221 |  |  |  |
| hydrocarbon-licence | Hydrocarbon Licence | Proof of exploration rights from North Sea Transition Authority (NSTA) |  |  |  |  |  |  |
| land-contamination-assessment | Land contamination assessment | Report on potential land contamination issues - if contamination is found on site remediation and mitigation proposals will need to be included |  |  | National Planning Policy Framework (NPPF), paras 196 to 201 | Needed if the site is known or suspected to be contaminated. |  |  |
| landscaping-plan | Landscaping plan | A plan of a site considering both soft-landscaping (natural elements like flowers, trees, and grass) as well as hard-landscaping (man-made features like lawn furniture, fountains, and sheds) |  |  |  |  |  |  |
| lighting-assessment | Lighting assessment | A lighting assessment is required for all applications that include use of floodlighting or a significant amount of external lighting |  |  |  |  |  |  |
| location-plan | Location plan | A location plan that shows the site outlined clearly in red in relation to the surrounding area, at a scale of 1:1250 or 1:2500, showing at least 2 named roads and surrounding land and buildings. A blue line must be drawn around any other land owned by the applicant close to or adjoining the application site |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| noise-and-traffic-assessment | Noise and Traffic Assessment | Evaluates operational impact on surrounding communities |  |  |  |  |  | 2025-03-27 |
| noise-assessment | Noise assessment | A report that assesses the impact of noise from the proposed development on the surrounding area |  |  | National Planning Policy Framework (NPPF), paras 187 and 198 |  | 2025-04-25 |  |
| photos | Site photographs | Pictures to show the existing context and condition of the site and surrounding area |  |  | Section 3A, The Planning (Listed Buildings and Conservation Areas) Regulations 1990 |  |  |  |
| planning-statement | Planning statement | The statement identifies the context and need for a proposed development, and assesses how the development is in accordance with the relevant national and local policies |  |  |  |  |  |  |
| roof-plan-existing | Roof plan - existing | Drawing showing the roof as it is now |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) Section 3A, The Planning (Listed Buildings and Conservation Areas) Regulations 1990 | general requirement |  |  |
| roof-plan-proposed | Roof plan - proposed | Drawing showing the proposed changes to the roof |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended);Section 3A, The Planning (Listed Buildings and Conservation Areas) Regulations 1990 | general requirement |  |  |
| schedule-of-works | Schedule of Works |  |  |  | Section 3A, The Planning (Listed Buildings and Conservation Areas) Regulations 1990 | required by Camden for all lbc applications |  |  |
| section-existing | Section - existing | A plan that shows an existing vertical cut through a building or site, revealing the interior and exterior profiles |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| section-proposed | Section - proposed | A plan that shows the proposed vertical cut through a building or site, revealing the interior and exterior profiles |  | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement |  |  |
| site-plan | Site plan | A site plan that shows the proposed development in relation to the site boundaries and other existing buildings at a scale of 1:200 or 1:500 is advised | Block plan | Plans and drawings | Article 7, Town and Country Planning (Development Management Procedure) (England) Order 2015 (as amended) | general requirement. For extraction of oil and gas needs to Needed to show site layout, access, and safety zones |  |  |
| site-restoration | Site restoration plan |  |  |  |  | Required under UK planning conditions to ensure post-production remediation |  | 2025-03-27 |
| sketch-plan | Sketch Plan | Often a plan showing the position of the trees listed in an application |  |  |  |  |  | 2025-03-27 |
| sci | Statement of community involvement (SCI) | Sets out how residents and businesses have been involved in the design and development process of the proposals |  |  | National Planning Policy Framework (NPPF), para 41 |  |  |  |
| structural-damage | Structural damage report | A report that relates specifically to the structural condition of the property if it has been affected by nearby trees |  |  |  | Mentioned in "Trees - Addtional information" section of tree works form |  |  |
| subsidence-report | Subsidence Report | A report by an engineer or surveyor describing damage, vegetation, soil, roots, and repair proposals |  |  |  |  |  | 2025-03-27 |
| sustainable-drainage-strategy | Sustainable Drainage Strategy (SuDS) |  |  |  |  |  |  | 2025-03-27 |
| transport-assessment | Transport assessment or statement | A description and analysis of the existing transport conditions and details of the expected impact of the proposed development on the local transportation system |  |  | National Planning Policy Framework (NPPF), paras 109 - 114 |  |  |  |
| travel-plan | Travel plan | A package of actions to encourage safe, healthy and sustainable travel options for a new development |  |  | National Planning Policy Framework (NPPF), paras 109 - 114 |  |  |  |
| ecology-assessment | Ecology Assessment | A document to identify how protection of biodiversity and habitat quality will be achieved and enhanced, where possible. | Ecology Report |  | National Planning Policy Framework (NPPF), paras 187 - 195 National Planning Practice Guidance (NPPG), under the heading ‘Natural Environment’ |  | 2025-03-27 |  |
| fire-statement | Fire statement | A report that sets out how the proposal handles the fire safety aspects, including details of fire safety measures, access for firefighting, and evacuation plans. | Fire Safety Report |  | The Town and Country Planning (Development Management Procedure)(England) Order 2015 (as amended) |  | 2025-04-25 |  |
| habitat-baseline | Habitat baseline plan |  |  |  |  |  | 2025-04-25 |  |
| proposed-habitat-plan | Proposed habitat plan |  |  |  |  |  | 2025-04-25 |  |
| sustainability-statement | Sustainability statement | A report that outlines how the development will meet sustainability objectives, including energy efficiency, water conservation, and waste management. | Sustainability report |  | National Planning Policy Framework (NPPF), paras 44 – 45 and 162 to 169 |  | 2025-04-25 |  |
| bng-metric | Biodiveristy Net Gain Metric | A metric used to assess the biodiversity value of a site before and after development, ensuring that the development results in a net gain for biodiversity. | BNG metric |  | The Environment Act 2021 National Planning Policy Framework (NPPF), paragraphs 187 - 195National Planning Practice Guidance (NPPG), under the heading ‘Natural Environment’ |  | 2025-04-25 |  |
