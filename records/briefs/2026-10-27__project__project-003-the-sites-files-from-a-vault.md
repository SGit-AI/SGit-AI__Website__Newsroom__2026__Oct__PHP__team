# PROJECT-003: the sites' files served from a vault, and lighter git pushes

Status: a project (`records/briefs/2026-10-27__brief__projects-and-the-projects-desk.md`), opened by conductor@php.newsroom on
27 October 2026 at the editor's request. Board `conductor-0015`. Lead proposed: dev. Nothing changes on the sites until
checkpoint A is passed.

## The ask

The editor, 27 October: "a new vault that is going to be used to capture the data and the files that are used in the
main website, so that we reduce the amount of data that we publish in our Git pushes … that data is much better served
from S3, from our vaults". It would be an append-only vault, "maybe even mapped by date … year, month, day, even hour …
or maybe you organise by section". Pages would fetch each file by its object id, with the read key published so anyone
can read it.

## What the conductor measured first (27 October, 13:00 UTC)

- **The repositories are small; their history is what grows.** Current trees: team 47 MB, refs 34 MB, data 21 MB,
  site 17 MB, press 12 MB, updates 9 MB. Packed histories: team 110 MB (296 commits), refs 80 MB (41 commits), site
  58 MB, updates 26 MB, press 10 MB, data 4 MB.
- **What changes, today:** lines changed per kind of file since midnight. In refs: HTML 177,426, JSON 25,730,
  Markdown 13,480. In team: HTML 57,500, the records 25,056, Markdown 9,427, JSON 8,939. **The weight is generated HTML
  pages,** rewritten by every edition, and editions now run every ten minutes. Data files and images are a small part.
- **What sgit can serve today** (cli.sgit.ai, 0.26.0):
  - read keys may be published;
  - `sgit cat` reads one file from the server with no clone (for an agent or CI, not a browser);
  - the browser library reads **normal** vaults;
  - **the browser cannot read pack vaults** (the limitations page: "The browser cannot read packs").
  - Reading one file of a pack vault with no clone ("Phase 4") is not released.

## What the plan does with that

1. **The biggest saving needs no vault:** stop committing generated pages. Each site's CI already builds its edition;
   it can publish the built pages as a GitHub Pages artifact instead of committing them, so a site's git history holds
   only its sources (content, records, the build) and not ten editions an hour of rewritten HTML. This removes most of
   the growth.
2. **The vault is right for files that never change once written:** images, figures, decks, PDFs and each data
   version's files. A vault object is named by its hash, so a page can pin it forever and cache it forever. It moves
   them out of git and onto S3, as the editor wants.
3. **The site vault must be a normal vault, not a pack vault,** until the browser can read packs. That is a named
   exception to "every vault is a pack vault", for this one vault, because browsers are its readers.
4. **Never the pages' text.** A file in the vault is encrypted and decrypted in the reader's browser. Search engines and
   readers without JavaScript would see nothing, so HTML and the words of articles stay served as plain pages.

## The layout

The vault is append-only: a file is written once and never changed or deleted, and a new version is a new file.

`<section>/<yyyy>/<mm>/<dd>/<hh>/<name>`, for example `articles/has-anyone-been-hacked/2026/10/27/09/ladder.png` or
`data/2026/10/27/11/sources.json`. Section first, so one section can be fetched or audited alone; then the date and
hour of writing, so the history reads in order.

Each edition writes a **manifest** into git, which is small: each logical path, its object id and its hash. Pages ask
for the object id through the manifest. The press's `route.js` resolves the id, fetches it from the server, decrypts
it with the published read key and checks the hash.

## Roles

| Member | Role |
| --- | --- |
| **dev** | **leads**: the measurement, the pages-as-artifacts change, the vault, the manifest and `route.js` |
| security | reviews each phase: the published read key, the new host in the CSP, the workflows; signs off before the cutover |
| story-site | the loading behaviour of figures and decks (placeholders, failures) |
| observability | measures load times before and after, from the telemetry lane |
| the CLI team (through the editor) | asked whether the browser can read pack vaults, and when single-object reads by id ship |
| the editor | passes each checkpoint |

## Phases and checkpoints

| Phase | What | Checkpoint |
| --- | --- | --- |
| 0. Measure | per repository, which paths make the history grow (a week's numbers), and GitHub's limits as they apply (repository size, Pages site size, deploys per hour) | **A**: the editor agrees the plan's order |
| 1. Pages as artifacts | one site first (refs, the heaviest), published from its CI's build without committing the HTML; then the others | **B**: refs served from the artifact for a day with no break; the history stops growing with each edition |
| 2. The site vault | a normal vault, its read key published, the layout above, the manifest, `route.js` reading by id; pilot with the press's article figures and decks | **C**: security's review; the pilot pages load as fast as before (observability) |
| 3. Move what fits | each data version's files and every image, section by section; git keeps the manifests | **D**: the editor closes the project |

## Definition of done

- No generated page is committed to any site's git. Every site is deployed from its CI's build.
- Images, figures, decks and data files are served from the site vault by object id, each checked against its hash.
- Each repository's history grows only with its sources.
- Security has signed off; load times are no worse.

## Next step

Phase 0: dev measures. Its daily wake checks the editions; this project runs in the projects desk or in dev's own
session once the editor starts it.

## What waits for the editor

Who leads (proposed: dev). The exception to the pack-only rule for this one vault. Phase 1 before phase 2, as above.
