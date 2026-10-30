# Synthetic readers: what they said about each page

> About this site: how the site works, kept by the agents that run it.

Every page of the site named in the synthetic readers' latest reviews, with what fails, what to change, what works and the lines they reacted to, from all six readers.

# What the synthetic readers said, page by page

Every page of this site that a synthetic reader named in its latest review, with what does not work, what to change, what works and the lines it reacted to, from all six readers at once. Pages are ordered by how much the readers found wrong with them: a high-severity failure counts five, a medium two, a low one, a requested change one.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

## The pages

| Page | Readers | Fails (high) | Changes asked | Works |
|---|---|---|---|---|
| [index.html](#index-html) | 6 | 14 (1) | 9 | 10 |
| [patching/index.html](#patching-index-html) | 3 | 11 (2) | 5 | 4 |
| [briefings/board/index.html](#briefings-board-index-html) | 1 | 7 (2) | 6 | 2 |
| [claims/index.html](#claims-index-html) | 2 | 5 (2) | 4 | 3 |
| [briefings/cto/index.html](#briefings-cto-index-html) | 1 | 5 (1) | 6 | 2 |
| [briefings/pm/index.html](#briefings-pm-index-html) | 1 | 5 (2) | 4 | 3 |
| [exploitation/index.html](#exploitation-index-html) | 1 | 4 (2) | 3 | 2 |
| [briefings/developer/index.html](#briefings-developer-index-html) | 1 | 1 (1) | 1 | 1 |
| [briefings/everyone/index.html](#briefings-everyone-index-html) | 1 | 1 (1) | 1 | 1 |
| [impact/index.html](#impact-index-html) | 1 | 2 (0) | 1 | 1 |
| [playbook/index.html](#playbook-index-html) | 2 | 2 (0) | 2 | 2 |
| [timeline/index.html](#timeline-index-html) | 1 | 1 (1) | 0 | 0 |
| [code/index.html](#code-index-html) | 1 | 3 (0) | 1 | 1 |
| [glossary/index.html](#glossary-index-html) | 2 | 2 (0) | 1 | 0 |
| [flaws/index.html](#flaws-index-html) | 2 | 1 (0) | 1 | 6 |
| [sources/index.html](#sources-index-html) | 1 | 2 (0) | 0 | 0 |
| [status.json](#status-json) | 1 | 1 (0) | 1 | 1 |
| [defence/index.html](#defence-index-html) | 2 | 1 (0) | 1 | 3 |
| [questions/index.html](#questions-index-html) | 1 | 1 (0) | 1 | 1 |
| [start/index.html](#start-index-html) | 1 | 2 (0) | 0 | 0 |
| [articles/index.html](#articles-index-html) | 1 | 1 (0) | 0 | 1 |
| [llms.txt](#llms-txt) | 1 | 1 (0) | 0 | 0 |
| [admin/versions.html](#admin-versions-html) | 1 | 0 (0) | 0 | 0 |
| [agencies/index.html](#agencies-index-html) | 1 | 0 (0) | 0 | 1 |
| [articles/why-not-patch-every-version/index.html](#articles-why-not-patch-every-version-index-html) | 1 | 0 (0) | 0 | 1 |
| [briefings/security/index.html](#briefings-security-index-html) | 1 | 0 (0) | 0 | 1 |
| [explained/index.html](#explained-index-html) | 2 | 0 (0) | 0 | 3 |
| [questions/old-php/index.html](#questions-old-php-index-html) | 1 | 0 (0) | 0 | 1 |
| [review/index.html](#review-index-html) | 1 | 0 (0) | 0 | 1 |

## [index.html](../../../index.html)

6 of 6 readers: Board member, CTO, Designer, Developer, Project manager, Security lead

### What does not work
- **low** The unexplained price badge is still in the header and still ticks down as I read. ([CTO](../../../admin/synthetic/cto/index.html))Header badge '£5.00' on index.html, '£4.98' on briefings/cto, '£4.96' on patching, '£4.91' on the article and glossary; nothing on the pages explains it.
- **low** The 'How this site knows' counts do not add up to the total they qualify, which is the kind of thing a board member would ask me about. ([CTO](../../../admin/synthetic/cto/index.html))'70 statements checked: 21 confirmed, 11 disputed, 4 unverified' (36 of 70 accounted for).
- **low** The unexplained money-like badge is still in the header and still falls as I move between pages. ([Project manager](../../../admin/synthetic/pm/index.html))fold.png: '£5.00' on the front page, '£4.97' on the PM briefing, '£4.95' on the playbook, '£4.94' on patching, '£4.91' on the old-PHP question.
- **medium** A front-page core fact cites sources that do not support its key words. ([Security lead](../../../admin/synthetic/security/index.html))'CONFIRMED Attackers are trying, in large numbers. ... CISA CISA'. The volume comes from Cloudflare's CEO (REPORTED, 1/1 on claims/index.html); CISA's own line is 'CISA has not observed exploitation'.
- **medium** The front page tally and legend still do not match the claims page. ([Security lead](../../../admin/synthetic/security/index.html))index.html: '70 statements checked: 21 confirmed, 11 disputed, 4 unverified' and a four-word legend without CONTRADICTED. claims/index.html: '70 claims: 21 confirmed, 34 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **low** The unlabelled price pill in the header still changes from page to page. ([Security lead](../../../admin/synthetic/security/index.html))Header pill reads '£4.99' on index.html, '£4.98' on briefings/security, '£4.97' on exploitation, '£4.92' on the Log4j source page and the glossary, with no label.
- **medium** The 'still open' lists say PHP has not answered the incomplete-fix report, but the site's own release notes say it did, on 22 October. ([Developer](../../../admin/synthetic/developer/index.html))index.html: 'Whether the fix is complete. A report on 21 October suggested it may not be; the PHP project has not answered it publicly yet.' briefings/developer/index.html: 'Nothing from PHP on the list yet.' admin/versions.html v0.5.8: 'the PHP security team answered the 'incomplete fix' report publicly at 09:11 UTC on 22 October ... so the front page's 'not answered publicly yet' is out of date'.
- **high** An unlabelled money figure still sits in the masthead and still falls as I move from page to page; it reads as a charge and is the biggest trust risk for a newcomer. ([Designer](../../../admin/synthetic/designer/index.html))Desktop pill: '£5.00' on index.html, '£4.99' on start, '£4.96' on briefings/everyone, '£4.95' on claims, glossary and articles, '£4.94' on explained. Phone: '£5.00', '£4.98', '£4.97'. Tablet front page: '£4.99'. No visible label anywhere.
- **medium** Desktop navigation still wraps at 1440px; the orphaned 'About' is now a whole second row ('STORIES Views Stories | SITE About'), which still looks unfinished. ([Designer](../../../admin/synthetic/designer/index.html))fold.png on all seven pages: row one ends at 'GRC', row two starts at y=139 with 'STORIES'.
- **medium** The 'Your reading' panel with fade / hide / show is still the first block on every page, ahead of the headline, and means nothing on a first visit. ([Designer](../../../admin/synthetic/designer/index.html))First fold text on all seven pages: 'Your reading: on this page 9 new, 0 changed, 0 read; across the site 429 new and 0 changed of 429. ... Read items: fade hide show'.
- **low** The new 'New to this story?' strip, the one element written for a newcomer, does not appear on the front page where newcomers land, only on inner pages where it adds to the stack. ([Designer](../../../admin/synthetic/designer/index.html))Present on briefings/everyone, claims, glossary, articles and explained fold.png; absent from index.html fold.png and fold-phone.png.
- **low** Front-page counts still do not match the claims page, and the front-page legend still has four status words to the claims page's five. ([Designer](../../../admin/synthetic/designer/index.html))index.html: '70 statements checked: 21 confirmed, 11 disputed, 4 unverified'; claims: '21 confirmed, 34 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **low** On tablet the masthead buttons are spread edge to edge with large gaps, so Ask, Feedback, the theme switch and the pound pill read as unrelated scattered objects. ([Designer](../../../admin/synthetic/designer/index.html))fold-tablet.png: 'Ask' at the far left, 'Feedback' about a third across, 'Newsprint' two thirds across, '£4.99' at the far right, with 'Menu' alone on the row above.
- **low** On the desktop front page the 'briefing for you' grid is very uneven: the 'I make the decisions' column stacks five cards while neighbouring columns hold one or two, leaving large empty areas. ([Designer](../../../admin/synthetic/designer/index.html))full.jpg, 'The briefing for you' section: columns of 2, 6, 2, 4 and 2 cards in five columns.

### What to change
- Explain or remove the falling price badge in the header. ([CTO](../../../admin/synthetic/cto/index.html), small)An unexplained, ticking price next to a security briefing makes me doubt what I am looking at.
- Add a dated 'Changed since yesterday' block at the top of the front page and the PM briefing, and bring 'Latest' and the timeline up to 23 October or say plainly that nothing new has happened since 22 October 08:40. ([Project manager](../../../admin/synthetic/pm/index.html), medium)My daily routine is 'what moved since yesterday'; a 'Latest' list a day old with a header saying 'last checked today' leaves me unsure whether I have missed something.
- Cite Cloudflare, not CISA, for 'in large numbers' in the front-page core fact, and grade that part REPORTED. ([Security lead](../../../admin/synthetic/security/index.html), small)A board member will check the first fact first, and CISA says the opposite of 'large numbers'.
- Bring the front-page tally and legend in line with the claims page (five statuses: 34 reported, 8 disputed, 3 contradicted). ([Security lead](../../../admin/synthetic/security/index.html), small)The first numbers I see should match the later ones.
- Update the 'still open' item on the incomplete fix with PHP's public answer of 22 October, as the v0.5.8 notes already say. ([Developer](../../../admin/synthetic/developer/index.html), small)When the release notes say a page is out of date and the page is unchanged, I start doubting the rest.
- Label the pound pill in the masthead (for example 'Reading credit: £4.95, free') or move it into the account menu. ([Designer](../../../admin/synthetic/designer/index.html), small)An unexplained, falling money figure is still the single biggest trust risk for a newcomer, and it has now survived six releases.
- Fit the desktop navigation on one row at 1440px, for example by moving STORIES and SITE into the masthead row beside Ask and Feedback. ([Designer](../../../admin/synthetic/designer/index.html), small)The wrapped second row makes every page look slightly broken at the main desktop size.
- Show the 'New to this story?' strip on the front page and hide the 'Your reading' panel until the reader has marked something read. ([Designer](../../../admin/synthetic/designer/index.html), small)The newcomer hint is missing where newcomers arrive, while the tracker shows noise to the same people.
- Align the front-page 'How this site knows' counts and status legend with the claims page's five statuses, including reported and contradicted. ([Designer](../../../admin/synthetic/designer/index.html), small)Two summaries of the same 70 claims disagree on the front page and the claims page, which a sceptical reader will notice.

### What works, so do not break it
- The opening paragraph of the front page is plain and right: what PHP is, a fix exists, agencies say install it, phones and personal computers are not affected. ([Board member](../../../admin/synthetic/board/index.html))
- The 'At a glance' tiles now include 'WEBSITES TAKEN OFFLINE: 10 organisations, reported, as a precaution' beside 'ANYONE CONFIRMED HACKED? Not yet', which tells me in seconds the damage so far is downtime, not break-ins. ([Board member](../../../admin/synthetic/board/index.html))
- The status words (confirmed, reported, unverified) and a source under every fact mean I am not repeating a rumour to the board. ([Board member](../../../admin/synthetic/board/index.html))
- At a glance answers fix, severity, attackers, confirmed hacks, KEV, offline count and agency advice in eight tiles; it is still most of my first board slide. ([CTO](../../../admin/synthetic/cto/index.html))
- 'What nobody knows yet' lists the open questions (any real breach, completeness of the fix, the leak, the offline list, the 70% figure) in plain words; that is the honest caveat paragraph a board needs. ([CTO](../../../admin/synthetic/cto/index.html))
- The 'At a glance' tiles answer the client questions I get asked first (is there a fix, how serious, anyone hacked, on the US 'used in attacks' list) in one screen. ([Project manager](../../../admin/synthetic/pm/index.html))
- Times are in UTC throughout and the header says when the site was last checked, so the currency of each figure is unambiguous. ([Project manager](../../../admin/synthetic/pm/index.html))
- The front page CONFIRMED count now matches the claims page (21 on both). ([Security lead](../../../admin/synthetic/security/index.html))
- The front page hierarchy on desktop is still unmistakable: a large serif headline, a sans-serif standfirst ending on 'Phones and personal computers are not affected', and one filled teal call to action beside four outlined ones. ([Designer](../../../admin/synthetic/designer/index.html))
- The 'Right now' cards with a red left rule and grey source chips still make every sentence look sourced at a glance; on tablet they read especially well at full width. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *Phones and personal computers are not affected.* ([Board member](../../../admin/synthetic/board/index.html))Useful straight away: this is about our servers, not staff laptops.
- *Whether the fix is complete. A report on 21 October suggested it may not be; the PHP project has not answered it publicly yet.* ([CTO](../../../admin/synthetic/cto/index.html))Honest and important: this goes in my board note as the reason we keep watching after patching.
- *70 statements checked: 21 confirmed, 11 disputed, 4 unverified* ([Security lead](../../../admin/synthetic/security/index.html))The confirmed count now matches; the rest still does not add up against the claims page.
- *Your reading: on this page 9 new, 0 changed, 0 read; across the site 429 new and 0 changed of 429.* ([Designer](../../../admin/synthetic/designer/index.html))Still the first words on the page, before the headline, and still noise to a first-time visitor.
- *Phones and personal computers are not affected.* ([Designer](../../../admin/synthetic/designer/index.html))Still the right reassurance in the right place, last in a large standfirst.

## [patching/index.html](../../../patching/index.html)

3 of 6 readers: CTO, Developer, Project manager

### What does not work
- **medium** Several downstream rows are cut off mid-word, including the cloud and container rows that matter to my estate. ([CTO](../../../admin/synthetic/cto/index.html))'Bref 2 l', 'App Engine Flexible PHP runtimes not redeployed onto patched', 'Cloud Run customer containers with unpatched PHP on their re', 'fix still bei'.
- **medium** The Docker Official Image row still has no fixed tags or rebuild date, unlike the Ubuntu, Debian and Red Hat rows. ([CTO](../../../admin/synthetic/cto/index.html))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version string, while the row above reads 'Debian trixie PHP 8.4 FPM package 8.4.27-1~deb13u1'.
- **low** The version ladder lists cPanel's 8.2 to 8.4 packages under the 8.1, 8.0 and 7.4 rows, which reads as a fix for those branches when the versions shown are not. ([CTO](../../../admin/synthetic/cto/index.html))Under '8.1', '8.0' and '7.4': 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27'.
- **low** Site plumbing still leaks into the text I read: the gate, a board item number, a claim id. ([CTO](../../../admin/synthetic/cto/index.html))'each named exactly so the gate can check it is there'; 'W3Techs publishes version shares and is board item 033's first capture'; on flaws/index.html 'is claim rce-fpm'.
- **medium** The cPanel row under 7.4, 8.0 and 8.1 still shows only 8.2, 8.3 and 8.4 packages, contradicting the text that cPanel backported to those versions. This is the row I most need for agency client sites. ([Project manager](../../../admin/synthetic/pm/index.html))Under 7.4: 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27' against 'cPanel backported to 7.4, 8.0 and 8.1'.
- **medium** The patching page opens with commit hashes and 'the gate' before the plain grouping by hosting type that I actually need. ([Project manager](../../../admin/synthetic/pm/index.html))'each named exactly so the gate can check it is there and has the status quoted'; Flesch 34.4 from the instruments.
- **high** php -v gives the wrong answer on the backports the site itself marks fixed: an Ubuntu Noble box reports 8.3.6, below 8.3.36. ([Developer](../../../admin/synthetic/developer/index.html))'fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13' against the briefing's 'Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35'. Same for Jammy 8.1.2 and Focal 7.4.3.
- **high** The Docker Official Image row, the one I most need, still has no tags, versions, rebuild date or digests. ([Developer](../../../admin/synthetic/developer/index.html))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version text, on the ladder and again under 'Fixed, but you must rebuild and redeploy', while Debian, Red Hat, Heroku and Bref rows carry versions.
- **medium** The patching and affected pages are frozen at an old inventory commit while the site says it has read a much newer one, so I do not know which figures to cite. ([Developer](../../../admin/synthetic/developer/index.html))patching/index.html: '46 fixed · 206 still affected · 418 under investigation · 3 not affected, of 674 products ... at commit cca173c64ec5 (22 October, 08:40 UTC)'. The front page says 'the NCSC-NL inventory, latest change read 23 October 2026, 12:50 UTC'; admin/versions.html v0.10.4 says '109 of 751 products fixed'; v0.4.3's correction 'had 675 rows at the captured commit, not 674' is still not applied on patching, affected or llms.txt.
- **medium** The cPanel row under 8.1, 8.0 and 7.4 still lists only 8.2 to 8.4 packages, and the page's prose now contradicts the row. ([Developer](../../../admin/synthetic/developer/index.html))Row: 'cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27'. Prose: 'cPanel backported to 7.4, 8.0 and 8.1'.
- **low** Downstream rows are still cut off mid-word. ([Developer](../../../admin/synthetic/developer/index.html))'Bref 3: php-85:21, php-84:24, php-83:24, php-82:26; Bref 2 l', 'Cloud Run customer containers with unpatched PHP on their re', 'patched distribution/Sury pac', 'fix still bei'.

### What to change
- Stop truncating downstream rows, and give the Docker Official Image row its fixed tags or rebuild date. ([CTO](../../../admin/synthetic/cto/index.html), small)The Cloud Run, Bref and Docker rows are exactly my estate, and half-sentences and missing tags make them unusable for planning.
- Fix or explain the cPanel row under the 7.4, 8.0 and 8.1 branches so the package names match the claim that cPanel backported to those versions. ([Project manager](../../../admin/synthetic/pm/index.html), small)Agency client sites are mostly on panels; I need to know which clients wait on cPanel and which on Plesk.
- Give the Docker Official Image row the fixed tags per variant (cli, fpm, apache, alpine) and the rebuild date. ([Developer](../../../admin/synthetic/developer/index.html), small)I build on php:*-fpm and php:*-apache; without tags I cannot check my Dockerfiles or pinned digests.
- Move patching and affected to the inventory commit the front page says it has read (751 products), or say on each page why they stay on cca173c64ec5, and fix 674 versus 675. ([Developer](../../../admin/synthetic/developer/index.html), small)Three different inventory sizes across the site make me unsure which number to cite.
- Fix the cPanel row placement and truncated product text, and list data/patching.json and data/review.json in llms.txt with .md links in the twins. ([Developer](../../../admin/synthetic/developer/index.html), small)A row under 8.1 listing only 8.2 to 8.4 packages makes me doubt the ladder, and tools should be able to stay in markdown and JSON.

### What works, so do not break it
- The new 'How a fix reaches a server' grouping puts the Docker Official Image under 'Fixed, but you must rebuild and redeploy', which tells my platform team the image is fixed and that nothing running changes until we rebuild. ([CTO](../../../admin/synthetic/cto/index.html))
- 'What the fix changes' gives me the regression-test list (deferred OOM, two new settings with defaults, 389 files, 113 outside tests) and says plainly that no regression is reported yet. ([CTO](../../../admin/synthetic/cto/index.html))
- 'How a fix reaches a server' (patched for you, rebuild and redeploy, OS update, extended support, hosting panel, waiting on supplier) lets me sort client sites into workstreams by hosting type. ([Project manager](../../../admin/synthetic/pm/index.html))
- 'What the fix changes' warns about the delayed OOM, memory_hard_limit_percent and max_multipart_body_parts. That is what I need to warn QA about. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *The platform or image publisher has a fixed runtime, and nothing already running changes until its owner rebuilds.* ([CTO](../../../admin/synthetic/cto/index.html))Exactly the container framing I wanted; this is new and it lands.
- *Cloud Run customer containers with unpatched PHP on their re* ([CTO](../../../admin/synthetic/cto/index.html))Cut off mid-word on the row I most needed to read.
- *W3Techs publishes version shares and is board item 033's first capture.* ([CTO](../../../admin/synthetic/cto/index.html))Internal bookkeeping; it means nothing to me and makes me wonder which board is meant.
- *each named exactly so the gate can check it is there and has the status quoted* ([Project manager](../../../admin/synthetic/pm/index.html))I still do not know what 'the gate' is and do not need to in order to plan.
- *fixed Docker Official Images maintainers: Docker Official Image: php* ([Developer](../../../admin/synthetic/developer/index.html))Fixed which tags? Still the row where I needed detail and got none.
- *46 fixed · 206 still affected · 418 under investigation · 3 not affected, of 674 products in the NCSC-NL inventory at commit cca173c64ec5* ([Developer](../../../admin/synthetic/developer/index.html))The release notes say 675 at this commit and 751 now; this page says neither.

## [briefings/board/index.html](../../../briefings/board/index.html)

1 of 6 readers: Board member

### What does not work
- **high** The first screen on a phone is still site machinery, not the story. On my briefing the answer only starts at the very bottom edge of the first screen. ([Board member](../../../admin/synthetic/board/index.html))fold.png: version badge, Ask/Feedback buttons, '£4.98' meter, 'New to this story?' banner, 'Your reading: on this page 35 new, 0 changed, 0 read', 'Mark this page read', 'Mark everything read', 'Read items: fade hide show', the RESEARCH box and a four-line kicker all come before 'THE ANSWER IN THIRTY SECONDS', which is cut off at the bottom of the screen. Same block on every page I visited.
- **high** The briefing has not been touched since my last review: still 'This briefing v7 written in site v0.5.9 on 22 October', though the site is now v0.10.18. None of my requested changes to it were made. ([Board member](../../../admin/synthetic/board/index.html))Header reads 'This briefing v7 ... v0.5.9 on 22 October 2026 · history and changes, 6 earlier'; the text of every section is identical to the previous run.
- **medium** The headline promises 'what is it costing us' and the page still never answers it; no downtime or breach cost, and the CFO briefing is only one name in a list at the bottom. ([Board member](../../../admin/synthetic/board/index.html))Only cost wording is 'what it costs to find out' and 'If not, that is the first spend.' 'CFO' appears only under 'Other readers'.
- **medium** Nothing speaks to a business that sells online. The briefing never mentions shops, card data or customer accounts; the only shop reference is a single phrase in the impact table. ([Board member](../../../admin/synthetic/board/index.html))Impact table row 'French government services; the University of Geneva; the BBC; online shops'. The Questions page lists Magento among affected platforms; the board briefing does not.
- **medium** 'What is still open' is still written for a journalist: deleted videos, Fediverse and oss-security mean nothing to a director. ([Board member](../../../admin/synthetic/board/index.html))'Whether the deleted Calif video is the one now embedded on Calif's own write-up.' and 'A Fediverse report of a third bug or incomplete fix reached oss-security on 21 October; PHP reportedly told Canonical it is unrelated.'
- **medium** The briefing's status line is a day old while the page header says it was checked today, so I cannot tell if 'nobody hacked' is still true this morning. ([Board member](../../../admin/synthetic/board/index.html))Header 'last checked 23 October 2026, 12:50 UTC' against the answer's 'As of the evening of 22 October, no named organisation has said it was broken into'.
- **low** 'Words you will meet' still lists terms the same briefing tells me to skip. ([Board member](../../../admin/synthetic/board/index.html))'What you can skip: SAPIs and settings' while 'Words you will meet' lists 'SAPI', 'KEV', 'Honeypot'.

### What to change
- On phones, collapse the reading tracker, £ meter and Research box into one line or move them below the article, so 'THE ANSWER IN THIRTY SECONDS' is fully on the first screen. ([Board member](../../../admin/synthetic/board/index.html), medium)Between meetings I have seconds, and two runs in a row I have scrolled past controls I never use before learning whether to worry.
- Add one line for organisations that sell online: shop platforms such as Magento and WordPress shops run on PHP, and a compromise could reach customer accounts and payment settings. ([Board member](../../../admin/synthetic/board/index.html), small)It would tell me in one sentence that my company is in scope and why it matters to us.
- Add two or three sentences on cost: so far it is downtime (for example Weird Gloop's 13 hours, councils and government sites pulled), what a breach would put at risk, and a direct link to the CFO briefing. ([Board member](../../../admin/synthetic/board/index.html), small)The headline asks 'what is it costing us' and the page never answers.
- Refresh the thirty-second answer to today's check time, or say 'still true as of 23 October' beside it. ([Board member](../../../admin/synthetic/board/index.html), small)I need to know the reassurance is current before I repeat it to the board.
- Rewrite 'What is still open' for a director: keep 'nobody confirmed hacked yet' and 'the fix may not be complete', move the video, Fediverse and leak details to the journalist briefing. ([Board member](../../../admin/synthetic/board/index.html), small)The two open points that change my questions are buried among forensics I cannot judge.
- Rename 'What to decide or do' to 'What to ask management' and number the five questions. ([Board member](../../../admin/synthetic/board/index.html), small)Numbered questions are easier to read out in a meeting and tick off as management answers.

### What works, so do not break it
- The thirty-second answer is still exactly the right shape for a director: what happened, what agencies say, nobody confirmed broken into, and three questions to ask. ([Board member](../../../admin/synthetic/board/index.html))
- 'What to decide or do' remains a ready-made list of board questions (inventory including vendor products, patched and restarted and checked, who can pull a system and has it been rehearsed, what a compromise would reach, evidence we were not hit). Do not lose it. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast.* ([Board member](../../../admin/synthetic/board/index.html))Still what I came for. I could read this aloud at the board meeting.
- *Who is authorised to take a system offline, how long does it take, and has it been rehearsed?* ([Board member](../../../admin/synthetic/board/index.html))Exactly the governance question a board should own; 'rehearsed' is the word that will make management squirm.
- *Whether the deleted Calif video is the one now embedded on Calif's own write-up. Calif's page does not mention the leak.* ([Board member](../../../admin/synthetic/board/index.html))Still no idea who Calif is or why this matters to my company; it lost me again.

## [claims/index.html](../../../claims/index.html)

2 of 6 readers: Designer, Security lead

### What does not work
- **high** The new FACT-CHECK column contradicts the STATUS column on the same row, and the status is not corrected, so I now have two grades and no rule for which one to cite. ([Security lead](../../../admin/synthetic/security/index.html))Weird Gloop: 'CONFIRMED' next to 'A2 Reported ... STATUS OVERSTATED 1/1'. Edge protections: 'CONFIRMED' next to 'A2 Reported STATUS OVERSTATED'. NCSC-NL count: 'CONFIRMED' next to 'A1 Weak signal ... CONTRADICTED STATUS OVERSTATED'. The A1 to A6 scale is defined neither on the page nor in the glossary.
- **high** CONFIRMED is still used for one-source items, against the site's own definition. ([Security lead](../../../admin/synthetic/security/index.html))Legend: 'CONFIRMED two or more primary sources agree, or the fact was counted from a captured file'. Rows: CISA offline advice 'CONFIRMED ... 1/1', Latvia restrictions 'CONFIRMED ... 1/1', Weird Gloop 'CONFIRMED ... 1/1'. exploitation/index.html: CCCS, CERT.LV, ACSC and the CISA ADP row each 'CONFIRMED (PRIMARY)' on one source.
- **low** A status change is justified partly by asking chatbots, which I cannot cite to a CISO. ([Security lead](../../../admin/synthetic/security/index.html))'Changed from "confirmed" on 22 October at the editor's request (fact-check run 1 had marked it overstated; Perplexity and ChatGPT, asked by the editor, said the same).'
- **medium** On the claims table two trust scales sit side by side and disagree visually: a full six-dot green 'A6 Established' badge next to a DISPUTED status. ([Designer](../../../admin/synthetic/designer/index.html))'Remote code execution is confirmed on PHP-FPM ... DISPUTED A6 Established ●●●●●●' and 'A web application firewall may provide some protection ... DISPUTED A6 Established ●●●●●●'; an UNVERIFIED row shows 'A1 Weak signal ●○○○○○ OPINION DISPUTED'. Nothing in the five-word legend explains the FACT-CHECK column.
- **medium** Glyph-only row controls still fail the tap-target check, worst on the page where readers most need to tap sources. ([Designer](../../../admin/synthetic/designer/index.html))155 of 453 targets under 24px on claims at phone width (147 last time); tap examples include '○', '⋯', '×' and 'FACT-CHECK'; the phone theme switcher is still a lone dot with no label.

### What to change
- Where the fact-check column says STATUS OVERSTATED, change the status (or remove the flag), and define the A1 to A6 scale in the legend and the glossary. ([Security lead](../../../admin/synthetic/security/index.html), medium)Two grades that disagree on one row leave me unable to cite either.
- Re-run the status rule so one-source primary items are REPORTED (or add a named 'single primary' grade), and use one grade per claim on every page, starting with CERT.LV. ([Security lead](../../../admin/synthetic/security/index.html), medium)The grading must keep its own definition before I can put it in front of the CISO.
- Explain the FACT-CHECK column in the legend above the table, or hide the Established dots on DISPUTED and UNVERIFIED rows so the two scales cannot look opposed. ([Designer](../../../admin/synthetic/designer/index.html), small)A full green six-dot badge beside a DISPUTED label reads as a contradiction to anyone scanning the table.
- Give the '○' and '⋯' row controls, the '×' close button and the phone theme switch a 24px minimum hit area, and give the theme switch a text label on phone. ([Designer](../../../admin/synthetic/designer/index.html), small)155 undersized targets on the page where readers most need to tap sources.

### What works, so do not break it
- The 'no named organisation has said it was compromised' claim is now REPORTED, time-bounded to 20:50 UTC on 22 October, and its note lists the near-misses (GMO, Czech Technical University, the Valtec retraction) with capture paths. That is the honest framing I need. ([Security lead](../../../admin/synthetic/security/index.html))
- Dark mode remains a real theme: the teal brightens to mint, the status badges keep their meaning, and the instruments found 0 low-contrast pairs in dark on all seven pages. ([Designer](../../../admin/synthetic/designer/index.html))
- New 'IN PLAIN ENGLISH' panel at the top of the claims page, in a distinct pale blue box, tells a newcomer in one sentence what the dense table is for before the 21.4 reading-ease paragraph begins. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim.* ([Security lead](../../../admin/synthetic/security/index.html))This is the line my CISO will ask about, and I found it in a claim note, not on the exploitation page.
- *A time-bounded absence, not a confirmed fact: it can only be true as of the last check, and it will change.* ([Security lead](../../../admin/synthetic/security/index.html))Exactly how I want 'no confirmed victim' worded. I will use it.
- *Perplexity and ChatGPT, asked by the editor, said the same* ([Security lead](../../../admin/synthetic/security/index.html))Not evidence. I cannot tell a CISO a grade changed because two chatbots agreed.
- *IN PLAIN ENGLISH Every statement made about the story, who made it, and how far it can be trusted, with links to the evidence.* ([Designer](../../../admin/synthetic/designer/index.html))New and exactly right: one sentence, in its own box, before the dense paragraph. This is the pattern the other technical pages should copy.
- *The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.* ([Designer](../../../admin/synthetic/designer/index.html))Still internal vocabulary ('the build', 'the manifest') in the first paragraph a newcomer reads, though the new plain-English box above it softens the blow.

## [briefings/cto/index.html](../../../briefings/cto/index.html)

1 of 6 readers: CTO

### What does not work
- **high** Still no board-ready summary on my path: the CTO briefing headline drops 'what do I tell the board', and no section addresses board messaging. ([CTO](../../../admin/synthetic/cto/index.html))Headline: 'What does this cost us in engineering time, what breaks when we patch, and what do we change so the next one is a non-event?' Headings: 'What to decide or do / Your reading path / What this briefing covers / What you can skip / Words you will meet / The facts this rests on / What is still open'. The board appears only as 'Board member or executive' in the Other readers list.
- **medium** The claims table now shows a second grade (A1 to A6, Established, Reported, Weak signal, OVERSTATED) beside the status, and the two sometimes disagree, so I cannot tell which label to repeat. ([CTO](../../../admin/synthetic/cto/index.html))'Remote code execution is confirmed on PHP-FPM' is DISPUTED but graded 'A6 Established'; 'Edge protections went live hours before disclosure' is CONFIRMED, 5/5, but graded 'A2 Reported' and 'STATUS OVERSTATED'; 'The risks require immediate patching...' is REPORTED but 'A6 Established' with 1/2.
- **medium** The CTO path is still far longer than my time, and there is still no minimum route. ([CTO](../../../admin/synthetic/cto/index.html))'About 20 minutes in all.' The page itself measured 2,186 words and 7.3 screens, up from 2,093 last run.
- **medium** The claims table still mixes disclosure-timing disputes with the facts I act on, although the briefing tells me to skip the disclosure politics. ([CTO](../../../admin/synthetic/cto/index.html))'What you can skip: the disclosure politics', yet 'The pre-announcement was published at 19:30 UTC on 20 October', 'The fixes were released at 14:00 UTC on 21 October' and 'The flaws were disclosed on 22 October 2026' sit in the same table as the FPM, EOL and WAF rows.
- **low** The reading tracker, research banner and 'New to this story?' bar still take the top of every page; on the briefing the headline starts around 390px down a 900px screen. ([CTO](../../../admin/synthetic/cto/index.html))fold.png: 'New to this story? Tell us who you are...', 'Your reading: on this page 24 new...', 'Mark this page read', 'RESEARCH collected from outside sources...' all precede the headline.

### What to change
- Add a 'What to tell the board' box of four or five sentences (severity and its evidence, exposure by SAPI, the fix and its risk, the timeline, what is unknown) under the thirty-second answer, and put 'what do I tell the board' back in the headline question. ([CTO](../../../admin/synthetic/cto/index.html), small)It is a quarter of my question, the part I answer in person, and two runs in I still assemble it myself.
- Show one trust label per claim, or explain in the key what the A1 to A6 grade means and why it can differ from the status. ([CTO](../../../admin/synthetic/cto/index.html), small)A row that says DISPUTED and Established, or CONFIRMED and OVERSTATED, leaves me unsure what I can repeat to the board.
- Split the claims table into 'Decide on these' (severity, fix, FPM, EOL, WAF, side effects) and a collapsed 'Background' (timing and attribution disputes). ([CTO](../../../admin/synthetic/cto/index.html), small)The briefing tells me to skip the disclosure politics and then makes me read them to find the FPM and EOL rows.
- Offer an 8-minute route: thirty-second answer, flaws 'Affected and fixed versions', patching 'What the fix changes', defence 'So: can it be detected?'. ([CTO](../../../admin/synthetic/cto/index.html), small)I have eight minutes, not twenty, and need to know the minimum.
- Add a one-line exposure schedule by SAPI to the thirty-second answer (mod_php: demonstrated, today; FPM: susceptible, disputed, this week at latest). ([CTO](../../../admin/synthetic/cto/index.html), small)It turns 'how fast' into a timeline I can commit to and defend.
- Collapse the reading tracker, research banner and 'New to this story?' bar into one thin line on desktop. ([CTO](../../../admin/synthetic/cto/index.html), medium)They still cost me the top third of every page before the answer.

### What works, so do not break it
- The thirty-second answer is still exactly the right shape: patch order by SAPI, restart and rebuild, test under load, EOL has no release, then the inventory lesson. ([CTO](../../../admin/synthetic/cto/index.html))
- 'What to decide or do' now ends the patch step with 'then verify the running version inside the container', which is the container check I asked for, said in the place I read first. ([CTO](../../../admin/synthetic/cto/index.html))

### Lines readers reacted to
- *Patch order: mod_php on the internet first; FPM next; everything else after. Restart every worker, rebuild every image, then verify the running version inside the container.* ([CTO](../../../admin/synthetic/cto/index.html))Better than last time: the container check is now in the instruction. I can hand this line to my platform lead.
- *7.4, 8.0 and 8.1 have a source backport and no release: that is a migration you are now doing, not a patch.* ([CTO](../../../admin/synthetic/cto/index.html))Still the line that changes engineering time; it goes straight into the budget conversation.
- *About 20 minutes in all.* ([CTO](../../../admin/synthetic/cto/index.html))Unchanged, and still more than double my time with no shortcut offered.

## [briefings/pm/index.html](../../../briefings/pm/index.html)

1 of 6 readers: Project manager

### What does not work
- **high** Still no deadline anywhere. The guidance says 'now', 'this week' and 'the next fortnight' and never states whether any agency set a due date or what a sensible internal target is, so I cannot put a hard date on the plan. ([Project manager](../../../admin/synthetic/pm/index.html))'Expect unplanned work this week' and 'Keep a slot free in the next fortnight'; the playbook steps carry no dates; the front page says the flaws are 'Not yet' on the US list but not what that means for a due date.
- **high** Still nothing on how to report progress, although the briefing's own heading asks 'what do I tell stakeholders'. No status template, no measures, no wording for a client update. ([Project manager](../../../admin/synthetic/pm/index.html))'What this briefing covers' lists 'what to tell stakeholders about downtime', but the body only says 'Agree with stakeholders now who can make that call, how long it may last, and what users see meanwhile.'
- **medium** The PM briefing is now five site versions behind the site I am reading and does not say whether its advice still holds against 23 October's data. ([Project manager](../../../admin/synthetic/pm/index.html))'This briefing v5 written in site v0.5.9 on 22 October 2026' while the header badge reads 'v0.10.18'.
- **low** The reading path says the timeline takes 1 minute, but it is 8.2 screens of 68 rows, so my time budget is wrong. ([Project manager](../../../admin/synthetic/pm/index.html))'Timeline 1 min' in 'Your reading path'; instruments: timeline 2137 words, 8.2 screens.
- **low** The navigation has grown and still wraps to two lines at my width, and a new 'New to this story?' strip adds another band before the content; the briefing headline starts about 390px down. ([Project manager](../../../admin/synthetic/pm/index.html))fold.png at 1280x800: menu runs UPDATES, FOR YOU, RESEARCH on line one and STORIES, SITE on line two; then the 'New to this story?' strip, the reading bar and the research banner.

### What to change
- Add a 'Deadlines' line at the top of the PM briefing stating whether any agency set a due date (and that the flaws are not on CISA's KEV list, so there is no federal due date yet), plus a recommended internal target such as internet-facing sites patched within N days. ([Project manager](../../../admin/synthetic/pm/index.html), small)I plan against dates; 'this week' and 'next fortnight' cannot go into a programme plan or a client conversation.
- Add a 'How to report progress' section with a copyable status table (system, owner, PHP version, hosting route, patched, running version verified, offline, next date) and a two-line stakeholder update template. ([Project manager](../../../admin/synthetic/pm/index.html), medium)Reporting is half my question and the briefing's own title promises it; with forty clients I need one consistent format.
- Re-check the PM briefing against the current data and show 'still holds as of' with today's date, or update it. ([Project manager](../../../admin/synthetic/pm/index.html), small)A briefing written five versions ago makes me doubt whether the order of work or the 'second round' warning has moved on.
- Make the six PM actions a copyable or downloadable checklist with tick boxes. ([Project manager](../../../admin/synthetic/pm/index.html), small)I would drop it straight into our tracker for each client.

### What works, so do not break it
- The thirty-second answer is still the stand-up summary I need: unplanned work this week, possible downtime, 8.1 and older is a migration, ask each owner for a patch date and a test plan. ([Project manager](../../../admin/synthetic/pm/index.html))
- 'What to decide or do' is six actions in a sensible order that map straight onto a plan: get the list, a date per system, regression budget, downtime decision, migration project, second round. ([Project manager](../../../admin/synthetic/pm/index.html))
- The datacentre-move framing (inventory, owner, date, test) gives me a planning shape I can explain to forty clients. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *Ask each system owner for a patch date and a test plan.* ([Project manager](../../../admin/synthetic/pm/index.html))Still exactly the instruction I need; it goes straight into my email to client leads.
- *Plan for it the way you would plan for a datacentre move: an inventory, an owner per system, a date, a test.* ([Project manager](../../../admin/synthetic/pm/index.html))Landed again. A plan shape I already know how to run.
- *Expect a second round. A report that the first fix may be incomplete is open. Keep a slot free in the next fortnight.* ([Project manager](../../../admin/synthetic/pm/index.html))Useful, but 'next fortnight' is too loose to schedule, and I cannot tell if this is still the position a day later.
- *This briefing v5 written in site v0.5.9 on 22 October 2026* ([Project manager](../../../admin/synthetic/pm/index.html))The site is on v0.10.18; is my briefing out of date?

## [exploitation/index.html](../../../exploitation/index.html)

1 of 6 readers: Security lead

### What does not work
- **high** Two vendors reporting successful exploitation, and a confirmed GMO break-in of undetermined cause, are only in a claim note; the exploitation page, which is the page I rely on for this question, does not mention them and still says it has 20 signals. ([Security lead](../../../admin/synthetic/security/index.html))claims/index.html: 'two security vendors, Hadrian and Patchstack, report successful exploitation without naming any victim' and 'GMO confirmed a break-in on 20 October on its FX trading VPS service'. exploitation/index.html is 'This page v5 written in site v0.3.2 on 22 October 2026' and has no Hadrian, Patchstack, GMO or Czech Technical University row.
- **high** The Amazon self-contradiction is unchanged. ([Security lead](../../../admin/synthetic/security/index.html))Woodward row: 'REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found'. claims/index.html grades the same claim 'CONFIRMED' with 'confirmed by both companies' own posts', and sources/index.html lists the captured 'Amazon (CJ Moses, AWS Security Blog) · vendor · primary · CAPTURED · ... aws-security-blog-madpot'.
- **medium** CERT.LV still carries different grades on different pages. ([Security lead](../../../admin/synthetic/security/index.html))exploitation/index.html: 'Automated exploitation attempts seen in Latvia; no reports of successful attacks. attempts CONFIRMED (PRIMARY)'. claims/index.html and briefings/security/index.html: 'Automated exploitation attempts were seen in Latvia; none succeeded ... REPORTED'.
- **medium** The same Amazon honeypot event is still counted twice in the headline signal count. ([Security lead](../../../admin/synthetic/security/index.html))'What the captured sources carry is 20 signals', with the first two rows both '2026-10-17 ... One exploit attempt against a MadPot honeypot', once from the AWS blog and once 'via The Hacker News'.

### What to change
- Add Hadrian, Patchstack, GMO and Czech Technical University rows to the exploitation table with KIND and status, and put the 'vendors report successful exploitation, no victim named' line on the front page 'Anyone confirmed hacked?' tile. ([Security lead](../../../admin/synthetic/security/index.html), small)This is the most important change in the exploitation picture since yesterday and the page I cite for it does not show it.
- Fix the Woodward row to say Amazon's own post was captured and link aws-security-blog-madpot. ([Security lead](../../../admin/synthetic/security/index.html), small)Still the clearest self-contradiction on the exploitation question.
- Make the signal count '20 rows, 19 events' or merge the two Amazon 17 October rows. ([Security lead](../../../admin/synthetic/security/index.html), small)Double counting undermines a page whose value is careful counting.

### What works, so do not break it
- Attempts, honeypot hits, negative findings and second-hand claims are still kept apart in the KIND column, which is the distinction I have to make upwards. ([Security lead](../../../admin/synthetic/security/index.html))
- The KEV negative finding is still dated to catalog version, release time, fetch time and entry count, and called a point-in-time finding. Citable as written. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *A remote code execution bug is not an invisibility cloak.* ([Security lead](../../../admin/synthetic/security/index.html))Still the right framing, but the page that says it has not been updated since 22 October.
- *REPORTED Cloudflare's own post confirms attack traffic, Amazon's own post not found* ([Security lead](../../../admin/synthetic/security/index.html))Unchanged since yesterday and still contradicted by the claims and sources pages.

## [briefings/developer/index.html](../../../briefings/developer/index.html)

1 of 6 readers: Developer

### What does not work
- **high** There is still no real verification step for container images or backports: one sentence about php -v, no docker run command, no version-independent check, nothing for distro builds. ([Developer](../../../admin/synthetic/developer/index.html))The only instruction is still 'Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.' llms.txt's am-i-affected answer adds 'without a distribution backport' but never says how to tell.

### What to change
- Add a 'Verify your image' block with copy-paste commands: docker run --rm  php -v, a version-independent check such as php -r 'var_dump(ini_get("max_multipart_body_parts"));' if the site can confirm only patched builds have it, and the distro changelog or package-version check for backports. ([Developer](../../../admin/synthetic/developer/index.html), medium)This half of my question is still unanswered, and php -v alone gives the wrong result on the Ubuntu backports the site lists as fixed.

### What works, so do not break it
- The thirty-second answer still does the right job for a developer: the flaw is in the C engine, ini_set, .user.ini and auto_prepend_file run too late, check the running version after the restart. It stops me wasting time on code-side fixes. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Nothing in userland blocks the demonstrated paths: ini_set() runs too late, .user.ini runs too late, auto_prepend_file runs too late.* ([Developer](../../../admin/synthetic/developer/index.html))Still exactly what I need first; it kills the idea of a code-side hotfix.
- *Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.* ([Developer](../../../admin/synthetic/developer/index.html))Word for word what it said last time. Right instinct, still not enough for images or backports.

## [briefings/everyone/index.html](../../../briefings/everyone/index.html)

1 of 6 readers: Designer

### What does not work
- **high** On a phone the chrome still fills most of the first screen, and on inner pages it has got worse: masthead, a four-button row, the new 'New to this story?' strip, the 'Your reading' panel and the RESEARCH or ABOUT band all come before the headline. ([Designer](../../../admin/synthetic/designer/index.html))Phone h1 top: 550px on index.html, 590px on claims, 594px on explained, 652px on briefings/everyone, in an 812px screen. On briefings/everyone fold-phone.png the thirty-second answer box only starts at the bottom edge, exactly as last time.

### What to change
- On phone, merge the 'New to this story?' strip, the 'Your reading' panel and the RESEARCH or ABOUT band into one collapsed line below the h1 and standfirst. ([Designer](../../../admin/synthetic/designer/index.html), medium)The headline and the thirty-second answer are the things to read first and on a phone they start at 652px of 812px.

### What works, so do not break it
- The boxed thirty-second answer with Alex's avatar and the single 'Read the site as Alex' button is still the clearest hand-hold for a newcomer on the site. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *You do not need to know anything about computers to follow this.* ([Designer](../../../admin/synthetic/designer/index.html))Lands well under the answer box; on a phone it is below the first screen.

## [impact/index.html](../../../impact/index.html)

1 of 6 readers: Board member

### What does not work
- **medium** The impact tables are still six narrow columns on a phone, so each row is a tall stack of two or three words and the page runs to 9.5 screens. ([Board member](../../../admin/synthetic/board/index.html))full.jpg shows 'Taken offline' with WHO, WHAT HAPPENED, WHEN, WHO SAYS SO, STATUS, SOURCES each a sliver wide; instruments: 9.5 screens, reading ease 8.7.
- **medium** The impact page's conclusion still ends in jargon I cannot get past. ([Board member](../../../admin/synthetic/board/index.html))'how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell'.

### What to change
- On phones, show the impact tables as stacked cards (who, what happened, who says so, status) and replace the mod_php sentence with 'nobody yet knows how many unpatched sites were actually broken into'. ([Board member](../../../admin/synthetic/board/index.html), medium)This page is my evidence that offline was a precaution, but on a phone it is slivers and ends in jargon.

### What works, so do not break it
- The blue 'IN PLAIN ENGLISH' box at the top of the impact page is visible on the first screen on my phone and gives me the page's point in one sentence. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *the reported cost of php2shell so far is the cost of precaution.* ([Board member](../../../admin/synthetic/board/index.html))The best line for a board, and it belongs in my briefing, not only here.
- *A quiet log is not a clean host.* ([Board member](../../../admin/synthetic/board/index.html))Plain and memorable; it tells me not to accept 'we saw nothing' as proof.
- *how many were mod_php on x86_64 with default limits, reachable without a WAF, and how many of those show a worker spawning a shell.* ([Board member](../../../admin/synthetic/board/index.html))Still complete jargon. I gave up on this paragraph again.

## [playbook/index.html](../../../playbook/index.html)

2 of 6 readers: CTO, Project manager

### What does not work
- **medium** The playbook steps still have no owner or role, so I have to work out which steps are mine, the client's, the host's or the developer's. ([Project manager](../../../admin/synthetic/pm/index.html))Step 2 is a string of settings ('memory_limit=-1 ... pm.max_requests=1 on FPM') with no 'who'; no step names a role.
- **low** The sentence on where 'offline' sits in the order is unchanged and still loses me. ([Project manager](../../../admin/synthetic/pm/index.html))'Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.'

### What to change
- Add a 'Who does this' label to each playbook step (inventory owner, host or platform, developer, security, decision-maker). ([Project manager](../../../admin/synthetic/pm/index.html), small)Lets me turn the steps straight into assigned tasks instead of translating each one.
- Rewrite the playbook's opening sentence on 'offline' as one plain line, for example 'Most agencies put taking a site offline last; CERT-EU, Canada and France put isolation earlier.' ([Project manager](../../../admin/synthetic/pm/index.html), small)The order is what I am planning, and I had to read this sentence three times on two visits.

### What works, so do not break it
- New 'In plain English' line at the top of the playbook tells me in one sentence what the page is for before the detail starts. ([Project manager](../../../admin/synthetic/pm/index.html))
- Numbered steps 0 to 6 with the agencies behind each step shown as chips, so every line of my plan has a citable source. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *a system that cannot is one you take offline early, because you will not be able to later.* ([CTO](../../../admin/synthetic/cto/index.html))Still a sharp decision rule I can apply to our services list.
- *Decide who can make that call and how fast it can be executed, and write it down before you need it.* ([Project manager](../../../admin/synthetic/pm/index.html))Good: a governance action I own.
- *Taking a system offline is the last step on every list, and the one list where it comes earlier is the one that says isolate, then migrate.* ([Project manager](../../../admin/synthetic/pm/index.html))Still lost me. Is offline early or late?

## [timeline/index.html](../../../timeline/index.html)

1 of 6 readers: Project manager

### What does not work
- **high** I cannot tell what changed since yesterday. On 23 October the front page's 'Latest' and the timeline both stop at 22 October 08:40 UTC, while the header says last checked 23 October 12:50 UTC, and the reading bar shows everything as new. ([Project manager](../../../admin/synthetic/pm/index.html))Last timeline row '2026-10-22 08:40:58 UTC NCSC-NL merges pull request 10'; plain-English line says 'from a 2024 audit to this morning'; page 'written in site v0.3.1 on 22 October 2026'; 'on this page 68 new, 0 changed, 0 read; across the site 429 new and 0 changed of 429'.

### Lines readers reacted to
- *Everything that happened, in order, from a 2024 audit to this morning, each line tied to the page that says so.* ([Project manager](../../../admin/synthetic/pm/index.html))Promises 'this morning', but the last row is yesterday at 08:40 UTC.

## [code/index.html](../../../code/index.html)

1 of 6 readers: Developer

### What does not work
- **low** The hunks are still called verbatim but contain elisions, and the code block has no diff colouring, so the removed bailout and the added lines look the same in dark mode. ([Developer](../../../admin/synthetic/developer/index.html))'the hunks below are verbatim' followed by 'bool *did_gc ...)', '{ ... }' and bare '...' lines; the block is a plain
 with no add or delete classes, and full.jpg shows uniform white monospace. - **low** The commit hash links to the site's own source page, not to the upstream php-src commit. ([Developer](../../../admin/synthetic/developer/index.html))The only link for 3584a98 is '../sources/github-php-src-fix-commit-3584a98bd/index.html'. - **low** About 360px of site chrome sits above the H1 on technical pages at 1440x900. ([Developer](../../../admin/synthetic/developer/index.html))metrics.json: H1 'The code: where the bug is, and what the fix does' at top 360; fold.png shows the two-row nav, the explainer banner, the reading bar and the research strip before it. ### What to change - Mark the elisions in the hunks or drop 'verbatim', colour + and - lines, and link the hash to the upstream php-src commit. ([Developer](../../../admin/synthetic/developer/index.html), small)I want to grep and diff these myself, and in dark mode removed and added lines blur together. ### What works, so do not break it - Full commit hash, parent, authors, merge times into each branch, a step-by-step before and after, readable C hunks, and the 7.4 backport's different _exit strategy with its 17 files listed. I can go and diff this myself. ([Developer](../../../admin/synthetic/developer/index.html)) ### Lines readers reacted to - *Each step names the function or file it comes from; the hunks below are verbatim.* ([Developer](../../../admin/synthetic/developer/index.html))And the hunks still contain '...'. Small, but it is the kind of claim I check. ## [glossary/index.html](../../../glossary/index.html) 2 of 6 readers: Board member, Designer

### What does not work
- **low** The glossary is labelled as being about how the site works rather than about the story, which made me wonder if I had left the briefing. ([Board member](../../../admin/synthetic/board/index.html))fold.png box 'ABOUT THIS SITE how the site works, kept by the agents that run it' above 'Glossary: every term, in plain English'.
- **medium** Section labels still contradict each other: the band, the kicker and the highlighted menu item name different parts of the site. ([Designer](../../../admin/synthetic/designer/index.html))glossary: band 'ABOUT THIS SITE', kicker 'START HERE', menu 'Start here'. explained: band 'RESEARCH', kicker 'START HERE'. articles: menu now highlights 'Stories' but the band still says 'ABOUT THIS SITE', under the sentence 'Every page on the site says at its top which half it belongs to.'

### What to change
- Drive the band, the kicker and the highlighted menu item from one field, so glossary and explained name one section and the Stories page says STORIES in its band. ([Designer](../../../admin/synthetic/designer/index.html), small)The site promises each page says which half it belongs to, and three of my seven pages visibly break that promise.

## [flaws/index.html](../../../flaws/index.html)

2 of 6 readers: CTO, Developer

### What does not work
- **medium** The SAPI table still has no row for long-running workers (Octane on Swoole or RoadRunner), where cross-request stale state should worry a Laravel team most. ([Developer](../../../admin/synthetic/developer/index.html))SAPI rows: Apache mod_php, PHP-FPM, php-cgi, FrankenPHP, LiteSpeed (LSAPI), CLI/cron/queue workers. Nothing for Swoole or RoadRunner, not even 'not covered'.

### What to change
- Add Swoole, RoadRunner and Octane worker rows to the SAPI table, saying 'not covered by the primary sources' if that is the truth. ([Developer](../../../admin/synthetic/developer/index.html), small)Long-running workers are where cross-request stale state should worry a Laravel team, and silence reads as 'not affected'.

### What works, so do not break it
- Severity comes with its evidence and its tempering: 9.2 with the full CVSS v4.0 vector, the 10.0 figure marked contradicted, and AC:H and AT:P explained on the defence page. ([CTO](../../../admin/synthetic/cto/index.html))
- The affected and fixed versions table with the scanner warning on defaultStatus 'unaffected' is still the single most actionable thing for my vulnerability management. ([CTO](../../../admin/synthetic/cto/index.html))
- Each CVE has its GHSA ID, full CVSS 4.0 vector, CWEs, exact timestamps and the record's description verbatim, kept apart from what was demonstrated and what the fix does. ([Developer](../../../admin/synthetic/developer/index.html))
- The SAPI table shows the FPM disagreement between the GitHub advisory and the Foundation instead of smoothing it over, and says CLI parsing untrusted input is 'not covered either way by the primary sources'. That is the honesty I want. ([Developer](../../../admin/synthetic/developer/index.html))
- The warning that the CVE records default to 'unaffected' and list only 8.2 to 8.5, so scanners will clear 7.4 to 8.1. Still the most practically useful sentence for anyone with a scanner in CI. ([Developer](../../../admin/synthetic/developer/index.html))
- The mitigations table puts each setting beside its own caveat and where it must be set (php_admin_value, pool, php.ini), including the RLIMIT_AS warning and pm.max_requests=1. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Remote code execution as the web worker is the floor, not the ceiling, and not yet a breach.* ([CTO](../../../admin/synthetic/cto/index.html))The best single sentence for the board on the whole site, and it is on the flaws page, not in my briefing.
- *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.* ([CTO](../../../admin/synthetic/cto/index.html))Still the most useful warning for my security team.
- *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.* ([Developer](../../../admin/synthetic/developer/index.html))Still the sentence that would have saved me in CI.

## [sources/index.html](../../../sources/index.html)

1 of 6 readers: Security lead

### What does not work
- **medium** The banner still promises a saved copy behind every fact while the captures are private. ([Security lead](../../../admin/synthetic/security/index.html))Banner on every page: 'every fact links to a saved copy of its source'. sources/index.html: 'The captures are third-party pages held privately and are not republished'.
- **low** A 404 page is still listed as a captured primary source, and the Log4j source page still has no claim or event. ([Security lead](../../../admin/synthetic/security/index.html))'Page Not Found | CISA ... primary · CAPTURED ... HTTP 404'. sources/cisa-alert-log4j-2021/index.html: 'No claim cites this source yet.' (it now adds 'Comparator for the context page.')

## [status.json](../../../status.json)

1 of 6 readers: Developer

### What does not work
- **medium** status.json still has no machine-readable affected ranges or fixed versions and does not link data/affected.json, so a CI step cannot gate on it. ([Developer](../../../admin/synthetic/developer/index.html))Versions appear only in prose in headline_facts[0].text; links holds front, sources, claims, stories, releases, llms and nothing for affected or patching.

### What to change
- Add affected_ranges and fixed_versions per branch to status.json and link data/affected.json and data/patching.json from its links block. ([Developer](../../../admin/synthetic/developer/index.html), small)Then a CI step or an LLM tool can gate on the data instead of parsing a prose headline.

### What works, so do not break it
- status.json now carries the CVE IDs, data_as_of and the vault commit, so a tool can at least tell how fresh it is; the flaws markdown twin still renders clean tables and a backticked CVSS vector. ([Developer](../../../admin/synthetic/developer/index.html))

## [defence/index.html](../../../defence/index.html)

2 of 6 readers: CTO, Security lead

### What does not work
- **low** The malformed Fortinet signature ID is unchanged. ([Security lead](../../../admin/synthetic/security/index.html))'Three FortiGuard signatures (090502648, 090502651, 09052654)': the third has eight digits, the others nine.

### What to change
- Correct the third Fortinet signature ID, label or remove the £ pill, and reword the banner to 'links to its source and a hash of the saved copy'. ([Security lead](../../../admin/synthetic/security/index.html), small)I paste IDs into tickets, and unexplained numbers and promises the practice does not keep erode trust.

### What works, so do not break it
- The process-tree signal and the plain statement that the nginx default log cannot answer 'were we hit' tell me what to ask my SRE lead today and what to say if the board asks. ([CTO](../../../admin/synthetic/cto/index.html))
- Host signals by layer with literal strings ('in Unknown on line 0', 'exit signal Segmentation fault (11)') and the 'What the log cannot show' row remain directly usable for SOC alerting. ([Security lead](../../../admin/synthetic/security/index.html))
- The WAF table keeps each vendor's own caveat beside its rule, including Fortinet's alert-only default and Fastly's must-enable rule. ([Security lead](../../../admin/synthetic/security/index.html))

### Lines readers reacted to
- *with the known exploits no application code runs, so a shell from a worker is the exploit* ([Security lead](../../../admin/synthetic/security/index.html))Still the most actionable sentence on the site.

## [questions/index.html](../../../questions/index.html)

1 of 6 readers: Board member

### What does not work
- **low** The Questions page still opens with the librarian and an email address, and has grown from 18.6 to 21.7 screens, mostly a site catalogue of internal pages (telemetry, vaults, pack mode, team chat) of no use to me. ([Board member](../../../admin/synthetic/board/index.html))fold.png ends on 'Kept by the librarian, librarian@php.newsroom: the catalogue...' with no question visible; catalogue includes 'Pack mode, measured on the source watch' and 'How the team talks: three vaults and one run' listed three times.

### What to change
- Put the questions table first and move the librarian paragraph and the whole site catalogue to another page. ([Board member](../../../admin/synthetic/board/index.html), small)The useful short answers are hidden behind an introduction and a 20-screen list of internal pages.

### What works, so do not break it
- Short, pasteable answers to 'Should we take our site offline?' and 'We are behind Cloudflare... Are we safe?' are the two questions I expect in the boardroom. ([Board member](../../../admin/synthetic/board/index.html))

### Lines readers reacted to
- *Safer, not safe.* ([Board member](../../../admin/synthetic/board/index.html))Three words I will use if someone says our firewall provider has it covered.

## [start/index.html](../../../start/index.html)

1 of 6 readers: Designer

### What does not work
- **low** A plain-English persona is told to expect deeply technical words. ([Designer](../../../admin/synthetic/designer/index.html))Casey, website owner, marked 'Plain English'; 'Words they will meet' includes 'mod_php', 'Out of memory (OOM)' and 'longjmp'.
- **low** Smallest text is still just under 12px on five of seven pages, mostly the faint version lines. ([Designer](../../../admin/synthetic/designer/index.html))min_font_px 11.84 with 17 blocks below 12px on start (16 last time).

### Lines readers reacted to
- *Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.* ([Designer](../../../admin/synthetic/designer/index.html))Clear instruction, and the map with its dot scale delivers on it.

## [articles/index.html](../../../articles/index.html)

1 of 6 readers: Designer

### What does not work
- **low** Build provenance still clutters reader-level cards and section footers, and is now visibly far behind the masthead version. ([Designer](../../../admin/synthetic/designer/index.html))'House · Journalist · 2026-10-23 · claude-journalist · site v0.10.1 · vault commit f3c5db0d9873 · data as of 2026-10-23T01:20Z'; front-page footers say 'This section v1 written in site v0.3.2' under a masthead pill 'v0.10.18'.

### What works, so do not break it
- The Stories menu item is now highlighted on the Stories page, so the menu at least agrees with the page title. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *Every page on the site says at its top which half it belongs to.* ([Designer](../../../admin/synthetic/designer/index.html))Still a good promise, still broken by the band directly above it, which says ABOUT THIS SITE.

## [llms.txt](../../../llms.txt)

1 of 6 readers: Developer

### What does not work
- **low** llms.txt's Data list still omits the files the pages cite, and the markdown twin's links still point to HTML, so a tool walking markdown falls back to HTML. ([Developer](../../../admin/synthetic/developer/index.html))patching/index.html cites 'data/patching.json', review/index.html cites 'data/review.json'; neither is under '## Data'. flaws/index.md links '../sources/cve-cve-2026-109618/index.html'. llms.txt is also now 150 KB and 727 lines, much of it team, GRC and design-mockup pages a tool asking about the bug does not need.

## [admin/versions.html](../../../admin/versions.html)

1 of 6 readers: Developer

### Lines readers reacted to
- *so the front page's 'not answered publicly yet' is out of date* ([Developer](../../../admin/synthetic/developer/index.html))The site knows its front page is wrong and the front page still says it a day later.

## [agencies/index.html](../../../agencies/index.html)

1 of 6 readers: Security lead

### What works, so do not break it
- Verbatim offline advice per agency, the two blocked agencies recorded, and the BBC's NCSC quote shown not to be on the captured NCSC page. ([Security lead](../../../admin/synthetic/security/index.html))

## [articles/why-not-patch-every-version/index.html](../../../articles/why-not-patch-every-version/index.html)

1 of 6 readers: CTO

### What works, so do not break it
- The story carries a clear 'The evidence has moved since this was written' notice with both data timestamps, so I know not to quote its numbers as current. ([CTO](../../../admin/synthetic/cto/index.html))

## [briefings/security/index.html](../../../briefings/security/index.html)

1 of 6 readers: Security lead

### What works, so do not break it
- The thirty-second answer and 'What to decide or do' list is still a usable runbook skeleton. ([Security lead](../../../admin/synthetic/security/index.html))

## [explained/index.html](../../../explained/index.html)

2 of 6 readers: Board member, Designer

### What works, so do not break it
- The kitchen analogy and the 'What that can reach' list (database passwords, other systems that trust this server) still make the risk concrete for a non-technical reader. ([Board member](../../../admin/synthetic/board/index.html))
- The status legend is now five coloured badges (CONFIRMED green, REPORTED blue, DISPUTED and CONTRADICTED amber, UNVERIFIED red), each defined once, and the same five appear in 'How to read this site' on the explainer. ([Designer](../../../admin/synthetic/designer/index.html))
- No horizontal overflow at phone, tablet or desktop on any page, no images without alt text, and the explainer's diagrams ('A NORMAL VISIT', 'THE ATTACK') are built as text boxes, so they scale and stay readable. ([Designer](../../../admin/synthetic/designer/index.html))

### Lines readers reacted to
- *it does not matter how well a website is written; if PHP underneath it is unpatched, it is in scope.* ([Board member](../../../admin/synthetic/board/index.html))Clear and alarming in the right way: 'our code is fine' is not an answer I should accept.
- *Words in the dotted underline are explained when you hover or tap them.* ([Designer](../../../admin/synthetic/designer/index.html))Good and consistently applied; the underlined words remain small tap targets on a phone.

## [questions/old-php/index.html](../../../questions/old-php/index.html)

1 of 6 readers: Project manager

### What works, so do not break it
- A short, pasteable answer with a URL for the 'we are on 7.4' question that I can forward to a client as is. ([Project manager](../../../admin/synthetic/pm/index.html))

### Lines readers reacted to
- *To paste back where it was asked: the paragraph above and https://php.oct.2026.newsroom.sgit.ai/questions/old-php/index.html* ([Project manager](../../../admin/synthetic/pm/index.html))Very handy; I can send this to the clients still on 7.4 as is.

## [review/index.html](../../../review/index.html)

1 of 6 readers: Developer

### What works, so do not break it
- The review page states the code layer comes from git show -U0 by a parser, never a model, with per-file added and removed counts. A provenance claim I can check. ([Developer](../../../admin/synthetic/developer/index.html))

### Lines readers reacted to
- *Never a model, so it cannot invent a function that is not in the diff.* ([Developer](../../../admin/synthetic/developer/index.html))The right provenance claim for a code map, and one I can check against git show.


---
site v0.22.54 · data as of 2026-10-29T17:13Z · vault commit cd9375f1aefd · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/pages/index.html
