---
reference: planning-application-planning-performance-agreement
dataset: planning-application
field: planning-performance-agreement
---

### How to use it

Use this field only to classify whether the particular planning application was subject to a Planning Performance Agreement (PPA).

- Use `subject-to-ppa` when a PPA applied.
- Use `not-subject-to-ppa` when it is known that no PPA applied.
- Use `unknown` when the authority cannot establish whether a PPA applied.

The field has a `MUST` requirement level, so supply one of these values for each application. Do not use `unknown` simply because no one has checked. An omitted value means the classification has not been supplied.

These values do not distinguish a renegotiated PPA from another PPA. Do not use this field to describe the agreement, its terms or its milestones.
