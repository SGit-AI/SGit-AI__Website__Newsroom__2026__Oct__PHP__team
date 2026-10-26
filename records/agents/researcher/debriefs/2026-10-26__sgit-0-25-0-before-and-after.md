---
agent: researcher
title: sgit-ai 0.24.0 against 0.25.0 on the source watch vault, measured before and after
date: 2026-10-26
round: 2
branch: dev (team)
commits: the run records of the 07:00 and 09:30 wakes of 26 October
site_version: not applicable
tokens: unknown
tokens_how: not read
outside_scope: 0
out_of_scope_requests: 0
pushbacks: 0
overrides: 0
injection_seen: 0
---

## What I was asked

The editor, 26 October: report any slowness found in sgit; then, after 0.25.0: put the before and after numbers in the
run notes.

## What I measured

The vault is the source watch, 7r83qic5, a pack vault: 79,465 files in the working tree (2.7 GB), 38,474 tree objects
(one per folder), 176,093 loose objects in the local store (3.5 GB), 14 or more commit packs on the server. Same clone,
same machine, nothing else running. 0.24.0 was measured on 26 October between 01:25 and 08:13 UTC, 0.25.0 at 07:50
UTC (the commands) and in the pass of 09:34 UTC.

| | 0.24.0 | 0.25.0 |
| --- | --- | --- |
| `status` | 155 s (profiled) | 11 s the first time (builds the scan cache), 3.3 s after |
| `history log` | more than 8 min | 9 s |
| `pull` (up to date) | not timed | 2.3 s |
| data export (reads `history log`) | about 9 min | 34 s |
| pass phase 1, commit (12,800 to 12,970 new objects) | 4 min 24 s, 4 min 12 s, 4 min 11 s, 12 min 38 s | **25 s** |
| pass phase 1, push | 4 min 22 s, 3 min 56 s, 4 min 6 s, 4 min 16 s | **67 s** |
| pass phase 2, commit (about 60 objects) | 4 min 43 s | 4 s |
| pass phase 2, push | 3 min 46 s | 16 s |
| whole pass | 57 min and 59 min | **35 min** |

Not sgit, and unchanged: the probe of 413 sites (5 min 44 s to 6 min 4 s), the watch of about 850 pages (25 min 53 s to
27 min 25 s) and discovery (under 20 s). They are 33 of the 35 minutes.

## Where 0.24.0 spent its time (cProfile of one `status`, 155 s)

85 percent was rebuilding the flat list of tracked paths from the 38,474 tree objects, through `Type_Safe.from_json`
(about 3 ms a tree), done twice per command; `push` began with a full `status`. The report is at
`/tmp/claude-0/-home-user-SGit-AI--Website--Newsroom--2026--Oct--PHP/b6197591-7c1d-576a-9bde-73a5578df47e/scratchpad/sgit-slowness-report.md`
in the session's scratchpad, and was sent to the editor. 0.25.0 is the fix the CLI team made from it.

## What it changes

A commit and a push cost what the change costs, not the size of the vault. Phases are cheap now (about 20 seconds
each), so the plan of three phases, one commit each, can come back without costing 16 minutes. Nothing was lost on the
upgrade: the vault stayed in sync with nothing to commit.

## What I did not do

Time a one-file commit or a small push in isolation on 0.25.0 (the release notes give under 5 s and 10 to 18 s); the
phase 2 numbers above (4 s and 16 s) are the nearest measurement.
