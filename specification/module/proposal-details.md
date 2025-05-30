| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters[] | Identifies which reserved matters are being submitted for approval as part of this application. | outline;reserved-matters | MUST | See [reserved matter type enum](https://github.com/digital-land/planning-application-data-specification/discussions/209)  |
| related-application | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | A description of what is being proposed, including the development, works, or change of use. | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | Has any work on the proposal has already started. (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | The date when work on the proposal started. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | Has the development or works have already been completed (`true`/`false`) | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | The date when the development or works were completed. In `YYYY-MM-DD` format. | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | For applications made on or after 1 August 2021, is the proposal for public service infrastructure development (`true`/`false`)| full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-date | date of the decision | If decided | |
