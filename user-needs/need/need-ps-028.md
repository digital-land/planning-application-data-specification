---
need: need-ps-028
status: proposed
priority: high
name: Count applications awaiting a decision at a given date
statement: >
  As an analyst, I need to know how many applications were awaiting a decision at a given date, including applications received in earlier periods, so that I can report the outstanding caseload consistently over time.
actors:
  - analyst
scope: in
themes:
  - statistics
  - monitoring
source:
  - type: other
    notes: >
      Research with MHCLG stats, August 2026, identifies a comprehensive count of applications on hand at a particular date as a key question and highlights the risk that older applications awaiting decisions could be missing from open data. It also highlights reporting gaps that can arise when new longitudinal data requirements are introduced without addressing existing records.
variations:
next_step: review
notes: >
  Confirm with statistics colleagues the meaning of applications on hand, the relevant dates and treatment of withdrawals, invalid applications and other states before mapping the need to the specification.
  This overlaps with need-ps-001, which supports operational workload management. It is distinct because consistent statistical snapshots require coverage of applications received before the reporting period and their state at the chosen date, rather than only current status or counts received and decided during a period. The analyst user group follows documentation/user-groups.md; central government statistics is the evidenced context.
---
