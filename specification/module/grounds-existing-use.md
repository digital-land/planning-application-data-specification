field | description | application-types | required | notes
-- | -- | -- | -- | --
use-lawful-reason | Explanation of why the existing or last use is lawful |   | MUST | 
documents[]{} | List of supporting documentary evidence |   | MAY | Optional unless evidence is needed to support the justification.
use | Stated use class of the existing or last use (if applicable) |   | MAY | Use [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189) (e.g., C3, B1, E).
specified-use | Specify the use if no applicable use class | | MAY | Rule: must if `use` is `sui` or `other`
