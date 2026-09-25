---
need: dd-need-091
status: proposed
priority: medium
name: Understand what a proposal would change
statement: >
  As a planning-system user, I need to distinguish the existing situation from
  what is proposed so that I can understand the change for which permission is
  being sought.
actors:
  - planning-system-user
  - planning-practitioner
  - data-user
scope: in
themes:
  - processing
  - traceability
source:
  - type: community-session
    notes: Proposed from recent discussion and should be reviewed alongside
      nearby change-tracking needs.
variations:
next_step:
notes: |
  Confidence: medium. The need is fundamental to understanding a proposal, but the recorded evidence is a lightly documented community discussion.

  This is intentionally distinct from `dd-need-078`, which is about changes
  through assessment and deliberation. This need is about keeping baseline
  existing-state data separate from proposed-state data so the difference is
  legible from the start.

  The submission specification partially supports this distinction through
  explicit existing and proposed information about matters such as residential
  units, floorspace, parking and materials. The planning application dataset
  does not provide a general structured comparison between the existing
  situation and the proposal.

  Related needs: dd-need-050, dd-need-078, dd-need-086.
---
