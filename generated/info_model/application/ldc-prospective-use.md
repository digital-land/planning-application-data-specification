# LDC Proposed Use

Prospective use of the site

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Proposal details LDC](#proposal-details-ldc)
* [Grounds for application (information about the existing use(s))](#grounds-for-application-(information-about-the-existing-use(s)))
* [Grounds for proposed use](#grounds-for-proposed-use)

## Application data specification

| field | description | data-type | required | notes |
| --- | --- | --- | --- | --- |

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