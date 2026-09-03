---
reference: planning-application-document-public-register-status
dataset: planning-application-document
field: public-register-status
---

### How to use it

Use `public-register-status` to record whether an individual document may be made publicly available on the planning register.

Assess each document separately. This field is not the status of the planning application and must not contain workflow values such as `valid`, `under-consideration`, `approved` or `withdrawn`.

Use one of the values from the `public-register-status` codelist:

| Value | Use when |
| --- | --- |
| `publish` | The document has been assessed as suitable for public availability. |
| `withhold` | The document should not be made publicly available because access needs to be controlled. |
| `not-assessed` | No decision has yet been recorded about whether the document is suitable for public availability. |

Only records with `public-register-status` set to `publish` are included in the National Public View.
