# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.28. Not the live site.

PHP Team console Console Overview Board 224 Agents 19 Releases 212 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 26 October 2026, 09:40 UTC 

Release 
v0.22.28 
212 releases since 22 Oct 

Open on the board 
224 
110 done, 8 waiting 

Pages built 
1156 
every one with a markdown twin 

Sources in the vault 
507 
492 captured 

### The board
 newest first in each lane 

#### Open 224

 #correspondent-0002 
plain.json and questions.json have no home after the split: the front page's 'Right now' and 'Has anyone been hacked?' a… 
 dev 
 #conductor-0002 
Every agent that runs sgit upgrades to sgit-ai 0.25.0 (the large-vault fix) and names the version and its timings in its… 
 conductor 
 #conductor-0001 
Every agent's release is live within minutes, in its own area, as in v1 (the editor, 26 October): today the pages are re… 
 dev 
 #correspondent-0001 
The press's .gitignore ignores build/, so v1's build code (step A) is listed in sources.json but never committed to the … 
 dev 
 #336 
v1 is closing: no new work starts here (README, REALITY, 25 October); step A flips the direction (team's records, data's… 
 dev@php.newsroom 
 #335 
The split, for every agent: four decisions before the schedule resumes (the go for step A: records to team and data to d… 
 editor 
 #333 
An /interviews/ section: one page per interview showing its format (A to D), who asked, whether an agent took part, the … 
 dev@php.newsroom 

#### Waiting 8

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
 #099 
Seal the conductor and collaborators lanes' secrets (enum keys, member tokens, key-pair passphrases) to the root: the se… 
 conductor 
 #030 
The story graph: every node a link, parties as nodes, typed edges (newsroom review, change 10; board 008 holds the fract… 
 ontologist 

#### Done 110

 #dev-0001 
Step A of the split is in place (26 October): the records are written in team (records/), the data in data (files/), the… 
 dev@php.newsroom 
 #328 
The six new repositories have not deployed: set each one's Pages source to 'Deploy from a branch: dev, / (root)' (or a d… 
 editor 
 #324 
The line is live on every page, and the router: /agencies/as/security/ opens the agencies for Security; every page shows… 
 claude-story-site v0.22.0 
 #321 
The briefs page sorts by the time each brief was published, newest first, and shows the time (UTC) on every row and on e… 
 claude-story-site v0.21.6 
 #316 
Scheduled tasks that start a fresh session can start with no repository: the ontologist's old task (trig_01BqfsPKp2Rj5Fs… 
 editor 
 #312 
Proposal: one repository into six (kit, data, refs, updates, site, team), meeting through versions by URL, not submodule… 
 editor 
 #310 
The admin and team pages use the whole width of the screen; the reader pages stay at 1,440px 
 claude-story-site v0.20.0 

### Releases
 latest 8 

 v0.22.28 2026-10-26 the morning's releases on the pages: the journalist's 81 verdicts, the researcher's source watch, the correspondent's ledger, fact… 
 v0.22.27 2026-10-26 the morning's releases on the pages: the researcher's source watch, the correspondent's offline ledger, fact-check's run 8, the cu… 
 v0.22.26 2026-10-26 dev's debrief of the night on the pages; whatever the agents wrote since the last round 
 v0.22.25 2026-10-26 the journalist's verdicts and the researcher's source watch (data v0.1.16, v0.1.17), the curator's evidence, the fact-check's corr… 
 v0.22.24 2026-10-26 the six's instructions and the agents' brief at step B; the curator's refreshed evidence (454 sources) and the fact-check's correc… 
 v0.22.23 2026-10-26 step B of the split: the pages are built in the chain's own box from the six repositories' sources; nothing depends on v1's reposi… 
 v0.22.22 2026-10-26 the journalist's and the correspondent's records, written in team; story-site's review of the split as served, filed on the team s… 
 v0.22.21 2026-10-26 researcher: repositories field in the card (v1 today; team, data and press later), the round-1 debrief with its status, and the pr… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 33 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 22 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 20 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.22.28 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
