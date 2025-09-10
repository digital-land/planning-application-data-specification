# Voluntary agreement

Details of any voluntary agreements made as part of an oil and gas extraction application.

**Voluntary agreement module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| draft-agreement-included | Draft agreement included | Has an outline or draft agreement been included? (True / False) |  | MUST |  |
| agreement-summary | Agreement summary | Summary of the agreement |  | MAY | Rule: is a MUST if `draft-agreement-included` is `True` |

**Validation rules**

- agreement-summary is required when draft-agreement-included is true
- Module only applies to extraction-oil-gas application types