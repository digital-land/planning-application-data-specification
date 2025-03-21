# Outline planning

Applications that are used to understand whether the basic nature of a development is viable

## Sub-type: Outline Planning Permission with All Matters Reserved

## Contents

Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [All types of development: Non-residential floorspace](#all-types-of-development-non-residential-floorspace-non-res-floorspace)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Assessment of flood risk](#assessment-of-flood-risk-flood-risk-assessment)
* [Authority employee / member](#authority-employee-member-conflict-of-interest)
* [Biodiversity net gain](#biodiversity-net-gain-bng)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Description of the proposal](#description-of-the-proposal-proposal-details)
* [Employment](#employment-employment)
* [Existing use](#existing-use-existing-use)
* [Hours of operation](#hours-of-operation-hrs-operation)
* [Industrial or commercial processes and machinery](#industrial-or-commercial-processes-and-machinery-processes-machinery-waste)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration-ownership-certs)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Residential units (including conversion)](#residential-units-including-conversion-res-units)
* [Site address details](#site-address-details-site-details)
* [Site area](#site-area-site-area)
* [Site visit](#site-visit-site-visit)

---

## Application data specification

field	| description	| data-type | required | notes
--- | --- | --- | --- | ---
reference | UUID for the application record | UUID | MUST | 
application-types[] | A list of planning application types | Enum | MUST | See [list of application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)
application-sub-type | Sub-category of the application | Enum | See [list of application sub-types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv)
planning-authority | The reference of the planning authority the application has been submitted to | Organisation reference | MUST | 
submission-date | Date the application is submitted. In `YYYY-MM-DD` format |	Date | MUST |	
modules[] | List of required sections/modules for this application | List |	MUST | List of predefined module references that can be used to validate the application
documents[]{} | List of submitted documents | List | MUST |	Uses a document model to capture references and details.

**Document structure**

field | description | required | notes
--- | --- | --- | ---
reference | A reference for the document | MUST | This should be unique
name | The name or title of the document | MUST | 
description | Brief description of what the document contains	| MAY | Optional but useful for context
document-types[] | List of codelist references that the document covers | MUST | Use the planning requirements enum
file | The digital file or a reference to where the file is stored | MUST | Object / URL / Blob
mime-type | The document's MIME type | MAY | e.g., application/pdf, image/jpeg

---

## Modules

These modules are all required for this application type

### Agent contact details (agent-contact)

Details needed for contacting the agent

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| Contact-details{} | Details of how to contact the individual | | MAY | Rule: is a MUST if `application-type` is `pip` |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the individual | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Agent name and address (agent-details)

Details about the agent

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent{} | Details of the agent | | MUST | |

**Agent object**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| company | The company the agent works for | | MAY | |
| Contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact agent | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### All types of development: Non-residential floorspace (non-res-floorspace)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
non-residential-change | Does the proposal involve the loss, gain, or change of non-residential floorspace? |   | MUST | Boolean (Yes / No).
floorspace-details[]{} | List of non-residential floorspace changes by use class |   | MAY | Required if non-residential-change is Yes.
room-details[] | List of room changes for hotels, residential institutions and hostels | | MAY | Required if change to hotels, residential institutions and hostel floorspace |

**Floorspace details**


Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
use-class | Type of non-residential use class | Enum | MUST | See [Use Class Enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
specified-use | Specify the use that sits outside the lettered use classes | String | MAY | Rule: is a MUST if `use-class` is `other` or `sui generis`
existing-gross-floorspace | Existing gross internal floorspace (sqm) | Number | MUST | Must be 0 or positive.
floorspace-lost | Gross floorspace to be lost by change of use (sqm) | Number | MUST | Must be 0 or positive.
total-gross-proposed | Total gross internal floorspace proposed (sqm) | Number | MUST | Must be 0 or positive.
net-additional-floorspace | Net additional gross internal floorspace (sqm) | Number | MUST | Calculated as total-gross-proposed - existing-gross-floorspace.


**Room details**

For certain use classes (C1, C2, C2A), applicants must provide room details:

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
use-class | Type of non-residential use class | Enum | MUST | Only required for C1, C2, C2A, or Other.
existing-rooms-lost | Existing rooms to be lost by change of use | Number | MUST | Must be 0 or positive.
total-rooms-proposed | Total rooms proposed (including change of use) | Number | MUST | Must be 0 or positive.
net-additional-rooms | Net additional rooms following development | Number | MUST | Calculated as total-rooms-proposed - existing-rooms-lost.

---

### Applicant contact details (applicant-contact)

Details needed for contacting the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| Contact-details{} | Details of how to contact the individual | | MAY | Rule: is a MUST if `application-type` is `pip` |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the individual | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Applicant name and address (applicant-details)

Details about the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicants[]{} | Details for one or more applicants | | MUST | Rules: must be one or more named applicants |

**Applicant object**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| Contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact agent | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact agent | MUST | see Phone number below. Only one number can be set as the primary number |
| fax-number | Fax number used to contact the applicant | MAY | is this still necessary? |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Assessment of flood risk (flood-risk-assessment)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
flood-risk-area | Is the site within an area at risk of flooding? |   | MUST | Boolean True or False
data-provided-by | Who provided the data: Applicant or System/Service? |   | MAY | Enum (Applicant / System/Service).
flood-risk-assessment | Reference of the flood risk assessment document |   | MAY | Required if flood-risk-area is True.
within-20m-watercourse | Is the proposal within 20 metres of a watercourse? |   | MUST | Boolean True or False.
increases-flood-risk | Will the proposal increase the flood risk elsewhere? |   | MUST | Boolean True or False.
surface-water-disposal[] | How will surface water be disposed of? |   | MUST | Multiple options allowed (see [surface water disposal type enum](https://github.com/digital-land/planning-application-data-specification/discussions/195)).


---

### Authority employee / member (conflict-of-interest)

This section ensures transparency by declaring any connection between the applicant or agent and the local authority’s staff or elected members that could present a conflict of interest.

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member  | | MUST | answer may be different depending on the parties involved |
| name | Name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how individual is related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST |

---

### Biodiversity net gain (bng)

This section asks for information to show how the development will protect or improve wildlife habitats on the site, and whether any exemptions or special rules apply.

| field | description | application-types | data-type | required | notes |
| --- | --- | --- | --- | --- | --- |
| bng-exempt | Applicants for planning permission are required to make a statement as to whether they believe the biodiversity gain condition will apply if permission is granted. Householder applicants need to confirm the biodiversity gain condition does not apply. (`true`/`false`) | hh | Boolean | MUST | |
| bng-condition-applies | Does the applicant believe the Biodiversity Gain Condition applies? | full;outline;demolition-con-area | Boolean | MUST | |
| bng-condition-exemption-reason | Reason why BNG does not apply, referencing exemptions or transitional arrangements | full;outline;demolition-con-area | String | MAY | | Rule: Required if `bng-condition-applies` = False |
| bng-details{} | Biodiversity net gain details | full;outline;demolition-con-area | Object | MAY | Rule: is MUST if bng-condition-applies = True |

Rule: if `application-types` includes `hh` (the householder application) then only the `bng-exempt` field is required

**BNG details** structure

Field | Description | Data Type | Required | Notes
--- | --- | --- | --- | ---
pre-development-date | Date of pre-development biodiversity value calculation | Date | MUST | Rule: Must align with application or justified earlier date
pre-development-biodiversity-value | Calculated biodiversity value | Number | MUST | In Habitat Biodiversity Units
earlier-date-reason | Reason for using an earlier pre-development date | String | MAY | If date is earlier than application submission
habitat-loss-after-2020 | Has there been degradation of onsite habitat(s) after 30 Jan 2020? | Boolean | MAY | True/False
habitat-loss-details{} | Details of loss/degradation events | Object | MAY | Required if habitat-loss-after-2020 = True
metric-publication-date | Publication date of the biodiversity metric tool used | Date | MUST | 
irreplaceable-habitats | Does the site contain irreplaceable habitats? | Boolean | MUST | True/False
irreplaceable-habitats-details | Description and references for any irreplaceable habitats | String | MAY | Required if irreplaceable-habitats = True
supporting-documents[]{} | A list of documents supporting the information provided | LIST | MUST | Rules for various required documents can be seen in Planning requirement documents section


**Habitat loss details** structure

Field | Description | Data Type | Required
--- | --- | --- | ---
loss-date | Date the activity causing the loss occurred | Date | MUST
pre-loss-biodiversity-value | Biodiversity value immediately before the activity | Number | MUST
supporting-evidence | Description or reference to supporting documents | String | MAY

**Planning requirement documents**

* Completed biodiversity metric tool - Shows pre-development value and loss if applicable (REQUIRED)
* Habitat plan - Plan showing onsite habitats at the relevant date (REQUIRED)
* Irreplaceable habitat plan - Plan showing onsite irreplaceable habitats (REQUIRED If irreplaceable-habitats = Yes)

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Checklist (checklist)

This section provides details of the national planning requirements the applicant is required to submit along with the application

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type |  | MUST |  |

---

### Declaration (declaration)

Applicants and agents are required to declare information provided is correct

| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | The applicant(s) and agent need to confirm the information provided is correct to the best of their knowledge | | MUST | Boolean - `true` / `false`
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |

---

### Description of the proposal (proposal-details)

Details about the proposal

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters-for-approval[] | Identifies which reserved matters are being submitted for approval as part of this application. | outline;reserved-matters | MUST | See [reserved matter type enum](https://github.com/digital-land/planning-application-data-specification/discussions/209)  |
| related-proposal | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | A description of what is being proposed, including the development, works, or change of use. | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | Has any work on the proposal has already started. (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | The date when work on the proposal started. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | Has the development or works have already been completed (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | The date when the development or works were completed. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | (`true`/`false`)| full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided | |

---

### Employment (employment)

Please complete the following information regarding employees

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-employees{} | Counts of existing employees |   | MUST | Required for all non-residential applications.
proposed-employees | Counts of proposed employees |   | MUST | Required if the proposal affects employment capacity.
employment-impact | Summary of net employment change (gain/loss) |   | MAY | Calculated based on existing and proposed values.

**Employees**
Field | Description | Notes
-- | -- | --
full-time | Number of full-time employees | Must be a positive integer or 0.
part-time | Number of part-time employees | Must be a positive integer or 0.
fte | Total full-time equivalent (FTE) | Calculated as full-time + (part-time ÷ 2).

---

### Existing use (existing-use)

_To do: add description for module_

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-use-details | Describe the current use of the site |   | MUST | 
site-vacant | True or False | | MUST | 
last-use-details | Describe the last use of the site | | MAY | Rule, is a MUST if `site-vacant` is True 
last-use-end-date | Date the last use ended (YYYY-MM-DD format) | | MAY | Rule, is a MUST if `site-vacant` is True 
is-contaminated-land | Is the site known to be contaminated? (True/False) | | MUST | 
is-suspected-contaminated-land | Is the site suspected of contamination? (True/False) | | MUST | 
proposed-use-contamination-risk | Is the proposed use vulnerable to the presence of contamination? (True/False) | | MUST |
contamination-assessment | Reference to contamination assessment document | | MAY | Is a MUST if `is-contaminated-land`, `is-suspected-contaminated-land` or `proposed-use-contamination-risk` is True

---

### Hours of operation (hrs-operation)

Please state the hours of opening for each non-residential use proposed:

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation[]{} | State the hours of opening for each non-residential use | | MUST | |
| additional-information | | extraction-oil-gas | MAY | |

**hours of operation**
| field | description | required | notes |
| --- | --- | --- | --- |
| non-residential-use | | MUST | Should this be a use class? |
| opening-times[]{} | Structured data for opening hours by day | MAY | one of `hours-of-operation` or `hours-unknown` must be completed |
| hours-unknown | Applicant states they do not know the hours of operation | MAY | one of `hours-of-operation` or `hours-unknown` must be completed |

**Opening times**
| field | description | notes |
| --- | --- | --- |
| day-type | Day of the week | One of [day-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/197) |
| open-time | | HH:MM |
| close-time | | HH:MM |
| closed | True or False | If True, `open-time` and `close-time` must be empty. Explicitly state when closed |

---

### Industrial or commercial processes and machinery (processes-machinery-waste)

_To do: add description for module_

Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
site-activity-details | Description of activities, processes, and end products | | MUST | Describe site operations, including plant, ventilation, and machinery.
proposal-waste-management | Whether the proposal involves waste management development | | MUST | True if the proposal includes waste management.
waste-management[] | List of waste management facilities involved | | MAY | MUST if proposal-waste-management is True.
waste-streams{} | Annual throughput for waste streams | | MAY | MUST if proposal-waste-management is True.

**Waste management**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
type | Type of waste management facility | Enum | MUST | See [Waste Management Type Enum](https://github.com/digital-land/planning-application-data-specification/discussions/164)
not-applicable | Whether the facility is not applicable | Boolean | MAY | If True, capacity and throughput are not required.
total-capacity | Total capacity of void in cubic metres (or tonnes/litres) | Integer | MAY | MUST if not-applicable is False.
annual-throughput | Maximum annual operational throughput in tonnes/litres | Integer | MAY | MUST if not-applicable is False.

**Waste streams**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
municipal | Maximum throughput for municipal waste | Integer | MAY | Annual throughput in tonnes/litres.
construction-demolition | Maximum throughput for construction and demolition waste | Integer | MAY | Annual throughput in tonnes/litres.
commercial-industrial | Maximum throughput for commercial and industrial waste | Integer | MAY | Annual throughput in tonnes/litres.
hazardous | Maximum throughput for hazardous waste | Integer | MAY | Annual throughput in tonnes/litres.

---

### Ownership certificates and agricultural land declaration (ownership-certs)

Ownership of the site and/or property for development needs to be understood

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
sole-owner | Is the applicant the sole owner of the land? (True/False) |   | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |   | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[] | List of known owners and agricultural tenants |   | MAY | Required for Certificate-B or Certificate-C.
steps-taken | Steps taken to identify unknown owners or tenants |   | MAY | Required for Certificate-C or Certificate-D.
newspaper-notice | Newspaper notice details for unknown owners/tenants |   | MAY | Required for Certificate-C or Certificate-D.
ownership-cert-option | Ownership certificate type based on ownership and tenancy |   | MUST | See [ownership certificate type enum](https://github.com/digital-land/planning-application-data-specification/discussions/224)
applicant-signature | Signature of the applicant |   | MAY |  
agent-signature | Signature of the agent (if applicable) |   | MAY |  
signature-date | Date of applicant or agent signature |   | MUST | Format: YYYY-MM-DD.

**Owners and tenants**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Owner or tenant details | Person model | MUST | Reuse existing Person model.
notice-date | Date notice was served | Date | MUST | Format: YYYY-MM-DD.

**Newspaper notice**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
newspaper-name | Name of the newspaper | String | MUST |  
publication-date | Date of publication | Date | MUST | Format: YYYY-MM-DD.

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

---

### Pre-application advice (pre-app-advice)

A section for providing details of pre application advice received from the authority


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Has pre-application advice has been sought | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Boolean (`true`/`false`) |
| officer-name | Name of officer who dealt with pre-app advice | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| reference | Reference for pre-application advice application | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-date | Date applicant received the advice, in `YYYY-MM-DD` format | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-summary | Summary of the advice received | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | is this necessary if they have provided the reference? |

---

### Residential units (including conversion) (res-units)

_To do: add description for module_

Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
residential-unit-change | Proposal includes the gain, loss or change of use of residential units (True/False) | | MUST | Could be calculated from answers to next parts?
unit-counts[] | List of unit counts by tenure and housing type | | MAY | Is MUST if `residential-unit-change` is True
total-proposed-units | | | MUST |
total-existing-units | | | MUST |
net-change | Calculated net change in units |  | AUTO | Calculated as proposed-units - existing-units. Format: Integer

**Unit counts**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | One of: market-housing, affordable-rent, home-ownership, starter-homes, custom-build.
housing-type | Type of housing | Enum | MUST | One of: houses, flats-maisonettes, sheltered-housing, bedsit-studio, cluster-flats, other.
unknown-units | Whether the number of units is unknown  | Boolean | MAY | True if the applicant does not know the unit count.
existing-units[] | Number of existing units by bedroom count | Object | MAY | See "Bedroom Count Structure" below.
proposed-units[] | Number of proposed units by bedroom count | Object | MAY | See "Bedroom Count Structure" below.

**Bedroom count** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
bedroom-1 | Number of 1-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-2 | Number of 2-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-3 | Number of 3-bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-4+ | Number of 4 or more bedroom units | Integer | MAY | Not required if unknown is True.
bedroom-count-unknown | Number units where the bedroom number is unknown | Integer | MAY | Not required if unknown is True.
total-units | Total number of units | Integer | MAY | Not required if unknown is True. Calculated as the sum of all bedroom counts.

---

### Site address details (site-details)

Details to help locate the site proposed for development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-boundary | Geometry of the site of the development | | MUST | online services can send the boundary supplied by the applicant/agent. Paper forms would need one of the other fields translated into this |
| address-text | Text address if available for the site | | MAY | does the address need to be structured data or a blob of text like in some app forms? |
| easting | Grid reference | | MAY | |
| northing | Grid reference | | MAY | |
| latitude | Latitude coordinate in EPSG:4326 (WGS84) | | MAY | |
| longitude | Longitude coordinate in EPSG:4326 (WGS84) | | MAY | |
| description | Description of the location if `address-text` does not exist for development/site | | MAY | | 

### Rules

Applicant/agent must provide one of:
* site-boundary
* address
* easting + northing

---

### Site area (site-area)

_To do: add description for module_

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-area |  | | MUST | In hectares. Ideally should be calculated from site boundary. |
| site-area-provided-by | Either Applicant or System/Service | | MAY | Authority can use this to determine if they need to check the calculation |

---

### Site visit (site-visit)

Details needed to support a site visit

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-seen-from | Can site be seen from a public road  public footpath  bridleway or other public land (`true`/`false`) | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Indicates whether a site visit can be done without arranging access |
| contact-type | Indicate who the authority should be contacting | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | See [site visit contact type enum](https://github.com/digital-land/planning-application-data-specification/discussions/222). Enum + other |
| contact | The name of the applicant or agent | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `applicant` or `agent`. Rule: name must match agent if `contact-type` is `agent`. Rule: name must match applicant name if `contact-type` is `applicant` |
| other-contact{} | Details of specifially named contact | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `other` |

**Other contact structure**
| name | Name of person to contact | MUST | |
| number | Phone number of person to contact | MUST | |
| email | Email of person to contact | MUST | |

---

## Sub-type modules
The following modules are required for this sub-type.


## Required codelists

The following codelists are required by modules in this application type:

### Contact priority (contact-priority)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| primary | Primary | The preferred item to use |
| secondary | Secondary | The option to use if primary is not working |

---

### Day type (day-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| monday-friday | Monday to Friday | |
| saturday | Saturday | |
| sunday | Sunday | |
| bank-holiday | Bank holiday | |

---

### Housing type (housing-type)

_To do: add description for codelist_

reference | name | description | application-types
-- | -- | -- | --
houses | Houses | Detached, semi-detached, or terraced houses. |  
flats-maisonettes | Flats/Maisonettes | Self-contained apartments or maisonettes. |  
sheltered-housing | Sheltered Housing | Housing with support for older or disabled people. |  
bedsit-studio | Bedsit/Studio | Single-room living spaces. |  
cluster-flats | Cluster Flats | Flats with shared communal areas. |  
other | Other | Any other housing type not listed. |  
live-work-units | Live-Work Units | Properties combining residential and workspace. | ldc
unknown | Unknown | When the type of housing is uncertain. | ldc

---

### Ownership certificate type (ownership-cert-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
certificate-a | Certificate A | Applicant is the sole owner of the land and there are no agricultural tenants.
certificate-b | Certificate B | Applicant knows all other owners or agricultural tenants and has notified them.
certificate-c | Certificate C | Applicant knows some of the other owners or agricultural tenants and has notified those they know.
certificate-d | Certificate D | Applicant does not know any of the other owners or agricultural tenants.

---

### Reserved matter type (reserved-matter-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| access | Access | |
| appearance | appearance | |
| landscaping | Landscaping | |
| layout | layout | |
| scale | Scale | |

---

### Site visit contact type (site-visit-contact-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
applicant | Applicant | The applicant of the application
agent | Agent | The agent who completed the form

---

### Surface water disposal type (surface-water-disposal-type)

_To do: add description for codelist_

reference | name | description
-- | -- | --
sustainable-drainage | Sustainable drainage system | System designed to manage surface water sustainably.
soakaway | Soakaway | Underground pit allowing water to drain naturally.
main-sewer | Main sewer | Surface water directed into the main sewer system.
existing-watercourse | Existing watercourse | Water discharged into an existing river, stream, or canal.
pond-lake | Pond/lake | Surface water discharged into a pond or lake.

---

### Tenure type (tenure-type)

_To do: add description for codelist_

reference | name | description | application-types
-- | -- | -- | --
market-housing | Market Housing | Private housing for sale or rent. |  ldc;full;outline
social-rented | Social Rented Housing | Public/social housing at below-market rents. | ldc
intermediate-housing | Intermediate Housing | Housing with rents or ownership costs between social housing and market housing. | ldc
key-worker-housing | Key Worker Housing | Housing for essential workers (e.g. teachers, NHS staff). | ldc
affordable-rent | Social, Affordable, or Intermediate Rent | Housing for below-market rent. | full;outline
home-ownership | Affordable Home Ownership | Shared ownership or similar schemes. | full;outline
starter-homes | Starter Homes | Discounted homes for first-time buyers. | full;outline
custom-build | Self-Build and Custom Build | Homes built or commissioned by individuals. | full;outline

---

### Waste management type (waste-management-type)

_To do: add description for codelist_

reference | name | description
-- | -- | --
inert-landfill | Inert Landfill | Disposal site for inert waste materials.
non-hazardous-landfill | Non-Hazardous Landfill | Landfill for non-hazardous waste.
hazardous-landfill | Hazardous Landfill | Landfill site for hazardous waste.
energy-waste-incineration | Energy from Waste Incineration | Incineration facility generating energy from waste.
other-incineration | Other Incineration | Non-energy-producing incineration sites.
landfill-gas-plant | Landfill Gas Generation Plant | Plant generating energy from landfill gas.
pyrolysis-gasification | Pyrolysis/Gasification | Facilities using pyrolysis or gasification processes.
metal-recycling | Metal Recycling Site | Site for recycling metals.
transfer-stations | Transfer Stations | Facilities for sorting and transferring waste.
mrf | Material Recovery Facility (MRF) | Facility for sorting recyclable materials.
household-amenity-site | Household Civic Amenity Sites | Public waste disposal sites for households.
open-windrow-composting | Open Windrow Composting | Outdoor composting of biodegradable waste.
in-vessel-composting | In-Vessel Composting | Enclosed composting for controlled conditions.
anaerobic-digestion | Anaerobic Digestion | Plant for organic waste decomposition without oxygen.
mbt | Mechanical, Biological, or Thermal (MBT) | Combined waste treatment facility.
sewage-treatment | Sewage Treatment Works | Plant for treating wastewater.
other-treatment | Other Treatment | Any other waste treatment not listed.
construction-recycling | Recycling Facilities for Construction Waste | Sites recycling construction and demolition waste.
waste-storage | Storage of Waste | Facilities for storing waste before processing.
other-waste-management | Other Waste Management | Any other waste management facility not listed.
other-developments | Other Developments | Any other related developments.

---

