| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| advertisement-proposal-description |  |  | MUST | |
| advertisement-proposal-type[]{} | Expected to provide counts for each advertisement type | | MUST |  |

**advertisement-proposal-type**

| field | description | notes |
| --- | --- | --- |
| advertisement-type | one of the advertisement-types or other | see [advertisement-type enum](https://github.com/digital-land/planning-application-data-specification/discussions/190) |
| advertisement-count | number of this type of advertisement | |
| advertisement-other-description | If other is selected then details are required | |
