# Advertisement types

Module for capturing information about different types of advertisements 
proposed, including their counts and descriptions


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| advertisement-proposal-description | Advertisement proposal description | Description of the advertisement proposal |  | MUST |  |
| advertisement-proposal-type | Advertisement proposal type[]{} | Expected to provide counts for each advertisement type |  | MUST |  |


**Advertisement proposal type model**

field | name | description | required | notes
-- | -- | -- | -- | --
advertisement-type | Advertisement type | One of the advertisement-types or other | MUST | Select from the **advertisement-type** enum
advertisement-count | Advertisement count | Number of this type of advertisement | MUST | 
advertisement-other-description | Advertisement other description | Details required if other advertisement type is selected | MAY | Rule: is a MUST if `advertisement-type` is `other`

**Validation rules**

- At least one advertisement-proposal-type entry must be provided
- advertisement-other-description is required when advertisement-type is 'other'
- advertisement-count must be a positive integer