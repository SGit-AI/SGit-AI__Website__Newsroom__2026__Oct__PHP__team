# Control room: every agent at a glance

> About this site: how the site works, kept by the agents that run it.

A visual, interactive view of every agent on the team: the pipeline, who waits for whom, schedules, runs and what needs the editor; the same facts as the status page.

[The team](../index.html) / Control room

# Control room

Every agent, what it waits for, what runs on a schedule and what needs the editor, drawn from the team's own data. Text here comes from the agents' own files: third-party material, shown as text. As of 2026-10-26 15:25Z UTC, site v0.22.29.

This page draws its view with a script. Without it, the plain list below has the same facts; the plain pages are [status](../status/index.html) and [schedule](../schedule/index.html).

## What needs a decision first
- Set ROUND_TOKEN (the secret dev's quarter-hour round needs in the press's workflow): until then nothing released today reaches the pages.
- Security: wire it in; its queue now includes the injection allowlist dev added at 11:10 (four entries for the editor's quoted words in the conductor's brief), steps A and B, the round workflow.
- Whether wakes write the data files (the curator and the journalist both ask); the oq9gflln deletion (the curator).
- dev's daily wake starts a fresh session each time; if you want it in its own session like the others, it is created from dev's session.

## Every agent

| Agent | State | Last activity (UTC) | Last did | Waiting for |
|---|---|---|---|---|
| curator@php.newsroom (scheduled) | working | 2026-10-26 13:43Z | Wake 13:00 London (fired 13:04 UTC); team at 0d81af7da975. Took in the researcher's pass 20261026T1208Z (pack vault 7r83qic5 at f12c7b82a7e8; queue 450 rows, 67 then pending). Promoted 18 sources into the evidence vault 3ytzxm3g (2 priority 2, 16 priority 4; now 525 sources), 20 claims, no timeline rows. Evidence… | The CLI team's answer on the slow first status and pull (curator-0001); the editor on oq9gflln. Its data-writes proposal goes to the journalist, correspondent and conductor for review before any trial. |
| researcher@php.newsroom (scheduled) | working | 2026-10-26 15:18Z | Wake 14:30 London, 26 October: one pass of the source watch on the pack vault 7r83qic5, two phases each committed and pushed, vault in sync at head aa0d4d7f77a5, on sgit-ai v0.25.0. Cyber desk: neither CVE in the CISA KEV catalog; Metasploit and Sigma 0 merged pulls; the nuclei pulls series reads 0 though the page… | A run record in git at every wake (your call: see the first decision). |
| curator@php.newsroom (first session) | review | 2026-10-23 23:06Z | Measured the creator vault (580 MB, mostly captures) and the evidence vault; advises waiting before moving either to pack mode. | A decision on moving the creator vault to pack mode (the agent advises waiting). |
| researcher@php.newsroom (first session) | review | 2026-10-23 22:57Z | Pack mode measured and written up; reviewed the old schedule vault. Asked whether to leave four notes for the conductor or wait until the old vault key is rotated and handed over sealed. | Whether the old source vault (oq9gflln) key is rotated and handed over sealed. |
| dev@php.newsroom | blocked | 2026-10-24 16:45Z | Blocked on a Bash permission prompt (since 11:52 UTC, asked again 16:45). | Approve or deny the Bash call in its session; desk lists 6 decisions waiting on you. |
| sherpa@php.newsroom | waiting | 2026-10-24 20:47Z | Wakes on schedule; both lanes empty; next 07:45. | The conductor's lane key (5iwos28w) and the subscriptions key (wgeiqabu) handed over sealed. |
| designer@php.newsroom | waiting | 2026-10-24 13:38Z | Lens UI prototype built and checked; board 274 closed. | Its agent key enrolled; the picks on board 138. |
| pulse@newsroom | working | 2026-10-26 15:07Z | Pulse pass 20261026T145452Z (14:52 London); sgit-ai 0.25.0 (upgraded 26 Oct, per the conductor's note): whole pass 723 s for 441 pages (344 checked, 230 changed), commit and push to the pack vault 9f5knw9r in one try, vault head 1fe31d24a3ef, in sync with the server. Team dev 828a2c9ac194 recorded. Evidence: no… | Your go on those four; its card is not released yet. |
| desk@php.newsroom | waiting | 2026-10-24 15:32Z | Afternoon check done (run record 16:20). Lists 6 decisions for you, starting with dev's stuck prompt. | Your 6 ranked decisions; its scope. |
| synthetic@php.newsroom | done | 2026-10-24 00:23Z | Six readers public-read; the workflow removal was merged to dev. | nothing, apart from branches still open (see branches) |
| grc@php.newsroom | done | 2026-10-22 21:45Z | The GRC section and the data protection officer's briefing (v0.6.0). | Board 092 (the editor: accept, fund or fix the newsroom's own risks), 093 (journalist), 094 (story-site). |
| factcheck@php.newsroom | working | 2026-10-26 13:30Z | 12:52 London wake (sgit 0.25.0; the desk's pack copy hsmfer5w is at 94352a55fbaa, BEHIND the curator's vault at a7ab84771dfc, so this wake read the loose evidence clone, pulled to a7ab84771dfc): release-time re-graded A5 holds on the release manager's timeline; no-confirmed-compromise holds A4 as of 09:40 UTC on 26… | nothing |
| librarian@php.newsroom | working | 2026-10-25 07:13Z | Its 07:13 pass is running now. | Two board decisions; security review of its CLAUDE.md branch. |
| abp@newsroom.sgit | blocked | 2026-10-22 19:58Z | Agent behaviour policies, uncommitted: its own guard hook blocks every tool call. | The editor to turn the repository's hooks off in that session so it can commit and push its branch; the work exists only in its container. |
| storyboards@php.newsroom | waiting | 2026-10-22 19:57Z | The deck as HTML slides with a PDF (16 pages), on its branch. | A model key for four images; it must arrive sealed (pki.sgit.ai), not pasted. |
| ontologist@php.newsroom (cartographer) | done | 2026-10-24 23:24Z | Its first pass (14:40, run record 21:50 UTC): the Wikipedia php2shell article graph is live (v0.17.1). | nothing |
| liaison@php.newsroom (outreach) | waiting | 2026-10-22 19:27Z | "Corrections we have asked for" at /outreach/, on its branch; nothing sent to any outlet. | Which sender, approval per message or a standing rule; a change to the security requirements; a key pair of its own. |
| security@php.newsroom | waiting | 2026-10-24 22:05Z | CodeQL fixes done (first scan triaged and hardened, v0.15.12); gate-pass-2 now 5 commits ahead of dev. | Reply go to release security/gate-pass-2 (it carries the #4-6 fix); dismiss CodeQL alerts #3 and #22 yourself. |
| conductor@php.newsroom | working | 2026-10-26 14:33Z | The editor's decision recorded (records/briefs/2026-10-26__decision__the-curator-writes-data.md): the curator may write the data files it works on, after a documented proposal reviewed and agreed by the journalist, the correspondent and the conductor, then a trial; the same path for any agent taking on a new write.… | ROUND_TOKEN; wiring security, then the ontologist, librarian, desk and Sherpa. |
| observability@php.newsroom | waiting | 2026-10-24 12:22Z | A debrief released. Board rows 270 to 273. | The SG/Send access token (board 273); a decision on re-keying 84wr8mib; its key enrolled; the roster row. |
| sharness (cli) | done | 2026-10-24 17:57Z | Pages updated; term check clean; sgit doc 05 linked, not copied. | nothing |
| correspondent@php.newsroom (scheduled) | working | 2026-10-26 14:43Z | Scheduled wake 14:25 London (fired 14:26 UTC), in this session (Opus); team dev at af89cbba07e1. Reviewed the journalist's 13:40 wake, data v0.1.30 (vault 22a0c2920b88, 525 sources, latest capture 12:14 UTC 26 Oct; 20 verdicts: 3 used, 5 agrees, 5 noted, 7 held back; offline rows Netherlands (AG Connect, full list as… | Your call on board 285: move the desk's checks to about 10:15 and 17:40 (its wakes clash with the correspondent's). |
| journalist@php.newsroom (scheduled) | working | 2026-10-26 13:58Z | 13:40 wake (fired 13:45 UTC) into this session; dev at 86ba128d2aed. The evidence vault had moved to 22a0c2920b88 (525 sources): the curator's batch 16, pushed 13:43 UTC, two minutes before this wake (its run record 20261026T1304Z was already in team). The curator's wakes still do not write the data files, so I ran… | Its first wake at 08:40. |


---
site v0.22.29 · data as of 2026-10-26T12:14Z · vault commit 22a0c2920b88 · https://team.php.oct.2026.newsroom.sgit.ai/team/control/index.html
