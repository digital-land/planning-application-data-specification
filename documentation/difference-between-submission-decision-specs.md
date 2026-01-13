# The differences between the submission specification and the decision specification

## The core distinction: inputs vs. outcomes

The fundamental difference between the two specifications lies in their position and function within the planning permission process.

The Submission Specification is designed to control and validate inputs (what is required to assess an application), whereas the Decision Specification is designed to record outcomes (what was decided and legally agreed upon).

### The submission specification: driven by business logic

The submission specification essentially baselines existing planning application forms, recreating their purpose as structured data. Because its primary goal is to facilitate the validation and assessment of an application, it embeds business logic.

* **Logic and validation**  
  This specification includes explicit logic to "guide" the data entry. It uses conditional rules (e.g., "if X is true, then Y is required") to ensure that the data payload is valid before it even reaches a planning officer,.
  For example, if a user indicates `will-residential-units-change` is "true", the logic dictates that a `residential-unit-summary` MUST be provided.
* **Purpose**
  It acts as a gatekeeper. By defining field types, constraints, and conditional logic, it allows systems to automatically validate data payloads, ensuring that what is submitted matches the strict legislative requirements. Ideally, this shifts the burden of accuracy onto the system rather than the applicant.

Therefore, the **submission specification takes the form of an object model** because an application is a single, bundled object containing everything required to validate and assess it at the point of submission.


### The decision specification: a record of fact

In contrast, the decision specification defines the data needed to represent the outcome of the process.

It does not require the same "input validation" business logic because it is recording a set of events that have already occurred and artefacts produced, rather than guiding a user through a variable process.

* **Focus on the record**
  This specification is designed to capture "all the up-to-date stuff at the point of the decision". It creates a structured record of the Decision Notice, which is the legal instrument of the planning system.
* **Components without conditional logic**
  Instead of complex "if/then" input rules, this specification focuses on linking static data points to create a transparent audit trail, including:
  * What: The decision outcome (granted/refused) and the reasons.
  * Conditions: A structured record of conditions imposed, including who requested them and their status (e.g., discharged),.
  * Process: An application log capturing what happened (consultations, dates).
* **Purpose**
  Its primary users are monitoring teams, developers, and policymakers who need to analyse trends, track housing delivery, or manage appeals,. It ensures that the legal decision is "authoritative, traceable, and valid" for downstream processes.


Therefore, the **decision specification is best represented as a relational model**, as it must connect multiple linked records, for example decisions, conditions, logs, ,e tc, rather than package everything into a single object. This mirrors how the decision and its components exist and evolve in practice.

## Summary comparison

Below is a summary of the key differences between the two specifications.

| Feature | Submissions | Decisions |
| --- | --- | --- |
| Primary role | Input: Defines what is needed to validate and assess an application |Outcome: Captures what is known after a decision is made |
| Logic type | Active/conditional: Uses business logic (declarative model) to enforce rules and validate data upon entry | Passive/record-keeping: Records the final state of facts and legal obligations (conditions) |
| Key artefact | Application form (converted to data) | Decision notice (converted to data) |
| User goal | "I want to build something" / "I know if I can build something" | "I need to know what has been granted" / "I need to monitor policy impact" |
| Model type | Object | Relational |

## Analogy

To visualise the difference:

* The **Submission specification** is like a digital tax return form. It has built-in logic that stops you from proceeding if you miss a box or enter conflicting numbers (business logic/validation).
* The **decision specification** is like the receipt or certificate you receive afterwards. It doesn't ask you questions; it simply records the final, unchangeable facts of the transaction for your records and for auditors (outcome/record).
