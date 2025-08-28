# Trees ownership

Information about ownership of trees affected by the proposed works


| is-applicant-owner | Is applicant owner | Whether the applicant owns the trees affected by the proposed works | notice-trees-in-con-area, consent-under-tpo | MUST |  |
| owner | Tree owner[]{} | Details of the tree owner when applicant is not the owner | notice-trees-in-con-area, consent-under-tpo | MAY | Rule: is a MUST if `is-applicant-owner` is `False` |


**Tree owner model**

field | name | description | required | notes
-- | -- | -- | -- | --
person | Person{} | Personal identification details of the tree owner | MUST | 
contact-details | Contact details{} | Contact information for the tree owner | MAY | 


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