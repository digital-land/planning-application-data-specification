Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
foul-sewage-disposal-types[] | List of ways foul sewage will be disposed of | | MUST | See [foul-sewage-disposal-type ENUM](https://github.com/digital-land/planning-application-data-specification/discussions/165)
produce-foul-sewage | Proposed development produce any foul sewage (True/False) | extraction-oil-gas | MUST | 
connect-to-drainage-system | Does the proposal need to connect to the existing drainage system (True/False) | | MUST | 
drainage-system-details | Details of the drawings/plans that show the existing system | | MAY | Rule, is a MUST if `connect-to-drainage-system` is TRUE or `extraction-oil-gas` application 
