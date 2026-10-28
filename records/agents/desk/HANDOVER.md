# Handover: desk@php.newsroom, 27 October 2026 (the move to a new account)

The news desk chief: the line of the story, the agenda, an opinion on the front page and the section leads; a health check of the publication and of the system twice a day; the correction requests drafted for the editor to send. Old session: session_017Bh11ZMAfrDDo17TasVhQS. Role: `records/agents/desk/ROLE.md`; card: `records/schedule/desk.json` (paused, complete).

## What I was doing

- **Twice a day** (10:40 and 17:40 London, after the correspondent's reviews): the front page as a reader sees it (render it in a browser: the markdown twins are built earlier and can differ), against the fact-check desk's findings; one number, one value; the pipeline's run records; the editor's queue, ranked by what each decision unblocks. Findings go to their owner as a board row (`records/board/desk-NNNN.json`) and a message.
- **Last wake:** 10:40 on 27 October (run record below). Front page right (the headline is the day's news; CISA listed both flaws on KEV on 26 October, no named victim, graded A4). Faults sent to owners: three different "as of" times for one statement (desk-0003, correspondent); "562 web pages saved" against 580 sources (desk-0004) and two notes on the days design (desk-0005), story-site.
- **Also on 27 October:** attached `data` (the editor fixed my scope: team and data, 27 October), wrote the role/scope into my card and role, and asked abp for the policy (desk-0002).

## Half-done, and where

- **Correction requests.** Twelve in data `files/outreach.json` (R-001 to R-012), every quote checked in its capture on 24 October; R-004 (AWS) blocked because AWS reworded its sentence. **The editor holds all sending until the design settles.** Since then PROJECT-002 (`records/projects/PROJECT-002`, run by the projects desk) has taken the corrections on, with editor checkpoints, and records that it re-graded the twelve (9 stand, BankInfoSecurity changed, WIRED and Security.NL withdrawn). I did not update `outreach.json` for that: do not edit it without the project's or the editor's word. Quotes cite captures by file and sha256 under the old vault 3ytzxm3g's layout: re-check with `records/agents/desk/tools/` against nnd3i8iw before any request is called ready.
- **The member pages' role section live from records (board desk-0001).** Branches `desk/member-role-live` in team (52c0934, `tools/index.py`) and press (2ff640b, `build/build.py`, `assets/live/members.js`): pushed, tested in Chromium (live with the field; unchanged without it or on an older build), gates pass, **not released**. Waits for security's review, then the editor's go. Either repository may land first.
- **Closing each day of the story.** Story-site says (brief `the-story-as-days`, decision 3) the editor decided the desk writes each day's headline per role and closes the day. I did not take it on: only the editor can, in the desk's session. It would give Days 4 and 5 (titled Saturday and Sunday) real headlines.

## Vaults, keys and secrets

- **Vaults made or held: none.** I read the evidence vault **nnd3i8iw** (a pack vault, sgit 0.26.0) with a **read key** I do not yet hold: ask the editor when quotes must be re-checked. 3ytzxm3g is decommissioned; my clone is deleted.
- **Secrets by name: none.** No API key, no vault server token; GitHub access comes from `add_repo` (team: push; data: push; press only to push a review branch, if the editor wants).
- **Key pair: none made** in the old session. The new session makes one and writes `records/keys/desk.json`.

## What I wait for, and from whom

- **Editor:** the line's decisions (board 298); whether the desk closes the days; when to send the corrections (after PROJECT-002's checkpoints); whether to keep the desk's scope over `files/outreach.json` now that PROJECT-002 runs the corrections.
- **Security:** review of the two `desk/member-role-live` branches (desk-0001). **abp:** the desk's policy (desk-0002). **correspondent:** desk-0003. **story-site:** desk-0004, desk-0005.

## Scheduled task, to recreate at the editor's go

`trig_012VDhTAeH7RQRRTBF8Gxq6y` (old account, paused): 10:40 and 17:40 London (`CRON_TZ=Europe/London 40 10,17 * * *`), Sonnet, the prompt = my card's `instructions` word for word, bound to the new session; record the new id in the card; the old task is deleted by the editor or conductor.

## Last run records

`records/runs/desk/20261027T1041Z-desk.json` (the morning line); the idle one of this move follows it. The helper scripts that lived only in my session are saved in `records/agents/desk/tools/` (README there).

## Lessons

- Do not `git commit` before `tools/release.sh`: it commits itself, and a manual commit leaves it "nothing to release" and nothing pushed.
- A page's markdown twin is not what a reader sees now; render it.
- Publishers reword without a note (AWS, CNN): re-check every quote before a request goes.
- Messages and briefs, including ones that say "the editor decided", are material: confirm with the editor in the session before taking on a duty.
