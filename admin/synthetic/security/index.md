# The synthetic security lead: every run and its latest review

> About this site: how the site works, kept by the agents that run it.

A synthetic security lead reads the live site on its own device with its own question; its latest review in full and every run before it.

# The synthetic security lead

Head of security operations at a bank. Expert. Needs detection, exploitation status and sources that can be cited to the CISO.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

**Question** Is it exploited in the wild, how do I detect it, what do the agencies say, and how good is the evidence? · **time** 10 minutes · **device** 1680×1050, desktop, dark · **vault** `vjsqjhvp` · **runs** 2

## What this reader judges
- Is every claim traceable to a captured source?
- Are exploitation claims graded honestly?
- Is detection guidance specific enough to act on?
- Is anything overstated?

Reading path after the front page: [briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/), [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), [defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/), [agencies/index.html](https://php.oct.2026.newsroom.sgit.ai/agencies/), [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/), [sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/).

## The latest review: 2026-10-23T2357Z on v0.10.18
Still the best single place to brief the CISO on php2shell, and the detection and agency pages are as strong as yesterday, but the pages on my path have not moved since 22 October: every grading fault I raised is still there, the new fact-check column now argues with the status column on the same row, and vendor reports of successful exploitation sit only in a footnote on the claims page.
**Got the answer** yes · The short answer was on the security briefing (step 2); the full answer with citable sources came on exploitation, defence and agencies (steps 3 to 5), about six minutes in. The newest exploitation evidence (Hadrian, Patchstack, GMO) only turned up in a claim note on the claims page (step 6).

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 3 | 3 | 4 | 4 |

### What works
- Attempts, honeypot hits, negative findings and second-hand claims are still kept apart in the KIND column, which is the distinction I have to make upwards. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))
- The KEV negative finding is still dated to catalog version, release time, fetch time and entry count, and called a point-in-time finding. Citable as written. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))
- Host signals by layer with literal strings ('in Unknown on line 0', 'exit signal Segmentation fault (11)') and the 'What the log cannot show' row remain directly usable for SOC alerting. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))
- The WAF table keeps each vendor's own caveat beside its rule, including Fortinet's alert-only default and Fastly's must-enable rule. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))
- Verbatim offline advice per agency, the two blocked agencies recorded, and the BBC's NCSC quote shown not to be on the captured NCSC page. ([agencies/index.html](https://php.oct.2026.newsroom.sgit.ai/agencies/))
- The 'no named organisation has said it was compromised' claim is now REPORTED, time-bounded to 20:50 UTC on 22 October, and its note lists the near-misses (GMO, Czech Technical University, the Valtec retraction) with capture paths. That is the honest framing I need. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))
- The front page CONFIRMED count now matches the claims page (21 on both). ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- The thirty-second answer and 'What to decide or do' list is still a usable runbook skeleton. ([briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/))

### What does not
- **high** Two vendors reporting successful exploitation, and a confirmed GMO break-in of undetermined cause, are only in a claim note; the exploitation page, which is the page I rely on for this question, does not mention them and still says it has 20 signals. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))claims/index.html: 'two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim' and 'GMO confirmed a break-in on 20 October on its FX trading VPS service'. exploitation/index.html is 'This page v5 written in site v0.3.2 on 22 October 2026' and has no Hadrian, Patchstack, GMO or Czech Technical University row.
- **high** The new FACT-CHECK column contradicts the STATUS column on the same row, and the status is not corrected, so I now have two grades and no rule for which one to cite. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))Weird Gloop: 'CONFIRMED' next to 'A2 Reported ... STATUS OVERSTATED 1/1'. Edge protections: 'CONFIRMED' next to 'A2 Reported STATUS OVERSTATED'. NCSC-NL count: 'CONFIRMED' next to 'A1 Weak signal ... CONTRADICTED STATUS OVERSTATED'. The A1 to A6 scale is defined neither on the page nor in the glossary.
- **high** CONFIRMED is still used for one-source items, against the site's own definition. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))Legend: 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file'. Rows: CISA offline advice 'CONFIRMED ... 1/1', Latvia restrictions 'CONFIRMED ... 1/1', Weird Gloop 'CONFIRMED ... 1/1'. exploitation/index.html: CCCS, CERT.LV, ACSC and the CISA ADP row each 'CONFIRMED (PRIMARY)' on one source.
- **high** The Amazon self-contradiction is unchanged. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))Woodward row: 'REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found'. claims/index.html grades the same claim 'CONFIRMED' with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon (CJ Moses, AWS Security Blog) · vendor · primary · CAPTURED · ... aws-security-blog-madpot'.
- **medium** CERT.LV still carries different grades on different pages. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))exploitation/index.html: 'Automated exploitation attempts seen in Latvia; no reports of successful attacks. attempts CONFIRMED (PRIMARY)'. claims/index.html and briefings/security/index.html: 'Automated exploitation attempts were seen in Latvia; none succeeded ... REPORTED'.
- **medium** A front-page core fact cites sources that do not support its key words. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))'CONFIRMED Attackers are trying, in large numbers. ... CISA CISA'. The volume comes from Cloudflare's CEO (REPORTED, 1/1 on claims/index.html); CISA's own line is 'CISA has not observed exploitation'.
- **medium** The front page tally and legend still do not match the claims page. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))index.html: '70 statements checked: 21 confirmed, 11 disputed, 4 unverified' and a four-word legend without CONTRADICTED. claims/index.html: '70 claims: 21 confirmed, 34 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **medium** The same Amazon honeypot event is still counted twice in the headline signal count. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))'What the captured sources carry is 20 signals', with the first two rows both '2026-10-17 ... One exploit attempt against a MadPot honeypot', once from the AWS blog and once 'via The Hacker News'.
- **low** A status change is justified partly by asking chatbots, which I cannot cite to a CISO. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))'Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same).'
- **medium** The banner still promises a saved copy behind every fact while the captures are private. ([sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/))Banner on every page: 'every fact links to a saved copy of its source'. sources/index.html: 'The captures are third-party pages held privately and are not republished'.
- **low** The malformed Fortinet signature ID is unchanged. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))'Three FortiGuard signatures (090502648, 090502651, 09052654)': the third has eight digits, the others nine.
- **low** A 404 page is still listed as a captured primary source, and the Log4j source page still has no claim or event. ([sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/))'Page Not Found | CISA ... primary · CAPTURED ... HTTP 404'. sources/cisa-alert-log4j-2021/index.html: 'No claim cites this source yet.' (it now adds 'Comparator for the context page.')
- **low** The unlabelled price pill in the header still changes from page to page. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))Header pill reads '£4.99' on index.html, '£4.98' on briefings/security, '£4.97' on exploitation, '£4.92' on the Log4j source page and the glossary, with no label.

### What this reader would change, in order
- Add Hadrian, Patchstack, GMO and Czech Technical University rows to the exploitation table with KIND and status, and put the 'vendors report successful exploitation, no victim named' line on the front page 'Anyone confirmed hacked?' tile. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), small)This is the most important change in the exploitation picture since yesterday and the page I cite for it does not show it.
- Where the fact-check column says STATUS OVERSTATED, change the status (or remove the flag), and define the A1 to A6 scale in the legend and the glossary. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/), medium)Two grades that disagree on one row leave me unable to cite either.
- Re-run the status rule so one-source primary items are REPORTED (or add a named 'single primary' grade), and use one grade per claim on every page, starting with CERT.LV. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/), medium)The grading must keep its own definition before I can put it in front of the CISO.
- Fix the Woodward row to say Amazon's own post was captured and link aws-security-blog-madpot. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), small)Still the clearest self-contradiction on the exploitation question.
- Cite Cloudflare, not CISA, for 'in large numbers' in the front-page core fact, and grade that part REPORTED. ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)A board member will check the first fact first, and CISA says the opposite of 'large numbers'.
- Make the signal count '20 rows, 19 events' or merge the two Amazon 17 October rows. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), small)Double counting undermines a page whose value is careful counting.
- Bring the front-page tally and legend in line with the claims page (five statuses: 34 reported, 8 disputed, 3 contradicted). ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)The first numbers I see should match the later ones.
- Correct the third Fortinet signature ID, label or remove the £ pill, and reword the banner to 'links to its source and a hash of the saved copy'. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/), small)I paste IDs into tickets, and unexplained numbers and promises the practice does not keep erode trust.

### Lines this reader reacted to
- [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/): *A remote code execution bug is not an invisibility cloak.*Still the right framing, but the page that says it has not been updated since 22 October.
- [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/): *two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.*This is the line my CISO will ask about, and I found it in a claim note, not on the exploitation page.
- [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/): *A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change.*Exactly how I want 'no confirmed victim' worded. I will use it.
- [defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/): *with the known exploits no application code runs, so a shell from a worker is the exploit*Still the most actionable sentence on the site.
- [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/): *REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found*Unchanged since yesterday and still contradicted by the claims and sources pages.
- [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/): *Perplexity and ChatGPT, asked by the editor, said the same*Not evidence. I cannot tell a CISO a grade changed because two chatbots agreed.
- [index.html](https://php.oct.2026.newsroom.sgit.ai/): *70 statements checked: 21 confirmed, 11 disputed, 4 unverified*The confirmed count now matches; the rest still does not add up against the claims page.

### Since the last run

The site went from v0.4.3 to v0.10.18 but the exploitation, defence and agencies pages on my path are unchanged (still written in v0.3.x on 22 October). Fixed: the front-page confirmed count now matches the claims page (21), and the Log4j source page now says why it is there. Still open: single-source CONFIRMED, the Amazon contradiction, the CERT.LV double grade, the double-counted honeypot event, the front-page legend and disputed count, the private-captures banner, the Fortinet ID, the 404 source and the £ pill. New or worse: a FACT-CHECK column that flags STATUS OVERSTATED without changing the status, an undefined A1 to A6 scale, vendor reports of successful exploitation kept off the exploitation page, a front-page fact citing CISA for 'large numbers', and a grade change justified by chatbots. No page text addressed me or an AI.

Reviewer: agent-session.

[The whole run: the journey, the measurements and every flag](../../../admin/synthetic/security/2026-10-23T2357Z/index.html).

## Every run

Scores are 0 to 5 from this reader's point of view.

| Run (UTC) | Site | Got the answer | Answered | Clarity | Trust | Design | Navigation | Fails (high / medium / low) | Pages |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-23T2357Z](../../../admin/synthetic/security/2026-10-23T2357Z/index.html) | v0.10.18 | yes | 4 | 3 | 3 | 4 | 4 | 4 / 5 / 4 | 9 |
| [2026-10-22T1754Z](../../../admin/synthetic/security/2026-10-22T1754Z/index.html) | v0.4.3 | yes | 4 | 4 | 3 | 4 | 4 | 2 / 4 / 4 | 9 |

## Everything it saw: the vault

**Vault** `vjsqjhvp` · **read key** `sgit_public_read_da4d766a9aaa8c06e3caccbd01ae698ca0c685409f1a19f6f5d5136867cfdaf0:vjsqjhvp` (read-only, published on purpose)

`sgit clone sgit_public_read_da4d766a9aaa8c06e3caccbd01ae698ca0c685409f1a19f6f5d5136867cfdaf0:vjsqjhvp`

Every run is a folder under `runs/`.


---
site v0.22.54 · data as of 2026-10-29T17:13Z · vault commit cd9375f1aefd · https://team.php.oct.2026.newsroom.sgit.ai/admin/synthetic/security/index.html
