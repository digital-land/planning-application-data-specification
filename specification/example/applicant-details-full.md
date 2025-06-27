---
application-type: full
name: Full application with multiple applicants
---

```json
{
  "applicant-details": {
    "applicants": [
      {
        "reference": "APL-001",
        "person": {
          "title": "Mrs",
          "first-name": "Jane",
          "last-name": "Smith",
          "address-text": "123 Main Street, London",
          "postcode": "SW1A 1AA"
        },
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
      },
      {
        "reference": "APL-002",
        "person": {
          "title": "Mr",
          "first-name": "John",
          "last-name": "Doe",
          "address-text": "456 High Street, London",
          "post-code": "SW1A 2BB"
        },
        "contact-details": {
          "email": "john.doe@example.com",
          "phone-numbers": [
            {
              "number": "020 7987 6543",
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
* Full application with multiple applicants
* Each applicant has a unique reference
* Complete person details including optional title and postcode
* Contact details for each applicant
* Phone numbers with primary/secondary priorities
