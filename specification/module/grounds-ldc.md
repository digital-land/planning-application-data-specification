Field | Description | Application-type | Required? | Notes
-- | -- | -- | -- | --
grounds-pre-2024[] | List of grounds pre 2024-04-25 under which the certificate is sought | | MUST | At least one ground must be selected. See [Grounds Enum](https://github.com/digital-land/planning-application-data-specification/discussions/204)
grounds-post-2024[] | List of grounds post 2024-04-25 under which the certificate is sought | | MUST | At least one ground must be selected. See [Grounds Enum](https://github.com/digital-land/planning-application-data-specification/discussions/204) .
other-details | Explanation if "Other" ground is selected | | MAY | Required if grounds-pre-2024 or grounds-post-2024 includes other.
supporting-applications[]{} | List of supporting planning permissions, certificates, or notices affecting the application site. Include its date and the number of any condition being breached | | MAY | Optional, but strengthens the application.
reason | Reason why the development is considered lawful | | MUST | Applicant’s explanation for granting the certificate.

**Supporting applications / decisions**

_This is similar to other models where supporting or related applications are required. the difference being that this one also needs the condition number._

Field | Description | Data Type | Required? | Notes
-- | -- | -- | -- | --
reference-number | Reference number of planning permission, certificate, or notice | String | MAY | Optional, strengthens application.
condition-number | Number of any condition being breached | String | MAY | Relevant if certificate relates to condition breach.
decision-date | Date of the decision (DD/MM/YYYY) | Date | MAY | Must be before the application submission date.
