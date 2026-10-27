# Prototype F: the line, the front page

The front page of the line prototype: one band under the masthead that says one thing to the persona in front of it, and the page under it ordered for that role, at the depth they asked for.

> Prototype F for review, built from the data of release v0.22.44. Not the live site. Every part of the page is listed here; a reader sees the parts written for their role.

Developing · data as of 27 October 2026, 00:45 UTC 
## Two serious security flaws in PHP, the software behind many of the world's websites

A fix came out on 21 October. Whoever runs a website needs to install it, and restart it. 
Fixed in PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. An update only counts once the service restarts. 
Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker, rebuild images, verify with php -v inside the running container. 
Your answer 
A critical flaw in software that runs many websites, fixed on 21 October. Every agency says update first; some say take systems offline if you cannot. As of 14:42 UTC on 26 October, the latest capture in the evidence vault, no named organisation has said it was broken into through this flaw, though attempts are widespread. Your questions are: do we know every system running PHP, are they updated and restarted, and who can pull a system offline and how fast. 
Two serious holes were found in PHP, software that runs on the servers behind a large share of websites. They were fixed on 21 October 2026. Your phone and laptop are not the target: websites are, and it is the job of whoever runs them to update. Some sites were taken offline as a precaution. As of 14:42 UTC on 26 October, the latest capture in the evidence vault, no named organisation has said it was compromised through php2shell. 
Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when. 
Target 8.5.12, 8.4.27, 8.3.36 or 8.2.35; restart every worker and rebuild images. Until then: session.upload_progress.enabled=0 in php.ini or the pool, low post_max_size, fatal_error_backtraces=0 on 8.5, pm.max_requests=1 on FPM. Verify with php -v inside the running container. Keep session.upload_progress.enabled=0 after the update as well: CVE-2026-115560, published by PHP on 23 October (as Cloudflare and SOCRadar report), affects the fixed releases under a rare session setting and is fixed only in the next regular release. 
The 70% figure is a share of websites that use PHP, restated as a share of the Internet. The release was 21 October, not 22. Three parties claim the discovery; their dates do not conflict, their framing does. No agency has confirmed a successful compromise. CISA listed both flaws as known exploited on 26 October, naming no victim: exploited is not the same as a confirmed compromise. 
Two classes: an out-of-memory longjmp leaving request memory uninitialised, and worker global state pointing at freed request memory across requests. mod_php was exploited before application code; FPM for the first flaw is disputed. The fix removes longjmp for OOM. A report of an incomplete fix is open. 
The whole site, unfiltered: every part of the page, in the usual order. 

Is there a fix? 
Yes 
since 21 October 

How serious? 
Critical 
both flaws, 9.2 of 10 

Anyone broken into? 
None named 
millions of attempts 

Government advice 
Update 
all 16 agencies agree 

### Three questions for your team

1 

#### Do we know every system that runs PHP?

Websites, internal tools, suppliers, and the images we build from. 

2 

#### Is each one updated, and restarted?

Fixed in PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. An update only counts once the service restarts. 

3 

#### Who can take a system offline, and how fast?

Two US agencies say take it offline if it cannot be updated. Decide now who makes that call. 

### Does it touch you?

Two flaws were found in PHP itself, the engine that runs WordPress, Drupal, Wikipedia's software and millions of other sites. Either lets anyone on the internet, with no password, run commands on the 
Not your phone or laptop: the flaw is on web servers. It affects organisations that run websites on PHP, and their visitors only indirectly. If you run a website, the question is whether PHP on its se 

### What to do

A fix has been available since 21 October. Organisations that run websites on PHP are installing it. 
Every government cyber agency says: install the fix now. If you cannot, the US agencies say take the website offline; the UK puts that after temporary mitigations, and several European agencies say cu 
Attackers are trying to use the flaws, in large numbers: millions of attempts by one internet security company's count. On 26 October CISA, the US cyber agency, added both flaws to its list of flaws k 

### Your next three actions

1 

#### Patch internet-facing first.

mod_php, then FPM, then the rest. Restart every worker; rebuild every image. 

2 

#### Bound the known paths.

session.upload_progress off, low post_max_size, pm.max_requests on FPM. Each blocks a path; none is a fix. 

3 

#### Watch the process tree.

Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing about the host. 

### Right now

A fix has been available since 21 October. Organisations that run websites on PHP are installing it. 
Every government cyber agency says: install the fix now. If you cannot, the US agencies say take the website offline; the UK puts that after temporary mitigations, and several European agencies say cu 
Attackers are trying to use the flaws, in large numbers: millions of attempts by one internet security company's count. On 26 October CISA, the US cyber agency, added both flaws to its list of flaws k 

### What nobody knows yet

Whether any website was actually broken into before it installed the fix. 
Whether the fix is complete. A report on 21 October suggested it may not be; the PHP security team replied on the mailing list on 22 October, and this site will settle the question once that reply is 
Who leaked the news on 20 October, and where. 

### Attack signals

 2026-10-17 One exploit attempt against a MadPot honeypot from a commercial anonymisation network, four days before disclosure; 'it remains unclear how the actor 
 2026-10-17 One exploit attempt against a MadPot honeypot from an IP on a commercial anonymisation network, geolocated to Australia, four days before disclosure. 
 2026-10-20 to 21 'We observed attack traffic targeting our customers' after the leak, and attackers 'mutating the attack payload to try to bypass our protections'. No 

### The advice, now

Every government cyber agency says: install the fix now. If you cannot, the US agencies say take the website offline; the UK puts that after temporary mitigations, and several Euro 
Attackers are trying to use the flaws, in large numbers: millions of attempts by one internet security company's count. On 26 October CISA, the US cyber agency, added both flaws to 

### The spectrum
 every agency, by what it says to do with a system you cannot patch 

 6 No offline advice 
 EU ENISA CSIRTs Network AU ASD's ACSC NZ NCSC NL NCSC-NL IT ACN / CSIRT Italia JP JPCERT/CC 

 2 Consider it, or after other steps 
 UK NCSC CH BACS 

 1 Restrict access 
 LV CERT.LV 

 3 Isolate from the internet 
 EU CERT-EU FR CERT-FR CA CCCS 

 2 Take it offline 
 US NSA Cybersecurity US CISA 
Not readable from this capture environment: CCN-CERT, CNCS. 

### How sure are we?
 70 facts 

- 20 confirmed 
- 36 reported 
- 7 disputed 
- 3 contradicted 
- 4 unverified 

### Fixed versions, and the settings until you are there

 Fixed in 8.5.12 · 8.4.27 · 8.3.36 · 8.2.35 
 memory_limit=-1, set where applications cannot Removes the controllable memory-limit failure; an underlying allocation failure can still reach the vulnerable 
 A low post_max_size (8M without uploads, 32M w Reduces exposure to specific attack paths; does not make an installation safe. 
 A container or cgroup memory limit as an avail Do not use RLIMIT_AS or RLIMIT_DATA: they can cause the vulnerable allocation failure. 
 session.upload_progress.enabled=0 in php.ini, Blocks the confirmed session paths only. ini_set() and .user.ini are too late. 

### Which setups are exposed

 Apache mod_php Unauthenticated RCE demonstrated over HTTP with default input and memory limits, before any application code runs. 
 PHP-FPM For CVE-2026-109618 the GitHub advisory says no complete FPM exploit has been demonstrated; the PHP Foundation blog says RCE was confirmed on FPM thro 
 php-cgi Listed by php.net among installations serving web requests. 

### Where the fix is

{'commit': '3584a98bda0f2c0d367255b046798b0d3a221a19', 'short': '3584a98bd', 'subject': 'Avoid state corruption via bailout', 'author': 'Arnaud Le Blanc', 'authored': '2026-10-18T15:26:39Z', 'committe 
[{'layer': 'The language a site is written in (PHP code)', 'in_scope': False, 'text': "Not where the bug is. A site's own PHP code can be perfect; php2shell.com's phrase is that a 'Hello World' applic 

### Before you write: three things often got wrong

- contradicted The flaws are CVSS 10.0
who says it: social posts on 20 October, relayed by a vendor and a news site 
- disputed Remote code execution is confirmed on PHP-FPM
who says it: PHP Foundation blog; GHSA-6wmf for the session path 
- unverified The 8.5.12 fix may be incomplete, or there is a third, different bug
who says it: Fediverse posts relayed to oss-security by Aaron Rainbolt and Yves-Alexis Perez 

### The numbers in the news, and how far each holds

 70% Not stated. The headline is a restatement of the body's figure for websites. unverified 
 almost 70% The share of websites whose server-side language is PHP, as commonly published by web-technology surveys. Neither page names the survey. reported 
 about 30 million Not stated. reported 
 2,608,039 Hosts observed on the internet that expose PHP, as counted by one scanning vendor. reported 
 about 6,000 Resources identified by the national CERT as potentially affected, in one country. reported 
 674 Rows in the inventory: 206 marked Vulnerable, 46 Fix, 418 Investigation, 3 Not vulnerable, 1 without a status. confirmed 

### How it unfolded

 2024 An audit spots the out-of-memory weakness. Nobody can show it is exploitable, so it is left. 
 Aug 2026 Three teams using AI turn it into working attacks within three weeks and report them to PHP. 
 20 Oct The secret leaks: the CVE numbers circulate two days early, with a wrong severity score. 
 21 Oct PHP releases the fix a day ahead of plan. Firewall vendors already have rules live. 
 22 Oct Agencies warn: update, or take systems offline. Sites go dark as a precaution. 

### Also contested
 14 facts 
- disputed All PHP versions from 5 onwards are affected by at least one of the flaws
who says it: NCSC-NL; Wiz ('>= 5.4'); CERT-FR (5.x, 6.x, 7.x, 8.0, 8.1) 
- disputed A web application firewall may provide some protection until systems are patched
who says it: CISA 
- unverified 70% of the Internet is affected
who says it: Wiz (headline, X post); the BBC, which reports it as Wiz's 'roughly 70%' 

### The open questions

1 

#### Whether any website was actually broken into before it installed the fix.

2 

#### Whether the fix is complete. A report on 21 October suggested it may not be; the PHP secur

ity team replied on the mailing list on 22 October, and this site will settle the question once that reply is saved here. Separate 

3 

#### Who leaked the news on 20 October, and where.

### The two bug classes

[{'step': 'Before the fix', 'text': "When a request pushed PHP past memory_limit, the allocator called zend_mm_safe_error, which raised a fatal error inside a zend_try and then called zend_bailout(): a C longjmp back to 

### What was shown

 Apache mod_php Unauthenticated RCE demonstrated over HTTP with default input and memory limits, before any application code runs. 
 PHP-FPM For CVE-2026-109618 the GitHub advisory says no complete FPM exploit has been demonstrated; the PHP Foundation blog says RCE was confirmed o

---
site v0.22.44 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/line/index.html
