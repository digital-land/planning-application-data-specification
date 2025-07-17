Field | Description | Data Type | Application Type | Required? | Notes
-- | -- | -- | -- | -- | --
related-application{} | Details of the related planning permission | Object | s73, approval-condition, non-material-amendment | MUST | See Related Proposal Structure below.
condition-numbers[] | List of condition numbers related to this application | Array (String) | s73, approval-condition | MAY | The paper forms limit this to 10 conditions but a digital offering does not need to set a limit
original-application-type | Type of original planning application | Enum | non-material-amendment | MAY | Example: 'Full', 'Householder and Listed Building'.
is-householder-development | Is the development to an existing dwelling-house or development within its curtilage (`true`/`false`) | Boolean | non-material-amendment | MAY | Use to calculate the fee
has-development-started | Whether the development has already started | Boolean | s73, approval-condition | MUST | True/False
development-start-date | Date when development started | Date | s73, approval-condition | MAY | Required if development-started is True.
has-development-completed | Whether the development has been completed | Boolean | s73, approval-condition | MUST | True/False
development-completed-date | Date when development was completed | Date | s73, approval-condition | MAY | Required if development-completed is True.

**Related proposal structure**

Field | Description | Required? | Notes
-- | --  | -- | --
description | Detailed description of the approved development | MUST | As shown in the decision letter.
reference | Reference for the original application for the approved development | MUST | Must match the decision letter.
decision-date | Date of the planning decision | MUST | Must be before the application submission date.

