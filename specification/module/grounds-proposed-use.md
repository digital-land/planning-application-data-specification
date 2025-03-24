field | description | application-type | required? | notes
-- | -- | -- | -- | --
use | State proposed use class | | MAY | Applicant's view of the relevant Use Class, if applicable. (see [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189))
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`
operation-type | Whether the proposed use is temporary or permanent | | MUST | Uses [operation type enum](https://github.com/digital-land/planning-application-data-specification/discussions/203).
temporary-details | Details of temporary use | | MAY | Required if operation-type is temporary.
reason | Reason why the development is considered lawful | | MUST | Explanation supporting the certificate application.
