# Tree preservation order details

Details of any Tree Preservation Orders (TPO) affecting the development site

**Tree preservation order details module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| tpo-reference | TPO reference[] | Reference for a Tree Preservation Order covering affected trees |  | MAY |  |
| tpo-provided-by | TPO provided by | How was the list of TPO references generated - by the applicant or system/service |  | MAY | Select from the **provided-by** enum |

**Validation rules**

- TPO references should be verified by the authority if provided by applicant
- Authority can use tpo-provided-by to determine validation requirements