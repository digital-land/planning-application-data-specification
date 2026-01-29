# Foul sewage disposal

How waste water will leave the property as part of the proposed development

**Foul sewage disposal module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| has-new-disposal-arrangements | Has new disposal arrangements | Does the proposal include any new foul sewage disposal arrangments |  | MUST |  |
| foul-sewage-disposal-types | Foul sewage disposal types[] | List of ways foul sewage will be disposed of |  | MAY | Select from the **foul-sewage-disposal-type** enum. Rule: is a MUST if `has-new-disposal-arrangements` is `True` |
| produce-foul-sewage | Produce foul sewage | Whether the proposed development will produce any foul sewage | extraction-oil-gas | MUST |  |
| connect-to-drainage-system | Connect to drainage system | Whether the proposal needs to connect to the existing drainage system | full, outline-some, technical-details-consent | MUST |  |
| connect-to-drainage-system-oil-gas | Connect to drainage system (oil and gas) | Whether the proposal needs to connect to the existing drainage system (oil and gas applications) | extraction-oil-gas | MUST | Select from the **yes-no-unknown** enum |
| supporting-documents | Supporting documents[]{} | References to plans or drawings showing details of the existing drainage system |  | MAY |  |


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- if connect-to-drainage-system == true then supporting-documents is required
- if application-type includes 'extraction-oil-gas' then supporting-documents is required
- if connect-to-drainage-system-oil-gas == 'yes' then supporting-documents is required
- each document in supporting-documents must have a `reference` that matches a document in application.documents