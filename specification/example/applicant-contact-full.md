---
application-type: full
name: Full application with applicant contact details
---

```json
{
  "applicant-contact": {
    "applicant-reference": "APL-001",
    "contact-details": {
      "email": "jane.smith@example.com",
      "phone-numbers": [
        {
          "number": "020 7123 4567",
          "contact-priority": "primary"
        },
        {
          "number": "07700 900123",
          "contact-priority": "secondary"
        }
      ]
    }
  }
}
```

This example shows:
* Full application with applicant contact details
* Reference to an applicant from the applicant details component
* Email address and multiple phone numbers
* One primary and one secondary contact number
