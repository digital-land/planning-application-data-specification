# Access and rights of way

Details of any changes the proposed development would make to existing access arrangements or public rights of way

**Access and rights of way module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| new-altered-vehicle | New or altered vehicle access | Is a new or altered vehicle access proposed to/from the public highway |  | MUST | Select from the **rights-of-way-answer** enum |
| new-altered-pedestrian | New or altered pedestrian access | Is a new or altered pedestrian access proposed to/from the public highway |  | MUST | Select from the **rights-of-way-answer** enum |
| change-right-of-way | Change to right of way | Will the proposal change public rights of way (diversion/extinguishment/creation) | full, hh, outline | MUST | Select from the **rights-of-way-answer** enum |
| new-right-of-way | New right of way | Will new public rights of way be provided within or adjacent to the site | full, extraction-oil-gas, outline | MUST | Select from the **rights-of-way-answer** enum |
| new-public-road | New public road | Will new public roads be provided within the site | full, extraction-oil-gas, outline | MUST | Select from the **rights-of-way-answer** enum |
| temp-right-of-way | Temporary right of way changes | Are temporary changes to rights of way needed while the site is worked | extraction-oil-gas | MUST | Select from the **rights-of-way-answer** enum |
| future-new-right-of-way | Future new right of way | Will new public rights of way be provided after extraction? | extraction-oil-gas | MUST | Select from the **rights-of-way-answer** enum |
| supporting-documents | Supporting documents[]{} | Supporting documents that provide additional information about the materials to be used |  | MAY |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name for the document. For example, The Site Plan | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- All fields must use values from rights-of-way-answers codelist
- If new-altered-vehicle is yes, details must be provided in highways module
- If change-right-of-way is yes, separate rights of way order may be needed
- If temp-right-of-way is yes, details of temporary diversions must be provided
- each document in supporting-documents must have a `reference` that matches a document in application.documents