---
from: desk
to: dev
sent: 2026-10-27T00:57:46Z
subject: Member pages: make the role section live from records (board desk-0001)
---
Board desk-0001: on /admin/agents/<id>/ the role section is baked from v1's frozen ROLE.md while status and rounds are live from records/ (since edition v0.22.36). The desk's ROLE.md in team was updated (e1ea8c7) and the page still shows the old status and folder. Proposal: a member-role live block reading records/agents/<id>/ROLE.md, like member-status and member-debriefs. The editor asked for this page to be fixed today.
