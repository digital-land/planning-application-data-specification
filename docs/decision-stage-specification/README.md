# Decision stage specification

The decision stage specification defines the data required to represent the outcome of a planning application, including the decision itself, any conditions, reasons, and related information needed to understand and act on that decision.

### Purpose

The decision stage specification is designed to:

* Standardise how planning decisions are recorded and shared – ensuring all authorities capture and publish decision data in a consistent, machine-readable format.
* Create a single source of truth – allowing decision information to be entered once and reused across registers, reports and systems.
* Replace manual and repetitive tasks – reducing the administrative burden on local planning authorities by making activities such as completing PS1 and PS2 returns automatable and, in time, real-time.
* Improve transparency and interoperability – enabling decision data to be linked across the wider planning process (applications, conditions, appeals, completions) and compared across authorities.
* Support better monitoring and policymaking – providing accurate, structured data for national statistics, housing delivery tracking, and local performance insights.
* Free up planners’ time – allowing officers to focus more on professional planning work rather than administrative data entry and reporting.

### Research

Because there are no existing de facto standards for planning decisions, unlike the submission stage, where the current application forms provided a clear starting point, we’ve had to begin the decision stage work with foundational research.

Our aim is to understand what information is actually needed, by whom, and for what purpose before defining any data structure. We’ve started by gathering evidence through broad engagement with the community (interviews and questionnaires) and are now carrying out deep-dive research sessions to explore specific user needs in more detail.

This approach follows the “start small” principle: we’ll begin with a minimal, evidence-based core and only add parts and fields once there is a clear and validated need.


### Specification development

We’re basing the decision data specification on a clear hierarchy of inputs to ensure it is both legally robust and practically useful:

1.	Legislation
    * Primarily Article 35 and 40 of the Development Management Procedure Order (DMPO), which sets the legal basis for what must appear on the decision notice and planning register.
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
