# Planning Application Data Model

This specification sets out how to structure and share planning application data.

## Contents

* [Application model](#application-model)

* [Modules](#modules)

	* [Adjoining premises](#adjoining-premises-adj-premises)
	* [Advertisement period](#advertisement-period-advert-period)
	* [Agent contact details](#agent-contact-details-agent-contact)
	* [Agent name and address](#agent-name-and-address-agent-details)
	* [All types of development: Non-residential floorspace](#all-types-of-development-non-residential-floorspace-non-res-floorspace)
	* [Applicant contact details](#applicant-contact-details-applicant-contact)
	* [Applicant name and address](#applicant-name-and-address-applicant-details)
	* [Assessment of flood risk](#assessment-of-flood-risk-flood-risk-assessment)
	* [Authority employee/member](#authority-employee-member-conflict-of-interest)
	* [Biodiversity and geological conservation](#biodiversity-and-geological-conservation-bio-geo-arch-con)
	* [Biodiversity net gain](#biodiversity-net-gain-bng)
	* [Checklist](#checklist-checklist)
	* [Condition(s) - removal](#conditions---removal-con-remove-vary)
	* [Declaration](#declaration-declaration)
	* [Demolition](#demolition-demolition)
	* [Description of existing use, building works or activity](#description-of-existing-use-building-works-or-activity-desc-existing-use)
	* [Description of proposed works](#description-of-proposed-works-desc-proposed-works)
	* [Description of proposed works, impacts and risks](#description-of-proposed-works-impacts-and-risks-desc-work-impacts-risks)
	* [Description of the proposal](#description-of-the-proposal-proposal-details)
	* [Description of the proposal](#description-of-the-proposal-proposal-details-ldc)
	* [Description of the proposed development including any non-residential development](#description-of-the-proposed-development-including-any-non-residential-development-proposal-details-inc-non-residential)
	* [Description of use, building works or activity](#description-of-use-building-works-or-activity-use-works-activity)
	* [Description of your proposal](#description-of-your-proposal-desc-your-proposal)
	* [Designated areas](#designated-areas-designated-areas)
	* [Details of proposed advertisement(s)](#details-of-proposed-advertisements-proposed-advert-details)
	* [Discharge of condition](#discharge-of-condition-discharge-con)
	* [Eligibility](#eligibility-eligibility)
	* [Eligibility - Larger house extension](#eligibility---larger-house-extension-eligibility-extension)
	* [Eligibility - Related operations and works](#eligibility---related-operations-and-works-eligibility-related-works)
	* [Eligibility - The current building and site](#eligibility---the-current-building-and-site-eligibility-current-building)
	* [Eligibility - The proposed development](#eligibility---the-proposed-development-eligibility-proposal)
	* [Employment](#employment-employment)
	* [Equipment and method used](#equipment-and-method-used-equip-method)
	* [Existing use](#existing-use-existing-use)
	* [Explanation for proposed demolition work](#explanation-for-proposed-demolition-work-demolition-reason)
	* [Foul sewage](#foul-sewage-foul-sewage)
	* [Grounds for application](#grounds-for-application-grounds-for-application)
	* [Grounds for application (information about the existing use(s))](#grounds-for-application-information-about-the-existing-uses-grounds-existing-use)
	* [Grounds for application (information about the proposed use(s))](#grounds-for-application-information-about-the-proposed-uses-grounds-proposed-use)
	* [Grounds for application for a lawful development certificate](#grounds-for-application-for-a-lawful-development-certificate-grounds-ldc)
	* [Hazardous substances](#hazardous-substances-haz-substances)
	* [Hedgerow removal notice](#hedgerow-removal-notice-hedgerow-removal)
	* [Hours of operation](#hours-of-operation-hrs-operation)
	* [Identification of tree(s) and description of works](#identification-of-trees-and-description-of-works-tree-work-details)
	* [Immunity from listing](#immunity-from-listing-immunity-from-listing)
	* [Industrial or commercial processes and machinery](#industrial-or-commercial-processes-and-machinery-processes-machinery-waste)
	* [Information in support of a lawful development certificate](#information-in-support-of-a-lawful-development-certificate-info-support-ldc)
	* [Interest details](#interest-details-interest-details)
	* [Listed building alterations](#listed-building-alterations-lb-alter)
	* [Listed building grading](#listed-building-grading-lb-grade)
	* [Location of advertisement(s)](#location-of-advertisements-advert-location)
	* [Materials](#materials-materials)
	* [Neighbour and community consultation](#neighbour-and-community-consultation-community-consultation)
	* [Non-material amendment(s) sought](#non-material-amendments-sought-nm-amendment-details)
	* [Ownership certificates and agricultural land declaration](#ownership-certificates-and-agricultural-land-declaration-ownership-certs)
	* [Parking](#parking-parking)
	* [Part discharge of condition(s)](#part-discharge-of-conditions-part-discharge)
	* [Pedestrian and vehicle access, roads and rights of way](#pedestrian-and-vehicle-access-roads-and-rights-of-way-access-rights-of-way)
	* [Plans, drawings and other supporting material](#plans-drawings-and-other-supporting-material-plans-drawings-supporting-materials)
	* [Pre-application advice](#pre-application-advice-pre-app-advice)
	* [Related proposals](#related-proposals-related-proposals)
	* [Residential units (including conversion)](#residential-units-including-conversion-res-units)
	* [Site address details](#site-address-details-site-details)
	* [Site area](#site-area-site-area)
	* [Site information](#site-information-site-info)
	* [Site ownership](#site-ownership-site-ownership)
	* [Site visit](#site-visit-site-visit)
	* [Storage](#storage-storage-facilities)
	* [Supporting information](#supporting-information-supporting-info)
	* [Trade effluent](#trade-effluent-trade-effluent)
	* [Tree preservation order details](#tree-preservation-order-details-tpo)
	* [Trees - additional information](#trees---additional-information-trees-additional)
	* [Trees and hedges](#trees-and-hedges-trees-hedges)
	* [Trees location](#trees-location-trees-location)
	* [Trees ownership](#trees-ownership-trees-ownership)
	* [Type of development](#type-of-development-dev-type)
	* [Type of proposed advertisement(s)](#type-of-proposed-advertisements-advertisement-types)
	* [Types of application](#types-of-application-types-application)
	* [Vehicle parking](#vehicle-parking-vehicle-parking)
	* [Voluntary agreements / planning obligations](#voluntary-agreements-planning-obligations-vol-agreement)
	* [Waste storage and collection](#waste-storage-and-collection-waste-storage-collection)---

## Application model

field	| description	| data-type | required | notes
--- | --- | --- | --- | ---
reference | UUID for the application record | UUID | MUST | 
application-types[] | A list of planning application types | Enum | MUST | See [list of application types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-type.csv)
application-sub-type | Further classification of the application type for specific variations | Enum | See [list of application sub-types](https://github.com/digital-land/planning-application-data-specification/blob/main/data/planning-application-sub-type.csv)
planning-authority | The reference of the planning authority the application has been submitted to | Organisation reference | MUST | 
submission-date | Date the application is submitted. In `YYYY-MM-DD` format |	Date | MUST |	
modules[] | List of required sections/modules for this application | List |	MUST | List of predefined module references that can be used to validate the application
documents[]{} | List of submitted documents | List | MUST |	Uses a document model to capture references and details.
fee{} | The fee payable for the application | Object | MUST | 

**Document structure**

field | description | required | notes
--- | --- | --- | ---
reference | A reference for the document | MUST | This should be unique
name | The name or title of the document | MUST | 
description | Brief description of what the document contains	| MAY | Optional but useful for context
document-types[] | List of codelist references that the document covers | MUST | Use the planning requirements enum
file | The digital file or a reference to where the file is stored | MUST | Object / URL / Blob
mime-type | The document's MIME type | MAY | e.g., application/pdf, image/jpeg

**Fee structure**

field | description | required | notes
--- | --- | --- | ---
amount | The total amount due | MUST | 
amount-paid | The amount paid | MUST |
transactions[] | References to payments or financial transactions related to this application. | MAY | Useful for audit and reconciliation.

---

## Modules

These are all the modules that can be used across application types.

### Adjoining premises

* Reference: `adj-premises`
* [Discussion #25](https://github.com/digital-land/planning-application-data-specification/discussions/25)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| addresses[]{} | A list of addressed for the adjoining properties | | MUST |  |

**Address model**

field | description | data type | required | notes
-- | -- | -- | -- | --
address-test | Address details | String | MUST | 
postcode | Postcode of address if available | String | MAY | 
uprn | UPRN if known | UPRN | MAY | 

---

### Advertisement period

* Reference: `advert-period`
* [Discussion #27](https://github.com/digital-land/planning-application-data-specification/discussions/27)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advert-start-date | The start of the time period that consent to advertisement is sought | advertising | MUST | should be in `YYYY-MM-DD` format |
| advert-end-date | The end of the time period that consent to advertisement is sought | advertising | MUST | should be in `YYYY-MM-DD` format |

---

### Agent contact details

Details needed for contacting the person representing the applicant

* Reference: `agent-contact`
* [Discussion #30](https://github.com/digital-land/planning-application-data-specification/discussions/30)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent-reference | Use a reference from the agent details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

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

### Agent name and address

Details about the person representing the applicant

* Reference: `agent-details`
* [Discussion #28](https://github.com/digital-land/planning-application-data-specification/discussions/28)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| agent{} | Details of the agent | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

**Agent object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |
| company | The company the agent works for | | MAY | |
| contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

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

### All types of development: Non-residential floorspace

* Reference: `non-res-floorspace`
* [Discussion #46](https://github.com/digital-land/planning-application-data-specification/discussions/46)

field | description | application-types | required | notes
-- | -- | -- | -- | --
non-residential-change | Does the proposal involve the loss, gain, or change of non-residential floorspace? |   | MUST | Boolean (true / false).
floorspace-details[]{} | List of non-residential floorspace changes by use class |   | MAY | Required if non-residential-change is Yes.
room-details[] | List of room changes for hotels, residential institutions and hostels | | MAY | Required if change to hotels, residential institutions and hostel floorspace |

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

### Applicant contact details

Details needed for contacting the applicant

* Reference: `applicant-contact`
* [Discussion #31](https://github.com/digital-land/planning-application-data-specification/discussions/31)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicant-reference | Use a reference from the applicant details component | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Required to match contact details to a named individual | 
| contact-details{} | Details of how to contact the individual | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | |

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

### Applicant name and address

Details about the applicant

* Reference: `applicant-details`
* [Discussion #29](https://github.com/digital-land/planning-application-data-specification/discussions/29)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| applicants[]{} | Details for one or more applicants | hh;full;outline;reserved-matters;demolition-con-area;lbc;advertising;ldc;prior-approval;s73;approval-condition;consent-under-tpo;non-material-amendment;pip;extraction-oil-gas;hedgerow-removal;notice-trees-in-con-area | MUST | Rules: must be one or more named applicants |

**Applicant object**
| field | description | required | notes |
| --- | --- | --- | --- |
| reference | A reference for the person | MUST | This can be used to refer to person again elsewhere in the application |
| Person{} | Detail to help identify a person | MUST | |
| contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

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

### Assessment of flood risk

* Reference: `flood-risk-assessment`
* [Discussion #49](https://github.com/digital-land/planning-application-data-specification/discussions/49)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
flood-risk-area | Is the site within an area at risk of flooding? |   | MUST | Boolean True or False
data-provided-by | Who provided the data: Applicant or System/Service? |   | MAY | Enum (Applicant / System/Service).
flood-risk-assessment | Reference of the flood risk assessment document |   | MAY | Required if flood-risk-area is True.
within-20m-watercourse | Is the proposal within 20 metres of a watercourse? |   | MUST | Boolean True or False.
increases-flood-risk | Will the proposal increase the flood risk elsewhere? |   | MUST | Boolean True or False.
surface-water-disposal[] | How will surface water be disposed of? |   | MUST | Multiple options allowed (see [surface water disposal type enum](https://github.com/digital-land/planning-application-data-specification/discussions/195)).


---

### Authority employee/member

Any connection between the applicant or agent and the local authority’s staff or elected members that could present a conflict of interest

* Reference: `conflict-of-interest`
* [Discussion #50](https://github.com/digital-land/planning-application-data-specification/discussions/50)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared. | | MUST | Answer may be different depending on the parties involved. "With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member" |
| name | Name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how individual is related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST |

---

### Biodiversity and geological conservation

* Reference: `bio-geo-arch-con`
* [Discussion #51](https://github.com/digital-land/planning-application-data-specification/discussions/51)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
protected-species-impact | Is there a likelihood of protected and priority species being affected? |   | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
biodiversity-features-impact | Is there a likelihood of important habitats or biodiversity features being affected? |   | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
geological-features-impact | Is there a likelihood of features of geological conservation importance being affected? |   | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no
archaeological-features-impact | Is there a likelihood of features of archaeological conservation importance being affected? | extraction-oil-gas | MUST | One of [affect area enum](https://github.com/digital-land/planning-application-data-specification/discussions/201) or no

---

### Biodiversity net gain

Information to show how the development will protect or improve wildlife habitats on the site, and whether any exemptions or special rules apply

* Reference: `bng`
* [Discussion #53](https://github.com/digital-land/planning-application-data-specification/discussions/53)

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

**documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document | String | MUST | Must be provided for each document
document-name | Name of the document | String | MUST | Descriptive name for clarity

---

### Checklist

Details of the national planning requirements the applicant should submit along with the application

* Reference: `checklist`
* [Discussion #55](https://github.com/digital-land/planning-application-data-specification/discussions/55)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| national-req-types[] | List of the document types required for the given application type |  | MUST |  |

---

### Condition(s) - removal

* Reference: `con-remove-vary`
* [Discussion #56](https://github.com/digital-land/planning-application-data-specification/discussions/56)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reason | Why applicant wishes condition(s) to be removed or changed | | MUST |  |
| condition-change | State how the condition should vary | | MAY | |

---

### Declaration

Applicants and agents must declare information provided is correct

* Reference: `declaration`
* [Discussion #57](https://github.com/digital-land/planning-application-data-specification/discussions/57)

| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | | MUST | (`true` / `false`)
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |

---

### Demolition

* Reference: `demolition`
* [Discussion #60](https://github.com/digital-land/planning-application-data-specification/discussions/60)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| demolition | True or False based on whether proposal includes partial or total demolition of a listed building | lbc | MUST |  |
| demolition-total | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| demolition-building-in-curtilage | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| demolition-part | True or False | lbc | MAY | Rule: is a MUST if `demolition` is True |
| listed-building-volume | Volume of listed building in cubic metres | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST |
| demolition-volume | Volume of part to be demolished in cubic metres | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST |
| part-built-date | The approximate date the part to be removed was built | lbc | MAY | Rule: if `demolition-part` is true then this is a MUST Format should be YYYY-MM-DD. Approximate dates are allowed |
| description | Description of the the building or part you are proposing to demolish | lbc | MUST | |
| reason | Reason for demolition | lbc | MUST | |

---

### Description of existing use, building works or activity

* Reference: `desc-existing-use`
* [Discussion #61](https://github.com/digital-land/planning-application-data-specification/discussions/61)

field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details[]{} | List of existing site uses and related land areas |   | MUST | Rule: At least one use must be provided.

**existing use structure**

field | description | required | notes
-- | -- | -- | --
use | The Use class of the use | MUST | See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or other
use-details | Further detail of the use | MAY | Rule: required if `use` is `sui` or `other`
land-part | State which part of the land the `use` relates to | MUST | 

---

### Description of proposed works

* Reference: `desc-proposed-works`
* [Discussion #156](https://github.com/digital-land/planning-application-data-specification/discussions/156)

Field | Description | Data Type | Application Type | Required? | Notes
-- | -- | -- | -- | -- | --
proposed-works-details | Description of the proposed works | String |  | MUST | Detailed explanation of the work
extension-depth | How far the extension extends beyond the rear wall | Float | prior-approval | MUST | Measured externally in meters
max-extension-height | Maximum height of the extension | Float | prior-approval | MUST | Measured externally from natural ground level
eaves-height | Height at the eaves of the extension | Float | prior-approval | MUST | Measured externally from natural ground level

---

### Description of proposed works, impacts and risks

* Reference: `desc-work-impacts-risks`
* [Discussion #81](https://github.com/digital-land/planning-application-data-specification/discussions/81)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
description | Description of proposed development including details of proposed work and external appearance |  | MUST | 
dwellinghouse-height | Height from ground to highest point of roof | | MUST | Should be in metres
proposed-height | Height once the additional storeys have been added | | MUST | Should be in metres
impact-on-amenity | Details of the impacts on the amenity of any adjoining premises including overlooking, privacy and the loss of light including how these will be mitigated | | MUST | Should include mitigations
air-traffic-defence-impacts | Details of any air traffic and defence asset impacts, include how these will be mitigated | | MUST | Should include mitigations
protected-view-impact | Provide details of the impact on any protected view | | MUST | Form says where relevant

---

### Description of the proposal

Details about the proposal

* Reference: `proposal-details`
* [Discussion #45](https://github.com/digital-land/planning-application-data-specification/discussions/45)

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
| decision-data | date of the decision | If decided | |

---

### Description of the proposal

* Reference: `proposal-details-ldc`
* [Discussion #206](https://github.com/digital-land/planning-application-data-specification/discussions/206)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-incl-building-operations | True or False | ldc | MUST | Is this only for lawful development certificate for proposed work |
| proposal-building-operations-description | | ldc | MAY | If `proposal-incl-building-operations` is True then this must be filled in |
| proposal-incl-change-of-use | True or False | ldc | MUST | |
| proposal-change-of-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-description | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-existing-use-stop-date | | ldc | MAY | If `proposal-incl-change-of-use` is True then this must be filled in |
| proposal-started | True or False | ldc | MUST | |

---

### Description of the proposed development including any non-residential development

* Reference: `proposal-details-inc-non-residential`
* [Discussion #79](https://github.com/digital-land/planning-application-data-specification/discussions/79)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of proposed development including non-residential development |  | MUST | |
| net-dwellings-min | The minimum number of net additional dwellings proposed as part of the development. This accounts for any existing dwellings lost and new dwellings created. | | MUST |  |
| net-dwellings-max | The maximum number of net additional dwellings proposed as part of the development, allowing for flexibility in the final housing numbers. | | MUST |  |
| non-residential-use[]{} | The amount of non-residential use. Can be floorspace, hectares or both. | | MUST | From form: "Can be expressed as a range, a maximum or a fixed amount". This is used to check non-residential use is less than residential use |

**Non residential use structure**

| field | description | notes |
| --- | --- | --- |
| non-residential-measurement-type | The type of value being provided. `floorspace` or `site-area` | See [non-residential-measurement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/188) |
| exact-value | Exact figure of non-residential use | m2 for floorspace, hectares for site-area |
| min | Low bound of non-residential use | m2 for floorspace, hectares for site-area |
| max | Upper bound of non-residential use | m2 for floorspace, hectares for site-area |

---

### Description of use, building works or activity

Please state for which of these you need a lawful development certificate/building works (you must tick at least one option):

* Reference: `use-works-activity`
* [Discussion #62](https://github.com/digital-land/planning-application-data-specification/discussions/62)

field | description | application-types | required | notes
-- | -- | -- | -- | --
ldc-need[] | What is the lawful development certificate needed for? |   | MUST | At least one of [lawful development need enum](https://github.com/digital-land/planning-application-data-specification/discussions/205).
use | If existing-use or use-breach-of-condition is True, state the relevant Use Class |   | MAY | If `existing-use` or `breach-con-existing-use ` in `ldc-need` then applicant needs to provide `use`. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or `other`
specified-use | The specific use if no use class suitable | | MAY | Rule: must be provided if `use` is `sui` or `other`

---

### Description of your proposal

* Reference: `desc-your-proposal`
* [Discussion #63](https://github.com/digital-land/planning-application-data-specification/discussions/63)

Field | Description | Data Type | Application Type | Required? | Notes
-- | -- | -- | -- | -- | --
related-proposal{} | Details of the related planning permission | Object | s73, approval-condition, non-material-amendment | MUST | See Related Proposal Structure below.
condition-numbers[] | List of condition numbers related to this application | Array (String) | s73, approval-condition | MAY | Up to 10 condition numbers.
original-application-type | Type of original planning application | Enum | non-material-amendment | MAY | Example: 'Full', 'Householder and Listed Building'.
householder-development | Is the development to an existing dwelling-house or development within its curtilage (`true`/`false`) | Boolean | non-material-amendment | MAY | Use to calculate the fee
development-started | Whether the development has already started | Boolean | s73, approval-condition | MUST | True/False
start-date | Date when development started | Date | s73, approval-condition | MAY | Required if development-started is True.
development-completed | Whether the development has been completed | Boolean | s73, approval-condition | MUST | True/False
completion-date | Date when development was completed | Date | s73, approval-condition | MAY | Required if development-completed is True.

**Related proposal structure**

Field | Description | Required? | Notes
-- | --  | -- | --
proposal-description | Detailed description of the approved development | MUST | As shown in the decision letter.
reference-number | Reference number of the planning permission | MUST | Must match the decision letter.
decision-date | Date of the planning decision | MUST | Must be before the application submission date.


---

### Designated areas

* Reference: `designated-areas`
* [Discussion #59](https://github.com/digital-land/planning-application-data-specification/discussions/59)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
designations[] | List of designated areas that apply to the site |   | MUST | Multiple selections allowed. If None of the above is selected, no other options can be chosen. Leave blank if none. See [designations enum](https://github.com/digital-land/planning-application-data-specification/discussions/193)

---

### Details of proposed advertisement(s)

* Reference: `proposed-advert-details`
* [Discussion #82](https://github.com/digital-land/planning-application-data-specification/discussions/82)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisement[] | Structured data about each proposed advertisement |  | MUST | Rule: must be one or more entries |

**Advertisement**

| field | description | notes |
| --- | --- | --- |
| height-from-ground | Height from ground to the base of the advertisement | in metres |
| height | Height of dimensions of advertisement | in metric |
| width | Width of dimensions of advertisement | in metric |
| depth | Depth of dimensions of advertisement | in metric |
| symbol-height-max | Maximum height of any individual letters or symbols | in metric |
| colour | Colour of proposed sign | |
| materials | Materials of proposed sign | | 
| max-projection | Maximum projection of the advertisement from the face of the building | |
| illuminated | True or False. Will the sign(s) be illuminated? | |
| illumination-method | | Required if `illuminated` is true |
| illuminance-level | | Required if `illuminated` is true. cd/m2 |
| illumination-type | Static or intermittent | Required if `illuminated` is true. Is an illumination-type codelist required? |

---

### Discharge of condition

* Reference: `discharge-con`
* [Discussion #149](https://github.com/digital-land/planning-application-data-specification/discussions/149)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description-list | Description or list of materials/details that are being submitted for approval | approval-condition | MUST |  |

---

### Eligibility

* Reference: `eligibility`
* [Discussion #44](https://github.com/digital-land/planning-application-data-specification/discussions/44)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
applicant-land-interest | Does the applicant have an interest in the land? (True/False) |   | MUST | If False, application cannot proceed.
ownership-notification | If not the sole owner, has notification been given under Article 10? (Enum) |   | MAY | One of Yes, No, Not Applicable. Required if applicant is not sole owner.
notified-persons[]{} | List of persons notified, including address and date |   | CONDITIONAL | Rule: Required if `ownership-notification` is Yes.

**Notified person**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person-notified | Name of the person notified | String | MUST | Full name.
address | Address of the person notified | String | MUST | Full postal address.
date-of-notification | Date notification was sent | Date | MUST | Format: YYYY-MM-DD.

---

### Eligibility - Larger house extension

* Reference: `eligibility-extension`
* [Discussion #192](https://github.com/digital-land/planning-application-data-specification/discussions/192)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
single-storey-extension | Will the extension be a single storey? (True/False) |   | MUST | If False, the application cannot proceed.
extension-height-over-4m | Will the extension exceed 4 metres in height? (True/False) |   | MUST | If True, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
rear-extension-length | Will the extension extend beyond the rear wall of the original dwelling? |   | MUST | See conditional logic for limits based on attachment type.
extension-length | Length of rear extension (in metres) |   | MUST | 
within-site-constraints | Is the dwellinghouse within any restricted area? (True/False) |   | MUST | If True, the application cannot proceed.
site-constraints[] | List of specific site constraints |   | MAY | Rule: Required if within-site-restrictions is True. See [site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)

---

### Eligibility - Related operations and works

* Reference: `eligibility-related-works`
* [Discussion #87](https://github.com/digital-land/planning-application-data-specification/discussions/87)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| external-support-required | Will the proposed engineering works include external support structures or extend beyond the curtilage for wall or foundation strengthening? | | MUST | Impacts whether prior approval is applicable. True or False |

---

### Eligibility - The current building and site

* Reference: `eligibility-current-building`
* [Discussion #88](https://github.com/digital-land/planning-application-data-specification/discussions/88)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
in-building-construction-period | Was the current building constructed between 1 July 1948 and 28 October 2018? (`True`/`False`) |   | MUST | One of True, False. If False, application cannot proceed.
additional-storeys-added | Have additional storeys already been added to the original building? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
dwelling-permitted-use | Was the current use of the building granted by permitted development rights? (`True`/`False`) |   | MUST | One of True, False. If True, application cannot proceed
site-location-constraint | Is any part of the land or site located in a restricted area? (`True`/`False`)  |   | MUST | One of True, False. If True, application cannot proceed

---

### Eligibility - The proposed development

* Reference: `eligibility-proposal`
* [Discussion #89](https://github.com/digital-land/planning-application-data-specification/discussions/89)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
principal-part-only | Will the additional storeys be constructed only on the principal part of the building? |   | MUST | If No, the application cannot proceed.
ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any additional storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
existing-ceiling-height-exceeds-3m | Will the internal floor-to-ceiling height of any existing storey exceed 3 metres? |   | MUST | If Yes, the application cannot proceed.
building-height-exceeds-18m | Will the height of the extended building exceed 18 metres? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-3-5m | Will the roof exceed 3.5 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
roof-height-exceeds-7m | Will the roof exceed 7 metres above the highest part of the existing roof? |   | MUST | If Yes, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
extension-on-attached-dwelling | Will the extension result in the highest part exceeding 3.5 metres above the attached roof? |   | MAY | Only applicable if the dwelling is not detached.
extension-below-terrace-roof | Will th extension result in the highest part exceeding 3.5 metres above any roof in the terrace? |   | MAY | Only applicable if the dwelling is not detached.
roof-pitch-matching | Will the roof pitch of the extended dwelling match the existing roof pitch? |   | MUST | If No, the application cannot proceed.
window-on-side-elevation | Will the development include a side elevation window or roof slope window? |   | MUST | If Yes, further assessment may be required.
materials-similar-exterior | Will exterior materials be similar to those of the existing dwelling? |   | MUST | If No, the application cannot proceed.
dwellinghouse-use | Will the extended dwelling remain as a Class C3 dwellinghouse or ancillary use? |   | MUST | If No, the application cannot proceed.

---

### Employment

Please complete the following information regarding employees

* Reference: `employment`
* [Discussion #43](https://github.com/digital-land/planning-application-data-specification/discussions/43)

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

### Equipment and method used

* Reference: `equip-method`
* [Discussion #85](https://github.com/digital-land/planning-application-data-specification/discussions/85)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| equipment-plan | Details of equipment to be used as part of the application including the maximum height and type of drilling rig to be used | extraction-oil-gas | MUST | |

---

### Existing use

* Reference: `existing-use`
* [Discussion #42](https://github.com/digital-land/planning-application-data-specification/discussions/42)

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

### Explanation for proposed demolition work

* Reference: `demolition-reason`
* [Discussion #86](https://github.com/digital-land/planning-application-data-specification/discussions/86)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
demolition-reason | Explanation of why demolition is necessary | | MUST | 

---

### Foul sewage

* Reference: `foul-sewage`
* [Discussion #41](https://github.com/digital-land/planning-application-data-specification/discussions/41)

Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
foul-sewage-disposal-types[] | List of ways foul sewage will be disposed of | | MUST | See [foul-sewage-disposal-type ENUM](https://github.com/digital-land/planning-application-data-specification/discussions/165)
produce-foul-sewage | Proposed development produce any foul sewage (True/False) | extraction-oil-gas | MUST | 
connect-to-drainage-system | Does the proposal need to connect to the existing drainage system (True/False) | | MUST | 
drainage-system-details | Details of the drawings/plans that show the existing system | | MAY | Rule, is a MUST if `connect-to-drainage-system` is TRUE or `extraction-oil-gas` application 

---

### Grounds for application

* Reference: `grounds-for-application`
* [Discussion #90](https://github.com/digital-land/planning-application-data-specification/discussions/90)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| grounds-for-application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted including why listed building consent is not required |  | MUST | |
| documents[] | Reference(s) to any supporting documentary evidence| | MUST |  |

---

### Grounds for application (information about the existing use(s))

* Reference: `grounds-existing-use`
* [Discussion #92](https://github.com/digital-land/planning-application-data-specification/discussions/92)

field | description | application-types | required | notes
-- | -- | -- | -- | --
use-lawful-reason | Explanation of why the existing or last use is lawful |   | MUST | 
documents[] | List of supporting documentary evidence |   | MAY | Optional unless evidence is needed to support the justification.
use | Stated use class of the existing or last use (if applicable) |   | MAY | Use [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) (e.g., C3, B1, E).
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`

---

### Grounds for application (information about the proposed use(s))

* Reference: `grounds-proposed-use`
* [Discussion #93](https://github.com/digital-land/planning-application-data-specification/discussions/93)

field | description | application-type | required? | notes
-- | -- | -- | -- | --
use | State proposed use class | | MAY | Applicant's view of the relevant Use Class, if applicable. (see [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189))
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`
operation-type | Whether the proposed use is temporary or permanent | | MUST | Uses [operation type enum](https://github.com/digital-land/planning-application-data-specification/discussions/203).
temporary-details | Details of temporary use | | MAY | Required if operation-type is temporary.
reason | Reason why the development is considered lawful | | MUST | Explanation supporting the certificate application.

---

### Grounds for application for a lawful development certificate

* Reference: `grounds-ldc`
* [Discussion #91](https://github.com/digital-land/planning-application-data-specification/discussions/91)

Field | Description | Application-type | Required? | Notes
-- | -- | -- | -- | --
grounds[] | List of grounds under which the certificate is sought | | MUST | At least one ground must be selected. See [Grounds Enum](https://github.com/digital-land/planning-application-data-specification/discussions/204) .
other-details | Explanation if "Other" ground is selected | | MAY | Required if grounds[] includes other.
supporting-applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site. Include its date and the number of any condition being breached | | MAY | Optional, but strengthens the application.
reason | Reason why the development is considered lawful | | MUST | Applicant’s explanation for granting the certificate.

**Supporting applications / decisions**

_This is similar to other models where supporting or related applications are required. the difference being that this one also needs the condition number._

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Reference number of planning permission, certificate, or notice | String | MAY | Optional, strengthens application.
condition-number | Number of any condition being breached | String | MAY | Relevant if certificate relates to condition breach.
decision-date | Date of the decision (DD/MM/YYYY) | Date | MAY | Must be before the application submission date.

---

### Hazardous substances

* Reference: `haz-substances`
* [Discussion #40](https://github.com/digital-land/planning-application-data-specification/discussions/40)

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

### Hedgerow removal notice

This section is used to provide details about the hedgerows being removed

* Reference: `hedgerow-removal`
* [Discussion #217](https://github.com/digital-land/planning-application-data-specification/discussions/217)

field | description | application-types |	required | notes
--- | --- | --- | --- | ---
removal-reasons | Reasons for the proposed removal of hedgerow(s) | hedgerow-removal | MUST |
plan-references[] | References to plans showing the stretches of hedgerows to be removed | hedgerow-removal | MUST | References should be document references from `application.documents`
hedgerow-length | Total length of hedgerow proposed for removal (in metres) | hedgerow-removal | MUST	|Rule: Must be a positive number
hedgerow-less-than-30-years | Is the hedgerow less than 30 years old? (`true`/`false`) | hedgerow-removal | MUST |	
planting-evidence-attached | Is evidence of the date of planting attached?	(`true`/`false`) | hedgerow-removal | MAY |	Required if `hedgerow-less-than-30-years` is `true`
interest-declaration | The applicant's interest or ownership | hedgerow-removal | MUST | See the [hedegerow interest declaration enum](https://github.com/digital-land/planning-application-data-specification/discussions/216)

---

### Hours of operation

Please state the hours of opening for each non-residential use proposed:

* Reference: `hrs-operation`
* [Discussion #39](https://github.com/digital-land/planning-application-data-specification/discussions/39)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| hours-of-operation[]{} | List the hours of operation by non-residential use | | MUST | |
| additional-information | Any additional detail about operational hours | extraction-oil-gas | MAY | |

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

### Identification of tree(s) and description of works

* Reference: `tree-work-details`
* [Discussion #94](https://github.com/digital-land/planning-application-data-specification/discussions/94)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of work applicant wishes to carry out. It should include identifying the trees, species and setting out the work | notice-trees-in-con-area;consent-under-tpo | MUST | |
| tree-details[]{} | Details of each tree that is part of the proposal | notice-trees-in-con-area;consent-under-tpo | MAY | |

**tree details structure**

field | description | application-type
-- | -- | --
reference | Identifier for the tree, use the TPO identifier is applicable |  
species | The species of the tree  |  
description-of-works | Describe the nature of the work to this tree  |  
reason | Explain the reason for the work | tpo
replanting-description | Details of replanting | tpo

---

### Immunity from listing

* Reference: `immunity-from-listing`
* [Discussion #38](https://github.com/digital-land/planning-application-data-specification/discussions/38)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| cert-of-im-sought | Has a certificate of immunity been sought. Options: Yes, No, Don't know |  | MUST |  |
| application-result | Provide the result of the application | | MAY | Rule: is required if `cert-of-im-sought` is True |

---

### Industrial or commercial processes and machinery

* Reference: `processes-machinery-waste`
* [Discussion #95](https://github.com/digital-land/planning-application-data-specification/discussions/95)

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

### Information in support of a lawful development certificate

* Reference: `info-support-ldc`
* [Discussion #96](https://github.com/digital-land/planning-application-data-specification/discussions/96)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| existing-use-start-date | YYYY-MM-DD | | MUST | |
| existing-use-interrupted | True or False | | MUST | |
| interruption-details | | | MAY | Rule, is a MUST if `existing-use-interrupted` is True |
| existing-use-change | True or False | | MUST | |
| existing-use-change-details | | | MAY | Rule, is a MUST if `existing-use-change` is True |

---

### Interest details

This section collects information on who owns the land or building and the applicants interest

* Reference: `interest-details`
* [Discussion #212](https://github.com/digital-land/planning-application-data-specification/discussions/212)

field | description | application-Types | required | notes
-- | -- | -- | -- | --
applicant-interest | Applicant's interest in the land/listed building | ldc | MUST | One of: see [applicant's interest type enum](https://github.com/digital-land/planning-application-data-specification/discussions/202) or `None`.
owner-details[]{} | Details of the owner if the applicant is a lessee or occupier | ldc | MAY | Rule: Required if `applicant-interest` is Lessee or Occupier.
interested-persons[]{} | Details of other interested persons in the listed building | ldc | MAY | Rule: Required if `applicant-interest` is None.
applicant-owns-land | Does the applicant own the land? (`True`/`False`) | advertising | MUST |
permission-obtained | Has permission of the owner for the display of an advertisement been obtained? | advertising | MAY | Rule is a MUST if `applicant-owns-land` is `False` |
| permission-not-obtained-details | Details if permission from the owner has not been obtained | advertising | MAY | Rule is a MUST if `applicant-owns-land` is `False` and `permission-obtained` is `False` |

The [legislation](https://www.legislation.gov.uk/uksi/2007/783/schedule/2) states "No advertisement is to be displayed without the permission of the owner of the site or any other person with an interest in the site entitled to grant permission."

**Owner(s) model**

field | description | data type | required | notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.

**Interested persons model**

field | description | data type | required | notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
nature-of-interest | Nature of the interest in the building | String | MUST | 
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.
reason-not-informed | Reason why they were not informed | String | MAY | Rule: Required if `informed-of-application` is `False`.

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| post-code | The post code for the address provided | MAY | |

---

### Listed building alterations

* Reference: `lb-alter`
* [Discussion #99](https://github.com/digital-land/planning-application-data-specification/discussions/99)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| proposal-alter-lb | True or False if proposal includes alterations |  | MUST |  |
| proposal-alter-lb-types[] | Select from a list of listed building alteration types, select all that apply | | MAY | Rule: is required if `proposal-alter-lb` is True |
| document-reference[] | References to documents detailing the proposed alterations | | MAY | Rule: is required if `proposal-alter-lb` is True |

See [listed building alteration types enum](https://github.com/digital-land/planning-application-data-specification/discussions/187)

---

### Listed building grading

* Reference: `lb-grade`
* [Discussion #36](https://github.com/digital-land/planning-application-data-specification/discussions/36)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| listed-building-grade | Selected from [listed-building-grade](https://dluhc-datasets.planning-data.dev/dataset/listed-building-grade) or "don't know" |  | MUST | Note the certificate of lawfulness apps do not ask about ecclesiastical grades |
| listed-building | Provide the listed building reference | | MAY | Would make it easier to cross-reference with the official listing |
| provided-by | Details of source of the data. `Applicant` or `System/Service` | | MAY | This can be used by authority to determine if they need to check the data they have been provided |

---

### Location of advertisement(s)

* Reference: `advert-location`
* [Discussion #64](https://github.com/digital-land/planning-application-data-specification/discussions/64)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-advert-in-place | True of False |  | MUST | |
| advert-placed-date | YYYY-MM-DD | | MAY | Rule is a MUST if `is-advert-in-place` is True |
| is-replacement-advert | True or False | | MUST |  |
| document-reference[] | References to drawings and photos showing existing signs | | MAY | Rule is a MUST if `is-advert-in-place` OR  `is-replacement-advert` are True |
| is-advert-overhanging | True or False if advertisement will project over a footpath or other public highway | | MUST | |

---

### Materials

Where details about the materials to be used or changed should be provided, including type, colour and name for each material

* Reference: `materials`
* [Discussion #26](https://github.com/digital-land/planning-application-data-specification/discussions/26)

**Materials**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element[]{} | List of building elements where materials are being described (e.g., walls, roof). |  | MUST | See Building element structure. One entry per building element.
additional-material-information | Indicates whether additional documents are provided to supplement the materials description |  | MUST | (`true` or `false`).
supporting-documents[] | Details for documents providing additional material information. |  | MAY | Required if additional-material-information is true.


**Building element**
| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
building-element-type | Identifies the part of the building the materials relate to, such as walls, roofs, windows, or doors. | MUST | Must use values from the [building element types enum](https://github.com/digital-land/planning-application-data-specification/discussions/207).
existing-materials | Description of the materials currently used for this building element. | MAY | Complete if known and applicable.
proposed-materials | Description of the materials proposed for this building element as part of the development. | MAY | Complete if known and applicable.
materials-not-applicable | Indicates that material details are not applicable for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.
materials-not-known | Indicates that the materials are unknown for this building element. | MAY | Boolean: true or false. Required if both existing-materials and proposed-materials are left blank.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Neighbour and community consultation

* Reference: `community-consultation`
* [Discussion #65](https://github.com/digital-land/planning-application-data-specification/discussions/65)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| have-consulted | True or False |  | MUST | |
| description | Provide details of consultation | | MAY | Rule: is a MUST if `neighbours-consulted` is True |

---

### Non-material amendment(s) sought

* Reference: `nm-amendment-details`
* [Discussion #76](https://github.com/digital-land/planning-application-data-specification/discussions/76)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | Description of the non-material amendments the applicant seeks to make | | MUST | |
| substituting-document | True or False | | MUST | |
| replacement-documents[] | address, if available for the site | | MAY | Rule, is a MUST if is True |
| reason | Reason why applicant wants to make the amendment | | MUST | |

**Replacement-document**

| field | description | required | notes |
| --- | --- | --- | --- |
| old-document | Reference of the old document | MUST | |
| new-document | Reference for the new document | MUST | |

---

### Ownership certificates and agricultural land declaration

Ownership of the site and/or property for development needs to be understood

* Reference: `ownership-certs`
* [Discussion #78](https://github.com/digital-land/planning-application-data-specification/discussions/78)

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

### Parking

Details of how the proposed development will affect the parking area required

* Reference: `parking`
* [Discussion #66](https://github.com/digital-land/planning-application-data-specification/discussions/66)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| description | A description of how the proposed works will affect existing car parking arrangements | hh | MAY | |

---

### Part discharge of condition(s)

* Reference: `part-discharge`
* [Discussion #140](https://github.com/digital-land/planning-application-data-specification/discussions/140)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| discharging-part | Is applicant trying to discharge part of condition? (True or False) | | MUST |  |
| discharging-part-details | Indicate which part of the condition the application relates to | | MAY | Rule, is MUST if `discharging-part` is true |

---

### Pedestrian and vehicle access, roads and rights of way

Any changes to how people or vehicles access the site, including any new or affected roads, footpaths, or public rights of way

* Reference: `access-rights-of-way`
* [Discussion #100](https://github.com/digital-land/planning-application-data-specification/discussions/100)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | Is a new or altered vehicle access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-altered-pedestrian | Is a new or altered pedestrian access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| change-right-of-way | Will the proposal change public rights of way? (diversion/extinguishment/creation) | full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers.|
| new-right-of-way | Will new public rights of way be provided within or adjacent to the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-public-road | Will new public roads be provided within the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| temp-right-of-way | Are temporary changes to rights of way needed while the site is worked? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| future-new-right-of-way | Will new public rights of way be provided after extraction? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| supporting-documents[]{} | List of document supporting the information provided | extraction-oil-gas;full;hh;outline | MAY | Required if any answer is `true`. |

---

### Plans, drawings and other supporting material

* Reference: `plans-drawings-supporting-materials`
* [Discussion #102](https://github.com/digital-land/planning-application-data-specification/discussions/102)

Field | Description | application-type | Required? | Notes
-- | -- | -- | -- | --
documents[]{} | List of plans, drawings, and supporting documents |  | MUST | See Document Structure below.
inspection-address | Address where supporting material can be inspected |  | MUST | Full postal address for document inspection.

**documents**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Pre-application advice

Details of pre-application advice received from the local planning authority

* Reference: `pre-app-advice`
* [Discussion #35](https://github.com/digital-land/planning-application-data-specification/discussions/35)


| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advice-sought | Has pre-application advice has been sought | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MUST | Boolean (`true`/`false`) |
| officer-name | Name of officer who dealt with pre-app advice | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| reference | Reference for pre-application advice application | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-date | Date applicant received the advice, in `YYYY-MM-DD` format | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | |
| advice-summary | Summary of the advice received | hh;full;outline;demolition-con-area;lbc;ldc;reserved-matters;advertising;s73;approval-condition;non-material-amendment;extraction-oil-gas | MAY | is this necessary if they have provided the reference? |

---

### Related proposals

* Reference: `related-proposals`
* [Discussion #34](https://github.com/digital-land/planning-application-data-specification/discussions/34)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| has-related-proposals | True of False. True if any related applications, previous proposals or demolitions for the site |  | MUST | |
| related-proposal[] | List of related applications | MAY | Rule is a MUST if `has-related-proposals` is True |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided | |

---

### Residential units (including conversion)

* Reference: `res-units`
* [Discussion #33](https://github.com/digital-land/planning-application-data-specification/discussions/33)

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

### Site address details

Details to locate the site proposed for development

* Reference: `site-details`
* [Discussion #70](https://github.com/digital-land/planning-application-data-specification/discussions/70)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-locations[]{} | Details of the sites on which the tree(s) are located | notice-trees-in-con-area;consent-under-tpo | MAY | Rule: only required if the site is different from the applicant's address | 

**site-location/details structure**

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

### Site area

* Reference: `site-area`
* [Discussion #103](https://github.com/digital-land/planning-application-data-specification/discussions/103)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-area |  | | MUST | In hectares. Ideally should be calculated from site boundary. |
| site-area-provided-by | Either Applicant or System/Service | | MAY | Authority can use this to determine if they need to check the calculation |

---

### Site information

* Reference: `site-info`
* [Discussion #104](https://github.com/digital-land/planning-application-data-specification/discussions/104)

## Site information 

Field | Description | Application-Types | Required? | Notes
-- | -- | -- | -- | --
site-area{} | The total area of the site |   | MUST | See "Site Area Structure" below
existing-use[]{} | Structured information on the current use of the site |   | MUST | An array, as there may be multiple uses (see "Existing Use Structure")
known-constraints[] | A list of the known constraints affecting the site |   | MUST | See the [Site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)
supporting-documents[]{} | A list of documents with the supporting information for the idenitifed site constraints | MAY | Rule: a MUST if `known-constraints` is not empty

### Site Area Structure

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
value | Numeric value representing site area | Number | MUST | Should ideally be calculated from site boundary
unit | Unit of measurement for site area | Enum | MUST | One of: m2, hectares
provided-by | Whether the site area was provided by the applicant or system |   | MAY | Enum: Applicant, System/Service

### Existing Use Structure

field | description | data type | required? | notes
-- | -- | -- | -- | --
uses[]{} | List of applicable uses | Enum | MUST | Mixed-use sites can list multiple classes. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
floorspace | Total floorspace for the use | Number | MUST | Numeric value. Expected in m2

**Use structure**
field | description | data-type | required | notes
--- | --- | --- | --- | ---
use | A non-residential use | Enum+other | MUST | 
specified-use | A specified use if no applicable use class | String | MAY | Rule: must if `use` is `sui` or `other`

**documents structure**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
details | Additional details about the document, for example, details about the constraint it references | String | MAY | 

---

### Site ownership

* Reference: `site-ownership`
* [Discussion #105](https://github.com/digital-land/planning-application-data-specification/discussions/105)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-owner{} | | | MUST |  |
| applicant-interest | Description of applicant's interest in the land | | MUST |  |
| applicant-interest-adjoining-land | Description of applicant's interest in the adjacent land | | MUST |  |

**Site-owner** 
| field | description | required | notes |
| --- | --- | --- | --- |
| fullname | | MUST |  |
| address-text | | MUST |  |

---

### Site visit

Details needed to support a site visit

* Reference: `site-visit`
* [Discussion #32](https://github.com/digital-land/planning-application-data-specification/discussions/32)

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

### Storage

* Reference: `storage-facilities`
* [Discussion #67](https://github.com/digital-land/planning-application-data-specification/discussions/67)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| `storage-facilities-description` | Details and proposed facilities for the storage of oil, fuel and chemicals and the proposed means of their protection | | MUST | | 

---

### Supporting information

* Reference: `supporting-info`
* [Discussion #107](https://github.com/digital-land/planning-application-data-specification/discussions/107)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| replacement-drawings[]{} | List of approved drawings being replaced by new drawings | | MUST | |

**Replacement-document**

| field | description | required | notes |
| --- | --- | --- | --- |
| old-drawing | Reference of the old drawing | MUST | |
| new-drawing | Reference for the new drawing | MUST | |
| reason | Reason for replacing the drawing | | MAY |  |

---

### Trade effluent

* Reference: `trade-effluent`
* [Discussion #74](https://github.com/digital-land/planning-application-data-specification/discussions/74)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| `disposal-required` | True or False depending on if proposal involves the disposal of trade effluents or waste | | MUST | | 
| `description` | Describe the nature, volume and means of disposal of trade effluents or waste | | MAY | Rule: is a MUST if `disposal-required` is True |

---

### Tree preservation order details

* Reference: `tpo`
* [Discussion #108](https://github.com/digital-land/planning-application-data-specification/discussions/108)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| tpo-reference[] | List of references for the TPOs covering the affected trees | consent-under-tpo | MAY | Applicant only has to provide if known |
| tpo-provided-by | How was the list of references generated? Was it by the Applicant or System/Service | consent-under-tpo | MAY | Authority can use this to determine if they need to check reference |

---

### Trees - additional information

* Reference: `trees-additional`
* [Discussion #109](https://github.com/digital-land/planning-application-data-specification/discussions/109)

field | description | application-types | required | notes
--- | --- | --- | --- | ---
advice-from-authority | Any advice provided on-site by a Local Planning Authority (LPA) officer | consent-under-tpo;notice-trees-in-con-area | MAY | 
condition-concerns | Are there concerns the tree(s) are diseased or might break or fall? (`true`/`false`) | consent-under-tpo | MUST | Rule: if true then Arboricultural impact assessment document is required
causing-subsidence | Is subsidence damage being caused by the tree(s)? (`true`/`false`) | consent-under-tpo | MUST | Rule: if `true` then Subsidence Report is required
causing-structural-damage | Is structural damage being caused by the tree(s)? (`true`/`false`) | consent-under-tpo | MUST | Rule: if `true` then a Structural damage report is required
supporting-documents[]{} | A list of the documents supporting the work required to trees | consent-under-tpo;notice-trees-in-con-area | MUST | Rule: must include sketch plan, supporting documents, reports, or photographs and any documents required given the answers to the above questions

**Supporting document structure**

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity
description | Description of the document | String | MAY | Optional description of the document

---

### Trees and hedges

Details of trees and hedges affecting the site or that will be affected by the proposed development

* Reference: `trees-hedges`
* [Discussion #110](https://github.com/digital-land/planning-application-data-specification/discussions/110)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| falling-trees-risk | There are falling trees on-premises or adjacent premises that are a risk to the development. (`true`/`false`) | hh | MUST | |
| falling-trees-document{} | Details of document showing location of trees | hh | MAY | Rule: is a MUST if `falling-trees-risk` is `true` |
| tree-removal | Do trees or hedges need to be pruned or removed (`true`/`false`) | hh | MUST | |
| tree-removal-plan{} | Details of document showing location of trees and hedges | hh | MAY | Rule: is a MUST of ` tree-removal` is `true` |
| trees-on-site | Trees or hedges are on the proposed development site (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |
| trees-on-adj-land | Trees or hedges on land adjacent to the proposed development site that could influence the development or might be important as part of the local landscape character (`true`/`false`) | full;outline-some;extraction-oil-gas | MUST | |

**tree removal plan**

field | description | data type | required? | notes
-- | -- | -- | -- | --
document-reference | Unique identifier for the document | String | MUST | Must be provided for each document
name | Name of the document | String | MUST | Descriptive name for clarity

---

### Trees location

* Reference: `trees-location`
* [Discussion #111](https://github.com/digital-land/planning-application-data-specification/discussions/111)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| site-locations[]{} | Details of the sites on which the tree(s) are located | notice-trees-in-con-area;consent-under-tpo | MAY | Rule: only required if the site is different from the applicant's address | 

**site-location/details structure**

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

One of these must be provided per site:
* site-boundary
* address
* easting + northing

Applicant only needs to provide this if the site is different from their address

---

### Trees ownership

* Reference: `trees-ownership`
* [Discussion #112](https://github.com/digital-land/planning-application-data-specification/discussions/112)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| is-applicant-owner | Does the applicant own the trees? (`true`/`false`) | notice-trees-in-con-area;consent-under-tpo | MUST | |
| owner[]{} | Details of the owner | | MAY | Rule: required if `is-applicant-owner` is `false` |

**Owner structure**
| field | description | required | notes |
| --- | --- | --- | --- |
| Person{} | Detail to help identify a person | MUST | |
| contact-details{} | Details of how to contact the individual | MAY | Rule: is a MUST if `application-type` is `pip` |

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

### Type of development

* Reference: `dev-type`
* [Discussion #113](https://github.com/digital-land/planning-application-data-specification/discussions/113)

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

### Type of proposed advertisement(s)

* Reference: `advertisement-types`
* [Discussion #114](https://github.com/digital-land/planning-application-data-specification/discussions/114)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisement-proposal-description |  |  | MUST | |
| advertisement-proposal-type[]{} | Expected to provide counts for each advertisement type | | MUST |  |

**advertisement-proposal-type**

| field | description | notes |
| --- | --- | --- |
| advertisement-type | one of the advertisement-types or other | see [advertisement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/190) |
| advertisement-count | number of this type of advertisement | |
| advertisement-other-description | If other is selected then details are required | |

---

### Types of application

* Reference: `types-application`
* [Discussion #73](https://github.com/digital-land/planning-application-data-specification/discussions/73)

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
permission-types[] | List of permission types being applied for | Array | MUST | One or more from the [permission types enum](https://github.com/digital-land/planning-application-data-specification/discussions/198).
related-proposals[]{} | List of related proposals with reference and decision dates | Array | MAY | Required if any application type involves prior permissions.
other-details | | String | MAY |  If there are other details not covered by the application types 
consolidate-permissions | Is the applicant willing to consolidate or update existing permissions? | Boolean | MUST | Yes / No. If Yes, further details are required.
consolidate-details | Details about the consolidation or update of permissions | String | CONDITIONAL | Required if consolidate-permissions is Yes.

**Related proposals** 

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
proposal-type | Type of related proposal | Enum | MUST | Enum value from Application Type
reference-number | Reference number of the related proposal | String | MUST | Unique identifier for the proposal
decision-date | Decision date of the related proposal | Date | MUST | Format: YYYY-MM-DD.

---

### Vehicle parking

Please provide information on the existing and proposed number of on-site parking spaces: 

* Reference: `vehicle-parking`
* [Discussion #72](https://github.com/digital-land/planning-application-data-specification/discussions/72)

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

### Voluntary agreements / planning obligations

* Reference: `vol-agreement`
* [Discussion #115](https://github.com/digital-land/planning-application-data-specification/discussions/115)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| draft-agreement-included | outline or draft agreement included? (True / False) | | MUST | |
| agreement-summary | Summary of the agreement | | MAY | Rule: is a MUST if `draft-agreement-included` is True |

---

### Waste storage and collection

* Reference: `waste-storage-collection`
* [Discussion #84](https://github.com/digital-land/planning-application-data-specification/discussions/84)

| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| needs-waste-storage-area | True or False | | MUST | |
| waste-storage-area-details | | | MAY | Rule, is a MUST if `needs-waste-storage-area` is True |
| separate-recycling-arrangements | True or False | | MUST | |
| separate-recycling-arrangements-details | | | MAY | Rule, is a MUST if `separate-recycling-arrangements` is True |

---

