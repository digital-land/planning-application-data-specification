---
application-type: pip
name: PIP application with required contact details
---

```json
{
  "applicant-details": {
    "applicants": [
      {
        "reference": "APP-001",
        "person": {
          "first-name": "Sarah",
          "last-name": "Wilson",
          "contact-address": {
            "address-text": "789 Park Road, Manchester",
            "postcode": "M1 1AA"
          }
        },
        "contact-details": {
          "email": "sarah.wilson@example.com",
          "phone-numbers": [
            {
              "number": "0161 234 5678",
              "contact-priority": "primary"
            }
          ]
        }
      }
    ]
  }
}
```

This example shows:
* Planning in Principle (PIP) application where contact details are required
* Single applicant with minimal required fields
* Contact details with single primary phone number
* Address details without optional title field
