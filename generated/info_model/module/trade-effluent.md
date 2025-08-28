# Trade effluent

Information about the disposal of trade effluents or waste, including whether 
disposal is required and details about the nature, volume and means of disposal


| is-disposal-required | Disposal required | Does the proposal involve the disposal of trade effluents or waste (true/false) |  | MUST |  |
| description | Description | describe the nature, volume and means of disposal of trade effluents or waste |  | MAY | Rule: is a MUST if `disposal-required` is `True` |

**Validation rules**

- description is required when disposal-required is true
- Module applies to full, extraction-oil-gas, and outline application types