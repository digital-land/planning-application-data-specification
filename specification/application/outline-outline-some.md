# Outline planning

Applications that are used to understand whether the basic nature of a development is viable

## Sub-type: Outline Planning Permission with Some Matters Reserved

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [All types of development: Non-residential floorspace](#all-types-of-development-non-residential-floorspace-non-res-floorspace)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Assessment of flood risk](#assessment-of-flood-risk-flood-risk-assessment)
* [Authority employee/member](#authority-employee-member-conflict-of-interest)
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

### Sub-type modules

* [Biodiversity and geological conservation](#biodiversity-and-geological-conservation-bio-geo-arch-con)
* [Foul sewage](#foul-sewage-foul-sewage)
* [Hazardous substances](#hazardous-substances-haz-substances)
* [Materials](#materials-materials)
* [Pedestrian and vehicle access, roads and rights of way](#pedestrian-and-vehicle-access-roads-and-rights-of-way-access-rights-of-way)
* [Trade effluent](#trade-effluent-trade-effluent)
* [Trees and hedges](#trees-and-hedges-trees-hedges)
* [Vehicle parking](#vehicle-parking-vehicle-parking)
* [Waste storage and collection](#waste-storage-and-collection-waste-storage-collection)

### Required codelists

* [Affected area type](#affected-area-type-affected-area-type)
* [Building element type](#building-element-type-building-element-type)
* [Contact priority](#contact-priority-contact-priority)
* [Day type](#day-type-day-type)
* [Foul sewage disposal type](#foul-sewage-disposal-type-foul-sewage-disposal-type)
* [Hazardous substance type](#hazardous-substance-type-hazardous-sub-type)
* [Housing type](#housing-type-housing-type)
* [Ownership certificate type](#ownership-certificate-type-ownership-cert-type)
* [Parking space type](#parking-space-type-parking-space-type)
* [Reserved matter type](#reserved-matter-type-reserved-matter-type)
* [Rights of way answer](#rights-of-way-answer-rights-of-way-answer)
* [Site visit contact type](#site-visit-contact-type-site-visit-contact-type)
* [Surface water disposal type](#surface-water-disposal-type-surface-water-disposal-type)
* [Tenure type](#tenure-type-tenure-type)
* [Use class](#use-class-use-class)
* [Waste management type](#waste-management-type-waste-management-type)

---

## Application data specification

field	| description	| data-type | required | notes
--- | --- | --- | --- | ---
reference | UUID for the application record | UUID | MUST | 
application-types[] | A list of planning application types | Enum | MUST | See [list of application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)
application-sub-type | Further classification of the application type for specific variations | Enum | See [list of application sub-types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv)
planning-authority | The reference of the planning authority the application has been submitted to | Organisation reference | MUST | 
submission-date | Date the application is submitted. In `YYYY-MM-DD` format |	Date | MUST |	
modules[] | List of required sections/modules for this application | List |	MUST | List of predefined module references that can be used to validate the application
documents[]{} | List of submitted documents | List | MUST |	Uses a document model to capture references and details.
fee{} | The fee payable for the application | Object | MAY | 

**Document structure**

field | description | required | notes
--- | --- | --- | ---
reference | A reference for the document | MUST | This should be unique
name | The name or title of the document | MUST | 
description | Brief description of what the document contains	| MAY | Optional but useful for context
document-types[] | List of codelist references that the document covers | MUST | Use the planning requirements enum
file{} | The digital file or a reference to where the file is stored | MUST | Must contain either `url` or `base64`, but not both.

**Fee structure**

field | description | required | notes
--- | --- | --- | ---
amount | The total amount due | MUST | 
amount-paid | The amount paid | MUST |
transactions[] | References to payments or financial transactions related to this application. | MAY | Useful for audit and reconciliation.

**File data structure**

field | description | required | notes
--- | --- | --- | ---
url | A URL pointing to the stored file | MAY | For previously uploaded or hosted files
base64 | Base64-encoded content of the file | MAY | For inline file uploads
filename | Name of the file being uploaded | MUST | Useful for identifying and preserving the file
mime-type | The file's MIME type | MAY | e.g., `application/pdf`, `image/jpeg`
checksum | Hash of the file contents (e.g., SHA-256) | MAY      | Used for file validation and checking files have not been tampered with
file-size | Size of the file in bytes | MAY | Can be used to enforce limits

---

## Modules

These modules are all required for this application type

### Agent contact details (agent-contact)

Details needed for contacting the person representing the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent-reference | Use a reference from the agent details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |

**Phone number structure**
| field | description | notes |
| --- | --- | --- | 
| number | A phone number | see [phone-numbers pattern](https://design-system.service.gov.uk/patterns/phone-numbers/) |
| contact-priority | Set the priority of this number. Only one should be `primary` | See [contact priority enum](https://github.com/digital-land/planning-application-data-specification/discussions/200) |

Rule: one phone number provided should have `contact-priority` == `primary`

---

### Agent name and address (agent-details)

Details about the person representing the applicant

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent{} | Details of the agent | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Agent object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |
| company | The company the agent works for | MAY | |
| user-role | A specific of the user, either agent or proxy | MAY | used to determine if the details should be redacted

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |

---

### All types of development: Non-residential floorspace (non-res-floorspace)

Details of any new non-residential development involved in the proposal

field | description | application-types | required | notes
-- | -- | -- | -- | --
non-residential-change | Does the proposal involve the loss, gain, or change of non-residential floorspace? | full;outline | MUST | Boolean (true / false).
floorspace-details[]{} | List of non-residential floorspace changes by use class | full;outline | MAY | Required if non-residential-change is Yes.
room-details[] | List of room changes for hotels, residential institutions and hostels | full;outline | MAY | Required if change to hotels, residential institutions and hostel floorspace |

**Floorspace details**


field | description | data type | required | notes
-- | -- | -- | -- | --
use | Type of non-residential use class | Enum+other | MUST | See [Use Class Enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
specified-use | Specify the use that sits outside the lettered use classes | String | MAY | Rule: is a MUST if `use` is `other` or `sui generis`
existing-gross-floorspace | Existing gross internal floorspace (sqm) | Number | MUST | Must be 0 or positive.
floorspace-lost | Gross floorspace to be lost by change of use (sqm) | Number | MUST | Must be 0 or positive.
total-gross-proposed | Total gross internal floorspace proposed (sqm) | Number | MUST | Must be 0 or positive.
net-additional-floorspace | Net additional gross internal floorspace (sqm) | Number | MUST | Calculated as total-gross-proposed - existing-gross-floorspace.


**Room details**

For certain use classes (C1, C2, C2A), applicants must provide room details:

field | description | data type | required | notes
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
| applicant-reference | Use a reference from the applicant details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Contact details object**
| field | description | required | notes |
| --- | --- | --- | --- |
| email | Email used to contact individual | MUST |  |
| phone-number[]{} | 1 or more telephone numbers to contact individual | MUST | see Phone number below. Only one number can be set as the primary number |

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
| applicants[]{} | Details for one or more applicants | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Rules: must be one or more named applicants |

**Applicant object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |

---

### Assessment of flood risk (flood-risk-assessment)

An assessment needed for any developments within any flood risk zones

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
flood-risk-area | Is the site within an area at risk of flooding? | full;outline;extraction-oil-gas | MUST | Boolean True or False
data-provided-by | Who provided the data: Applicant or System/Service? | full;outline;extraction-oil-gas | MAY | Enum (Applicant / System/Service).
flood-risk-assessment | Reference of the flood risk assessment document | full;outline;extraction-oil-gas | MAY | Required if flood-risk-area is True.
within-20m-watercourse | Is the proposal within 20 metres of a watercourse? | full;outline;extraction-oil-gas | MUST | Boolean True or False.
increases-flood-risk | Will the proposal increase the flood risk elsewhere? | full;outline;extraction-oil-gas | MUST | Boolean True or False.
surface-water-disposal[] | How will surface water be disposed of? | full;outline;extraction-oil-gas | MUST | Multiple options allowed (see [surface water disposal type enum](https://github.com/digital-land/planning-application-data-specification/discussions/195)).


---

### Authority employee/member (conflict-of-interest)

Any connection between the applicant or agent and the local authority’s staff or elected members that could present a conflict of interest

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared. | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MUST | Answer may be different depending on the parties involved. "With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member" |
| name | Name of the individual with the conflict | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| conflict-details | Details including name, role and how individual is related to them | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;notice-trees-in-con-area | MAY | Rule: if `conflict-to-declare` is true then this is a MUST |

---

### Biodiversity net gain (bng)

Information to show how the development will protect or improve wildlife habitats on the site, and whether any exemptions or special rules apply

| field | description | application-types | data-type | required | notes |
| --- | --- | --- | --- | --- | --- |
| bng-exempt | Applicants for planning permission are required to make a statement as to whether they believe the biodiversity gain condition will apply if permission is granted. Householder applicants need to confirm the biodiversity gain condition does not apply. (`true`/`false`) | hh | Boolean | MUST | |
| bng-condition-applies | Does the applicant believe the Biodiversity Gain Condition applies? | full;outline;demolition-con-area | Boolean | MUST | |
| bng-condition-exemption-reason | Reason why BNG does not apply, referencing exemptions or transitional arrangements | full;outline;demolition-con-area | String | MAY | | Rule: Required if `bng-condition-applies` = False |
| bng-details{} | Biodiversity net gain details | full;outline;demolition-con-area | Object | MAY | Rule: is MUST if bng-condition-applies = True |

Rule: if `application-types` includes `hh` (the householder application) then only the `bng-exempt` field is required

**BNG details** structure

field | description | data type | required | notes
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

field | description | data type | required
--- | --- | --- | ---
loss-date | Date the activity causing the loss occurred | Date | MUST
pre-loss-biodiversity-value | Biodiversity value immediately before the activity | Number | MUST
supporting-evidence | Description or reference to supporting documents | String | MAY

**Planning requirement documents**

* Completed biodiversity metric tool - Shows pre-development value and loss if applicable (REQUIRED)
* Habitat plan - Plan showing onsite habitats at the relevant date (REQUIRED)
* Irreplaceable habitat plan - Plan showing onsite irreplaceable habitats (REQUIRED If irreplaceable-habitats = Yes)

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Checklist (checklist)

Details of the national planning requirements the applicant should submit along with the application

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST |  |

---

### Declaration (declaration)

Applicants and agents must declare information provided is correct

| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | (`true` / `false`)
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |

---

### Description of the proposal (proposal-details)

Details about the proposal

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters[] | Identifies which reserved matters are being submitted for approval as part of this application. | outline;reserved-matters | MUST | See [reserved matter type enum](https://github.com/digital-land/planning-application-data-specification/discussions/209)  |
| related-application | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | A description of what is being proposed, including the development, works, or change of use. | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | Has any work on the proposal has already started. (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | The date when work on the proposal started. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | Has the development or works have already been completed (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | The date when the development or works were completed. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | For applications made on or after 1 August 2021, is the proposal for public service infrastructure development (`true`/`false`)| full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-date | date of the decision | If decided | |

---

### Employment (employment)

Information about employees

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-employees{} | Counts of existing employees | full;outline;extraction-oil-gas | MUST | Required for all non-residential applications.
proposed-employees | Counts of proposed employees | full;outline;extraction-oil-gas | MUST | Required if the proposal affects employment capacity.
employment-impact | Summary of net employment change (gain/loss) | full;outline;extraction-oil-gas | MAY | Calculated based on existing and proposed values.

**Employees**
Field | Description | Notes
-- | -- | --
full-time | Number of full-time employees | Must be a positive integer or 0.
part-time | Number of part-time employees | Must be a positive integer or 0.
fte | Total full-time equivalent (FTE) | Calculated as full-time + (part-time ÷ 2).

---

### Existing use (existing-use)

Application for development that doesn't change the existing use of the building

field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details | Describe the current use of the site | full;outline;extraction-oil-gas | MUST | 
site-vacant | True or False | | MUST | 
last-use-details | Describe the last use of the site | full;outline;extraction-oil-gas | MAY | Rule, is a MUST if `site-vacant` is True 
last-use-end-date | Date the last use ended (YYYY-MM-DD format) | full;outline;extraction-oil-gas | MAY | Rule, is a MUST if `site-vacant` is True 
is-contaminated-land | Is the site known to be contaminated? (True/False) | full;outline;extraction-oil-gas | MUST | 
is-suspected-contaminated-land | Is the site suspected of contamination? (True/False) | full;outline;extraction-oil-gas | MUST | 
proposed-use-contamination-risk | Is the proposed use vulnerable to the presence of contamination? (True/False) | full;outline;extraction-oil-gas | MUST |
contamination-assessment | Reference to contamination assessment document | full;outline;extraction-oil-gas | MAY | Is a MUST if `is-contaminated-land`, `is-suspected-contaminated-land` or `proposed-use-contamination-risk` is True

---

### Hours of operation (hrs-operation)

Hours of opening for each non-residential use proposed

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation[]{} | List the hours of operation by non-residential use | full;outline;extraction-oil-gas | MUST | |
| additional-information | Any additional information (such as hours of use of other machinery within the site-generators, pumps, etc) | extraction-oil-gas | MAY | |

**hours of operation**
| field | description | required | notes |
| --- | --- | --- | --- |
| use | The use class | MUST | One of the [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) + other |
| use-other | Specify use if use is other | MAY	Required if `use` is `other`
| operational-times[]{} | Structured data for operational hours by day | MAY | Rule: Must be completed if hours-not-known is not provided |
| hours-not-known | Applicant states they do not know the hours of operation | MAY | Rule: Must be completed if operational-times is not provided |

**Opening times**
| field | description | notes |
| --- | --- | --- |
| day-type | Day or type of day | One of [day-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/197) |
| time-ranges[]{} | Opening and closing times for the day	| MUST | Can have multiple ranges (e.g., morning and evening opening) |
| closed | True or False | If True, `open-time` and `close-time` must be empty. Explicitly state when closed |

**time range structure**
field	| description |	required | notes
--- | --- | --- | ---
open-time | Opening time | MUST | Format: `HH:MM`
close-time | Closing time | MUST | Format: `HH:MM`

---

### Industrial or commercial processes and machinery (processes-machinery-waste)

Activities and processes which would be carried out on the site and the end products including plant, ventilation, or air conditioning

Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
site-activity-details | Description of activities, processes, and end products | full;outline | MUST | Describe site operations, including plant, ventilation, and machinery.
proposal-waste-management | Whether the proposal involves waste management development | full;outline | MUST | True if the proposal includes waste management.
waste-management[] | List of waste management facilities involved | full;outline | MAY | MUST if proposal-waste-management is True.
waste-streams{} | Annual throughput for waste streams | full;outline | MAY | MUST if proposal-waste-management is True.

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
sole-owner | Is the applicant the sole owner of the land? (True/False) | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MUST | If True, ownership-cert-option is Certificate-A.
agricultural-tenants | Are there any agricultural tenants? (True/False) |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MUST | If True, Certificate-A cannot apply.
owners-and-tenants[]{} | List of known owners and agricultural tenants | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY | Required for Certificate-B or Certificate-C.
steps-taken | Steps taken to identify unknown owners or tenants | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY | Required for Certificate-C or Certificate-D.
newspaper-notice[]{} | Newspaper notice details for unknown owners/tenants |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MAY | Required for Certificate-C or Certificate-D.
ownership-cert-option | Ownership certificate type based on ownership and tenancy | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MUST | See [ownership certificate type enum](https://github.com/digital-land/planning-application-data-specification/discussions/224)
applicant-signature | Signature of the applicant | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MAY |  
agent-signature | Signature of the agent (if applicable) |  hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas | MAY |  
signature-date | Date of applicant or agent signature | hh;full;outline;demolition-con-area;lbc;s73;extraction-oil-gas  | MUST | Format: YYYY-MM-DD.

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
| postcode | The post code for the address provided | MAY | |

---

### Pre-application advice (pre-app-advice)

Details of pre-application advice received from the local planning authority


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Has pre-application advice has been sought | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Boolean (`true`/`false`) |
| officer-name | Name of officer who dealt with pre-app advice | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| reference | Reference for pre-application advice application | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-date | Date applicant received the advice, in `YYYY-MM-DD` format | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-summary | Summary of the advice received | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | is this necessary if they have provided the reference? |

---

### Residential units (including conversion) (res-units)

The amount of residential units included as part of your proposal

Field | Description | Application type | Required? | Notes
-- | -- | -- | -- | --
residential-unit-change | Proposal includes the gain, loss or change of use of residential units (True/False) | full;outline;ldc | MUST | Could be calculated from answers to next parts?
residential-unit-summary[]{} | Breakdown of unit counts by tenure and housing type | full;outline;ldc | MAY | Is MUST if `residential-unit-change` is True
total-existing-units | The total number of existing units | full;outline;ldc | MUST |
total-proposed-units | The total number of proposed units | full;outline;ldc | MUST |
net-change | Calculated net change in units | full;outline;ldc | MUST | Calculated as proposed-units - existing-units. Format: Integer

**residential-unit-summary**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
tenure-type | Category of housing tenure | Enum | MUST | See [tenure type enum](https://github.com/digital-land/planning-application-data-specification/discussions/162)
housing-type | Type of housing | Enum | MUST | See [housing type enum](https://github.com/digital-land/planning-application-data-specification/discussions/163)
existing-unit-breakdown[]{} | Number of existing units by bedroom count | Object | MAY | See "Unit quantities Structure" below.
proposed-unit-breakdown[]{} | Number of proposed units by bedroom count | Object | MAY | See "Unit quantities Structure" below.

**Unit quantities** 

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
units-unknown | Whether the number of units is unknown (`true`/`false`) | Boolean | MUST | 
units-per-bedroom-no[]{} | For this tenure and unit type | Object | MAY | MUST if `units-unknown` is False. See bedroom count
total-units | Total number of units | Integer | MAY | Not required if `units-unknown` is True. Calculated as the sum of all bedroom counts.


**bedroom count**

field | description | data-type | required | notes
-- | -- | -- | -- | --
no-bedrooms-unknown | Set to true when counting units where bedroom number is unknown | Boolean | MUST || Default is false
no-of-bedrooms | The number of bedrooms in unit | integer | MAY | MUST if no-bedrooms-unknown is true
units | the number of units of that bedroom count | integer | MUST | 0 or above



rule: if residential-unit-change = true, at least one breakdown for existing and proposed is required (count could be unknown).

---

### Site address details (site-details)

Details to locate the site proposed for development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-locations[]{} | Details of the sites on which the tree(s) are located | notice-trees-in-con-area;consent-under-tpo | MAY | Rule: only required if the site is different from the applicant's address | 

**site-location/details structure**

| field | description | required | notes |
| --- | --- | --- | --- |
| site-boundary | Geometry of the site of the development | MUST | online services can send the boundary supplied by the applicant/agent. Paper forms would need one of the other fields translated into this |
| address-text | Text address if available for the site | MAY | does the address need to be structured data or a blob of text like in some app forms? |
| postcode | The post code for the address provided | MAY | |
| easting | Grid reference | MAY | |
| northing | Grid reference | MAY | |
| latitude | Latitude coordinate in EPSG:4326 (WGS84) | MAY | |
| longitude | Longitude coordinate in EPSG:4326 (WGS84) | MAY | |
| description | Description of the location if `address-text` does not exist for development/site | MAY | |
| uprns[] | Where known, list the UPRNs affected by the proposal | MAY | UPRN data can support clearer tracking, analysis, and integration across systems. We recommend that the list of uprns is derived where possible |

### Rules

Applicant/agent must provide one of:
* site-boundary
* address
* easting + northing

---

### Site area (site-area)

Size of the site

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-area | Provide the size of the size in hectares | full;outline | MUST | In hectares. Ideally should be calculated from site boundary. |
| site-area-provided-by | Either Applicant or System/Service | full;outline | MAY | Authority can use this to determine if they need to check the calculation |

---

### Site visit (site-visit)

Details needed to support a site visit

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| can-be-seen-from | Can site be seen from a public road  public footpath  bridleway or other public land (`true`/`false`) | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Indicates whether a site visit can be done without arranging access |
| contact-type | Indicate who the authority should be contacting | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | See [site visit contact type enum](https://github.com/digital-land/planning-application-data-specification/discussions/222). Enum + other |
| contact-reference | A reference for the applicant or agent who is the contact point for the site visit | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `applicant` or `agent`. Rule: name must match agent if `contact-type` is `agent`. Rule: name must match applicant name if `contact-type` is `applicant` |
| other-contact{} | Details of specifically named contact | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | Rule: is a MUST if `contact-type` is `other` |

**Other contact structure**

| field | description | requirement-level | notes |
| --- | --- | --- | --- |
| fullname | Name of person to contact | MUST | |
| number | Phone number of person to contact | MUST | |
| email | Email of person to contact | MUST | |

---

### Biodiversity and geological conservation (bio-geo-arch-con)

Details of any impact to biodiversity or geological convservation

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
protected-species-impact | Is there a likelihood of protected and priority species being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
biodiversity-features-impact | Is there a likelihood of important habitats or biodiversity features being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
geological-features-impact | Is there a likelihood of features of geological conservation importance being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
archaeological-features-impact | Is there a likelihood of features of archaeological conservation importance being affected? | extraction-oil-gas | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no

---

### Foul sewage (foul-sewage)

Description of how sewage will be dealt with for the development

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
foul-sewage-disposal-types[] | List of ways foul sewage will be disposed of | full;extraction-oil-gas;outline | MUST | See [foul-sewage-disposal-type ENUM](https://github.com/digital-land/planning-application-data-specification/discussions/165)
produce-foul-sewage | Proposed development produce any foul sewage (True/False) | extraction-oil-gas | MUST | 
connect-to-drainage-system | Does the proposal need to connect to the existing drainage system (True/False) | full;extraction-oil-gas;outline | MUST | 
drainage-system-details | Details of the drawings/plans that show the existing system | full;extraction-oil-gas;outline | MAY | Rule, is a MUST if `connect-to-drainage-system` is TRUE or `extraction-oil-gas` application 

---

### Hazardous substances (haz-substances)

Does proposal include use or storage of hazardous substances? This module is used to determine if hazardous substances consent would also be required

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
involves-hazardous-substances | Indicates if hazardous substances are involved | full;outline  | MUST | One of Yes, No, Not Applicable.
substance-types[] | List of hazardous substances and their quantities |  full;outline  | MAY | Required if hazardous-substances-involved is Yes.
hazardous-sub-consent-req | Does the proposal involve the use or storage of any substances requiring hazardous substances consent? (`true`/`false`) | extraction-oil-gas | MUST | 
hazardous-sub-consent-details | Details of hazardous substance consent | extraction-oil-gas | MAY | Is a MUST if `hazardous-sub-consent-req` is true

**Hazardous substance types**

Field | Description | Notes
-- | -- | --
hazardous-substance-type | Reference of hazardous substance type | Predefined list (see [hazardous-substances enum](https://github.com/digital-land/planning-application-data-specification/discussions/196)) + option for Other.
name | Name of the hazardous substance | Only required if Other is selected
amount | Amount of the substance in tonnes | Numeric. Must be greater than 0.

---

### Materials (materials)

Details about the materials to be used or changed should be provided, including type, colour and name for each material

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-elements[]{} | List of building elements where materials are being described (e.g., walls, roof). | hh;full;demolition-con-area;lbc;advertising;outline | MUST | See Building element structure. One entry per building element.
additional-material-information | Indicates whether additional documents are provided to supplement the materials description | hh;full;demolition-con-area;lbc;advertising;outline | MUST | (`true` or `false`).
supporting-documents[] | Details for documents providing additional material information. | hh;full;demolition-con-area;lbc;advertising;outline | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Pedestrian and vehicle access, roads and rights of way (access-rights-of-way)

Any changes to how people or vehicles access the site, including any new or affected roads, footpaths, or public rights of way

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | Is a new or altered vehicle access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-altered-pedestrian | Is a new or altered pedestrian access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| change-right-of-way | Will the proposal change public rights of way? (diversion/extinguishment/creation) | full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers.|
| new-right-of-way | Will new public rights of way be provided within or adjacent to the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-public-road | Will new public roads be provided within the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| temp-right-of-way | Are temporary changes to rights of way needed while the site is worked? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| future-new-right-of-way | Will new public rights of way be provided after extraction? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| supporting-documents[]{} | List of documents supporting the information provided | extraction-oil-gas;full;hh;outline | MAY | Required if any answer is `true`. |

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity
---

### Trade effluent (trade-effluent)

Effluents that will be produced from a process or activity undertaken on the site

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| `is-disposal-required` | Does the proposal involve the disposal of trade effluents or waste (`true`/`false`) | full;extraction-oil-gas;outline | MUST | | 
| `description` | Describe the nature, volume and means of disposal of trade effluents or waste | full;extraction-oil-gas;outline | MAY | Rule: is a MUST if `disposal-required` is True |

---

### Trees and hedges (trees-hedges)

Details of trees and hedges affecting the site or that will be affected by the proposed development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-falling-trees-risk | There are falling trees on-premises or adjacent premises that are a risk to the development. (`true`/`false`) | hh | MUST | |
| falling-trees-document{} | Details of document showing location of trees | hh | MAY | Rule: is a MUST if `has-falling-trees-risk` is `true` |
| tree-removal | Do trees or hedges need to be pruned or removed (`true`/`false`) | hh | MUST | |
| tree-removal-plan{} | Details of document showing location of trees and hedges | hh | MAY | Rule: is a MUST of ` tree-removal` is `true`. See supporting document structure below |
| trees-on-site | Trees or hedges are on the proposed development site (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |
| trees-on-adj-land | Trees or hedges on land adjacent to the proposed development site that could influence the development or might be important as part of the local landscape character (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |

**supporting documents**

_Used for tree-removal-plan_

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Vehicle parking (vehicle-parking)

Existing and proposed number of on-site parking spaces

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
parking-spaces[]{} | List of parking spaces by vehicle type |   | MUST | One object per vehicle type, including “Other” if specified.

**Parking space items**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
parking-space-type | Type of vehicle from the codelist | Enum / String | MUST | Select from [parking space type enum](https://github.com/digital-land/planning-application-data-specification/discussions/199), or "other" if user specifies a custom type.
vehicle-type-other | Custom value if "Other" is selected | String | MAY | Rule: Required only if `vehicle-type` is "other".
total-existing | Existing on-site parking spaces | Number | MUST | Must be 0 or positive.
total-proposed | Total proposed spaces, including retained spaces | Number | MUST | Must be 0 or positive.
unknown-proposed | Is the total proposed number unknown? | Boolean | MUST | If True, total-proposed can be left blank.
difference-in-spaces | Calculated difference between existing and proposed spaces | Number | MUST | Calculated as total-proposed - total-existing. Could be calculated by applicant or system

---

### Waste storage and collection (waste-storage-collection)

Proposed waste storage and collection

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| needs-waste-storage-area | Does the proposal require a waste storage area (`true`/`false`) | full;outline | MUST | |
| waste-storage-area-details | Details of the waste storage area | full;outline | MAY | Rule, is a MUST if `needs-waste-storage-area` is True |
| separate-recycling-arrangements | Does the proposal include separate recycling arrangements? (`true`/`false`) | full;outline | MUST | |
| separate-recycling-arrangements-details | Provide details of the recycling arrangements | full;outline | MAY | Rule, is a MUST if `separate-recycling-arrangements` is True |

---

## Sub-type modules
The following modules are required for this sub-type.

### Biodiversity and geological conservation (bio-geo-arch-con)

Details of any impact to biodiversity or geological convservation

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
protected-species-impact | Is there a likelihood of protected and priority species being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
biodiversity-features-impact | Is there a likelihood of important habitats or biodiversity features being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
geological-features-impact | Is there a likelihood of features of geological conservation importance being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
archaeological-features-impact | Is there a likelihood of features of archaeological conservation importance being affected? | extraction-oil-gas | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no

---

### Foul sewage (foul-sewage)

Description of how sewage will be dealt with for the development

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
foul-sewage-disposal-types[] | List of ways foul sewage will be disposed of | full;extraction-oil-gas;outline | MUST | See [foul-sewage-disposal-type ENUM](https://github.com/digital-land/planning-application-data-specification/discussions/165)
produce-foul-sewage | Proposed development produce any foul sewage (True/False) | extraction-oil-gas | MUST | 
connect-to-drainage-system | Does the proposal need to connect to the existing drainage system (True/False) | full;extraction-oil-gas;outline | MUST | 
drainage-system-details | Details of the drawings/plans that show the existing system | full;extraction-oil-gas;outline | MAY | Rule, is a MUST if `connect-to-drainage-system` is TRUE or `extraction-oil-gas` application 

---

### Hazardous substances (haz-substances)

Does proposal include use or storage of hazardous substances? This module is used to determine if hazardous substances consent would also be required

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
involves-hazardous-substances | Indicates if hazardous substances are involved | full;outline  | MUST | One of Yes, No, Not Applicable.
substance-types[] | List of hazardous substances and their quantities |  full;outline  | MAY | Required if hazardous-substances-involved is Yes.
hazardous-sub-consent-req | Does the proposal involve the use or storage of any substances requiring hazardous substances consent? (`true`/`false`) | extraction-oil-gas | MUST | 
hazardous-sub-consent-details | Details of hazardous substance consent | extraction-oil-gas | MAY | Is a MUST if `hazardous-sub-consent-req` is true

**Hazardous substance types**

Field | Description | Notes
-- | -- | --
hazardous-substance-type | Reference of hazardous substance type | Predefined list (see [hazardous-substances enum](https://github.com/digital-land/planning-application-data-specification/discussions/196)) + option for Other.
name | Name of the hazardous substance | Only required if Other is selected
amount | Amount of the substance in tonnes | Numeric. Must be greater than 0.

---

### Materials (materials)

Details about the materials to be used or changed should be provided, including type, colour and name for each material

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-elements[]{} | List of building elements where materials are being described (e.g., walls, roof). | hh;full;demolition-con-area;lbc;advertising;outline | MUST | See Building element structure. One entry per building element.
additional-material-information | Indicates whether additional documents are provided to supplement the materials description | hh;full;demolition-con-area;lbc;advertising;outline | MUST | (`true` or `false`).
supporting-documents[] | Details for documents providing additional material information. | hh;full;demolition-con-area;lbc;advertising;outline | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Pedestrian and vehicle access, roads and rights of way (access-rights-of-way)

Any changes to how people or vehicles access the site, including any new or affected roads, footpaths, or public rights of way

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | Is a new or altered vehicle access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-altered-pedestrian | Is a new or altered pedestrian access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| change-right-of-way | Will the proposal change public rights of way? (diversion/extinguishment/creation) | full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers.|
| new-right-of-way | Will new public rights of way be provided within or adjacent to the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-public-road | Will new public roads be provided within the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| temp-right-of-way | Are temporary changes to rights of way needed while the site is worked? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| future-new-right-of-way | Will new public rights of way be provided after extraction? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| supporting-documents[]{} | List of documents supporting the information provided | extraction-oil-gas;full;hh;outline | MAY | Required if any answer is `true`. |

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity
---

### Trade effluent (trade-effluent)

Effluents that will be produced from a process or activity undertaken on the site

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| `is-disposal-required` | Does the proposal involve the disposal of trade effluents or waste (`true`/`false`) | full;extraction-oil-gas;outline | MUST | | 
| `description` | Describe the nature, volume and means of disposal of trade effluents or waste | full;extraction-oil-gas;outline | MAY | Rule: is a MUST if `disposal-required` is True |

---

### Trees and hedges (trees-hedges)

Details of trees and hedges affecting the site or that will be affected by the proposed development

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-falling-trees-risk | There are falling trees on-premises or adjacent premises that are a risk to the development. (`true`/`false`) | hh | MUST | |
| falling-trees-document{} | Details of document showing location of trees | hh | MAY | Rule: is a MUST if `has-falling-trees-risk` is `true` |
| tree-removal | Do trees or hedges need to be pruned or removed (`true`/`false`) | hh | MUST | |
| tree-removal-plan{} | Details of document showing location of trees and hedges | hh | MAY | Rule: is a MUST of ` tree-removal` is `true`. See supporting document structure below |
| trees-on-site | Trees or hedges are on the proposed development site (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |
| trees-on-adj-land | Trees or hedges on land adjacent to the proposed development site that could influence the development or might be important as part of the local landscape character (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |

**supporting documents**

_Used for tree-removal-plan_

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Vehicle parking (vehicle-parking)

Existing and proposed number of on-site parking spaces

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
parking-spaces[]{} | List of parking spaces by vehicle type |   | MUST | One object per vehicle type, including “Other” if specified.

**Parking space items**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
parking-space-type | Type of vehicle from the codelist | Enum / String | MUST | Select from [parking space type enum](https://github.com/digital-land/planning-application-data-specification/discussions/199), or "other" if user specifies a custom type.
vehicle-type-other | Custom value if "Other" is selected | String | MAY | Rule: Required only if `vehicle-type` is "other".
total-existing | Existing on-site parking spaces | Number | MUST | Must be 0 or positive.
total-proposed | Total proposed spaces, including retained spaces | Number | MUST | Must be 0 or positive.
unknown-proposed | Is the total proposed number unknown? | Boolean | MUST | If True, total-proposed can be left blank.
difference-in-spaces | Calculated difference between existing and proposed spaces | Number | MUST | Calculated as total-proposed - total-existing. Could be calculated by applicant or system

---

### Waste storage and collection (waste-storage-collection)

Proposed waste storage and collection

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| needs-waste-storage-area | Does the proposal require a waste storage area (`true`/`false`) | full;outline | MUST | |
| waste-storage-area-details | Details of the waste storage area | full;outline | MAY | Rule, is a MUST if `needs-waste-storage-area` is True |
| separate-recycling-arrangements | Does the proposal include separate recycling arrangements? (`true`/`false`) | full;outline | MUST | |
| separate-recycling-arrangements-details | Provide details of the recycling arrangements | full;outline | MAY | Rule, is a MUST if `separate-recycling-arrangements` is True |

---


## Required codelists

The following codelists are required by modules in this application type:

### Affected area type (affected-area-type)

Specifies whether a biodiversity or geological feature is on the development site or on land directly next to it.

reference | name | description
--- | --- | ---
on-development-site | On development site | 
adjacent-to-site | On adjacent site | 

---

### Building element type (building-element-type)

A set of building elements that applicants are expected to provide material information for

| reference | name | description | application-types | notes |
| --- | --- | --- | --- | --- |
| walls | Walls | A vertical construction that bounds or subdivides spaces | advertising;demolition-con-area;full;hh;outline | Referring to same thing as [IfcWall](https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD1/HTML/link/ifcbuildingelement.htm) |
| roof | Roof | A covering of the top part of a building, it protects the building against the effects of weather | advertising;demolition-con-area;full;hh;outline | Referring to same thing as IfcWall |
| windows | Windows | | advertising;demolition-con-area;full;hh;outline | |
| doors | Doors | | advertising;demolition-con-area;full;hh;outline | |
| boundary-treatments | Boundary treatments | | advertising;demolition-con-area;full;hh;lbc;outline | |
| vehicle-access-hard-standings | Vehicle access and hard-standings | | advertising;demolition-con-area;full;hh;lbc;outline | |
| lighting | Lighting | | advertising;demolition-con-area;full;hh;lbc;outline | |
| external-walls | External walls | | lbc | |
| roof-covering | Roof covering | | lbc | |
| chimney | Chimney | | lbc | |
| external-doors | External doors | | lbc | |
| ceilings | Ceilings | | lbc | |
| internal-walls | Internal walls | | lbc | |
| floors | Floors | | lbc | |
| internal-doors | Internal doors | | lbc | |
| rainwater-goods | Rainwater goods | | lbc | |
| other | Other | | advertising;demolition-con-area;full;hh;lbc;outline | |

---

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

### Foul sewage disposal type (foul-sewage-disposal-type)

_To do: add description for codelist_

| reference | name | description |
| --- | --- | --- |
| mains-sewer | Mains sewer | |
| cess-pit | Cess pit | |
| septic-tank | Septic tank | |
| package-treatment | Package treatment plant | |
| other | Other | |

---

### Hazardous substance type (hazardous-sub-type)

_To do: add description for codelist_

Reference | Name | Notes
-- | -- | --
acrylonitrile | Acrylonitrile |  
ammonia | Ammonia |  
bromine | Bromine |  
chlorine | Chlorine |  
ethylene-oxide | Ethylene oxide |  
flour | Flour |  
hydrogen-cyanide | Hydrogen cyanide |  
liquid-oxygen | Liquid oxygen |  
liquid-petroleum-gas | Liquid petroleum gas |  
phosgene | Phosgene |  
refined-white-sugar | Refined white sugar |  
sulphur-dioxide | Sulphur dioxide |  

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

### Parking space type (parking-space-type)

_To do: add description for codelist_

reference | name | description
-- | -- | --
car-space | Cars | Standard on-site parking spaces for cars.
light-goods-vehicle-space | Light Goods/Public Carrier Vehicles | Vans, delivery vehicles, and public carriers.
motorcycle-space | Motorcycles | Spaces designated for motorbikes.
disability-space | Disability Space | Accessible parking spaces.
cycle-space | Cycle Space | Bicycle parking, including racks or shelters.

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

### Rights of way answer (rights-of-way-answer)

_To do: add description for codelist_

reference | name | application-types | description
--- | --- | --- | ---
true | True | extraction-oil-gas;full;hh;outline | The statement is true
false | False | extraction-oil-gas;full;hh;outline | The statement is false
unknown | Unknown | outline | The answer is unknown 

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

