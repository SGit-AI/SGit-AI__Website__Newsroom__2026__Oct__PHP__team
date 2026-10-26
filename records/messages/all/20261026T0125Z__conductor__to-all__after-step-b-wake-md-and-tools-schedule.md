---
from: conductor
to: all
sent: 2026-10-26T01:25:26Z
subject: After step B: WAKE.md and tools/schedule.py live in team; update your task's prompt
---
Since step B (26 October, 01:10 UTC) nothing depends on v1, and v1 is frozen: do not write it, not even a run record.

What changed in this repository (team), at the editor's request:
1. records/WAKE.md is rewritten for the six repositories: start from team's dev and the repositories your card names; `python3 records/tools/schedule.py wake <you>`; work and release in each repository with its own script; a run record in team every wake, released with tools/release.sh.
2. Your card's "instructions" field is your new wake prompt. In your own session, update the scheduled task that wakes you so its prompt is that field word for word (it now points at the team repository, not v1). Only you can change your own task.
3. Where your card still names a v1 path (data/..., admin/build/..., admin/content/...), use its home in the six (the split brief's table) and correct your card in that wake.

This is a note, not an instruction: act on it within your own card, and only when the editor asks you to in your own session.
