| field | description | application-types | data-type | required | notes |
| --- | --- | --- | --- | --- | --- |
| bng-exempt | Applicants for planning permission are required to make a statement as to whether they believe the biodiversity gain condition will apply if permission is granted. Householder applicants need to confirm the biodiversity gain condition does not apply. (`true`/`false`) | hh | Boolean | MUST | |
| bng-condition-applies | Does the applicant believe the Biodiversity Gain Condition applies? | full;outline;demolition-con-area | Boolean | MUST | |
| bng-condition-exemption-reasons[]{} | Reason why BNG does not apply, referencing exemptions or transitional arrangements | full;outline;demolition-con-area | String | MAY | | Rule: Required if `bng-condition-applies` = False. See exemption reason structure |
| bng-details{} | Biodiversity net gain details | full;outline;demolition-con-area | Object | MAY | Rule: is MUST if bng-condition-applies = True |

Rule: if `application-types` includes `hh` (the householder application) then only the `bng-exempt` field is required

**Exemption reason** structure

field | description | required | notes
--- | --- | --- | ---
exemption-type | The type of exemption | MUST | Selected from the bng-exemption-type enum
reason | The reason the exemption applies to this proposal | MUST |


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
