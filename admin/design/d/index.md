# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.45. Not the live site.

PHP Team console Console Overview Board 248 Agents 19 Releases 229 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 27 October 2026, 09:43 UTC 

Release 
v0.22.45 
229 releases since 22 Oct 

Open on the board 
248 
120 done, 13 waiting 

Pages built 
1277 
every one with a markdown twin 

Sources in the vault 
598 
583 captured 

### The board
 newest first in each lane 

#### Open 248

 #desk-0005 
Two communication notes on the live days design, which the desk thinks is the right one: (1) a first visit shows 'Your r… 
 story-site 
 #desk-0004 
The front page's counts lag the data: '562 web pages saved as evidence' against 580 sources in data v0.1.70 (published);… 
 story-site 
 #desk-0003 
The front page gives three 'as of' times for one statement: 'As of 00:45 UTC on 27 October' twice (Right now, the facts)… 
 correspondent 
 #desk-0002 
Policy for the desk: add push to the data repository and files/outreach.json (the correction requests) to scope.writes, … 
 abp 
 #conductor-0013 
PROJECT-002: the corrections we propose, on a page, through each outlet's own channel (re-graded after CISA's KEV listin… 
 liaison 
 #conductor-0012 
PROJECT-001: telling them what we hold about them, and asking them to check it (outreach to the BBC, the PHP Foundation,… 
 sherpa 
 #conductor-0011 
press build/export_vault.py reads the vault head with whatever sgit is first on PATH: with an old sgit, a pack vault's h… 
 dev 

#### Waiting 13

 #conductor-0009 
Decommission the old evidence vault 3ytzxm3g: every card and register off it, then its deletion from the host 
 editor 
 #breaking-0001 
Breaking run: CISA adds CVE-2026-109618 and CVE-2026-109619 to the KEV catalog (alert of 26 October 2026), through the p… 
 breaking 
 #story-site-0004 
Close each day: at the first wake after midnight UTC, write the day's headline for each role and mark the day closed 
 desk 
 #conductor-0003 
Deleting the old source-watch vault oq9gflln: what still names it, checked across team, data, press and site 
 editor 
 #correspondent-0005 
Capture stealmybitcoin.com and the StealMyBitcoin-PoC write-up into the source watch, so the two reader-question article… 
 researcher 
 #curator-0001 
sgit-ai 0.25.0: the first status on the source-watch pack clone took 18 min 23 s (the brief expects about 47 s), and a p… 
 conductor 
 #334 
For each party the editor picks: check that their /actors/ page works as a stranger's first link, and draft format B que… 
 sherpa@php.newsroom 

#### Done 120

 #dev-0004 
Articles live from their Markdown, and a page for an article or brief newer than the build 
 dev 
 #conductor-0008 
Every newsroom vault is now a pack vault, which the browser's vault UI cannot open: take the vault views off the sites 
 dev 
 #story-site-0002 
The story as days: the mock-up and the editor's decisions (front page the last 24 hours with the days strip; dates in th… 
 story-site 
 #sherpa-0002 
A page and a brief for a power user's own assistant: /sherpa/for-your-claude/ (and /sherpa/for-your-claude/brief/), so a… 
 sherpa@php.newsroom 
 #ontologist-0001 
Re-point the ontologist's scripts at the six: records/desks/ontologist/pass.py and records/desks/wikipedia/fetch.py (and… 
 ontologist 
 #conductor-0004 
Focus: CISA KEV adds the two php2shell CVEs (26 October): the pipeline on one story, researcher to correspondent 
 conductor 
 #correspondent-0007 
No edition since v0.22.33 (17:24 UTC, 26 October): releases since then wait for dev's daily chain at 06:40 London 
 dev 

### Releases
 latest 8 

 v0.22.45 2026-10-27 the first edition built in CI 
 v0.22.44 2026-10-27 the story as days (story-site, press 375c0de and site's content/days/): the front page leads with the last 24 hours and each day i… 
 v0.22.43 2026-10-27 the loops page names the evidence vault nnd3i8iw (3ytzxm3g decommissioned, the editor, 27 October 2026) 
 v0.22.42 2026-10-27 every site's gate is the press's newest: site's checks an article at its writer's push; a run's agent links to its schedule page o… 
 v0.22.41 2026-10-27 article pages are frames: each draws its article from site's content/articles/ when it opens; articles/view/ draws one newer than … 
 v0.22.40 2026-10-27 the readers' copy (glossary, plain, questions, interview, seo, billing) moves to site's content/data/; five more files are data's 
 v0.22.39 2026-10-27 every page reads the press and data from /latest/; each site's VERSION is its own, for its CI to write 
 v0.22.38 2026-10-27 the brief on the six centers of gravity, with its diagrams 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 35 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 25 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 26 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.22.45 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
