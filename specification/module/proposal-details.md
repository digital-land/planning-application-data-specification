| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| reserved-matters-for-approval | Select one or more from reserved-matters ENUM | outline;reserved-matters | MUST | for outline (all) would expect all to be expected |
| related-proposal | Details about the approved development, as shown in the decision letter | reserved-matters | MUST | See related proposal structure below
| proposal-description | | advertising;demolition-con-area;full;hh;lbc;outline | MUST | can be about development or change of use |
| proposal-started | True or False | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-started-date | | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work started, date must be pre-application submission, blank means not started |
| proposal-completed | True or False | advertising;demolition-con-area;full;hh;lbc;outline | MUST | |
| proposal-completed-date | | advertising;demolition-con-area;full;hh;lbc;outline | MAY | Rules: only required if work completed, date must be pre-application submission, blank means not completed |
| is-psi | True or False | full;outline | MUST | |
| pip-reference | Reference for related permission in principle application | full | MUST | |

**Related proposal**

| field | description | notes |
| --- | --- | --- |
| reference | reference for the related proposal | |
| description | description of the related proposal | |
| decision-data | date of the decision | If decided |
