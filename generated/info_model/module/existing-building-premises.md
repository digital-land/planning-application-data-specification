# Existing building premises

Addresses of flats and other premises within the existing building, supplied as a structured list or in supporting documents.

**Existing building premises module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | Addresses of all flats and other premises within the existing building. |  | MAY |  |
| supporting-documents | Supporting documents[]{} | References to documents supplied with the application containing the complete list of addresses of flats and other premises within the existing building. |  | MAY |  |


**Contact address component**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Text representation of an address or site | MUST | 
postcode | Postcode | Postcode for a contact address or site | MAY | 
uprn | UPRN | Unique Property Reference Number for a property | MAY | 


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- At least one of addresses or supporting-documents must contain one or more items.
- The complete list of addresses must be provided through at least one of these routes.