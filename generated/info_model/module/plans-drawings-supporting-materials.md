# Plans, drawings and supporting materials

Additional materials and specifications that form part of the planning application

**Plans, drawings and supporting materials module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| plans-documents | Plans documents[]{} | List of plans, drawings, and supporting documents |  | MUST |  |
| inspection-address | Inspection address | Full postal address where supporting material can be inspected |  | MUST | Should this be the address-text field |


**Plans document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference-number | Reference number | Unique identifier for the document | MUST | 
name | Name | Name of the document (descriptive) | MUST | 

**Validation rules**

- plans-documents.length >= 1
- plans-documents[].reference-number must be unique
- plans-documents[].name.length > 0
- inspection-address must include street, town/city, and postcode