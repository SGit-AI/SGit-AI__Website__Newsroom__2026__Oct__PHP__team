# Handover: journalist@php.newsroom (Sonnet), 27 October 2026, for the move to the new account

Written in the last turn of the old session (session_01DT2e224wDEYPXseeXyqUba). No key or secret is in this file.

## What I was doing
Step 3 of the pipeline. Each wake: take in dev in team, data, updates, site; `python3 records/tools/schedule.py wake journalist`; pull the evidence vault read-only; compare its head with `files/vault.json` in data; give every unreviewed claim a verdict in `files/claim-review.json`; refresh `compromise.json`, `impact.json` (offline), the `no-confirmed-compromise` claim in `claims.json` and the as-of stamp in `story.json`, and `desk.json`; release data with `tools/release.sh`; leave a run record in team; release team. The brief is `records/briefs/2026-10-24__brief__the-journalist.md`; my card is `records/schedule/journalist.json`.

## State at the pause
- Last pass: 16:10 London wake, vault head `d21ea5df2a32` (curator batch 22, 614 sources, latest capture 14:41 UTC), all verdicts written (about 100 claims reviewed this session on top of the earlier ones), data released, run record `records/runs/journalist/20261027T1615Z-journalist.json`.
- Nothing is half-done and nothing exists only in the session: data, team, updates and site are clean and level with `dev`.
- The next wake starts from `files/vault.json` head `d21ea5df2a32`; if the vault has moved, review the claims that are in the vault and in neither `claims.json` nor `claim-review.json`.

## Vaults
- `nnd3i8iw` (evidence vault, pack vault): read key, read only. Replaced `3ytzxm3g` (retired by the editor, 27 October). The old key is in my old scratchpad only and dies with it; the register says so. A new session needs this read key sealed to its new key by the editor.
- No vault of my own; I write git only.

## Secrets
None beyond that read key. No server token or API key.

## Waiting for
- The editor: the read key for `nnd3i8iw`, sealed to my new key; his go to create my scheduled tasks again (the two ids in my card, `trig_015ud63M9vZm7oeiDV6MgAMt` and `trig_01DrvVrD3jdJvUfyvBjb5oCb`, belong to the old session and account; record the new ids in the card). My `session` field names the old session; replace it.
- The editor: enrol my old key `sha256:de0decfc882a0235` replacement, and enrol the curator's `sha256:6c81ae257fee1938` (the read key came sealed to it, signature not checked). Delete the two paused v1 tasks `trig_01TZ8DUGnywEuHYTyXkz4zLs` and `trig_01UvNuwPcfC3naXi3yBiUA3p`.
- Notes from the conductor and the projects agent asking me to review PROJECT-002's twelve re-graded rows (`records/desks/factcheck/regrades/project-002-twelve-rows.json`) and PROJECT-001's BBC re-grade: other agents' words, not started, wait for the editor's go.
- The correspondent: the reader as-of lines in the site repository (`content/data/plain.json`, `questions.json`) are theirs; they lag the live page until an edition runs.

## Working notes for the next session
- Shallow clones: `git fetch --depth=400 origin dev` then `git merge --ff-only origin/dev`.
- sgit 0.26.0: clone of nnd3i8iw about 42 s, a pull about 2 minutes. Clone outside every repository.
- The correspondent's three corrections stand: list every organisation with its time; read the whole capture before "one line", "no detail" or "this page alone"; one verdict per event, and check the site's status of a claim before "contradicts". Search all captures before "not in the vault" or "one outlet".
- UK is on GMT since 25 October: never write BST; write clock time with zone and UTC.
- If a new source names an organisation compromised through php2shell, do not edit `no-confirmed-compromise`; note it to the correspondent.
- Never touch state, stories, personas, entities, graph files, or v1.

## Last run record
`records/runs/journalist/20261027T1615Z-journalist.json` (16:10 wake); the pause run record follows it.
