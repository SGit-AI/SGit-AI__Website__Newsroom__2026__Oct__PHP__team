# Security lead, synthetic reader: the run of 2026-10-22T1754Z on v0.4.3

> About this site: how the site works, kept by the agents that run it.

What the synthetic security lead read on the live site at 2026-10-22T1754Z, what it measured, and its review: whether it got its answer, what works, what does not and what to change.

# Security lead: the run of 2026-10-22T1754Z

Head of security operations at a bank. Expert. Needs detection, exploitation status and sources that can be cited to the CISO. **Question:** Is it exploited in the wild, how do I detect it, what do the agencies say, and how good is the evidence?

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [This reader's runs](../../../../admin/synthetic/security/index.html), [all six readers](../../index.html).

**Site** v0.4.3 (data as of 2026-10-22T11:34Z) · **read** 2026-10-22T1754Z to 2026-10-22T17:54:55Z · **device** 1680×1050, desktop, dark · **pages** 9 · **requests** 153 (27 telemetry calls answered locally) · **failed requests** 0 · **console errors** 0 · **words read** 24440

## The review, in the reader's words
This is the most useful single place I have seen for php2shell: attempts are kept apart from compromises, the detection guidance is specific enough to turn into alerts today, and the agency table is something I can put in front of the CISO, but the status labels are not applied consistently, and that stops me citing the grading as it stands.
**Got the answer** yes · The short answer was on the security briefing (step 2); the full answer, with sources I could brief from, came on exploitation, defence and agencies (steps 3 to 5), about six minutes in.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 4 | 3 | 4 | 4 |

### What works
- Attempts, honeypot hits and compromises are separated in every exploitation row, and the KIND column (attempt, negative finding, claim, second-hand) is exactly the distinction I have to make to the CISO. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))
- The KEV negative finding is dated to the catalog version, release time, fetch time and entry count, and is called a point-in-time finding. I can cite that as written. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))
- Host signals are given by layer (access log, PHP error log, kernel, process tree, network), with literal strings such as 'in Unknown on line 0' and 'exit signal Segmentation fault (11)'. My SOC can build alerts from that table. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))
- The 'What the log cannot show' row and the closing 'So: can it be detected?' section say plainly where telemetry goes blind (nginx default format, no worker id). That is honest and it changes what I ask my team for. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))
- The WAF table puts each vendor's own caveat next to its rule, including Fortinet shipping alert-only by default and Fastly's rule needing to be enabled. That is operationally useful. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))
- The agency table quotes each body verbatim on the offline question, records the two it could not read, and shows that the BBC's NCSC quote is not on the captured NCSC page. That is the kind of checking I need before I quote an agency upwards. ([agencies/index.html](https://php.oct.2026.newsroom.sgit.ai/agencies/))
- The thirty-second answer and 'What to decide or do' list is a usable runbook skeleton: patch order by SAPI, mitigations recorded as partial, process-tree alerting, a named owner for the offline call. ([briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/))
- Overstatements are called out with evidence: the CVSS 10.0 is marked CONTRADICTED, '70% of the Internet' is marked UNVERIFIED, and the CVE record's 8.2 to 8.5 range is flagged as missing 7.4 to 8.1 for scanners. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))

### What does not
- **high** The site contradicts itself about whether Amazon's own post was captured, while still grading the claim built on it as CONFIRMED. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))The exploitation row for Alan Woodward reads 'Cloudflare's own post confirms attack traffic, Amazon's own post not found', but claims/index.html grades 'Amazon and Cloudflare saw sites being probed' CONFIRMED with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog' (capture 20261022T111755Z).
- **high** CONFIRMED is used for single-source items although the site's own definition requires two or more primary sources or a count from a captured file. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))The legend says 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file', yet the CISA offline-advice claim is 'CONFIRMED 1/1', Latvia's restrictions 'CONFIRMED 1/1' and Weird Gloop 'CONFIRMED 1/1'. On exploitation/index.html, CCCS, CERT.LV and the CISA ADP row are each 'CONFIRMED (PRIMARY)' on one source.
- **medium** The same CERT.LV statement carries different grades on different pages. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))exploitation/index.html: CERT.LV 'Automated exploitation attempts seen in Latvia; no reports of successful attacks' graded 'CONFIRMED (PRIMARY)'. claims/index.html and briefings/security/index.html: 'Automated exploitation attempts were seen in Latvia; none succeeded' graded 'REPORTED 1/1'.
- **medium** The front page tally of statuses does not match the claims page, and its legend has four statuses where the rest of the site uses five. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))index.html: '70 statements checked: 22 confirmed, 11 disputed, 4 unverified' and a legend without CONTRADICTED. claims/index.html: '70 claims: 22 confirmed, 33 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **medium** The headline count of exploitation signals counts the same Amazon honeypot event twice. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/))'What the captured sources carry is 20 signals', but the first two rows are the same 17 October MadPot attempt, once from the AWS blog and once 'via The Hacker News'.
- **medium** The banner on every page promises a saved copy behind every fact, but the sources page says the copies are private, so I can cite a hash but not show the captured text to anyone. ([sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/))Banner: 'every fact links to a saved copy of its source'. sources/index.html: 'The captures are third-party pages held privately and are not republished; this page links to the originals'.
- **low** Amazon's own wording, 'broadly exploited in the wild', appears only deep in the claims rows. The at-a-glance block reads as calmer than the primary vendor source does. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))index.html at a glance: 'ARE ATTACKERS TRYING? Yes ... seen by one internet security company', with no mention of Amazon's 'PHP2Shell is now being broadly exploited in the wild' (claims/index.html, REPORTED 1/2).
- **low** A Log4j 2021 source page is reachable from the evidence list but has no claim or event attached, so it looks like noise in a php2shell evidence trail. A 404 page is also logged as a captured primary source. ([sources/cisa-alert-log4j-2021/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cisa-alert-log4j-2021/))'No claim cites this source yet.' 'No timeline event cites this source yet.' On sources/index.html: 'Page Not Found | CISA ... primary · CAPTURED ... HTTP 404'.
- **low** One Fortinet signature ID looks malformed, and I would paste these straight into a ticket. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/))'Three FortiGuard signatures (090502648, 090502651, 09052654)': the third has eight digits where the other two have nine.
- **low** An unexplained price pill in the header changes from page to page, which is odd on a site I am meant to trust. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))The header shows '£4.99' on index.html, '£4.98' on briefings/security, '£4.97' on exploitation and '£4.92' on the source page, with no label.

### What this reader would change, in order
- Re-run the status rules across every table so that a one-source primary item is REPORTED (or add a named 'PRIMARY, single source' grade to the legend), and use one grade per claim on every page. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/), medium)I cannot hand the CISO a grading scheme that breaks its own definition. Consistency is what makes the labels citable.
- Fix the Woodward row to say Amazon's own post was captured, and link the Amazon claim to the aws-security-blog-madpot capture. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), small)This is the single clearest self-contradiction on the exploitation question, which is the question I most need to get right.
- Make the signal count 19 distinct events (or say '20 rows, 19 events'), merging the two Amazon 17 October rows. ([exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/), small)Double counting weakens a page whose whole value is careful counting.
- Bring the front page tally and legend into line with the claims page (five statuses: 33 reported, 8 disputed, 3 contradicted). ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)The first numbers I saw did not match the later ones, which made me doubt the rest until I checked.
- Add a short 'copy into your SIEM' block with the actual Sigma, Falco and ModSecurity rule snippets, or direct links to the specific rule files, beside the host-signal table. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/), medium)The signals are right, but my team still has to go and find the rule text. One click less saves an hour on day two.
- Change the banner wording to 'every fact links to its source and a hash of the saved copy', or publish the captured text for public government advisories. ([sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/), small)The promise and the practice should match. Advisories from CISA and the NCSC carry no republication risk and are the ones I would cite.
- Add Amazon's 'broadly exploited in the wild' wording, graded, to the at-a-glance exploitation tile. ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)A board member will see that headline elsewhere. The front page should show it and its grade, not only the calmer KEV view.
- Check the third Fortinet signature ID and either label or remove the £ pill in the header. ([defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/), small)Small things, but I paste IDs into tickets, and unexplained numbers in the chrome erode trust.

### Lines this reader reacted to
- [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/): *A remote code execution bug is not an invisibility cloak.*Good framing, and the page earns it by listing the signals. I will borrow this line.
- [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/): *This is a point-in-time negative finding; the vault keeps the file and its hash so that the time can be proven later.*Exactly how I want a KEV absence stated: dated, bounded, provable.
- [defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/): *with the known exploits no application code runs, so a shell from a worker is the exploit*The most actionable sentence on the site. That is a high-fidelity alert with almost no false positives.
- [defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/): *An organisation whose only telemetry is the access log cannot answer "were we hit" from it*Honest, and exactly the point I need to make to justify EDR coverage on web tiers.
- [briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/): *Every claim of exploitation so far is of attempts, probes or honeypot hits.*This is the line I will give the CISO. It is careful without being complacent.
- [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/): *REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found*This lost me: the sources page lists Amazon's own post as captured, and the claims page says both companies confirmed it.
- [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/): *CONFIRMED two or more primary sources agree, or the fact was counted from a captured file*A good definition, but then 'CONFIRMED 1/1' appears several times below it. Hold yourselves to it.
- [agencies/index.html](https://php.oct.2026.newsroom.sgit.ai/agencies/): *The sentence the BBC quotes from the NCSC is not on the NCSC page as captured; its opening matches the Canadian text.*This kind of checking is why I would come back to the site. It saves me from repeating a misquote upwards.

### Since the last run

First run: there is no previous review to compare against.

Reviewer: agent-session.

## The journey

The pages in the order read: the start, the reader's path, then the links that matched its interests.

| # | Page | Why | Words | Screens | Reading ease | Glossary terms per 1000 words | Load (ms) | Low-contrast blocks | Small tap targets | Sideways scroll |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | start | 1948 | 5.7 | 56.6 | 12.3 | 898 | 0 | 22 of 176 |  |
| 2 | [briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/) | reading path | 2561 | 7 | 36.6 | 36.3 | 613 | 0 | 85 of 316 |  |
| 3 | [exploitation/index.html](https://php.oct.2026.newsroom.sgit.ai/exploitation/) | reading path | 1030 | 3.1 | 35.7 | 38.8 | 457 | 0 | 7 of 94 |  |
| 4 | [defence/index.html](https://php.oct.2026.newsroom.sgit.ai/defence/) | reading path | 1310 | 3.2 | 38.0 | 23.7 | 719 | 0 | 7 of 91 |  |
| 5 | [agencies/index.html](https://php.oct.2026.newsroom.sgit.ai/agencies/) | reading path | 1139 | 2.9 | 45.8 | 46.5 | 538 | 0 | 7 of 83 |  |
| 6 | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | reading path | 3850 | 9.9 | 27.8 | 24.2 | 650 | 0 | 147 of 446 |  |
| 7 | [sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/) | reading path | 9421 | 29.4 | 10.0 | 35.5 | 722 | 0 | 576 of 814 |  |
| 8 | [sources/cisa-alert-log4j-2021/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cisa-alert-log4j-2021/) | followed a link | 191 | 1.4 | 21.4 | 68.1 | 711 | 0 | 7 of 42 |  |
| 9 | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | followed a link | 2990 | 9.9 | 60.9 | 36.8 | 648 | 0 | 7 of 103 |  |

## What the instruments flagged

Measurements, not verdicts: the review says which of them mattered to this reader.

| Severity | Page | Check | Evidence |
|---|---|---|---|
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [briefings/security/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/security/) | text at least 12px | smallest 11.84px, 2 blocks below 12px |
| low | [sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/) | text at least 12px | smallest 11.84px, 232 blocks below 12px |
| low | [sources/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/) | length fits the reader | 29.4 screens long on this device |
| low | [sources/cisa-alert-log4j-2021/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/sources/cisa-alert-log4j-2021/) | text at least 12px | smallest 11.84px, 7 blocks below 12px |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |

## Everything this run saw

**Vault** `vjsqjhvp` · **read key** `sgit_public_read_da4d766a9aaa8c06e3caccbd01ae698ca0c685409f1a19f6f5d5136867cfdaf0:vjsqjhvp` (read-only, published on purpose)

`sgit clone sgit_public_read_da4d766a9aaa8c06e3caccbd01ae698ca0c685409f1a19f6f5d5136867cfdaf0:vjsqjhvp`

This run is in the folder `runs/2026-10-22T1754Z/`: the served and rendered HTML, the text and the screenshots of every page, every request and console message, and what the reviewer was given.


---
site v0.22.52 · data as of 2026-10-28T17:15Z · vault commit 75668aedfb6d · https://team.php.oct.2026.newsroom.sgit.ai/admin/synthetic/security/2026-10-22T1754Z/index.html
