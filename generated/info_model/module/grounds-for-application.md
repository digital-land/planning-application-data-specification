# Grounds for application

Grounds for a Certificate of Lawfulness of Proposed Works application,
explaining why the certificate should be granted and why listed building
consent is not required, with supporting documentary evidence


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| grounds-for-application | Grounds for application | Reason(s) why Certificate of Lawfulness of Proposed Works should be granted,
including explanation of why listed building consent is not required
 |  | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details |  | MUST |  |


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**File model**

field | name | description | required | notes
-- | -- | -- | -- | --
url | URL | A URL pointing to the stored file for previously uploaded or hosted files | MAY | 
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded useful for identifying and preserving the file | MUST | 
mime-type | MIME type | The file's MIME type such as application/pdf or image/jpeg | MAY | 
checksum | Checksum | Hash of the file contents used for file validation and checking files have not been tampered with | MAY | 
file-size | File size | Size of the file in bytes that can be used to enforce limits | MAY | 

**Validation rules**

- grounds-for-application.length > 0
- documents.length >= 1
- documents[].reference.length > 0 AND documents[].name.length > 0
- documents[].reference should be unique across application.documents[]