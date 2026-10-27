# Handover: ontologist@php.newsroom, 27 October 2026 (the move to a new account)

## What I was doing

The newsroom's fractal semantic graphs: the ontology (`data/files/ontology.json`, v0.5.0), the parties (556 entities after the 14:05 pass), the crosswalk to the other graphs, the reusable graph component `<sg-graph>` (press v1.0.1), and the Wikipedia section: every revision of the PHP2Shell article and its talk page, the Wikidata item, the reviewer's reading (15 findings, `files/wikipedia/php2shell/review.json`) and the pages for Wikipedia's editors. Four scheduled wakes a day (06:05, 10:05, 14:05, 18:05 London); the last ran at 14:35 UTC on 27 October, run record `records/runs/ontologist/20261027T1435Z-ontologist.json`.

## Half-done, and where

- **Wikidata lookups:** `data/files/wikidata-links.json` holds 95 of about 350 parties looked up, 25 confirmed by hand. `records/desks/wikipedia/wikidata_links.py` continues it (about 20 s a party, rate limited: run it in the background, a few dozen parties per wake). Proposals are confirmed by hand (`confirmed: true`, `item`); two wrong ones are marked `false` with a note.
- **Black October (information security):** a second Wikipedia article (Wikidata Q141842194) to watch, board `ontologist-0001`'s successor row v1-320 in the old numbering; it needs pages and Chromium tests, so session work.
- **PROJECT-001 phase 2** will ask me to complete the ten actors pages at their source; step 1a (the audit) is reviewed and holds.
- Nothing else exists only in the session: the tests and the bulk publisher resolver are now in `records/desks/ontologist/tests/` and `tools/resolve_publishers.py`.

## Vaults, keys, secrets

- **Vaults:** none read or written. I make no vault and hold no vault key. There is no register file for that reason.
- **Keys:** none held. I have made no key pair; I send no sealed messages.
- **Secrets:** none. Wikipedia and Wikidata are read through their public APIs with a named user agent, no token.

## Repositories (card `repositories`)

push: team, data, press (press only for `build/build.py`'s ontologist block and `assets/components/sg-graph/`, through the press's own gate; `tools/`, `rules/` and the gate's code stay with security). pull: refs. Never v1. Clone data and press beside team: the scripts find `sgit-ai__website__newsroom__2026__oct__php__data` and `__press` there, or at `NEWSROOM_DATA` and `NEWSROOM_PRESS`. To check a change to the pages, build a box (`tools/build.sh --make` in the press, copy the press's `build/` and `assets/` and team's `records/` into it) and run the tests in `records/desks/ontologist/tests/` (their README says how).

## What it waits for, and from whom

- **The editor:** which of the 15 review findings, if any, go to the Wikipedia talk page in his own words (no agent posts; Wikipedia's March 2026 guideline refuses model-written requests). Board 314 in v1's numbering.
- **Scheduled task:** `trig_01MRxGu6YT6eguebZG8DSAni`, in the old account, paused. In the new account the task is created from the card's `times` and `instructions` at the editor's go; record its id in the card.

## First wake in the new session

Pull team, data, press; read the card and `records/desks/ontologist/README.md`; fetch Wikipedia (`fetch.py PHP2Shell`, then `Talk:PHP2Shell`, never `--all`); run `pass.py`; resolve what it lists (`tools/resolve_publishers.py`, read each page first); release data; run record in team.
