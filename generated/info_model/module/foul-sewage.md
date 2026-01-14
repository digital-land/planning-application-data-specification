# Foul sewage disposal

How waste water will leave the property as part of the proposed development

**Foul sewage disposal module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| has-new-disposal-arrangements | Has new disposal arrangements | Does the proposal include any new foul sewage disposal arrangments |  | MUST |  |
| foul-sewage-disposal-types | Foul sewage disposal types[] | List of ways foul sewage will be disposed of |  | MAY | Select from the **foul-sewage-disposal-type** enum |
| produce-foul-sewage | Produce foul sewage | Whether the proposed development will produce any foul sewage |  | MUST |  |
| connect-to-drainage-system | Connect to drainage system | Whether the proposal needs to connect to the existing drainage system |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to plans or drawings showing details of the existing drainage system |  | MAY |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- if connect-to-drainage-system == true then supporting-documents is required
- if application-type includes 'extraction-oil-gas' then supporting-documents is required
- each document in supporting-documents must have a `reference` that matches a document in application.documents