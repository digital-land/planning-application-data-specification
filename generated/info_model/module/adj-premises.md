# Adjacent premises

Information about addresses of properties adjacent to the development site


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for the adjoining properties |  | MUST |  |


**Address model**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 
uprn | UPRN | Unique Property Reference Number | MAY | 

**Validation rules**

- At least one address must be provided
- Each address must have address-text as minimum requirement
- UPRN should be provided where known for accurate property identification