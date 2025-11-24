# Site information

Any additional relevant information about the development site.

**Site information module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| site-area | Site area{} | The total area of the site where development is proposed |  | MUST |  |
| existing-use | Existing use[]{} | Structured information on the current use of the site |  | MUST |  |
| known-constraints | Known constraints[] | A list of the known constraints affecting the site |  | MUST | Select from the **site-constraint** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used |  | MAY |  |


**Site area component**

field | name | description | required | notes
-- | -- | -- | -- | --
value | Value | Numeric value representing a measurement or quantity | MUST | 
unit | Unit | Unit of measurement for a value | MUST | 
provided-by | Provided by | Whether the information was provided by the applicant or calculated by the system | MAY | Select from the **provided-by** enum


**Existing use component**

field | name | description | required | notes
-- | -- | -- | -- | --
uses | Uses[]{} | List of applicable uses for a site or development | MUST | 
floorspace | Floorspace | Total floorspace for a use in square metres | MUST | 


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 


**Use component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
specified-use | Specified use | A specified use if no applicable use class is available | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`

**Validation rules**

- supporting-documents is required if known-constraints is not empty
- site-area value should ideally be calculated from site boundary
- site-area unit must be one of: m2, hectares
- provided-by must be one of: Applicant, System/Service
- use must reference valid use class or be 'other' or 'sui'
- specified-use is required if use is 'sui' or 'other'
- floorspace must be numeric value in m2
- each document in supporting-documents must have a `reference` that matches a document in application.documents