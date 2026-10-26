# Mockup C: a content page, what sixteen agencies advise

The agencies page redesigned: the answer in one line, every agency placed on one spectrum from no offline advice to take it offline, a card per agency, and the evidence table one click away.

> Mockup C for review, built from the data of release v0.22.22. Not the live site.

The analysis · government advice 
## 16 agencies. All say update. They split on offline.

The question that divides them is not whether to patch but what to do with a system you cannot patch today. Read left to right: from no offline advice to take it offline. 

In one line 
The US says take it offline. The UK says that is the fourth step. Europe says isolate. Australia, Japan and the Netherlands say nothing about it. 

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

### Agency by agency

 All 16 Take offline Isolate No offline advice 

#### NSA Cybersecurity
 US 
 Take offline 
 If an immediate update is not feasible, it is recommend[ed] that organizations take the system offline until it can be fully mitigated. 

 NSA Cyber on X NSA 

#### CISA
 US 
 Take offline 
 Organizations that cannot update immediately, or that continue to use PHP 8.1 or earlier unsupported versions, should take PHP-based systems offline until they can be pat 

 CISA CISA 

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

No take-offline or isolation advice. The BBC's 'Australian counterparts' framing is not supported by the page. Parts of the body are still pre-patch t 

 ACSC ACSC 

#### NCSC
 NZ 
 No offline advice 

The only agency to say active exploitation is reported. It does not say whose reports. Time converted from NZDT by this site. 

 NCSC New Zealand NCSC New Zealand 

#### NCSC-NL
 NL 
 No offline advice 

Runs the public php2shell GitHub repository with the software inventory the UK NCSC cites, cPanel detection and mitigation scripts, and an SPDX/VEX so 

 NCSC-NL NCSC-NL 

#### ACN / CSIRT Italia
 IT 
 No offline advice 

Update only. Lists the four fixed branches and no end-of-life branches. 

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

 The evidence table: every agency's words, dates and sources 
On the live site this is the full table, one row per agency with the verbatim sentence, the publication time and every saved source. 
 A wall of text becomes three layers: the one-line answer, the picture, and the cards; the evidence table is one click away, not the first thing you see.

---
site v0.22.22 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/c/index.html
