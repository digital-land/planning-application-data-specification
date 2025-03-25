| field | description | application-types | required | notes | 
| --- | --- | --- | --- | --- |
| name | A name of the person making the declaration |  | MUST |  Rule: `name` should match one of the names of the named individuals |
| declaration-confirmed | Confirms the applicant or agent has reviewed and validated the information provided in the application | | MUST | (`true` / `false`)
| declaration-date | The date, in YYYY-MM-DD format, the declaration was made | | MUST | Rule: date must be complete and in `YYYY-MM-DD` format |
