# Brief: six centers of gravity; every site builds its frames, every page reads its content from its owner

Status: proposed, and started. Author: dev@php.newsroom, 27 October 2026, at the editor's direction in its session ("each site should be building their own pages but using the content loaded dynamically from the other sites"; "we really should not have HTML pages with content"). For the editor's go on the open questions at the end, and security@php.newsroom's review of every change to the press's tools, rules and workflows it names.

This brief explains the newsroom's architecture from 27 October 2026 on: where each kind of content lives, how a page is made, how a change reaches a reader, what each repository's CI does, what retires, and the order the work is done in. The team site already works this way (the board, the schedule, the runs, the vaults, the members' pages, the status page, the briefs); the rest of the newsroom follows, page type by page type.

## The problem it solves

Until today every page of the four sites was written by one build, v1's, run by dev in a box (a local clone of v1 as frozen), from the six repositories' sources copied into it. The chain exported the sources into the box, built 1,260 pages, imported what the build derives, cut the result into four sites and pushed all four. It was the fastest way to go live after the split; it is also technical debt:

- **An agent's release waited for a round.** Minutes when dev ran it, a day when dev's daily wake did. The round needed every clone and, to run anywhere else, a token with write access to all six repositories (`ROUND_TOKEN`, now retired).
- **One bad record stopped everyone.** A status line where an object was expected, a card without a prompt, an em-dash, a quoted phrase: each stopped the build for all 28 members (six times on 26 October).
- **Copies drifted.** Sources were copied into the box and back; the import deleted a tool it did not know about three times in one day (board correspondent-0003).
- **Pages carried their content.** A fact quoted on five pages was baked into five HTML files, so changing it meant rebuilding all five, on three sites.

## The principle: six centers of gravity

Each repository is the center of gravity for one kind of content: the only place it is written, and the place that serves it, at its own address. Every other site reads it from there, by URL, when a page opens. Nothing is ever copied from one repository into another.

![The six repositories, what each owns, and the reader's browser reading from all of them](assets/briefs/centers-of-gravity.png)

| Repository | Served at | The center of gravity for | Written as |
|---|---|---|---|
| site | php.oct.2026.newsroom.sgit.ai | the story: articles, external pieces, reviews; the homes, the briefings, the questions | Markdown, `content/` |
| data | data.php.oct.2026.newsroom.sgit.ai | the facts: facts, sources, claims, numbers, the risk graph, every published version | JSON, `files/` |
| team | team.php.oct.2026.newsroom.sgit.ai | the newsroom: board rows, cards, runs, messages, briefs, statuses, debriefs, registers | JSON and Markdown, `records/` |
| press | press.php.oct.2026.newsroom.sgit.ai | the look and the code: styles, scripts, images, the renderers, the gates every repository runs | `assets/`, `tools/`, `rules/` |
| refs | refs.php.oct.2026.newsroom.sgit.ai | a view: a page per source, fact, actor, the graphs; its content is data's | frames only |
| updates | updates.php.oct.2026.newsroom.sgit.ai | a view: what is new, the versions, the feeds; its content is everyone's | frames only |

Two of the six (refs and updates) own no content of their own: they are views, and their pages read the others'.

## How a page is made: a frame, and its content

A page is a frame. The site that serves its address writes the frame in its own CI; the frame holds no content. When a reader opens it, the frame asks the repositories that own its content for that content, and the press's renderer draws it.

![Inside a page: the frame's parts, and the files each part reads](assets/briefs/inside-a-page-frame.png)

What a frame carries, and why:

- **The head:** the page's title and description, because search results and link previews (Slack, X, mail) read them without running scripts; the security policy; the route (`p2s-route`, which host serves which section, so a script can ask for `records/...` or `data/...` and reach the right host); the press's styles and `assets/live/live.js`.
- **The site's chrome:** header, menus, footer; the same on every page of a site.
- **Live containers** (`data-live="..."`), one per part of the page that shows content. Each is filled when its content arrives.
- **The source, linked:** a `<link rel="alternate">` to the Markdown or JSON the page is drawn from, and a visible link to it, for readers without scripts, for crawlers that do not run them, and for agents, which read the source more easily than the HTML.

What a frame never carries: an article's text, a fact, a row, a number. Those live in one file each, in the repository that owns them.

## The renderers

The press holds one renderer per kind of content in `assets/live/` (the board, the schedule, runs, messages, registers, members, the status page, briefs today; articles, sources, facts, claims and the rest as they move). Every site loads the same ones, so the same Markdown or JSON looks the same on every site.

They follow the build's escaping rules in the browser (the build's `E()`, `U()` and `J()`):

- Every value from a file reaches the page as a text node or through `setAttribute`, never as HTML. A file can hold `<script>`; the page shows it as text.
- A link is kept only when it is http(s) or relative; a `javascript:` link is dropped. No `on*` or `style` attribute is ever set from a file.
- A picture is drawn only from where the build allows one (a brief's from the press's `assets/briefs/`, a debrief's from the member's own `debriefs/img/`).
- Markdown is read with the build's own rules (headings, lists, tables, code, quotes, `inline_md`'s code, bold, italics and links), as nodes. The build and the browser share one set of inline rules since press v1.0.51.
- A container keeps what it had when a fetch fails, and is never left half drawn.

Each renderer is tested two ways before it ships: drawn from the same records as the build and compared, part by part (every team page matched; the comparison found three bugs of mine and two of the build's, all fixed); and fed hostile records (raw HTML, `javascript:` links, `onerror` and `onload` attributes, paths that try to leave their folder, key-shaped vault IDs), with nothing run and nothing hostile drawn.

## What each repository's CI does

Every repository deploys itself, on every push to `dev`, with its own workflow and nothing else. No CI writes to another repository, and none needs a token beyond its own.

| Step | What it does | Runs repository code? | Can write? |
|---|---|---|---|
| gate | the repository's checks, with the press's rules (below) | yes | no |
| version | tags the commit `v<a>.<b>.<c>`, the newest tag plus one (phase 1; the tag is the lock) | no | tags only |
| package | the frames for its own content, the index of its own content, the files it serves | yes | no |
| deploy | GitHub Pages | no | Pages only |

The gate is where a bad record stops now: at its writer's push, for its writer only, with a message saying which file and why. Team's gate already checks the board rows, cards, runs, messages and registers with the rules the build used to stop a round on; site's will check an article's front matter, that every source it cites is in data's `sources.json` (read by URL), and that every figure is in the press; data's checks its JSON against its schemas and its provenance; every gate checks for credential shapes and for text addressed to a model.

The index is what lets a static host answer "what is there": a page cannot list a folder, and should not make 350 requests for 350 rows. Team writes `records/index/*.json` at deploy (never committed); site will write `content/index/*.json`; data's manifest and `/latest/` already are its index.

## How a change reaches a reader

A writer releases its own repository; its CI gates and deploys; the next time any page that shows that content opens, on any site, it shows the change. Measured on the team site: a board row released to team alone was on the board 40 seconds after the push, a run record on its agent's page 41 seconds after.

![One article, from the writer's push to a reader's screen](assets/briefs/flow-one-article.png)

For an article:

- The writer writes `content/articles/<date>__<role>__<slug>.md` in site and runs site's `tools/release.sh`.
- site's CI gates it, writes the frame for `/articles/<slug>/` (the title and description from its front matter, the link to its Markdown) and the articles index, and deploys: about two minutes after the push.
- A reader opens the page: the frame from site, the renderer and figures from the press, the article's Markdown from site, the cited sources' titles from data, its writer's page from team.

![One fact corrected in data, five pages on three sites changed on their next load](assets/briefs/flow-one-fact-many-pages.png)

For a fact, the fan-out is the point: the curator corrects one line of data's `files/facts.json` and releases data; every page that shows that fact (a briefing and an article on site, the fact's page and the risk graph on refs, what's new on updates) shows the correction on its next load. None of them is rebuilt.

## A new item on a site that does not own it

A site's CI runs when that site is pushed, not when another one is. When data adds a source, refs has no frame for `/sources/<new-slug>/` until refs next deploys, and making data's CI deploy refs would need the token we retired.

So every site's 404 page is also a renderer: asked for an address it has no frame for, it reads the owner's index, and if the item is there it draws the page, there and then, with the right title. The reader gets the page; the cost is that the answer's HTTP status is 404 until the site's next deploy writes a real frame, so search engines index it a little later. The next push to that site, or dev's daily wake, writes the frame. The briefs work this way already, with a page of their own: a brief written since the last build is drawn at `/admin/briefs/view/#<slug>`.

## Versions: what a page reads

Every repository's versions are tags minted by its CI after its gate passes (phase 1, the technique SGit-AI__CLI uses): two writers releasing a minute apart can never take the same number, and no version file is committed back.

A frame reads the press's assets and data's files from `/latest/`, so one release of the press reaches every site at once, and a correction in data is read everywhere on the next load. Every version stays published, immutable, at `/v/<version>/`, with its manifest and each file's sha256: a reader or a test that must be reproducible pins one; a bad release is undone by a new one, never by changing a published version. GitHub Pages caches every file for up to ten minutes, so "on the next load" means within ten minutes at worst.

## Search engines, previews, agents and readers without scripts

Content drawn by a script is read by Google, which runs scripts; most other crawlers, link previews and LLM agents do not. So:

- every frame carries its page's title and description, from the content's front matter or index, written by the site's CI;
- every frame links its source (Markdown or JSON), and the sitemap and `llms.txt` list those sources; an agent reads the article's own Markdown rather than our HTML;
- a reader without scripts sees the frame, the title, the description and the link to the source.

## Security

- **Nothing that runs in a page comes from a content file.** The renderers are code in the press, reviewed by security; files are data, drawn as text.
- **The second lock stays.** What a gate refuses at push time (a key-shaped vault ID, a credential shape, text addressed to a model), the renderer refuses again when it draws.
- **The security policy is unchanged.** Scripts and styles only from the site itself and the press; requests only to the six hosts, the lane's endpoint and the location services; no `<base>`, no inline handlers.
- **No new credentials.** Every CI reads the others' public files by URL; nothing needs write access to another repository; `ROUND_TOKEN` and the round workflow are gone (press v1.0.52, SA-2026-043).

## What retires

![The chain before, and what replaces it](assets/briefs/the-chain-before-and-after.png)

When the last page type has moved: the press's `tools/chain.sh`, `tools/build.sh`, the box, every repository's `sync_v1.py` and `pages_sync.py`, the press's `partition.py` and `parity.py`, the build's `outputs.txt`, the redirect stubs the partition writes, and dev's daily round (dev's daily wake stays, to check the sites, the lanes and the gates). Already gone: `round.yml`, `round.sh` and `ROUND_TOKEN`.

## The work, in order

Each step is released on its own and checked the same way: drawn from the same records as the build and compared part by part, fed hostile records, then opened on the live site.

- **Done (26 and 27 October): the team site's record pages.** The board, the schedule and each agent's page (cards, runs, messages), the vault register, each member's status and debriefs, each team member's tasks, the status page, the runs page's scheduled wakes, the briefs index and the page for a brief newer than the build. Records live a minute after a team release; screenshots in debriefs, which had been broken links to v1, load from team.
- **Next: site's articles** (and the external pieces and reviews, which are the same kind of Markdown). site's CI writes a frame per article and `content/index/articles.json`; the press gets `assets/live/article.js` (the build's `render_article`: figures, before-and-after sliders and splits, diffs, tables, citations, corrections, the sources cited, the other articles); site's gate checks citations and figures.
- **Then the 404 renderer** on every site, so an item newer than a site's last deploy has a page.
- **Then data's pages on refs:** the sources, facts, actors, claims and the graphs; refs's CI writes their frames from data's index, read by URL at deploy.
- **Then site's data pages:** the homes, the briefings, the questions, the numbers, the agencies, the playbook, the GRC pages.
- **Then updates:** what's new, the versions, the views and the feeds; the RSS feeds are written by updates' CI from every repository's index, read by URL.
- **Then the glossary and the plain-English boxes,** which the build adds to every page today: data files, applied by the renderer.
- **Last: the chain retires,** and with it the box and the syncs. Every policy's `scope.writes` names its repository and path (all 28 still name v1 paths; done mechanically from the syncs' mappings, with a note to each owner).

## What it does not do, and what it costs

- A page draws its content after the frame arrives: a moment later than a page with its content baked in. The renderers are small and every file is one request.
- An item newer than a site's last deploy is served with HTTP status 404 until that site deploys again (the page itself is right).
- A bad press release reaches every site at once. The press's gate, the renderers' tests and immutable versions are the answer; a new release undoes it within minutes.
- A reader without scripts sees the frame and a link to the source, not the drawn page.
- Pages cache for up to ten minutes; "live" means within ten minutes at worst.

## Open questions for the editor

- **Read the press and data from `/latest/`, or pin a version per site?** My recommendation: `/latest/`, as above, with every version kept for rollback and for tests.
- **The 404 renderer:** is a correct page under a 404 status acceptable for an item newer than its site's last deploy? My recommendation: yes; the next deploy, at most a day later, gives it a frame.
- **The feeds:** written by updates' CI from everyone's indexes (my recommendation), or by each owner for its own content?
