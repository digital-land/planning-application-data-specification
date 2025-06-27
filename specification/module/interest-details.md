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
| postcode | The post code for the address provided | MAY | |
