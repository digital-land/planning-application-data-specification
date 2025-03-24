field | description | application-types | required | notes
-- | -- | -- | -- | --
ldc-need[] | What is the lawful development certificate needed for? |   | MUST | At least one of [lawful development need enum](https://github.com/digital-land/planning-application-data-specification/discussions/205).
use | If existing-use or use-breach-of-condition is True, state the relevant Use Class |   | MAY | If `existing-use` or `breach-con-existing-use ` in `ldc-need` then applicant needs to provide `use`. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189). One of enum or `other`
specified-use | The specific use if no use class suitable | | MAY | Rule: must be provided if `use` is `sui` or `other`
