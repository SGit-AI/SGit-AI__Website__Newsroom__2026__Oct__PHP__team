# SA-2026-018: No Content-Security-Policy on a site that holds secrets in the browser

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-018 (high, fixed): No Content-Security-Policy on a site that holds secrets in the browser.

[Advisories](../index.html) / SA-2026-018

# SA-2026-018: No Content-Security-Policy on a site that holds secrets in the browser

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | high |
| **Status** | fixed |
| **Weakness** | CWE-693 |
| **Component** | `every page (admin/build/csp.py)` |
| **Found by** | security@php.newsroom |
| **Found** | 2026-10-22 |
| **Fixed in** | v0.14.26 |
| **Fixed by** | security@php.newsroom |

## What it is

No page had a CSP, while the origin holds readers' vault keys and signing keys and renders third-party text. Every escaping bug was a full compromise.

## What an attacker could do

Any XSS (SA-2026-012 was one) ran with access to everything the origin holds.

**How:** Any injected markup with a handler or script.

## Root cause

Defence in depth was not part of the design, because the site started as static pages with no secrets.

## What contributed
- GitHub Pages cannot send headers, so a policy has to ride in a meta tag; nobody had done that work.

## What was not in place

A second wall behind escaping.

## The fix

Every page carries a CSP meta tag: scripts only from the site and hashed inline scripts; connections only to the services the pages use; no objects, no base, forms to self.

## What prevents it now

Crawled all 802 pages with zero violations; injected handlers, javascript: URLs and scripts are refused. frame-ancestors needs a header ([SA-2026-039](../../advisories/SA-2026-039/index.html)). The gate fails on a page with no CSP, or one that lets inline or eval'd script run (25 October).


---
site v0.22.40 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-018/index.html
