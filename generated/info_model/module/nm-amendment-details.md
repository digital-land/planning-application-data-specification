# Non-material amendment details

Details of non-material amendments to planning applications including
description of changes, document substitutions, and reasons for amendments


| description | Description | Description of the non-material amendments the applicant seeks to make |  | MUST |  |
| is-substituting-document | Substituting document | True or False indicating whether the amendment involves substituting documents |  | MUST |  |
| replacement-documents | Replacement documents[]{} | List of documents being replaced in the amendment with old and new document references |  | MAY | Rule: is a MUST if `is-substituting-document` is `True` |
| reason | Reason | Reason why applicant wants to make the amendment |  | MUST |  |


**Replacement document model**

field | name | description | required | notes
-- | -- | -- | -- | --
old-document | Old document | Reference of the old document being replaced in the amendment | MUST | 
new-document | New document | Reference for the new document replacing the old document in the amendment | MUST | 

**Validation rules**

- is-substituting-document == true REQUIRES replacement-documents.length >= 1
- replacement-documents[].old-document.length > 0 AND replacement-documents[].new-document.length > 0
- replacement-documents[].old-document != replacement-documents[].new-document
- description.length > 10
- reason.length > 5