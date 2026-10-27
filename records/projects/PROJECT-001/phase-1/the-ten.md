# PROJECT-001 phase 1, step 1c: the ten names (checkpoint A)

By the Sherpa, run by projects@php.newsroom. 27 October 2026. Nothing is sent. Detail: `the-ten.json`.

Nine of the ten pass all three tests (we hold their words, they are careful, they have a published channel) and each has one ask: check what we hold. The BBC, rank 10, scores 2 (a correction is open) and is a corrections case on the editor's briefing: its one ask is one Stage 1a correction submission, three points, and no check or interview. No channel URL is held in our data; each is to be confirmed. The order is the proposed send order.

| # | Name | Kind | The one ask | Channel (to confirm) | Clean hands first |
|---|---|---|---|---|---|
| 1 | Huntress | researcher/vendor | check-what-we-hold | Huntress's published press or contact page (huntress.com) | Read 27 Oct capture against 21 Oct text; PoC half disputed |
| 2 | Cloudflare | researcher/vendor | check-what-we-hold | Cloudflare's press office (cloudflare.com) | Link Prince's page; confirm post unchanged |
| 3 | Fastly | researcher/vendor | check-what-we-hold | Fastly's published press contact (fastly.com) | None; check only |
| 4 | Imperva Threat Research | researcher/vendor | check-what-we-hold | Imperva's published press contact (imperva.com) | Date the 'no traffic' line before KEV |
| 5 | Weird Gloop | other | check-what-we-hold | Weird Gloop's published contact page (weirdgloop.org) | None; check only |
| 6 | The PHP Group / php.net (the PHP security team) | maintainer | check-what-we-hold | the PHP security team's published security contact (php.net); no personal address | Add 2 sources to php-group, 2 to Zelenka; K-008/K-010/K-011 stated |
| 7 | NCSC-NL and the Dutch government (Rijksoverheid) | CERT/agency | check-what-we-hold | NCSC-NL contact page (ncsc.nl) and the Rijksoverheid press office | Fix 674/675 and 3/4; make a page; add 4 sources |
| 8 | CISA | CERT/agency | check-what-we-hold | the CISA media and public-affairs contact (cisa.gov) | Carve a page from agencies; add 6 sources; line 23 superseded first |
| 9 | American Banker | news | check-what-we-hold | American Banker's published contact or corrections route | Create page; ask 'is that still true?' |
| 10 | BBC News (live page; Audience Services complaints route) | news | correction (Stage 1a, 3 points) | BBC Audience Services (the BBC's own complaints route); channel to capture first | Fresh capture; capture complaints page; K-records; fix no-exploitation; complete page |

## Why each, and the words we hold

**1. Huntress.** We hold its rapid-response post, scoped and dated ('As of October 21 at 4:30pm ET, Huntress has not observed in-the-wild exploitation'), re-captured 27 October. It is the clearest case of 'attempted' kept apart from 'exploited', and its page is complete. Own words: `huntress-php2shell-rapid-response` (20261027T071509Z). Topic: 'exploited' against 'attempted'; 'leaked exploit'.

**2. Cloudflare.** We hold its WAF post, which counts attack traffic and not compromises and says 'almost 70% of websites'. Its page is complete and no request is open against it. Own words: `cloudflare-blog-php2shell-waf` (20261023T160435Z). Topic: '70% of the internet' against '70% of websites'; 'exploited' against 'attempted'.

**3. Fastly.** We hold its blog post, the most candid vendor on exploitability and on what a WAF cannot do. Its page is complete. Own words: `fastly-blog-php2shell` (20261024T133450Z). Topic: 'exploited' against 'attempted'.

**4. Imperva Threat Research.** We hold its post: 'no traffic matching the monitored exploit patterns' before disclosure and '69% of websites whose server-side language is known'. Its page is complete. Own words: `imperva-blog-php2shell` (20261023T080331Z). Topic: '70% of the internet' against '70% of websites whose server-side language is known'.

**5. Weird Gloop.** We hold its blog post, the only measured outage: 13 hours offline and about 94% of page views from cache. It makes no claim of compromise. Own words: `weirdgloop-blog-php2shell` (20261023T080157Z). Topic: 'millions of sites offline' against the trackers' counts.

**6. The PHP Group / php.net (the PHP security team).** We hold php.net's advisory and changelog, scoped ('only an update is a complete solution'), and the two CVE records it numbers. Our claims settle K-008, K-010 and K-011 against its wording, so it should see them first. Own words: `php-net-advisory` (20261022T080901Z), `php-net-changelog-8` (20261022T081558Z), `github-php-src-tags` (20261022T081558Z) and more. Topic: 'CVSS 10.0' (its 9.2); 'leaked exploit'.

**7. NCSC-NL and the Dutch government (Rijksoverheid).** We hold five of its publications, including the software inventory whose README says entries are 'investigation leads'. It advises a risk assessment per system and 'considering' switching off, not a shutdown order. Own words: `ncsc-nl-php2shell` (20261022T084815Z), `rijksoverheid-ncsc-php-news` (20261022T113033Z), `ncsc-nl-advisories` (20261022T081605Z) and more. Topic: 'millions of sites offline' (it advises assessment, not shutdown); no brief phrase matches closer.

**8. CISA.** We hold its 21 Oct alert ('has not observed exploitation ... as of the time of publication') and its 26 Oct KEV listing of both CVEs. It names no victim, which is the heart of 'exploited' against 'attempted'. Own words: `cisa-alert-kev-20261026` (20261027T004502Z), `cisa-alert-php-20261021` (20261022T081353Z), `cisa-kev-catalog` (20261027T004502Z) and more. Topic: 'exploited' against 'attempted': KEV on 26 October; no named victim.

**9. American Banker.** We hold its report that 'banks have so far dodged early damage' and that no U.S. bank has reported a compromise: scoped to reports, and it holds. It is a careful trade title, not a headline outlet. Own words: `americanbanker-news-banks-dodge-early-damage-from-php2s` (20261024T083755Z). Topic: 'exploited' against 'attempted'.

**10. BBC News (live page; Audience Services complaints route).** We hold its live page, which kept the hedge 'unable to independently verify that figure'. It is the editor's named first outlet and the origin of three points of ours, so its one ask is a correction submission, not a check or an interview. Own words: `bbc-live-ckgel5xp2xv9t` (20261022T080559Z). Topic: '70% of the internet' against '70% of websites'; 'millions of sites offline' against the trackers' counts.

Clean hands in full and the phase-2 work per member (ontologist, journalist, correspondent, story-site) are in `the-ten.json`.

## Starters not in the ten

- **BBC** (score 2): Chosen at rank 10 on the editor's briefing (via the coordinator): a corrections case, one Stage 1a submission with three points; no check or interview ask.
- **PHP Foundation** (score 2): Careful is unknown and K-008, K-010 are open on its wording; the PHP security team (php-group) goes first as the maintainers' message.
- **NCSC UK** (score 2): One source only (22 Oct), no later statement and no hedging evidence; ask once we have checked for a newer one.
- **Trend Micro** (score 2): One Japanese press release (23 Oct), no analysis post, no actors entry and no page; the brief's 'cited most' does not hold on our evidence. Left out unless an English research post is captured first.

## Reserves (up to five)

| Name | Score | Ask | Why |
|---|---|---|---|
| The PHP Foundation | 2 | check-what-we-hold | Starter. Score 2: no hedging evidence either way, and K-008 and K-010 are open against its wording. The PHP security team (rank 6) covers the maintainers; the Foundation would be a second PHP message. |
| UK National Cyber Security Centre (NCSC) | 2 | check-what-we-hold | Starter. Score 2: one source, one capture (22 Oct); no statement after 21 Oct held, and no hedging evidence. It would ask whether an earlier offline wording was published and changed. |
| Alexandre Daubois, PHP security team (personal blog) | 3 | interview, later | Score 3 but folded into rank 6 (one message to the team). Keep as a later interview ask (25 Oct brief, format A). |
| Die Presse | 3 | check-what-we-hold | Score 3 news; moved out when the BBC became one of the ten. 23 Oct explainer, no compromise known in Austria. Needs a page and an English reading; one short question. |
| CERT.LV (Latvia) | 3 | check-what-we-hold | Score 3 CERT; no page of its own (inside agencies) and the latvija.gov.lv source is not CERT.LV. Use if the editor wants a third CERT. |

## For the editor to decide

1. Is the BBC's page the 'BBC file' at /outlets/bbc/ (a template for every outlet) rather than /outreach/bbc/? And does point 3 (R-002) go now with a note that Wiz has been asked too, or wait for R-001?
2. Trend Micro: leave it out (one Japanese release), or ask us to capture an English post first and substitute it?
3. With the BBC as a corrections case, American Banker is the only news check-ask in the ten (Die Presse is first reserve); the other news outlets have a correction open. Is that enough news, or swap Die Presse back for a vendor?
4. One message to the PHP security team (with Zelenka and Daubois linked) instead of the PHP Foundation: agreed?
5. Order: complete-page vendors first (ranks 1 to 5), then those needing clean hands (6 to 10). Send the first five as soon as phase 2 passes, or all ten together?

## Corrections to PROJECT-002 (nothing fixed here)

- R-004 evidence in data outreach.json says 'CISA had not observed exploitation' with no date; superseded by the 26 Oct KEV listing. (files/outreach.json R-004 evidence)
- R-006 evidence says 'neither CVE is in CISA's catalogue ... as of this site's latest check': undated and now false. (files/outreach.json R-006 evidence)
- NCSC-NL inventory count: we say 674 rows, 3 not vulnerable; the file has 675, 4 (fact-check scale-ncsc-nl, contradicted). (agencies and rijksoverheid pages)
- Agencies page line 23 still leads with the old CISA statement as confirmed/A6; the superseded status should lead. (refs agencies page, lines 23 and 27)
- R-002 depends on a 22 Oct capture of the BBC page; recapture before sending, 'roughly 70%' may have changed. R-004 and R-007 have actor null. (files/outreach.json R-002, R-004, R-007)
- 44 sources that belong to actors are not in actors.json; Trend Micro has no alias or actor. (actors.json)

No text addressing an AI was found in anything read.
