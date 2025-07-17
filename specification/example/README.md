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

## LDC Interest Module Examples

### ldc-interest-owner.json
Shows a submission where:
- Applicant is the owner of the listed building
- No additional owner details or interested persons required
- Simplest case for Listed Building Consent applications

### ldc-interest-lessee.json
Shows a submission where:
- Applicant is a lessee of the listed building
- Owner details must be provided including notification status
- Single owner with complete person details and confirmation they were informed

### ldc-interest-interested-persons.json
Shows a submission where:
- Applicant has no direct interest in the property
- Multiple interested persons with different notification scenarios
- Includes both informed and not-informed persons with reasons
- Shows various types of interest (heritage group, adjacent owner)

### ldc-interest-complex.json
Shows a comprehensive submission where:
- Applicant is an occupier requiring owner details
- Multiple owners including corporate entities
- Additional interested persons with academic interest
- Demonstrates complex ownership and interest scenarios

Notes:
- When applicant-interest is "lessee" or "occupier", owner-details is required
- When applicant-interest is "none", interested-persons is required
- Person objects must include required fields: first-name, last-name, address-text
- reason-not-informed is only provided when informed-of-application is false
- Nature of interest should describe the person's specific connection to the property

## Hedgerow Removal Module Examples

### hedgerow-removal-owner.json
Shows a hedgerow removal notice where:
- Applicant is the owner of the land
- Hedgerow is older than 30 years (no planting evidence required)
- Agricultural access improvements for machinery
- Multiple plan references showing removal areas
- Standard numeric length specification

### hedgerow-removal-utility.json
Shows a hedgerow removal notice where:
- Utility operator is removing hedgerow for infrastructure
- Broadband network expansion project
- Multiple technical plan references
- Applicant has utility operator interest declaration
- Hedgerow is established (over 30 years old)

### hedgerow-removal-young-hedge.json
Shows a hedgerow removal notice where:
- Agricultural tenant is replacing old hedgerow
- Hedgerow is less than 30 years old
- Planting evidence is attached as required
- Farm modernization with native species replacement
- Demonstrates conditional requirement fulfillment

### hedgerow-removal-no-evidence.json
Shows a hedgerow removal notice where:
- Farm business tenant expanding existing buildings
- Hedgerow is less than 30 years old
- No planting evidence is attached (potential compliance issue)
- Business expansion for livestock housing
- Demonstrates scenario where conditional requirement may not be met

Notes:
- When hedgerow-less-than-30-years is true, planting-evidence-attached should be true
- hedgerow-length must be a positive number (in metres)
- plan-references should correspond to documents in application.documents
- interest-declaration must use values from hedgerow-interest-dec codelist
- removal-reasons should provide clear justification for the proposed removal

## Grounds for Proposed Use Module Examples

### grounds-proposed-use-permanent.json
Shows a grounds for proposed use submission where:
- Standard use class (B1 - Business) is specified
- Permanent operation type
- Reason based on established use through time
- No additional details required for permanent use

### grounds-proposed-use-temporary.json
Shows a grounds for proposed use submission where:
- Standard use class (A3 - Restaurants and cafes) is specified
- Temporary operation type requiring additional details
- Comprehensive temporary-details explaining duration and restrictions
- Reason covering temporary use provisions

### grounds-proposed-use-sui-generis.json
Shows a grounds for proposed use submission where:
- Sui generis use class requiring specification
- Specified-use provides detailed description of unique use
- Permanent operation with specialized requirements
- Reason explaining why the use is considered sui generis

### grounds-proposed-use-other.json
Shows a grounds for proposed use submission where:
- "Other" use class requiring specification
- Mixed-use development not fitting standard classes
- Specified-use describes the combination of uses
- Reason referencing permitted development provisions

Notes:
- When use is "sui" or "other", specified-use is required
- When operation-type is "temporary", temporary-details is required
- Reason should provide legal justification for lawful development
- Use class should reference the use-class codelist values
- Operation-type uses values from operation-type codelist (permanent/temporary)
