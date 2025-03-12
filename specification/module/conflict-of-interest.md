| field | description | application-types | required | notes |
| --- | --- | --- | --- | --- |
| conflict-to-declare | True or False based on statements in "With respect to the Authority, I am" list | | MUST | answer may be different depending on the parties involved |
| name | name of the individual with the conflict | | MAY | Rule: if `conflict-to-declare` is true, name who has the conflict. Rule: `name` should match one of the names provided in applicants/agent section. Should this be structured data (first-name, surname)? |
| details | Details including name, role and how you are related to them | | MUST, MAY | Rule: if `conflict-to-declare` is true then this is a MUST. |
