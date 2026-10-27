# PROJECT-001 phase 1, step 1a: what we hold about each actor

By ontologist@php.newsroom (run by projects@php.newsroom as a subagent), 27 October 2026. Data repository 0.1.62, refs commit 6407d1f. Full detail: `actors-audit.json` beside this file. Nothing was sent, committed or released.

## Totals

- 27 actors audited; **8 complete, 19 not**. "Complete" is strict: own page, nothing missing from actors.json or from the page, usable words of their own, every listed source cited by a claim row, no undated KEV line, no blocked or 404 capture.
- 44 sources in sources.json that belong to an actor but are not in actors.json (48 counting NCSC-NL under both agencies and rijksoverheid). Listed slugs missing from sources.json: 0.
- KEV: **0 page lines** say "CISA has not observed exploitation" or "not in KEV" without a date. 3 page lines carry the phrase dated and marked superseded (agencies:23, agencies:27, akamai:17). Only the agencies and Akamai pages carry the 26 October listing. **2 undated stale statements sit in data `outreach.json`**, not on a page: R-004 `evidence`, R-006 `evidence`.
- No text addressing an AI was found in any page, source note or request read (the word "claude" appears only in agent names such as claude-story-site).
- Four named candidates have **no page of their own**: NCSC-NL, NCSC UK, CISA (all inside `agencies`; NCSC-NL also inside `rijksoverheid`) and Trend Micro (nowhere).

## Table

Listed = sources in actors.json; found = ours by publisher or host; miss = found but not listed; own = a usable publication of theirs held; page = complete; KEV-stale = undated lines; corr = outreach requests (open unless noted).

| Actor | Listed | Found | Miss | Own | Page complete | KEV-stale | Corrections |
|---|---|---|---|---|---|---|---|
| php-group | 3 | 5 | 2 | y | n | 0 | - |
| php-foundation | 1 | 2 | 1 | y | n | 0 | - |
| zelenka | 2 | 4 | 2 | y | n | 0 | - |
| daubois | 1 | 1 | 0 | y | y | 0 | - |
| calif | 2 | 2 | 0 | y | y | 0 | - |
| openai | 3 | 4 | 2 | y | n | 0 | - |
| wiz | 2 | 2 | 0 | y | n | 0 | R-001 drafted |
| quarkslab | 2 | 1 | 1 | y | n | 0 | - |
| cloudflare | 1 | 1 | 0 | y | y | 0 | - |
| amazon | 1 | 1 | 1 | y | n | 0 | R-004 blocked* |
| chainguard | 2 | 0 | 0 | n | n | 0 | - |
| watchtowr | 2 | 2 | 2 | n | n | 0 | - |
| agencies | 3 | 33 | 30 | y | n | 0 | - |
| bbc | 1 | 1 | 0 | y | n | 0 | R-002 drafted |
| woodward | 1 | 0 | 0 | n | n | 0 | - |
| thn | 1 | 3 | 2 | y | n | 0 | R-007 drafted* |
| chainguard-lorenc | 2 | 0 | 0 | n | n | 0 | - |
| prince | 1 | 1 | 0 | y | y | 0 | - |
| imperva | 1 | 1 | 0 | y | y | 0 | - |
| fastly | 1 | 1 | 0 | y | y | 0 | - |
| akamai | 2 | 2 | 0 | y | n | 0 | - |
| huntress | 1 | 1 | 0 | y | y | 0 | - |
| weirdgloop | 1 | 1 | 0 | y | y | 0 | - |
| rijksoverheid | 2 | 6 | 4 | y | n | 0 | - |
| valtori | 2 | 1 | 1 | n | n | 0 | - |
| detectors | 4 | 4 | 0 | y | n | 0 | - |
| leblanc | 1 | 1 | 0 | n | n | 0 | - |

`*` = request has actor null in outreach.json; matched by publisher (R-004 AWS to amazon, R-007 The Hacker News to thn). All 12 requests are drafted or blocked; none sent. R-003, R-005, R-006, R-008 to R-012 name publishers that are not actors (CNN, WIRED, BankInfoSecurity, Fortune, Clarin, Le Temps, ITmedia, TechTarget).

## Named candidates without a page of their own

| Name | Where it lives | Found | Miss | Own words |
|---|---|---|---|---|
| NCSC-NL | rijksoverheid | 6 | 4 | y |
| NCSC UK | agencies | 1 | 0 | y |
| CISA | agencies | 7 | 6 | y |
| Trend Micro | none: no actor in actors.json, no page names Trend Micro | 1 | 1 | y |

- **NCSC-NL** found: ncsc-nl-advisories, ncsc-nl-php2shell, ncsc-nl-php2shell-software-list, ncsc-nl-php2shell-software-list-letters, ncsc-nl-site, rijksoverheid-ncsc-php-news
  - no page of its own; covered by two pages (rijksoverheid and agencies) that split its sources inconsistently
  - actors.json lists for rijksoverheid only rijksoverheid-ncsc-php-news and ncsc-nl-php2shell; missing: ncsc-nl-advisories, ncsc-nl-php2shell-software-list, ncsc-nl-php2shell-software-list-letters, ncsc-nl-site
  - the agencies page cites ncsc-nl-advisories and ncsc-nl-php2shell-software-list in claim rows but the actor does not list them
  - ncsc-nl-site is a home page only
- **NCSC UK** found: ncsc-news-php
  - no page of its own: one advisory (ncsc-news-php) inside the agencies page; nothing else of theirs held
  - we hold no NCSC UK statement after 21 October; check for one before asking
- **CISA** found: cisa-alert-kev-20261026, cisa-alert-log4j-2021, cisa-alert-php-20261021, cisa-ed-22-02-log4j, cisa-home, cisa-kev-catalog, cisa-kev-json
  - no page of its own: the sources sit inside the 13-agency page, so a recipient page would have to be carved out of it
  - actors.json lists only cisa-alert-php-20261021 for the agencies; missing: cisa-alert-kev-20261026, cisa-alert-log4j-2021, cisa-ed-22-02-log4j, cisa-home, cisa-kev-catalog, cisa-kev-json
  - the KEV statement of 26 October is on the agencies page (claim rows, lines 23 and 27) but the leading words of line 23 still read "CISA had not observed exploitation and neither CVE was in KEV" with status confirmed / A6; make the superseded status lead the row
  - cisa-ed-22-02-log4j capture is a 404 (not its text); cisa-home is a home page only
- **Trend Micro** found: trendmicro-ja-jp-about-newsroom-press-releases-2026
  - no actors.json entry and no page: create a party page (Trend Micro, with the press release of 23 October 2026) before any request
  - the one source is Japanese and held as news, primary false: recheck kind and publisher ("トレンドマイクロ" is not yet an alias of Trend Micro in the ontology), add an English reading of what the release claims (a free PHP2Shell Exposure Checker)
  - we hold one source only; look for an English Trend Micro post before asking

## Gaps per actor (what phase 2 must add)

**php-group** (The PHP Group / php.net)
- add to actors.json: github-php-src-branch-7.4-backport, github-php-src-tag-php-8.5.12
- page does not name at all: github-php-src-branch-7.4-backport
- uncertain: cve-cve-2026-109618 (CVE record, publisher "CVE Program (CNA: PHP Group)": PHP Group is the numbering authority); cve-cve-2026-109619 (same as CVE-2026-109618)

**php-foundation** (The PHP Foundation)
- add to actors.json: phpfoundation-blog-security-release-leak
- page does not name at all: phpfoundation-blog-security-release-leak
- page shows no claim row, so it says nothing about how we used its sources
- named in the sources list but cited by no claim row (how used not shown): php-foundation-blog-security-release

**zelenka** (Jakub Zelenka (bukka), PHP security team)
- add to actors.json: github-ghsa-6wmf-4rv5-p3rp, openwall-oss-security-2026-10-21-7

**daubois** (Alexandre Daubois, PHP security team (personal blog)): complete

**calif** (Calif (Ryan Austin, @lcfr_hax; Michal Zalewski)): complete
- uncertain: php2shell-com (joint microsite of OpenAI, Wiz and Calif (php2shell.com): belongs to all three, owner not )

**openai** (OpenAI (Patch the Planet, Codex Security, Amy Burnett))
- add to actors.json: openai-blog-coordinated-disclosure, openai-patch-the-planet-launch
- page does not name at all: openai-blog-coordinated-disclosure, openai-patch-the-planet-launch
- named in the sources list but cited by no claim row (how used not shown): patchtheplanet-org, openai-community-php-flaws
- capture is not their text (blocked/404): openai-blog-coordinated-disclosure, openai-patch-the-planet-launch; recapture or say plainly we do not hold it
- uncertain: php2shell-com (joint microsite of OpenAI, Wiz and Calif); openai-community-php-flaws (listed on the page, but a post on the OpenAI Developer Community forum by a user ("sps", L)
- listed but third-party (about them, not theirs): openai-community-php-flaws

**wiz** (Wiz Research)
- page shows no claim row, so it says nothing about how we used its sources
- named in the sources list but cited by no claim row (how used not shown): wiz-blog-php2shell, x-wiz-io-php2shell
- uncertain: php2shell-com (joint microsite of OpenAI, Wiz and Calif)

**quarkslab** (Quarkslab, OSTIF)
- add to actors.json: quarkslab-blog-php-src-audit
- named in the sources list but cited by no claim row (how used not shown): php-foundation-blog-security-release, calif-php2shell
- listed but third-party (about them, not theirs): php-foundation-blog-security-release, calif-php2shell

**cloudflare** (Cloudflare): complete

**amazon** (Amazon (CJ Moses))
- add to actors.json: aws-security-blog-madpot
- listed but third-party (about them, not theirs): thehackernews-php2shell-4days

**chainguard** (Chainguard)
- named in the sources list but cited by no claim row (how used not shown): techzine-php-chainguard
- no usable publication of their own held (all sources are about them): ask or capture before any request
- uncertain: x-feross-chainguard (post by Feross Aboukhadijeh (@feross) about Chainguard, not Chainguard's own)
- listed but third-party (about them, not theirs): php-foundation-blog-security-release, techzine-php-chainguard

**watchtowr** (watchTowr)
- add to actors.json: watchtowr-php2shell, watchtowr-php2shell-faq
- capture is not their text (blocked/404): watchtowr-php2shell, watchtowr-php2shell-faq; recapture or say plainly we do not hold it
- no usable publication of their own held (all sources are about them): ask or capture before any request
- listed but third-party (about them, not theirs): daubois-blog-php2shell-rumors, certeu-sa-2026-018

**agencies** (National agencies (NSA, CISA, NCSC UK, CERT-EU, CERT-FR, CCC)
- add to actors.json: nsa-x-2112903220209098897, nsa-x-2113068811058622971, nsa-x-nsacyber, cisa-alert-kev-20261026, cisa-alert-log4j-2021, cisa-ed-22-02-log4j, cisa-home, cisa-kev-catalog, cisa-kev-json, certeu-sa-2026-018, certfr-2026-ale-014, cccs-al26-026, cccs-alerts, acsc-alert-php, acsc-home, cyber-gov-au-site, ncsc-nz-alert-php, ncsc-nz-alerts, ncsc-nl-advisories, ncsc-nl-php2shell, ncsc-nl- ... (full list in the JSON)
- page does not name at all: nsa-x-2112903220209098897, nsa-x-2113068811058622971, nsa-x-nsacyber, cisa-alert-log4j-2021, cisa-ed-22-02-log4j, cisa-home, cccs-al26-026, cccs-alerts, acsc-alert-php, acsc-home, cyber-gov-au-site, ncsc-nz-alert-php, ncsc-nz-alerts, ncsc-nl-php2shell, ncsc-nl-php2shell-software-list-letters, ncsc-nl-site, rijksoverheid-ncsc-php-news, acn-it-php2shell, ch-ncsc-home, jpce ... (full list in the JSON)
- named in the sources list but cited by no claim row (how used not shown): nsa-press-php-4630238, ncsc-news-php
- capture is not their text (blocked/404): cisa-ed-22-02-log4j, cyber-gov-au-site, ncsc-nl-php2shell-software-list-letters; recapture or say plainly we do not hold it
- uncertain: nsa-x-nsacyber-nitter (nitter.net mirror of the NSACyber account; a third-party mirror, not NSA); lv-latvija-gov (latvija.gov.lv is a government portal that went offline, not CERT.LV); enisa-cnw-2026-04-php (ENISA / EU CSIRTs Network advisory: an EU agency not named on the agencies page); ccn-cert-al-11-26 (CCN-CERT (Spain) advisory: national CERT not named on the agencies page)

**bbc** (BBC News (live page; Kieran Kelly, Imogen James))
- page shows no claim row, so it says nothing about how we used its sources
- named in the sources list but cited by no claim row (how used not shown): bbc-live-ckgel5xp2xv9t

**woodward** (Alan Woodward, Surrey Centre for Cyber Security)
- no usable publication of their own held (all sources are about them): ask or capture before any request
- listed but third-party (about them, not theirs): bbc-live-ckgel5xp2xv9t

**thn** (The Hacker News (Ravie Lakshmanan))
- add to actors.json: thehackernews-php2shell-unpatched-alert, thehackernews-what-protects-you
- page does not name at all: thehackernews-php2shell-unpatched-alert, thehackernews-what-protects-you

**chainguard-lorenc** (Dan Lorenc, Chainguard)
- no usable publication of their own held (all sources are about them): ask or capture before any request
- uncertain: x-feross-chainguard (post by Feross Aboukhadijeh about Chainguard, not Dan Lorenc)
- listed but third-party (about them, not theirs): theregister-php-blames-chainguard, x-feross-chainguard

**prince** (Matthew Prince, Cloudflare CEO): complete

**imperva** (Imperva Threat Research): complete

**fastly** (Fastly): complete

**akamai** (Akamai)
- named in the sources list but cited by no claim row (how used not shown): akamai-blog-php-core-rce

**huntress** (Huntress): complete

**weirdgloop** (Weird Gloop (cookmeplox)): complete

**rijksoverheid** (The Dutch government and NCSC-NL)
- add to actors.json: ncsc-nl-advisories, ncsc-nl-php2shell-software-list, ncsc-nl-php2shell-software-list-letters, ncsc-nl-site
- page does not name at all: ncsc-nl-php2shell-software-list-letters, ncsc-nl-site
- named in the sources list but cited by no claim row (how used not shown): ncsc-nl-php2shell
- capture is not their text (blocked/404): ncsc-nl-php2shell-software-list-letters; recapture or say plainly we do not hold it
- uncertain: overheid-nl-site (overheid.nl is the Dutch government portal, not the Rijksoverheid news site or NCSC-NL)

**valtori** (Valtori and NCSC-FI)
- add to actors.json: fi-valtori
- page does not name at all: fi-valtori
- capture is not their text (blocked/404): fi-valtori; recapture or say plainly we do not hold it
- no usable publication of their own held (all sources are about them): ask or capture before any request
- listed but third-party (about them, not theirs): yle-finland-government-sites-shut, helsinkitimes-finland-shutdown

**detectors** (Community detection authors (darkfibr, rjmendez, Lexsah, Ble)
- named in the sources list but cited by no claim row (how used not shown): github-darkfibr-php2shell-detect, github-lexsah-php2shell-detection, gist-blevene-detection-guide
- uncertain: gist-silascutler-censys-query (detection-adjacent gist (Censys query) by Silas Cutler, not one of the four named authors)

**leblanc** (Arnaud Le Blanc and the PHP fix authors)
- page shows no claim row, so it says nothing about how we used its sources
- named in the sources list but cited by no claim row (how used not shown): github-php-src-fix-commit-3584a98bd
- capture is not their text (blocked/404): github-php-src-fix-commit-3584a98bd; recapture or say plainly we do not hold it
- no usable publication of their own held (all sources are about them): ask or capture before any request
- uncertain: github-php-src-branch-7.4-backport (backport branch in php/php-src; author not stated in sources.json); github-php-src-tag-php-8.5.12 (release tag "by adoy", not shown to be the fix author)

## Uncertainty

- Matching is by publisher string and URL host; news articles that merely name an actor are not counted as theirs. Joint or doubtful items are in each actor's `uncertain` (php2shell.com microsite shared by OpenAI, Wiz, Calif; the OpenAI community forum post; the CVE records issued by the PHP Group as numbering authority; nitter and Silas Cutler gists; agencies not named on the agencies page: ENISA, CCN-CERT, CNCS, NUKIB, NIST NVD).
- Captures marked "blocked" (watchTowr both, OpenAI blog, CISA ED 22-02 404, Valtori down, NCSC-NL letters folder, the php-src fix commit with no capture) are counted as found but not as their own words.
- The agencies actor holds 13 agencies in one page: its "found" count (33) is a union; the per-agency split is in `agency_breakdown`.
- BBC and The Hacker News: their reporting counts as their own words (it is their publication), though it is not a statement about themselves.
- Page "how used" is judged by whether a claim row cites the source; pages with no claim row (bbc, php-foundation in part, wiz, leblanc) show none.
