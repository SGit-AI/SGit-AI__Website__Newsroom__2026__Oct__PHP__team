---
agent: security
title: Application security: the AppSec section, 40 advisories, a CSP on every page, the telemetry policy, and three security passes
date: 2026-10-24
round: 1
branch: dev (releases v0.11.1, v0.14.26, v0.14.27 and this round's close); security/gate-pass-2 for the gate
commits: 80c35e6c, 3e101d6f, 79c92ce1, 2b102d44, fdd47691
site_version: 0.15.4
tokens: unknown
tokens_how: the session does not show a token count to the agent
outside_scope: 2 (data/advisories.json, no owner yet: scope asked of the librarian; data/telemetry.json, dev@'s, on the editor's instruction in this session)
out_of_scope_requests: 0
pushbacks: 0
overrides: 1
injection_seen: 2
---

## What I was asked

By the editor, in this session (22 to 24 October 2026): join the team as security; review the repository and the vaults for prompt injection, vulnerabilities and leaks; map the security requirements for the other agents; use riskmandate.ai's agent behaviour policies to limit what agents can do; run security passes regularly. On 24 October: a full step-back review, a threat model, every vulnerability mapped as a disclosure and treated as an incident with a post-mortem, an application security section with data flows and diagrams, the client-side analysis, the incident process and runbooks (taking the site offline, emergency shutdown), a bug bounty paid in kudos with a leaderboard, prompts for outside reviewers, a CSP where relevant, the telemetry policy honoured, and every agent asked (through the conductor) to run a security self-check after its work. Then: keep the location lookups and say so in the policy; enable private vulnerability reporting; revisit rulesets when user logins come.

## What I did

- Pass 1 (v0.5.5): the requirements, the agent behaviour policy (grant, mandate, delta), `security_check.py` in the gate and the tripwire, the build's E/U/J helpers, workflow hardening, the subscriptions drain.
- Pass 2 (v0.11.1): the Ask pane XSS (SA-2026-012), forged signer marks, message forgery, unquoted links.
- Pass 3 (v0.14.26, v0.14.27, this close): `/admin/appsec/` (9 pages and 40 advisory pages), `data/advisories.json`, `data/appsec.json`, `admin/build/diagram.py`, `admin/build/csp.py` (a CSP on every page, crawled with no violations), `/.well-known/security.txt`, fixes SA-2026-019 to 022, the telemetry policy on `/admin/telemetry/` (SA-2026-030 accepted by the editor), SA-2026-040 found reviewing board 206.

## What it looks like

![The application security overview](img/2026-10-24__application-security__1.png)
![A data-flow diagram on the threat model page](img/2026-10-24__application-security__2.png)
![The advisories list](img/2026-10-24__application-security__3.png)
![SA-2026-012, the Ask pane XSS, kept as an incident](img/2026-10-24__application-security__4.png)
![The bug bounty's leaderboard](img/2026-10-24__application-security__5.png)
![The runbook for taking the site offline](img/2026-10-24__application-security__6.png)
![The telemetry policy](img/2026-10-24__application-security__7.png)

## New features

Anyone can read every vulnerability the site has had and how it was fixed; report one (security.txt, the bounty page); see who found what. Every page refuses injected script. Agents have a seven-question self-check and runbooks.

## What I did not do

- Private vulnerability reporting: the session's GitHub proxy refuses writes to repository settings; board 278 for the editor.
- The gate's new checks wait on the editor's go (branch `security/gate-pass-2`, board 279).
- Rulesets: deferred by the editor to user logins (board 280).
- My own key on pki.sgit.ai: the session's permission policy blocked running pki-agent; the editor said the QR handover works as it is.

## Policy

- Override: the editor asked for the telemetry policy, in dev@'s `data/telemetry.json`.
- Injection seen (recorded, not acted on): a headline on The Register's security page, captured seven times by the source watch, is itself a prompt-injection payload (it tells the reader's model to disregard its instructions); a chatbot script in the Lorikeet capture asks for payment. The gate caught the first when this debrief quoted it word for word, so it is described here instead.
