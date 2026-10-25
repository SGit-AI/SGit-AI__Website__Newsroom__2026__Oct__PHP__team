# Brief: the lens, a site that shapes itself to the reader in front of them

> About this site: how the site works, kept by the agents that run it.

(Bret Victor's talk Inventing on Principle, 2012: creators need an immediate connection to what they create.)

# Brief: the lens, a site that shapes itself to the reader in front of them

Published 2026-10-24 13:35 UTC · `2026-10-24__brief__the-lens.md` · [all briefs](../index.html)

## Brief: the lens, a site that shapes itself to the reader in front of them

Status: a design, with a working prototype at `/admin/design/lens/` (prototype E); for the editor's go, then for dev. Author: story-site (claude-story-site), from the editor's note in its session of 24 October 2026. Follows the redesign (`2026-10-23__brief__the-redesign.md`, `2026-10-24__brief__the-redesign-live.md`) and the desk's review of it (`2026-10-24__review__the-redesign-for-communication.md`).

### The note

Okay, so now I believe the developers So already working on this workflow, which is fundamentally to go into a persona first application. So we already start doing a little bit of this, but this is kind of taking that on steroids, which is the whole UI, which is going to do some interesting technical challenges, but I think we can handle it. The whole UI needs to change once the user changes settings. So this is like the Brad Victor's inventing on principle concept, where, you know, I think we were mapping kind of four parameters or three parameters in terms of the workflow. And then the idea is that as I change those sliders or those options, the UI should change, right? Literally in front of the user in real time, right? Maybe we load some data, but it should be loading there, right? So that means the user should not have to refresh the page, should not have to do other stuff to see the impact of that change, because also it depends on the time, depends on the focus, depends on what they want to do, right? So can you think of it from a design point of view? I'm kind of imagining this on the top right, that the user makes the changes. Now, this is where it gets interesting. So we still have lots of pages on the website, and maybe some parts of the website have more or less support for this, right? I guess there'll be parts of the website. So for example, like if there's parts of the website that you can only access from a particular user, then actually gets interesting because you have less options, right? So we need to maybe think about how we're going to make that work. But the key point here is that the whole website now needs to reflect the user. And then as you navigate to pages, again, be careful with flickering, but as you navigate to multiple pages, how can we make sure that that experience doesn't change? And that means that from a UX point of view, you need to think, how can we, as soon as we can, get the user to A, understand that it's happening, B, make those selections, where I guess we start with the simpler and the most back to the point, you know, if you have 5 minutes, if you have 1 minute, is what you want to know, and then we expand from there, or maybe as you scroll down, but let's think about that design element of it, and think about how to actually make that work.

(Bret Victor's talk *Inventing on Principle*, 2012: creators need an immediate connection to what they create.)

### The idea in one line

One control at the top right holds four settings; every page is built whole and each part of it says which settings show it; moving a setting re-lays the page in the same frame, and the next page arrives already shaped.

### The four settings

| Setting | Choices | What it changes | Asked |
|---|---|---|---|
| **Time**: how long have you got? | 1 min, 5 min, 15 min, All | How many parts of each page show. 1 min is the answer and what to do; 5 the situation and its evidence; 15 the detail; All everything. | First, on the first visit |
| **Who**: which is closest to you? | The five groups (understand, decide, tell others, run systems, study), then any of the 16 readers; plus "I work on this site" | Which parts are for you, and the wording of the parts that have a version per reader (the answer, the one line) | Second |
| **Aim**: what do you want to do? | Understand it, Know what to do, Check the evidence | The order of the parts and, at 1 and 5 minutes, which ones. This is what tracks A, B and C were: three aims, now on one page instead of three addresses. | Third |
| **Seen**: what you marked "Got it" | Show, Fade, Hide | Parts you have read fade or leave, on every page, until they change | Never asked; in the control |

These replace "Focus, Standard, Everything", which the desk found are our words and do not focus (board 235): time is the reader's own measure. Who replaces the persona select. Aim folds the three homes into one page.

### How it works, so that nothing flickers

1. **Every page is built whole, always.** The build writes every part of a page; each part carries its rules as attributes: `data-t` (the shortest time that shows it), `data-aim` (the aims it serves), `data-for` (the readers it is for), and one order per aim (`--o-u`, `--o-a`, `--o-v`). A part with a version per reader holds each version (`.lv data-only=...`). Nothing is fetched to re-shape a page, so a change cannot wait on the network.

2. **The settings are on the page before it is drawn.** A small script in ``, loaded without `defer` (`assets/design/lens-boot.js`, under 1 KB), reads the settings from the browser and writes them onto `` as attributes. The first frame is already the reader's page: no flash of the standard page on the first visit or the tenth. Measured on the prototype: layout shift 0 when moving between its pages.

3. **The stylesheet does the shaping.** `lens.css` shows, hides and orders the parts from the attributes on ``. Moving a setting changes one attribute; the browser re-lays the page in the same frame. Where it can, the change is animated with the View Transitions API (each part has its own transition name, so parts slide to their new places), and parts that have just appeared flash once. Between pages, cross-document view transitions keep the header still.

4. **The reader sees a choice's effect before making it.** Each option in the control says what it would show on this page ("5 parts, about 3 min"), worked out from the parts on the page; a line under the title says what the page is showing now ("Showing 5 of 13 parts, about 3 min of reading, for Sam, security lead, to know what to do. Change").

5. **The settings are kept in this browser only**, as one record (`p2s.lens`); `p2s.persona` stays in step, so the rest of the site follows. Another open tab follows a change (the `storage` event). Later: the reader's vault, as board 140 asks.

6. **It works under the site's Content-Security-Policy**: the scripts are files; the one inline style is allowed.

### Pages with more or less support

Every page declares the settings it answers to (``). The control always shows all four, so it never jumps; a setting this page does not answer to is greyed, with the reason ("This page reads the same whatever you came to do; your aim is kept for the next page"). The choice is never lost: it applies again on the next page that answers to it.

A page that has not been tagged yet (proposed; not in the prototype) still answers to Seen and Time in the simplest way the build can give it: at 1 minute its first paragraph and plain-English box, then "The rest of this page (N min)". So the whole site supports the lens on day one, and pages get richer support one by one.

**A page for some readers only** (the team console, for example) says so at the top: who it is for, that nothing on it is hidden, and two buttons: "Read it anyway" (remembered for the visit) and "Back to your front page". Time and aim are greyed there. It is public, as everything here is; it is just not written for everyone, and links to it are left out of the menus of readers it is not for.

### The first visit: understand that it is happening, then choose

- A card at the top of the first page asks one question at a time, starting with the simplest: **How long have you got?** The page below re-shapes the moment it is answered, so the reader sees the site change before reading any explanation. Then **Which is closest to you?** (five groups, not sixteen readers), then **What do you want to do?** Each answer is applied at once.

- After the third answer, or "Skip", the card goes and the control at the top right pulses once, so the reader knows where the settings live. It reads, for example, "1 min · I make the decisions · Know what to do".

- At the end of every page shorter than All: "That is the page for the time you gave it. **Show more**", which moves Time up one step. Expanding as you read, as the note asks.

- On a phone the control is a chip in the one-line header (dev's 43px line, CI-003 step 1) and opens as a sheet from the bottom.

### The prototype (prototype E, `/admin/design/lens/`)

Built by `admin/build/design.py` from the live data, three pages:

- **The front page**: 13 parts, every one from data (the answer per reader, the four tiles, three questions for a decision maker, three actions for an operator, three contested claims for a writer, the open questions for a researcher, how sure we are, right now, the latest, the agencies, what nobody knows, the core facts, how it unfolded, the contested list, agency by agency).

- **The agencies**: answers to time, who and seen, not aim; its one line has a version per group.

- **The team console**: for the team only; the gate, and only Seen applies.

"Show what drives each part", in the control, labels every part with its rules, for review.

### What it means for the site (for dev, after the editor's go)

1. `lens-boot.js` and `lens.css` on every page (layout in `build.py`); the control replaces the dials in the top bar. One change, and every page keeps working, untagged.

2. A helper in the build to tag a part: `part(key, html, t=, aim=, for_=, order=)`, used page by page, starting with the front page, the briefings, the agencies, the numbers and the impact (board 141's list).

3. The fallback for untagged pages (first paragraph and plain-English box at 1 minute).

4. Menus by the same rules: a menu entry is a part, so it follows the settings without script.

5. The settings in the reader's vault (board 140), and the telemetry event to carry them (board 262 asks for the persona; time and aim matter as much).

### Decisions for the editor

1. Go for the lens to replace the two dials on the live site, or keep it in the prototype for now.

2. The words: "How long have you got?", "Which is closest to you?", "What do you want to do?", "Got it". The desk asked for plain words; these are a proposal.

3. Whether "I work on this site" is a reader like the others (it is in the prototype).

This brief is the file `admin/content/briefs/2026-10-24__brief__the-lens.md` in the repository, published as written.

← older: The telemetry lane's 1,000-event cap, and lanes in parallenewer: → Brief: the pipeline, from the researcher to the correspond


---
site v0.22.12 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-24__brief__the-lens/index.html
