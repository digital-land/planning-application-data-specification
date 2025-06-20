---
application-type: hh
name: Householder application with minimal fee structure
---

```json
{
  "application": {
    "reference": "550e8400-e29b-41d4-a716-446655440001",
    "application-types": ["hh"],
    "planning-authority": "LPA002",
    "submission-date": "2025-06-20",
    "modules": [
      "applicant-details",
      "site-details",
      "proposal-details"
    ],
    "documents": [
      {
        "reference": "DOC-HH-001",
        "name": "Location Plan",
        "document-types": ["location-plan"],
        "file": {
          "url": "https://storage.example.com/hh/location.pdf",
          "filename": "location.pdf",
          "mime-type": "application/pdf"
        }
      }
    ],
    "fee": {
      "amount": 206.00,
      "amount-paid": 0.00
    }
  }
}
```

This example shows:
* Householder application with simpler structure
* No application sub-type (optional field)
* Minimal document requirements
* Fee structure without transactions (optional field)
* File without optional metadata fields
