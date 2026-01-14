# Plans, drawings and supporting materials

Additional materials and specifications that form part of the planning application

**Plans, drawings and supporting materials module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| supporting-documents | Supporting documents[]{} | References to supporting documents that have been uploaded with the application |  | MUST |  |
| inspection-address | Inspection address | Full postal address where supporting material can be inspected |  | MUST | Should this be the address-text field |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- supporting-documents.length >= 1
- inspection-address must include street, town/city, and postcode
- each document in supporting-documents must have a `reference` that matches a document in application.documents