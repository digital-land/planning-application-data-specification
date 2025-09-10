# Trade effluent

Details of any liquid waste produced by industial processes on the proposed site, and how it will be diposed of.

**Trade effluent module**

| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| is-disposal-required | Disposal required | Does the proposal involve the disposal of trade effluents or waste (true/false) |  | MUST |  |
| description | Description | describe the nature, volume and means of disposal of trade effluents or waste |  | MAY | Rule: is a MUST if `disposal-required` is `True` |

**Validation rules**

- description is required when disposal-required is true
- Module applies to full, extraction-oil-gas, and outline application types