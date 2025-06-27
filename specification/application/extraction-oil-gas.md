# Development relating to the onshore extraction of oil and gas



## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Agent contact details](#agent-contact-details-agent-contact)
* [Agent name and address](#agent-name-and-address-agent-details)
* [Applicant contact details](#applicant-contact-details-applicant-contact)
* [Applicant name and address](#applicant-name-and-address-applicant-details)
* [Assessment of flood risk](#assessment-of-flood-risk-flood-risk-assessment)
* [Authority employee/member](#authority-employee-member-conflict-of-interest)
* [Biodiversity and geological conservation](#biodiversity-and-geological-conservation-bio-geo-arch-con)
* [Checklist](#checklist-checklist)
* [Declaration](#declaration-declaration)
* [Designated areas](#designated-areas-designated-areas)
* [Employment](#employment-employment)
* [Equipment and method used](#equipment-and-method-used-equip-method)
* [Existing use](#existing-use-existing-use)
* [Foul sewage](#foul-sewage-foul-sewage)
* [Hazardous substances](#hazardous-substances-haz-substances)
* [Hours of operation](#hours-of-operation-hrs-operation)
* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration-ownership-certs)
* [Pedestrian and vehicle access, roads and rights of way](#pedestrian-and-vehicle-access-roads-and-rights-of-way-access-rights-of-way)
* [Plans, drawings and other supporting material](#plans-drawings-and-other-supporting-material-plans-drawings-supporting-materials)
* [Pre-application advice](#pre-application-advice-pre-app-advice)
* [Site address details](#site-address-details-site-details)
* [Site ownership](#site-ownership-site-ownership)
* [Site visit](#site-visit-site-visit)
* [Storage](#storage-storage-facilities)
* [Trade effluent](#trade-effluent-trade-effluent)
* [Trees and hedges](#trees-and-hedges-trees-hedges)
* [Type of development](#type-of-development-dev-type)
* [Types of application](#types-of-application-types-application)
* [Voluntary agreements / planning obligations](#voluntary-agreements-planning-obligations-vol-agreement)

### Required codelists

* [Affected area type](#affected-area-type-affected-area-type)
* [Contact priority](#contact-priority-contact-priority)
* [Day type](#day-type-day-type)
* [Designations](#designations-designation)
* [Development phases](#development-phases-development-phases)
* [Foul sewage disposal type](#foul-sewage-disposal-type-foul-sewage-disposal-type)
* [Hazardous substance type](#hazardous-substance-type-hazardous-sub-type)
* [Ownership certificate type](#ownership-certificate-type-ownership-cert-type)
* [Permission type](#permission-type-permission-type)
* [Rights of way answer](#rights-of-way-answer-rights-of-way-answer)
* [Site visit contact type](#site-visit-contact-type-site-visit-contact-type)
* [Surface water disposal type](#surface-water-disposal-type-surface-water-disposal-type)
* [Use class](#use-class-use-class)

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

### Biodiversity and geological conservation (bio-geo-arch-con)

Details of any impact to biodiversity or geological convservation

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
protected-species-impact | Is there a likelihood of protected and priority species being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
biodiversity-features-impact | Is there a likelihood of important habitats or biodiversity features being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
geological-features-impact | Is there a likelihood of features of geological conservation importance being affected? | full;extraction-oil-gas;outline-some | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
archaeological-features-impact | Is there a likelihood of features of archaeological conservation importance being affected? | extraction-oil-gas | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no

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

### Designated areas (designated-areas)

Areas that are protected because of their natural and cultural importance

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
designations[] | List of designated areas that apply to the site | extraction-oil-gas | MUST | Multiple selections allowed. If None of the above is selected, no other options can be chosen. Leave blank if none. See [designations enum](https://github.com/digital-land/planning-application-data-specification/discussions/193)

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

### Equipment and method used (equip-method)

Information about the equipment and methods proposed

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| equipment-plan | Details of equipment to be used as part of the application including the maximum height and type of drilling rig to be used | extraction-oil-gas | MUST | |

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

### Plans, drawings and other supporting material (plans-drawings-supporting-materials)

_To do: add description for module_

Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
documents[]{} | List of plans, drawings, and supporting documents | extraction-oil-gas | MUST | See Document Structure below.
inspection-address | Address where supporting material can be inspected | extraction-oil-gas | MUST | Full postal address for document inspection.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

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

### Site ownership (site-ownership)

Who currently owns the site

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-owner{} | | extraction-oil-gas | MUST |  |
| applicant-interest | Description of applicant's interest in the land | extraction-oil-gas | MUST |  |
| applicant-interest-adjoining-land | Description of applicant's interest in the adjacent land | extraction-oil-gas | MUST |  |

**Site-owner** 
| field | description | required | notes |
| --- | --- | --- | --- |
| fullname | | MUST |  |
| address-text | | MUST |  |

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

### Storage (storage-facilities)

Any storage of materials proposed during construction

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| `storage-facilities-description` | Details and proposed facilities for the storage of oil, fuel and chemicals and the proposed means of their protection | extraction-oil-gas | MUST | | 

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

### Type of development (dev-type)

Type of development

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
development-phases[] | Phases of oil and gas development the application covers | Array (Enum) | MUST | One or more of: exploratory, appraisal, production. See [development phase enum](https://github.com/digital-land/planning-application-data-specification/discussions/194)
development-description | Brief description of the development, including main oils, gases, and machinery | String | MUST | Free text.
quantity-cubic-metres | Quantity of oil or gas involved (in cubic metres) | Number | MUST | 
permission-period-years | Period of permission sought (in years) | Number | MAY | Optional if period is not defined.
hydrocarbon-licence-block | Hydrocarbon licence block where the development is located | String | MUST | Typically an identifier like "PEDL123".
surface-site-area-hectares | Surface site area in hectares (ha) | Number | MUST | Value must be positive. Should it be calculated from the site boundary?
site-hectares-provided-by | Who provided the site hectares value | String | MAY | Either Applicant or System. Authority can use it to know if they need to check calculation
environmental-statement | Is an Environmental Statement attached to the application? | Boolean | MUST | Yes / No.
environmental-statement-reference | Reference of the environmental statement document supplied with application | String | MAY | Required if environmental-statement is True

---

### Types of application (types-application)

Type of application

field | description | data type | application-types | required | notes
-- | -- | -- | -- | -- | --
permission-types[] | List of permission types being applied for | Array | extraction-oil-gas | MUST | One or more from the [permission types enum](https://github.com/digital-land/planning-application-data-specification/discussions/198).
related-proposals[]{} | List of related proposals with reference and decision dates | Array | extraction-oil-gas | MAY | Required if any application type involves prior permissions.
other-details | | String | extraction-oil-gas | MAY |  If there are other details not covered by the application types 
consolidate-permissions | Is the applicant willing to consolidate or update existing permissions? | Boolean | extraction-oil-gas | MUST | Yes / No. If Yes, further details are required.
consolidate-details | Details about the consolidation or update of permissions | String | extraction-oil-gas | CONDITIONAL | Required if consolidate-permissions is Yes.

**Related proposals** 

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
proposal-type | Type of related proposal | Enum | MUST | Enum value from Application Type
reference-number | Reference number of the related proposal | String | MUST | Unique identifier for the proposal
decision-date | Decision date of the related proposal | Date | MUST | Format: YYYY-MM-DD.

---

### Voluntary agreements / planning obligations (vol-agreement)

Any voluntary agreements or planning obligations

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| draft-agreement-included | outline or draft agreement included? (True / False) | extraction-oil-gas | MUST | |
| agreement-summary | Summary of the agreement | extraction-oil-gas | MAY | Rule: is a MUST if `draft-agreement-included` is True |

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

### Designations (designation)

_To do: add description for codelist_

reference | name | notes
-- | -- | --
world-heritage-site | World Heritage Site | Site of global cultural or natural importance.
national-park | National Park (including The Broads and The New Forest) | Protected area for natural beauty and recreation.
area-outstanding-natural-beauty | Area of Outstanding Natural Beauty (AONB) | Designated for distinctive landscape value.
site-special-scientific-interest | Site of Special Scientific Interest (SSSI) | Protected for wildlife, geology, or landform.
national-nature-reserve | National Nature Reserve | Important area for wildlife and conservation.
conservation-area | Conservation Area | Area designated for historical or architectural significance.
special-area-conservation | Special Area of Conservation | Designated under the EU Habitats Directive.
special-protection-area | Special Protection Area/Ramsar site | Protected for bird species under the EU Birds Directive.
green-belt | Green Belt | Area designated to prevent urban sprawl.

---

### Development phases (development-phases)

_To do: add description for codelist_

reference | name | description
-- | -- | --
exploratory | Exploratory Phase | Initial drilling and testing for hydrocarbons.
appraisal | Appraisal Phase | Further testing to determine viability.
production | Production Phase | Full-scale extraction and production operations.

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

### Ownership certificate type (ownership-cert-type)

_To do: add description for codelist_

reference | name | description
--- | --- | ---
certificate-a | Certificate A | Applicant is the sole owner of the land and there are no agricultural tenants.
certificate-b | Certificate B | Applicant knows all other owners or agricultural tenants and has notified them.
certificate-c | Certificate C | Applicant knows some of the other owners or agricultural tenants and has notified those they know.
certificate-d | Certificate D | Applicant does not know any of the other owners or agricultural tenants.

---

### Permission type (permission-type)

_To do: add description for codelist_

reference | name | requires related proposal?
-- | -- | --
oil-gas-full-permission | Full planning permission for oil and gas working | No
waste-full-permission | Full planning permission for controlled waste | No
renewal-unimplemented | Renewal of unimplemented permission | Yes
renewal-temporary | Renewal of temporary permission | Yes
extension-existing-site | Extension to an existing site | Yes
variation-condition | Variation of condition(s) | Yes
romp-review | Review of conditions for Mineral Permissions (ROMPs) | Yes
minerals-development | Previous permissions for minerals development on the site | Yes

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

