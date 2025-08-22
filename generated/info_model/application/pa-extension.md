# Larger Home Extension

Planning application for extension

## Contents

* [Application data specification](#application-data-specification)

### Modules

* [Adjacent premises](#adjacent-premises)
* [Description of proposed works](#description-of-proposed-works)
* [Eligibility extension](#eligibility-extension)

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

## Adjacent premises

Information about addresses of properties adjacent to the development site


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| addresses | Addresses[]{} | A list of addresses for the adjoining properties | MUST |  |


**Address model**

field | name | description | required | notes
-- | -- | -- | -- | --
address-text | Address Text | Flexible field for capturing addresses | MUST | 
postcode | Postcode | The postal code | MAY | 
uprn | UPRN | Unique Property Reference Number | MAY | 

**Validation rules**

- At least one address must be provided
- Each address must have address-text as minimum requirement
- UPRN should be provided where known for accurate property identification

## Description of proposed works

Description of proposed development works including extension measurements
and detailed work specifications for planning applications


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| proposed-works-details | Proposed works details | Description of the proposed works including detailed explanation of the work | MUST |  |
| extension-depth | Extension depth | How far the extension extends beyond the rear wall, measured externally in metres | MUST |  |
| max-extension-height | Maximum extension height | Maximum height of the extension, measured externally from natural ground level in metres | MUST |  |
| eaves-height | Eaves height | Height at the eaves of the extension, measured externally from natural ground level in metres | MUST |  |

**Validation rules**

- extension-depth > 0 AND max-extension-height > 0 AND eaves-height > 0
- eaves-height <= max-extension-height
- extension-depth measurement taken from external face of existing rear wall
- max-extension-height and eaves-height measured from natural ground level
- proposed-works-details.length > 10

## Eligibility extension

Eligibility criteria for extension applications to determine if the proposal
meets the requirements for the application type


| reference | name | description | requirement | notes |
| --- | --- | --- | --- | --- |
| is-single-storey-extension | Single storey extension | Will the extension be a single storey | MUST |  |
| is-extension-height-over-4m | Extension height over 4m | Will the extension exceed 4 metres in height | MUST |  |
| is-dwelling-detached | Dwelling detached | Is the dwelling detached | MUST |  |
| is-extension-beyond-rear-wall | Extension beyond rear wall | Will the extension extend beyond the rear wall of the original dwelling | MUST |  |
| extension-length | Extension length | Length of rear extension in metres | MUST |  |
| is-within-site-constraints | Within site constraints | Is the dwellinghouse within any restricted area | MUST |  |
| site-constraints | Site constraints[] | List of specific site constraints that restrict development | MAY | Select from the **designation** enum |

**Validation rules**

- if is-single-storey-extension == false then application is ineligible
- if is-extension-height-over-4m == true then application is ineligible
- if is-within-site-constraints == true then application is ineligible
- if is-within-site-constraints == true then site-constraints is required
- extension-length must comply with permitted development limits based on is-dwelling-detached value
