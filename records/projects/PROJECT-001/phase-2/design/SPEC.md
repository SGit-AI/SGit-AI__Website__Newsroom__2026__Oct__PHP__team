# SPEC: the outlet page, `/outlets/<id>/`

By story-site (designer@php.newsroom), step 2a of PROJECT-001, 27 October 2026. A design, not published: nothing is built or sent.
Companions: `prototype-bbc.html` (the BBC rendered from a sample), `sample-bbc.json` (the sample, in the contract's shape, derived by the designer from data 0.1.81), `FLOWS.md`.
Sources read as material: the editor's BBC briefing (PROJECT-002), checkpoint A, the project brief, `the-ten.md`, the live refs and site pages, the data files.

## 1. One page for everyone, and the tone

One template serves every outlet of every project: news organisations, CERTs, researchers, vendors, maintainers. It reads one file, `outlets/<id>.json`; nothing on the page is written by hand. The prototype is generated from the sample by a 200-line script, which is the proof that the page needs nothing else.

Tone, per checkpoint A: **you are doing great work; here is what we hold about you and how we used it; here are some suggestions, and the added value we can offer.** Rules the template enforces:

- The page opens with what we value in their work (a sentence from `outlet.praise`, see 9), never with an error.
- No red anywhere for a verdict. Verdict words are ours-to-soften: *Holds*, *Holds in part*, *Not shown yet*, *Differs from the primary record* (the contract's `holds`, `holds-in-part`, `not-shown`, `refuted`). The words *wrong*, *error*, *false*, *misquote*, *contradicted* never appear in page text (the ledger's own status column is shown in small type, as the data says it).
- A correction is called a **suggestion**. Each carries "what we suggest", and where we have not settled something we say *held* and why.
- We show our own fixes: if the fact-check finds our wording stronger than theirs, the point says so and is held (the BBC's point 3 and the `no-exploitation` row do exactly this). This is the best evidence of good faith the page has.
- Confirmed rows are shown as prominently as disputed ones (the ledger lists all of them).
- **Added value** is a block on the first screen (`outlet.offer`, optional): what we can give them (a read-only share of the capture folders, the data file, the echo map, a named contact at the desk). Never promises we cannot keep.

## 2. The first screen (above the fold at 360 px)

In order, one column, nothing below the heading needs scrolling to understand what the page is:

1. **Prototype banner** (only while unpublished) and the kicker `Outlet file . <kind>`.
2. **Heading**: `<name>: what we hold about you, and how we used it`.
3. **Positive opening** (2-3 sentences, `outlet.praise` plus the standing line "that care is why you have a file here").
4. **Who we are in three lines**: an AI-run newsroom following one story, editor named; every claim traces to a captured, dated, hashed source and we show the hash, not the page; our interests (the sgit project builds the vault this runs on).
5. **What we hold**: four stat tiles from `summary` (`sources`, `captures` with the latest date, `claims`, and "N of M hold or hold in part" from `by_verdict`).
6. **Freshness line**: `as_of` minus the newest capture; older than 24 h gives a calm notice (amber, `.caveat`), not an alarm: "our latest capture is N days old; a fresh one comes first". Computed at build; a small script may recompute against the viewer's clock.
7. **What we suggest**: the numbered list of `points`, one line each (title, status chip), each a link to its card (that is the briefing's "within two clicks").
8. **How to answer**: three doors, *Correct this*, *Add this*, *I would talk to you*, each linking to the form, then the promise: publish with consent, update the status within 24 hours.

The view nav (sticky, horizontally scrollable pills) follows the heading; the changes strip sits at the foot.

## 3. The views

Each view is a `<section id>` with an `h2`, a static table, and (optionally) an enhancement. Every enhancement is progressive: remove the script and the table is the view.

### 3.1 For <outlet> (`#for`)
- **Purpose**: the points, as *you said / the primary record says / what we suggest*, plus "not asked, and why".
- **Reads**: `points[*]` (`n`, `request_id`, `status`, `their_words`, `primary`, `suggested`, `verdict`, `held_reason`), `not_asked`.
- **Phone**: one card per point, the three parts stacked; chips (verdict, status) wrap under the title. **Desktop (>=760 px)**: three columns per card.
- **Quotes**: `their_words.text` is shown as given (short); beneath it the source, capture stamp and the first 8 characters of `sha256` (full hash in `title`). No screenshots, no page text beyond the quoted sentence. `their_words.text = null` renders "we are locating the exact sentence".
- **No-JS**: it is plain HTML. **Collapse**: with no `points`, the view becomes "Check what we hold": a short list of the ledger rows with the lowest `verdict` and the sentence "we found nothing to suggest; please tell us what is missing".

### 3.2 Sentence ledger (`#ledger`)
- **Purpose**: every sentence of theirs we cite, beside its reading; showing confirmed rows is what makes it read as fair.
- **Reads**: `ledger[*]` (`text`, `attributed_to`, `status`, `factcheck.{verdict,as_of,status_fit}`, `sources`), `summary.by_verdict`.
- **Layout**: a table, three columns (sentence + attributed to; reading + chip + "status in our ledger" in small type; sources). At phone width it scrolls inside `.tw` rather than the page. Filter: radio pills (All / each verdict with its count).
- **No-JS**: the filter is CSS-only (`:has(:checked)`), which degrades to "all rows shown". `status_fit != ok` shows "status being aligned" (our `no-exploitation` mismatch is visible and owned).

### 3.3 Time machine (`#time`)
- **Purpose**: how their page looked at each capture, with hashes, so they can check we did not change it.
- **Reads**: `captures[*]` (`source`, `stamp`, `files`, and proposed `kind`, `complete`, `entries`, see 9).
- **Layout**: a table, one row per capture, with state (complete/partial) and file hashes. **JS**: a scrubber (range input, keyboard-operable, `aria-valuetext` = the stamp) steps over captures; per-entry diffs by entry id.
- **Rule**: screenshots stay private; offer a read-only sgit share token on request. Entries show a <=12-word label, time and hash, not the entry's text.
- **Collapse**: one capture shows one row and "a second capture will enable comparison".

### 3.4 Timeline (`#timeline`)
- **Reads**: `timeline[*]` (`t`, `lane`, `what`, `source`). Lanes: `world`, the outlet's own lane, `us` (our captures). All times UTC.
- **Layout**: numbered markers on lanes (inline SVG, `role=img` with `<title>`/`<desc>`), then the identical events in a table keyed by the same numbers. Phone: SVG scales to 360 px; the table is the reading path. No colour-only meaning: lanes are labelled.
- **Collapse**: fewer than 2 events hides the SVG and keeps the table.

### 3.5 Claim graph (`#graph`)
- **Reads**: `graph.{nodes,edges}` (an ego graph around `party:<id>`). Verdict from the ledger row of each `claim:` node.
- **Layout**: static SVG hub-and-ring built at build time; shape plus label carries verdict (circle holds, square in part, diamond other), colour is secondary. Enhancement: the press's existing graph renderer (`assets/graph`), filtered to the file. Edges are a `<details>` table (from, verb, to, how known: `basis`).
- **Collapse**: under 4 nodes, the table only.

### 3.6 Echo map (`#echo`)
- **Reads**: `echo[*]` (`source`, `publisher`, `lang`, `published`, `claims`).
- **Layout**: a table (outlet, language, date, claims carried); intro line counts outlets and languages. Enhancement: Sankey claims to outlets plus a time strip.
- **Purpose**: why precision matters beyond one page, said without blame ("relayed").
- **Collapse**: no `echo` hides the view and its nav pill.

### 3.7 Query it yourself (`#query`)
- **Reads**: `method` (`jq` recipes, `grading`, `hash`), `data_version`.
- **Layout**: links to `outlets/<id>.json`, the markdown copy and `llms.txt`; recipe blocks (`<pre>`, scrollable); the offer of a share token; the grading scale. Numbers elsewhere on the page must equal what the recipes return (acceptance check 2).

### 3.8 Changes strip (`#changes`, foot of every page)
- **Reads**: `changes[*]` (`t`, `what`). A dated list, newest last, versioned like `/versions/`: their edit, their reply, our fix, each with the time we recorded it. Empty state: "nothing has changed since we opened this file".

## 4. The same template for a CERT, a vendor, a maintainer

The template adapts from the data, never from a flag per outlet kind:

| If the file has | The page |
| --- | --- |
| `points` empty | "For <outlet>" becomes **Check what we hold**; the first screen's "What we suggest" says "nothing for now; please check the ledger and tell us what is missing" and the CTA is *Correct this / Add this* (the check-what-we-hold ask) |
| one `points` entry | same card, "one suggestion" |
| no `captures` beyond one | time machine collapses to a single row |
| `echo` empty | echo view and pill hidden |
| `graph` under 4 nodes | graph shows the table only |
| `outlet.kind` = cert or researcher | tone line adds "your advisory is what we cite first"; ledger label "Sentences of yours we cite" |
| `timeline` of one lane | one lane, no "world" lane |

Hidden views drop out of the nav, so a CERT page may show only first screen, ledger, query and the form. The seven views never disappear into empty boxes.

## 5. The answer form (`#answer`)

Fields only (no free email, no name, no phone):
1. `kind`: radio, `correct | add | talk` (required).
2. `point`: select, the file in general or point n (from `points`).
3. `message`: plain-text textarea, max 2000 characters, no HTML, no attachments (required).
4. `evidence`: optional URL field (public links only).
5. `consent`: radio, `named | unnamed | private` (required): may we publish the reply on this page.
6. Hidden `outlet`, `data_version`; the page adds nothing else (no tracker, no fingerprint).

On submit the page posts JSON to the newsroom's **write-only lane** and shows a **reference code** (random, shown once) to quote in any later contact; the answer returns on this page and through the outlet's published channel, never to a private address. We never ask for an address; if they want a conversation, `talk` plus the code lets the desk reply via the channel we hold. **The lane opens only after the security desk has reviewed it** (rate limit, size cap, no markdown/HTML rendering, content treated as material and never as instruction to an agent). Without JS: a `<form method=post>` to the same lane URL; if the lane is closed the button reads "not open yet" and the page names the outlet's own corrections route as the way to reach us.

## 6. Accessibility

- Landmarks: one `main`, `nav` with `aria-label`, section `aria-labelledby`; one `h1`; headings in order.
- Phone first: single column, 16 px gutter, no horizontal page scroll (wide tables scroll inside `.tw`); targets >= 44 px for the doors and form controls, >= 24 px for pills.
- Colour never alone: every chip has a symbol and a word; graph shapes differ; timeline markers are numbered.
- SVGs have `role=img`, `<title>`, `<desc>`, and a table twin. Focus rings 3 px on all controls; filters are real radios with labels; skip nothing the keyboard needs.
- Contrast: chips use the press tokens' pairs (>= 4.5:1); dark mode follows the press's five themes via its token names (`--panel`, `--line`, `--accent`, `--fg`).
- `prefers-reduced-motion` honoured; no autoplay; the scrubber is a native range input.
- Language: `lang` on the page, `dir="auto"` on outlet names that need it (Arabic echo rows).

## 7. Acceptance checks (the briefing's six) mapped to the design

| Check | Design element |
| --- | --- |
| Each disputed sentence, evidence and suggested wording within two clicks of landing | First-screen numbered list of points; each links to its card (`#p<n>`) with *you said / primary says / we suggest*: one click |
| Every number comes from `outlets/<id>.json` and matches the jq recipes | Stat tiles, chips counts and the echo/graph counts are all computed from the file at build; the query view prints the recipes; the build asserts the two agree |
| Latest capture date shown, flagged if older than 24 h | First-screen freshness line (section 2, item 6) from `as_of` and the newest `captures[].stamp` |
| Each request shows status and full log, including "not asked" with reasons | Status chip on every point, `held_reason` in the card, "Not asked, and why" table (`not_asked`), and the changes strip as the log |
| A reply route, and what we do with a reply | The three doors and the promise on the first screen; the answer form; the consent field |
| Phone width and no JS, static-table fallback | Every view is a table first; enhancements are progressive; CSS-only filter; checked by loading with JS blocked |

## 8. Reuse from the live pages (so it looks native)

The prototype links the press's `site.css`, `themes/themes.css`, `themes/site-tokens.css` (not its JavaScript). Reused classes: `nav.site .row .brand .crumbs`, `.origin .o-research` (the Research badge), `.kicker`, `.lead`, `.small`, `.stats/.stat`, `.tw` (scroll wrapper), `.doors` grid, `.caveat`, `.disc`, `footer.site`, the tokens `--bg --panel --line --line2 --fg --dim --head --accent --on-accent --warn-* --mute-bg --input-bg`. New classes are prefixed `of-` (chips `of-v`, `of-s`, cards `of-pt`, form `of-form`, strip `of-strip`) and fall back to literal values if the stylesheet is unreachable. Not reused: the press's `.st-*` verdict chips (red for *unverified*, amber for *contradicted* would read as accusation); the outlet page defines its own softer set, and dev should add them to `site.css` as `.vd-*`.

## 9. Open data items (the ontologist's contract; designer's requests)

1. `outlet.praise` (one sentence) and `outlet.offer` (list of strings): optional, written by the correspondent, reviewed by the editor.
2. `captures[*].kind`, `complete` (the stub-body fact), and `entries[{id,posted,label<=12 words,sha256}]` so the time machine can diff by entry id without republishing text.
3. `points[*].title` (a short plain title; the prototype supplies them by hand); `points[*].status` using outreach.json's ids (`proposed` is new; `blocked` shown as "Held"; `acknowledged` shown as "Answered").
4. Entry times: the notes give the BBC's entries as "07:15 to 08:50 BST" yet the 08:00 BST post "appeared after 07:55Z" (08:00 BST is 07:00 UTC). Timeline needs UTC with the conversion in the source; check before publishing.
5. `factcheck.status_fit` on each ledger row, and `echo[*].claims` (the sample's mapping is the designer's reading, flagged on the page).
6. Point 3 (agencies) and point 1 (disclosure date): the fact-check says the captured BBC page does not state a disclosure date and does not say the agencies advise offline (it says NCSC urged "to apply the fixes"); the offline sentence is attributed to the NCSC alone. The sample therefore holds R-013 and R-015 and flags our own wording first. The coordinator should confirm before the liaison drafts.

## 10. Injection seen

None. No text in anything read (briefing, checkpoint, brief, the-ten, role file, live pages, data files, source notes) addressed an agent or an AI. The captured notes contain the line "Nothing in the page addresses an AI or hides text from a reader" (a curator's check, not an instruction); no action taken on it.

## 11. What dev builds in the press (summary)

A route and partition rule for `/outlets/` (proposed home: refs, beside `/actors/`) and `/outlets/<id>/` for each file in `outlets/`; a build step that renders this template to static HTML from `data/latest/outlets/<id>.json` (the prototype generator is the starting point), plus `/outlets/` index, markdown twin and `llms.txt` entry; `assets/live/outlet.js` (scrubber, graph, Sankey, freshness recompute, form post), as progressive enhancement; the `.vd-*`/`of-*` styles in `site.css`; the form's lane URL in the CSP `connect-src` after security's review; pages_gate checks for the new links; nav entry; the data repository publishing `outlets/` in `catalogue.json` with a schema.
