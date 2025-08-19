# Notification of proposed works to trees in a conservation area

Notification, 6 weeks prior to works being carried out, of proposed works to a tree in a conservation area that is not subject to a Tree Preservation order

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
* [Trees additional information](#trees-additional-information)
* [Trees location](#trees-location)
* [Trees ownership](#trees-ownership)
* [Identification of tree(s) and description of works](#identification-of-tree(s)-and-description-of-works)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |
| application | The details of the application payload to be submitted | object | MUST |  |

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

## Trees additional information

Additional information about trees on the site, including condition concerns, 
damage reports, and supporting documentation


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| advice-from-authority | Advice from authority | Any advice provided on-site by a Local Planning Authority (LPA) officer | MAY |  |
| supporting-documents | Supporting documents[]{} | Documents supporting the work required to trees | MUST |  |


**Supporting document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 

**Validation rules**

- If condition-concerns is true then Arboricultural impact assessment document is required
- If causing-subsidence is true then Subsidence Report is required
- If causing-structural-damage is true then a Structural damage report is required
- supporting-documents must include sketch plan, supporting documents, reports, or photographs
- supporting-documents must include any documents required based on condition concerns, subsidence, or structural damage

## Trees location

Location information for trees affected by the proposed works, required when the site is different from the applicant's address


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-site-different | Is site different | Whether the site where trees are located is different from the applicant's address | MUST |  |
| site-locations | Site locations[]{} | Details of the sites on which the tree(s) are located | MAY | Rule: is a MUST if `is-site-different` is `True` |


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

- site-locations only required if the site is different from the applicant's address
- At least one location method must be provided per site: site-boundary, address-text, or easting+northing
- If easting is provided, northing must also be provided and vice versa
- Online services can send the boundary supplied by the applicant/agent
- Paper forms would need other fields translated into site-boundary

## Trees ownership

Information about ownership of trees affected by the proposed works


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-applicant-owner | Is applicant owner | Whether the applicant owns the trees affected by the proposed works | MUST |  |
| owner | Tree owner[]{} | Details of the tree owner when applicant is not the owner | MAY | Rule: is a MUST if `is-applicant-owner` is `False` |


**Tree owner model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Detail to help identify a person | MUST | 
contact-details | Contact details{} | A structured object containing contact information for an individual. This component is required for planning in principle (PiP) applications and optional for other application types. Contains email and phone contact information. | MAY | 


**Person obj model**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 


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

- owner details required when is-applicant-owner is false

## Identification of tree(s) and description of works

Details of trees and proposed work to them, including identification, 
species and work descriptions


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| description | Description | Description of work applicant wishes to carry out, including identifying the trees, species and setting out the work | MUST |  |
| tree-details | Tree details[]{} | Details of each tree that is part of the proposal | MAY |  |


**Tree details model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
species | Species | The species of the tree | MAY | 
description-of-works | Description of works | Description of the nature of the work to be carried out on this tree | MAY | 

**Validation rules**

- Tree identifiers should use TPO reference numbers where applicable
- Description must include tree identification, species and work details

## Required codelists

This are the codelist required to support this specification:

- contact-priority
- user-role-type