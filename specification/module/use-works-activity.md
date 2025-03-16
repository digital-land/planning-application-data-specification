Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
ldc-need[] | Is the application for an existing use? (True/False) |   | MUST | At least one of [lawful development need enum](https://github.com/digital-land/planning-application-data-specification/discussions/205).
use-class | If existing-use or use-breach-of-condition is True, state the relevant Use Class |   | MAY | If `existing-use` or `breach-con-existing-use ` in `ldc-need` then applicant needs to provide `use-class` of the use. See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
