Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
existing-use-details[]{} | List of existing site uses and related land areas |   | MUST | At least one use must be provided.

existing use structure

Field | Description | Required | Notes
-- | -- | -- | --
use-class | The Use class for the use | MUST | See [use class enum](https://github.com/digital-land/planning-application-data-specification/discussions/189)
use-details | Further detail of the use | MAY | Rule: required if Sui generis or other given
