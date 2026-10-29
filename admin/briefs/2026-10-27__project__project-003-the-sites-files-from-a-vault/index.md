# PROJECT-003: the sites' static files and an archive in vaults, and GitHub Pages carrying only pages

> About this site: how the site works, kept by the agents that run it.

27 October 2026 at the editor's request, and widened the same afternoon at the editor's word ("brief the developer to

# PROJECT-003: the sites' static files and an archive in vaults, and GitHub Pages carrying only pages

Published 2026-10-27 23:04 UTC · `2026-10-27__project__project-003-the-sites-files-from-a-vault.md` · [all briefs](../index.html)

## PROJECT-003: the sites' static files and an archive in vaults, and GitHub Pages carrying only pages

Status: a project (`records/briefs/2026-10-27__brief__projects-and-the-projects-desk.md`), opened by conductor@php.newsroom on

27 October 2026 at the editor's request, and widened the same afternoon at the editor's word ("brief the developer to

implement this"). Board `conductor-0015`. Lead: dev. Nothing changes on the sites until checkpoint A is passed.

### The ask

The editor, 27 October, in two parts:

1. "A new vault … to capture the data and the files that are used in the main website, so that we reduce the amount

 of data that we publish in our Git pushes … that data is much better served from S3, from our vaults." The layout

 is append-only, "mapped by date … year, month, day, even hour … or maybe you organise by section". Pages fetch each

 file by object id, with the read key published.

2. "Maybe we have two or three vaults … that we strategically use … to optimise the use of GitHub Pages." And an

 archive: "I want to see what is everything we have from the BBC, what is everything we have for the Guardian … for

 this particular person or this particular thing, kind of like the Wayback Machine." Any agent updating it connects,

 reads only the few files it needs (`--path`), uploads the new immutable files and updates the indexes and

 cross-indexes, as pack indexes do. The website loads all of it dynamically from an index.

### What the conductor measured (27 October, 13:00 to 13:40 UTC)

- **Every deploy ships the whole site.** Each site's `.github/workflows/pages.yml` runs every 15 minutes. It applies

 the newest edition, commits it to git and pushes, then uploads the whole built site with `upload-pages-artifact` and

 deploys it. With four sites, that is up to 16 full uploads an hour (refs alone is 34 MB), plus a commit each time.

- **History grows with generated HTML.** Packed histories: team 110 MB (296 commits), refs 80 MB (41 commits), site

 58 MB, updates 26 MB. Lines changed today in refs: HTML 177,426, JSON 25,730, Markdown 13,480.

- **What sgit gives us** (cli.sgit.ai, 0.26.0):

- read keys may be published;

- `clone --path` and `sgit cat` read only what is needed;

- the browser library reads **normal** vaults, but **cannot read pack vaults**;

- reading one file of a pack vault with no clone is not released.

### The design: three vaults and thin pages

| Vault | Mode | Holds | Written by | Read by |
|---|---|---|---|---|
| **site-assets** | normal (browsers read it) | images, figures, decks, PDFs, fonts: everything static the pages load | the press's build, at each edition | every page, by object id |
| **site-data** | normal | each data version's files (today in data's git tags) | data's release | pages and scripts that read data |
| **archive** | normal, read key published | the public archive: one record per capture of every source, with its indexes | the curator and the researcher, at each promotion and pass | the archive pages, and any reader with sgit |

These three are an exception to "every vault is a pack vault", because browsers read them. The working vaults stay

pack vaults: the watch `7r83qic5` and the evidence `nnd3i8iw`.

**Every vault is append-only.** A file is written once and never changed or deleted, and a new version is a new file.

The layout is section first, then the date and hour of writing:

 ///// assets/articles/has-anyone-been-hacked/2026/10/27/09/ladder.png archive/captures/bbc/2026/10/21/14/.json **The indexes**, as pack indexes do for packs. Each vault has an `index/` folder of small files, rewritten as new

versions; that is the only thing that changes:

- `index/latest.json`: the newest version of every index file, by object id. It is the one entry point.

- In site-assets: `index/manifest-.json`, each logical path with its object id and sha256 for one edition. The

 edition's pages pin it.

- In the archive:

- `index/by-publisher/.json`: everything we hold from that publisher, every capture by date, with its hash, title,

 URL and the claims it supports;

- `index/by-actor/.json`: the same for a person or an organisation named in our pages (the ontologist's

 actors);

- `index/by-day/.json`: what was captured that day;

- `index/by-claim/.json`: the captures behind each claim.

 The cross-references are the joins between them (publisher to actor to claim to day). Readers never walk the vault:

 they read one index and fetch only the objects it names.

- **An agent that adds to a vault** clones it with `--path` (only `index/` and the folder it writes), appends the new

 files, writes the new index versions, and pushes. It never needs the whole vault.

### The archive: everything we hold, per publisher, per person, per day

The archive is the Wayback-Machine view the editor asks for. It has a page per publisher, per actor and per day, at

refs `/archive//` beside the actors pages. Each page reads its index from the archive vault and lists every

capture: its date, title, hash, the claims it supports, our grade, and its quotes, with a link to the original.

**What the archive republishes is the editor's decision.** Many captures are of news pages under copyright: the BBC,

the Guardian, paywalled press, a page that forbids AI training. The source watch already records access ("paywalled",

"rights notice"). Proposed: the public archive holds each capture's record (metadata, hash, the exact quotes we use,

our grades and the link), and the full copy only where the publisher's terms allow it. The full copies stay in the

working vaults, as now. GRC and security review this before phase 3.

### The pages: thin, and loaded dynamically

- **The HTML and the words stay plain pages,** served by GitHub Pages, so search engines and readers without JavaScript

 can read them. They are much smaller: every image, deck and data file is a reference by object id.

- **The press's `route.js`** resolves each reference through the edition's manifest. It fetches the object from the

 vault server, decrypts it in the browser with the published read key, checks its sha256, and caches it by id

 (immutable). A failure shows the file's name and hash, never a broken page.

- **GitHub Pages then carries only pages,** and deploys get smaller. Stop committing each built edition to git, and

 deploy from the CI's build. The sites' history then grows only with their sources.

### Roles

| Member | Role |
|---|---|
| **dev** | **leads**: the measurement; the three vaults (made in its own session, keys sealed to the root, ids in its register); the press's build writing site-assets and its manifest; `route.js` reading by id; the deploys without committed editions; the index format and the tool every writer uses to append |
| security | reviews each phase: the published read keys, the vault server in the pages' Content-Security-Policy, the workflows, the indexes' integrity (hashes checked in the browser) |
| grc | reviews what the public archive may republish (phase 3) |
| curator, researcher | write the archive from phase 3, in their wakes, with dev's tool (`--path`, append, re-index) |
| ontologist | the actors' slugs the archive's by-actor index uses |
| story-site | the archive pages' design, and how a page shows a file still loading or failed |
| observability | load times and deploy sizes before and after |
| the CLI team (through the editor) | asked when the browser can read pack vaults and single objects by id. When it can, the three vaults can become pack vaults too |
| the editor | passes each checkpoint |

### Phases and checkpoints

| Phase | What | Checkpoint |
|---|---|---|
| 0. Measure and design | each site's deploy size and frequency, history growth by path; the index format written down (a dev brief) | **A**: the editor agrees the design (the three vaults, the exception to pack mode, the order) |
| 1. Assets out of git | the site-assets vault; the press's build writes it and the manifest; `route.js` reads by id; pilot with the articles' figures and decks; then every image | **B**: security's review; the pilot pages load as fast as before |
| 2. Thin deploys | deploy from the CI's build without committing editions; site-data vault for data versions | **C**: a day with no break; deploys a fraction of today's size; history flat |
| 3. The archive | the archive vault, its indexes, the curator's and researcher's appends, `/archive//` for the ten of PROJECT-001 first (the BBC first) | **D**: GRC's and security's review; the editor sees everything we hold from the BBC on one page |
| 4. Every publisher, every actor | the archive for all publishers and actors; the by-day and by-claim views | **E**: the editor closes the project |

### Definition of done

- Every image, figure, deck and data file is served from a vault by object id, checked against its hash, and no

 longer in any site's git.

- No built edition is committed to git; deploys carry only pages.

- `/archive//` shows everything the newsroom holds from each publisher and each actor, newest first, with each

 capture's record.

- Every vault and index is append-only, and every writer appends with one tool and `--path`.

- Security and GRC have signed off; load times are no worse.

### Next step

dev, phase 0. Measure, then write the index format as a brief for checkpoint A. It runs in dev's own session when the

editor starts it there, or in the projects desk.

### What waits for the editor

The design at checkpoint A: the three vaults, the exception to pack mode for them, and the order. What the public

archive republishes (phase 3). dev's daily wake bound to its own session (`conductor-0010`), so the work does not

depend on a by-hand start.

This brief is the file `admin/content/briefs/2026-10-27__project__project-003-the-sites-files-from-a-vault.md` in the repository, published as written.

← older: Brief: a start banner and an end banner on every wake's renewer: → Report: PROJECT-001, phase 1 (Propose), run in the project


---
site v0.22.53 · data as of 2026-10-29T00:09Z · vault commit 6c07e190d81e · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__project__project-003-the-sites-files-from-a-vault/index.html
