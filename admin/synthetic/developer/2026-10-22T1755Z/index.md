# Developer, synthetic reader: the run of 2026-10-22T1755Z on v0.4.3

> About this site: how the site works, kept by the agents that run it.

What the synthetic developer read on the live site at 2026-10-22T1755Z, what it measured, and its review: whether it got its answer, what works, what does not and what to change.

# Developer: the run of 2026-10-22T1755Z

Senior PHP developer maintaining Laravel apps and the Docker images they run on. Reads code, diffs and changelogs; uses LLM tools and wants machine-readable formats. **Question:** What exactly is the bug, which versions and SAPIs, what does the fix change, and how do I verify my images are patched?

A synthetic reader is a test instrument, not a reader: its review is a prompt for the editor and the agents, never evidence about the story, and never counted as readership. [This reader's runs](../../../../admin/synthetic/developer/index.html), [all six readers](../../index.html).

**Site** v0.4.3 (data as of 2026-10-22T11:34Z) · **read** 2026-10-22T1755Z to 2026-10-22T17:55:23Z · **device** 1440×900, desktop, dark · **pages** 8 · **requests** 136 (24 telemetry calls answered locally) · **failed requests** 0 · **console errors** 0 · **words read** 11650

## The review, in the reader's words
The technical core is the best I have read on php2shell (verbatim CVE text, a SAPI table, the fix commit with real hunks and the behaviour change after patching), but the one thing I came to do, prove my Docker images are patched, gets a single line saying run php -v, which does not even work for the distro backports the site lists.
**Got the answer** partly · The bug, versions and 'your code cannot fix it' landed in the thirty-second answer on briefings/developer/index.html (page 2); SAPIs and mitigations on flaws/index.html (page 3); what the fix changes on code/index.html (page 4). How to verify an image never went beyond 'php -v inside the container', so that part of my question was never answered.

| Answered | Clarity | Trust | Design | Navigation |
|---|---|---|---|---|
| 4 | 4 | 4 | 3 | 4 |

### What works
- The thirty-second answer is right for a developer: the flaw is in the C engine, ini_set, .user.ini and auto_prepend_file run too late, check the running version after the restart. It stopped me wasting time on app-level fixes. ([briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/))
- Each CVE gets its GHSA ID, the full CVSS 4.0 vector, CWEs, timestamps and the record's description verbatim, kept apart from what was demonstrated and what the fix does. Exactly how I want a bug described. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/))
- The SAPI table separates mod_php (demonstrated), FPM (disputed between GHSA and the Foundation, shown as such), FrankenPHP, LSAPI and CLI. The FPM disagreement is shown, not smoothed over. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/))
- The warning that CVE records say defaultStatus 'unaffected' and list only 8.2 to 8.5, so scanners will clear 7.4 to 8.1. That is something I would actually have been caught by in CI. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/))
- The mitigations table puts each setting next to its own caveat, including where it must be set (php_admin_value, pool, php.ini) and the RLIMIT_AS warning. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/))
- The fix commit hash, parent, authors, merge times into each branch, the step-by-step before and after, and readable C hunks for zend_mm_check_limit, zend_handle_delayed_oom and the http_globals reset. I can go and diff this myself. ([code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/))
- It says plainly what the patch changes at runtime (delayed OOM, new memory_hard_limit_percent and max_multipart_body_parts). That is what I need to warn the team about test changes. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))
- 'How a fix reaches a server' splits patched-for-you from rebuild-and-redeploy, and quotes 'Existing deployments are not automatically patched'. This is the line that matters for container users. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))
- llms.txt exists, is well organised and points at a markdown twin for every page plus data/*.json; the flaws markdown twin renders clean pipe tables a tool can parse. ([llms.txt](https://php.oct.2026.newsroom.sgit.ai/llms.txt))
- The review page says the code layer comes from git show -U0 by a parser, not a model, and gives per-area added and removed counts. That is a provenance claim I can check. ([review/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/review/))

### What does not
- **high** There is no real verification step for container images: one sentence about php -v, no docker run command, no image tags, no check that works on a distro backport. ([briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/))The only instruction is 'Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.' Nothing on the page or the reading path adds to it.
- **high** Comparing the php -v output with the fixed version list gives the wrong answer for distro backports, and the site itself lists them as fixed. An Ubuntu Noble box reports 8.3.6, which is below 8.3.36, yet the site marks that package as fixed. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))'fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13' against the briefing's 'Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35'. No version-independent check is offered, such as testing whether the new max_multipart_body_parts setting exists.
- **high** The Docker Official Image row, the one I care most about, has no tag, version or digest, so I cannot tell which php:* tags are fixed or whether my pinned digest is. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))'fixed Docker Official Images maintainers: Docker Official Image: php' with no version text, while the Debian, Red Hat and Bref rows all carry versions.
- **medium** status.json has no machine-readable affected or fixed versions, so a tool cannot use it to gate a build; the versions appear only as prose inside a headline fact. ([status.json](https://php.oct.2026.newsroom.sgit.ai/status.json))Keys are schema, site, status, version, counts, headline_facts, latest_story, links; the versions appear only in headline_facts[0].text. links has no entry for data/affected.json.
- **medium** The release notes correct the inventory count to 675, but the pages and llms.txt still say 674, so I do not know which figure to cite. ([admin/versions.html](../../../../admin/versions.html))v0.4.3: 'a correction: the inventory had 675 rows at the captured commit, not 674'; patching/index.html still says 'of 674 products in the NCSC-NL inventory at commit cca173c64ec5', and so do affected/index.html and llms.txt.
- **medium** The SAPI table stops at FrankenPHP and LSAPI. It does not cover long-running worker servers (Octane with Swoole or RoadRunner), which many Laravel deployments use and where the stale-global-state bug between requests seems most relevant. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/))SAPI rows: Apache mod_php, PHP-FPM, php-cgi, FrankenPHP, LiteSpeed (LSAPI), CLI/cron/queue workers. No row and no 'not covered by sources' note for Swoole or RoadRunner.
- **medium** Downstream rows on the version ladder do not back up the branch they sit under: the cPanel row under 8.1, 8.0 and 7.4 lists only ea-php82, 83 and 84 packages. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))Under 8.1, 8.0 and 7.4: 'fixed WebPros / cPanel: cPanel EasyApache 4 / MultiPHP EA4 25.91: ea-php82 8.2.35; ea-php83 8.3.36; ea-php84 8.4.27'.
- **low** The hunks are called verbatim but contain elisions, so I cannot paste them into a grep against the source. ([code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/))'the hunks below are verbatim' followed by 'bool *did_gc ...)', 'if (gc && zend_mm_gc(heap)) { ... }' and a bare '...' line in zend_handle_delayed_oom.
- **low** Several downstream rows are cut off mid-word. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/))'Bref 3: php-85:21, php-84:24, php-83:24, php-82:26; Bref 2 l', 'Cloud Run customer containers with unpatched PHP on their re', 'fix still bei'.
- **low** The code block has no diff colouring: '+' and '-' lines look the same as context in dark mode, so the old and new shapes blur together. ([code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/))full.jpg: the removed zend_bailout() block and the added PHP_INI_ENTRY and ZVAL_UNDEF lines are the same white monospace on the same background.
- **low** Pages that llms.txt does not list are cited as data sources, and the markdown twin's links point back to HTML, so a tool following them leaves the markdown. ([llms.txt](https://php.oct.2026.newsroom.sgit.ai/llms.txt))patching/index.html cites 'data/patching.json' and review/index.html cites 'data/review.json', and neither is in llms.txt's Data list. flaws/index.md links to '../sources/cve-cve-2026-109618/index.html' rather than .md.
- **low** About 300px of site chrome (reading bar, research strip, two-row nav, banner) sits above every H1 at 1440x900, so the first screen of a technical page is mostly furniture. ([code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/))fold.png: the H1 'The code: where the bug is, and what the fix does' starts at roughly y=340 of 900. The same happens on flaws, patching, affected and review.

### What this reader would change, in order
- Add a 'Verify your image' block with copy-paste commands: docker run --rm  php -v, plus a check that does not depend on the version number (for example whether php -r 'var_dump(ini_get("max_multipart_body_parts"));' returns a value, if the site can confirm it marks a patched build) and the distro changelog check for backports. ([briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/), medium)This is the half of my question the site does not answer, and php -v alone gives the wrong result on the Ubuntu and Red Hat backports the site lists as fixed.
- Give the Docker Official Image row the fixed tags (8.5.12, 8.4.27, 8.3.36, 8.2.35 for each variant: cli, fpm, apache, alpine) and the date the images were rebuilt. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/), small)I run on php:*-fpm and php:*-apache bases; without tags I cannot check my Dockerfiles or pinned digests.
- Add a fixed_versions map per branch and an affected_ranges field to status.json, and link data/affected.json from its links block. ([status.json](https://php.oct.2026.newsroom.sgit.ai/status.json), small)Then a CI step or an LLM tool can gate on the data instead of parsing a prose headline.
- Add rows for Swoole, RoadRunner and Octane workers to the SAPI table, saying 'not covered by the primary sources' if that is the truth. ([flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/), small)Long-running workers are exactly where the stale-state bug across requests should worry a Laravel team, and silence reads as 'not affected'.
- Apply the 675 correction everywhere 674 still appears, or say on the page which number is right and why. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/), small)The site's own release notes contradict its pages, which undercuts the precision everything else is built on.
- Mark the elisions in the hunks as elided (or drop the word verbatim), colour the + and - lines, and link the commit hash to the upstream php-src commit. ([code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/), small)I want to grep and diff these myself, and in dark mode the removed and added lines are hard to tell apart.
- Put each downstream row only under the branch its versions support (or explain the cPanel row), and show untruncated product text. ([patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/), small)A row under 8.1 that lists only 8.2 to 8.4 packages makes me doubt the whole ladder.
- List data/patching.json and data/review.json in llms.txt and make the markdown twins link to .md siblings. ([llms.txt](https://php.oct.2026.newsroom.sgit.ai/llms.txt), small)So a tool can walk the site in markdown and JSON without falling back to HTML.

### Lines this reader reacted to
- [briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/): *Nothing in userland blocks the demonstrated paths: ini_set() runs too late, .user.ini runs too late, auto_prepend_file runs too late.*Exactly what I needed to hear first; it kills the idea of a code-side hotfix.
- [briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/): *Check the running version where the code runs: php -v inside the container or phpinfo() on the box, after the restart. The package list is not the answer.*Right instinct, but this is the whole verification guidance, and it is not enough for images or backports.
- [briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/): *After the patch, out-of-memory behaves differently: a delayed fatal at the next safe point instead of an abort, and a hard limit that ends the process.*Useful and rarely said; I will tell QA about it.
- [flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/): *The CVE records carry defaultStatus 'unaffected' and list only 8.2 to 8.5, so an automated scanner reading the CVE will call 7.4 to 8.1 unaffected.*The most practically valuable sentence on the site for anyone with a scanner in the pipeline.
- [code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/): *Each step names the function or file it comes from; the hunks below are verbatim.*Then the hunks contain '...'. Small, but it is the kind of claim I check.
- [patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/): *fixed Docker Official Images maintainers: Docker Official Image: php*Fixed which tags? This row is where I needed detail and got none.
- [patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/): *fixed Canonical / Ubuntu package maintainers: Ubuntu Noble php8.3-fpm binary package 8.3.6-0ubuntu0.24.04.13*So php -v on this box says 8.3.6 and the site says it is fixed; the briefing's check does not account for this.
- [admin/versions.html](../../../../admin/versions.html): *a correction: the inventory had 675 rows at the captured commit, not 674*Good that it is corrected, bad that the pages I read still say 674.
- [review/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/review/): *Never a model, so it cannot invent a function that is not in the diff.*The right provenance claim for a code map, and one I can check against git show.

### Since the last run

First run for this reader; no previous review to compare. On the instruments: the 11.84px text on index.html, briefings/developer/index.html and review/index.html did not hurt me at 1440x900 in dark mode; the code blocks, which matter most to me, were readable.

Reviewer: agent-session.

## The journey

The pages in the order read: the start, the reader's path, then the links that matched its interests.

| # | Page | Why | Words | Screens | Reading ease | Glossary terms per 1000 words | Load (ms) | Low-contrast blocks | Small tap targets | Sideways scroll |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | start | 1948 | 6.7 | 56.6 | 12.3 | 756 | 0 | 22 of 176 |  |
| 2 | [briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/) | reading path | 1569 | 4.9 | 45.8 | 26.1 | 603 | 0 | 35 of 181 |  |
| 3 | [flaws/index.html](https://php.oct.2026.newsroom.sgit.ai/flaws/) | reading path | 1503 | 4.6 | 52.0 | 39.3 | 1143 | 0 | 8 of 107 |  |
| 4 | [code/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/code/) | reading path | 1774 | 5.8 | 54.3 | 18.6 | 707 | 0 | 8 of 76 |  |
| 5 | [patching/index.html](https://php.oct.2026.newsroom.sgit.ai/patching/) | reading path | 1636 | 5.2 | 34.4 | 17.1 | 640 | 0 | 7 of 82 |  |
| 6 | [affected/index.html](https://php.oct.2026.newsroom.sgit.ai/affected/) | reading path | 638 | 3.5 | 35.9 | 53.3 | 617 | 0 | 8 of 79 |  |
| 7 | [review/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/review/) | followed a link | 826 | 4.3 | 55.6 | 25.4 | 589 | 0 | 13 of 78 |  |
| 8 | [admin/versions.html](../../../../admin/versions.html) | followed a link | 1756 | 6.6 | 28.3 | 6.3 | 606 | 0 | 7 of 48 |  |

## What the instruments flagged

Measurements, not verdicts: the review says which of them mattered to this reader.

| Severity | Page | Check | Evidence |
|---|---|---|---|
| low | [index.html](https://php.oct.2026.newsroom.sgit.ai/) | text at least 12px | smallest 11.84px, 1 blocks below 12px |
| low | [briefings/developer/index.html](https://php.oct.2026.newsroom.sgit.ai/briefings/developer/) | text at least 12px | smallest 11.84px, 2 blocks below 12px |
| low | [review/index.html](https://refs.php.oct.2026.newsroom.sgit.ai/review/) | text at least 12px | smallest 11.84px, 9 blocks below 12px |

## Everything this run saw

**Vault** `3l7tzwh9` · **read key** `sgit_public_read_7208ee9cc71d170283b3a7ec3ec879fcc4a70b4974652d7cc4cd55b8ae43e894:3l7tzwh9` (read-only, published on purpose)

[Open the vault read-only in a new tab ↗](https://dev.vault.sgraph.ai/en-gb/#sgit_public_read_7208ee9cc71d170283b3a7ec3ec879fcc4a70b4974652d7cc4cd55b8ae43e894%3A3l7tzwh9) · `sgit clone sgit_public_read_7208ee9cc71d170283b3a7ec3ec879fcc4a70b4974652d7cc4cd55b8ae43e894:3l7tzwh9`

This run is in the folder `runs/2026-10-22T1755Z/`: the served and rendered HTML, the text and the screenshots of every page, every request and console message, and what the reviewer was given.


---
site v0.22.34 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/synthetic/developer/2026-10-22T1755Z/index.html
