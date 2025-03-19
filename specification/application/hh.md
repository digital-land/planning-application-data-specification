# Householder planning application

A simplified process for applications to alter or enlarge a single house (but not a flat), including works within the boundary/garden

## Contents

Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Authority employee / member](#authority-employee-member-conflict-of-interest)
* [Biodiversity net gain](#biodiversity-net-gain-bng)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of the proposal](#description-of-the-proposal-proposal-details)
* [Materials](#materials-materials)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration-ownership-certs)
* [Parking](#parking-parking)
* [Pedestrian and vehicle access, roads and rights of way](#pedestrian-and-vehicle-access-roads-and-rights-of-way-access-rights-of-way)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Site address details](#site-address-details-site-details)
* [Site visit](#site-visit-site-visit)
* [Trees and hedges](#trees-and-hedges-trees-hedges)

---

## Modules

These modules are all required for this application type

### Agent contact details (agent-contact)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| email | Email used to contact agent | | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

---

### Agent name and address (agent-details)


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| title | Title of individual | | MAY |  |
| first-name | First name of the individual | | MUST |  |
| last-name | last name of the individual | | MUST |  |
| company | company agent works for | | ? | |
| address-text | The address that can be used to correspond with the agent | | MAY | |
| post-code | The post code for the address provided | | MAY | |
| email | Email used to contact agent | pip | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | pip | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | pip | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Applicant contact details (applicant-contact)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| email | Email used to contact applicant | | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact applicant | | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

---

### Applicant name and address (applicant-details)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| title | Title of individual | | MAY |  |
| first-name | First name of the individual | | MUST |  |
| last-name | last name of the individual | | MUST |  |
| address-text | The address that can be used to correspond with the applicant| | MAY | |
| post-code | The post code for the address provided | | MAY | |
| email | Email used to contact agent | pip | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | pip | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | | pip | MAY | is this still necessary? |

We should decide if one combined module makes sense for all forms (issue #23)

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Let user set which is the primary number to use | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Authority employee / member (conflict-of-interest)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | True or False based on statements in "With respect to the Authority, I am" list | | MUST | answer may be different depending on the parties involved |
| name | name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how you are related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST. |

---

### Biodiversity net gain (bng)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| bng-exempt | Flag true for householder, false otherwise | | MUST | |

---

### Checklist (checklist)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type |  | MUST |  |

---

### Declaration (declaration)

| field | description | application-types |
| --- | --- | --- |
| name | A name of the person making the declaration |  |
| declaration-confirmed | `true` or `false` based on answer | |
| declaration-date | the date, in YYYY-MM-DD format, the person made the declaration | |

---

### Description of the proposal (proposal-details)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters-for-approval | Select one or more from reserved-matters ENUM | outline;reserved-matters | MUST | for outline (all) would expect all to be expected |
| related-proposal | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | True or False | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | True or False | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | True or False | full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided |

---

### Materials (materials)

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| building-element[] | Each of the categories listed in the Materials section | | MUST | see building element structure |
| additional-material-information | True or False | | MUST | |
| document-reference[] | | | MAY | Rule: complete if `additional-information` is True |

**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| building-element-type | one from [building element types lenum](https://github.com/digital-land/planning-application-data-specification/discussions/207) | | MUST | |
| existing-materials | | | MAY | if applicable |
| proposed-materials | | | MAY | if applicable |
| materials-not-applicable | True or False | | MAY | MUST if `existing-materials` and `proposed-materials` not filled out |
| materials-not-known | True or False | | MAY | MUST if `existing-materials` and `proposed-materials` not filled out |

---

### Ownership certificates and agricultural land declaration (ownership-certs)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
sole-owner | Is the applicant the sole owner of the land? (True/False) |   | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |   | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[] | List of known owners and agricultural tenants |   | MAY | Required for Certificate-B or Certificate-C.
steps-taken | Steps taken to identify unknown owners or tenants |   | MAY | Required for Certificate-C or Certificate-D.
newspaper-notice | Newspaper notice details for unknown owners/tenants |   | MAY | Required for Certificate-C or Certificate-D.
ownership-cert-option | Ownership certificate type based on ownership and tenancy |   | MUST | Enum: Certificate-A, Certificate-B, Certificate-C, Certificate-D. Determined by applicant or system?
applicant-signature | Signature of the applicant |   | MAY |  
agent-signature | Signature of the agent (if applicable) |   | MAY |  
signature-date | Date of applicant or agent signature |   | MUST | Format: YYYY-MM-DD.

**Owners and tenants**

Requires the Person model

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person | Owner or tenant details | Person model | MUST | Reuse existing Person model.
notice-date | Date notice was served | Date | MUST | Format: YYYY-MM-DD.

**Newspaper notice**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
newspaper-name | Name of the newspaper | String | MUST |  
publication-date | Date of publication | Date | MUST | Format: YYYY-MM-DD.

---

### Parking (parking)

| field | description | application-types |
| --- | --- | --- |
| description | A description of how the proposed works will affect existing car parking arrangements | hh |

---

### Pedestrian and vehicle access, roads and rights of way (access-rights-of-way)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | True or False if a new or altered vehicle access is proposed to or from the public highway | extraction-oil-gas;full;hh;outline | MUST | for outline apps answer can be "unknown" |
| new-altered-pedestrian | True or False if a new or altered pedestrian access is proposed to or from the public highway | extraction-oil-gas;full;hh;outline | MUST | for outline apps answer can be "unknown" |
| change-right-of-way | True or False if the proposals require any diversions/extinguishments and/or creation of rights of way | full;hh;outline | MUST | for outline apps answer can be "unknown" |
| new-right-of-way | True or False if there any new public rights of way to be provided within or adjacent to the site | extraction-oil-gas;full;outline | MUST | for outline apps answer can be "unknown" |
| new-public-road | True or False if there any new public roads to be provided within the site | extraction-oil-gas;full;outline | MUST | for outline apps answer can be "unknown" |
| temp-right-of-way | True or False if the proposals require any diversions/extinguishments and/or creation of rights of way whilst the site is being worked | extraction-oil-gas | MUST | for outline apps answer can be "unknown" |
| future-new-right-of-way | True or False if there any new public rights of way to be provided with or adjacent to the site after extraction | extraction-oil-gas | MUST | for outline apps answer can be "unknown" |
| document-reference[] | References for associated documents | extraction-oil-gas;full;hh;outline | MAY | MUST if true for any other answer |

---

### Pre-application advice (pre-app-advice)


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | a flag indicating if pre-application advice has been sought |  | MUST | is this inferrable from other information provided? |
| officer-name | name of officer who dealt with pre-app advice | | MAY | |
| reference | reference for pre-application advice application | | MAY | |
| advice-date | date applicant received the advice | | MAY | |
| advice-summary | summary of the advice received | | MAY | is this necessary if they have provided the reference? |

---

### Site address details (site-details)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-boundary | Geometry of the site of the development | | MUST | online services can send the boundary supplied by the applicant/agent. Paper forms would need one of the other fields translated into this |
| address | address, if available for the site | | MAY | does the address need to be structured data or a blob of text like in some app forms? |
| easting | grid reference | | MAY | |
| northing | grid reference | | MAY | |
| latitude | Latitude coordinate in EPSG:4326 (WGS84) | | MAY | |
| longitude | Longitude coordinate in EPSG:4326 (WGS84) | | MAY | |

### Rules

Applicant/agent must provide one of:
* site-boundary
* address
* easting + northing

---

### Site visit (site-visit)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-seen-from | Flag if site be seen from a public road  public footpath  bridleway or other public land | | MUST | Indicates whether a site visit can be done without arranging access |
| contact-name | Name of person to contact | | MUST | |
| contact-number | Phone number of person to contact | | MUST | |
| contact-email | Email of person to contact | | MUST | |

Does the authority primarily need to know who to contact for a site visit or do they categorically need to know if the person to contact is neither the applicant or the agent?

---

### Trees and hedges (trees-hedges)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| falling-trees-risk | True or false. Need to know if falling trees on-premises or adjacent premises are a risk to the development | hh | | |
| falling-trees-document | reference to document showing location of trees | hh | | |
| tree-removal | True or False. Need to know if plans need trees or hedges to be pruned or removed | hh | | |
| tree-removal-document | reference of document showing location of trees and hedges | hh | | |
| trees-on-site | Trees or hedges are on the proposed development site (true / false ) | full;outline-some;extraction-oil-gas | MUST | |
| trees-on-adj-land | Trees or hedges on land adjacent to the proposed development site that could influence the development or might be important as part of the local landscape character (true / false) | full;outline-some;extraction-oil-gas | MUST | |

---


## Required codelists

The following codelists are required by modules in this application type:

### Building element type (building-element-type)

A set of building elements that applicants are expected to provide material information for

| reference | name | application-types | 
| --- | --- | -- |
| walls | Walls | advertising;demolition-con-area;full;hh;outline |
| roof | Roof | advertising;demolition-con-area;full;hh;outline |
| windows | Windows | advertising;demolition-con-area;full;hh;outline |
| doors | Doors | advertising;demolition-con-area;full;hh;outline |
| boundary-treatments | Boundary treatments | advertising;demolition-con-area;full;hh;lbc;outline |
| vehicle-access-hard-standings | Vehicle access and hard-standings | advertising;demolition-con-area;full;hh;lbc;outline |
| lighting | Lighting | advertising;demolition-con-area;full;hh;lbc;outline |
| external-walls | External walls | lbc |
| roof-covering | Roof covering | lbc |
| chimney | Chimney | lbc |
| external-doors | External doors | lbc |
| ceilings | Ceilings | lbc |
| internal-walls | Internal walls | lbc |
| floors | Floors | lbc |
| internal-doors | Internal doors | lbc |
| rainwater-goods | Rainwater goods | lbc |
| other | Other | advertising;demolition-con-area;full;hh;lbc;outline |

---

### Contact priority (contact-priority)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

---

