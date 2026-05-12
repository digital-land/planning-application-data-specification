# Eligibility

Whether certain eligibility criteria has been met and the right people notified

**Eligibility module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| applicant-land-interest | Applicant land interest | Does the applicant have an interest in the land |  | MUST |  |
| ownership-notification | Ownership notification | If not the sole owner, has notification been given under Article 10 |  | MAY | Select from the **yes-no-not-applicable** enum |
| notified-persons | Notified persons[]{} | List of persons notified, including address and date |  | MAY | Rule: is a MUST if `ownership-notification` is `True` |


**Notified person component**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | details of the owner (or tenant when not a listed building consent application) | MAY | 
notice-date | Notice date | Date when notice was served | MAY | 


**Person obj component**

field | name | description | required | notes
-- | -- | -- | -- | --
title | Title | The title of the individual | MAY | 
first-name | First Name | The first name of the individual | MUST | 
last-name | Last Name | The last name of the individual | MUST | 
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 

**Validation rules**

- applicant-land-interest == true (required for application to proceed)
- if applicant-land-interest == 'partial', then ownership-notification is required
- if ownership-notification == 'yes', then notified-persons must be provided
- if ownership-notification == 'no', application cannot proceed without valid justification