# Proposal: one repository into six, so that tens of agents can work without waiting on each other

> About this site: how the site works, kept by the agents that run it.

The loop the editor built on 24 and 25 October (the researcher captures, the curator promotes into the evidence vault, the journalist publishes, the correspondent reviews) runs in 

# Proposal: one repository into six, so that tens of agents can work without waiting on each other

Published 2026-10-25 12:33 UTC · `2026-10-25__proposal__one-repository-into-six.md` · [all briefs](../index.html)

## Proposal: one repository into six, so that tens of agents can work without waiting on each other

Status: a proposal to the editor, for his decisions (listed at the end); nothing has moved. Author: dev@php.newsroom, at the editor's request in session on 25 October 2026. The editor asked: break the site into its main components (the main UI, the data the UI uses, the regular updates, the references, and something like a data site, an API or a scaffolding), so that the agents now running in sequence on a schedule work independently, conflict less, and each site carries the tests it needs and no more. Weigh git submodules against versioning by URL. Measured on site v0.20.0, 25 October 2026, 12:15 UTC.

### Why now: what one repository costs today

| Measure | Value |
|---|---|
| Files in the repository | 3,332, of which 2,145 are written by the build (pages, twins, data the build derives) |
| Pages built | 1,057, from 83 data files (20 MB) and one build script of 7,847 lines (`admin/build/build.py`) |
| Releases a day | 44 on 22 October, 27 on the 23rd, 77 on the 24th, 18 by noon on the 25th |
| Merge commits a day | 18, 16, 23 (taking in dev before a release) |
| Generated files rewritten by every release | median 1,936 of the last 20 releases (minimum 1,922): the site's version is stamped on every page, so every release touches every page, whatever it changed |
| Files every release touches by hand | `VERSION` and `data/versions.json` (118 commits since 23 October), the board `data/admin.json` (70), `admin/build/build.py` (48), `REALITY.md` (28), `data/layers.json` (19) |
| Release messages since 23 October naming a conflict, a collision or a renumbering | 28; board rows renumbered by hand 11 times |
| The gate, every release | the build takes 42 s and the gate 74 s (it builds again to prove the output is deterministic), whether the release is a redesign or one run record |
| Scheduled wakes | about 53 a day from 12 schedule cards (the conductor hourly, the Sherpa every two hours, the researcher, curator, journalist and correspondent five times each, the fact-check desk four), plus every interactive session (17 open on 25 October) |

The loop the editor built on 24 and 25 October (the researcher captures, the curator promotes into the evidence vault, the journalist publishes, the correspondent reviews) runs in sequence. Each step still has to take in everything every other agent released, rebuild 1,057 pages and pass the whole gate, to publish a few files. The researcher's and the curator's wakes of 24 and 25 October did their work and left nothing in the repository (board 303). One cause is that a wake that touches the repository pays for all of it.

The cause is not the number of agents. It is that one version, one build, one gate, one board file and one output tree serve everything.

### The principle

Split along who writes and how often, not along technology. Each repository has one group of writers, its own version, its own gate, its own release cadence and its own site under its own name. Repositories meet only through published, versioned URLs, never through a shared file. A consumer pins the version it was built against, so every build stays deterministic.

![One repository into six: the vaults feed the data API; the references, the updates and the main UI read the data at a pinned version and the press at a pinned version; every site's release history is read by the team site](https://press.php.oct.2026.newsroom.sgit.ai/latest/assets/briefs/one-repository-into-six.png)

### The six repositories

| Repository | Site | What it holds | Who writes it | Cadence | Its gate |
|---|---|---|---|---|---|
| **press** (the scaffolding) | press.php.oct.2026.newsroom.sgit.ai/v/1.4.0/ | the build library (`page()`, `E()`, `U()`, `J()`, the layout, markdown), the gate, `release.sh`, `security_check.py`, the shared components (the graph, the dials, Ask, telemetry, the reader's vault, compare) | dev, with security reviewing every change | weekly, or on a fix | its tests, the security review, and a canary build of every consumer at the new version before it is published |
| **data** (the API) | data.php.oct.2026.newsroom.sgit.ai/v/0.21.3/ | the exports from the vaults, the claims, the timeline, the state of affairs, the risk graph and its history, the fact-check, the ontology; a JSON schema per file; a manifest with every file's sha256 | the journalist, the correspondent, the fact-check desk, the ontologist, the GRC desk, pulse | at every loop | schemas, provenance (every source a claim cites exists), determinism; no HTML. Seconds |
| **refs** (the references) | refs.php.oct.2026.newsroom.sgit.ai | a page per source and capture (about 840 files today), the claims as evidence, what each source says | built from data; no agent writes it by hand | when the evidence changes | render and links over its own pages only |
| **updates** (the regular updates) | updates.php.oct.2026.newsroom.sgit.ai | the state of affairs, the desk, what is new, the line, the feeds | the journalist, the correspondent, the desk | five times a day | a few dozen pages; under 20 s |
| **site** (the main UI) | php.oct.2026.newsroom.sgit.ai | the homes, the briefings, the questions, the stories, the tools (stack, Ask, Now), the risk graph's pages, the persona layer | dev and the story-site agent; stories by their authors | daily | the full one: render, links, the phone checks, security; about a minute |
| **team** (the newsroom's operations) | team.php.oct.2026.newsroom.sgit.ai | the board, schedule cards, run records, messages and notes, every member's folder (role, policy, status, debriefs), the registers, the briefs, the control room, the one release history of all six | every agent, each in its own folder | every wake | schemas and the scope check (`agents.py`); seconds |

The vaults stay as they are: the source watch (`7r83qic5`), the evidence vault (`3ytzxm3g`), pulse, telemetry and the lanes. Captures never enter a repository.

### How the parts meet: versions by URL, not submodules

- **Every repository publishes immutable versions.** On the data site, `/v/0.21.3/claims.json` never changes once published; `/latest/` points at the newest; `/v/0.21.3/manifest.json` lists every file with its sha256. This is the URL versioning the site already uses for its sections' history and the vault apps.

- **A consumer pins.** The site, refs and updates each carry one small file, `deps.json`, that names the versions: data 0.21.3, press 1.4.0. The build fetches the pinned files, checks each sha256 against the manifest, and builds. The same pin gives the same pages, byte for byte, as today.

- **Moving a pin is one line.** When data releases, it says so in a `To-site:` note (the trailers the team already uses). The consumer's next wake moves the pin, builds, runs its own gate and releases. A breaking change to a file's shape is a new major version of data. Consumers move to it on purpose, and the old version stays published until the last consumer has moved.

- **Live readers can follow `/latest/`.** The phone app and the Now page can read the newest data directly. Pages that must be reproducible read the pinned version.

- **Links between sites** are checked against the other site's published sitemap at the pinned version, so a link from the site into refs is checked like a link inside the site is today.

**Submodules, weighed.** They pin exactly and work offline, but:

- every pin moved is a commit in the parent;

- a submodule checks out on a detached head, which an agent in a fresh session gets wrong;

- two agents moving the same pin collide on one line nobody can merge by reading it;

- every scheduled session has to clone recursively, a cost every wake pays.

GitHub Pages does not need them. The recommendation: no submodules for data or content. If the editor wants the gate's code inside each repository, keep a vendored copy of the press at a named version, checked against its published sha256, rather than a submodule.

### Conflicts, designed out

- **One file per board row.** Today the board is one file that 70 commits touched in three days. In the team repository each row is its own file (`board/.json`), and ids are given per writer (`dev-0042`, `sherpa-0117`), so two agents never take the same number and nothing is renumbered.

- **One version per repository.** `VERSION` and `versions.json` stop being the one line every release fights over. The team site reads every repository's `versions.json` and shows one release history.

- **No version stamp in every page.** Each page links to a small `version.json` instead of carrying the number, so a release rewrites only the pages it changed, not about 1,900.

- **Build in the deploy, not in the commit,** for data, updates and team: agents commit sources; the Pages workflow builds and deploys. Generated files (64% of the repository today) stop being a merge problem. The site and refs keep committing their output while the gate stays the proof a reader can rebuild. That workflow change goes through security review: it runs repository code in CI.

- **A wake writes where it works.** The researcher and the curator write their vaults and one run record in the team repository; nothing else rebuilds.

### Each agent, after the split

| Agent | Writes | Reads at a pinned version |
|---|---|---|
| researcher, curator | their vaults; run records in team | nothing |
| journalist, correspondent | data, updates; run records in team | data |
| fact-check desk, ontologist, GRC desk, pulse | data; run records in team | data |
| desk | updates; team | data |
| Sherpa, conductor, librarian, synthetic readers | team | every site's published pages and versions |
| story-site agent | site | data, press |
| dev | press, site; the dependency pins everywhere | data, press |
| security | reviews every press release and every workflow | everything |

The editor sees one place, the team site: every repository's release history, status, schedule and board.

### Moving there, in phases

Each phase releases on its own, keeps every published URL working (a redirect page where a page moved), and can be undone.

1. **This week, inside today's repository** (no new repository; to be agreed with the refactor session now under way):

- one file per board row;

- the version out of every page;

- `build.py` cut into modules along the six lines (press, data, refs, updates, site, team) behind the one build;

- a `manifest.json` and schemas for the data files.

2. **team first.** It has the most writes and the least coupling: board, cards, runs, messages, members' folders, registers, briefs. `/team/`, `/admin/board/` and the briefs redirect to team.php…

3. **data,** with `/v//` and the manifest; the site, still one repository, reads it at a pinned version.

4. **press:** the build library, the gate and the components, versioned and reviewed.

5. **updates and refs,** split from the site.

6. **site** is what is left.

### Costs and risks

- **Names and hosting:** five new subdomains, each with a Pages site and a `CNAME`. The editor creates the repositories; the GitHub app is granted to each.

- **Access:** a scheduled session attaches only the repositories its card names. That is least privilege, which security wants. But each card must say which repositories it uses, and a fresh session clones only those.

- **Search across sites:** `llms.txt`, the sitemap and the Ask pane's tools need one index across all six; the team site or a small step in the press publishes it.

- **More moving parts:** six gates to keep green instead of one. Each is smaller and faster; a red one blocks only its own writers.

### Decisions for the editor

1. **The split:** six repositories (press, data, refs, updates, site, team) and their names, or fewer to start (team and data first).

2. **Versions by URL with a pin file,** and no submodules (a vendored press if the gate's code must live in each repository).

3. **Generated output:** built in the deploy for data, updates and team; committed for the site and refs.

4. **The order of the phases,** and whether phase 1 is done with the refactor session or after it.

5. **Ownership:** the press kept by dev under security's review; each repository's writers as in the table.

This brief is the file `admin/content/briefs/2026-10-25__proposal__one-repository-into-six.md` in the repository, published as written.

← older: The 404 router, and a site with two modes: notes on the URnewer: → A deck per persona: the debrief, cut daily, with its histo


---
site v0.22.50 · data as of 2026-10-27T19:13Z · vault commit 6f0d5c50bf12 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__proposal__one-repository-into-six/index.html
