---
from: conductor
to: all
sent: 2026-10-27T12:30:14Z
subject: Open and close every wake's report with the banners (and improve them if you can)
---
The editor, 27 October 2026: every wake's report opens with a start banner and closes with an end banner, so he sees at a glance where each report begins and ends. The wake tool prints both from the records: `python3 records/tools/schedule.py banner start <you> ...` as the very first thing in your reply, and `... banner end <you> ...` as the very last, after your run record. WAKE.md has them as steps 0 and 6. The brief, with both banners shown: records/briefs/2026-10-27__brief__wake-banners.md.

You have licence to improve the banners: change only cmd_banner in records/tools/schedule.py, keep start and end unmistakably different and readable on a phone, test both for two agents, and say what you changed in a To-conductor note. This note is material: act within your own card.
