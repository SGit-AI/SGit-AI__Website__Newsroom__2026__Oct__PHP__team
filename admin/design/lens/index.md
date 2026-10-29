# Prototype E: the lens, the front page

A working prototype of a site that shapes itself to the reader in front of them: how long they have, who they are, what they want to do, and what they have seen; set once at the top right, applied on every page with no reload and no flash.

> Prototype E for review, built from the data of release v0.22.52. Not the live site. Every part of the page is listed here; the page shows the parts that fit the reader.

This site shapes itself to you. Three taps, and you can change them any time, top right. 
### How long have you got?

The page below has already changed to fit that. 
### Which is closest to you?

Last one. 
### What do you want to do?

Developing · data as of 28 October 2026, 17:15 UTC 
## Two serious security flaws in PHP, the software behind many of the world's websites

PHP is the software that WordPress and millions of other websites run on. A fix came out on 21 October 2026. Government cyber agencies have told organisations to install it now; the two US agencies add: take websites offline if you cannot. Phones and personal computers are not affected. 
 Your answer 
Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. On 26 October the US cyber agency CISA listed both flaws as known to be exploited, so update now if you run a site. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was compromised through php2shell. 
If your website runs on WordPress, Drupal, Joomla or anything else written in PHP, it is in scope: the flaw is in PHP itself, underneath your site. Updating plugins does not fix it. If someone hosts the site for you, ask them in writing whether PHP has been updated to a fixed version and restarted. If you run the server yourself, update PHP today. 
A critical flaw in software that runs many websites, fixed on 21 October. Every agency says update first; some say take systems offline if you cannot. On 26 October CISA added both flaws to its Known Exploited Vulnerabilities catalog: it holds evidence of exploitation, and names no victim. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was broken into through this flaw, though attempts are widespread and a researcher's decoy servers were broken into. Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast. 
Expect unplanned work this week: updating PHP on every system that uses it, restarting, and re-testing. Some teams may take systems offline for hours as a precaution. Anything still on PHP 8.1 or older has no ready-made fix and becomes a migration project. Ask each system owner for a patch date and a test plan. 
The documented cost so far is precaution, not breach: hours to a day of downtime for organisations that pulled sites, and engineering time to update. CISA listed both flaws as known exploited on 26 October, which raises the bar for 'we had not patched'. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was compromised through this flaw. Ask your broker now, in writing, whether a precautionary shutdown with no breach is covered. Do not use 70% of the Internet in any forecast. 
A flaw is not a breach. An unpatched, internet-facing PHP application holding personal data is a risk to record and treat; it becomes a breach to assess when there is a sign of compromise on it. No named organisation has said it was compromised through php2shell as of the last check. Ask your hosts in writing, review from 17 October, and document the assessment either way. 
The flaw is in the PHP runtime, so exposure is every internet-facing system running PHP, including vendor appliances. Review logs from 17 October (the earliest reported attempt), not from the fix. Attempts are reported at scale; no named victim is confirmed. Patch first, isolate where you cannot. 
Patch internet-facing mod_php first, then FPM, then the rest; restart every worker and rebuild every image. The fix changes how PHP behaves when memory runs out, so test under load. 7.4 to 8.1 have no release. Afterwards, invest in an inventory that answers 'where is PHP' in minutes. 
The 70% figure is a share of websites that use PHP, restated as a share of the Internet. The release was 21 October, not 22. Three parties claim the discovery; their dates do not conflict, their framing does. No agency has confirmed a successful compromise. CISA listed both flaws as known exploited on 26 October, naming no victim: exploited is not the same as a confirmed compromise. 
Safe to say: two critical flaws in PHP were fixed on 21 October; we updated or isolated our systems; we have no evidence of compromise and review continues. Do not say '70% of the Internet', 'the most severe ever' or 'exploited everywhere'. Point people to php.net and your national agency. 
Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when. 
Every application on an affected runtime is in scope, including ones with no uploads or sessions: the demonstrated paths run before application code. Add the running PHP version to the SBOM and fail the pipeline on an unfixed one. Detection belongs at the edge and on the host, not in the app. 
Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker and rebuild images. Until then: session.upload_progress.enabled=0 in php.ini or the pool, low post_max_size, fatal_error_backtraces=0 on 8.5, pm.max_requests=1 on FPM. Verify with php -v inside the running container. Keep session.upload_progress.enabled=0 after the update as well: CVE-2026-115560, published by PHP on 23 October (as Cloudflare and SOCRadar report), affects the fixed releases under a rare session setting and is fixed only in the next regular release. 
Your code is not the problem and cannot be the fix: the flaw is in the engine beneath it. ini_set, .user.ini and auto_prepend_file all run too late. Check the running version where the code runs, after the restart, and tell the platform owner today if your target is 8.1 or older. 
Two classes: an out-of-memory longjmp leaving request memory uninitialised, and worker global state pointing at freed request memory across requests. mod_php was exploited before application code; FPM for the first flaw is disputed. The fix removes longjmp for OOM. A report of an incomplete fix is open. 
A bug class seen and shelved in 2024 was turned into working exploits by three AI-assisted teams within three weeks in August 2026. The disclosure leaked 22.5 hours early. Agencies split on the hardest question, offline or not, along lines that look institutional rather than technical. 
Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. On 26 October the US cyber agency CISA listed both flaws as known to be exploited, so update now if you run a site. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was compromised through php2shell. 
A critical flaw in software that runs many websites, fixed on 21 October. Every agency says update first; some say take systems offline if you cannot. On 26 October CISA added both flaws to its Known Exploited Vulnerabilities catalog: it holds evidence of exploitation, and names no victim. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was broken into through this flaw, though attempts are widespread and a researcher's decoy servers were broken into. Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast. 
The 70% figure is a share of websites that use PHP, restated as a share of the Internet. The release was 21 October, not 22. Three parties claim the discovery; their dates do not conflict, their framing does. No agency has confirmed a successful compromise. CISA listed both flaws as known exploited on 26 October, naming no victim: exploited is not the same as a confirmed compromise. 
Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when. 
Two classes: an out-of-memory longjmp leaving request memory uninitialised, and worker global state pointing at freed request memory across requests. mod_php was exploited before application code; FPM for the first flaw is disputed. The fix removes longjmp for OOM. A report of an incomplete fix is open. 
Release v0.22.52. The site is rebuilt from the evidence vault; the board, the agents and their schedules are in the team console. 
Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. On 26 October the US cyber agency CISA listed both flaws as known to be exploited, so update now if you run a site. As of 09:43 UTC on 27 October, the latest capture in the evidence vault, no named organisation has said it was compromised through php2shell. 

 1 min+ aim: understand verify 

Is there a fix? 
Yes 
PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35 

How serious? 
Critical 
both flaws, rated 9.2 of 10 

Facts we hold 
70 
20 confirmed, 15 contested 

Agencies compared 
16 
all say install the fix 

 1 min+ aim: act understand for: decide 

### Three questions for your team

1 

#### Do we know every system that runs PHP?

Websites, internal tools, suppliers and the images we build from. 

2 

#### Is each one updated, and restarted?

Fixed in PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. An update only counts once the service restarts. 

3 

#### Who can take a system offline, and how fast?

Two US agencies say take it offline if it cannot be updated; decide now who calls it. 

 1 min+ aim: act for: act team 

### Your next three actions
 The whole playbook 

1 

#### Patch internet-facing first

mod_php, then FPM, then the rest. Restart every worker; rebuild every image; check the running version after the restart. 

2 

#### Bound the known paths

session.upload_progress off, low post_max_size, pm.max_requests on FPM. Each blocks a path; none is a fix. 

3 

#### Watch the process tree

Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing about the host. 

 1 min+ aim: act verify for: communicate 

### Before you write: three things often got wrong

- 
 contradicted The flaws are CVSS 10.0
who says it: social posts on 20 October, relayed by a vendor and a news site 
- 
 disputed Remote code execution is confirmed on PHP-FPM
who says it: PHP Foundation blog; GHSA-6wmf for the session path 
- 
 unverified The 8.5.12 fix may be incomplete, or there is a third, different bug
who says it: Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez 

 1 min+ aim: understand for: understand 

### Does it touch you?

#### What happened?

Two flaws were found in PHP itself, the engine that runs WordPress, Drupal, Wikipedia's software and millions of other sites. Either lets anyone on the internet, with no password, run commands on the web server. The fix came out on 21 October 2026. 

#### Does it affect me?

Not your phone or laptop: the flaw is on web servers. It affects organisations that run websites on PHP, and their visitors only indirectly. If you run a website, the question is whether PHP on its server has been updated and restarted. 

#### Has anyone been hacked?

Attackers have been trying: Cloudflare reports millions of attempts and Amazon a honeypot hit four days before disclosure. But as of 17:15 UTC on 28 October no named organisation has said it was broken into through this flaw. CISA listed both flaws as exploited on 26 October, which means it has evidence they are being exploited, but it names no victim. Two companies in Japan are named in reports of a break-in without saying how it happened: GMO is investigating one, and an Italian site reports that Square Enix confirmed unauthorised access to its systems. A Czech university says it stopped an attack. A researcher's decoy servers, left on an unpatched version on purpose, were broken into on 24 to 26 October: proof the attack works, not a victim. 

 1 min+ aim: understand verify for: study 

### The open questions

- 
Whether any website was actually broken into before it installed the fix. 
- 
Whether the fix is complete. A report on 21 October suggested it may not be; the PHP security team replied on the mailing list on 22 October, and this site will settle the question once that reply is saved here. Separately, on 23 October PHP published an advisory for another flaw, CVE-2026-115560, which affects fully patched releases and needs a rare session setting (reported by Cloudflare, SOCRadar and The Hacker News). 
- 
Who leaked the news on 20 October, and where. 
- 
How many websites went offline, and why. The reports this site holds range from a single site to a whole government's platform; a community tracker lists about fifty sites that went dark and came back. Nobody has counted them all. 
- 
Where the 70% figure comes from. None of the pages that use it says how it was measured. 

 1 min+ aim: verify 
### How sure are we?

- 20 confirmed 
- 35 reported 
- 9 disputed 
- 2 contradicted 
- 4 unverified 
Every fact carries one of five words for how far it can be trusted. 

 5 min+ aim: understand act 

### Right now

- 
A fix has been available since 21 October. Organisations that run websites on PHP are installing it.
 php.net 
- 
Every government cyber agency says: install the fix now. If you cannot, the US agencies say take the website offline; the UK puts that after temporary mitigations, and several European agencies say cut it off from the public internet first.
 CISA NCSC UK CERT-EU 
- 
Attackers are trying to use the flaws, in large numbers: millions of attempts by one internet security company's count. On 26 October CISA, the US cyber agency, added both flaws to its list of flaws known to be exploited: it has evidence of exploitation, and names no victim. As of 17:15 UTC on 28 October, no named organisation has said it was broken into through this flaw. Two security companies withdrew what they had said: Sophos a claimed successful break-in, and Palo Alto Networks' Unit 42, on 25 October, a statement tying an attack on a European government agency to the flaws. US banks and the large crypto platforms report none.
 Matthew Prince, Cloudflare CEO on… CISA CISA 
- 
The advice is moving from 'install the fix' to 'and check whether you were already broken into'. Singapore's and Luxembourg's authorities now say so.
 CNA Paperjam 
- 
Some organisations took websites offline as a precaution: the Dutch government took its cyber agency's own site offline, and Dutch press reported the DigiD login down too. Almost all of them are back.
 Rijksoverheid / NCSC-NL TPO.nl PHPocalypse Tracker 

 5 min+ aim: understand act 

### The latest

- 
 27 Oct CISA adds a different flaw to the same catalog: CVE-2026-111497, in Google's Brotli decoder (due date for US federal civilian agencies 10 November; no victim named). It is not php2shell, but PHP's official Windows builds bundle Brotli: The Hacker News reports new Windows builds released on 26 October (8.5.12-1, 8.4.27-1, 8.3.36-1, 8.2.35-1) and quotes the PHP Foundation: the flaw can be reached there through the cURL extension when automatic response decompression is turned on, which is off by default in cURL but which applications and HTTP client libraries can turn on. 
- 
 26 Oct, 22:24 UTC CISA adds both flaws to its Known Exploited Vulnerabilities catalog (the version released at 22:24 UTC on 26 October): it has evidence they are exploited, names no victim, and gives US federal civilian agencies until 29 October to fix them. 
- 
 23 Oct, 10:03 UTC Die Presse: as of 12:03 Vienna time (10:03 UTC) on 23 October no successful attack via the PHP flaws was known in Austria. 
- 
 23 Oct, 09:16 UTC Japan's RainForest reports that its honeypots recorded 21 php2shell-related requests from 14 different addresses: attempts, not break-ins. 
- 
 23 Oct, 07:58 UTC IT Social: the update closes the flaw, but obliges a hunt for possible compromises; the published figures count attempts, not intrusions. 

 5 min+ aim: act verify understand 

### The spectrum
 every agency, by what it says to do with a system you cannot patch 

 5 No offline advice 
 EU ENISA CSIRTs Network AU ASD's ACSC NZ NCSC NL NCSC-NL JP JPCERT/CC 

 3 Consider it, or after other steps 
 UK NCSC IT ACN / CSIRT Italia CH BACS 

 1 Restrict access 
 LV CERT.LV 

 3 Isolate from the internet 
 EU CERT-EU FR CERT-FR CA CCCS 

 2 Take it offline 
 US NSA Cybersecurity US CISA 
Not readable from this capture environment: CCN-CERT, CNCS. 

 5 min+ aim: understand verify for: understand decide communicate act team 

### What nobody knows yet

- 
Whether any website was actually broken into before it installed the fix. 
- 
Whether the fix is complete. A report on 21 October suggested it may not be; the PHP security team replied on the mailing list on 22 October, and this site will settle the question once that reply is saved here. Separately, on 23 October PHP published an advisory for another flaw, CVE-2026-115560, which affects fully patched releases and needs a rare session setting (reported by Cloudflare, SOCRadar and The Hacker News). 
- 
Who leaked the news on 20 October, and where. 
- 
How many websites went offline, and why. The reports this site holds range from a single site to a whole government's platform; a community tracker lists about fifty sites that went dark and came back. Nobody has counted them all. 
- 
Where the 70% figure comes from. None of the pages that use it says how it was measured. 

 15 min+ aim: understand verify 

### The core facts

- 
 confirmed There are two flaws. Both are in PHP itself, underneath every website that uses it, and both are rated critical: 9.2 out of 10. 
- 
 confirmed Someone anywhere on the internet, with no password, can use them against a website that has not installed the fix, and make its server run their own commands. Researchers proved this on the most traditional way of running PHP; for other setups it is likely but less certain. 
- 
 confirmed The fix is in PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35, released on 21 October 2026. Websites on PHP 8.1 or older have no ready-made fix. 
- 
 reported The weak spot was first noticed in 2024 and left alone, because nobody could show it was dangerous. In August 2026, three research teams using AI tools showed that it was, and told the PHP project. 
- 
 confirmed The plan was to announce the fix on 22 October. Word leaked out on 20 October, so it was released a day early. 
- 
 reported Attackers are trying, in large numbers: one internet security company reports millions of attempts, and Amazon reports a decoy server hit four days before the announcement. No named organisation has said it was broken into through these flaws, as of 17:15 UTC on 28 October. The US government's official list of flaws known to be used in attacks added both on 26 October, naming no victim. 
- 
 confirmed Every agency says install the fix. They disagree on what to do if you cannot: the US says take the website offline, the UK lists that as a last resort, several European agencies say cut it off from the public internet, and some say nothing about it. 
- 
 confirmed The headline '70% of the Internet' is not what it sounds like. It is roughly the share of websites whose server-side language is known that use PHP, which is what the same company's own article says; nobody has measured how many are actually at risk. 

 15 min+ aim: understand 

### How it unfolded

- 
 2024 An audit spots the out-of-memory weakness. Nobody can show it is exploitable, so it is left. 
- 
 Aug 2026 Three teams using AI turn it into working attacks within three weeks and report them to PHP. 
- 
 20 Oct The secret leaks: the CVE numbers circulate two days early, with a wrong severity score. 
- 
 21 Oct PHP releases the fix a day ahead of plan. Firewall vendors already have rules live. 
- 
 22 Oct Agencies warn: update, or take systems offline. Sites go dark as a precaution. 

 15 min+ aim: verify 

### Contested
 disputed, contradicted, unverified 
- 
 contradicted The flaws are CVSS 10.0
who says it: social posts on 20 October, relayed by a vendor and a news site 
- 
 disputed Remote code execution is confirmed on PHP-FPM
who says it: PHP Foundation blog; GHSA-6wmf for the session path 
- 
 unverified The 8.5.12 fix may be incomplete, or there is a third, different bug
who says it: Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez 
- 
 disputed All PHP versions from 5 onwards are affected by at least one of the flaws
who says it: NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) 
- 
 disputed A web application firewall may provide some protection until systems are patched
who says it: CISA 
- 
 unverified 70% of the Internet is affected
who says it: Wiz (headline, X post); the BBC, which reports it as Wiz's 'roughly 70%' 
- 
 disputed Frontier AI found the flaw ahead of attackers, giving defenders time to prepare
who says it: OpenAI 
- 
 disputed Chainguard unilaterally broke the embargo on 21 October at 07:41 UTC by publishing built images containing the fix
who says it: PHP Foundation; Chainguard's CEO accepts the time and denies leaking 
- 
 contradicted The flaws were disclosed on 22 October 2026
who says it: Not stated by the BBC. A framing found in coverage and in two sources that date the releas 
- 
 disputed The pre-announcement was published at 19:30 UTC on 20 October
who says it: PHP Foundation 

 All+ 

### Agency by agency

#### NSA Cybersecurity
 US 
 Take offline 
 If an immediate update is not feasible, it is recommend[ed] that organizations take the system offline until it can be fully mitigated. 

 NSA Cyber on X NSA NSA Cyber on X 

#### CISA
 US 
 Take offline 
 Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be patched or updated. 

 CISA CISA CISA 

#### NCSC
 UK 
 After mitigations 
 If you are unable to apply the temporary mitigations, or applying them would take too long, you should consider taking the system offline until it can be fully mitigated. 

 NCSC UK 

#### CERT-EU
 EU institutions 
 Isolate 
 Where that is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix is applied and verified. 

 CERT-EU 

#### ENISA CSIRTs Network
 EU 
 No offline advice 

An index of about 30 national advisories, work in progress: a truncated CVE in the heading and a Dutch 'en'. 

 ENISA CNW 

#### CERT-FR (ANSSI)
 FR 
 Isolate first 
 Le CERT-FR recommande d'isoler les équipements affectés puis de procéder à la migration vers une version maintenue... 

 CERT-FR 

#### CCCS
 CA 
 Isolate 
 Where immediate remediation is not feasible, organisations should consider isolating internet-facing applications from public networks until a fix can be applied. 

 CCCS CCCS 

#### ASD's ACSC
 AU 
 No offline advice 

No take-offline or isolation advice. Parts of the body are still pre-patch text. Corrected 27 October 2026, PROJECT-001: the BBC said only that Australia's counterparts ' 

 ACSC ACSC 

#### NCSC
 NZ 
 No offline advice 

The only agency to say active exploitation is reported. It does not say whose reports. Time converted from NZDT by this site. 

 NCSC New Zealand NCSC New Zealand 

#### NCSC-NL
 NL 
 No offline advice 

Runs the public php2shell GitHub repository with the software inventory the UK NCSC cites, cPanel detection and mitigation scripts, and an SPDX/VEX source list. 

 NCSC-NL NCSC-NL NCSC-NL 

#### ACN / CSIRT Italia
 IT 
 Consider 
 Qualora non fosse possibile applicare tempestivamente gli aggiornamenti di sicurezza, si raccomanda di valutare di porre offline i siti e i servizi web che utilizzano versioni vulnerabili di PHP, sosp 

 ACN / CSIRT Italia 

#### BACS (NCSC)
 CH 
 Consider 
 Check, particularly for critical applications, whether a temporary disconnection from the internet or taking the system offline is necessary. 

 BACS Swiss BACS 

#### CERT.LV
 LV 
 Restrict from abroad 
 Systems that cannot be updated must have internet access restricted, with no public availability until the risk is removed. 

 CERT.LV 

#### JPCERT/CC
 JP 
 No offline advice 

Translations are this site's. 

 JPCERT/CC JPCERT/CC 

#### CCN-CERT
 ES 
 Could not be read 

The title ('actualización inmediata') points to immediate-update advice. The block is recorded in the vault. 

 CCN-CERT 

#### CNCS
 PT 
 Could not be read 

The block is recorded in the vault. 

 CNCS 

 All+ 

### Everything else we hold

 Every claim (70) Every source (675) The timeline The numbers The code How this site knows 

That is the page for the time you gave it. How this prototype works (for the editor and dev) 
- Every part of every page is built, always. Each part says which settings show it: a time tier, an aim, a kind of reader. 
- A tiny script in the page head (no defer) reads the settings and puts them on the page before anything is drawn, so a page never flashes the wrong version, on the first page or the tenth. 
- The stylesheet shows, hides and orders the parts from those settings. Changing a setting changes one attribute; the browser re-lays the page in the same frame, and animates it where it can (View Transitions). 
- The counts on each option (“6 parts, about 3 min”) are worked out from the parts on this page, so the reader sees what a choice will do before making it. 
- A page that does not answer to a setting says so in the control, and keeps the setting for the next page. A page for some readers only says who it is for, and lets anyone read it anyway. 
- “Got it” marks a part as seen; Fade or Hide takes it out of the way on every page, until it changes.

---
site v0.22.52 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/lens/index.html
