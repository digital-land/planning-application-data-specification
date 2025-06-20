---
application-type: full
name: Full planning application with documents and fee
---

```json
{
  "application": {
    "reference": "550e8400-e29b-41d4-a716-446655440000",
    "application-types": ["full"],
    "application-sub-type": "major-dwellings",
    "planning-authority": "LPA001",
    "submission-date": "2025-06-20",
    "modules": [
      "applicant-details",
      "site-details", 
      "proposal-details",
      "bng"
    ],
    "documents": [
      {
        "reference": "DOC-001",
        "name": "Site Location Plan",
        "description": "Plan showing the location of the application site",
        "document-types": ["location-plan"],
        "file": {
          "url": "https://storage.example.com/documents/location-plan.pdf",
          "filename": "location-plan.pdf",
          "mime-type": "application/pdf",
          "checksum": "sha256:d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2d2",
          "file-size": 2048576
        }
      },
      {
        "reference": "DOC-002", 
        "name": "Proposed Plans",
        "description": "Architectural drawings of the proposed development",
        "document-types": ["proposed-plans"],
        "file": {
          "base64": "JVBERi0xLjQKJcfsj6IKNSAwIG9iago8PAovTGVuZ3RoIDYgMCBSCi9GaWx0ZXIgL0ZsYXRlRGVjb2RlCj4+CnN0cmVhbQp4nFvzloEBCQACCw==",
          "filename": "proposed-plans.pdf",
          "mime-type": "application/pdf",
          "file-size": 1024000
        }
      }
    ],
    "fee": {
      "amount": 462.00,
      "amount-paid": 462.00,
      "transactions": ["TXN-20250620-001"]
    }
  }
}
```

This example shows:
* Full planning application with complete metadata
* Multiple application types and sub-type classification
* Required modules for validation
* Documents with both URL and base64 file storage options
* Complete fee structure with payment information
* File metadata including checksums and sizes for validation
