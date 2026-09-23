# Supporting information

Drawings approved as part of the original decision and drawings submitted with the reserved matters application

**Supporting information module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| approved-drawings | Approved drawings[]{} | Drawings approved as part of the original planning decision |  | MAY |  |
| submitted-drawing-references | Submitted drawing references[] | Reference numbers of drawings submitted with the application for approval |  | MAY |  |
| approved-drawings-document | Approved drawings schedule{} | Reference to an uploaded decision notice or drawing schedule that identifies drawings approved as part of the original planning decision |  | MAY |  |
| submitted-drawings-document | Submitted drawings schedule{} | Reference to an uploaded schedule that identifies drawings submitted with the application for approval |  | MAY |  |
| reason | Reason | Reasons for any changes to the original drawings |  | MAY |  |


**Approved drawing component**

field | name | description | required | notes
-- | -- | -- | -- | --
name | Name | Name or title of the approved drawing | MUST | 
reference | Reference | Reference number of the approved drawing | MUST | 


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- Provide approved-drawings and submitted-drawing-references, or approved-drawings-document and submitted-drawings-document, but do not mix the two routes
- References must be unique within approved-drawings and submitted-drawing-references
- approved-drawings-document and submitted-drawings-document references must match documents in submission-details.documents