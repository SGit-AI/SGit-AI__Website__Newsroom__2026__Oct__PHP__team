# The synthetic designer: every run and its latest review

> About this site: how the site works, kept by the agents that run it.

A synthetic designer reads the live site on its own device with its own question; its latest review in full and every run before it.

# The synthetic designer

Product and content designer. Judges hierarchy, typography, layout, consistency, accessibility and whether the site guides a newcomer. Checks phone, tablet and desktop, light and dark.

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [All six readers](../index.html).

**Question** Does the site look and feel trustworthy, does it guide a newcomer, and does it work on every screen for every reader? · **time** 10 minutes · **device** 1440×900, desktop, light (also phone, tablet, dark) · **vault** `dpdx3q13` · **runs** 2

## What this reader judges
- Is the visual hierarchy clear: what is the one thing to read first?
- Is type legible and are tap targets big enough on a phone?
- Is the site consistent from page to page?
- Are there accessibility failures (contrast, alt text, focus, overflow)?

Reading path after the front page: [start/index.html](../../../start/index.html), [briefings/everyone/index.html](../../../briefings/everyone/index.html), [claims/index.html](../../../claims/index.html), [glossary/index.html](../../../glossary/index.html), [articles/index.html](../../../articles/index.html).

## The latest review: 2026-10-23T2358Z on v0.10.18
The site still looks calm, sourced and trustworthy, and the claims page is clearer than it was, but almost none of my structural complaints from v0.4.3 were touched: the unlabelled pound pill still ticks down, two utility boxes (now three, with the new newcomer strip) still sit above every headline, and the section labels still disagree with each other.
**Got the answer** partly · Trust and look were clear on the first desktop screen of index.html; the newcomer guidance was clear on start/index.html (the reader map) and briefings/everyone/index.html (the thirty-second answer); the every-screen question stayed only partly answered, because the phone captures again put the h1 between 550px and 652px down an 812px screen on every page.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 3 |

### What works
- The front page hierarchy on desktop is still unmistakable: a large serif headline, a sans-serif standfirst ending on 'Phones and personal computers are not affected', and one filled teal call to action beside four outlined ones. ([index.html](../../../index.html))
- Dark mode remains a real theme: the teal brightens to mint, the status badges keep their meaning, and the instruments found 0 low-contrast pairs in dark on all seven pages. ([claims/index.html](../../../claims/index.html))
- New 'IN PLAIN ENGLISH' panel at the top of the claims page, in a distinct pale blue box, tells a newcomer in one sentence what the dense table is for before the 21.4 reading-ease paragraph begins. ([claims/index.html](../../../claims/index.html))
- The status legend is now five coloured badges (CONFIRMED green, REPORTED blue, DISPUTED and CONTRADICTED amber, UNVERIFIED red), each defined once, and the same five appear in 'How to read this site' on the explainer. ([explained/index.html](../../../explained/index.html))
- The 'Right now' cards with a red left rule and grey source chips still make every sentence look sourced at a glance; on tablet they read especially well at full width. ([index.html](../../../index.html))
- The boxed thirty-second answer with Alex's avatar and the single 'Read the site as Alex' button is still the clearest hand-hold for a newcomer on the site. ([briefings/everyone/index.html](../../../briefings/everyone/index.html))
- The Stories menu item is now highlighted on the Stories page, so the menu at least agrees with the page title. ([articles/index.html](../../../articles/index.html))
- No horizontal overflow at phone, tablet or desktop on any page, no images without alt text, and the explainer's diagrams ('A NORMAL VISIT', 'THE ATTACK') are built as text boxes, so they scale and stay readable. ([explained/index.html](../../../explained/index.html))

### What does not
- **high** An unlabelled money figure still sits in the masthead and still falls as I move from page to page; it reads as a charge and is the biggest trust risk for a newcomer. ([index.html](../../../index.html))Desktop pill: '£5.00' on index.html, '£4.99' on start, '£4.96' on briefings/everyone, '£4.95' on claims, glossary and articles, '£4.94' on explained. Phone: '£5.00', '£4.98', '£4.97'. Tablet front page: '£4.99'. No visible label anywhere.
- **high** On a phone the chrome still fills most of the first screen, and on inner pages it has got worse: masthead, a four-button row, the new 'New to this story?' strip, the 'Your reading' panel and the RESEARCH or ABOUT band all come before the headline. ([briefings/everyone/index.html](../../../briefings/everyone/index.html))Phone h1 top: 550px on index.html, 590px on claims, 594px on explained, 652px on briefings/everyone, in an 812px screen. On briefings/everyone fold-phone.png the thirty-second answer box only starts at the bottom edge, exactly as last time.
- **medium** Section labels still contradict each other: the band, the kicker and the highlighted menu item name different parts of the site. ([glossary/index.html](../../../glossary/index.html))glossary: band 'ABOUT THIS SITE', kicker 'START HERE', menu 'Start here'. explained: band 'RESEARCH', kicker 'START HERE'. articles: menu now highlights 'Stories' but the band still says 'ABOUT THIS SITE', under the sentence 'Every page on the site says at its top which half it belongs to.'
- **medium** On the claims table two trust scales sit side by side and disagree visually: a full six-dot green 'A6 Established' badge next to a DISPUTED status. ([claims/index.html](../../../claims/index.html))'Remote code execution is confirmed on PHP-FPM ... DISPUTED A6 Established ●●●●●●' and 'A web application firewall may provide some protection ... DISPUTED A6 Established ●●●●●●'; an UNVERIFIED row shows 'A1 Weak signal ●○○○○○ OPINION DISPUTED'. Nothing in the five-word legend explains the FACT-CHECK column.
- **medium** Desktop navigation still wraps at 1440px; the orphaned 'About' is now a whole second row ('STORIES Views Stories | SITE About'), which still looks unfinished. ([index.html](../../../index.html))fold.png on all seven pages: row one ends at 'GRC', row two starts at y=139 with 'STORIES'.
- **medium** The 'Your reading' panel with fade / hide / show is still the first block on every page, ahead of the headline, and means nothing on a first visit. ([index.html](../../../index.html))First fold text on all seven pages: 'Your reading: on this page 9 new, 0 changed, 0 read; across the site 429 new and 0 changed of 429. ... Read items: fade hide show'.
- **low** The new 'New to this story?' strip, the one element written for a newcomer, does not appear on the front page where newcomers land, only on inner pages where it adds to the stack. ([index.html](../../../index.html))Present on briefings/everyone, claims, glossary, articles and explained fold.png; absent from index.html fold.png and fold-phone.png.
- **medium** Glyph-only row controls still fail the tap-target check, worst on the page where readers most need to tap sources. ([claims/index.html](../../../claims/index.html))155 of 453 targets under 24px on claims at phone width (147 last time); tap examples include '○', '⋯', '×' and 'FACT-CHECK'; the phone theme switcher is still a lone dot with no label.
- **low** Front-page counts still do not match the claims page, and the front-page legend still has four status words to the claims page's five. ([index.html](../../../index.html))index.html: '70 statements checked: 21 confirmed, 11 disputed, 4 unverified'; claims: '21 confirmed, 34 reported, 8 disputed, 3 contradicted, 4 unverified'.
- **low** Build provenance still clutters reader-level cards and section footers, and is now visibly far behind the masthead version. ([articles/index.html](../../../articles/index.html))'House · Journalist · 2026-10-23 · claude-journalist · site v0.10.1 · vault commit f3c5db0d9873 · data as of 2026-10-23T01:20Z'; front-page footers say 'This section v1 written in site v0.3.2' under a masthead pill 'v0.10.18'.
- **low** On tablet the masthead buttons are spread edge to edge with large gaps, so Ask, Feedback, the theme switch and the pound pill read as unrelated scattered objects. ([index.html](../../../index.html))fold-tablet.png: 'Ask' at the far left, 'Feedback' about a third across, 'Newsprint' two thirds across, '£4.99' at the far right, with 'Menu' alone on the row above.
- **low** On the desktop front page the 'briefing for you' grid is very uneven: the 'I make the decisions' column stacks five cards while neighbouring columns hold one or two, leaving large empty areas. ([index.html](../../../index.html))full.jpg, 'The briefing for you' section: columns of 2, 6, 2, 4 and 2 cards in five columns.
- **low** A plain-English persona is told to expect deeply technical words. ([start/index.html](../../../start/index.html))Casey, website owner, marked 'Plain English'; 'Words they will meet' includes 'mod_php', 'Out of memory (OOM)' and 'longjmp'.
- **low** Smallest text is still just under 12px on five of seven pages, mostly the faint version lines. ([start/index.html](../../../start/index.html))min_font_px 11.84 with 17 blocks below 12px on start (16 last time).

### What this reader would change, in order
- Label the pound pill in the masthead (for example 'Reading credit: £4.95, free') or move it into the account menu. ([index.html](../../../index.html), small)An unexplained, falling money figure is still the single biggest trust risk for a newcomer, and it has now survived six releases.
- On phone, merge the 'New to this story?' strip, the 'Your reading' panel and the RESEARCH or ABOUT band into one collapsed line below the h1 and standfirst. ([briefings/everyone/index.html](../../../briefings/everyone/index.html), medium)The headline and the thirty-second answer are the things to read first and on a phone they start at 652px of 812px.
- Drive the band, the kicker and the highlighted menu item from one field, so glossary and explained name one section and the Stories page says STORIES in its band. ([glossary/index.html](../../../glossary/index.html), small)The site promises each page says which half it belongs to, and three of my seven pages visibly break that promise.
- Explain the FACT-CHECK column in the legend above the table, or hide the Established dots on DISPUTED and UNVERIFIED rows so the two scales cannot look opposed. ([claims/index.html](../../../claims/index.html), small)A full green six-dot badge beside a DISPUTED label reads as a contradiction to anyone scanning the table.
- Fit the desktop navigation on one row at 1440px, for example by moving STORIES and SITE into the masthead row beside Ask and Feedback. ([index.html](../../../index.html), small)The wrapped second row makes every page look slightly broken at the main desktop size.
- Show the 'New to this story?' strip on the front page and hide the 'Your reading' panel until the reader has marked something read. ([index.html](../../../index.html), small)The newcomer hint is missing where newcomers arrive, while the tracker shows noise to the same people.
- Give the '○' and '⋯' row controls, the '×' close button and the phone theme switch a 24px minimum hit area, and give the theme switch a text label on phone. ([claims/index.html](../../../claims/index.html), small)155 undersized targets on the page where readers most need to tap sources.
- Align the front-page 'How this site knows' counts and status legend with the claims page's five statuses, including reported and contradicted. ([index.html](../../../index.html), small)Two summaries of the same 70 claims disagree on the front page and the claims page, which a sceptical reader will notice.

### Lines this reader reacted to
- [claims/index.html](../../../claims/index.html): *IN PLAIN ENGLISH Every statement made about the story, who made it, and how far it can be trusted, with links to the evidence.*New and exactly right: one sentence, in its own box, before the dense paragraph. This is the pattern the other technical pages should copy.
- [index.html](../../../index.html): *Your reading: on this page 9 new, 0 changed, 0 read; across the site 429 new and 0 changed of 429.*Still the first words on the page, before the headline, and still noise to a first-time visitor.
- [articles/index.html](../../../articles/index.html): *Every page on the site says at its top which half it belongs to.*Still a good promise, still broken by the band directly above it, which says ABOUT THIS SITE.
- [briefings/everyone/index.html](../../../briefings/everyone/index.html): *You do not need to know anything about computers to follow this.*Lands well under the answer box; on a phone it is below the first screen.
- [index.html](../../../index.html): *Phones and personal computers are not affected.*Still the right reassurance in the right place, last in a large standfirst.
- [start/index.html](../../../start/index.html): *Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.*Clear instruction, and the map with its dot scale delivers on it.
- [claims/index.html](../../../claims/index.html): *The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.*Still internal vocabulary ('the build', 'the manifest') in the first paragraph a newcomer reads, though the new plain-English box above it softens the blow.
- [explained/index.html](../../../explained/index.html): *Words in the dotted underline are explained when you hover or tap them.*Good and consistently applied; the underlined words remain small tap targets on a phone.

### Since the last run

From v0.4.3 to v0.10.18 the claims page improved (a plain-English summary box, five colour-coded status badges, the claims count now includes reported) and the Stories menu item is now highlighted on the Stories page; but my two high-severity failures are still open (the unlabelled pound pill still ticks from £5.00 to £4.94, and the phone headline still sits at 550px to 652px, now pushed further by a new 'New to this story?' strip on inner pages), the band and kicker contradictions on glossary, explained and articles are still open, the desktop nav still wraps (now a whole second row instead of a lone 'About'), the reading tracker is still above every headline, undersized targets on claims rose from 147 to 155, the front-page counts still disagree with the claims page, build provenance is still on story cards, and the FACT-CHECK column is a new source of visual contradiction (A6 Established beside DISPUTED). No page text addressed me or an AI.

Reviewer: agent-session.

[The whole run: the journey, the measurements and every flag](../../../admin/synthetic/designer/2026-10-23T2358Z/index.html).

## Every run

Scores are 0 to 5 from this reader's point of view.

| Run (UTC) | Site | Got the answer | Answered | Clarity | Trust | Design | Navigation | Fails (high / medium / low) | Pages |
|---|---|---|---|---|---|---|---|---|---|
| [2026-10-23T2358Z](../../../admin/synthetic/designer/2026-10-23T2358Z/index.html) | v0.10.18 | partly | 3 | 3 | 4 | 3 | 3 | 2 / 5 / 7 | 7 |
| [2026-10-22T1755Z](../../../admin/synthetic/designer/2026-10-22T1755Z/index.html) | v0.4.3 | partly | 3 | 3 | 4 | 3 | 3 | 2 / 4 / 3 | 7 |

## Everything it saw: the vault

**Vault** `dpdx3q13` · **read key** `sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297:dpdx3q13` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297%3Adpdx3q13) · `sgit clone sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297:dpdx3q13`

Every run is a folder under `runs/`.

## See it live, here

[Open the vault in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297%3Adpdx3q13) Read-only, in the official vault UI.


---
site v0.22.39 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://php.oct.2026.newsroom.sgit.ai/admin/synthetic/designer/index.html
