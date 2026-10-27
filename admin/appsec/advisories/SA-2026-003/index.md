# SA-2026-003: Article links could inject attributes

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-003 (medium, fixed): Article links could inject attributes.

[Advisories](../index.html) / SA-2026-003

# SA-2026-003: Article links could inject attributes

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | medium |
| **Status** | fixed |
| **Weakness** | CWE-79 |
| **Component** | `admin/build/build.py (article_inline)` |
| **Found by** | security@php.newsroom |
| **Found** | 2026-10-22 |
| **Fixed in** | v0.5.5 |
| **Fixed by** | security@php.newsroom |

## What it is

The article renderer escaped text without escaping quotes, then put link targets into href="...". A link target holding a quote could add attributes, such as an event handler.

## What an attacker could do

Stored XSS through any article text, including guest articles.

**How:** [x](/a" onmouseover="...) in an article became a live handler.

## Root cause

html.escape(quote=False) was used for text that later landed inside an attribute.

## What contributed
- The markdown renderer was hand-written, with regexes, after escaping.

## What was not in place

Escaping matched to the output context, and link targets restricted to a safe character set.

## The fix

Link targets are quoted, escaped and restricted to [A-Za-z0-9/._#-]; https links exclude quotes and spaces.

## What prevents it now

The gate fails on any inline event-handler attribute in generated HTML (security_check.py, since the editor's go on 25 October).


---
site v0.22.46 · data as of 2026-10-27T19:13Z · vault commit 6f0d5c50bf12 · https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-003/index.html
