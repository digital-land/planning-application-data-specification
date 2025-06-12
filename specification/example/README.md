# Example Site Visit JSON

These examples show valid JSON structures for the site-visit module under different scenarios.

## site-visit-applicant.json
Shows a site visit where:
- The site can be seen from public land
- The applicant is the contact person
- Includes applicant details from the main application

## site-visit-other.json
Shows a site visit where:
- The site cannot be seen from public land
- A third party is the contact person
- Full contact details are provided in the other-contact structure

Note that when contact-type is "other", the other-contact structure must include all required fields (fullname, phone-number, and email).
