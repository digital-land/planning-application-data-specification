# LDC Proposed Use

Prospective use of the site

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Proposal details LDC](#proposal-details-ldc)
* [Grounds for application (information about the existing use(s))](#grounds-for-application-(information-about-the-existing-use(s)))
* [Grounds for proposed use](#grounds-for-proposed-use)

# Application fields

Core planning application structure containing reference information,
application types, submission details, modules, documents, and fees


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| reference | Reference | A unique reference for the data item | MUST |  |
| application-types | Application types[] | A list of planning application types that define the nature of the planning application | MUST | Select from the **application-type** enum |
| application-sub-type | Application sub type | Further classification of the application type for specific variations within the main application type | MAY | Select from the **application-sub-type** enum |
| planning-authority | Planning authority | The reference of the planning authority the application has been submitted to, e.g. local-authority:CMD | MUST |  |
| submission-date | Submission date | Date the application is submitted in YYYY-MM-DD format | MUST |  |
| modules | Modules[] | List of required modules for this application that can be used to validate the application | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MUST |  |
| fee | Fee{} | The fee payable for the application including amounts and transaction details | MAY |  |


**Document model**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST | 
name | Name | A name of a person | MUST | 
description | Description | A text description providing details about the subject. For parking changes, this describes how the proposed works affect existing car parking arrangements. | MAY | 
document-types | Document types[] | List of codelist references that the document covers | MUST | Select from the **planning-requirement** enum
file | File{} | The digital file or a reference to where the file is stored | MUST | 


**Fee model**

field | name | description | required | notes
-- | -- | -- | -- | --
amount | Amount | The total amount due for the application fee | MUST | 
amount-paid | Amount paid | The amount paid towards the application fee | MUST | 
transactions | Transactions[] | References to payments or financial transactions related to this application | MAY | 


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

- reference must be a valid UUID format
- application-types must reference valid application type codelist values
- application-sub-type must reference valid application sub-type codelist values
- planning-authority must be a valid organisation reference
- modules must reference existing module definitions
- document references must be unique within the application
- file must contain either url or base64, but not both
- document-types must reference valid planning requirement codelist values

## Proposal details LDC

Details of the proposal for lawful development certificate applications

| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposal-incl-building-operations | Proposal incl building operations | Does the proposal include building operations? | MUST | For lawful development certificate for proposed work |
| proposal-building-operations-description | Proposal building operations description | Description of the building operations included in the proposal | MAY | Rule: is a MUST if `proposal-incl-building-operations` is `True` |
| proposal-incl-change-of-use | Proposal incl change of use | Does the proposal include a change of use? | MUST |  |
| proposal-change-of-use-description | Proposal change of use description | Description of the change of use included in the proposal | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True`. Required if proposal-incl-change-of-use is true |
| proposal-existing-use-description | Proposal existing use description | Description of the existing use before the proposed change of use | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-existing-use-stop-date | Proposal existing use stop date | Date when the existing use stopped or will stop | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-started | Proposal started | Has any work on the proposal already been started | MUST |  |

**Validation rules**

- proposal-building-operations-description is required when proposal-incl-building-operations is true
- proposal-change-of-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date must be in YYYY-MM-DD format

## Grounds for application (information about the existing use(s))

Information about the existing or last use of the site to support 
a lawful development certificate application, including lawful justification,
use classification, and supporting documentary evidence


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| use-lawful-reason | Use lawful reason | Explanation of why the existing or last use is considered lawful, 
providing justification for a lawful development certificate application
 | MUST |  |
| documents | Documents[]{} | List of submitted documents with references and details | MAY |  |
| use | Use | A use class or type of use | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other` |


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

- use-lawful-reason.length > 0
- use IN ['sui', 'other'] REQUIRES specified-use.length > 0
- documents[].reference.length > 0 AND documents[].name.length > 0
- documents[].reference should be unique across application.documents[]

## Grounds for proposed use

Information about the proposed use class, operation type, and supporting reasoning for lawful development certificate applications


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| use | Use | State proposed use class | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available | MAY |  |
| operation-type | Operation type | Whether the proposed use is temporary or permanent | MUST | Select from the **operation-type** enum |
| temporary-details | Temporary details | Details of temporary use including duration and specific arrangements | MAY |  |
| reason | Reason | A textual reason | MUST |  |

**Validation rules**

- specified-use is required if use is 'sui' or 'other'
- temporary-details is required if operation-type is 'temporary'

## Required codelists

This are the codelist required to support this specification:

- planning-requirement