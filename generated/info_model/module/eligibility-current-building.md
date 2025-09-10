# Eligibility current building

How the current building meets eligibity criteria

**Eligibility current building module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| was-constructed-btw-1948-2018 | Was constructed between 1948 and 2018 | Was the current building constructed between 1 July 1948 and 28 October 2018? If False, application cannot proceed. |  | MUST |  |
| has-additional-storeys | Additional storeys added | Have additional storeys already been added to the original building? If True, application cannot proceed. |  | MUST |  |
| was-use-granted-by-pdr | Use granted by permitted development right | Was the current use of the building granted by permitted development rights? If True, application cannot proceed. |  | MUST |  |
| is-site-in-restricted-area | Site in restricted area | Is any part of the land or site located in a restricted area? If True, application cannot proceed. |  | MUST |  |

**Validation rules**

- was-constructed-btw-1948-2018 == true (required for application to proceed)
- has-additional-storeys == false (required for application to proceed)
- was-use-granted-by-pdr == false (required for application to proceed)
- is-site-in-restricted-area == false (required for application to proceed)
- was-constructed-btw-1948-2018 == true AND has-additional-storeys == false AND was-use-granted-by-pdr == false AND is-site-in-restricted-area == false