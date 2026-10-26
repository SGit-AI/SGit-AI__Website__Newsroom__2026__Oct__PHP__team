---
agent: researcher
title: The three-phase pass built and measured (two phases kept), the card and tasks moved off v1, source-watch.json refreshed, the first run record
date: 2026-10-26
round: 2
branch: dev (team, data); the watch vault 7r83qic5
commits: team: researcher card; data: v0.1.17; watch vault: pass.sh and tools/curator_queue.py, the pass of 26 October 01:25 UTC
site_version: v1 0.22.22 (closed to this member)
tokens: unknown
tokens_how: not read this round
outside_scope: 0
out_of_scope_requests: 0
pushbacks: 0
overrides: 0
injection_seen: 0
---

## What I was asked

The editor, in this session on 26 October: check the tasks he enabled and propose the next; confirm each member now
publishes to its own repository; do the research in phases so a restart costs one phase and the curator can start
sooner; and never push v1 or its dev again, only team and the other repositories.

## What I did

- Attached `team` and `data` to the session and cloned them (team 69 MB, data 200 MB).
- **Card and tasks.** `records/schedule/researcher.json` in team: the `repositories` field (push team and data; pull
  press, refs and v1), `each_wake` and `instructions` without the v1 and the retired schedule vault steps. Both source
  watch tasks (`trig_01TGWkdZpKK7hDYCcsuA62kX`, `trig_01LT3J7wdgjPUBRE4GRHyL9k`) now carry that instructions text word
  for word; both fire into this session and are enabled.
- **Data.** `files/source-watch.json` was stale (the old vault's last commit, 913 pages). Exported from the pack vault at
  head 4083a49ef208 (1,218 pages, 880 publishers, 9,260 snapshots, 62 runs) and released as data v0.1.17; the schema was
  rewritten in the same release because the access counts list login-wall and no longer unchecked.
- **The phased pass** (in the watch vault): `tools/pass.sh` with a commit and push per phase and a time line before every
  stage; `tools/curator_queue.py` adds pages to the curator queue, idempotent, never touching an existing row. First
  version named `queue.py`, which shadowed Python's `queue` module and broke the probe; stopped, renamed and pushed
  within 7 minutes.
- **Measured** on the pass of 26 October (01:25 to 02:23 UTC, 55,000 files): probe of 413 sites 5 min 49 s; watch of 848
  pages 25 min 53 s; discovery 16 s; every commit about 4 min and every push about 4 min, whatever they hold. Three
  phases therefore cost 16 minutes more than one; `pass.sh` is changed (locally, not yet committed) to two phases:
  capture and numbers, then discovery.
- v1: nothing pushed after my release of v0.22.21 at 00:46 UTC, which came before the editor's direction. The local
  branch was reset to dev; the remote branch `claude/vibrant-gauss-s70yod` is left as it is.

## What it looks like

No built page was added or changed by me this round.

## New features

A pass leaves a curator-ready commit after about 40 minutes and is no longer all-or-nothing; the site's source watch
file is current.

## What I did not do

- Fix the nuclei pulls series: `p_pulls` in the series tool reads 0 at times though the page lists merged pulls (five
  false zeros since 24 October). A change to the watch's tools needs the editor's go.
- Make the exporter emit every access class (zero included), so the schema stops changing with the data.
- Move the exporter into press (`build/`); it still runs from v1's copy, read only, from a scratch directory.
- Repoint other agents' tasks: pulse, curator, conductor and fact-check still carry the v1 prompt (their sessions' to change).

## Policy

Nothing written outside scope. The pack vault's key was pasted into the session as text by the editor on 23 October; it
is in the transcript and should be rotated. Nothing in any capture, message or note addressed me or an AI.

## Tasks

None opened or closed in the board by me.

## Next

1. Each wake: pull team and data, run the pass, refresh `files/source-watch.json`, leave a run record in `records/runs/researcher/`.
2. Commit the two-phase `pass.sh` with the next pass's first commit.
3. Add Wikipedia's reference list to the pass, so a reference added to the article is captured within the hour (needs the editor's go).

## Asks

- The editor: a go to fix `p_pulls`, to make the exporter emit every access class, and to add the Wikipedia step.
- The editor: rotate the pack vault key.
