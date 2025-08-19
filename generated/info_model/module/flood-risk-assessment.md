# Flood risk assessment

Information about flood risk assessments for planning applications including flood risk area status, 
data sources, assessment documents, watercourse proximity, flood risk impacts, and surface water disposal methods


| reference | name | description | only for application | requirement | notes |
| --- | --- | --- | --- | --- | --- |
| flood-risk-area | Flood risk area | Is the site within an area at risk of flooding? |  | MUST |  |
| data-provided-by | Data provided by | Who provided the data: Applicant or System/Service? |  | MAY | Select from the **provided-by** enum. opens possibility for services to work it out and not rely on the applicant to know |
| flood-risk-assessment | Flood risk assessment | Reference of the flood risk assessment document |  | MAY | Rule: is a MUST if `flood-risk-area` is `True` |
| within-20m-watercourse | Within 20m watercourse | Whether the development is within 20 metres of a watercourse |  | MUST |  |
| increases-flood-risk | Increases flood risk | Whether the development increases flood risk |  | MUST |  |
| surface-water-disposal | Surface water disposal[] | Method for disposing of surface water |  | MUST | Select from the **surface-water-disposal-type** enum |

**Validation rules**

- flood-risk-assessment document reference is required when flood-risk-area is true
- surface-water-disposal must contain at least one disposal method