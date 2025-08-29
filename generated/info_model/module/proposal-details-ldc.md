# Proposal details LDC

Details of the proposal for lawful development certificate applications

**Proposal details LDC module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| proposal-incl-building-operations | Proposal incl building operations | Does the proposal include building operations? |  | MUST | For lawful development certificate for proposed work |
| proposal-building-operations-description | Proposal building operations description | Description of the building operations included in the proposal |  | MAY | Rule: is a MUST if `proposal-incl-building-operations` is `True` |
| proposal-incl-change-of-use | Proposal incl change of use | Does the proposal include a change of use? |  | MUST |  |
| proposal-change-of-use-description | Proposal change of use description | Description of the change of use included in the proposal |  | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True`. Required if proposal-incl-change-of-use is true |
| proposal-existing-use-description | Proposal existing use description | Description of the existing use before the proposed change of use |  | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-existing-use-stop-date | Proposal existing use stop date | Date when the existing use stopped or will stop |  | MAY | Rule: is a MUST if `proposal-incl-change-of-use` is `True` |
| proposal-started | Proposal started | Has any work on the proposal already been started |  | MUST |  |

**Validation rules**

- proposal-building-operations-description is required when proposal-incl-building-operations is true
- proposal-change-of-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-description is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date is required when proposal-incl-change-of-use is true
- proposal-existing-use-stop-date must be in YYYY-MM-DD format