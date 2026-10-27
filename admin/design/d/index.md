# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.42. Not the live site.

PHP Team console Console Overview Board 239 Agents 19 Releases 226 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 26 October 2026, 17:09 UTC 

Release 
v0.22.42 
226 releases since 22 Oct 

Open on the board 
239 
116 done, 11 waiting 

Pages built 
1231 
every one with a markdown twin 

Sources in the vault 
561 
546 captured 

### The board
 newest first in each lane 

#### Open 239

 #story-site-0003 
Build the story as days: the day file's shape, the day renderer and the front page as the last 24 hours with the strip, … 
 story-site 
 #story-site-0001 
Review of the line and the router on the live site: the router is done; the line promises a shaped page that the live pa… 
 story-site 
 #dev-0003 
Tag ruleset on the six repositories, so a published version can never move or vanish (CI owns the version: the editor's … 
 editor 
 #sherpa-0002 
A page and a brief for a power user's own assistant: /sherpa/for-your-claude/ (and /sherpa/for-your-claude/brief/), so a… 
 sherpa@php.newsroom 
 #conductor-0006 
Build /breaking/ from content/breaking/*.md (the list, a page per item), and files/breaking.json in the data catalogue 
 dev 
 #conductor-0005 
A section for breaking news on the main site: /breaking/, items BREAKING-001, 002, … each with its own page 
 story-site 
 #security-0001 
SA-2026-043: retire the round's write token: the editor deletes and revokes ROUND_TOKEN; dev removes .github/workflows/r… 
 dev 

#### Waiting 11

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
 #331 
Interviews and outreach: choose the first wave (the brief proposes Weird Gloop, the PHP security team, the three discove… 
 editor 
 #307 
Ten scheduled tasks still carry their long prompts, which only their own sessions can change: paste the card's prompt (s… 
 editor 

#### Done 116

 #story-site-0002 
The story as days: the mock-up and the editor's decisions (front page the last 24 hours with the days strip; dates in th… 
 story-site 
 #conductor-0004 
Focus: CISA KEV adds the two php2shell CVEs (26 October): the pipeline on one story, researcher to correspondent 
 conductor 
 #correspondent-0007 
No edition since v0.22.33 (17:24 UTC, 26 October): releases since then wait for dev's daily chain at 06:40 London 
 dev 
 #sherpa-0001 
Three of the press's lane drains still use v1 paths and break or misfile in v2: collaborators (feedback and enrolments),… 
 dev 
 #correspondent-0003 
The chain deletes records/tools/schedule.py from team at every second import (editions v0.22.28 and v0.22.32): WAKE.md's… 
 dev 
 #dev-0001 
Step A of the split is in place (26 October): the records are written in team (records/), the data in data (files/), the… 
 dev@php.newsroom 
 #330 
Telemetry from agents' local test servers: assets/telemetry.js sends from any host, so 439 of the telemetry vault's 2,08… 
 dev@php.newsroom 

### Releases
 latest 8 

 v0.22.42 2026-10-27 every site's gate is the press's newest: site's checks an article at its writer's push; a run's agent links to its schedule page o… 
 v0.22.41 2026-10-27 article pages are frames: each draws its article from site's content/articles/ when it opens; articles/view/ draws one newer than … 
 v0.22.40 2026-10-27 the readers' copy (glossary, plain, questions, interview, seo, billing) moves to site's content/data/; five more files are data's 
 v0.22.39 2026-10-27 every page reads the press and data from /latest/; each site's VERSION is its own, for its CI to write 
 v0.22.38 2026-10-27 the brief on the six centers of gravity, with its diagrams 
 v0.22.37 2026-10-27 the briefs read live; telemetry capped at 40 events a tab, with five lanes 
 v0.22.36 2026-10-26 the rest of the team site reads its records when it opens: member status and rounds, tasks, status, runs 
 v0.22.35 2026-10-26 the schedule pages and the vault register read the team's records when they open 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 34 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 24 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 24 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.22.42 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
