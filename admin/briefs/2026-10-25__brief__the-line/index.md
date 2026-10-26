# Brief: the line, and a site that is persona first

> About this site: how the site works, kept by the agents that run it.

Everything in this pack was made from the site's own data at release v0.15.18 (24 October 2026, 08:37 UTC): data/personas.json, the front page's parts, the agencies, the numbers an

# Brief: the line, and a site that is persona first

Published 2026-10-25 02:45 UTC · `2026-10-25__brief__the-line.md` · [all briefs](../index.html)

## Brief: the line, and a site that is persona first

Status: a design, agreed with the editor on 25 October 2026, for the design agent (story-site) to build, then dev. Author: Claude, working with the editor (Dinis Cruz) in a design session on 24 and 25 October 2026. It follows and replaces parts of the lens brief (`2026-10-24__brief__the-lens.md`, prototype E at `/admin/design/lens/`), and takes in the desk's review (`2026-10-24__review__the-redesign-for-communication.md`).

Everything in this pack was made from the site's own data at release v0.15.18 (24 October 2026, 08:37 UTC): `data/personas.json`, the front page's parts, the agencies, the numbers and the facts by status.

### The editor's direction, in his words

From the session, in order:

"Asking for the time available is not a good place to start." "We want to map users to personality … and the personality should dictate everything that happens on the website. … we are fundamentally recreating the website based on who the user is. So it needs to be super clear." "Do you want it to be more technical? Do you want it to be less technical? Because you could be an executive that wants things very technical or not." "What's the delta, what has changed, new … show me the website the way it looked a while back." "We should default to one, though we need to make it very clear that there's others … you're viewing this website as X." "We should never lose that top line, because that top line is fundamentally our ability to talk directly to the user. … that should basically travel through with the user through the whole site. And some pages will have more, other pages will have less. … we're tracking not only the multiple personas, but … the multiple timelines … first visit, second visit, you haven't been here for a while, you just came back, or same visit the same day … it can be bigger or smaller depending on the scenario."

And the default persona is the **Executive**.

### The idea in one line

Every page carries **the line**: one band under the masthead that says one thing, to the persona in front of it, at this moment of their visits; and the page under it is re-shaped for that persona and depth, with what has changed since they were last here marked and what they have read folded away.

### 1. What changes from the lens (prototype E)

| In the lens | Now | Why |
|---|---|---|
| Four settings in a control: Time, Who, Aim, Seen | One choice (**role**, optionally a closer **reader**) plus **depth**. The rest is worked out. | The editor: start from who they are, not how long they have. |
| Time: 1, 5, 15 min, All | Removed as a setting. The role decides what a page shows; "Show everything on it" at the end of a page; catch-up mode for long absences. | Time is a limit, not a reason to come. |
| Who: five groups, sixteen readers, "I work on this site" | **Seven roles** (six centres of gravity plus Everything), the sixteen readers inside them. The team is not a reader: team pages are gated (section 7). | Readers recognise "Executive", "Security", "Journalist"; the editor named these. |
| Aim: Understand, Act, Verify | Folded into the role: each role has its own order of parts. | Aim was mostly order (lens README, question 4); the role already implies it. |
| Seen: Show, Fade, Hide, by hand ("Got it") | **Automatic**: a part is read when it has been on screen and scrolled past. Read parts fold to one row until they change. | Nobody keeps marking by hand (lens README, question 5). |
| The first-visit card, three questions | **The line's panel**: the site has already chosen (Executive, or a guess), says why, and shows the six others. One tap or none. | Default to one; make the others obvious. |
| The status line under the title ("Showing 7 of 13 parts…") | **The line**, on every page, always. | One place to talk to the reader. |

What stays from the lens, unchanged: every page is built whole; parts carry their rules as attributes; a blocking script in `` puts the reader's state on `` before first paint; the stylesheet does the shaping; nothing is fetched to re-shape a page; View Transitions; the CSP rules. The lens brief's "How it works, so that nothing flickers" still holds and is the foundation for this one.

### 2. The persona model: role, reader, depth

Full data: `spec/roles.json`. Pictures: `screenshots/journeys/`.

| Role | Reads as | Its question | Readers (from `personas.json`) | Default depth | Front page, in order |
|---|---|---|---|---|---|
| **Executive** (default) | an Executive | Are we exposed? What do I decide? | Board member, CFO, Programme manager, Data protection officer, CTO | Plain | Answer · four tiles · three questions for your team · right now / what nobody knows · what governments advise |
| **General reader** | a general reader | Does it touch me? What do I do? | Curious reader, Website owner | Plain | Answer · does it touch you / what to do · four tiles · right now / what nobody knows |
| **Security** | Security | What do we patch, block and watch? | Security lead, CISO, Head of AppSec | Technical | Answer · next three actions · attack signals / the advice now · the spectrum · how sure are we |
| **Engineer** | an Engineer | Which versions, settings and commands? | Platform engineer, Developer | Deep | Answer · fixed versions and settings · next three actions · exposure / what your code can't do |
| **Journalist** | a Journalist | What holds up? Who said it first? | Journalist, Communications | Technical | Answer · before you write · the numbers and how far each holds · how it unfolded · also contested |
| **Researcher** | a Researcher | What's the evidence? What's still open? | Security researcher, Policy analyst | Deep | Answer · the open questions · the two bug classes / what was shown · contested · how it unfolded |
| **Everything** | everything | The whole site, unfiltered. | none | Technical | Every part, in the usual order |

- **The role** decides which parts a page shows and their order, the menu (the reader's path through the site, from `personas.json`), what counts as news for them, and the line's wording.

- **The reader** is optional, inside a role. It changes the thirty-second answer and the line's one-liner where a reader has their own (the CFO's answer is about cost and cover). If no reader is chosen, the role uses its first reader's answer (Executive: the board member's).

- **Depth** (Plain, Technical, Deep; `personas.json` depths 1, 2, 3) changes how facts are worded, not which parts show. Each role and reader has a default; the reader can turn it. Example, the same fact:

- Plain: "A fix came out on 21 October. Whoever runs a website needs to install it, and restart it."

- Technical: "Fixed in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35. An update only counts once the service restarts."

- Deep: "Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker, rebuild images, verify with php -v inside the running container."

- Seven role × depth cells have no reader (an Executive who wants it deep, for example). They still work: the role's parts at that depth. They are listed in `spec/roles.json` (`emptyCells`) so the desk can decide whether to write readers for them.

- **Everything** is an escape hatch, not a persona: no filter, the standard order, the full menu. It is offered last, with a dashed outline.

### 3. The line

The line sits directly under the masthead on every page, full width, and is **never closed**. It can grow and shrink; it cannot go away. It says **one thing at a time**. It is the one place the site talks to the reader, and the place the reader changes who they are.

#### Sizes

| Size | When | Height |
|---|---|---|
| **Line** | The resting state: most pages, most of the time | one row, about 52 px |
| **Open** | News for you, a question, a gate | the row, then up to three items, then actions |
| **Panel** | First visit, on the page the reader lands on, if it's the front page | larger lead, the reason, "That's me", and the six other roles |

#### Four slots, left to right

1. **Who**: the persona chip, always first, always tappable; opens the control (section 8). Its dot: **teal** = confirmed, **amber** = not confirmed yet, **orange** = borrowed for this visit. It also carries short state: "Executive · 3 new", "Executive · Deep", "Security · as of Thu", "Journalist · shared".

2. **What**: one sentence, a bold lead then the rest, written for this role, on this page, at this moment.

3. **Picture** (optional, per page): a 140 px wide picture of the page's data. The agencies page: the spectrum of offline advice. The numbers page: the 70 facts by status. The past view: the dates. Never wider, never more than one.

4. **Do**: at most two actions ("Show me", "That's me", "Undo", "Back to today"). On the open and panel sizes, the six other roles may follow as a row of choices.

#### Tones

| Tone | Colours | Used for |
|---|---|---|
| Calm | `#e6f2f0` on ink, teal edge | the resting line; "now reading as" |
| Ask | white, 3 px teal edge | we need an answer |
| News | navy `#0f1b2d`, light text | something changed |
| Borrowed | `#fdf1e2`, amber | a shared view or a date in the past |
| Gate | `#fdf1e2`, 3 px `#b45309` edge | this page isn't for you |

These are the site's existing tokens (`assets/design/v2.css`); dark mode follows the same names.

#### What it says: the first rule that applies wins

| # | Rule | Tone, size | Example |
|---|---|---|---|
| 1 | **This page isn't for you** (the team console for an Executive) | Gate, open | "This page is for the team that runs the site. Nothing on it is hidden; it just isn't written for an Executive." [Read it anyway] [Back to your front page] |
| 2 | **You're borrowing a view**: a shared link, or a date in the past | Borrowed, line | "You're seeing the Journalist view from a shared link. Yours, Executive, is kept. This lasts for this visit only." [Switch to mine] [Make it mine] |
| 3 | **We need an answer**: first visit; the next visit if never answered | Ask, panel or open | "You're viewing this as an Executive. The short version, for people deciding what to do. We start everyone here until you tell us otherwise." [That's me] Not you? Read it as: General reader · Security · Engineer · Journalist · Researcher · Everything |
| 4 | **It just changed**, while the page is open | News, line | "Just updated: 1 change for you. "Right now" has a new line. Nothing moves until you ask." [Show me] [Later] |
| 5 | **Since you were last here**; catch-up after a week | News, open | "Since Thursday at 18:40: 3 changes for an Executive." + three items. [Show me] [Mark as seen] |
| 6 | **You just changed your view** | Calm, line | "Now reading as Security. Your next three actions come first. What you've read stays read." [Undo]. Fades to rule 7 after about 6 seconds. |
| 7 | **Nothing else to say**: the page's one line for you | Calm, line | Agencies, Executive: "All 16 say update. Two, both US, say take it offline if you can't: decide who makes that call." |

**Banners merge, never stack.** One line, one message. Where two rules apply on the same load they are written as one: a returning reader who never answered and has news gets "Still reading as an Executive? Since yesterday: 2 changes for you." with both the question's and the news's actions.

Every word is in `spec/line-copy.json`, and `reference/line-engine.js` (`computeLine`) turns state into the line; its tests in `reference/line-engine.test.mjs` check that no placeholder is ever left unfilled for any role, moment and page.

#### Every page has a one line for every role

Rule 7 means each page needs a sentence per role: its answer, for that reader. This is the biggest writing job in this brief.

- Written so far, in `spec/line-copy.json` (`pageLines`): the front page, the agencies, the numbers and the playbook, with a fallback (`_`) for roles without their own line.

- For pages not yet written: "{Page title}. This page reads the same for every view; yours, {role}, is kept for the next page." So every page supports the line on day one.

- The front page's line is the role's one-liner; its thirty-second answer stays in the hero.

- Numbers in lines come from data, as `AGENTS.md` asks (desk review, board 232). "16", "2 of 16", "19 confirmed" are counts the build must fill, not text.

### 4. Who you start as

The first match wins (`startingRole` in the engine):

1. **A shared link**, `?as=&depth=…`: for this visit only. It never overwrites a saved view unless the reader taps "Make it mine". On a first visit it reads as a guess: "You came from a link shared set to this view."

2. **A saved view** in this browser.

3. **Our last guess, never answered**: asked on at most two visits, then kept quietly.

4. **A guess from where the reader came from**, always with the reason in the line:

- a government or CERT advisory (cisa.gov, ncsc.gov.uk, cert.europa.eu, cert.ssi.gouv.fr, ncsc.nl, …) → **Security**, "You came from a government security advisory, so we started you here."

- a search with a PHP version or a SAPI in it ("php 8.4.27 fpm") → **Engineer**

- a mailing-list or research archive (openwall, seclists, GitHub advisories) → **Researcher**

- a news site → **General reader**

5. **Otherwise: Executive.**

The full list and the match rules are in `spec/roles.json` (`guesses`). Referrers are read in the browser only; nothing is sent anywhere.

### 5. The reader's timelines: visit moments

Every load is one of eleven moments, worked out before first paint from the stored record, the clock and the URL (`momentFrom`; order and thresholds in `spec/moments.json`).

| Moment | How it's recognised | What the line does | What the page does |
|---|---|---|---|
| **First visit** | nothing stored; or the same first visit, still unanswered | Panel on the front page, open on inner pages: who we think you are, why, the six others | The role's page |
| **Same visit, reading on** | active in the last 30 minutes | The page's one line | Parts marked read as they're read |
| **Back within the hour** | a new visit, under 60 minutes, nothing new | The page's one line | Read parts folded |
| **Later the same day** | a new visit today, nothing new for you | "Nothing new for you since 09:15." then the page's line | Read parts folded into one row: "Read · Three questions for your team · unchanged since you read it · Open" |
| **Second visit, never answered** | not confirmed, asked once | "Still reading as an Executive? Since yesterday: 2 changes for you." | Changed parts marked |
| **Back within a week** | a new visit with changes for you | "Since Thursday at 18:40: 3 changes for an Executive." Up to three items | Changed parts carry "Changed since Thursday" |
| **Back after a week or more** | changes for you and away 7 days or more; or more than 20 changes for you | "It's been [10] days. [46] changes since you were here. Rather than all of them: where it stands now, then the five that matter most for an Executive." [Catch me up] | Catch-up: the answer for today, then five changes |
| **Story updates while reading** | a new build lands while the page is open | "Just updated: 1 change for you." Nothing moves until asked | "Just updated" on the part |
| **Just changed view** | the reader changed role, reader or depth | "Now reading as Security…" [Undo] | Re-laid in place, in the same frame |
| **Opened a shared link** | `?as=` differs from the saved view | Borrowed: whose view, that yours is kept | The shared role's page |
| **Looking at the past** | an as-of date in the session | "As it was on Thursday at 18:40. What's changed since is marked. Nothing here is saved." [Back to today] | That day's headline and page; parts changed since marked "Changed after this date" |

**When a visit ends.** A gap of 30 minutes without activity starts a new visit. `lastVisit` moves forward only then (to the previous visit's last activity), never on arrival, so a reload never wipes "since you were last here". "Show me", "Mark as seen" and "Catch me up" move it to now. The engine's `visitStart()` says whether a load starts a visit and from when to count changes.

**What persists through a visit.** The first-visit question stays on every page of the first visit until answered (open size on inner pages); the second-visit question likewise on the second visit; changes for you stay in the line on every page until the reader taps "Show me" or "Mark as seen". "Nothing new since …" is said on arrival only.

**What counts as a change.** Each part has a content hash at build time. A part is **changed** for a reader when its hash differs from the one stored when they read it. An item is **new** when it was added to the change log after `lastVisit`. A change is **for you** when its part or item is tagged for your role; everything else is counted as "elsewhere", one tap away, never hidden. Switching role keeps what you've read. Looking at the past never marks anything read.

### 6. What the browser remembers

One record in `localStorage`, **`p2s.lens` version 2** (it replaces prototype E's v1 record), read synchronously by `lens-boot.js` before first paint, written by `lens.js`. Schema: `spec/storage.schema.json`; example: `spec/storage.example.json`.

It holds: role, reader, depth (and whether the reader set it), how the role was set (default, guess, shared, chosen), confirmed, how many times we asked, first visit, last visit, last active, visits, the release last caught up with, `seen` (part → content hash when read), the last 20 things the line said and what was tapped (so it never repeats itself), and a history of views.

- **For this visit only** (`sessionStorage`, `p2s.lens.session`): a shared view, a date in the past, "Read it anyway" on a page for others, the last view change (for Undo).

- `p2s.persona` stays in step, so the rest of the site keeps working.

- Other tabs follow a change through the `storage` event.

- **Share this view** copies `?as=&depth=`. Nothing about what was read travels in a link.

- **Copy my view**, for a reader's own other device: the same link with `&since=`, so "since you were last here" carries over. Later, the reader's vault (board 140) does this without a link.

- **Forget me on this browser**: deletes the record, the session and `p2s.persona`; the next load is a first visit.

- Telemetry (board 262): send role, depth and the line's rule number with page views. Never the reader's history.

### 7. Pages with more or less support, and pages for others

- Every page declares what it answers to, as in the lens (``). The line is on every page regardless.

- A page that hasn't been tagged yet shows its standard content and the fallback line (section 3).

- **A page for some readers only** (the team console): rule 1, the gate, in the line. The page under it is dimmed, not hidden: "Nothing on it is hidden. It just isn't written for an Executive." [Read it anyway] is remembered for the visit. Links to it stay out of the menus of roles it isn't for. The team is not a persona; a team member taps "Read it anyway" once per visit, or the console gets its own sign-in later.

### 8. The control, behind the chip

Tapping the chip opens the control (prototype: the earlier "Control" artboard): the seven roles, the readers inside the chosen role, depth (Plain, Technical, Deep), show (Everything new / Not yet read / Everything), as of (the dates of the story, today last), Share this view, Forget me. Every change re-lays the page in place and the line says what moved, with Undo. On a phone the chip is in the one-line header and the control opens as a sheet from the bottom.

### 9. The page under the line

- **Front pages per role**: the orders in the table in section 2; content from the evidence vault, as today. Screenshots of all seven in `screenshots/journeys/`.

- **Changed parts** carry a small badge above them: "Changed since Thursday", "Just updated", or in the past view "Changed after this date".

- **Read parts** fold to one row on a return visit the same day, with "Open".

- **The past view** shows that day's headline and the parts as they stood; it needs the build to keep each release's parts (the site already keeps releases).

- **Menus are by role**: the reader's path from `personas.json`, then "Everything". A menu entry is a part, so it follows the role without script (lens brief, point 4).

### 10. How to build it on the site (for dev, after the design agent)

1. **Boot** (`lens-boot.js`, blocking, in ``, under 2 KB): read `p2s.lens` and the session, the URL (`?as=`, `?asof=`) and `document.referrer`; work out the role (section 4) and the moment (section 5); write them onto `` as `data-role`, `data-depth`, `data-moment`, `data-confirmed`. Nothing else. The first frame is the reader's page.

2. **The line's words**: the build writes, per page, the line's page lines for every role (`data-line-`) and a small JSON island with the page's change log since the last few releases (part key, time, role tags). The line is pre-rendered for rule 7 from attributes alone, so the common case needs no script; `lens.js` fills rules 1 to 6 after first paint inside a **reserved height** (the line's one-row height is always present; open and panel sizes grow below it with a View Transition), so layout shift stays 0 for the line size.

3. **The engine**: port `reference/line-engine.js` as is into `lens.js` (it is pure, has no DOM, and is tested); load the words from the build, generated from `spec/line-copy.json`.

4. **Content hashes**: the build adds `data-hash` to every part; `lens.js` records `seen` with an IntersectionObserver (on screen 3 s or more, then scrolled past).

5. **Changes**: the change log is a by-product of the build's diff between releases, tagged with roles by the same rules as the parts.

6. **Live updates**: poll the release number (the site already exposes it) every few minutes while a page is open; on a new one, rule 4.

7. **Past view**: `?asof=` serves the stored release for that date with the line in borrowed tone; nothing is written to `seen`.

8. **CSP**: scripts are files, as today; no inline script.

### 11. The words

- Plain words, as the desk asked: "You're viewing this as", "That's me", "Not you? Read it as", "Show me", "Mark as seen", "Catch me up", "Back to today", "Read it anyway", "Switch to mine", "Make it mine", "Forget me on this browser".

- No site machinery in the reader's path: no version tags or commit hashes in "since you were here" (board 234).

- One "as of" per statement across the line, the hero and the answers (board 232). Today the thirty-second answers in `personas.json` still say "as of the evening of 22 October" while the page says 24 October; fix before rollout.

- The front page headline is the day's news (board 230): the mockups use the desk's wording, "Three days on: no confirmed break-ins, and the advice is now to check whether you were hit."

- Numbers in [brackets] in the copy are placeholders for the build.

### 12. Acceptance

- [ ] Every page has the line, at one of three sizes, with the chip first; it can't be closed.

- [ ] A first visit with no clues reads "You're viewing this as an Executive." with the six other roles visible without a tap.

- [ ] A visit from a CERT advisory starts as Security and says why.

- [ ] Choosing another role re-lays the page in place with no reload, says so in the line, and offers Undo.

- [ ] A shared link never changes a saved view unless the reader keeps it.

- [ ] A return the next day lists up to three changes for the role, and the changed parts are marked in the page.

- [ ] A return later the same day says "Nothing new for you since …" and folds read parts.

- [ ] After a week away, catch-up replaces the list.

- [ ] Looking at the past is borrowed tone, marks later changes, and writes nothing to `seen`.

- [ ] The team console shows the gate in the line and dims, not hides, the page.

- [ ] Never two messages at once.

- [ ] Layout shift 0 on load and between pages, measured; the line's row is reserved before first paint.

- [ ] Every page has a one line for every role, or the fallback.

- [ ] "Forget me" returns the browser to a first visit.

- [ ] The engine's tests pass (`node --test reference/line-engine.test.mjs`), ported or as is.

- [ ] Phone: the chip in the one-line header, the control as a bottom sheet, the headline in the top 250 px (desk review).

### 13. Rollout

1. The line and the boot script on every page, rule 7 only, with fallback lines. The lens control is removed. (Every page keeps working.)

2. Roles, readers and depth: the front page per role, then the agencies, the numbers, the playbook, the impact (board 141's order).

3. First visit and guesses (rules 3, 4 of section 4).

4. Seen, changes and the return moments (rules 5, 6); folding read parts.

5. Shared links, the past view, the gate (rules 1, 2).

6. Page lines for every page; the desk reviews the copy.

7. The reader's vault (board 140), telemetry (board 262).

### 14. Decisions for the editor

1. **Executive as the default**, over the General reader. Agreed in the session; noted because most arrivals from the news are general readers, which the guess handles.

2. **The team is not a persona**; team pages are gated in the line. Or a team sign-in later.

3. **The seven empty role × depth cells**: write readers for any of them (an Executive who wants it deep is the likeliest), or leave them to the role's defaults.

4. **Thresholds**: a new visit after 30 minutes idle; catch-up after 7 days or 20 changes; ask at most twice. All in `spec/moments.json`.

5. **Who writes the page lines**: story-site drafts, the desk approves, per page.

### What's in this pack

See `README.md` for the file index and the screenshots, and `prototype/index.html` to try it.

---

### What was built against it (story-site, 25 October 2026)

Prototype F, at `/admin/design/line/`: the front page, the agencies, the numbers, the playbook, a page for the

team, and a catalogue of every line the rules produce, all from the evidence vault of the release they were

built in. The engine and the spec are the pack's, vendored under `assets/design/line/`; the runtime

(`boot.js`, `line.js`, `line.css`) and the page builder (`admin/build/design.py`, `build_line`) are this

site's. The numbers the pack left as placeholders are filled from data at build time, so no sentence can

carry a number the vault does not hold. What is still to do is in the debrief and on the board.

This brief is the file `admin/content/briefs/2026-10-25__brief__the-line.md` in the repository, published as written.

← older: Brief: Wikipedia as an anchor, read as a fractal semantic newer: → Refactoring the site to URL paths and a single page: how a


---
site v0.22.23 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__brief__the-line/index.html
