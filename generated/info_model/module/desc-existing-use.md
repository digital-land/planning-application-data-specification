# Description of existing use

Information about the existing uses of the development site, including 
use classes and which parts of the land they relate to


**Description of existing use module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| existing-use-details | Existing use details[]{} | List of existing site uses and related land areas |  | MUST |  |


**Existing use detail component**

field | name | description | required | notes
-- | -- | -- | -- | --
use | Use | A use class or type of use | MUST | Select from the **use-class** enum. an option needs to be "other"
use-details | Use details | Further detail of the use | MAY | Rule: is a MUST if `use` is `sui`. Rule: is a MUST if `use` is `other`
land-part | Land part | Which part of the land the use relates to | MUST | 

**Validation rules**

- existing-use-details must contain at least one item
- if use == 'sui' OR use == 'other' then use-details is required