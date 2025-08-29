# Grounds for lawful development certificate

Grounds on which a lawful development certificate is being sought,
including supporting evidence and explanations


**Grounds for lawful development certificate module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| grounds-pre-2024 | Grounds pre 2024[] | List of grounds pre 2024-04-25 under which the certificate is sought |  | MAY | Select from the **grounds-ldc-pre-apr-2024** enum |
| grounds-post-2024 | Grounds post 2024[] | List of grounds post 2024-04-25 under which the certificate is sought |  | MAY | Select from the **grounds-ldc-post-apr-2024** enum |
| other-details | Other details | Explanation if other ground is selected |  | MAY |  |
| supporting-applications | Supporting applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site |  | MAY |  |
| reason | Reason | A textual reason |  | MUST |  |


**Supporting applications component**

field | name | description | required | notes
-- | -- | -- | -- | --
reference-number | Reference number | Reference number of the planning permission | MAY | 
condition-number | Condition number | Number of any condition being breached | MAY | 
decision-date | Decision date | The date when the decision was made, in YYYY-MM-DD format | MAY | 

**Validation rules**

- grounds-pre-2024 is not empty OR grounds-post-2024 is not empty
- if grounds-pre-2024 contains 'other' OR grounds-post-2024 contains 'other' then other-details is required