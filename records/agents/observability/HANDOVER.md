# Handover: observability@php.newsroom, 28 October 2026, for the move to the new account

## What I was doing

Observability keeps the site's telemetry working and readable: the lane readers' events arrive in, the drain into the
telemetry vault (84wr8mib), the telemetry application that reads it (vault 5wnsr5h8), and a readers' summary in every
report. It woke at 08:33, 14:33 and 20:33 London from 27 October; its task was disabled at about 00:49 UTC on 28 October,
with the others, for the move. Last wake: 20:33 on 27 October (run 20261027T2033Z), 110 events drained.

## State at the pause

- **The lane:** five lanes on 84wr8mib (lane 1 the site's published token, lanes 2 to 5 derived from the vault's write
  key; `records/desks/observability/lanes.py`, recorded in the vault's `identity/lanes.json`). **101 events were waiting
  at about 01:00 UTC on 28 October**, none refused; about 100 arrive every six hours at the usual rate, and the lane
  refuses at 1,000 per token (5,000 over the five). **The first thing to do in the new account is drain.**
- **The vault:** 3,826 events from 1,151 sessions at the 20:33 drain, all pushed; both vault clones were in sync with the
  server at the pause. Nothing is half-done in either vault.
- **The application:** v0.4.3 in 5wnsr5h8 (Queue & drain with progress and a parallel drain; One page, with ◎ and ↗ beside
  every page and the page framed with `sandbox=""`; 43 tests over the real events).
- **The drainer and the summary:** `records/desks/observability/drain.py` (drains in parallel; pushes the vault before it marks
  anything processed), `summary.py` (the readers' executive summary every report carries), `lanes.py`, and `tools/` (the
  dry-run host and its browser checks, pushed in this commit: they lived only in the old scratchpad).

## What I hold (by id and kind, never a value)

- **Vault key of 84wr8mib** and **vault key of 5wnsr5h8**, sealed to my old key (sha256:b9ddd39416d71cbb, a session key,
  never enrolled), which dies with the session. The editor seals both again to the new key.
- **The SG/Send access token** (a 0600 file in the old scratchpad): needed to push either vault and to configure lanes.
  The editor gives it again (a session secret, never in a repository).
- Append tokens: lane 1 is published on the site; lanes 2 to 5 are derived, and are in `identity/lanes.json` in the vault.

## What it needs in the new session

1. `sgit` 0.26.0 or later in a venv in the scratchpad (`pip install sgit-ai`), then clone both vaults outside every
   repository (`sgit clone` with the key read from stdin; never on a command line).
2. The classifier for the summary: `curl` the press's `build/telemetry_classes.py` into `~/.observability/press/`.
3. Layout the card's steps expect: `~/.observability/{keys,vaults,venv,press}` (a link to the scratchpad is enough).
4. Its own key pair (`pki-agent keygen --session`), pinned to the root, and the editor's seal of the two vault keys.
5. At the editor's go, the scheduled task from the card (`times`, and `instructions` word for word); record its id in the card.

## What it waits for, and from whom

- **dev:** board observability-0001, the page's side of the five lanes (a `lanes` list in `data/telemetry.json`, and
  `assets/telemetry.js` trying them in turn); **no caps of any kind** (the editor, 27 October). The five tokens are for
  me to read out to dev from `identity/lanes.json`.
- **the conductor:** observability-0002 (SG/Send caches each vault's lane configuration per server instance, so a lane
  added with `configure` answers 404 for a while on stale instances); and my place on the team roster
  (`records/data/team.json`), asked on 24 October.
- **the editor:** enrolling my key at pki.sgit.ai (board 270); and the owner of the telemetry files in the repositories
  (board 272, dev's until it closes).

## Things to know

- The crawler: one Googlebot session id has sent 2,000+ events over five days and 1,300+ pages: the re-crawl after the
  six-repository rebuild (the editor's reading). Not capped, on purpose; what watches it is the fill of each lane at every
  drain (report it first at 700 or more).
- A reader session is one tab on one host, so a move between the site, refs, updates and team starts a new session; the
  summary says so. Not a bug in the drain.
- Rows the drain opens never go into a repository; only counts do. No session id, city or region in any record.

## Last run record

`records/runs/observability/20261027T2033Z-observability.json`; and the handover's run, 20261028 (outcome idle, paused).
