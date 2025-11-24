# Outline planning

Applications that are used to understand whether the basic nature of a development is viable

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

* [BNG exemption type](#bng-exemption-type)
* [Contact priority](#contact-priority)
* [Day type](#day-type)
* [Housing type](#housing-type)
* [Tenure type](#tenure-type)
* [Use class](#use-class)
* [Use class for accommodation](#use-class-for-accommodation)
* [User role type](#user-role-type)
* [Waste management type](#waste-management-type)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


**Application fields module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-subtype** enum |
| planning-authority | Planning authority | The reference of the planning authority the application has been submitted to, e.g. local-authority:CMD | MUST | Select from the **planning-authority** enum. Currently built by combining local-authority, development-corporation and national-park-authority datasets from planning.data.gov.uk |
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

## Employment

How the proposed development will impact existing and proposed employee numbers

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

How the site is currently being used.

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

Results of any flood risk assessments made for the development site

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

Proposed operating hours if the proposed development is intended for non-residential use.

**Hours of operation module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation | Hours of operation[]{} | List the hours of operation by non-residential use | MUST |  |


**Hours of operation component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-other | Use other | Specify use if use is "other" | MAY | Rule: is a MUST if `use` is `other`. Required if use is "other"
operational-times | Operational times[]{} | Structured data for operational hours by day | MAY | Rule: is a MUST if `hours-not-known` is `True`. Must be completed if hours-not-known is not provided
hours-not-known | Hours not known | Applicant states they do not know the hours of operation | MAY | 


**Operational times component**

field | name | description | required | notes
-- | -- | -- | -- | --
day-type | Day type | Day or type of day | MUST | Select from the **day-type** enum
closed | Closed | True or False - explicitly state when closed | MAY | If True, open-time and close-time must be empty
time-ranges | Time ranges[]{} | Opening and closing times for the day | MAY | Rule: is a MUST if `closed` is `False`. Can have multiple ranges (e.g., morning and evening opening)


**Time range component**

field | name | description | required | notes
-- | -- | -- | -- | --
open-time | Open time | Opening time | MUST | Format: HH:MM
close-time | Close time | Closing time | MUST | Format: HH:MM

**Validation rules**

- At least one hours-of-operation entry must be provided
- Either operational-times or hours-not-known must be provided within each hours-of-operation entry
- use-other is required when use is 'other'
- time-ranges is required when not closed
- open-time and close-time must be in HH:MM format
- close-time must be after open-time within same time range

## Non residential floorspace

Details of changes to non-residential floorspace in the proposed development.

**Non residential floorspace module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| non-residential-change-outline | Non residential change | Does the proposal involve the loss, gain, or change of non-residential floorspace? | MUST | Select from the **yes-no-unknown** enum. this is only used in outline applications where unknown is an option |
| floorspace-details-outline | Floorspace details[]{} | List of non-residential floorspace changes by use class. | MAY | Rule: is a MUST if `non-residential-change-outline` is `True`. This field is used solely for outline applications |
| room-details-outline | Room details[]{} | List of room changes for hotels, residential institutions and hostels | MAY | Required if change to hotels, residential institutions and hostel floorspace (C1, C2, C2A use classes). Only for outline applications. |


**Floorspace details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | 
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
existing-gross-floorspace | Existing gross floorspace | Existing gross internal floorspace, in sqm | MUST | 
is-floorspace-lost-known | Is floorspace lost known | Whether the amount of floorspace to be lost is known | MAY | 
floorspace-lost | Floorspace lost | Gross floorspace to be lost by change of use, in sqm | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-floorspace-lost-known` is `True`
is-total-gross-proposed-known | Is total gross proposed known | Whether the total gross proposed floorspace is known | MAY | 
total-gross-proposed | Total gross proposed | Total gross internal floorspace proposed, in sqm | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-total-gross-proposed-known` is `True`
net-additional-floorspace | Net additional floorspace | Net additional gross internal floorspace, in sqm | MUST | Calculated as total-gross-proposed - existing-gross-floorspace. This should be calculated automatically


**Room details component**

field | name | description | required | notes
-- | -- | -- | -- | --
use-class-accommodation | Use class for accommodation | Type of non-residential use class referring to accommodation uses | MUST | Select from the **use-class-accommodation** enum. Only required for C1, C2, C2A, or Other use classes. Used to indicate gain or loss in room counts

use-other | Use other | Specify use if use is "other" | MAY | Rule: is a MUST if `use-class-accommodation` is `other`. Required if use is "other"
not-applicable | Not applicable | Whether the facility is not applicable | MAY | 
is-existing-rooms-lost-known | Is existing rooms lost known | Whether the total existing rooms that will be lost is known | MAY | 
existing-rooms-lost | Existing rooms lost | Existing rooms to be lost by change of use | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-existing-rooms-lost-known` is `True`. Must be 0 or positive
is-total-rooms-proposed-known | Is total rooms proposed known | Whether the total rooms proposed is known | MAY | 
total-rooms-proposed | Total rooms proposed | Total rooms proposed (including change of use) | MAY | Rule: is a MUST if `not-applicable` is `False`. Rule: is a MUST if `is-total-rooms-proposed-known` is `True`. Must be 0 or positive
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

Details of pre-application advice previously received from the planning authority

**Pre-application advice module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Pre-application advice sought | Whether pre-application advice has been sought from the planning authority | MUST |  |
| officer-name | Officer name | Name of the planning officer who provided the pre-application advice | MAY | Rule: is a MUST if `advice-sought` is `True` |
| reference | Reference | A unique reference for the data item | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-date | Advice date | Date when pre-application advice was received, in YYYY-MM-DD format | MAY | Rule: is a MUST if `advice-sought` is `True` |
| advice-summary | Advice summary | Summary of the pre-application advice received from the planning authority | MAY | Rule: is a MUST if `advice-sought` is `True` |



## Processes machinery waste

How waste will be managed on the site

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

What development, works or change of use is proposed

**Description of the proposal module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposal-description | Proposal description | A description of what is being proposed, including the development, works, or change of use | MUST |  |
| reserved-matters | Reserved matters[] | Identifies which reserved matters are being submitted for approval as part of this application | MUST | Select from the **reserved-matter-type** enum |
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

## Site area

How big the site is including relevant measurements

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

### Day type

| reference | name | description |
| --- | --- | --- |
| monday-friday | Monday to Friday |  |
| saturday | Saturday |  |
| sunday | Sunday |  |
| bank-holiday | Bank holiday |  |

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

### Use class for accommodation

| reference | name | description | notes | entry-date | start-date | end-date |
| --- | --- | --- | --- | --- | --- | --- |
| c1 | C1 – Hotels | Includes hotels, boarding houses, and guest houses. |  | 2025-10-27 |  |  |
| c2 | C2 – Residential Institutions | Care homes, hospitals, and boarding schools. |  | 2025-10-27 |  |  |
| c2a | C2A – Secure Residential Institutions | Prisons, young offender institutions. |  | 2025-10-27 |  |  |
| other | Other (Please Specify) | Free text required if selected. |  | 2025-10-27 |  |  |

### User role type

| reference | name | description |
| --- | --- | --- |
| agent | Agent | A professional agent working for the applicant |
| proxy | Proxy | An individual working on behalf of the applicant but not in a professional capacity |

### Waste management type

| reference | name | description |
| --- | --- | --- |
| inert-landfill | Inert Landfill | Disposal site for inert waste materials. |
| non-hazardous-landfill | Non-Hazardous Landfill | Landfill for non-hazardous waste. |
| hazardous-landfill | Hazardous Landfill | Landfill site for hazardous waste. |
| energy-waste-incineration | Energy from Waste Incineration | Incineration facility generating energy from waste. |
| other-incineration | Other Incineration | Non-energy-producing incineration sites. |
| landfill-gas-plant | Landfill Gas Generation Plant | Plant generating energy from landfill gas. |
| pyrolysis-gasification | Pyrolysis/Gasification | Facilities using pyrolysis or gasification processes. |
| metal-recycling | Metal Recycling Site | Site for recycling metals. |
| transfer-stations | Transfer Stations | Facilities for sorting and transferring waste. |
| mrf | Material Recovery Facility (MRF) | Facility for sorting recyclable materials. |
| household-amenity-site | Household Civic Amenity Sites | Public waste disposal sites for households. |
| open-windrow-composting | Open Windrow Composting | Outdoor composting of biodegradable waste. |
| in-vessel-composting | In-Vessel Composting | Enclosed composting for controlled conditions. |
| anaerobic-digestion | Anaerobic Digestion | Plant for organic waste decomposition without oxygen. |
| mbt | Mechanical, Biological, or Thermal (MBT) | Combined waste treatment facility. |
| sewage-treatment | Sewage Treatment Works | Plant for treating wastewater. |
| other-treatment | Other Treatment | Any other waste treatment not listed. |
| construction-recycling | Recycling Facilities for Construction Waste | Sites recycling construction and demolition waste. |
| waste-storage | Storage of Waste | Facilities for storing waste before processing. |
| other-waste-management | Other Waste Management | Any other waste management facility not listed. |
| other-developments | Other Developments | Any other related developments. |
