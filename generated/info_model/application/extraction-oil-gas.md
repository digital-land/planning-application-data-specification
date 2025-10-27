# Development relating to the onshore extraction of oil and gas

Development relating to the onshore extraction of oil and gas
(including exploratory, appraisal and production phases) and the associated
plans, documents and validation information required to support an
application.


## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Access and rights of way](#access-and-rights-of-way)
* [Agent contact details](#agent-contact-details)
* [Agent details](#agent-details)
* [Applicant contact details](#applicant-contact-details)
* [Applicant details](#applicant-details)
* [Biodiversity, geological and archaeological conservation](#biodiversity,-geological-and-archaeological-conservation)
* [Checklist](#checklist)
* [Conflict of interest](#conflict-of-interest)
* [Declaration](#declaration)
* [Designated areas](#designated-areas)
* [Development type](#development-type)
* [Employment](#employment)
* [Equipment and method](#equipment-and-method)
* [Existing use](#existing-use)
* [Flood risk assessment](#flood-risk-assessment)
* [Foul sewage disposal](#foul-sewage-disposal)
* [Hazardous substances](#hazardous-substances)
* [Hours of operation](#hours-of-operation)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration)
* [Plans, drawings and supporting materials](#plans,-drawings-and-supporting-materials)
* [Pre-application advice](#pre-application-advice)
* [Site details](#site-details)
* [Site ownership](#site-ownership)
* [Site Visit Details](#site-visit-details)
* [Storage facilities](#storage-facilities)
* [Trade effluent](#trade-effluent)
* [Trees and hedges information](#trees-and-hedges-information)
* [Types application](#types-application)
* [Voluntary agreement](#voluntary-agreement)

### Codelists

* [Contact priority](#contact-priority)
* [Day type](#day-type)
* [Hazardous substance type](#hazardous-substance-type)
* [Use class](#use-class)
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

## Access and rights of way

Details of any changes the proposed development would make to existing access arrangements or public rights of way

**Access and rights of way module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | New or altered vehicle access | Is a new or altered vehicle access proposed to/from the public highway | MUST | Select from the **rights-of-way-answer** enum |
| new-altered-pedestrian | New or altered pedestrian access | Is a new or altered pedestrian access proposed to/from the public highway | MUST | Select from the **rights-of-way-answer** enum |
| new-right-of-way | New right of way | Will new public rights of way be provided within or adjacent to the site | MUST | Select from the **rights-of-way-answer** enum |
| new-public-road | New public road | Will new public roads be provided within the site | MUST | Select from the **rights-of-way-answer** enum |
| temp-right-of-way | Temporary right of way changes | Are temporary changes to rights of way needed while the site is worked | MUST | Select from the **rights-of-way-answer** enum |
| future-new-right-of-way | Future new right of way | Will new public rights of way be provided after extraction? | MUST | Select from the **rights-of-way-answer** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used | MAY |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 

**Validation rules**

- All fields must use values from rights-of-way-answers codelist
- If new-altered-vehicle is yes, details must be provided in highways module
- If change-right-of-way is yes, separate rights of way order may be needed
- If temp-right-of-way is yes, details of temporary diversions must be provided

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

## Biodiversity, geological and archaeological conservation

Details of potential impacts to the biodiversity of the site, or any noteable archaeological or geological features.

**Biodiversity, geological and archaeological conservation module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| protected-species-impact | Protected species impact | Where is there a likelihood of protected and priority species being affected? | MUST | Select from the **affected-area-type** enum |
| biodiversity-features-impact | Biodiversity features impact | Where is there a likelihood of important habitats or biodiversity features being affected? | MUST | Select from the **affected-area-type** enum |
| geological-features-impact | Geological features impact | Where is there a likelihood of features of geological conservation importance being affected? | MUST | Select from the **affected-area-type** enum |
| archaeological-features-impact | Archaeological features impact | Where is there a likelihood of features of archaeological conservation importance being affected? | MUST | Select from the **affected-area-type** enum |

**Validation rules**

- All impact assessments must use values from the affect-area codelist or 'no'
- Archaeological features impact is only required for extraction-oil-gas applications
- Impact assessments should be based on ecological surveys and site assessments

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

## Designated areas

Details of any 'designated area' the develpoment site is on, such as a Conservation Area or National Park.

**Designated areas module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| designations | Designations[] | List of designated areas that apply to the site | MUST | Select from the **designation** enum |

**Validation rules**

- Multiple selections allowed from the designation codelist
- If none of the designated areas apply to the site, the array should be empty
- Each designation in the array must be unique (no duplicates)

## Development type

Supporting information for developments used for oil and gas exploration or mining 

**Development type module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| development-phase | Development phase | Phases of oil and gas development the application covers | MUST | Select from the **development-phase** enum |
| development-description | Development description | Brief description of the development, including main oils, gases, and machinery | MUST |  |
| quantity-cubic-metres | Quantity cubic metres | Quantity of oil or gas involved in cubic metres | MUST |  |
| permission-period-years | Permission period years | Period of permission sought in years | MAY |  |
| hydrocarbon-licence-block | Hydrocarbon licence block | Hydrocarbon licence block where the development is located | MUST | Typically an identifier like "PEDL123" |
| surface-site-area-hectares | Surface site area hectares | Surface site area in hectares | MAY | could this be calculated from the site boundary? |
| site-hectares-provided-by | Site hectares provided by | Who provided the site hectares value (applicant or system) | MAY | Select from the **provided-by** enum |
| environmental-statement | Environmental statement | Is an Environmental Statement attached to the application | MUST |  |
| environmental-statement-reference | Environmental statement reference | Reference to the environmental statement document | MAY | Rule: is a MUST if `environmental-statement` is `True` |

**Validation rules**

- development-phase must contain at least one value from development-phases codelist
- quantity-cubic-metres must be a positive number
- surface-site-area-hectares must be a positive number
- environmental-statement-reference is required when environmental-statement is true
- environmental-statement-reference must reference a valid document in the application
- hydrocarbon-licence-block typically follows format PEDL123

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

## Equipment and method

How oil and gas will be extracted as part of the proposed development.

**Equipment and method module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| equipment-plan | Equipment plan | Details of equipment to be used as part of the application including the maximum height and type of drilling rig to be used | MUST |  |

**Validation rules**

- Equipment-plan must include details of equipment types and specifications
- For drilling operations, maximum height and type of drilling rig must be specified
- This module is only applicable to extraction-oil-gas applications

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

## Foul sewage disposal

How waste water will leave the property as part of the proposed development

**Foul sewage disposal module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| has-new-disposal-arrangements | Has new disposal arrangements | Does the proposal include any new foul sewage disposal arrangments | MUST |  |
| foul-sewage-disposal-types | Foul sewage disposal types[] | List of ways foul sewage will be disposed of | MAY | Select from the **foul-sewage-disposal-type** enum |
| produce-foul-sewage | Produce foul sewage | Whether the proposed development will produce any foul sewage | MUST |  |
| connect-to-drainage-system | Connect to drainage system | Whether the proposal needs to connect to the existing drainage system | MUST |  |
| drainage-system-details | Drainage system details | Details of the drawings/plans that show the existing drainage system | MAY |  |

**Validation rules**

- if connect-to-drainage-system == true then drainage-system-details is required
- if application-type includes 'extraction-oil-gas' then drainage-system-details is required

## Hazardous substances

What hazardous substances may be used as part of the development

**Hazardous substances module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| involves-hazardous-substances | Involves hazardous substances | Indicates if hazardous substances are involved in the proposal | MUST | Select from the **yes-no-not-applicable** enum |
| substance-types | Substance types[]{} | List of hazardous substances and their quantities | MAY | Rule: is a MUST if `involves-hazardous-substances` is `yes` |
| hazardous-sub-consent-req | Hazardous substance consent required | Does the proposal involve the use or storage of any substances requiring hazardous substances consent | MUST |  |
| hazardous-sub-consent-details | Hazardous substance consent details | Details of hazardous substance consent requirements | MAY | Rule: is a MUST if `hazardous-sub-consent-req` is `True` |


**Hazardous substance component**

field | name | description | required | notes
-- | -- | -- | -- | --
hazardous-substance-type | Hazardous substance type | Reference of hazardous substance type from predefined list | MUST | Select from the **hazardous-sub-type** enum
hazardous-substance-other | Hazardous substance other | The specific name of the hazardous substance if other is selected | MAY | Rule: is a MUST if `hazardous-substance-type` is `other`
amount | Amount | The total amount due for the application fee | MUST | 

**Validation rules**

- if involves-hazardous-substances == 'yes' then substance-types is required
- if hazardous-sub-consent-req == true then hazardous-sub-consent-details is required
- if hazardous-substance-type == 'other' then name is required
- amount > 0

## Hours of operation

Proposed operating hours if the proposed development is intended for non-residential use.

**Hours of operation module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation | Hours of operation[]{} | List the hours of operation by non-residential use | MUST |  |
| additional-information | Additional information | Any additional information (such as hours of use of other machinery within the site-generators, pumps, etc) | MAY |  |


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



## Plans, drawings and supporting materials

Additional materials and specifications that form part of the planning application

**Plans, drawings and supporting materials module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| plans-documents | Plans documents[]{} | List of plans, drawings, and supporting documents | MUST |  |
| inspection-address | Inspection address | Full postal address where supporting material can be inspected | MUST | Should this be the address-text field |


**Plans document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference-number | Reference number | Unique identifier for the document | MUST | 
name | Name | Name of the document (descriptive) | MUST | 

**Validation rules**

- plans-documents.length >= 1
- plans-documents[].reference-number must be unique
- plans-documents[].name.length > 0
- inspection-address must include street, town/city, and postcode

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

## Site ownership

For oil and gas extraction developments, who owns or has an interest in the site.

**Site ownership module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| site-owner | Site owner{} | Details of the owner of the development site | MUST |  |
| applicant-interest | Applicant interest | Description of the applicant's interest in the land | MUST |  |
| applicant-interest-adjoining-land | Applicant interest adjoining land | Description of the applicant's interest in the adjacent land | MUST |  |


**Site owner component**

field | name | description | required | notes
-- | -- | -- | -- | --
fullname | Full name | The complete name of a person | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 



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

## Storage facilities

For oil and gas extraction developments, how chemicals will be stored

**Storage facilities module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| storage-facilities-description | Storage facilities description | Details and proposed facilities for the storage of oil, fuel and chemicals and the proposed means of their protection | MUST |  |



## Trade effluent

Details of any liquid waste produced by industial processes on the proposed site, and how it will be diposed of.

**Trade effluent module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-disposal-required | Disposal required | Does the proposal involve the disposal of trade effluents or waste (true/false) | MUST |  |
| description | Description | describe the nature, volume and means of disposal of trade effluents or waste | MAY | Rule: is a MUST if `disposal-required` is `True` |

**Validation rules**

- description is required when disposal-required is true
- Module applies to full, extraction-oil-gas, and outline application types

## Trees and hedges information

Details of trees and/or hedges that will be affected by the proposed development

**Trees and hedges information module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| trees-on-site | Trees on site | Whether trees or hedges are present on the proposed development site | MUST |  |
| trees-on-adj-land | Trees on adjacent land | Whether trees or hedges on land adjacent to the proposed development site could influence the development or might be important as part of the local landscape character | MUST |  |

**Validation rules**

- falling-trees-document reference must match a document in application.documents
- tree-removal-plan reference must match a document in application.documents

## Voluntary agreement

Details of any voluntary agreements made as part of an oil and gas extraction application.

**Voluntary agreement module**

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| draft-agreement-included | Draft agreement included | Has an outline or draft agreement been included? (True / False) | MUST |  |
| agreement-summary | Agreement summary | Summary of the agreement | MAY | Rule: is a MUST if `draft-agreement-included` is `True` |

**Validation rules**

- agreement-summary is required when draft-agreement-included is true
- Module only applies to extraction-oil-gas application types

## Required codelists

Below are the codelists required to support this specification:

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

### Hazardous substance type

| reference | name | description |
| --- | --- | --- |
| acrylonitrile | Acrylonitrile |  |
| ammonia | Ammonia |  |
| bromine | Bromine |  |
| chlorine | Chlorine |  |
| ethylene-oxide | Ethylene oxide |  |
| flour | Flour |  |
| hydrogen-cyanide | Hydrogen cyanide |  |
| liquid-oxygen | Liquid oxygen |  |
| liquid-petroleum-gas | Liquid petroleum gas |  |
| phosgene | Phosgene |  |
| refined-white-sugar | Refined white sugar |  |
| sulphur-dioxide | Sulphur dioxide |  |

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

### User role type

| reference | name | description |
| --- | --- | --- |
| agent | Agent | A professional agent working for the applicant |
| proxy | Proxy | An individual working on behalf of the applicant but not in a professional capacity |
