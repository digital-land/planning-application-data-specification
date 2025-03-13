Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
single-storey-extension | Will the extension be a single storey? (True/False) |   | MUST | If False, the application cannot proceed.
extension-height-over-4m | Will the extension exceed 4 metres in height? (True/False) |   | MUST | If True, the application cannot proceed.
dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
rear-extension-length | Will the extension extend beyond the rear wall of the original dwelling? |   | MUST | See conditional logic for limits based on attachment type.
extension-length | Length of rear extension (in metres) |   | MUST | 
within-site-constraints | Is the dwellinghouse within any restricted area? (True/False) |   | MUST | If True, the application cannot proceed.
site-constraints[] | List of specific site constraints |   | MAY | Rule: Required if within-site-restrictions is True. See [site constraints enum](https://github.com/digital-land/planning-application-data-specification/discussions/191)
