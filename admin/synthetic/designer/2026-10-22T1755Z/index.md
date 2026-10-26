# Designer, synthetic reader: the run of 2026-10-22T1755Z on v0.4.3

> About this site: how the site works, kept by the agents that run it.

What the synthetic designer read on the live site at 2026-10-22T1755Z, what it measured, and its review: whether it got its answer, what works, what does not and what to change.

# Designer: the run of 2026-10-22T1755Z

Product and content designer. Judges hierarchy, typography, layout, consistency, accessibility and whether the site guides a newcomer. Checks phone, tablet and desktop, light and dark. **Question:** Does the site look and feel trustworthy, does it guide a newcomer, and does it work on every screen for every reader?

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [This reader's runs](../../../../admin/synthetic/designer/index.html), [all six readers](../../index.html).

**Site** v0.4.3 (data as of 2026-10-22T11:34Z) · **read** 2026-10-22T1755Z to 2026-10-22T17:56:14Z · **device** 1440×900, desktop, light (also phone, tablet, dark) · **pages** 7 · **requests** 119 (21 telemetry calls answered locally) · **failed requests** 0 · **console errors** 0 · **words read** 15258

## The review, in the reader's words
The type, colour and evidence styling feel calm and trustworthy, and the front page does point a newcomer somewhere sensible, but two stacked utility boxes sit above every headline, an unlabelled pound figure ticks down as I move around, and the page labels do not agree with each other, so the site looks more finished than it guides.
**Got the answer** partly · Trust and look were clear on the first desktop screen of index.html; the guidance question was answered on start/index.html (the reader map); the every-screen question only partly, after the phone screenshots showed the headline pushed to the lower third of the first screen on every page.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 3 |

### What works
- Strong serif headline, a generous sans-serif standfirst and one filled teal call to action beside two outlined ones: on desktop the one thing to read first is unmistakable. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- Dark mode is a real theme, not an inversion: the teal shifts to a brighter mint, the red rules soften, and the instruments found 0 low-contrast pairs in dark on every page. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- The 'Right now' cards with a red left rule and small grey source chips make every sentence look sourced at a glance; it is the most trustworthy visual pattern on the site. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))
- The reader map is a genuine piece of information design: two axes, dot-scale depth markers (one, two, three dots) and coloured initial avatars by role group. ([start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/))
- The boxed 'The answer in thirty seconds' panel with the reader's avatar and a single 'Read the site as Alex' button is the clearest hand-hold for a newcomer anywhere on the site. ([briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/))
- Status badges are consistent between the front page and the claims table (CONFIRMED in green, UNVERIFIED in red, REPORTED and DISPUTED neutral) and each is defined once above the table. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))
- Pill-shaped jump links (letters on the glossary, questions on the explainer) give long pages a visible table of contents in the first screen. ([explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/))
- No horizontal overflow on any page at phone, tablet or desktop, and no images missing alt text. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))

### What does not
- **high** On a phone the site chrome eats most of the first screen: masthead, a theme dot, a price pill, the 'New to this story?' banner, the 'Your reading' panel and the RESEARCH band all come before the headline. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))Phone metrics put the h1 at 590px on claims and 550px on index.html in an 812px-tall screen; on briefings/everyone the thirty-second answer box only starts at the very bottom edge of fold-phone.png.
- **high** An unlabelled money figure sits in the masthead and changes from page to page with no explanation, which reads as a charge and undermines trust for a newcomer. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))Desktop pill shows '£4.99' on index.html, '£4.96' on briefings/everyone, '£4.95' on claims and glossary, '£4.94' on explained; the phone shows '£5.00', '£4.98' and '£4.97'. Nothing on the visible page says what it is.
- **medium** Page labels contradict each other: the band, the kicker and the highlighted menu item disagree about which part of the site a page belongs to. ([glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/))glossary: band 'ABOUT THIS SITE', kicker 'START HERE', menu highlights 'Start here'. explained: band 'RESEARCH' but kicker 'START HERE'. articles: band 'ABOUT THIS SITE' on the Stories page, while articles itself says 'Every page on the site says at its top which half it belongs to'.
- **medium** Desktop navigation wraps: 'About' drops alone onto a second row under 'SITE', which looks like a layout bug at 1440px. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))fold.png on every page: the 'SITE' label ends row one and 'About ▾' sits by itself on row two at y=99.
- **medium** The reading-tracker panel ('Your reading: on this page 9 new, 0 changed, 0 read', fade / hide / show) is the first thing on every page, above the headline, and means nothing to a first-time visitor. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))It is the first block of fold text on all seven pages, ahead of the h1; 'Read items: fade hide show' has no explanation.
- **medium** Small, glyph-only controls repeat across the site and fail the tap-target check on phone. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/))147 targets under 24px on claims at phone width; examples include the '○' and '⋯' buttons on every claim row (they do carry aria-labels, but visually they are bare symbols), and the theme switcher on phone is a lone teal dot with no visible label.
- **low** Machine provenance is shown at reader level on story cards and section footers, cluttering cards and contradicting the site's own version. ([articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/))'House · Journalist · 2026-10-22 · claude-journalist · site v0.4.0 · vault commit 200d08971937 · data as of 2026-10-22T11:34Z'; front-page sections say 'This section v1 written in site v0.3.2' while the masthead says v0.4.3.
- **low** Counts on the front page do not match the status scheme used on the claims page. ([index.html](https://php.oct.2026.newsroom.sgit.ai/))index.html: '70 statements checked: 22 confirmed, 11 disputed, 4 unverified'; claims: '22 confirmed, 33 reported, 8 disputed, 3 contradicted, 4 unverified'. The front page legend also lists four status words, claims lists five.
- **low** Smallest text is just under 12px on six of seven pages. ([start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/))min_font_px 11.84 with 16 blocks below 12px on start; the metadata lines ('This page v4 written in site v0.3.1') are visibly the faintest, smallest text on the page.

### What this reader would change, in order
- On phone, move the 'Your reading' panel and the RESEARCH / ABOUT band below the h1 and standfirst (or collapse them into one line), so the headline is in the top third of the first screen. ([index.html](https://php.oct.2026.newsroom.sgit.ai/), medium)The headline is the one thing to read first and on a phone it currently starts two-thirds of the way down on every page.
- Label the pound pill in the masthead (for example 'Reading credit: £4.95, free') or hide it until the reader opens the account menu. ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)An unexplained, falling money figure is the single biggest trust risk for a newcomer.
- Make the band, kicker and highlighted menu item come from one source, so glossary and explained both say the same section, and the Stories page says STORIES. ([glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/), small)The site promises each page states which half it belongs to; inconsistent labels break that promise visibly.
- Fit the desktop navigation on one row at 1440px (tighten spacing or fold 'About' into the masthead). ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)The orphaned 'About' makes every page look slightly broken on the main desktop size.
- Give the '○' and '⋯' row controls and the read-state pills a 24px minimum hit area, and give the phone theme switcher a visible text label. ([claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/), small)147 undersized targets on the one page where readers most need to tap sources.
- Show only the reader's 'Read items' controls after the first page mark, with a one-line hint the first time ('Mark what you have read; we keep it in this browser'). ([start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/), medium)Fade, hide and show mean nothing before a newcomer has read anything.
- Move vault commit, agent name and 'written in site vX' lines into the history link, leaving date and author on the card. ([articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/), small)The cards read as build logs; the provenance is good but it is not reader-level information.
- Align the front-page counts with the claims page's five statuses, including reported. ([index.html](https://php.oct.2026.newsroom.sgit.ai/), small)A designer notices when two summaries of the same numbers disagree, and so will a sceptical reader.

### Lines this reader reacted to
- [index.html](https://php.oct.2026.newsroom.sgit.ai/): *Phones and personal computers are not affected.*Placed last in the standfirst at a large size: the reassurance a newcomer needs, exactly where they look.
- [index.html](https://php.oct.2026.newsroom.sgit.ai/): *Your reading: on this page 9 new, 0 changed, 0 read; across the site 340 new and 0 changed of 340.*The first words on the page, before the headline. As a first-time visitor this is noise.
- [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/): *Across: how much technical language the reader wants. Down: what they need to do with the story. Pick the one closest to you.*A clear instruction for a two-axis chart; the visual delivers on it.
- [briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/): *You do not need to know anything about computers to follow this.*Lands well, set right under the answer box.
- [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/): *The words are defined here, once, and the build refuses a claim whose sources are not in the manifest.*Trust-building idea, but 'the build' and 'the manifest' are internal words in the intro paragraph of a page also flagged at reading ease 27.8.
- [articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/): *Every page on the site says at its top which half it belongs to.*A good promise that the page itself breaks: this Stories page is labelled ABOUT THIS SITE.
- [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/): *Words in the dotted underline are explained when you hover or tap them.*Good, and the dotted underline is consistent everywhere, though the underlined terms are small tap targets on a phone.

### Since the last run

First run: no previous review to compare with.

Reviewer: agent-session.

## The journey

The pages in the order read: the start, the reader's path, then the links that matched its interests.

| # | Page | Why | Words | Screens | Reading ease | Glossary terms per 1000 words | Load (ms) | Low-contrast blocks | Small tap targets | Sideways scroll |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | start | 1948 | 6.7 | 56.6 | 12.3 | 964 | 0 | 22 of 176 |  |
| 2 | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | reading path | 3682 | 16.8 | 59.9 | 37.5 | 735 | 0 | 6 of 307 |  |
| 3 | [briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/) | reading path | 806 | 3 | 57.2 | 14.9 | 597 | 0 | 65 of 230 |  |
| 4 | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | reading path | 3850 | 11.5 | 27.8 | 24.2 | 695 | 0 | 147 of 446 |  |
| 5 | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | reading path | 2990 | 11.5 | 60.9 | 36.8 | 473 | 0 | 7 of 103 |  |
| 6 | [articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/) | reading path | 644 | 2.4 | 54.7 | 3.1 | 667 | 0 | 20 of 58 |  |
| 7 | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | followed a link | 1338 | 4 | 64.1 | 17.9 | 703 | 0 | 7 of 84 |  |

## What the instruments flagged

Measurements, not verdicts: the review says which of them mattered to this reader.

| Severity | Page | Check | Evidence |
|---|---|---|---|
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | text at least 12px | smallest 11.84px, 16 blocks below 12px |
| medium | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | little jargon for a non-specialist | 37.5 glossary terms per 1,000 words: Patch, Primary source, CVE, Exploit, exploitation, mod_php |
| low | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | length fits the reader | 16.8 screens long on this device |
| low | [briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/) | text at least 12px | smallest 11.84px, 2 blocks below 12px |
| medium | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | readable for a non-specialist | Flesch reading ease 27.8 (below 45 is hard) |
| low | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | length fits the reader | 11.5 screens long on this device |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | length fits the reader | 11.5 screens long on this device |
| low | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | tap targets at least 24px (phone) | 23 small targets |
| low | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | tap targets at least 24px (phone) | 6 small targets |
| low | [briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/) | tap targets at least 24px (phone) | 65 small targets |
| low | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | tap targets at least 24px (phone) | 147 small targets |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | tap targets at least 24px (phone) | 7 small targets |
| low | [articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/) | tap targets at least 24px (phone) | 15 small targets |
| low | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | tap targets at least 24px (phone) | 7 small targets |
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | tap targets at least 24px (tablet) | 22 small targets |
| low | [start/index.html](https://php.oct.2026.newsroom.sgit.ai/start/) | tap targets at least 24px (tablet) | 6 small targets |
| low | [briefings/everyone/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/everyone/) | tap targets at least 24px (tablet) | 65 small targets |
| low | [claims/index.html](https://php.oct.2026.newsroom.sgit.ai/claims/) | tap targets at least 24px (tablet) | 147 small targets |
| low | [glossary/index.html](https://php.oct.2026.newsroom.sgit.ai/glossary/) | tap targets at least 24px (tablet) | 7 small targets |
| low | [articles/index.html](https://php.oct.2026.newsroom.sgit.ai/articles/) | tap targets at least 24px (tablet) | 19 small targets |
| low | [explained/index.html](https://php.oct.2026.newsroom.sgit.ai/explained/) | tap targets at least 24px (tablet) | 7 small targets |

## Everything this run saw

**Vault** `dpdx3q13` · **read key** `sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297:dpdx3q13` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297%3Adpdx3q13) · `sgit clone sgit_public_read_d38e486c514c3f320e437bf757110c772af8241c595baa6ec0a4504d72069297:dpdx3q13`

This run is in the folder `runs/2026-10-22T1755Z/`: the served and rendered HTML, the text and the screenshots of every page, every request and console message, and what the reviewer was given.


---
site v0.22.34 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/synthetic/designer/2026-10-22T1755Z/index.html
