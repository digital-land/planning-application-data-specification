Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
has-new-disposal-arrangements | Does the proposal include any new foul sewage disposal arrangments? | full;extraction-oil-gas;outline | MUST | Allows applicant to state no new disposal arrangements included
foul-sewage-disposal-types[] | List of ways foul sewage will be disposed of | full;extraction-oil-gas;outline | MAY | See [foul-sewage-disposal-type ENUM](https://github.com/digital-land/planning-application-data-specification/discussions/165). Rule: MUST if has-new-disposal-arrangements is true
produce-foul-sewage | Proposed development produce any foul sewage (True/False) | extraction-oil-gas | MUST | 
connect-to-drainage-system | Does the proposal need to connect to the existing drainage system (True/False) | full;extraction-oil-gas;outline | MUST | 
drainage-system-details | Details of the drawings/plans that show the existing system | full;extraction-oil-gas;outline | MAY | Rule, is a MUST if `connect-to-drainage-system` is TRUE or `extraction-oil-gas` application 
