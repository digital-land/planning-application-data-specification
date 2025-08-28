# Voluntary agreement

Information about voluntary agreements related to extraction oil and gas applications, 
including whether a draft agreement is included and summary details


| draft-agreement-included | Draft agreement included | Has an outline or draft agreement been included? (True / False) |  | MUST |  |
| agreement-summary | Agreement summary | Summary of the agreement |  | MAY | Rule: is a MUST if `draft-agreement-included` is `True` |

**Validation rules**

- agreement-summary is required when draft-agreement-included is true
- Module only applies to extraction-oil-gas application types