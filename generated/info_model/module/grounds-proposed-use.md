# Grounds for proposed use

What the new site will be used for

**Grounds for proposed use module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| use | Use | State proposed use class |  | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available |  | MAY |  |
| operation-type | Operation type | Whether the proposed use is temporary or permanent |  | MUST | Select from the **operation-type** enum |
| temporary-details | Temporary details | Details of temporary use including duration and specific arrangements |  | MAY |  |
| reason | Reason | A textual reason |  | MUST |  |

**Validation rules**

- specified-use is required if use is 'sui' or 'other'
- temporary-details is required if operation-type is 'temporary'