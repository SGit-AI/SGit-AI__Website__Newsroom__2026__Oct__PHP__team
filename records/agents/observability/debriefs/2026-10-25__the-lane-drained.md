---
agent: observability
title: The telemetry lane drained (150 events), what was in it, and a drainer that pushes before it marks
date: 2026-10-25
round: 3
branch: claude/wonderful-allen-vu7tzg
commits: see status.json
site_version: when the round ended, see the release
tokens: unknown
tokens_how: the session does not show a token count
outside_scope: 0
out_of_scope_requests: 0
pushbacks: 0
overrides: 0
injection_seen: 0
---

## What I was asked

The editor, in this session, on 25 October 2026: "drain the vault, the append lane, and see what's in there."

## What I did

- Pulled the telemetry vault (84wr8mib): someone had drained earlier that day (280 events, `drain/2026-10-25.jsonl`); 150 more were waiting in the lane, 11:33 to 20:28 UTC.
- Wrote `admin/observability/drain.py`: the telemetry application's drain, from the command line, in the same order (list, fetch, open with the drain key kept in the vault, append, reports, commit and push, and only then mark processed) and with the same row bytes (checked: an existing row reproduces byte for byte). The lane's enum key is derived from the vault key; the access token comes from the environment; nothing secret is printed. dev's `telemetry_drain.py` is untouched: it needs a passphrase file this session does not have, and it marks events processed before the vault is pushed.
- A dry run first (opened all 150, wrote nothing), then the drain: 150 readable, 0 undecryptable, 0 already drained; pushed as `drain 2026-10-25: 150 event(s)`; marked processed; the lane is empty. The vault now holds 2,083 events from 674 sessions.
- Read what came in, as untrusted claims, in aggregate: 62 sessions (59 new). Readers: 26 views in 18 sessions, mostly from Great Britain, from Google, LinkedIn and kode24.no or this site itself; /sources/calif-php2shell/ the most read; 3 of 18 read more than one page. Synthetic: 68 views in 40 sessions, all but one declaring webdriver. Crawlers: 54 views in 2 sessions (Googlebot from Mountain View, 53 of them in one session). Power users: 2 views, declared. No value addressed to a model, no hidden characters, no path off the site.
- One finding, board 330 for dev: 39 of the 150 (and 439 of the vault's 2,084, 21%) were sent from agents' local test servers (localhost and 127.0.0.1), because `assets/telemetry.js` sends from any host. All declared webdriver, so no reader count is wrong; but they use up the lane's cap.

## What it looks like

No page a reader sees changed this round, so there is no screenshot: the work is a vault commit and a tool.

## New features

Whoever holds the telemetry vault's key can drain it from the command line with `admin/observability/drain.py`, safely in the order the application uses.

## What I did not do

- The public stats vault (0cfkdcvh) and `data/telemetry-report.json` were not updated: the first needs a key I do not hold, the second is dev's file.
- No fix to `assets/telemetry.js`: dev's file (board 272, 330).

## Policy

No write outside scope. The security self-check: the tool prints no key or token; it reads the access token from the environment and passes it to sgit only; the rows it opens stay in the vault and the session's scratch directory.

## Tasks

Opened 330 (dev: telemetry from local test servers). 270 and 272 stay open.

## Next

1. A proposed card for a scheduled lane check and drain with this tool, for the editor's go.
2. Count the events the cap refuses, with dev.
