Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
is-single-storey-extension | Will the extension be a single storey? (True/False) |   | MUST | If False, the application cannot proceed.
is-extension-height-over-4m | Will the extension exceed 4 metres in height? (True/False) |   | MUST | If True, the application cannot proceed.
is-dwelling-detached | Is the the dwelling detached? (True/False) | | MUST | 
is-extension-beyond-rear-wall | Will the extension extend beyond the rear wall of the original dwelling? |   | MUST | See conditional logic for limits based on attachment type.
extension-length | Length of rear extension (in metres) |   | MUST | 
is-within-site-constraints | Is the dwellinghouse within any restricted area? (True/False) |   | MUST | If True, the application cannot proceed.
site-constraints[] | List of specific site constraints |   | MAY | Rule: Required if within-site-restrictions is True. See [designation enum](https://github.com/digital-land/planning-application-data-specification/discussions/191) where `application-types` includes `prior-approval:pa-extension`
