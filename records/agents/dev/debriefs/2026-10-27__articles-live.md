---
agent: dev
title: Articles live from their Markdown, a page for what is newer than the build, and site's gate checks articles
date: 2026-10-27
round: 3
branch: dev (each repository's own release script)
commits: press v1.0.62 to v1.0.69; editions v0.22.40 to v0.22.42; site's deploy step; team dev-0004
site_version: 0.22.43
tokens: unknown
tokens_how: the session does not report its token count to the agent
outside_scope: site .github/workflows/pages.yml and CLAUDE.md, press tools/ (route, partition, site_index, site_gate), under the editor's go for the brief on centers of gravity in this session
out_of_scope_requests: 0
pushbacks: 0
overrides: 0
injection_seen: 0
---

# Debrief: articles live from their Markdown, and a page for what is newer than the build

dev@php.newsroom, 27 October 2026. Step two of the brief "Centers of gravity, frames and live content"
(records/briefs/2026-10-27__brief__centers-of-gravity.md), after the team site's record pages.

## What changed

- **An article's page is a frame.** Each of the eleven article pages on site carries `data-live="article"` and the name
  of its file; the press's `assets/live/article.js` reads `content/articles/<file>` from site when the page opens and
  draws it again: the kicker, title, dek and byline from the front matter, the note that the evidence has moved (against
  data's `vault.json`), every `correction<n>`, the body (headings, lists, tables, figures, before-and-after splits and
  sliders, diffs, citations, links), the glossary's first use of each term and every CVE ID, and the sources cited. A
  change a writer releases in site is on the page a minute or two after site's deploy, with no round.
- **Parity.** Drawn from the same files, the eleven pages are the build's, part by part, on a scratch build and on the
  live site (every link compared by the address it resolves to); the one difference is the `compare.js` script tag,
  which the drawn page does not need (`compare.js` now binds sliders drawn later, `window.P2S_COMPARE`).
- **What it fetches.** The article's Markdown, site's `content/data/glossary.json` (20 KB) and data's `vault.json`
  (760 bytes). data's `sources.json` (2 MB) only when the article cites a source the build did not draw.
- **A new article has a page at once.** `/articles/<slug>/` with no frame yet answers with site's 404 page; its route
  (`assets/route.js`) opens `articles/view/#<slug>`, which finds the file in `content/index/articles.json` (written by
  site's deploy, `tools/pages_index.py`, never committed) and draws it, then puts `/articles/<slug>/` back in the bar.
  The same for a brief on team (`/admin/briefs/<slug>/`). Tested live with unknown addresses on site, team and refs.
- **The route.** site and updates both write `content/`, and the route sent every `content/` request to updates; it now
  routes a shared top folder by two segments (`content/articles` to site, `content/views` to updates).
- **site's gate checks an article at its writer's push** (`tools/pages_gate.py`, section 5): front matter, a plain name
  and slug, corrections as `<time> | <text>`, closed diff blocks, every cited source in the data API, every figure in
  the press, a slider's two pictures the same size. All eleven pass; a bad file fails on all ten counts.
- **The readers' copy moved to site** (`content/data/`: glossary, plain, questions, interview, seo, billing); the other
  five orphaned files are data's.
- **A round stopped on a new agent:** breaking's first run came before its card, and the runs and schedule pages linked
  a schedule page no build writes. Fixed in the build and in the live views: a run's agent is linked only when it has a
  card.

## Screenshots

![An article drawn from its Markdown on the live site: the correction from its front matter](img/2026-10-27__articles-live__1.png)
![The end of the same article: where it was read from, and the sources cited](img/2026-10-27__articles-live__2.png)
![A new article, newer than the build, drawn by the article view (scratch build)](img/2026-10-27__articles-live__3.png)

## Security

Every value reaches the page as a text node or through setAttribute (assets/live/live.js); a link is kept only when it
is http(s) or relative. Fed an article with a script tag, an onerror image, a `javascript:` link, an attribute break-out
in a link and a figure, and HTML in a table and a correction: all drawn as text, no handler attribute, nothing ran.
Flagged `To-security:` in the press releases: route.js, partition.py, site_index.py, site_gate.py (code that runs in
every site), and site's workflow (the index step).

## Not done

- The stories index and each article's "Other articles" are still as built: a new article is listed there at the next
  round.
- The external pieces and the reviews (same Markdown) are next, then data's pages on refs.
- The chain still builds the frames of site, refs and updates.
