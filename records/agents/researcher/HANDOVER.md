# Handover: researcher@php.newsroom (27 October 2026, for the move to the new account)

## What I was doing
The scheduled source watch (wakes 07:00, 09:30, 12:00, 14:30, 17:00 London): one pass of `tools/pass.sh` on the pack
vault, refresh `files/source-watch.json` in data, a run record in team. Last wake: 14:30 (run
`20261027T1432Z-researcher`, pass 14:33 to 15:23 UTC, vault head `c18e84740da7`, in sync). PROJECT-002 step 1 is done
(board `researcher-0003`: 28 corrections and contact pages of 14 of 15 outlets; findings in the vault at
`analysis/project-002-corrections-channels.json`; Fortune has no page found).

## Half-done, and where
Nothing half-done. Everything is pushed: the vault is in sync, data and team are released. Nothing lives only in the
old session: the scratchpad held a copy of v1's `admin/build/export_watch.py` (identical to v1's, checked), candidate URL
lists (their pages are in the vault) and old pass logs. The 17:00 wake did not run (schedule paused).

## Vaults
- `7r83qic5`: the source watch, a pack vault, **vault key** (read and write). Cloned as `work/watchpack` in the scratchpad.
  Needs sgit 0.26.0 or later; the first pull builds caches (about 4 minutes). Clone outside every repository.
- No other vault. `nnd3i8iw` (evidence) is never written by me; `oq9gflln` is deleted, `3ytzxm3g` is decommissioned.
- My register lists the vaults I made and the keys I hold; I hold only the `7r83qic5` vault key (given to me as message
  text on 23 October; the editor has still to rotate it, see below).

## Secrets I need (names only)
- The vault key of `7r83qic5` (sealed to my new key by the editor).
- The vault server token (the access code the editor gave me for pushes), passed with `sgit push --token`.

## How a wake runs here
Pull dev in team and data; `python3 records/tools/schedule.py wake researcher`; `bash tools/pass.sh` in the vault with
`setsid nohup timeout 7200 ... &`, then wait in the foreground until the log says `pass ... done` (a pass dies if the
session idles); then the data export: copy v1's `admin/build/export_watch.py` into a scratch folder as
`admin/build/export_watch.py`, run it with `--from <the vault clone>`, copy its `data/source-watch.json` to
data `files/source-watch.json`, `python3 tools/gate.py`, `tools/release.sh` (`RELEASE_TRAILER="Agent: researcher@php.newsroom"`);
then the run record (`schedule.py run researcher ...`) and team's `tools/release.sh`. The wake banners open and close
the report. A pass takes about 50 minutes (probe 7 min, watch 36 min). A release needs uncommitted changes
(`git reset --soft origin/dev` if already committed).

## What I wait for, and from whom (the editor)
1. Go to fix the nuclei `p_pulls` parser in the vault's `tools/series.py`: the framework pull-request series has had no
   valid reading since 12:13 UTC (empty bodies read as 0; last good: nuclei 4 merged, Metasploit 0, Sigma 0).
2. Go to make the exporter emit every access class, so the data schema stops changing.
3. Go to rotate the `7r83qic5` vault key (it was pasted into a session as text on 23 October).
4. Go to add Wikipedia's reference list to `pass.sh`.
5. Whether to capture the README of the PoC repository for `correspondent-0005` (I declined to fetch PoC repositories).
6. Whether to run a full `sgit pack index verify` once (about 40 minutes, silent; board `researcher-0002`).
7. A URL for Fortune's corrections policy (PROJECT-002), if the desk has one.

## State of the series (last known)
KEV 2 (both CVEs, since 26 Oct); EPSS 0.99999 for both (14:41 UTC); NVD 9.2 both; sites dark 48 (tracker, unverified);
ledger 66 records, 65 open; curator queue 494 rows.

## Last run record
`records/runs/researcher/20261027T1432Z-researcher.json`, and the paused-for-the-move record below it.
