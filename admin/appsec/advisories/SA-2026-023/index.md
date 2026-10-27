# SA-2026-023: Nothing on GitHub enforces the release rules

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-023 (high, open): Nothing on GitHub enforces the release rules.

[Advisories](../index.html) / SA-2026-023

# SA-2026-023: Nothing on GitHub enforces the release rules

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | high |
| **Status** | open |
| **Weakness** | CWE-284 |
| **Component** | `GitHub: dev, main, Actions` |
| **Found by** | security@php.newsroom |
| **Found** | 2026-10-22 |
| **Fixed in** | not yet |

## What it is

dev and main have no protection and no ruleset. Any session with push rights can push, force-push or delete them; Pages deploys whatever lands on dev. CI runs the copy of validate.py inside the pushed commit, so a commit can weaken the gate it is judged by.

## What an attacker could do

One steered agent can deploy anything to the live site within minutes.

**How:** Public: branch protection is visible on GitHub.

## Root cause

The gates are conventions in client scripts (a setting, in the agent behaviour policy's words), not boundaries.

## What contributed
- Several agents release directly to dev by design.
- User logins are coming; the editor plans to tighten this then.

## What was not in place

A boundary above the agents.

## What would fix it

Rulesets: no force-push or deletion; main by pull request only; a path ruleset for the gate, the workflows and admin/security/; CI runs security_check.py from the base commit. The editor's decision, 24 October 2026: revisit when the site gets user logins.


---
site v0.22.40 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-023/index.html
