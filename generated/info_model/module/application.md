# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


**Application fields module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item |  | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application |  | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type |  | MAY | Select from the **application-subtype** enum |
| planning-authority | Planning authority | A reference of the planning authority the application has been submitted to, e.g. local-authority:CMD for London borough of Camden |  | MUST | Select from the **planning-authority** enum. Currently built by combining local-authority, development-corporation and national-park-authority datasets from planning.data.gov.uk |
| submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format |  | MUST |  |
| modules | Modules[] | List of required modules for this application that can be used to validate the application |  | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details |  | MUST |  |
| fee | Fee{} | The fee payable for the application including amounts and transaction details |  | MAY |  |


**Document component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A reference for the document | MUST | 
name | Name | The name or title of the document | MUST | 
description | Description | Brief description of what the document contains | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**Fee component**

field | name | description | required | notes
-- | -- | -- | -- | --
amount | Amount | The total amount due for the application fee | MUST | 
amount-paid | Amount paid | The amount paid towards the application fee | MUST | 
transactions | Transactions[] | References to payments or financial transactions related to this application | MAY | 


**File component**

field | name | description | required | notes
-- | -- | -- | -- | --
url | URL | A URL pointing to the stored file | MAY | 
base64-content | Base64 | Base64-encoded content of the file for inline file uploads | MAY | 
filename | Filename | Name of the file being uploaded | MUST | 
mime-type | MIME type | The file's MIME type such as application/pdf or image/jpeg | MAY | 
checksum | Checksum | Hash of the file contents used for file validation and checking files have not been tampered with | MAY | 
file-size | File size | Size of the file in bytes that can be used to enforce limits | MAY | 

**Validation rules**

- reference must be a valid UUID format
- application-types must reference valid application type codelist values
- application-sub-type must reference valid application sub-type codelist values
- planning-authority must be a valid organisation reference
- modules must reference existing module definitions
- document references must be unique within the application
- file must contain either url or base64, but not both
- document-types must reference valid planning requirement codelist values