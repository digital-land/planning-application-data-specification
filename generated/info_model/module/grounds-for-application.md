# Grounds for application

Why a Certificate of Lawfulness of Propose Works is being requested.

**Grounds for application module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| grounds-for-application | Grounds for application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted,
including explanation of why listed building consent is not required
 |  | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details |  | MUST |  |


**Document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | The name or title of the document | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**File component**

field | name | description | required | notes
-- | -- | -- | -- | --
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded | MUST | 
mime-type | MIME type | The file's MIME type such as application/pdf or image/jpeg | MAY | 
file-size | File size | Size of the file in bytes that can be used to enforce limits | MAY | 

**Validation rules**

- grounds-for-application.length > 0
- documents.length >= 1
- documents[].reference.length > 0 AND documents[].name.length > 0
- documents[].reference should be unique across application.documents[]