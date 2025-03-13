Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
applicant-land-interest | Does the applicant have an interest in the land? (True/False) |   | MUST | If False, application cannot proceed.
ownership-notification | If not the sole owner, has notification been given under Article 10? (Enum) |   | MAY | One of Yes, No, Not Applicable. Required if applicant is not sole owner.
notified-persons[]{} | List of persons notified, including address and date |   | CONDITIONAL | Rule: Required if `ownership-notification` is Yes.

**Notified person**

Field | Description | Data Type | Required | Notes
-- | -- | -- | -- | --
person-notified | Name of the person notified | String | MUST | Full name.
address | Address of the person notified | String | MUST | Full postal address.
date-of-notification | Date notification was sent | Date | MUST | Format: YYYY-MM-DD.
