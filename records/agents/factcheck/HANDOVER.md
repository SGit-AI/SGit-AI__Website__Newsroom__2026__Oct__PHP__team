# Handover: factcheck@php.newsroom (the fact-check desk), 27 October 2026

Written in the old account's session, for the move (records/briefs/2026-10-27__brief__moving-to-a-new-account.md). No key or token is named here.

## What the desk was doing

Four wakes a day (08:52, 12:52, 16:52, 20:52 London), each one: take in team and data, read the inbox, pull the evidence vault, run `fc.py changed` (re-grade every new or changed claim against its captures, quotes found verbatim with sha256), `fc.py check` (0 failures) and `fc.py drift`, check KEV, NVD and php.net, re-fetch W3Techs on the 08:52 wake, write `Run-N.json` and a run record, export `files/factcheck.json` into data, release data then team. The grade model, the tickets and the contradictions are in `records/desks/factcheck/` (README.md is the runbook; `assessments.json`, `contradictions.json`, `investigations/php-share/`, `runs/`, `regrades/`, the Issues-FS tracker in `.issues/`).

## State at the pause

- Latest run: Run-13, run record `20261027T1256Z-factcheck`; data v0.1.77 carries the 13th run. 70 assessments, 12 contradictions.
- Done today: CISA's KEV listing of both CVEs (26 October) is graded in (Evidence-19; `cisa-none` superseded; `kev-precedent` A2; K-002 gains CISA). PROJECT-002 step 2 is done: the twelve correction rows re-graded after the listing (9 stand, row 3 changed, rows 2 and 12 withdrawn), in `records/desks/factcheck/regrades/project-002-twelve-rows.json`.
- Half-done: nothing unpushed. Open and not mine to close: K-010 (original embargo time), K-011, Finding-128 (Wersm's unbacked "confirmed compromises"), Finding-127 and the board rows 183, 224, 233 in the old numbering.
- `fc.py` reads the data repository's `files/` (beside the team clone, or `FC_DATA`) and writes `files/factcheck.json` there.

## Vaults

- `nnd3i8iw`, the evidence vault (pack, read key): the desk reads it. Clone it outside every repository: `sgit clone - <dir>` with the key on stdin from a mode-600 file; needs sgit-ai 0.26.0 or later. The key comes from the editor, sealed to the new key.
- `hsmfer5w`, the desk's own pack copy of the old evidence vault (vault key, made 26 October, sealed to the root and to the registry key): stale at 94352a55fbaa and no longer read. A new session does not need it.
- `3ytzxm3g`: retired; marked so in the register.

## Secrets needed (by name)

- The vault server access token (`SG_SEND_ACCESS_TOKEN` in the session environment), for `sgit pull` and `clone`.
- Nothing else: KEV, NVD, php.net and W3Techs are public.

## Waits for

- The editor: the new session's key enrolment; the read key for `nnd3i8iw` sealed to it; his go to create the scheduled task.
- The journalist: review of the twelve rows (PROJECT-002 step 2). The liaison: the page and requests on top of them.
- The old scheduled task was `trig_01NJcbVPAcxf5w7N298HCbRE` (paused); the new one is made from the card's `times` and `instructions`, word for word, and its id recorded in the card.

## Gaps closed in the last turn

The card's `repositories` now names `never` (v1) and its model in words (Sonnet). The register lists every vault and key held.
