---
description: Name and contact information if an agent is being used.
end-date: ''
entry-date: 2025-05-30
fields:
- field: agent-reference
  required-if: 
    - field: agent-details.agent.reference
      operator: not_empty
- field: contact-details
  required-if: 
    - field: agent-details.agent.reference
      operator: not_empty
module: agent-contact
name: Agent contact details
---
