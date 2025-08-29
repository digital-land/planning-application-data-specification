# Supporting information

Information to support the application, including details of approved 
drawings being replaced by new drawings


**Supporting information module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| replacement-drawings | Replacement drawings[]{} | List of approved drawings being replaced by new drawings |  | MUST |  |


**Replacement drawing component**

field | name | description | required | notes
-- | -- | -- | -- | --
old-drawing-reference | Old drawing reference | Reference of the old drawing being replaced | MUST | 
new-drawing-reference | New drawing reference | Reference for the new drawing that replaces the old drawing | MUST | 
reason | Reason | A textual reason | MAY | 

**Validation rules**

- old-drawing-reference references must match existing approved drawing identifiers
- new-drawing-reference references must match documents in application.documents
- Each old-drawing-reference reference must be unique within replacement-drawings array