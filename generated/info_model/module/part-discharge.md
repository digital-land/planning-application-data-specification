# Part discharge

Information about whether the applicant is trying to discharge part of a condition
and details about which part of the condition is being addressed


**Part discharge module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-discharging-part | Is discharging part | Is applicant trying to discharge part of condition? |  | MUST |  |
| discharging-part-details | Discharging part details | Indicate which part of the condition the application relates to |  | MAY | Rule: is a MUST if `discharging-part` is `True` |

**Validation rules**

- discharging-part-details is required when is-discharging-part is true
- discharging-part-details should specify which part of the condition is being addressed