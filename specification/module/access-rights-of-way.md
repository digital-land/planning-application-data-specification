| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| new-altered-vehicle | Is a new or altered vehicle access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-altered-pedestrian | Is a new or altered pedestrian access proposed to/from the public highway? | extraction-oil-gas;full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| change-right-of-way | Will the proposal change public rights of way? (diversion/extinguishment/creation) | full;hh;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers.|
| new-right-of-way | Will new public rights of way be provided within or adjacent to the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| new-public-road | Will new public roads be provided within the site? | extraction-oil-gas;full;outline | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| temp-right-of-way | Are temporary changes to rights of way needed while the site is worked? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| future-new-right-of-way | Will new public rights of way be provided after extraction? | extraction-oil-gas | MUST | See [rights of way answers enum](https://github.com/digital-land/planning-application-data-specification/discussions/210) for possible answers. |
| supporting-documents[]{} | List of documents supporting the information provided | extraction-oil-gas;full;hh;outline | MAY | Required if any answer is `true`. |

**supporting documents**

field | description | data type | required? | notes
-- | -- | -- | -- | --
reference | Unique identifier for the document. It should match a document attached to the application | String | MUST | Must be provided for each document. Rule: must match a reference in `application.documents`
name | Name of the document | String | MUST | Descriptive name for clarity