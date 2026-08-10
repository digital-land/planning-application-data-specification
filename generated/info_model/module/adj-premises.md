# Adjacent premises

Addresses of premises next to the development site, used to notify their owners or occupiers.

**Adjacent premises module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for adjacent premises, used to notify their owners or occupiers. |  | MUST |  |


**Contact address component**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Text representation of an address or site | MUST | 
postcode | Postcode | Postcode for a contact address or site | MAY | 
uprn | UPRN | Unique Property Reference Number for a property | MAY | 

**Validation rules**

- At least one contact address must be provided
- Each contact address must have address-text as minimum requirement
- UPRN should be provided where known for accurate premises identification