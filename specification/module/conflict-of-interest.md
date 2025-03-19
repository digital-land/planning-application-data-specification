| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | With respect to the Authority, is any named individual a member of staff, an elected member, related to a member of staff or related to an elected member  | | MUST | answer may be different depending on the parties involved |
| name | Name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how individual is related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST |
