# Mockup B: the front page for a security lead, Standard view

A three-column working view for a security lead: their reading path and the site by task on the left, what changed since the last visit and the next three actions in the middle, and the state of the evidence as charts on the right.

> Mockup B for review, built from the data of release v0.22.46. Not the live site.

S 
 Sam 
Security lead 

Your reading path 

2 of 5 read · next: Exploitation signals 
 Today 9 new What to do The incident Detection and defence The agencies 16 Every claim 70 Ask 

Since your last visit · 27 October 2026, 19:13 UTC 

## 9 things are new, 3 changed. Two matter for your runbook.

Internet-facing mod_php first, then FPM, then everything else. Where patching slips, apply php.net's temporary settings and record that each blocks a known path only. Alert on PHP workers spawning shells or fetching tools. Decide now who calls isolate or offline, and when. 

### Your next three actions
 The whole playbook 

1 

#### Patch internet-facing first

mod_php, then FPM, then the rest. Restart every worker; rebuild every image. 

2 

#### Bound the known paths

session.upload_progress off, low post_max_size, fatal_error_backtraces off on 8.5. None of these is a fix. 

3 

#### Watch the process tree

Alert on a PHP worker spawning a shell or a downloader. A clean access log proves nothing. 

### What changed

 All Facts Timeline Questions Stories 

 New story v0.22.46 
#### Someone stole the bitcoin. What that does, and does not, tell us about php2shell

✓ 

 New question v0.22.46 
#### Has anyone actually been hacked?

✓ 

 New front v0.22.46 
#### Front page: right now

✓ 

 New front v0.22.46 
#### Front page: latest

✓ 

 Changed front v0.22.46 
#### Front page: the core facts

✓ 

 Changed fact disputed v0.22.46 
#### The UK's NCSC, the NSA and their counterparts in the EU and Australia advise taking systems offline where patching is not feasible

 ACSC CERT-EU NCSC-NL ACN / CSIRT Italia 
✓ 

 Changed fact disputed v0.22.46 
#### There is no evidence yet that hackers have exploited the flaw

 BBC News Amazon CISA 
✓ 

 Changed fact reported v0.22.46 
#### As of 19:13 UTC on 27 October, no named organisation has said it was compromised through php2shell. That the flaws are exploited is now CISA's position: on 26 October it added both

 CISA CISA Huntress Amazon 
✓ 

 Changed fact contradicted v0.22.46 
#### The flaws were disclosed on 22 October 2026

 php.net php-src 
✓ 

Marked read, an item fades and then leaves this list; it comes back only if what it says changes. 

#### How sure are we?

- 20 confirmed 
- 35 reported 
- 9 disputed 
- 2 contradicted 
- 4 unverified 

#### Events per day, October

 12 17 18 19 20 21 22 26 
Red: from the leak on 20 October. 

#### Exploitation signals

- 2026-10-17 
Amazon: One exploit attempt against a MadPot honeypot from a commercial anonymisation network, fou 
- 2026-10-17 
Amazon: One exploit attempt against a MadPot honeypot from an IP on a commercial anonymisation net 
- 2026-10-20 to 21 
Cloudflare: 'We observed attack traffic targeting our customers' after the leak, and attackers 'mutati 
- 2026-10-21T02:00Z 
Amazon: Proof-of-concept attempts begin, then six hours of attempts from anonymised infrastructure 
 0 confirmed compromises 

#### Fixed in

 8.5.12 8.4.27 8.3.36 8.2.35 
8.1 and older: source backports only.

---
site v0.22.46 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/b/index.html
