# User groups for user needs

We have defined a set of user groups that we use in the planning application user needs.

The purpose of these groups is to keep user needs readable and reusable. A need should not have to list every possible user who benefits from the information. At the same time, the actor should not be so broad that it hides the motivation for the need.

## Principles

- Use the most specific user group that still describes the need without narrowing it.
- Use a broader group when the same motivation genuinely applies across several kinds of user.
- Do not list multiple users in the statement just to avoid choosing a group.
- Do not use a specialist job title as the main actor unless the need only makes sense for that specialist role.
- Keep specialist roles, sectors or service contexts as supporting detail where they help explain evidence or implementation.

## User groups

| User group | Description and motivation | Current actors to rationalise |
|---|---|---|
| `applicant` | People applying for planning permission or acting for the applicant interest. They need to understand requirements, track progress, respond to requests and comply with decisions, conditions and obligations. | `applicant`, `agent`, `developer` |
| `appellant` | People challenging or involved in an appeal. They need reliable records of what happened, what was decided and what evidence or contextual data affected the decision. | `appellant` |
| `oversight-body` | Organisations or bodies that review, scrutinise or challenge planning decisions or processes after the event. They need reliable records so appeals, audits, investigations, enforcement questions or legal reviews can be checked against the information available at the relevant point in the process. | `oversight-body` |
| `public-user` | People outside the formal application team who want to understand, scrutinise or respond to planning activity affecting places they care about. They need information that is easy to find, recognise and interpret. | `member of public`, `member-of-public`, `member-of-the-public`, `public`, `citizen`, `interested-party` |
| `consultee` | Organisations or specialists asked to comment on applications. They need clear, timely and traceable information so they can provide advice within the planning process. | `consultee` |
| `planning-practitioner` | People doing planning casework, assessment, compliance, enforcement or specialist review. They need structured, reliable information to process applications, make decisions and manage records. | `planner`, `planning-officer`, `planning-authority-officer`, `development-management-planner`, `conservation-officer`, `heritage-officer`, `enforcement-officer`, `monitoring-officer`, `community-planning-officer`, `conservation-area-planner`, `housing-planning-officer`, `town-centre-planner`, `high-street-planner`, `economic-planning-officer`, `local-economic-development-planner` |
| `planning-authority` | The organisation responsible for administering the planning process. It needs consistent records to meet statutory duties, publish information, manage applications and support accountability. | `planning-authority`, `local-authority`, `authority-user` |
| `planning-service-manager` | People responsible for running or improving planning services. They need data to manage performance, workload, service quality and operational risk. | `planning-manager`, `planning-service-manager`, `planning-authority-manager`, `service-lead` |
| `strategic-planning-user` | People using planning data for place shaping, growth, housing, high streets or economic strategy. They need aggregated and comparable information to understand trends and plan interventions. | `strategic-planner`, `place-shaping-lead`, `housing-planning-lead`, `town-centre-lead`, `economic-regeneration-lead` |
| `analyst` | People analysing planning data across cases, areas or time periods. They need consistent, linkable and well-described data for monitoring, reporting, comparison and evidence building. | `analyst`, `central-government-analyst`, `housing-delivery-analyst` |
| `policy-user` | People shaping, stewarding or overseeing planning policy and standards. They need evidence about how the planning system is working so they can evaluate policy, target improvements and maintain trust. | `policy-maker`, `central-government`, `mhclg`, `policy-steward`, `planning-system-steward` |
| `service-builder` | People designing, building, integrating or operating digital planning services. They need stable, well-modelled data so services can exchange information, automate workflows and present planning records consistently. | `service-builder`, `software-supplier`, `system-integrator`, `public-register-service`, `process-user` |
| `planning-system-user` | People who need to understand or use planning application information across the planning system. Use this when the same need genuinely applies across several user groups and choosing one narrower group would misrepresent the breadth of the need. | `planning-system-user` |

## Using `planning-system-user`

`planning-system-user` should not be treated as a mistake or automatically replaced by a narrower group. It is useful where the need is about shared understanding of the planning process or record, and where the benefit is not limited to one role.

Use `planning-system-user` when:

- the same information need applies to applicants, public users, planning practitioners and other users in substantially the same way
- listing all relevant users would make the need harder to read
- choosing one group would incorrectly imply that the information exists primarily for that group
- the motivation is broad transparency, traceability, discovery or process understanding

Avoid `planning-system-user` when:

- the need is really about a specific task, duty or decision owned by one user group
- the need is analytical, operational, policy or service-building work that has a clearer user group
- the broad group is being used only because the evidence mentions several different users

Current `planning-system-user` needs mostly relate to:

- shared process transparency, especially timelines and key events
- site and location discovery
- access to decision, committee and officer-report information
- traceability between applications, decisions and conditions
- cross-cutting data principles such as spatial representation and familiar location identifiers

## Data-domain user groups

Some needs apply to the data itself rather than to a particular role in the planning system. These needs should use a data-domain user group so they remain applicable wherever the data is produced, exchanged or used.

| User group | Description and motivation |
|---|---|
| `data-user` | People or systems consuming planning application data. They need data that can be understood, interpreted and used reliably, regardless of the particular planning task or service in which it is used. |

Use `data-user` when the need describes a general property or capability of the data, such as identity, context, provenance or interoperability, and does not depend on a planning-domain role or task.

Use a planning user group such as `analyst`, `planning-practitioner` or `service-builder` when the motivation comes from a specific planning activity. A person may be both a planning-domain user and a data user, but the need should use the group that best explains why it exists.
