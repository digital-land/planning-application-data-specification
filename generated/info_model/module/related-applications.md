# Related applications

Information about related applications, previous proposals or demolitions for the site, including whether such proposals exist and details of any related applications


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| has-related-applications | Has related applications | Are there any related applications, previous proposals or demolitions for the site |  | MUST |  |
| related-applications | Related applications[]{} | List of related applications, previous proposals or demolitions for the site |  | MAY |  |


**Related application details model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MUST | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- related-applications must be provided when has-related-applications is true
- decision-date is optional and only relevant if the related proposal has been decided