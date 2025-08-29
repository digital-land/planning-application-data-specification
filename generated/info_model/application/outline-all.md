# Outline Planning Permission with All Matters Reserved

Outline planning permission with all matters reserved

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Biodiversity net gain](#biodiversity-net-gain)
* [Checklist](#checklist)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Employment](#employment)
* [Existing use](#existing-use)
* [Flood risk assessment](#flood-risk-assessment)
* [Hours of operation](#hours-of-operation)
* [Non residential floorspace](#non-residential-floorspace)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration)
* [Pre-application advice](#pre-application-advice)
* [Processes machinery waste](#processes-machinery-waste)
* [Description of the proposal](#description-of-the-proposal)
* [Residential units](#residential-units)
* [Site area](#site-area)
* [Site details](#site-details)
* [Site Visit Details](#site-visit-details)

### Codelists


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

## Biodiversity net gain

Information about biodiversity net gain requirements for the development,
including pre-development biodiversity value, habitat loss details, and
supporting documentation


**Biodiversity net gain module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |

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

## Employment

Module for capturing information about employment impacts of a development 
proposal, including existing and proposed employee counts


**Employment module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| existing-employees | Existing employees{} | Counts of existing employees | MUST |  |
| proposed-employees | Proposed employees{} | Counts of proposed employees | MUST |  |
| employment-impact | Employment impact | Summary of net employment change (gain/loss) | MAY |  |


**Employees component**

field | name | description | required | notes
-- | -- | -- | -- | --
full-time | Full-time | Number of full-time employees | MUST | 
part-time | Part-time | Number of part-time employees | MUST | 
total-fte | Total FTE | Total full-time equivalent (FTE) | MUST | 

**Validation rules**

- Existing-employees is required for all non-residential applications
- Proposed-employees is required if the proposal affects employment capacity
- Employment-impact is calculated based on existing and proposed values
- Full-time and part-time employee counts must be positive integers or 0
- FTE is calculated as full-time + (part-time ÷ 2)

## Existing use

Information about the current and previous use of the site, including contamination status and supporting documents.


**Existing use module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| existing-use-details | Existing use details[]{} | List of existing site uses and related land areas | MUST |  |
| site-vacant | Site vacant | Is the site currently vacant | MUST |  |
| last-use-details | Last use details | Description of the last use of the site | MAY | Rule: is a MUST if `site-vacant` is `True` |
| last-use-end-date | Last use end date | Date the last use ended (YYYY-MM-DD format) | MAY | Rule: is a MUST if `site-vacant` is `True` |
| is-contaminated-land | Is contaminated land | Is the site known to be contaminated? | MUST |  |
| is-suspected-contaminated-land | Is suspected contaminated land | Is the site suspected of contamination? | MUST |  |
| proposed-use-contamination-risk | Proposed use contamination risk | Is the proposed use vulnerable to the presence of contamination? | MUST |  |
| contamination-assessment | Contamination assessment | Reference to contamination assessment document | MAY |  |


**Existing use detail component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-details | Use details | Further detail of the use | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`
land-part | Land part | Which part of the land the use relates to | MUST | 

**Validation rules**

- last-use-details and last-use-end-date are required if site-vacant is true
- contamination-assessment is required if any of is-contaminated-land, is-suspected-contaminated-land, or proposed-use-contamination-risk is true

## Flood risk assessment

Information about flood risk assessments for planning applications including flood risk area status, 
data sources, assessment documents, watercourse proximity, flood risk impacts, and surface water disposal methods


**Flood risk assessment module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| flood-risk-area | Flood risk area | Is the site within an area at risk of flooding? | MUST |  |
| data-provided-by | Data provided by | Who provided the data: Applicant or System/Service? | MAY | Select from the **provided-by** enum. opens possibility for services to work it out and not rely on the applicant to know |
| flood-risk-assessment | Flood risk assessment | Reference of the flood risk assessment document | MAY | Rule: is a MUST if `flood-risk-area` is `True` |
| within-20m-watercourse | Within 20m watercourse | Whether the development is within 20 metres of a watercourse | MUST |  |
| increases-flood-risk | Increases flood risk | Whether the development increases flood risk | MUST |  |
| surface-water-disposal | Surface water disposal[] | Method for disposing of surface water | MUST | Select from the **surface-water-disposal-type** enum |

**Validation rules**

- flood-risk-assessment document reference is required when flood-risk-area is true
- surface-water-disposal must contain at least one disposal method

## Hours of operation

Hours of opening for each non-residential use proposed

**Hours of operation module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |

**Validation rules**

- At least one hours-of-operation entry must be provided
- Either operational-times or hours-not-known must be provided within each hours-of-operation entry
- use-other is required when use is 'other'
- time-ranges is required when not closed
- open-time and close-time must be in HH:MM format
- close-time must be after open-time within same time range

## Non residential floorspace

Information about non-residential floorspace changes including use class details and room counts for specific accommodation types

**Non residential floorspace module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| floorspace-details | Floorspace details[]{} | List of non-residential floorspace changes by use class | MAY |  |
| room-details | Room details[]{} | List of room changes for hotels, residential institutions and hostels | MAY | Required if change to hotels, residential institutions and hostel floorspace (C1, C2, C2A use classes) |


**Floorspace details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | 
existing-gross-floorspace | Existing gross floorspace | Existing gross internal floorspace, in sqm | MUST | 
floorspace-lost | Floorspace lost | Gross floorspace to be lost by change of use, in sqm | MUST | 
total-gross-proposed | Total gross proposed | Total gross internal floorspace proposed, in sqm | MUST | 
net-additional-floorspace | Net additional floorspace | Net additional gross internal floorspace, in sqm | MUST | Calculated as total-gross-proposed - existing-gross-floorspace


**Room details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use-class | Use class | Type of non-residential use class | MUST | Select from the **use-class** enum. Only required for C1, C2, C2A, or Other use classes
existing-rooms-lost | Existing rooms lost | Existing rooms to be lost by change of use | MUST | Must be 0 or positive
total-rooms-proposed | Total rooms proposed | Total rooms proposed (including change of use) | MUST | Must be 0 or positive
net-additional-rooms | Net additional rooms | Net additional rooms following development | MUST | Calculated as total-rooms-proposed - existing-rooms-lost

**Validation rules**

- floorspace-details is required when non-residential-change is true
- room-details is required when floorspace involves C1, C2, C2A, or other use classes
- specified-use is required when use is other or sui generis
- All floorspace values must be 0 or positive
- All room values must be 0 or positive
- net-additional-floorspace must equal total-gross-proposed minus existing-gross-floorspace
- net-additional-rooms must equal total-rooms-proposed minus existing-rooms-lost

## Ownership certificates and agricultural land declaration

Information about ownership of the site and/or property for development, including agricultural tenants and notification requirements.


**Ownership certificates and agricultural land declaration module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |



## Pre-application advice

Information about any pre-application advice sought from the planning authority


**Pre-application advice module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Processes machinery waste

Information about site activities, processes, and waste management development
including facility types, capacities, and throughput details


**Processes machinery waste module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| site-activity-details | Site activity details | Description of activities, processes, and end products including site operations, plant, ventilation, and machinery | MUST |  |
| proposal-waste-management | Proposal waste management | Whether the proposal involves waste management development | MUST |  |
| waste-management | Waste management[]{} | List of waste management facilities involved in the proposal | MAY |  |
| waste-streams | Waste streams throughput{} | Annual throughput for waste streams by waste type | MAY |  |


**Waste management component**

field | name | description | required | notes
-- | -- | -- | -- | --
waste-management-facility-type | Waste management facility type | Type of waste management facility | MUST | Select from the **waste-management-type** enum
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
total-capacity | Total capacity | Total capacity of void in cubic metres (or tonnes/litres) | MAY | Rule: is a MUST if `not-applicable` is `False`
annual-throughput | Annual throughput | Maximum annual operational throughput in tonnes/litres | MAY | Rule: is a MUST if `not-applicable` is `False`


**Waste streams component**

field | name | description | required | notes
-- | -- | -- | -- | --
municipal | Municipal | Maximum throughput for municipal waste (annual throughput in tonnes/litres) | MAY | 
construction-demolition | Construction demolition | Maximum throughput for construction and demolition waste (annual throughput in tonnes/litres) | MAY | 
commercial-industrial | Commercial industrial | Maximum throughput for commercial and industrial waste (annual throughput in tonnes/litres) | MAY | 
hazardous | Hazardous | Maximum throughput for hazardous waste (annual throughput in tonnes/litres) | MAY | 

**Validation rules**

- if proposal-waste-management == true then waste-management is required
- if proposal-waste-management == true then waste-streams is required
- if not-applicable == false then total-capacity is required
- if not-applicable == false then annual-throughput is required
- is-total-capacity-known and is-annual-throughput-known only apply to outline applications

## Description of the proposal

Information about what development, works or change of use is being proposed


**Description of the proposal module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |

**Validation rules**

- proposal-description must be clear and concise
- proposal-started-date must not be in the future
- proposal-completed-date must be after proposal-started-date if both provided
- reserved-matters must be valid types from the codelist
- related-application reference must exist in authority records
- pip-reference must match an existing Planning in Principle application
- PSI projects must be checked against infrastructure improvement plans

## Residential units

Information about residential units including existing and proposed unit counts, 
with detailed breakdowns by tenure and housing type


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

## Site area

Information about the size of the development site, including 
the area measurement and source of the measurement


**Site area module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| site-area-in-hectares | Site area in hectares | The size of the site in hectares | MUST |  |
| site-area-provided-by | Site area provided by | Who provided the site area value | MAY | Select from the **provided-by** enum |

**Validation rules**

- site-area-in-hectares must be a positive number
- Authority can use site-area-provided-by to determine if calculation verification is needed
- site-area-in-hectares is measured in hectares

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

## Site Visit Details

Details needed to support a site visit by the planning authority


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
