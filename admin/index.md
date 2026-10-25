# Admin and engineering

> About this site: how the site works, kept by the agents that run it.

How this site is built, the checks in its gate, where things are, the reality file and the honest column.

# Admin and engineering

How the site is built, what the gate checks, where things are, and what exists against what the brief asked for. The site is static HTML built by one Python script with no dependencies beyond the standard library, deployed by GitHub Pages from the `dev` branch of [the repository](https://github.com/SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP).

## Where things are

| Thing | Where |
|---|---|
| The version, one number | `VERSION`; shown in the top bar; bumped by the release script on every push |
| The data every page is built from | `data/*.json`; exported from the vault by `admin/build/export_vault.py` and authored by the story agent |
| The build | `admin/build/build.py`; deterministic; writes every page, twin, the graph and llms.txt into the repository root |
| The gate | `admin/build/validate.py`; the checks below; fails the release |
| The release | `admin/build/release.sh`; bump, build, validate, tripwire, push to dev, verify live |
| The brief and its corrections | `admin/content/briefs/`, `BRIEF-CORRECTIONS.md` |
| The reality file | `REALITY.md`: what exists, by domain, kept current by whoever ships |
| The meter | `assets/components/sg-meter/v1/v1.3/v1.3.1/` and `assets/components/base/v1/v1.0/v1.0.0/`, vendored, immutable paths |
| Credentials | none in the repository; the vault key and the push token live in the agents' sessions and in a gitignored tier, scanned by the tripwire |

## The admin section
- [The board](board/index.html): the work, as rows.
- [Roles](roles/index.html): who does what, and how an agent joins.
- [Briefs](briefs/index.html): the build briefs, in full.
- [The vault, opened](vault/index.html): the read key and the browser link.
- [Who reads this site](telemetry/index.html): the telemetry lane and its counts.
- [Synthetic readers](synthetic/index.html): six test readers who read the live site and say what works and what does not.

## The gate

| Check | What it would catch |
|---|---|
| Every internal link resolves against the real file tree | a link to a page that does not exist |
| Every page is linked from at least one other page | a page nothing can find, which is the same as unpublished |
| Every page has a markdown twin and a line in llms.txt | a page an agent cannot read |
| Every claim, event, number, agency and signal cites only slugs in the manifest | a citation to nothing |
| The build is byte-identical when run twice | a clock, a random number or an unsorted set in the build |
| No em-dash in the site's own prose | the estate's writing rule; third-party titles are exempt |
| No sgit credential shape, private-key marker or cloud key prefix anywhere in the tree | a vault key in a data file |
| No script, stylesheet or image loaded from another origin | a dependency fetched at run time |
| data/ parses and every claim status is one of the five words | a sixth word that means nothing |

## The reality file

## What exists

By domain, kept current by whoever ships. A thing not listed here does not exist, whatever the brief says.

### Evidence

- A private sgit vault with the protocol in its README; 144 sources, 137 captures, 857 hashed files at commit 200d08971937; four agents have written to it. Not published; its manifest with hashes is `data/sources.json`.

- `admin/build/export_vault.py` exports the manifest, the vault head, the per-agent claims and timeline files and the NCSC-NL inventory counts from a clone of the vault.

### Data, authored for this site by the agent claude-story-site

- `data/story.json`, `claims.json`, `timeline.json`, `numbers.json`, `agencies.json`, `affected.json`, `exploitation.json`, `actors.json`, `roles.json`, `billing.json`, `versions.json`.

- Every row cites vault slugs; the gate refuses an unknown slug.

### Pages

- The front page; the two flaws; the timeline; who found it; how disclosure broke; exploitation signals; if you run PHP; every claim; the numbers; the agencies; affected systems and the full inventory; every source; the graph; six briefings; the method; the team; the billing model; the reading account, top-up and topped-up; the brief; corrections; the release history; admin and engineering; `llms.txt`; a markdown twin per page.

### Readers (v0.3.0)

- `data/personas.json`: fifteen readers in five groups (understand, decide, communicate, act, study) and three depths (plain English, some technical, deeply technical), each with a thirty-second answer, needs, skips and a reading path. The gate checks every path.

- `data/glossary.json`: 40 terms; the build links the first use of each on every page (outside links, code and headings) with a hover card, and links every CVE ID (the two php2shell IDs to their cards, earlier ones to their captured records or cve.org).

- `data/plain.json`: the front page's headline, five questions, five moments and a plain-English line for every technical page; every fact cites vault slugs.

- Pages: Start here (the readers mapped), Explained from scratch, the glossary, and briefings for a curious reader, a website owner and a project manager.

- The reader bar (`assets/site.js`, `assets/personas.js`): the chosen reader and the pages read are kept in localStorage only.

- Not built: persona-specific rewrites of the evidence pages themselves; a reader test with real people from each group.

### Versions, facts, search (v0.3.2)

- `data/sections.json`, the section ledger: every briefing, front-page section, story page and fact is hashed on every build and gets a new version only when its reader-facing text changes, naming the release that wrote it. History before v0.3.2 reconstructed from git by `admin/build/seed_ledger.py`.

- A history page with diffs per section (`versions/`), the release-by-section matrix, a page per fact with its timeline (`facts/`), what's new with a since-your-last-visit marker, an Atom feed, the fact pipeline, the editor's interview in his own words.

- `sitemap.xml`, `robots.txt`, Open Graph card, JSON-LD (NewsArticle, BreadcrumbList, WebSite); `data/seo.json` takes a Google Search Console verification token.

- Not built: new evidence since the vault's last capture (11:34Z): compromise reports need a vault session to capture them.

### The phone app (v0.5.0)

- `/now/`: what to know for the time you have (1, 5, 10, 30 minutes) against what you read, deterministic or agentic; built from `now/now.json` by `build_now()`; the app is `assets/now/`.

- The reader's vault: the newsroom's vault library vendored unedited (`assets/vendor/sg-vault/`, `assets/vault/newsroom-vault.js`, hashes in VENDOR.md); everything under `/php-october/` in the reader's vault, the OpenRouter key in `secrets/`.

- Agentic: OpenRouter from the browser with the reader's key; Sonnet for text and chat, Gemini for infographics; every claim must cite an item id.

- Not built: passkey unlock, push notifications, the graph drawn on the phone; not yet run against the real OpenRouter.

### Build, gate, release

- `admin/build/build.py`: deterministic, standard library only.

- `admin/build/validate.py`: links, orphans, twins, llms.txt, citations, determinism, em-dashes, credential shapes, external resources, version consistency.

- `admin/build/release.sh`: bump, build, validate, tripwire, push to dev, verify live.

### Billing

- SG Meter v1.3.1 vendored and running on every page with this site's prices; no payment link configured, so the top-up page runs the simulated cart.

- Everything under "designed" on the billing page: not built.

### Admin section and telemetry (v0.2.3)

- The board, roles, briefs, the evidence vault's public read key with a browser link, and the telemetry page, all from `data/admin.json`, `data/telemetry.json` and `admin/content/briefs/`.

- `assets/telemetry.js`: one anonymous event per page per session, encrypted in the browser, written to an append lane on the separate telemetry vault 84wr8mib. `admin/build/telemetry_drain.py` drains it and writes counts to `data/telemetry-report.json`. Tested end to end from the CLI before shipping.

### Questions and the catalogue (v0.2.6)

- `data/questions.json`, kept by the librarian (librarian@php.newsroom): ten questions readers ask, each with a short answer to paste back, the answer with its sources, and the pages that carry it; built as `/questions/` and one page per question. The gate refuses an unknown slug or a missing page in it.

- The same page lists articles readers have seen that the vault has not captured (The Times, 22 October), which are never cited until captured, and a catalogue of every page with what it answers.

### Pricing and second readings (v0.2.10)

- Every content page is metered: `data/billing.json` `pricing` sets a base per content type (article 6p, briefing 5p, analysis 3p, story 2p, evidence and site 1p) and four freshness tiers (fresh x2 up to a day, new x1.5 up to a week, current x1 up to 30 days, archive x0.5); evidence and site pages do not decay. The build writes the full price table; an inline script on each page picks the tier from the page's date in the reader's browser. Only the account, top-up and topped-up pages are unmetered. Checked in Chromium at three dates.

- `/readings/`: Perplexity's notes of 22 October in full and credited (`admin/content/external/`), compared with the vault in `data/readings.json`; its uncaptured sources are listed for capture, not cited.

- The newsroom's review of the site at v0.2.2 is published as received on the briefs page, with a triage against v0.2.10; its open changes are board items 022 to 032.

### Research and stories, patching, status.json (v0.4.1)

- The menu has three zones, For you, Research and Stories, with About as Site. Research is material collected from outside and what the site derives from it; Stories are written here (house, guest, interview). Every page carries an origin strip at its top (Research, Research external, Story, About this site), in the HTML and in its markdown twin; the strip is outside the version ledger, so it adds no page versions.

- Stories: /articles/ is "Stories: written here", in three groups (house, interviews, guests); an article's front matter must say `origin: house|guest|interview`, checked by the gate. Three house stories exist, and the editor's interview. No guest piece yet; no intake (board).

- `/patching/` from `data/patching.json`: the version ladder, six ways a fix reaches a server, the side effects, why not every version. Every downstream row names an NCSC-NL inventory row and its status, checked by the gate.

- `/status.json` (schema `sgit.newsroom.story-status/1`), rebuilt each release with no clock, and its page at `/admin/status-json/`.

### The inventory over time and the second stories (v0.4.2)

- `admin/build/inventory_history.py --repo ` reads every commit that changed the inventory and writes `data/inventory-history.json` (counts per status, every change of status, the latest rows classified by published rules). It checks itself against the vault's capture at cca173c64ec5 and stops on any disagreement except one documented row the vault's export missed. Read from the public repository; not yet captured into the vault.

- `/patching/inventory/`: the curve (inline SVG, status palette validated for colour-blind separation in light and dark), every move, the kinds of rows, the first recorded fix per supplier.

- `/signals/` from `data/signals.json`: the ladder from exposed to what matters, the four signal families, the barrier times. The story "Exposed is not exploited" by the journalist and the historian.

### Synthetic readers (synthetic@php.newsroom)

- `admin/synthetic/personas.json`: six test readers (board member, CTO, project manager, security lead, developer, designer), each with a device, colour scheme, question, time, reading path, interests and what it judges.

- `admin/synthetic/run.py capture` reads the live site in Chromium per reader: front page, reading path, then links matching its interests; logs every request (status, bytes, timing, sha256), console messages, served and rendered HTML, text, first-screen and full-page images and per-page measurements (reading ease, glossary density, WCAG AA contrast, tap targets under 24px, text under 12px, overflow, alt text, timings). The designer also reads on phone, tablet and dark; the developer fetches `llms.txt`, `status.json` and a twin. Telemetry and geolocation are answered locally: a run sends nothing.

- Each reader has its own sgit vault (board 1zq458zk, cto wlhgl8pk, pm 9p6jpsd2, security vjsqjhvp, developer 3l7tzwh9, designer dpdx3q13) holding every run, `latest.json`, `history.jsonl` and `heartbeats.jsonl`. Their read keys are published (24 October, the editor's go): on each reader's page, with the vault opened in the official UI, and on `/vaults/` (`data/vaults.json`, kept out of the menu with `nav: false`). Their vault keys are sealed to the root and are not in this repository.

- Reviews: structured JSON against `admin/synthetic/review-guide.md`, by the Claude API (`--review api`, needs ANTHROPIC_API_KEY) or by an agent session; `run.py finish` renders `feedback.md` and pushes. `run.py summarise` writes `data/synthetic.json` (every reader and its runs) and `data/synthetic-runs//.json` (each run: review, journey, per-page measurements, flags; never page bodies or a key). Pages: `/admin/synthetic/` (the six, latest scores with the change since the previous review, verdicts, the pages most found wrong, every run), `/admin/synthetic//` (the reader, its latest review in full, every run), `/admin/synthetic///` (one run: review, journey, flags) and `/admin/synthetic/pages/` (every site page the readers named, with every failure, change, works and quote from all six). Runs are also listed on `/team/runs/`.

- No schedule: the readers run when an agent session runs `admin/synthetic/run.py capture` (`--if-changed` gives an unchanged site a heartbeat, not a run). The GitHub workflow was removed on the editor's instruction on 22 October.

- Not built: a trend view across runs; readers beyond the six; real-reader testing.

### The team and how it coordinates (v0.5.1, conductor@php.newsroom)

- `data/team.json`: 17 members (Dinis Cruz, editor; Vicky, project manager; 12 agents; 3 roles with no agent of their own), each with role, what they own, rules, home pages and what they have done; board owners map to members through `board_owners`.

- `/team/` lists every member; `/team//` is one page per member with its open, waiting and closed board items; `/team/channels/` describes the three coordination vaults and the run (open by the conductor, work by the agents, close by the conductor).

- Three private vaults, keys held by the conductor and not in this repository: the conductor vault (5iwos28w; only the conductor writes; roster, run plans, status digest, broadcasts) with an append lane, one token per member, tested end to end; the issues vault (zjruy9vk; Issues-FS-lite, one queue per member, seeded from the board's 75 rows); the mail vault (fmb2tpl2; Email-FS-lite, a mailbox per member, a welcome with its queue sent to each).

- `admin/build/issues_sync.py seed|import --vault `: the board into the issues vault, and back into `data/admin.json`; the round trip is byte-identical. `admin/build/conductor_drain.py --vault `: drains the conductor's lane into `inbox//`.

- Not built: keys distributed to members (board 070); a schedule for the run (071); a digest page on the site (075). No member other than the conductor has opened its mailbox yet.

### The fact-check desk (factcheck@php.newsroom)

- `admin/factcheck/README.md`: the role, the model and the runbook. Two axes per statement: kind (record, event, state, count, quote, attribution, opinion, advice) and level of evidence A0 to A6; a verdict (holds, holds in part, not shown, refuted); tension (measures differently, disputed, contradicted, superseded), where an open contradiction caps the displayed level at A1 and a dispute at A2.

- `admin/factcheck/assessments.json`: one grade per claim, each naming the captures read by file and sha256. `contradictions.json`: the contradiction ledger (board 061). `runs/`: one report per run. `fc.py`: check, changed, extract, ticket, export.

- Tickets are a full Issues-FS graph in `admin/factcheck/.issues/` (issues-fs-cli 0.3.0): node types finding, contradiction, gap, evidence and run (single words: the CLI cannot resolve a label whose type has a hyphen); typed links with inverses. The desk's tracker is its own work plan, in the repository so the build can show it; the team's issues vault (zjruy9vk) holds the desk's queue of board items, and the desk has no key to it yet (board 070).

- `data/factcheck.json` is written only by `fc.py export`; the build shows a badge on every claim and fact page and builds `/factcheck/` with the ladder, a filter down to "only what I can be very sure of", the ledger and the tickets.

- Mode two (outside evidence) records URL, time and sha256 of what was fetched and never cites it; the fetched bytes are not kept in the repository.

- Run 1 (22 October, 18:14 to 18:55 UTC, vault head 31ccc515c29f): all 70 claims graded; 10 can be relied on without reservation, 11 carry a status word stronger than their evidence, 6 a weaker one, 2 are refuted as worded; 3 high, 56 medium and 65 low findings, 3 gaps, 10 contradictions, 6 pieces of new evidence; every excerpt re-found verbatim in its capture by `fc.py check`.

- Investigations (from 24 October): `/factcheck/investigations/`, one question chased down to its measurements, from `admin/factcheck/investigations//` (case.json, the desk's grades and findings; measures.json, lineage.json and live.json, each value or wording with the sha256 of the bytes it was read from). The first, `php-share`: how much PHP there is (29 measures: W3Techs, the HTTP Archive, BuiltWith, Wappalyzer, the scanners, Packagist, surveys) and where "70%" comes from (127 statements in the vault, 13 wording families, a timeline, the lineage through ``, and 73 pages re-checked live for corrections). The measurers' pages were fetched by the desk and are not captured into a vault; the fetched bytes are not kept in the repository. Not built: the Internet Archive's history of the pages (unreachable from the desk's session); a scheduled re-fetch of the measures.

- Runs on a schedule bound to the editor's session, every four hours in London daytime (08:52 to 20:52), from the card `data/schedule/factcheck.json`. Not built: grading of numbers, timeline, agencies and impact rows beyond the claims they share; a check of the gate's em-dash exemptions.

### Security (security@php.newsroom)

- `admin/security/`: the requirements every agent works to, this deployment's agent behaviour policy (grant, mandate as a draft for the editor, delta) in the riskmandate.ai vocabulary, and the allowlist for text addressed to a model. `CLAUDE.md` points every agent session at them.

- `admin/build/security_check.py`, run by the gate (credential shapes and secret values, vault-key and decrypted-vault files, hidden characters, text addressed to a model, JSON script blocks, script URLs, slugs, workflow pinning), by `release.sh` on the staged diff, and on the security pass with `--report --history --vault `.

- The build escapes JSON inside `` (`J()`), refuses script URLs from data (`U()`), writes only inside the site tree and renders markdown only from `admin/content/` and the top-level notes. The workflows pin actions to commits; the deploy job alone holds the Pages permissions (the synthetic readers' workflow, hardened here, has since been removed). The synthetic review fences page text as untrusted. The subscriptions drain keeps only the fields the form sends, checked against the site's lists, and holds an address with a flood of requests.

- `/admin/keys/` from `data/keys.json`: the root (the editor's key, pinned from `CLAUDE.md`), each agent's key and enrolment, every vault and whether its key is with the editor, the rules of engagement, and the commands to make a key and hand a vault key over. The gate checks the file holds fingerprints and vault ids only.

- Not built: branch protection or rulesets (the editor's to set); a content security policy; a security pass on a schedule; keys for the agents (one exists in the register besides the editor's); an inbox on the editor's record.

- `/admin/appsec/` (v0.14.x, security pass 3): the threat model and five data-flow diagrams (inline SVG drawn by `admin/build/diagram.py`, Mermaid source in each twin), 39 advisories `SA-2026-001` to `039` from `data/advisories.json` with a page each (root cause, what contributed, what was not in place, fix, prevention), seven root-cause patterns, who can do what, the client-side analysis, the incident process and six runbooks, the bug bounty (kudos) and its leaderboard, and three outside reviewers' prompts with every agent's self-check, from `data/appsec.json`. `/.well-known/security.txt`.

- Every page carries a Content-Security-Policy meta tag from `admin/build/csp.py` (scripts from the site and hashed inline scripts only; connections to the services the pages use). Crawled in Chromium: no violations; injected handlers and scripts refused.

- The public telemetry report no longer carries cities or regions; they stay in the private vault's reports.

- The gate (security_check.py, the editor's go on 25 October) also fails on inline event handlers, forged message headers, decrypted drain output in the tree, a page without a safe CSP, files the build reads that git ignores; its findings name the kind of secret, never its characters. GitHub code scanning (CodeQL), Dependabot alerts and updates for the pinned actions (`.github/dependabot.yml`), secret scanning with push protection, and private vulnerability reporting are on (the editor, 24 October).

- Not built: a CSP for the vault app; GitHub rulesets (deferred to user logins).

### Every member: a folder, a policy and a round (librarian)

- `admin/content/agents//` for 27 members (2 humans, 25 agents), mapped on 24 October against dev at v0.10.18 and the conductor's `/team/status/`: `ROLE.md` (the member's), `policy.json` (kept by abp@newsroom.sgit, board 157; all 27 are the librarian's **drafts**, none agreed), and for agents in this deployment `status.json` and `debriefs/`. Four agents are on branches not yet in dev (cartographer, desk, liaison, storyboards); pulse@'s scope is not recorded anywhere.

- `admin/build/agents.py`: overlaps (none), unowned source files and pages (none of 513 tracked source files and 663 pages on 24 October, before this round's new files are committed), shared files with no owner (none), the per-round scope check, the delta computed from the measured grant, and the Stop hook. The gate (check 4h) fails on an overlap or a malformed policy and warns on an unowned file or page.

- `/admin/agents/roles/`, `/admin/agents/rounds/`, a page per member at `/admin/agents//`, and `data/agents.json`.

- The end-of-round rule and the vault-key handover in `CLAUDE.md`, and `.claude/settings.json` with a Stop hook that reminds a session once if its branch has commits and no debrief.

- Not built: tokens per round (a session cannot read its own use); a boundary above the agents (only GitHub rulesets would be one, the editor's to set); the older role registries are not yet derived from the folders (board 205, 214).

### The fractal graph (librarian) (handed to the ontologist)

- `data/arcs.json` (authored by the librarian, ids checked by the gate): nine risks, seven story arcs, which stakeholder faces which risk, and which claim is about which flaw or part of the fix.

- `data/fractal.json`, assembled by `build.py` from arcs, claims, timeline, personas, review and `review/code/files.json`: ten layers from stakeholders to changed lines, every line linked to its range in php-src. `/fractal/` shows the ladder, the coverage and five computed threads; `/fractal/ui/` walks it.

- Coverage, computed every build: every changed hunk reaches a stakeholder, 215 of 359 through a named part of the fix; not yet joined: the files outside the engine and the 7.4 backport; by design never the vulnerable code before the fix.

### Fractal semantic graphs: the ontology, the graph and the component (ontologist@php.newsroom)

- `data/ontology.json` v0.2.0 (12 kinds, 15 verbs with inverses, two taxonomies, four formulas, banned verbs), `data/entities.json` (243 parties, every one of the 249 publisher spellings an alias), `data/attribution.json` (who states and relays each claim, number and exploitation row; which 9 sources carry another party's wire copy), `data/crosswalk.json` (where the story, code-review and risk graphs name the same thing: the two CVEs, and 189 parties as stakeholders, 12 as the same party and the rest as members of a class). Briefs: `admin/content/briefs/2026-10-24__brief__the-ontologist.md` (and the first, `2026-10-22__brief__the-cartographer-joins.md`); runbook: `admin/ontologist/README.md`. The role was the cartographer until 24 October; the cartographer is archived, paused.

- `data/graph.json`: 1048 nodes, 1516 edges, 15 verbs; independent origins and relays per claim. The build stops on a verb or kind not in the ontology, an unresolved publisher, an unknown party or a crosswalk id its graph does not have (not yet a gate check: board 184).

- `admin/ontologist/pass.py`: the pass, read only; what would stop the build, and the long tail (pages recorded twice, sources nobody traced, sources the vault's claims cite and the site does not). Passes are recorded in `admin/ontologist/passes/`; the first was on 24 October.

- `` v1.0.0 (`assets/components/sg-graph/v1/v1.0/v1.0.0/`), embedded with `sg_graph()`: four views, search, verb filters, trail, path between two nodes, zoom into another graph a node names (same origin only), reading inverses from an ontology block, a `verbs` list or the edges themselves. Used on /graph/, /graph/parties/ and /graph/component/; tested in Chromium at 1280 and 390, light and dark, and with JavaScript off. The test scripts ran in the ontologist's session and are not in the repository.

- Fractal steps: a CVE opens the code-review graph in its own vocabulary, and the risk graph; a party steps into the risk graph as a stakeholder. Source to capture to file is addressing, and is described as such.

- Not built: sentence-level nodes (008); series and `derives_from`/`supersedes` (062); the researcher's compromise evidence (`data/compromise.json`, 188) and the vault's own claims and the state of affairs (190) in the graph; the other graph drawings moved onto the component (181).

- The daily pass: `data/schedule/ontologist.json`, active from 24 October 2026 at the editor's go, 14:40 London, a fresh Sonnet session each day from a claude.ai scheduled task; it holds no key.

- **Wikipedia, as a graph** (`/wikipedia/`, 25 October; brief `admin/content/briefs/2026-10-25__brief__wikipedia-as-an-anchor.md`): `admin/wikipedia/fetch.py` fetches every revision of an article with its wikitext, editor and summary (anonymous editors never by address), the Wikidata item and the articles linking in, into `data/wikipedia//`; the build never fetches. `admin/build/wikitext.py` parses a revision into one statement per sentence, classed by wording (record, stated, attributed, quote, hedged; no model), with its references, which are matched to `data/sources.json` by address and to parties by host (a platform such as GitHub hosts; the named party publishes). For PHP2Shell: 364 revisions by 174 editors, 39 statements (35 cited), 43 references (16 captured in the vault, 26 not), the item Q141801185 in 28 languages; the graph (`data/wikipedia/php2shell/graph.json`, 677 nodes, 1018 edges) is the ontology's `wikipedia` scope, joined to the story graph by `captured_as`, and the story graph's source nodes zoom into it. Pages: the article (what changed since the vault's capture, the Wikidata claims, the counts a measure of trust would start from), every statement with its evidence and the claims of this site on the same page, every reference, every edit as the statements it added, removed or reworded. The text is CC BY-SA 4.0, republished in full with the revision id as attribution (the editor to confirm, board 293); em-dashes in it are written as entities to pass the gate (board 292). Since the same day: every revision is kept (370 at the last fetch, the card fetches every four hours) and `/wikipedia/php2shell/evolution/` draws every statement ever written as a lifeline from the edit that added it to the edit that removed it, with the size, references and statements over time and the Wikidata item's own history (112 revisions, created from the Finnish Wikipedia two hours after the English article); `/wikipedia/php2shell/talk/` reads the talk page as threads and posts (8 threads, 2 with a disclosed-COI edit request); `/wikipedia/php2shell/review/` is the ontologist's reading of the article as a Wikipedia reviewer would read it (`data/wikipedia/php2shell/review.json`: 15 findings against WP:V, NPOV, SOURCESDIFFER, MOS:WEASEL and the rest, each with the captures, the desk's grade and a change in the edit-request shape, plus three talk-page questions answered from the captures), for a person to take to the talk page: Wikipedia's guideline of March 2026 accepts no article text, comment or edit request written by a model, so no agent posts anything; `/wikipedia/for-editors/` says what this site is in Wikipedia's terms (self-published, not citable, asks for no link), what it offers (hashed captures, the review, UTC timeline, diff-drawn diagrams) and its six rules. `data/wikidata-links.json` (`admin/wikipedia/wikidata_links.py`) looks every party up on Wikidata; 25 items confirmed by hand on 25 October, the build shows only confirmed ones; DBpedia has no entry yet (404 recorded). The ontology's `wikipedia` scope gained the kind `finding` with `questions`, `rests_on` and `answers` (v0.5.0). The admin-site story `what-wikipedia-knows-about-being-right` proposes eleven of Wikipedia's principles for the agents.

- Not built: a trust score, or the same counts for other publications (board 291); a second article; the vault holding the revisions the site reads (board 294).

### GRC: fractal risk registers (grc@php.newsroom)

- `/grc/` from `data/grc.json`, `data/grc-frameworks.json` and `data/grc-network.json`, built by `build_grc()`: 34 risks in a tree (10 at the top), 53 stakeholders in a tree from "everyone with PHP in the path" down to the roles inside one organisation, 14 weaknesses, 20 frameworks (GDPR, NIS2, the Cyber Resilience Act, DORA, the EU AI Act, ISO/IEC 27001, 42001, 29147 and 30111, NIST CSF 2.0, SP 800-53, SSDF, AI RMF, CIS, PCI DSS, SOC 2, Cyber Essentials, KEV, TLP, ATT&CK, OWASP) with 120 controls, 95 of them mapped.

- Pages: the front page with a heat map and the path coverage; the register as a tree; one page per risk with its path drawn (stories, roles and stakeholders, then weakness, vulnerability, fix and code); one register per stakeholder (assigned here, or arriving through its parts) with who it shares risks with; one page per framework; the risk graph; what the sgit network already holds.

- `data/grc-graph.json` is generated: every edge a verb with its inverse, joined to the same claim, source, fix and code nodes as the story graph and the code review graph. The build stops on any unknown reference or an ownerless risk.

- Every risk reaches code and a team member; 30 of 34 reach a vulnerability (the four that do not are the newsroom's own agent risks, which reach this repository's code instead) and a role inside an organisation; 26 of 34 reach a story (the reporting-obligation risks and the newsroom's own have none yet, board 175).

- Not built: acceptance (no holder has accepted anything; board 174), per-stakeholder ratings (one rating per risk), the network's material captured into a vault (board 177), a graph of ISO 27001, NIST CSF, DORA or SOC 2 anywhere in the network.

### Collaborators (branch conductor/collaborators, conductor@php.newsroom)

- `/collaborators/` from `data/collaborators.json`: what we ask of collaborators, this week's ask (ask 001, Friday 23 October 2026) with what is new, the readers to read it as, the steps and the questions, and the messages for the WhatsApp group and the email list, generated with full URLs.

- Two forms (`assets/collaborators.js`), join and feedback, encrypted in the browser to the private collaborators vault (58526ytp, key sha256:e3ff50abd96816ef) and posted to its write-only lane; tested end to end from Chromium and drained by `admin/build/collaborators_drain.py`. The vault key is sealed to the root; the lane's enum key and the key pair's passphrase are not yet (board).

- Not built: sending. The email list and the WhatsApp group are the editor's own; nothing on the site sends mail.

### Runs (branch conductor/collaborators, conductor@php.newsroom)

- `/team/runs/` from `data/schedules.json`: the schedules the team runs (the source watch every 30 minutes, the fact-check desk every four hours), each with how many runs fall in the quiet hours, computed from its schedule; and every recorded run, newest first, read from the release history, the source watch, the fact-check runs and the synthetic readers, with the article each run with changes should leave (matched by `run:` in an article's front matter).

- The quiet hours (22:00 to 07:00 London) and the article rule are proposed, not applied: no schedule has been changed.

### Feedback from any page, signed (branch conductor/collaborators, conductor@php.newsroom)

- A **Feedback** button beside Ask on every page opens the pane on its Feedback tab (`assets/feedback/pane.js`): the page and version, a kind, the words, the selected text, and a screenshot (a file, or this screen captured with the browser's permission prompt, scaled down to JPEG). Signed with the device's key, encrypted to the collaborators key, posted to the collaborators lane. Without a key, the tab says how to get an invitation.

- `/join/` (`assets/feedback/join.js`, `assets/feedback/identity.js`): an invitation link or QR code (`#j1..`, removed from the address bar at once) makes the device's key pair in sgit's format (RSA-OAEP 4096 and ECDSA P-256), private halves non-extractable in IndexedDB, and sends a signed enrolment.

- `/join/invite/` (`assets/feedback/invite.js`): an enrolled key that may invite (the editor) signs an invitation in the browser and gets a QR code, a link and a share button; nothing is stored. The drain enrols a key automatically when its enrolment and its invitation both verify (`admin/build/contributors.py`): three devices an invitation, in date. `admin/build/invite.py` is only the bootstrap for the editor's first key. `admin/build/contributors.py` checks signatures with `sgit pki verify` over pki.sgit.ai's canonical bytes; `collaborators_drain.py` marks every signed row enrolled, unknown key or unsigned, and saves screenshots beside it.

- Tested end to end in Chromium with two browser profiles (bootstrap, browser-signed invitation, second device enrolled automatically, signed feedback) with negative controls (a changed word, page, role or expiry fails; a key that may not invite cannot).

- Not built: the editor's review queue (phase 2); a key on more than one device; links to pki.sgit.ai records. No invitation has been sent.

### Your stack, the blast radius (v0.8.1, dev@php.newsroom)

- `/stack/` from `data/stack.json` (component kinds, links, settings mapped to the published mitigations, the two CVEs as rules, three example stacks), joined at build with `affected`, `defence` and `software` into `stack/catalogue.json`; the tool is `assets/stack.js`.

- Per PHP runtime and CVE: the version against the ranges (EOL branches affected with no upstream release), the providing platform against the NCSC-NL inventory (a distribution backport keeps its old version number, so the reader confirms the vendor build; an image's version is taken as it is), the SAPI's scope, whether the internet reaches it, the settings and edge rules that reduce it, each with its caveat. The blast radius: what runs on an affected runtime, what it and they can reach, one step further. What to do first; the inventory rows, edge entries and pages that name the stack.

- Kept in this browser (`p2s.stack.v1`); several stacks, export and import (an imported file is cleaned and rendered as text); synced by the Ask pane's vault to `/php-october/stack/.json`, the newer copy of each stack winning. Checked in Chromium (three examples, edits, a hostile import, phone, dark); the vault sync not yet run against a real reader vault.

- Not built: vulnerabilities beyond the two (the pulse), feed items matched to a stack, deletions carried across devices.

### Who reads this site, by group, and in public (v0.8.4, dev@php.newsroom)

- `admin/build/telemetry_classes.py`: every session is a reader, the editor, a power user or team member, synthetic (agents, tests, headless browsers) or a crawler. Declared by the browser since v0.8.4 (`assets/telemetry.js` sends `agent`, automation by class, never the user-agent string, and `who`, the role of an enrolled `/join/` key or the browser's setting on `/admin/telemetry/`), inferred before that (time zone, place, language, first page). The telemetry app (UX vault 5wnsr5h8, v0.2.1) runs the same rules, checked identical on all 279 sessions drained so far, filters every page by group and has a map.

- The public telemetry stats vault `0cfkdcvh`, read key published on `/vaults/` and `/admin/telemetry/`: its own app (hourly by group, a world map of readers, what readers read, by day, the method), `stats/summary.json` and `stats/hourly.json`. Counts only: no row, session id, city, region, time zone or time finer than the hour.

- `admin/build/telemetry_flow.sh
`: pull both, drain, classify (`reports/classes.json` in the private vault), publish (`admin/build/telemetry_publish.py`), push both; writes `data/telemetry-report.json` and `data/telemetry-public.json` for the next release. `/admin/telemetry/` draws the groups, the hourly chart and the map from them; `data/world.json` is Natural Earth 1:50m (public domain) in Equal Earth. - The telemetry app v0.4.0 (UX vault 5wnsr5h8), in modules (`app/modules/`: core, classes, model, journeys, charts, live, drain, pages, shell) with `tests/run.mjs` over real events (29 checks): checks the lane and pulls the vault on focus, at most once a minute; every mark filters (click, shift-click to exclude, drag the timeline); colour by any of six breakdowns on the validated palette; Journeys (Sankey, page network, paths, sessions side by side) and What works (per page and section, per source). Checked in a local bridge harness and in App Mode on the data vault. - The vault key is the master key (v0.8.5): the telemetry and subscriptions vaults hold their drain keys in `identity/private/drain-key.pkcs8.json` (protected by the vault's encryption) and their lanes in `identity/lanes.json`; the telemetry app (v0.3.0) drains with the vault key alone. The command-line drainers still use the local passphrase and the sgit key store. - Not built: a schedule for the flow (needs the editor's go); public stats after an in-browser drain (an app cannot write another vault). ### The Sherpa (branch sherpa/joins, sherpa@php.newsroom) - `admin/sherpa/`: the role (adapted from the SG/Send team's Sherpa), `friction-log.json` (schema `sgit.newsroom.friction-log/1`: nine frictions, each with reader, page, stage, intended, actual, expected, evidence, owner and status) and `reviews/` (the first walk, of v0.8.1). Advisory: it proposes and routes to owners, and fixes nothing itself. - In the roster (`data/team.json`), so `/team/sherpa/` exists; four board rows, the frictions it tracks to release. - Readers' feedback: `admin/sherpa/feedback.json` (schema `sgit.newsroom.reader-feedback/1`), one record per message with an id (UF-nnn), date, channel, site version, the reader's words as received and, point by point, the Sherpa's comment, whether it was reproduced, the recommendation and who can act. `build_sherpa()` (the Sherpa's block at the end of `build.py`) builds `/sherpa/` ("I'm the Sherpa, here to help you", the feedback register and the friction log) and one page per message; screenshots in `assets/sherpa/`, metadata stripped. UF-001 (23 October, a power user, by email): ten points, two interface bugs reproduced in Chromium (F015, F016). Readers are not named; whether a reader's words may be published is the editor's to confirm before release. - Ideas from collaborators: `admin/sherpa/ideas.json` (schema `sgit.newsroom.collaborator-ideas/1`), one record per conversation (CI-nnn), each comment, idea and question set against what the site has today, with links, what is missing, a recommendation and who could take it; built as `/sherpa/ideas//` and a section on `/sherpa/`. CI-001 (22 to 23 October, LinkedIn, a collaborator joining the power users): two comments, three ideas (user stories to execution paths and tests; threat scenarios and security assumptions beside stories; verified versus AI-inferred edges), three questions, an offer. Collaborators are named only when they agree (`name_on_site`). - Feedback from collaborators, a section of its own (`/feedback/`, under Yours): every piece of feedback kept whole, in a viewer with a menu of all of them on the left, the document as received in the middle and the Sherpa's comments beside each part of it on the right; readers can select text to highlight it and add a note (kept in their browser only, exportable as JSON; `assets/sherpa/viewer.js`). A report imported whole is `admin/sherpa/documents/.json` in blocks the comments anchor to (UF-003, with its seven screenshots, metadata stripped). `/feedback/briefs/`: the brief to the conductor from every open friction, by owner and severity, and requirements for other teams (`admin/sherpa/briefs.json`: pki.sgit.ai). Counts in `admin/sherpa/collab-stats.json`. The signed messages drained from the collaborators vault are counted, not published, until the editor confirms they may be. - The Sherpa drains the collaborators lane (`collaborators_drain.py` against its own clone of 58526ytp, then pushes the vault); first drain 24 October: five messages, one power user's key enrolled as `power-user-1`, the `editor` bootstrap invitation retired (its code had appeared in drained rows). Its schedule is active (`data/schedule/sherpa.json`). - The Sherpa's inbox (`admin/sherpa/inbox/`): vault d6zak0o3 with an append lane on the postmaster convention, senders `riskmandate` and `editor` (tokens derived, handed sealed), recipient sha256:3b964d5e3abf03c0; `admin/sherpa/send_to_lane.py` sends a MIME message with attachments to any such lane; tested end to end on 24 October (sent, drained by conductor_drain.py, an .eml with its attachment). The Sherpa's schedule is active: every two hours 07:45 to 21:45 London, the full pass at 11:45 and 17:45. - Not built: the Sherpa's line on the front page and the "Where next" block (proposed); the trail additions (proposed, for dev and the editor's go); a key enrolled on pki.sgit.ai. ### The risk graph as a tool (v0.10.13, dev@php.newsroom, the Sherpa's brief from CI-002) - Every edge of `data/grc-graph.json` carries `basis` {kind, ref}: `source` (a capture's slug), `code` (the fix commit), `inferred` (the agent), `confirmed` (who checked, from `data/grc-basis.json`); `build_grc` stops on an edge without a valid one. 1,418 edges: 316 source, 287 code, 815 inferred, 0 confirmed. - Tests as nodes: the 270 test files of the fix commit (`data/grc-tests.json`, from its file list in the evidence vault), each joined to the commit and, by name rules, to the remediation it exercises. - `/grc/explore/` (`assets/grc-explore.js`): start from any node and expand by verb, with the path back and the view in the address; or climb from code, a test or a fix to what it puts at stake. Inferred edges dashed, a switch hides them. - `/grc/gaps/`: eight rules as data (`data/grc-gaps.json`), computed at every build, each with its count, list and who could close it. - Not built, waiting for the editor: the design direction (CI-002.1), persona views of the graph (CI-002.7), user stories as a layer (CI-002.4). - The debrief for the collaborator (v0.10.14): `/articles/the-risk-graph-before-and-after/`, every change as v0.10.12 against v0.10.13 in real screenshots. Articles now take `!split[before](/png)[after](/png)` (side by side, stacked on a phone), `!slider[alt|left|right](/old.png)(/new.png) "note // note"` (one picture, fade or wipe between the two, `assets/compare.js`; without JavaScript the two stack) and ```diff blocks; a site link may carry a view address with `=`, `:`, `&` and `,`. ### The source watch is a pack vault (recorded by dev@php.newsroom, the editor's word of 24 October) - The source watch is `7r83qic5`, a pack-mode vault (sgit-ai 0.24.0 or later). `/vaults/`, `/vaults/source-watch/`, `data/source-watch.json`, `admin/build/export_watch.py`, the team, the schedules and every register's `holds` name it and nothing else; its read key is not published until the vault UI opens pack vaults, so the source-watch page has no embed or open link. - The vault the watch left is named only where the record is dated: the release history, the briefs and articles of 22 and 23 October, the evidence exports (`data/sources.json`, `claims.json`, `pulse.json`, `state.json`), the pack-mode measurement (`/admin/pack-mode/`, which compares the two) and the researcher's register of vaults made (every vault made stays listed with its seal date). - The counts on `/vaults/source-watch/` are from the export of 23 October, read before the move; the next `export_watch.py` run reads `7r83qic5`. ### Every release links the pages it changed (dev@php.newsroom, the editor's ask of 24 October) - `/admin/versions.html`: under each release, the pages it changed, new pages first, then by how much of their visible text changed; eight links, the rest behind a toggle. A page counts as changed when its `` differs from the previous release's with the two version numbers masked; pages where only a number or a link moved come after, and the pages that change at every release by construction (the release history, the board, the runs, what's new, the mockups) last. - `data/release-pages.json`, one entry per release, written once: filled back to v0.2.0 by `admin/build/release_pages.py --all`, and from now on by the build at a release's own build (the version has no release commit yet), against the last release commit. Where git or the history is missing (CI's shallow checkout), the stored entries stand. ### The redesign, live (story-site, 24 October 2026, the editor's go) - Three reader homes from one persona setting: `/` (Briefing), `/ops/` (Operations), `/analysis/` (Analysis); `data/personas.json` gives each persona its `track`. - The menu by task and two dials (who you are; Focus, Standard, Everything), stored in the browser only (`p2s.persona`, `p2s.view`); `assets/design/dials.js` and `assets/design/v2-live.css` are generated by `admin/build/design.py`. - Every `admin/` page sits in the team console (its own sidebar); public, as before. - The brief and the editor's words: `admin/content/briefs/2026-10-24__brief__the-redesign-live.md`. ### The lens, a prototype (story-site, 24 October 2026) - `/admin/design/lens/`: three pages (the front page, the agencies, the team console) that re-shape in place from four settings at the top right: time (1, 5, 15 minutes, all), who, aim (understand, act, check the evidence) and seen. Built by `admin/build/design.py` (`build_lens`) from the live data; `assets/design/lens-boot.js`, `lens.css` and `lens.js` are generated. - Not on the live reader pages: the live site still has the two dials of v0.14.0. The brief and the editor's words: `admin/content/briefs/2026-10-24__brief__the-lens.md`. ### The line, a prototype (story-site, 25 October 2026) - `/admin/design/line/`: six pages (the front page, the agencies, the numbers, the playbook, a page for the team, and a catalogue of every line) on the editor's design of 25 October: one band under the masthead that says one thing to the

 persona in front of it, at the moment of their visits they are in, and a page under it shaped for that role and depth.

- The engine, the roles, the words and the moments are the editor's pack, vendored under `assets/design/line/` with its

 19 tests (`node --test assets/design/line/engine.test.mjs`); `copy.json`, `config.js` and `shape.css` are generated by

 `admin/build/design.py` (`build_line`), which fills every number from the evidence vault.

- Not on the live reader pages: the live site still carries the two dials of v0.14.0. The brief and the editor's words:

 `admin/content/briefs/2026-10-25__brief__the-line.md`.

### The line and the router, live (story-site, 25 October 2026, the editor's go)

- Every page carries the line under the bar (`assets/design/line/`), in place of the two dials of v0.14.0: it says one thing

 to the reader, as the role they are (Executive by default), and keeps their record in this browser (`p2s.lens`).

- Every page shows its view in the address bar: `/agencies/as/security/`. `/404.html` answers any address past a reserved

 word (as, on, vs, since) by opening the page before it with that view; 28 cards (`/as//`) for the front

 page, the agencies, the numbers and the playbook unfurl in a chat with who they are for. Dated views are read, not applied.

- Scripts resolve their requests against the real page (`window.P2S_BASE`, and a fetch shim in `boot.js`), because the

 security policy rules out ``.

### One repository into six, pass one (dev@php.newsroom, 25 October 2026)

- The six repositories exist (`…__PHP__press`, `__data`, `__refs`, `__updates`, `__team`, `__site`), each with `dev` as default and its custom domain (`next.php.oct.2026.newsroom.sgit.ai` for the site until the cutover). This repository is still where every page is built and every agent writes.

- **press v1.0.0:** `sites.json` (which site owns which section) and `tools/partition.py`, which cuts this repository's committed output at one commit into a site. It installs each site's gate and release.

- **The four sites:** cut at `d9af616ffd0b` (v0.22.0). site has 230 pages of its own, refs 563, updates 60, team 242; every other address answers with a redirect. **data** v0.1.1: 49 entries, 466 files, a schema each. **team**: its records under `records/`, the board one file per row.

- Not deployed yet: their Pages source must be "Deploy from a branch" (dev, root), or get a workflow (security review).

### Recorded, not started

- The organisation as a digital twin (`admin/content/briefs/2026-10-22__brief__the-organisation-as-a-digital-twin.md`): a state machine of roles, runs and handovers, a common run record, the accountant, a bulletin board for agents, and a daily improvement loop with a budget.

### The vault key is the whole boundary (23 October 2026, conductor@php.newsroom)

- `admin/build/postmaster.py`: sgit.ai's convention (the vault key is the only secret): a lane's enum key, the key pair's passphrase and, where derived, the senders' tokens are HMAC-SHA256 of the vault's write key with fixed labels; the key pair lives in the vault at `.vault/postmaster/front-door-keypair/`, encrypted; the lane in `.vault/postmaster/lane.json`. The collaborators (58526ytp) and conductor (5iwos28w) vaults use it; both drains work from a clone with the vault key alone (tested from a fresh clone with the session's own key pair moved aside). A lane that answers 404 to the derived key is re-registered once by the drain (seen once on 23 October, cause unknown).

- `/team/vaults/`: every agent's vaults by ID and, from 23 October, the keys each agent holds (the `holds` list), never a key.

- The feedback pane takes up to three screenshots; `/join/` says whether this device's key is enrolled or waiting.

### The updates (journalist, for the conductor)

- `/updates/` and `/feeds/updates.xml` from `admin/content/updates/__.md` (front matter: id, at, kind flash|hourly|daily, title, summary, covers_from, covers_to, author); the guide is `admin/content/updates/README.md`, also at `/updates/readme/`. One update so far: the daily of 22 October, 20:03 UTC.

- `admin/build/updates_digest.py --since  --until origin/dev`: the facts for an update, from git alone.

- Stories can carry dated corrections (`correction1:  | ` in front matter), shown above the text, which stays as written.

- Not built: a schedule for the updates (needs the editor's go); the conductor's own session has not taken the beat yet.

### Views: the journalist's state of affairs (23 October)

- `/views/`, `/views/state/` (the current version), `/views/state/v/` (every version), `/views/state/v-v/` (what changed: the measures side by side, the text as a line diff), `/views/state/history/`. Versions are the journalist's own, independent of the site's releases: `admin/content/views/state/v.md` (immutable) and `data/state.json` (the measures, each with as-of and basis). The current version is also in the site's ledger. Two versions: v0 (22 October, reconstructed) and v1 (23 October, 14:11 UTC).

- `data/` re-exported from the evidence vault at `f3c5db0d9873` (227 sources, latest capture 01:20 UTC on 23 October); the inventory history re-read to `2fdc314ded28` (12:50 UTC on 23 October).

- "Last checked" in the header and on the front page is the newest of three times, each shown on the front page: the evidence vault's latest capture (still `data_as_of`, which the claims, articles and status.json are built from), the source watch's latest run (`data/source-watch.json`, re-exported at `20afaa62129d`) and the NCSC-NL inventory's latest change read (`data/inventory-history.json`). Before v0.10.6 it was the evidence vault's alone, which read as stale whenever the vault had not taken a capture for hours while the other two had moved.

- `data/` re-exported from the evidence vault at `1845598d9a38` (295 sources, latest capture 16:04 UTC on 23 October). The journalist's state of affairs is at version 2 (`/views/state/v2/`), written against it; the front page's "Right now" and "Latest" are from the same export. The source watch's pack vault `7r83qic5` is not read yet (no read key in this desk's session).

### Commit-FS-lite (24 October 2026, conductor@php.newsroom)

- Agents leave each other notes as trailers in their release commits (`To-:`, `To-all:`, beside `Agent:`). `admin/build/schedule.py notes ` reads them since the head the agent's last run recorded (run records now carry `head`); tested on a throwaway commit (a note continued over two lines, two recipients).

- `/team/comms/` lists every note in the last 600 commits on HEAD, built at release; each `/team/schedule//` lists the notes to it. AGENTS.md section 8 is the rule; CLAUDE.md does not mention it yet (security@'s file: asked in a note).

### Schedules, runs and messages in the repository (24 October 2026, conductor@php.newsroom)

- Replaces the schedule vault (below, now an archive no longer written). `data/schedule/.json`: each scheduled agent's card (objective, status, wake times in London time, model, session, brief, each wake's steps, reads, writes, never, the wake prompt word for word). Three cards: curator and researcher (active; drafted by the conductor from their scheduled tasks, for them to confirm), conductor (active since 24 October: hourly 07:15 to 21:15 London, a Sonnet session woken by one scheduled task; commits only when something changed).

- `data/runs//.json`, one per wake, and `data/messages//.md`, one per message, both written by `admin/build/schedule.py` (inbox, run, send; refuses key, token and sealed-link shapes). Six messages from the conductor (to all; curator; researcher; pulse; ontologist; librarian) and one run (this change, not a scheduled wake).

- `/team/schedule/` is built from those files at release, no JavaScript: one day of every wake as an SVG (quiet hours shaded), the cards, the latest runs, the messages; a page per agent (`/team/schedule//`) with its instructions, runs, inbox and outbox. `/team/runs/` lists the runs too. `data/schedules.json` keeps the quiet hours, the article rule and who is still to write a card (pulse, ontologist, librarian). AGENTS.md section 7 and CLAUDE.md say so.

### The schedule vault (23 October 2026, conductor@php.newsroom; retired 24 October 2026, kept as an archive)

- A public vault, `weic8imn` (read key on `/vaults/` and `/team/schedule/`): `schedules/.json`, `tasks//queued|done|failed/T-NNN.json` (a brief, `not_before`, `due_by`, `repeat_until`), `runs///.json` (schema `sgit.newsroom.run/1`, with the log), `index.json`, and `tools/schedule.py` (due, start, finish, idle, queue, index; refuses key and token shapes). Seeded with four schedules (curator and researcher setting up, fact-check paused, synthetic readers paused pending removal), the curator's and the researcher's routine tasks (repeating until 31 October) and 42 runs already recorded elsewhere.

- Until 24 October, `/team/schedule/` read the vault live in the browser with its read key (`assets/schedule/schedule.js`, since removed): schedules, tasks due and overdue, every run, a run's log on demand, by agent; tested in Chromium against the live vault.

- `AGENTS.md` section 7 and `CLAUDE.md`: every scheduled wake goes through the vault; no task due means one idle run and nothing else.

- Not built: queueing a task from the page (board); no scheduled agent has run through the vault yet.

### Not built

- A second fact-check desk on a different model; a review folder; a second model reading the vault; a Stripe link; tests beyond the gate.

- A second fact-check desk on a different model; a review folder; a second model reading the vault; a Stripe link; tests beyond the gate.

- `/claims/review/`: every claim in the evidence vault's per-agent files that is not in the site's claim table (86 at `1845598d9a38`, 81 from the curator), each with the journalist's verdict from `data/claim-review.json` (used, agrees, held back, with the reason) or "not yet reviewed". A new export lists new claims there without anyone editing a page.

- `/pulse/`: a separate section, not about PHP. The SGit newsroom's Pulse vault (`4klm5qlt`, pulse@newsroom), exported by `admin/build/export_pulse.py` into `data/pulse.json` (ladders, dates, attention counts, short quotes with their capture paths and hashes; no capture, no key), built by its own block at the end of `build.py`, one page per vulnerability (26). The PHP pages do not read it; the front page has one pointer, "What else is going on".

- `/views/desk/`, the journalist's desk (the editor's decision, 24 October 2026: the journalist keeps the site current after every evidence export): the cycle each export goes through, the five steps of the full pass and their status, the pass ledger (one row per hand-kept data file and the vault head it was last checked against) and a staleness report computed at every build from the markdown twins (dated 'as of' phrases older than the latest capture, outside pages kept as written by design), all from `data/desk.json`.

## The honest column

- **Not measured:** the editor's time and the inference cost behind each agent run.

- **Not yet run:** the verifier role, which re-reads every claim against its capture text.

- **Not reviewed:** the playbook and the blast-radius section are the site's own synthesis of agency advice and have not been reviewed by a security team.

- **Not live:** everything on the billing page under "designed".

- **No tests beyond the gate:** the build has no unit tests; the gate is the whole automated enforcement surface.

- **No review folder yet:** the estate's guidance asks for `review/` from the first commit; this repository starts it from its next change.


---
site v0.22.4 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/admin/index.html
