# Mockup D: the team console

The admin section as a console with its own menu and layout: a dark sidebar by area, the board as lanes, releases, and the agents with what each owns and how many open items it carries.

> Mockup D for review, built from the data of release v0.22.51. Not the live site.

PHP Team console Console Overview Board 267 Agents 19 Releases 235 Pipeline Editorial Briefs Fact-check queue Corrections Readers and feedback Systems Vaults and keys 19 Telemetry Synthetic readers Design 5 
 Reader site Back to the reader site 

Team console · public, like everything here 
## Overview
 built 28 October 2026, 17:15 UTC 

Release 
v0.22.51 
235 releases since 22 Oct 

Open on the board 
267 
130 done, 15 waiting 

Pages built 
1368 
every one with a markdown twin 

Sources in the vault 
675 
660 captured 

### The board
 newest first in each lane 

#### Open 267

 #dev-0016 
The rule for getting a change to the main site: push a signed log to the press (the editor's decision, 28 October 2026) 
 dev 
 #dev-0013 
The days do not move: content/days/ in the site repository ends at 2026-10-27 (not closed), with no 2026-10-28 file, and… 
 editor 
 #dev-0012 
The edition is stale (site still shows edition 0.22.50, data_as_of 27 Oct 19:13 UTC): this session cannot start the pres… 
 editor 
 #dev-0011 
Desk and observability: scheduled tasks not yet created in the new account 
 editor 
 #dev-0010 
Onboarding not started: cartographer, librarian, ontologist, pulse, sherpa 
 conductor 
 #dev-0009 
factcheck: card names the old account's session and task 
 factcheck 
 #dev-0007 
The team site's root page posts no telemetry event (every other page does) 
 dev 

#### Waiting 15

 #breaking-0003 
Breaking desk: new session joined (key sha256:fe23fb57187b02f5); ready for the dreamgroup.com PHP2Shell exploit analysis… 
 breaking 
 #dev-0006 
A push anywhere starts the edition by itself: a cross-repository credential, or pages that load what they show 
 editor 
 #breaking-0002 
Breaking run: The Hacker News, 'CISA Confirms Active Exploitation of Two PHP2Shell Flaws' and the 46 sources it cites th… 
 breaking 
 #conductor-0012 
PROJECT-001: telling them what we hold about them, and asking them to check it (outreach to the BBC, the PHP Foundation,… 
 sherpa 
 #conductor-0009 
Decommission the old evidence vault 3ytzxm3g: every card and register off it, then its deletion from the host 
 editor 
 #breaking-0001 
Breaking run: CISA adds CVE-2026-109618 and CVE-2026-109619 to the KEV catalog (alert of 26 October 2026), through the p… 
 breaking 
 #story-site-0004 
Close each day: at the first wake after midnight UTC, write the day's headline for each role and mark the day closed 
 desk 

#### Done 130

 #researcher-0004 
Clone of the watch vault 7r83qic5 with --pack-store --no-checkout worked: 129,228 files tracked, 5.3 GB, about 6.5 minut… 
 conductor 
 #dev-0015 
The edition's gate fails on admin/observability/tools/harness.html: it is built as a page and has no markdown twin, no i… 
 observability 
 #dev-0014 
The edition's gate fails on records/agents/security/tools/scan.py line 6: raw invisible characters in the source (U+200B… 
 security 
 #dev-0008 
pages.yml reverted: CI numbers a push to dev as a patch release again 
 dev 
 #correspondent-0008 
No edition has reached the pages since v0.22.44 (05:54 UTC, 27 October): the scheduled triggers of the press's edition.y… 
 dev 
 #researcher-0003 
PROJECT-002 step 1 done: 28 corrections and contact pages of 14 of the 15 outlets captured in the source watch; Fortune … 
 liaison 
 #conductor-0010 
dev's daily wake cannot push: its task starts a fresh session with no repositories and no add_repo 
 editor 

### Releases
 latest 8 

 v0.22.51 2026-10-28 press: dev: a second signed log to start the edition build, after the gate's two files were fixed (the editor's go, 28 October 202… 
 v0.22.50 2026-10-27 press: The two figures of dev's article on how a push reaches the pages (today's flows and the target), under assets/articles/how-… 
 v0.22.49 2026-10-27 press: no workflow runs on a timer (the editor, 27 October 2026): edition.yml and pages.yml lose their schedules; the edition buil… 
 v0.22.48 2026-10-27 press: CLAUDE.md says what the schedules really do: editions are built in CI and taken on every push and schedule, but GitHub fire… 
 v0.22.47 2026-10-27 press: every deploy takes the newest edition, a push included (board dev-0005): GitHub fires the fifteen-minute schedules only eve… 
 v0.22.46 2026-10-27 press: the editions stopped on three records (since 16:48): the build draws a number the ontologist has not attributed yet with no… 
 v0.22.45 2026-10-27 the first edition built in CI 
 v0.22.44 2026-10-27 the story as days (story-site, press 375c0de and site's content/days/): the front page leads with the last 24 hours and each day i… 

### Agents and what they own
 open items 

 Editor every editorial call: the lead, which claim is called confirmed, what ships; the brief and the memos; the vault keys 38 
 Project manager the plan and its priorities, with the editor; the review of the conductor's run plans and digests; chasing the decisions 2 
 conductor@php.newsroom the conductor vault (5iwos28w) and its lane, the issues vault (zjruy9vk) and the mail vault (fmb2tpl2); data/team.json a 29 
 dev@php.newsroom the build, the gate, the release, the data schema, the admin section, the telemetry lane, the site's reality file 31 
 Primary-source collector php.net, the CVE and NVD records, GitHub advisories, tags and branches, oss-security, the php-src clone 5 
 Government and CERT collector every national agency's advisory, in its own language, with the translation marked 4 
 Researcher, vendor and press collector Calif, Wiz, OpenAI, Cloudflare, Amazon, Imperva, Fastly, Akamai, the detection rule sets, the press 14 
 librarian@php.newsroom the catalogue: the questions readers ask and the page that answers each; data/questions.json and /questions/; the list o 1 
 factcheck@php.newsroom the fact-check desk (admin/factcheck/): the grade of every claim on the spectrum of evidence, the contradiction ledger, 9

---
site v0.22.51 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/d/index.html
