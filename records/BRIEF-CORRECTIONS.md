# Corrections to the brief, and to the site

Newest first. A correction names the date, what was wrong, what was found, and what was done instead. The mistake stays visible where it was made.

## 2026-10-24: the risk graph counted 91 of its edges twice

Since the risk graph was first built (v0.6.0), a claim that backs several risks had its "cites" edges to its sources added once for every risk: 75 repeated edges in the first graph of 442 nodes and 914 edges, 91 in the graph of v0.14.22 (721 nodes, 1,442 edges). Every repeat was the same claim citing the same source, so no link was wrong; the counts were too high. dev@php.newsroom found it while building the graph's history for CI-003 (`/grc/changes/`), where an edge is the same edge when its start, verb and end are the same. From v0.14.24 the build adds each edge once: 1,351 edges, of which 249 are read from a capture, 287 from the fix commit and 815 inferred. The figures quoted earlier (914, 1,418, 1,442) stay where they were written; the before-and-after article of 23 October carries a note.

## 2026-10-24: the Sherpa's CI-003 brief treated a shipped design as still open

The brief "the graph reviewed by people, and a first step for newcomers" (24 October, 09:40 London) listed the collaborator's design preference (A to D as complementary views) as waiting for the editor. It had shipped in v0.14.0 at 01:34 that morning, as the editor decided (story-site's brief "the redesign, live"): A is the front page, B /ops/, C /analysis/, D the team console. The Sherpa had measured the live phone header but not read what the design agent shipped. Found when the editor asked. Done instead: CI-003 items 1 and 2 rewritten against v0.14.14; the first step for newcomers is now precise: the front page's "Three ways to read this site" are his three doors under other names, offered by role and seventh on the page, 9,218px down on a phone (F035, a board row for story-site); and one inconsistency goes to the editor: the redesign puts the CTO in Operations, the three-views brief with the executive. The brief stays as written.

## 2026-10-24: the librarian's map had two members too many and one too few

The map of 22 October drafted a **design** member and an **ontologist** member. The record says otherwise: the story-site member is "Design, claims and the story pages" in the roster and its session `designer@php.newsroom` is mapped to it on `/team/status/`; and the cartographer joined "as the newsroom's ontologist" on its branch. Both splits are undone: design's files are the story site's, the ontology is the cartographer's. The map also drafted every `policy.json` without knowing that board 157 gives them to **abp@newsroom.sgit**; they are now kept by abp@, and the librarian's drafts are its starting point. The sherpa, the GRC desk, abp@ and pulse@ joined the map; the curator sessions are the newsroom lead's.

## 2026-10-22: the librarian built the cartographer's graph

The librarian built the fractal graph (`data/arcs.json`, `build_fractal()`, `/fractal/`) and changed the navigator and the stylesheet to show it. Graphs are the cartographer's scope, the navigator is the cartographer's and the stylesheet is design's. There was no map of who owns what when it was built; drawing that map is what showed it. The work stays as it is and is handed to the cartographer (the cartographer's, now the ontologist's, board rows "Join the other engine files", "Add the PHP 7.4 backport's hunks" and "Fill the cartographer"; first numbered 091, 092 and 101, renumbered as dev moved); the librarian's own scope is the catalogue (`admin/content/agents/librarian/`).

## 2026-10-22: the fractal graph, and the review navigator that never opened

The v0.1.0 correction below said the graph was not fractal. There is now one graph from the fifteen stakeholders down to the 359 changed hunks of the fix (`/fractal/`): every node opens into its own neighbourhood in the navigator, and every hunk links to its lines in php-src. It is fractal in that sense and not yet in the deeper one: a node does not yet open into a graph of a different kind (a source into its own claims graph, a function into its call graph).

Building it found two faults in the v0.2.5 review layer. The navigator at `/review/ui/` laid out the nearest sixteen neighbours of the node in focus and then drew all of them, so on the fix commit, which has 44, it stopped with a script error and showed nothing; it has done so since it shipped. And the review's nine `contains` edges named `area:Zend` and `area:main` while the nodes are `area:Zend/` and `area:main/`, so they joined nothing. The navigator now draws the sixteen and lists every neighbour; the fractal graph matches area ids either way and joins all 37 engine files to their areas. `data/review.json` itself is left as it was published.

## 2026-10-22, 20:03 UTC: two house stories, corrected from the fact-check desk's first run

"Where php2shell stands" said Italy gives no offline advice, and that the BBC's morning summary had the UK, US, EU and Australian agencies all advising offline. The fact-check desk (findings 43 and 45) found, in the same captures, that Italy's ACN does advise taking sites offline, and that the BBC page says those agencies urged users 'to apply the fixes', with the offline quote given to the NCSC alone. "php2shell in perspective" used the same BBC sentence as an example of a story hardening. Both stories now carry a dated correction above their text, which is left as written. The agencies and claims data the stories inherited the error from belong to claude-story-site (board 088).

## 2026-10-22, v0.4.2: the NCSC-NL inventory had 675 rows at the captured commit, not 674

Every page that counts the NCSC-NL inventory at commit cca173c64ec5 says 674 products, 3 of them not vulnerable. Reading the list's public history commit by commit, this site's new reader found 675: the vault's export had dropped one row, iBabs bestuursportaal, marked not vulnerable ('PHP is not being used in iBabs. This is confirmed by an email of the supplier.'). The other 674 rows and every status agree. The counts on the existing pages come from `data/software.json`, which is evidence and is only ever regenerated from the vault, so they are left as they are until the vault's export is fixed and re-run (board); the inventory pages built from the history carry the right count and say why.

## 2026-10-22, v0.3.1: the site's name, and who the front page is for

The site was named php2shell, after the incident. The editor's correction: it is PHP news for October 2026, which this month happens to be dominated by one security incident, and the next month can be tracked the same way. The brand, page titles and the footer now say PHP October 2026; php2shell stays as what the press calls the flaws. The front page had opened with CVE numbers, a nickname and the words unauthenticated remote code execution; it now opens with the current situation in plain words, and the technical version is on the specialist summary page.
## 2026-10-22, v0.2.10: "both ChatGPT and Claude", in part

The v0.1.0 entry below says no second model had read the vault. That is still true of the vault. What changed: the editor ran a research chat in Perplexity and gave this site its notes, which are now published in full and credited at /readings/, compared with the vault point by point. Perplexity read the web through search excerpts, not the vault, so this is a second reading of the story, not of the evidence. Board item 009 stays open for a second model reading the vault itself.

## 2026-10-22, v0.2.10: the pages that were free

The billing model said the site's account of itself was free, so that a reader would not be charged for checking it. The editor's rule is that every page is metered. Those pages are now metered at the 1p floor and never more; only the meter's own account pages stay free. The argument for the floor is kept on the billing page.

## 2026-10-22, v0.2.0: the repository and domain were renamed

After v0.1.0 the editor renamed the repository to `SGit-AI__Website__Newsroom__2026__Oct__PHP` and the domain to `php.oct.2026.newsroom.sgit.ai`, closer to the memo's `story.newsroom` shape. The `CNAME`, the site constants and this file were changed in v0.2.0; GitHub redirects the old repository name.

## 2026-10-22, v0.1.0: the brief's domain name

The memo proposes a name of the shape `php.story.newsroom.sgit.ai`; the repository's README already names `php.oct.2026.newsroom.sgit.ai`. The site is built for the README's name, with a `CNAME` file, because that is the one with a repository behind it. If the editor prefers the memo's shape, the `CNAME` file is the one line to change.

## 2026-10-22, v0.1.0: "both ChatGPT and Claude"

The first memo asks for both models to be used to connect the data. This first release was built in one Claude session reading the vault that several Claude agents filled; no second model has read the vault yet. Recorded as not done rather than described as done.

## 2026-10-22, v0.1.0: the semantic fractal graph

The second memo asks for the whole semantic fractal graph. What exists is one graph (claims, events, sources and citation edges) in `data/graph.json`, drawn on one page. It is not fractal: no node opens into a graph of its own. That is the next layer, not this one.
