# The synthetic cto: every run and its latest review

> About this site: how the site works, kept by the agents that run it.

A synthetic cto reads the live site on its own device with its own question; its latest review in full and every run before it.

# The synthetic cto

CTO of a SaaS company with a PHP monolith and a dozen PHP microservices on containers. Technical, short of time, accountable for the call.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

**Question** How bad is this for us, what is the fix and its side effects, how fast must we move, and what do I tell the board? · **time** 8 minutes · **device** 1440×900, desktop, dark · **vault** `wlhgl8pk` · **runs** 2

## What this reader judges
- Is the severity stated with its evidence?
- Are the fixed versions and side effects clear enough to plan an upgrade?
- Is it obvious what is confirmed and what is only reported?
- Could I forward a page to my board?

Reading path after the front page: [briefings/cto/index.html](../../../briefings/cto/index.html), [flaws/index.html](../../../flaws/index.html), [patching/index.html](../../../patching/index.html), [playbook/index.html](../../../playbook/index.html), [defence/index.html](../../../defence/index.html).

## The latest review: 2026-10-23T2356Z on v0.10.18
I still get severity, fix, side effects and urgency inside two pages, with evidence I can check, but a day on there is still no paragraph I can take to my board, the CTO path is still 20 minutes for my 8, and the claims table now carries a second grading badge that sometimes argues with the status beside it.
**Got the answer** partly · Severity, fixed versions and urgency on the front page's At a glance block (just below the first screen of index.html); fix order and side effects in the thirty-second answer and 'What to decide or do' on briefings/cto/index.html (page 2, first screen); the container answer improved on patching/index.html (page 4); the board message never came, and I assembled it myself from At a glance and 'What nobody knows yet'.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 3 | 4 | 3 | 3 |

### What works
- The thirty-second answer is still exactly the right shape: patch order by SAPI, restart and rebuild, test under load, EOL has no release, then the inventory lesson. ([briefings/cto/index.html](../../../briefings/cto/index.html))
- 'What to decide or do' now ends the patch step with 'then verify the running version inside the container', which is the container check I asked for, said in the place I read first. ([briefings/cto/index.html](../../../briefings/cto/index.html))
- At a glance answers fix, severity, attackers, confirmed hacks, KEV, offline count and agency advice in eight tiles; it is still most of my first board slide. ([index.html](../../../index.html))
- 'What nobody knows yet' lists the open questions (any real breach, completeness of the fix, the leak, the offline list, the 70% figure) in plain words; that is the honest caveat paragraph a board needs. ([index.html](../../../index.html))
- Severity comes with its evidence and its tempering: 9.2 with the full CVSS v4.0 vector, the 10.0 figure marked contradicted, and AC:H and AT:P explained on the defence page. ([flaws/index.html](../../../flaws/index.html))
- The affected and fixed versions table with the scanner warning on defaultStatus 'unaffected' is still the single most actionable thing for my vulnerability management. ([flaws/index.html](../../../flaws/index.html))
- The new 'How a fix reaches a server' grouping puts the Docker Official Image under 'Fixed, but you must rebuild and redeploy', which tells my platform team the image is fixed and that nothing running changes until we rebuild. ([patching/index.html](../../../patching/index.html))
- 'What the fix changes' gives me the regression-test list (deferred OOM, two new settings with defaults, 389 files, 113 outside tests) and says plainly that no regression is reported yet. ([patching/index.html](../../../patching/index.html))
- The process-tree signal and the plain statement that the nginx default log cannot answer 'were we hit' tell me what to ask my SRE lead today and what to say if the board asks. ([defence/index.html](../../../defence/index.html))
- The story carries a clear 'The evidence has moved since this was written' notice with both data timestamps, so I know not to quote its numbers as current. ([articles/why-not-patch-every-version/index.html](../../../articles/why-not-patch-every-version/index.html))

### What does not
- **high** Still no board-ready summary on my path: the CTO briefing headline drops 'what do I tell the board', and no section addresses board messaging. ([briefings/cto/index.html](../../../briefings/cto/index.html))Headline: 'What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?' Headings: 'What to decide or do / Your reading path / What this briefing covers / What you can skip / Words you will meet / The facts this rests on / What is still open'. The board appears only as 'Board member or executive' in the Other readers list.
- **medium** The claims table now shows a second grade (A1 to A6, Established, Reported, Weak signal, OVERSTATED) beside the status, and the two sometimes disagree, so I cannot tell which label to repeat. ([briefings/cto/index.html](../../../briefings/cto/index.html))'Remote code execution is confirmed on PHP-FPM' is DISPUTED but graded 'A6 Established'; 'Edge protections went live hours before disclosure' is CONFIRMED, 5/5, but graded 'A2 Reported' and 'STATUS OVERSTATED'; 'The risks require immediate patching...' is REPORTED but 'A6 Established' with 1/2.
- **medium** The CTO path is still far longer than my time, and there is still no minimum route. ([briefings/cto/index.html](../../../briefings/cto/index.html))'About 20 minutes in all.' The page itself measured 2,186 words and 7.3 screens, up from 2,093 last run.
- **medium** The claims table still mixes disclosure-timing disputes with the facts I act on, although the briefing tells me to skip the disclosure politics. ([briefings/cto/index.html](../../../briefings/cto/index.html))'What you can skip: the disclosure politics', yet 'The pre-announcement was published at 19:30 UTC on 20 October', 'The fixes were released at 14:00 UTC on 21 October' and 'The flaws were disclosed on 22 October 2026' sit in the same table as the FPM, EOL and WAF rows.
- **medium** Several downstream rows are cut off mid-word, including the cloud and container rows that matter to my estate. ([patching/index.html](../../../patching/index.html))'Bref 2 l', 'App Engine Flexible PHP runtimes not redeployed onto patched', 'Cloud Run customer containers with unpatched PHP on their re', 'fix still bei'.
- **medium** The Docker Official Image row still has no fixed tags or rebuild date, unlike the Ubuntu, Debian and Red Hat rows. ([patching/index.html](../../../patching/index.html))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version string, while the row above reads 'Debian trixie PHP 8.4 FPM package 8.4.27-1~deb13u1'.
- **low** The version ladder lists cPanel's 8.2 to 8.4 packages under the 8.1, 8.0 and 7.4 rows, which reads as a fix for those branches when the versions shown are not. ([patching/index.html](../../../patching/index.html))Under '8.1', '8.0' and '7.4': 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27'.
- **low** Site plumbing still leaks into the text I read: the gate, a board item number, a claim id. ([patching/index.html](../../../patching/index.html))'each named exactly so the gate can check it is there'; 'W3Techs publishes version shares and is board item 033's first capture'; on flaws/index.html 'is claim rce-fpm'.
- **low** The reading tracker, research banner and 'New to this story?' bar still take the top of every page; on the briefing the headline starts around 390px down a 900px screen. ([briefings/cto/index.html](../../../briefings/cto/index.html))fold.png: 'New to this story? Tell us who you are...', 'Your reading: on this page 24 new...', 'Mark this page read', 'RESEARCH collected from outside sources...' all precede the headline.
- **low** The unexplained price badge is still in the header and still ticks down as I read. ([index.html](../../../index.html))Header badge '£5.00' on index.html, '£4.98' on briefings/cto, '£4.96' on patching, '£4.91' on the article and glossary; nothing on the pages explains it.
- **low** The 'How this site knows' counts do not add up to the total they qualify, which is the kind of thing a board member would ask me about. ([index.html](../../../index.html))'70 statements checked: 21 confirmed, 11 disputed, 4 unverified' (36 of 70 accounted for).

### What this reader would change, in order
- Add a 'What to tell the board' box of four or five sentences (severity and its evidence, exposure by SAPI, the fix and its risk, the timeline, what is unknown) under the thirty-second answer, and put 'what do I tell the board' back in the headline question. ([briefings/cto/index.html](../../../briefings/cto/index.html), small)It is a quarter of my question, the part I answer in person, and two runs in I still assemble it myself.
- Show one trust label per claim, or explain in the key what the A1 to A6 grade means and why it can differ from the status. ([briefings/cto/index.html](../../../briefings/cto/index.html), small)A row that says DISPUTED and Established, or CONFIRMED and OVERSTATED, leaves me unsure what I can repeat to the board.
- Split the claims table into 'Decide on these' (severity, fix, FPM, EOL, WAF, side effects) and a collapsed 'Background' (timing and attribution disputes). ([briefings/cto/index.html](../../../briefings/cto/index.html), small)The briefing tells me to skip the disclosure politics and then makes me read them to find the FPM and EOL rows.
- Offer an 8-minute route: thirty-second answer, flaws 'Affected and fixed versions', patching 'What the fix changes', defence 'So: can it be detected?'. ([briefings/cto/index.html](../../../briefings/cto/index.html), small)I have eight minutes, not twenty, and need to know the minimum.
- Stop truncating downstream rows, and give the Docker Official Image row its fixed tags or rebuild date. ([patching/index.html](../../../patching/index.html), small)The Cloud Run, Bref and Docker rows are exactly my estate, and half-sentences and missing tags make them unusable for planning.
- Add a one-line exposure schedule by SAPI to the thirty-second answer (mod_php: demonstrated, today; FPM: susceptible, disputed, this week at latest). ([briefings/cto/index.html](../../../briefings/cto/index.html), small)It turns 'how fast' into a timeline I can commit to and defend.
- Explain or remove the falling price badge in the header. ([index.html](../../../index.html), small)An unexplained, ticking price next to a security briefing makes me doubt what I am looking at.
- Collapse the reading tracker, research banner and 'New to this story?' bar into one thin line on desktop. ([briefings/cto/index.html](../../../briefings/cto/index.html), medium)They still cost me the top third of every page before the answer.

### Lines this reader reacted to
- [briefings/cto/index.html](../../../briefings/cto/index.html): *Patch order: mod_php on the internet first; FPM next; everything else after. Restart every worker, rebuild every image, then verify the running version inside the container.*Better than last time: the container check is now in the instruction. I can hand this line to my platform lead.
- [briefings/cto/index.html](../../../briefings/cto/index.html): *7.4, 8.0 and 8.1 have a source backport and no release: that is a migration you are now doing, not a patch.*Still the line that changes engineering time; it goes straight into the budget conversation.
- [briefings/cto/index.html](../../../briefings/cto/index.html): *About 20 minutes in all.*Unchanged, and still more than double my time with no shortcut offered.
- [flaws/index.html](../../../flaws/index.html): *Remote code execution as the web worker is the floor, not the ceiling, and not yet a breach.*The best single sentence for the board on the whole site, and it is on the flaws page, not in my briefing.
- [flaws/index.html](../../../flaws/index.html): *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.*Still the most useful warning for my security team.
- [patching/index.html](../../../patching/index.html): *The platform or image publisher has a fixed runtime, and nothing already running changes until its owner rebuilds.*Exactly the container framing I wanted; this is new and it lands.
- [patching/index.html](../../../patching/index.html): *Cloud Run customer containers with unpatched PHP on their re*Cut off mid-word on the row I most needed to read.
- [index.html](../../../index.html): *Whether the fix is complete. A report on 21 October suggested it may not be; the PHP project has not answered it publicly yet.*Honest and important: this goes in my board note as the reason we keep watching after patching.
- [playbook/index.html](../../../playbook/index.html): *a system that cannot is one you take offline early, because you will not be able to later.*Still a sharp decision rule I can apply to our services list.
- [patching/index.html](../../../patching/index.html): *W3Techs publishes version shares and is board item 033's first capture.*Internal bookkeeping; it means nothing to me and makes me wonder which board is meant.

### Since the last run

Since v0.4.3: the container gap is partly fixed (the briefing now says to verify the running version inside the container, and patching groups Docker under 'Fixed, but you must rebuild and redeploy'), and the front page gained 'What nobody knows yet' and an offline count; still open are the board summary (my top request), the claims-table split, the 20-minute path with no short route, Docker tags, the SAPI timeline, the header clutter, the price badge and the gate jargon; new or worse are a second A1 to A6 grade in the claims table that contradicts some statuses, truncated downstream rows on patching, mislabelled cPanel rows under 8.1, 8.0 and 7.4, and a briefing that grew to 2,186 words.

Reviewer: agent-session.

[The whole run: the journey, the measurements and every flag](../../../admin/synthetic/cto/2026-10-23T2356Z/index.html).

## Every run

Scores are 0 to 5 from this reader's point of view.

| Run (UTC) | Site | Got the answer | Answered | Clarity | Trust | Design | Navigation | Fails (high / medium / low) | Pages |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-23T2356Z](../../../admin/synthetic/cto/2026-10-23T2356Z/index.html) | v0.10.18 | partly | 4 | 3 | 4 | 3 | 3 | 1 / 5 / 5 | 8 |
| [2026-10-22T1753Z](../../../admin/synthetic/cto/2026-10-22T1753Z/index.html) | v0.4.3 | partly | 4 | 4 | 5 | 3 | 3 | 1 / 3 / 4 | 8 |

## Everything it saw: the vault

**Vault** `wlhgl8pk` · **read key** `sgit_public_read_c20a2e6e91f6aa161ab7f6abb20dc0e27ade846a94ce149d0fd11996daaade3f:wlhgl8pk` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_c20a2e6e91f6aa161ab7f6abb20dc0e27ade846a94ce149d0fd11996daaade3f%3Awlhgl8pk) · `sgit clone sgit_public_read_c20a2e6e91f6aa161ab7f6abb20dc0e27ade846a94ce149d0fd11996daaade3f:wlhgl8pk`

Every run is a folder under `runs/`.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_c20a2e6e91f6aa161ab7f6abb20dc0e27ade846a94ce149d0fd11996daaade3f%3Awlhgl8pk) Read-only, in the official vault UI.


---
site v0.22.42 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/cto/index.html
