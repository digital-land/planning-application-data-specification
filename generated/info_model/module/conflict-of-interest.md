# Conflict of interest

Information about any conflicts of interest between the applicant/agent and the planning authority,
including relationships with staff or elected members


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| conflict-to-declare | Conflict to declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared | hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MUST |  |
| conflict-person-name | Conflict person name | Name of the individual with the conflict of interest that matches one of the names provided in applicants/agent section | hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |
| conflict-details | Conflict details | Details of the conflict of interest including name, role and how the individual is related to the planning authority | hh, full, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |

**Validation rules**

- conflict-person-name must match a name provided in applicants or agent sections