# Conflict of interest

Details of any conflict of interest that may exist between the applicant and planning authority.

**Conflict of interest module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| conflict-to-declare | Conflict to declare | Indicates whether any named applicant or agent has a relationship to the planning authority that must be declared | hh, full, technical-details-consent, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MUST |  |
| person-reference | Person reference | Reference to the applicant or agent with the conflict | hh, full, technical-details-consent, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MAY | Rule: is a MUST if `conflict-to-declare` is `True`. Used to link named individuals from the form to a particular declaration or confirmation statement, for example in the declaration module.
 |
| conflict-details | Conflict details | Details of the conflict of interest including name, role and how the individual is related to the planning authority | hh, full, technical-details-consent, outline, reserved-matters, demolition-con-area, lbc, advertising, ldc, consent-under-tpo, non-material-amendment, pip, extraction-oil-gas, notice-trees-in-con-area | MAY | Rule: is a MUST if `conflict-to-declare` is `True` |

**Validation rules**

- person-reference must equal an `applicant-details.applicants.reference` or an `applicant-details.agent.reference`