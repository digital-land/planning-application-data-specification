# Use works activity

Information about what the lawful development certificate is needed for and related use details

**Use works activity module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| ldc-need | LDC need[] | What is the lawful development certificate needed for? |  | MUST | Select from the **lawful-dev-cert-need** enum. At least one value must be provided |
| use | Use | A use class or type of use |  | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available |  | MAY |  |

**Validation rules**

- At least one ldc-need value must be provided
- use is required when ldc-need contains existing-use or breach-con-existing-use
- specified-use is required when use is sui or other