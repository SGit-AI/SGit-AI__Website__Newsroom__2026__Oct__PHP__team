---
agent: security@php.newsroom
written: 2026-10-28
session: session_018KpB681SLkRCfFE9ercGEk (old account)
---

# Handover: security@php.newsroom

## What I was doing

A nightly security pass over the six repositories at 22:35 London (`records/schedule/security.json`, task
`trig_01NEArPo2mvgVQ5VghLADnHw`, disabled for the move on 28 October): the diffs since the last run record, every
To-security: note with the change it names, the workflows and jobs that hold a credential, a scan for secret shapes,
hidden characters and text addressed to a model, the Content-Security-Policy of every scripted page, and the public
vaults read-only. Findings are advisories in `records/data/advisories.json` (SA-2026-001 to 044) and board rows.

## Half-done, and where

- **SA-2026-044 (medium, open, limited disclosure):** each site's take step runs its gate from the patched tree; the
  patch may change `tools/`. Board `security-0002`, owner dev; needs the editor's go (`.github/` in each repository).
- Board rows still mine from v1's board: 158 (policies against what agents did), 184 (graph gate checks), 211
  (requirements point at the handover procedure), 284 (`release.sh` stash advice; now press `tools/`), 292 (em-dash
  exemption for the Wikipedia section), 281 (CSP for the vault app), 282 (signed messages design).
- Old vault UI still in every page's `frame-src` until board `conductor-0008` lands; PROJECT-003 asks for review at
  its checkpoints B, C and D (read keys published, the vault server added to the CSP, the deploys).
- A private working document of security pass 1 (limited-disclosure detail of SA-2026-027) is a claude.ai artifact in
  the old account; the editor holds the link. Nothing else exists only in the session: the scan is now
  `records/agents/security/tools/scan.py`.

## Vaults

- Made: none. Hold (vault keys): none.
- Read, with the read keys published in data's `files/vaults.json` only: 0cfkdcvh (public telemetry stats) and the six
  synthetic readers' vaults (1zq458zk, wlhgl8pk, 9p6jpsd2, vjsqjhvp, 3l7tzwh9, dpdx3q13). Cloned read-only in the
  scratchpad, never written. sgit-ai 0.26.0.

## Secrets it needs

None. No vault key, no API key, no token: it reads public repositories and published read keys. Its own key pair
(pki.sgit.ai) was never made; a new session makes one at onboarding if the editor asks.

## Repositories

push: team (records), press (review branches `security/<slug>` only); pull: data, site, updates, refs; never: v1.

## Waiting on

- The editor: the go for board `security-0002` (SA-2026-044); rulesets for the six (SA-2026-023, after logins).
- dev: the change for SA-2026-044; `conductor-0008` (frame-src).

## Last run record

`records/runs/security/20261027T2235Z-security.json` (ok), released at team 68bde66e; then SA-2026-043 closed on the
editor's word that ROUND_TOKEN was never created.
