# SA-2026-026: Readers' keys on the shared origin: /now/ and the Ask pane

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-026 (medium, mitigated): Readers' keys on the shared origin: /now/ and the Ask pane.

[Advisories](../index.html) / SA-2026-026

# SA-2026-026: Readers' keys on the shared origin: /now/ and the Ask pane

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | medium |
| **Status** | mitigated |
| **Weakness** | CWE-922 |
| **Component** | `assets/now/now.js, assets/ask/ask.js` |
| **Found by** | security@php.newsroom |
| **Found** | 2026-10-22 |
| **Fixed in** | not yet |

## What it is

The reader's vault key is kept in sessionStorage, and in localStorage when "remember" is ticked; the vault holds the OpenRouter key and the SG/Send access token. A vault someone hands the reader can supply its own OpenRouter key and model settings.

## What an attacker could do

Any script on the origin reads the key (now blocked by the CSP); a malicious vault routes the reader's chats through an account its author can see.

**How:** Public in outline.

## Root cause

Secrets for one app share an origin with every page.

## What contributed
- The phone app and the Ask pane grew fast.

## What was not in place

An origin of its own for secret-holding apps.

## What would fix it

Move /now/ and the Ask pane to a subdomain; confirm before adopting a vault's key or model; allow-list model ids.


---
site v0.22.51 · data as of 2026-10-28T17:15Z · vault commit 75668aedfb6d · https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-026/index.html
