Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
applicant-interest | Applicant's interest in the listed building (Enum) |   | MUST | One of: see [applicant's interest type enum](https://github.com/digital-land/planning-application-data-specification/discussions/202) or `None`.
owner-details[] | Details of the owner if the applicant is a lessee or occupier |   | MAY | Rule: Required if `applicant-interest` is Lessee or Occupier.
interested-persons[] | Details of other interested persons in the listed building |   | MAY | Rule: Required if applicant-interest is None.

**Owner(s) model**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.

**Interested persons model**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person{} | Details of the interested person | Person Model | MUST | Structured as per [Person model](https://github.com/digital-land/planning-application-data-specification/discussions/147).
nature-of-interest | Nature of the interest in the building | String | MUST | E.g., ownership, tenancy, heritage group.
informed-of-application | Have they been informed? | Boolean | MUST | True if they were informed.
reason-not-informed | Reason why they were not informed | String | CONDITIONAL | Rule: Required if informed-of-application is False.

**Person object**
| field | description | required | notes |
| --- | --- | --- | --- |
| title | Title of individual | MAY |  |
| first-name | First name of the individual | MUST |  |
| last-name | last name of the individual | MUST |  |
| address-text | The address that can be used to correspond with the applicant| MUST | |
| postcode | The post code for the address provided | MAY | |
