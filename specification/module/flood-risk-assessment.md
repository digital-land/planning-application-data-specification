Field | Description | Application-Types | Required | Notes
-- | -- | -- | -- | --
flood-risk-area | Is the site within an area at risk of flooding? |   | MUST | Boolean True or False
data-provided-by | Who provided the data: Applicant or System/Service? |   | MAY | Enum (Applicant / System/Service).
flood-risk-assessment | Reference of the flood risk assessment document |   | MAY | Required if flood-risk-area is True.
within-20m-watercourse | Is the proposal within 20 metres of a watercourse? |   | MUST | Boolean True or False.
increases-flood-risk | Will the proposal increase the flood risk elsewhere? |   | MUST | Boolean True or False.
surface-water-disposal[] | How will surface water be disposed of? |   | MUST | Multiple options allowed (see [surface water disposal type enum](https://github.com/digital-land/planning-application-data-specification/discussions/195)).

