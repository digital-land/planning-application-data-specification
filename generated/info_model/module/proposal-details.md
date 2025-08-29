# Description of the proposal

Information about what development, works or change of use is being proposed


**Description of the proposal module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposal-description | Proposal description | A description of what is being proposed, including the development, works, or change of use | advertising, demolition-con-area, full, hh, lbc, outline | MUST |  |
| reserved-matters | Reserved matters[] | Identifies which reserved matters are being submitted for approval as part of this application | outline, reserved-matters | MUST | Select from the **reserved-matter-type** enum |
| related-application | Related application{} | Details about the approved development, as shown in the decision letter | reserved-matters | MUST |  |
| proposal-started | Proposal started | Has any work on the proposal already been started | advertising, demolition-con-area, full, hh, lbc, outline | MUST |  |
| proposal-started-date | Proposal start date | The date when work on the proposal started, in YYYY-MM-DD format | advertising, demolition-con-area, full, hh, lbc, outline | MAY | Rule: is a MUST if `proposal-started` is `True` |
| proposal-completed | Proposal completed | Has any work on the proposal already been completed | advertising, demolition-con-area, full, hh, lbc, outline | MUST |  |
| proposal-completed-date | Proposal completion date | The date when work on the proposal was completed, in YYYY-MM-DD format | advertising, demolition-con-area, full, hh, lbc, outline | MAY | Rule: is a MUST if `proposal-completed` is `True` |
| pip-reference | PIP reference | Reference number for the Planning in Principle (PIP) application this relates to | full | MAY |  |
| is-psi | Is public service infrastructure | For applications made on or after 1 August 2021, is the proposal for public service infrastructure development | full | MUST |  |


**Related application details component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST | 
description | Description | A description of the related application | MUST | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- proposal-description must be clear and concise
- proposal-started-date must not be in the future
- proposal-completed-date must be after proposal-started-date if both provided
- reserved-matters must be valid types from the codelist
- related-application reference must exist in authority records
- pip-reference must match an existing Planning in Principle application
- PSI projects must be checked against infrastructure improvement plans