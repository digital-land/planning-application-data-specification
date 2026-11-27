# Proposed demolition works

Buildings, reasons, methods, site restoration, expected dates and effects of proposed demolition works.

**Proposed demolition works module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| description | Description | Description of the buildings to be demolished. |  | MUST |  |
| reason | Reason | Reason why demolition needs to take place. |  | MUST |  |
| demolition-method | Demolition method | Description of the proposed method of demolition. |  | MUST |  |
| site-restoration-details | Site restoration details | Details of the proposed restoration of the site following demolition. |  | MUST |  |
| expected-works-start-date | Expected works start date | Date when the proposed works are expected to start. |  | MUST |  |
| expected-works-end-date | Expected works end date | Date when the proposed works are expected to be completed. |  | MUST |  |
| has-public-right-of-way | Public right of way on or adjoining site | Whether any public rights of way are within or immediately adjoining the site. |  | MUST |  |
| later-redevelopment-proposed | Later redevelopment proposed | Whether redevelopment or rebuilding is proposed at a later date following demolition. |  | MUST |  |
| tree-removal | Tree removal | Whether the proposal involves the felling or pruning of any trees. |  | MUST |  |
| supporting-documents | Supporting documents[]{} | References to plans showing details of the proposed tree felling or pruning. |  | MAY | Rule: is a MUST if `tree-removal` is `True` |
| demolition-spoil-disposal | Demolition spoil disposal | Description of how and where spoil or rubble from the proposed demolition would be disposed of. |  | MUST |  |


**Supporting document component**

field | name | description | required | notes | only for application
-- | -- | -- | -- | -- | --
reference | Reference | A unique reference for the data item | MUST |  | 
details | Details | Additional details or information about an item | MAY |  | pip

**Validation rules**

- `expected-works-start-date` and `expected-works-end-date` must both be after the application submission date.