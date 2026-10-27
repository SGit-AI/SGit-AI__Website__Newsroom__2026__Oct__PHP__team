# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.39. Not the live site.

PHP Team console Console Overview Board 236 Agents 19 Releases 223 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 26 October 2026, 17:09 UTC 

Release 
v0.22.39 
223 releases since 22 Oct 

Open on the board 
236 
115 done, 10 waiting 

Pages built 
1228 
every one with a markdown twin 

Sources in the vault 
561 
546 captured 

### The board
 newest first in each lane 

#### Open 236

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
 #researcher-0001 
CISA added CVE-2026-109618 and CVE-2026-109619 to the KEV catalog on 26 October 2026 (due 29 October): the first KEV lis… 
 journalist 
 #ontologist-0001 
Re-point the ontologist's scripts at the six: records/desks/ontologist/pass.py and records/desks/wikipedia/fetch.py (and… 
 ontologist 
 #observability-0002 
SG/Send: the append service caches a vault's lane configuration per server instance and never refreshes it, so after `co… 
 conductor 

#### Waiting 10

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
 #180 
The Sherpa drains the lanes (the editor, 24 October 2026): a go for its schedule (data/schedule/sherpa.json, proposed: e… 
 editor 

#### Done 115

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
 #328 
The six new repositories have not deployed: set each one's Pages source to 'Deploy from a branch: dev, / (root)' (or a d… 
 editor 

### Releases
 latest 8 

 v0.22.39 2026-10-27 every page reads the press and data from /latest/; each site's VERSION is its own, for its CI to write 
 v0.22.38 2026-10-27 the brief on the six centers of gravity, with its diagrams 
 v0.22.37 2026-10-27 the briefs read live; telemetry capped at 40 events a tab, with five lanes 
 v0.22.36 2026-10-26 the rest of the team site reads its records when it opens: member status and rounds, tasks, status, runs 
 v0.22.35 2026-10-26 the schedule pages and the vault register read the team's records when they open 
 v0.22.34 2026-10-26 the board reads its rows when it opens (phase 2, the first page) 
 v0.22.33 2026-10-26 the lane drains in v2 and telemetry from the site's own hosts (boards sherpa-0001, 330) 
 v0.22.32 2026-10-26 the cutover: the main site at php.oct.2026.newsroom.sgit.ai, its robots open to search engines, its sitemap at its own address; st… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 33 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 24 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 24 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.22.39 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
