# Grounds for application (information about the existing use(s))

Supporting inforation for a Lawful Development Certificate application relating to how the site has most recently been used.

**Grounds for application (information about the existing use(s)) module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| use-lawful-reason | Use lawful reason | Explanation of why the existing or last use is considered lawful, 
providing justification for a lawful development certificate application
 |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to supporting documents that have been uploaded with the application |  | MAY |  |
| use | Use | A use class or type of use |  | MAY | Select from the **use-class** enum. an option needs to be "other" |
| specified-use | Specified use | A specified use if no applicable use class is available |  | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other` |


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- use-lawful-reason.length > 0
- use IN ['sui', 'other'] REQUIRES specified-use.length > 0
- each document in supporting-documents must have a `reference` that matches a document in application.documents