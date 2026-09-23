# Description of the proposal

What development, works or change of use is proposed

**Description of the proposal module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| description | Proposal description | A description of the development, works, change of use or reserved matters for which approval is sought | advertising, demolition-con-area, full, hh, lbc, outline, reserved-matters, technical-details-consent | MUST |  |
| reserved-matters | Reserved matters[] | Identifies which reserved matters are being submitted for approval as part of this application | outline, reserved-matters | MUST | Select from the **reserved-matter-type** enum |
| related-application | Related application{} | Details about the approved development, as shown in the decision letter | reserved-matters | MUST |  |
| proposal-started | Proposal started | Has any work on the proposal already been started | advertising, demolition-con-area, full, hh, lbc, outline, reserved-matters, technical-details-consent | MUST |  |
| proposal-started-date | Proposal start date | The date when work on the proposal started, in YYYY-MM-DD format | advertising, demolition-con-area, full, hh, lbc, outline, reserved-matters, technical-details-consent | MAY | Rule: is a MUST if `proposal-started` is `True` |
| proposal-completed | Proposal completed | Has any work on the proposal already been completed | advertising, demolition-con-area, full, hh, lbc, outline, reserved-matters, technical-details-consent | MUST |  |
| proposal-completed-date | Proposal completion date | The date when work on the proposal was completed, in YYYY-MM-DD format | advertising, demolition-con-area, full, hh, lbc, outline, reserved-matters, technical-details-consent | MAY | Rule: is a MUST if `proposal-completed` is `True` |
| pip-reference | PIP reference | Reference number for the Planning in Principle (PIP) application this relates to | technical-details-consent | MAY |  |
| is-psi | Is public service infrastructure | For applications made on or after 1 August 2021, is the proposal for public service infrastructure development | full, technical-details-consent | MUST |  |


**Related application details component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | The reference for the related application | MUST |  | 
description | Description | A description of the related application | MUST |  | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY |  | 
eia-application | EIA application | Whether the related application was an Environmental Impact Assessment application | MUST |  | reserved-matters
environmental-statement-submitted | Environmental statement submitted | Whether an Environmental Statement was submitted with the related application | MAY | Rule: is a MUST if `eia-application` is `True` | reserved-matters

**Validation rules**

- description must be clear and concise
- proposal-started-date must not be in the future
- proposal-completed-date must be after proposal-started-date if both provided
- reserved-matters must be valid types from the codelist
- related-application reference must exist in authority records
- pip-reference must match an existing Planning in Principle application
- PSI projects must be checked against infrastructure improvement plans