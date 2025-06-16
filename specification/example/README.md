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

# Example JSON Files

These examples show valid JSON structures for different modules under different scenarios.

## Parking Module Examples

### parking-no-changes.json
Shows a parking submission where:
- No changes are being made to existing parking arrangements
- Minimal response required (just boolean flag)

### parking-with-changes.json
Shows a parking submission where:
- Existing parking arrangements are being modified
- Includes required description of the changes
- Example shows common scenario of garage conversion

Notes:
- Description should be specific about the impact on parking spaces
- Both on-street and off-street parking changes should be described
- Local authority may need to validate against parking standards

## Pre-application Advice Examples

### pre-app-advice-none.json
Shows a submission where:
- No pre-application advice was sought
- Only requires boolean flag

### pre-app-advice-with-reference.json
Shows a submission where:
- Formal pre-application advice was received
- Reference number provided
- No summary needed as reference links to formal advice

### pre-app-advice-informal.json
Shows a submission where:
- Informal pre-application advice was received
- No formal reference number available
- Detailed summary of advice provided instead

Key points demonstrated:
- Conditional field requirements based on advice-sought
- Alternative between reference and summary
- Date format requirements
- Proper summary formatting

## Trees and Hedges Examples

### trees-hedges-none.json
Shows a submission where:
- No trees/hedges on site or adjacent land
- No falling trees risk
- No tree removal needed
- Minimal response with all boolean flags false

### trees-hedges-removal.json
Shows a submission where:
- Trees present on development site
- Tree removal/pruning required
- Includes tree removal plan document reference
- No falling trees risk identified

### trees-hedges-risk.json
Shows a submission where:
- Trees present on both site and adjacent land
- Falling trees risk identified
- Includes risk assessment document reference
- No tree removal needed

Key points demonstrated:
- Conditional document requirements
- Document reference structure
- Boolean flag combinations
- Proper document naming

## Declaration Examples

### declaration-applicant.json
Shows a declaration where:
- Declaration made by the applicant directly
- All required fields provided (name, confirmation, date)
- Date is in correct YYYY-MM-DD format

### declaration-agent.json
Shows a declaration where:
- Declaration made by the agent on behalf of applicant
- Name matches agent details from application
- Current date used for declaration

Key points demonstrated:
- Module wrapping with "declaration" key
- Date format requirements
- Name matching requirements
- Boolean confirmation flag

## Description of Proposal Examples

### description-of-proposal-hh.json
Shows a basic householder application where:
- Simple proposal description for extension
- Work has not started or completed
- No related applications or reserved matters needed

### description-of-proposal-reserved.json
Shows a reserved matters application where:
- Multiple reserved matters being approved
- Links to previous outline permission
- Includes full related application details
- Work not yet started

### description-of-proposal-retrospective.json
Shows a retrospective application where:
- Work has already been completed
- Includes both start and completion dates
- Description indicates retrospective nature
- Dates are in valid sequence

Key points demonstrated:
- Module wrapping with "description-of-proposal" key
- Conditional field inclusion based on application type
- Date format requirements
- Related application structure
- Reserved matters array format
