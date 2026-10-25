# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.7. Not the live site.

PHP Team console Console Overview Board 216 Agents 19 Releases 191 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 25 October 2026, 09:35 UTC 

Release 
v0.22.7 
191 releases since 22 Oct 

Open on the board 
216 
108 done, 5 waiting 

Pages built 
1059 
every one with a markdown twin 

Sources in the vault 
418 
403 captured 

### The board
 newest first in each lane 

#### Open 216

 #329 
The line's prototype pages under /admin/design/line/ link to sources one level too shallow (../../../sources/… from admi… 
 story-site 
 #328 
The six new repositories have not deployed: set each one's Pages source to 'Deploy from a branch: dev, / (root)' (or a d… 
 editor 
 #327 
The line's next steps on the live pages: the reading path ('Next: your briefing') as one of its actions, dated views (on… 
 claude-story-site 
 #326 
sg-meter v1.3.1 edited in place: what a reader has paid for is keyed by the real page (window.P2S_REAL_PATH), not the ad… 
 dev 
 #325 
The gate and the router: exempt /404.html and the view cards (<page>/as/<reader>/) from the sitemap, llms.txt and orphan… 
 security 
 #323 
One repository into six, step 1: the one big session (press, data, team, refs, updates, site; every old address answerin… 
 dev@php.newsroom 
 #322 
One repository into six, step 0: create the six repositories (…__PHP__press, __data, __refs, __updates, __team, __site),… 
 editor 

#### Waiting 5

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
 #013 
Hand the telemetry vault key to the editor, sealed to his pki.sgit.ai key 
 dev 

#### Done 108

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
 #309 
The briefs page is a list of titles, newest first, and every brief has its own page and link (admin/briefs/<the file's n… 
 claude-story-site v0.20.0 
 #305 
Article: URL paths, personas in the address, and a single-page site, written before the work (a link that names its pers… 
 claude-story-site v0.19.0 

### Releases
 latest 8 

 v0.22.7 2026-10-25 the four reports on the split link each other, the proposal and the plan 
 v0.22.6 2026-10-25 one repository into six, in four reports on the briefs page: the first day in numbers, one source for every file (the design), the… 
 v0.22.5 2026-10-25 one repository into six: one source for every file, recorded (the plan's Progress, REALITY, the board): press v1.0.4 serves the as… 
 v0.22.4 2026-10-25 the control room loads under a view address (/team/control/as/executive/ fetched team/control/data/control.json): control.js resol… 
 v0.22.3 2026-10-25 assets/route.js sends every data/ request on the split sites to the data API, which now publishes every file the pages' scripts fe… 
 v0.22.2 2026-10-25 one resolver for every URL a script builds (assets/route.js, loaded first on every page; boot.js, the Ask pane, the phone app and … 
 v0.22.1 2026-10-25 pass one of the split, recorded: the press (v1.0.0) cuts this site's built pages at d9af616ffd0b into four sites (site 230 pages, … 
 v0.22.0 2026-10-25 the line is live on every page in place of the two dials, and the router: /agencies/as/security/ opens the agencies for Security, … 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 33 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 21 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 17 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 8

---
site v0.22.7 · https://php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
