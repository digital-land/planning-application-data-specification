# Description of your proposal

Written description of the proposed development including any additional relevant details.

**Description of your proposal module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| related-application | Related application{} | Details of the related planning permission | s73, approval-condition, non-material-amendment | MUST |  |
| condition-numbers | Condition numbers[] | List of condition numbers related to this application | s73, approval-condition | MAY |  |
| original-application-type | Original application type | Type of original planning application | non-material-amendment | MAY |  |
| is-householder-development | Is householder development | Is the development to an existing dwelling-house or development within its curtilage (true/false) | non-material-amendment | MAY |  |
| has-development-started | Has development started | Whether the development has already started | s73, approval-condition | MUST |  |
| development-start-date | Development start date | Date when development started | s73, approval-condition | MAY | Rule: is a MUST if `has-development-started` is `True` |
| has-development-completed | Has development completed | Whether the development has been completed | s73, approval-condition | MUST |  |
| development-completed-date | Development completed date | Date when development was completed | s73, approval-condition | MAY | Rule: is a MUST if `has-development-completed` is `True` |


**Related application details component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST | 
description | Description | A description of the related application | MUST | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- start-date is required when development-started is true
- completion-date is required when development-completed is true
- decision-date must be before the application submission date
- reference-number must match the decision letter
- proposal-description must match the decision letter
- Module applies to s73, approval-condition, and non-material-amendment application types