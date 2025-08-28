# Grounds for application (information about the existing use(s))

Information about the existing or last use of the site to support 
a lawful development certificate application, including lawful justification,
use classification, and supporting documentary evidence


| use-lawful-reason | Use lawful reason | Explanation of why the existing or last use is considered lawful, 
providing justification for a lawful development certificate application
 |  | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details |  | MAY |  |
| use | Use | A use class or type of use |  | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available |  | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other` |


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | A name of a person | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**File model**

field | name | description | required | notes
-- | -- | -- | -- | --
url | URL | A URL pointing to the stored file | MAY | 
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded | MUST | 
mime-type | MIME type | The file's MIME type such as application/pdf or image/jpeg | MAY | 
checksum | Checksum | Hash of the file contents used for file validation and checking files have not been tampered with | MAY | 
file-size | File size | Size of the file in bytes that can be used to enforce limits | MAY | 

**Validation rules**

- use-lawful-reason.length > 0
- use IN ['sui', 'other'] REQUIRES specified-use.length > 0
- documents[].reference.length > 0 AND documents[].name.length > 0
- documents[].reference should be unique across application.documents[]