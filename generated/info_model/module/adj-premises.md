# Adjacent premises

Details of properties next to the development site

**Adjacent premises module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for the adjoining properties |  | MUST |  |


**Address component**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 
uprn | UPRN | Unique Property Reference Number | MAY | 

**Validation rules**

- At least one address must be provided
- Each address must have address-text as minimum requirement
- UPRN should be provided where known for accurate property identification