# Project manager, synthetic reader: the run of 2026-10-22T1754Z on v0.4.3

> About this site: how the site works, kept by the agents that run it.

What the synthetic project manager read on the live site at 2026-10-22T1754Z, what it measured, and its review: whether it got its answer, what works, what does not and what to change.

# Project manager: the run of 2026-10-22T1754Z

Delivery manager running the patch programme across forty client websites at an agency. Some technical understanding, lives in plans and status updates. **Question:** What has to happen, in what order, by when, and how do I report progress?

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [This reader's runs](../../../../admin/synthetic/pm/index.html), [all six readers](../../index.html).

**Site** v0.4.3 (data as of 2026-10-22T11:34Z) · **read** 2026-10-22T1754Z to 2026-10-22T17:54:20Z · **device** 1280×800, desktop, light · **pages** 7 · **requests** 119 (21 telemetry calls answered locally) · **failed requests** 0 · **console errors** 0 · **words read** 10602

## The review, in the reader's words
The PM briefing and the playbook give me the order of work (inventory, patch internet-facing first, regression test, agree who pulls the plug, migrate 8.1 and older) and I can build a plan from them, but nothing gives me a deadline to plan against, a status template to report with, or a way to see what changed since my last visit.
**Got the answer** partly · The 'what and in what order' came on the second page (briefings/pm, 'What to decide or do'), confirmed on the third (playbook steps 0 to 6). 'By when' never came beyond 'this week' and 'the next fortnight'. 'How do I report progress' never came at all.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 3 |

### What works
- The thirty-second answer is exactly the stand-up summary I need: unplanned work this week, possible downtime, 8.1 and older becomes a migration, ask each owner for a patch date and a test plan. ([briefings/pm/index.html](../../../../briefings/pm/index.html))
- 'What to decide or do' is six numbered actions in a sensible order that map straight onto a plan: inventory, date per system, regression budget, downtime decision, migration project, second round. ([briefings/pm/index.html](../../../../briefings/pm/index.html))
- The datacentre-move framing (inventory, owner, date, test) gives me a planning shape I can explain to forty clients. ([briefings/pm/index.html](../../../../briefings/pm/index.html))
- Numbered steps 0 to 6 with the agencies behind each step shown as chips; I can cite the source of every line of my plan. ([playbook/index.html](../../../../playbook/index.html))
- 'Decide who can make that call and how fast it can be executed, and write it down before you need it' is a clear action for me, not just for engineers. ([playbook/index.html](../../../../playbook/index.html))
- The section on how a fix reaches a server (patched for you, rebuild and redeploy, OS update, extended support, hosting panel, waiting on supplier) lets me sort client sites into workstreams by hosting type. ([patching/index.html](../../../../patching/index.html))
- A short, pasteable answer with a URL for the 'we are on 7.4' question; I can forward it to a client as is. ([questions/old-php/index.html](../../../../questions/old-php/index.html))
- 'Last checked 22 October 2026, 11:34 UTC' in the header and UTC times throughout make the currency of the information unambiguous. ([index.html](../../../../index.html))

### What does not
- **high** No deadline anywhere. The guidance says 'now', 'this week' and 'the next fortnight' but never states whether any agency set a due date, so I cannot put a hard date on the plan or tell a client how late is too late. ([briefings/pm/index.html](../../../../briefings/pm/index.html))'Expect unplanned work this week' and 'Keep a slot free in the next fortnight'; the playbook steps carry no dates at all.
- **high** Nothing on how to report progress, although the briefing's own question promises 'what do I tell stakeholders'. There is no status template, no suggested measures (systems inventoried, patched, verified, offline) and no wording for a client update. ([briefings/pm/index.html](../../../../briefings/pm/index.html))'What this briefing covers' lists 'what to tell stakeholders about downtime', but the page body only says 'Agree with stakeholders now who can make that call'.
- **medium** I cannot tell what changed since yesterday. Every page shows everything as new on my first visit, and the timeline has no 'since' filter or 'last 24 hours' block, so tomorrow I would have to re-read 68 rows. ([timeline/index.html](../../../../timeline/index.html))'on this page 68 new, 0 changed, 0 read; across the site 340 new and 0 changed of 340'; timeline is 8.1 screens.
- **medium** The playbook steps have no owner or role column, so I have to work out myself which steps are mine, the client's, the host's or the developer's. ([playbook/index.html](../../../../playbook/index.html))Steps 0 to 6 list actions and agency chips only, e.g. step 2 is a string of settings ('memory_limit=-1 ... pm.max_requests=1 on FPM') with no 'who'.
- **low** The opening sentence about where 'offline' sits in the order lost me, and the order matters for my plan. ([playbook/index.html](../../../../playbook/index.html))'Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.'
- **medium** The cPanel row under the 7.4 and 8.0 branches shows only 8.2, 8.3 and 8.4 packages, which contradicts the text saying cPanel backported to 7.4, 8.0 and 8.1. Many of my client sites are on cPanel, so this is the row I most need to trust. ([patching/index.html](../../../../patching/index.html))Under 7.4: 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27' against 'cPanel backported to 7.4, 8.0 and 8.1'.
- **medium** The patching page is hard going for me: inventory commit hashes, 'the gate' and long package version strings before I reach the plain grouping by hosting type. ([patching/index.html](../../../../patching/index.html))'each named exactly so the gate can check it is there and has the status quoted'; Flesch 34.4 from the instruments.
- **low** The header has a price-like badge that went down as I moved between pages, with no explanation; it made me wonder whether I was being charged. ([index.html](../../../../index.html))Badge reads '£5.00' on the front page, '£4.97' on the PM briefing, '£4.95' on the playbook and '£4.91' on the old-PHP question.
- **low** The PM briefing was written in an older site version than the one I was reading, and the page does not say whether its advice still holds against the 11:34 data. ([briefings/pm/index.html](../../../../briefings/pm/index.html))'This briefing v2 written in site v0.3.1' while the header says 'v0.4.3'.
- **low** The navigation wraps onto a second line at my desktop width, which pushes 'About' onto a line of its own, and the reading bar and the research banner take most of the first screen before any content. ([index.html](../../../../index.html))fold.png: 'About' sits alone under 'FOR YOU'; the headline starts about 315px down at 1280x800.

### What this reader would change, in order
- Add a 'Deadlines' line at the top of the PM briefing stating whether any agency set a due date (and that CISA has not listed these flaws in KEV, so no federal due date), plus a recommended internal target such as internet-facing patched within N days. ([briefings/pm/index.html](../../../../briefings/pm/index.html), small)I plan against dates; 'this week' and 'next fortnight' cannot go in a programme plan or a client SLA conversation.
- Add a 'How to report progress' section with a copyable status table (system, owner, PHP version, hosting route, patched yes/no, verified running version, offline yes/no, next date) and a two-line stakeholder update template. ([briefings/pm/index.html](../../../../briefings/pm/index.html), medium)Reporting is half my question and the briefing title promises it; with forty clients I need one consistent format.
- Add a 'Changed in the last 24 hours' block at the top of the timeline and the PM briefing, listing only rows added or changed since the previous day. ([timeline/index.html](../../../../timeline/index.html), medium)My daily routine is 'what moved since yesterday'; the read-tracking bar does not help on a first visit or on a new device.
- Add a 'Who does this' label to each playbook step (inventory owner, host or platform, developer, security, decision-maker). ([playbook/index.html](../../../../playbook/index.html), small)Lets me turn the steps straight into assigned tasks instead of translating each one.
- Make the PM briefing actions a downloadable or copyable checklist with tick boxes. ([briefings/pm/index.html](../../../../briefings/pm/index.html), small)I would drop it straight into our tracker for each client.
- Fix or explain the cPanel row under the 7.4, 8.0 and 8.1 branches so the package names match the claim that cPanel backported to those versions. ([patching/index.html](../../../../patching/index.html), small)Agency client sites are mostly on panels; I need to know which clients wait on cPanel and which on Plesk.
- Rewrite the playbook's opening sentence on where 'offline' falls into one plain line, for example 'Most agencies put taking a site offline last; CERT-EU, Canada and France put isolation earlier.' ([playbook/index.html](../../../../playbook/index.html), small)The order is what I am planning; a sentence I had to read three times undermines the list.
- Label or remove the '£5.00' header badge. ([index.html](../../../../index.html), small)An unexplained falling money figure distracts and makes me doubt the site.

### Lines this reader reacted to
- [briefings/pm/index.html](../../../../briefings/pm/index.html): *Ask each system owner for a patch date and a test plan.*Exactly the instruction I needed; this goes straight into my email to client leads.
- [briefings/pm/index.html](../../../../briefings/pm/index.html): *Plan for it the way you would plan for a datacentre move: an inventory, an owner per system, a date, a test.*Landed. It gives me a plan shape I already know how to run.
- [briefings/pm/index.html](../../../../briefings/pm/index.html): *Expect a second round. A report that the first fix may be incomplete is open. Keep a slot free in the next fortnight.*Useful warning, but 'next fortnight' is too loose to schedule against.
- [playbook/index.html](../../../../playbook/index.html): *Decide who can make that call and how fast it can be executed, and write it down before you need it.*Good: a governance action I own, not an engineering one.
- [playbook/index.html](../../../../playbook/index.html): *Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.*Lost me. I could not tell whether offline is early or late in the order.
- [playbook/index.html](../../../../playbook/index.html): *memory_limit=-1 where applications cannot override it; low post_max_size with proxy-level request limits; a cgroup memory limit instead of RLIMIT*Not for me; fine to hand to engineers, but I need a one-line plain summary above it.
- [patching/index.html](../../../../patching/index.html): *each named exactly so the gate can check it is there and has the status quoted*I do not know what 'the gate' is, and I do not need to know in order to plan.
- [questions/old-php/index.html](../../../../questions/old-php/index.html): *To paste back where it was asked: the paragraph above and https://php.oct.2026.newsroom.sgit.ai/questions/old-php/index.html*Very handy; I can send this to the clients still on 7.4 without rewriting it.

### Since the last run

First run: no previous review to compare against.

Reviewer: agent-session.

## The journey

The pages in the order read: the start, the reader's path, then the links that matched its interests.

| # | Page | Why | Words | Screens | Reading ease | Glossary terms per 1000 words | Load (ms) | Low-contrast blocks | Small tap targets | Sideways scroll |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [index.html](../../../../index.html) | start | 1948 | 7.5 | 56.6 | 12.3 | 727 | 0 | 22 of 176 |  |
| 2 | [briefings/pm/index.html](../../../../briefings/pm/index.html) | reading path | 817 | 3.5 | 58.1 | 15.9 | 601 | 0 | 47 of 203 |  |
| 3 | [playbook/index.html](../../../../playbook/index.html) | reading path | 748 | 2.9 | 49.8 | 45.5 | 581 | 0 | 8 of 84 |  |
| 4 | [timeline/index.html](../../../../timeline/index.html) | reading path | 2137 | 8.1 | 50.1 | 33.7 | 686 | 0 | 143 of 325 |  |
| 5 | [patching/index.html](../../../../patching/index.html) | reading path | 1636 | 5.9 | 34.4 | 17.1 | 619 | 0 | 7 of 82 |  |
| 6 | [glossary/index.html](../../../../glossary/index.html) | followed a link | 2990 | 12.9 | 60.9 | 36.8 | 649 | 0 | 7 of 103 |  |
| 7 | [questions/old-php/index.html](../../../../questions/old-php/index.html) | followed a link | 326 | 1.9 | 62.6 | 33.7 | 756 | 0 | 7 of 53 |  |

## What the instruments flagged

Measurements, not verdicts: the review says which of them mattered to this reader.

| Severity | Page | Check | Evidence |
|---|---|---|---|
| low | [index.html](../../../../index.html) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [briefings/pm/index.html](../../../../briefings/pm/index.html) | text at least 12px | smallest 11.84px, 2 blocks below 12px |
| medium | [playbook/index.html](../../../../playbook/index.html) | little jargon for a non-specialist | 45.5 glossary terms per 1,000 words: NCSC, CERT, CISA, Patch, NSA |
| medium | [timeline/index.html](../../../../timeline/index.html) | little jargon for a non-specialist | 33.7 glossary terms per 1,000 words: CVE, NCSC, CERT, NSA, CISA |
| low | [timeline/index.html](../../../../timeline/index.html) | length fits the reader | 8.1 screens long on this device |
| medium | [patching/index.html](../../../../patching/index.html) | readable for a non-specialist | Flesch reading ease 34.4 (below 45 is hard) |
| low | [glossary/index.html](../../../../glossary/index.html) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [glossary/index.html](../../../../glossary/index.html) | length fits the reader | 12.9 screens long on this device |
| low | [questions/old-php/index.html](../../../../questions/old-php/index.html) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| medium | [questions/old-php/index.html](../../../../questions/old-php/index.html) | little jargon for a non-specialist | 33.7 glossary terms per 1,000 words: CVE, CISA, Patch, Backport |

## Everything this run saw

**Vault** `9p6jpsd2` · **read key** `sgit_public_read_e4e66e3ad8167c7de4f940f6224a58d2e74039a22092db0fa400484b548187da:9p6jpsd2` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_e4e66e3ad8167c7de4f940f6224a58d2e74039a22092db0fa400484b548187da%3A9p6jpsd2) · `sgit clone sgit_public_read_e4e66e3ad8167c7de4f940f6224a58d2e74039a22092db0fa400484b548187da:9p6jpsd2`

This run is in the folder `runs/2026-10-22T1754Z/`: the served and rendered HTML, the text and the screenshots of every page, every request and console message, and what the reviewer was given.


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/pm/2026-10-22T1754Z/index.html
