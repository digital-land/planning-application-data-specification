# Interest in land

Information about the applicant's interest in the land where an advertisement 
will be displayed, including ownership status and permission arrangements


| applicant-owns-land | Applicant owns land | True or False indicating whether the applicant owns the land where the advertisement will be displayed |  | MUST |  |
| permission-obtained | Permission obtained | True or False indicating whether permission of the owner for the display of an advertisement has been obtained |  | MAY |  |
| permission-not-obtained-details | Permission not obtained details | Details explaining why permission from the land owner has not been obtained for the advertisement display |  | MAY |  |

**Validation rules**

- permission-obtained must be provided when applicant-owns-land is false
- permission-not-obtained-details must be provided when applicant-owns-land is false and permission-obtained is false