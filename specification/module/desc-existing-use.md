field | description | application-types | required | notes
-- | -- | -- | -- | --
existing-use-details[]{} | List of existing site uses and related land areas |   | MUST | Rule: At least one use must be provided.

**existing use structure**

field | description | required | notes
-- | -- | -- | --
use | The Use class of the use | MUST | See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or other
use-details | Further detail of the use | MAY | Rule: required if `use` is `sui` or `other`
land-part | State which part of the land the `use` relates to | MUST | 
