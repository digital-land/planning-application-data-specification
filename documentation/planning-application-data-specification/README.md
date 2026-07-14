# Planning application data specification

The planning application data specification defines the authoritative record data that a planning authority creates and maintains as a planning application moves through the planning permission process. It includes application records, sites, documents, process events, decision notices, conditions and section 106 agreements.

### Purpose

The planning application data specification is designed to:

* Standardise how planning application records are created, maintained and shared, so authorities can exchange consistent, machine-readable data.
* Create an authoritative record that can be reused across planning registers, reports and connected systems.
* Reduce manual and repetitive tasks, including producing PS1 and PS2 returns.
* Improve transparency and interoperability by linking application, process, decision and related records across the planning process.
* Support monitoring, policymaking, national statistics, housing-delivery tracking and local performance insight.
* Free up planners’ time by reducing administrative data entry and reporting.

### Research

Unlike the submission specification, which could start from established planning application forms, the planning application data specification needs foundational research into the records that planning authorities create and maintain through the planning permission process.

Our aim is to understand what information is actually needed, by whom, and for what purpose before defining any data structure. We’ve started by gathering evidence through broad engagement with the community (interviews and questionnaires) and are now carrying out deep-dive research sessions to explore specific user needs in more detail.

This approach follows the “start small” principle: we’ll begin with a minimal, evidence-based core and only add parts and fields once there is a clear and validated need.

### Authoritative application data

The `planning-application-data` dataset identifies the authoritative structured
application data at two important points:

* `submitted-data-uri` identifies the application data as first received by the
  planning authority.
* `validated-data-uri` identifies the application data accepted through planning
  validation. It is required where the application has a `found-valid` event in
  `planning-permission-timeline`.

These URIs allow authorised users or systems to identify and retrieve the
artefacts. They do not imply public access or prescribe how the artefacts are
stored. Documents remain separate records in `planning-application-document`.

See [Reference authoritative application artefacts without prescribing
storage](../design-decisions/0018-reference-authoritative-application-artefacts-without-prescribing-storage.md)
for the modelling decision.

### Specification development

We’re basing the planning application data specification on a clear hierarchy of inputs, so it is both legally robust and practically useful:

1.	Legislation
    * Primarily Article 35 and 40 of the Development Management Procedure Order (DMPO), which set requirements for decision notices and planning-register information.
    * Includes the [work led by Camden to clarify the statutory requirements of the decision notice](https://github.com/digital-land/planning-application-data-specification/issues/330).
  
2.	PS1 and PS2 forms
    * Define MHCLG’s current data requirements.
    * Provide the data used to produce national planning statistics.

3. Community research
    * Builds on the broad engagement phase (interviews and questionnaires).
    * Now continues through deep-dive interviews to test and refine understanding of user needs.

4.	Internal requirements
    * Incorporates priorities from colleagues such as the development policy team.
    * Ensures alignment with departmental processes, policy objectives, and reporting needs.
