# Grounds for application

Why a Certificate of Lawfulness of Propose Works is being requested.

**Grounds for application module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| grounds-for-application | Grounds for application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted,
including explanation of why listed building consent is not required
 |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to supporting documents that have been uploaded with the application |  | MUST |  |


**Supporting document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
details | Details | Additional details or information about an item | MAY | 

**Validation rules**

- grounds-for-application.length > 0
- supporting-documents.length >= 1
- each document in supporting-documents must have a `reference` that matches a document in application.documents