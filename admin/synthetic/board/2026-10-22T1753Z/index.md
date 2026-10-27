# Board member, synthetic reader: the run of 2026-10-22T1753Z on v0.4.3

> About this site: how the site works, kept by the agents that run it.

What the synthetic board member read on the live site at 2026-10-22T1753Z, what it measured, and its review: whether it got its answer, what works, what does not and what to change.

# Board member: the run of 2026-10-22T1753Z

A non-executive director of a mid-sized retailer whose online shop runs on PHP. Not technical. Reads on a phone between meetings. **Question:** Is my company exposed, is management handling it, and what should I ask at the next board meeting?

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [This reader's runs](../../../../admin/synthetic/board/index.html), [all six readers](../../index.html).

**Site** v0.4.3 (data as of 2026-10-22T11:34Z) · **read** 2026-10-22T1753Z to 2026-10-22T17:53:31Z · **device** 390×844, phone, light · **pages** 6 · **requests** 102 (18 telemetry calls answered locally) · **failed requests** 0 · **console errors** 0 · **words read** 12242

## The review, in the reader's words
The board briefing gives me five sharp questions to put to management and a clear sense that nobody has been confirmed hacked, but on my phone I had to scroll past two screens of reading-tracker and research boxes before I saw it, and nothing told me what a retailer with an online shop should specifically worry about.
**Got the answer** partly · On page 2 (briefings/board/index.html): the thirty-second answer sits just below the first screen and the 'What to decide or do' list gives me my board questions about one screen further down; whether my own company is exposed is never answerable from the site, which is fair, but the briefing also does not say plainly that an online shop on PHP is squarely in scope until the explainer and the Questions page.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 4 | 4 | 2 | 3 |

### What works
- The thirty-second answer in the board briefing is exactly the shape I need: what happened, what agencies say, no confirmed break-in, and the three questions to ask. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))
- 'What to decide or do' is a ready-made list of board questions (inventory including vendor products, patched and restarted, who can pull a system, what a compromise would reach, evidence we were not hit). I can copy these straight into my notes. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))
- The 'At a glance' tiles (Is there a fix? Yes. Anyone confirmed hacked? Not yet.) tell me in seconds how worried to be. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- The opening paragraph is plain and reassuring in the right way: it says what PHP is, that a fix exists and that phones and laptops are not affected. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- The kitchen analogy and the 'What that can reach' list finally made the risk concrete for me: database passwords and other systems that trust the server. ([explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/))
- The 'IN PLAIN ENGLISH' line at the top of the impact page saves a non-technical reader: two lists, many offline as a precaution, nobody confirmed broken into. ([impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/))
- The Questions page answers 'Should we take our site offline?' and 'We are behind Cloudflare. Are we safe?' in short pasteable paragraphs, which are both questions I expect to hear in the boardroom. ([questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/))
- The status words (confirmed, reported, unverified) and the sources under each fact make me trust that I am not repeating a rumour to the board. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))

### What does not
- **high** On a phone the first screen of every page is site machinery, not the story: version badge, a £ meter, a reading tracker with 'fade / hide / show' buttons and a 'Research' box. On the board briefing the thirty-second answer only begins at the very bottom of the first screen. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))fold.png shows 'Your reading: on this page 35 new, 0 changed, 0 read', 'Mark this page read', 'Mark everything read', 'Read items: fade hide show', the RESEARCH box and the 'New to this story?' banner before 'THE ANSWER IN THIRTY SECONDS' appears at the bottom edge.
- **medium** The briefing promises to cover 'what is it costing us' but never gives me any sense of cost, for downtime or for a breach; it only points me to other readers' briefings. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))Heading question 'Are we exposed, what is it costing us...' while the body says 'what it costs to find out' and nothing more; the CFO briefing is only listed under 'Other readers'.
- **medium** Nothing speaks to my kind of business. Online shops are mentioned only in passing in a list of things the BBC reported offline; there is no line saying what an e-commerce site on PHP stands to lose (card data, customer accounts). ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))The only shop reference I found is 'French government services; the University of Geneva; the BBC; online shops' in the impact table; the Questions page says Magento runs on PHP but the board briefing does not.
- **medium** The 'What is still open' section in my briefing is written for a journalist, not a director: deleted videos, Fediverse reports and oss-security mean nothing to me. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))'Whether the deleted Calif video is the one now embedded on Calif's own write-up.' and 'A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October'.
- **medium** The impact page tables are squeezed into six narrow columns on a phone, so each row becomes a tall stack of two- or three-word lines and the page runs to more than nine screens. ([impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/))full.jpg shows the 'Taken offline' table with columns WHO, WHAT HAPPENED, WHEN, WHO SAYS SO, STATUS, SOURCES each a sliver wide; instruments: 9.4 screens, reading ease 8.9.
- **medium** The closing summary of the impact page drops straight into technical jargon I cannot get past. ([impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/))'how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell'.
- **low** Words listed for me to 'meet' include terms the briefing itself tells me to skip, which is confusing. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/))'What you can skip: SAPIs and settings' but 'Words you will meet' lists 'SAPI', 'KEV', 'Honeypot'.
- **low** The Questions page opens with a paragraph about a librarian and an email address before any question, and is 18.6 screens long, mostly a site catalogue I had no use for. ([questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/))'Kept by the librarian, librarian@php.newsroom: the catalogue: which page answers which question...'; instruments: 18.6 screens.

### What this reader would change, in order
- Move the reading tracker, £ meter and Research box below the article on phones (or collapse them into one line), so the thirty-second answer is the first thing on the first screen. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/), medium)Between meetings I have seconds; today I scroll past controls I never use before I learn whether to worry.
- Add two or three sentences on cost: what downtime has looked like for organisations so far (for example Weird Gloop's 13 hours) and what a breach would put at risk, with a link to the CFO briefing. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/), small)The headline asks 'what is it costing us' and the page never answers it.
- Add one line for organisations that sell online: shop platforms such as Magento and WordPress shops run on PHP, and a compromise could reach customer data and payment settings. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/), small)It would tell me in one sentence that my company is squarely in scope and why it matters to us.
- Rewrite 'What is still open' for a director: keep 'nobody confirmed hacked yet' and 'the fix may not be complete', drop the video and Fediverse details or move them to the journalist briefing. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/), small)The two open points that change my board questions are buried among forensics I cannot judge.
- On phones, turn the two impact tables into stacked cards (who, what happened, who says so, status) instead of six narrow columns. ([impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/), medium)The page is the evidence that offline is a precaution, but on my phone it is unreadable slivers.
- Replace the mod_php and x86_64 sentence at the end of the impact page with a plain version: nobody yet knows how many unpatched sites were actually broken into. ([impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/), small)It is the conclusion of the page and I could not follow it.
- Add a 'What to ask management' heading wording (instead of 'What to decide or do') and number the questions. ([briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/), small)Numbered questions are easier to read out in a meeting and to tick off as management answers.
- Put the questions first and move the librarian paragraph and the page catalogue to the bottom or another page. ([questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/), small)The useful short answers are hidden behind an introduction about how the site is run.

### Lines this reader reacted to
- [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/): *Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast.*This is what I came for. I could read this sentence aloud at the board meeting.
- [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/): *What is our evidence that we were not exploited between the leak on 20 October and our patch?*A good, pointed question I would not have thought to ask on my own.
- [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/): *Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.*I have no idea who Calif is or why this matters to my company; it lost me.
- [index.html](https://php.oct.2026.newsroom.sgit.ai/): *Phones and personal computers are not affected.*Useful straight away: it tells me this is about our servers, not our staff laptops.
- [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/): *it does not matter how well a website is written; if PHP underneath it is unpatched, it is in scope.*Clear and alarming in the right way: I cannot be told 'our code is fine' as an answer.
- [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/): *Taking a site offline is a decision an organisation makes, not evidence it was attacked.*Reassuring and worth repeating to colleagues who will see the headlines.
- [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/): *the reported cost of php2shell so far is the cost of precaution.*The single best line for a board: so far the damage is downtime, not breaches.
- [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/): *how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell.*Complete jargon. I gave up on this paragraph.
- [questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/): *Safer, not safe.*Three words I will use if someone tells me our firewall provider has it covered.

### Since the last run

First run: no previous review to compare against. Of the instruments' checks, the one that hurt me most was not on their list: the controls filling the first screen. The impact page's reading ease of 8.9 matched my experience at its end. Small tap targets (the breadcrumb and version badge) did not matter to me, as I never tapped them; the 11.84px text did not get in my way; page length mattered on the glossary and questions pages, which I skimmed rather than read.

Reviewer: agent-session.

## The journey

The pages in the order read: the start, the reader's path, then the links that matched its interests.

| # | Page | Why | Words | Screens | Reading ease | Glossary terms per 1000 words | Load (ms) | Low-contrast blocks | Small tap targets | Sideways scroll |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | start | 1948 | 13.5 | 56.6 | 12.3 | 894 | 0 | 23 of 168 |  |
| 2 | [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/) | reading path | 744 | 5.6 | 51.9 | 17.5 | 606 | 0 | 78 of 261 |  |
| 3 | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | reading path | 1338 | 9.4 | 64.1 | 17.9 | 595 | 0 | 8 of 76 |  |
| 4 | [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/) | reading path | 1166 | 9.4 | 8.9 | 12.0 | 731 | 0 | 8 of 77 |  |
| 5 | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | followed a link | 2990 | 20.2 | 60.9 | 36.8 | 787 | 0 | 8 of 95 |  |
| 6 | [questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/) | followed a link | 4056 | 18.6 | 51.9 | 18.7 | 731 | 0 | 28 of 200 |  |

## What the instruments flagged

Measurements, not verdicts: the review says which of them mattered to this reader.

| Severity | Page | Check | Evidence |
|---|---|---|---|
| medium | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | tap targets at least 24px | 23 of 168, e.g. v0.4.3, newsroom, 2026, October |
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | length fits the reader | 13.5 screens long on this device |
| medium | [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/) | tap targets at least 24px | 78 of 261, e.g. v0.4.3, newsroom, 2026, October |
| low | [briefings/board/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/board/) | text at least 12px | smallest 11.84px, 2 blocks below 12px |
| medium | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | tap targets at least 24px | 8 of 76, e.g. v0.4.3, newsroom, 2026, October |
| low | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | length fits the reader | 9.4 screens long on this device |
| medium | [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/) | tap targets at least 24px | 8 of 77, e.g. v0.4.3, newsroom, 2026, October |
| medium | [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/) | readable for a non-specialist | Flesch reading ease 8.9 (below 45 is hard) |
| low | [impact/index.html](https://php.oct.2026.newsroom.sgit.ai/impact/) | length fits the reader | 9.4 screens long on this device |
| medium | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | tap targets at least 24px | 8 of 95, e.g. v0.4.3, newsroom, 2026, October |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | length fits the reader | 20.2 screens long on this device |
| medium | [questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/) | tap targets at least 24px | 28 of 200, e.g. v0.4.3, newsroom, 2026, October |
| low | [questions/index.html](https://php.oct.2026.newsroom.sgit.ai/questions/) | length fits the reader | 18.6 screens long on this device |

## Everything this run saw

**Vault** `1zq458zk` · **read key** `sgit_public_read_f5578366fad746fe3273c3650bf76df06b1b69b157956ccf5a84e5ddb5ff73fb:1zq458zk` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_f5578366fad746fe3273c3650bf76df06b1b69b157956ccf5a84e5ddb5ff73fb%3A1zq458zk) · `sgit clone sgit_public_read_f5578366fad746fe3273c3650bf76df06b1b69b157956ccf5a84e5ddb5ff73fb:1zq458zk`

This run is in the folder `runs/2026-10-22T1753Z/`: the served and rendered HTML, the text and the screenshots of every page, every request and console message, and what the reviewer was given.


---
site v0.22.41 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/synthetic/board/2026-10-22T1753Z/index.html
