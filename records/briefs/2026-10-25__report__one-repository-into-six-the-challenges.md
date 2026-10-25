# Report: one repository into six, the challenges

Status: a report, written by dev@php.newsroom on 25 October 2026, the third of four on the split. [Report: one repository into six, the first day in numbers](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__report__one-repository-into-six-the-first-day/) is what was done; [Report: one source for every file](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__report__one-source-for-every-file/) is the design. This one is what went wrong, what nearly did, what the checks caught, and what it taught. Every item says what happened, why, the fix and where it is recorded. Nothing here is hidden elsewhere: the mistakes are mine unless said otherwise.

## In short

| | Count |
| --- | --- |
| Design decisions reversed by the editor during the work | 2 (copies of the shared files; how versions are numbered) |
| Bugs found by the split that were also live on v1 | 2 (the control room under a view address; 30 links that never resolved) |
| Bugs the split itself introduced, found before release | 9 |
| Times a check stopped a release | 4 (two as designed; two because the check itself was wrong) |
| Things this session could not do | 2 (deploy the sites; read GitHub's Pages and ruleset settings) |
| Mistakes in the record, corrected | 2 (a wrong date; a staging name that was never made) |
| Work lost, then recovered | 1 (a parked branch's stash) |

## Decisions that changed under way

**1. The shared files: copied, then served once.** The first cut (press v1.0.0) gave each site its own copy of v1's assets and data, 726 files and 25.95 MB each. I treated the pages' Content-Security-Policy, which allowed scripts and requests only from the page's own host, as a fixed constraint and designed around it. The editor treated it as configuration we own: "we can change and maintain those CSP … we don't want to have engineering issues (and ironically security issues) by having multiple sources for the same files." He was right, and the lesson is general: a security control that forces duplication is costing security somewhere else, so change the control (carefully, by exact host) rather than multiply the thing it protects. The redesign took under an hour: the instruction came after v0.22.1 (17:10 UTC), and the first cut without copies was pushed at 18:01. It is [Report: one source for every file](https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-25__report__one-source-for-every-file/).

**2. Versions: every release adds one to the last number.** I had given the press and the data API semantic versions (a moved section, or a widened schema, as a minor release). The editor: "apart from the first commit where you can put the release version, either v1.0.0 or v0.1.0, every next commit is a minor one. So it's v1.0.1 .2 .3 .4 or v0.1.1 .2 .3 .4." Both release scripts now take no part argument and always add one to the last number; the press's and the data's `CLAUDE.md`, and the docstring of `tools/schema.py`, say so. The data release script is one of the files that goes to security for review; that change was flagged.

## Bugs that were live on v1 too

**3. The control room under a view address.** `/team/control/as/executive/` asked for `team/control/data/control.json` and showed "could not be loaded". Two bugs on one line: `assets/control.js` resolved its data address against `location.href`, which the line has already moved to the view, instead of the page as loaded; and it passed a `URL` object to `fetch()`, which the new resolver only routed for strings. The browser test of the split found it; it was broken on v1 the same way. Fixed in v1 v0.22.4 (`window.P2S_BASE`, and the `fetch` wrapper routes `URL` objects).

**4. Thirty links that never resolved.** The partition resolves every link of every page, and so it found the ones that resolve nowhere: 27 on the line's prototype page `/admin/design/line/agencies/` (one directory too shallow; board row 329, story-site's), two on `graph/component/` and one in an advisory's markdown. It leaves them as v1 wrote them and lists them in `press.json`, so a site's gate tells them apart from a link the press broke.

## Bugs the split introduced, caught before release

**5. Scripts build URLs the HTML does not show.** Rewriting links in the HTML is not enough: scripts compute addresses at run time (`root + 'assets/ask/ask.js'`, `'../../data/control.json'`). And once the line moves the address bar to a view, a relative address resolves against the wrong page, and the policy rules out `<base>` (`base-uri 'none'`). The fix is one resolver, `assets/route.js`, loaded first on every page, and a route in every page that tells it where each kind of address goes. The scripts that load other scripts call it; `fetch()` goes through it.

**6. The data API did not have every file the scripts fetch.** It had the story's data, not the files the pages' scripts read. Four were found by the browser test (items, telemetry, contributors, collaborators: data v0.1.2), four more by comparing every `data/*.json` name in the scripts and every `data-src` in the pages with the catalogue (control, personas, stack, subscriptions: v0.1.4). The catalogue's note had even said personas "stays with the site"; one source made that impossible.

**7. The version check asked the wrong site.** A page's `fetch('VERSION')` went through the route, found no section named `VERSION`, and fell through to the main site. Every site serves its own `VERSION`. Since press v1.0.3 the route maps each runtime path to the site itself.

**8. The team's records collided with a page.** I first put the team's records under `ops/`, which is also the address of v1's `/ops/` page, which the team site serves. They moved to `records/`.

**9. A redirect would have overwritten the team's front page.** The partition writes a redirect at every address another site owns, including `index.html`, the main site's home, which on the team repository is the front page its own `tools/front.py` writes. Redirects now skip a repository's own files (`KEEP` and `OWN` in the partition).

**10. `lstrip('./')` is not "remove the prefix".** The first link resolver stripped a leading `./` with `lstrip`, which removes any of those characters, so `../x` and `.well-known/` came out wrong. It was replaced by explicit candidates (`t`, `t/index.html`) checked against the set of files each site serves.

**11. Root-relative links.** A link starting with `/` was resolved against the page's directory, so `/assets/…` would never be found. Since press v1.0.1 it is resolved from the site's root.

**12. The team front page cut sentences mid-word.** "the session's permission check stopped it; the" (board row 099). The front page now cuts at a word and adds an ellipsis.

**13. A Python call that does not exist the way I used it.** The press's gate compiled each tool with `py_compile.compile(..., cfile='/dev/null')`, which fails with `FileExistsError`. It now uses `compile()` on the source.

## Checks that stopped a release

**14. A stale press.** After v1 v0.22.5 (the release that recorded the work), the partition refused to cut: "press v1.0.4 does not hold v1's assets at this commit", naming `assets/design/line/config.js` and `copy.json`. I had assumed that a release changing only documents changes no asset. It does: v1's build writes those two files from the content, so every v1 release can change the assets. The check worked; the chain (assets, data, cuts) ran again, and press v1.0.5 and data v0.1.5 followed four minutes later. This is also the strongest argument for pass two: as long as v1's build writes into `assets/`, every v1 release is a press release.

**15. A file without a schema.** The data release stopped at the four new runtime files: `schemas/subscriptions.schema.json: missing`. Each shape was written (`tools/schema.py`) in the release that added the file.

**16. A data release blocked by its own gate (the check was wrong).** The gate first failed whenever the working copy differed from the newest version, which is every import, so a new version could never be made. It now notes the difference ("release a new version") and still fails on any change to a published version. A gate change goes to security; it was flagged to security when it was made.

**17. A team gate stricter than the records (the check was wrong).** It required a `note` on every board row and a `policy.json` for every member; v1 has neither everywhere. The required keys are now id, title, status and owner; a missing policy is a note.

## What this session could not do

**18. Deploy.** None of the six repositories has run a Pages build: every host answers "Site not found" (checked at 18:00 UTC). Their Pages source must be "Deploy from a branch: dev, / (root)", or a deploy workflow, which goes through security. The session's network proxy blocks GitHub's Pages API, so it can neither set the source nor read it. Board row 328, the editor's.

**19. Test the real hosts.** So the sites were tested without them: Chromium, with each of the six host names intercepted and served from its repository (and `access-control-allow-origin: *`, which GitHub Pages sends; checked on the live v1 site). That tests the pages, the scripts, the route, the policy and the cross-host requests. It does not test GitHub Pages' own behaviour: certificates, its 404 handling of view addresses, its caching. Those are the first things to check once the sites deploy.

## Mistakes in the record

**20. The staging name.** The plan named the main site's staging address `next.php.oct.2026.newsroom.sgit.ai`; the DNS record the editor made is `site.php.oct.2026.newsroom.sgit.ai`, and `next.` does not resolve. I noticed only when checking the hosts after the second cut. Since press v1.0.4 the site's `CNAME`, its robots and every page's policy name `site.`; the plan, REALITY and the site repositories' instructions were corrected.

**21. The date.** I wrote "26 October" for the editor's instruction and the work in several places; it was all on 25 October. Corrected in v1's plan, REALITY and the board. Press versions v1.0.1 to v1.0.5 are published and never change, so their copies of `sites.json`, `tools/partition.py` and `tools/release.sh` keep "26 October" in a comment; the next press release carries the correction.

## Work lost, then recovered

**22. A parked stash.** Before the split I parked an unfinished piece of work (the persona-first proposal and its mockups) in a git stash. Clearing what I took for a stale stash, `git stash drop` dropped that one. It was recovered from git's unreachable objects (`git fsck --unreachable`, then `git stash store` with the commit), whole, and is parked again. Separately, a release interrupted mid-merge left `index.lock` and a half-merge; it was aborted and reset to the base, and since then every git command names its repository (`git -C`) instead of changing directory first.

## What is still hard

- **Every v1 release is a chain of releases.** v1 release, press assets and release, data import and release, four cuts and four releases: about five minutes by hand, and easy to leave half done. Until pass two moves the sources out of v1, it should be one script, which goes to security with the rest of the press.
- **Immutable versions grow.** The data repository keeps every version whole: 12.8 MB each, six of them on the first day. At that rate a hundred releases are 1.3 GB, which GitHub will not like. Options for pass two: publish only changed files per version and resolve the rest through the manifest, or keep old versions outside the repository (a release asset, a vault), or prune old versions after a notice. The editor's call.
- **The press is trusted by every page.** It is now the source of every script on four sites. Its review by security is the most important open item of the split.
- **Two append tokens are in immutable versions.** Telemetry and subscriptions carry their lane's write-only token; rotating one is a new version, and the old one stays readable, as it does in v1's history.
- **The repositories' names.** Every push answers "This repository moved", because GitHub has the repositories under a different capitalisation (`SGit-AI__Website__Newsroom__2026__Oct__PHP__press`) from the lower-case one the clones use, v1's included. Pushes follow the redirect; the clones' remotes should be updated before anything depends on the exact name.

## What I would do differently

- Ask, before designing around a security control, whether the control is fixed or ours to change.
- Test in a browser before the first cut, not after: three of the bugs above were found only by loading pages, and each would have been cheaper an hour earlier.
- Check names against DNS, not against the plan.
- Write the chain as one script on the first day, with its own gate, and send it to security with the press.
