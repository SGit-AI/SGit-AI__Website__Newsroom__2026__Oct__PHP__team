# BBC re-grade, step 2b (journalist, for the projects desk)

27 October 2026, 15:20 UTC. Data commit d64be95. Full detail: `bbc-regrade.json` beside this file. Quotes were checked
against the capture files in the evidence vault nnd3i8iw (sha256 recomputed and matched). Nothing was sent, committed or released.
## The short answer

Of the four points, none goes as briefed. Point 1 and point 3 put words in the BBC's mouth that its page does not
carry. Point 2 is not a misquote. Point 4 is real but small. Two of our own "contradicted" BBC rows are the larger
problem, and they are ours to fix first. The kindest, strongest submission is one point (4), or none, after a fresh capture.
## The four points

| # | Point | Verdict | Goes? | Confidence |
| --- | --- | --- | --- | --- |
| 1 | "Disclosed on 22 October" | The BBC page does not say it. Our date (fixes released 21 Oct) is right. | No, drop R-013 | high |
| 2 | NCSC quote | Not a misquote; an earlier NCSC wording is the likely source | No, drop R-014 | medium-high |
| 3 | "Agencies advise offline" | The BBC did not say that; what it did say is true | No, drop R-015 | high |
| 4 | R-002 "roughly 70%" | Minor; Wiz does say "70% of the Internet" | Optional, last, with a note that Wiz is asked too | medium |

**1. Disclosure date.** Searched all three BBC `text.txt` captures, the extracted text and the 07:55Z raw page: no date of
release anywhere. The BBC says "a plan to release the fix in late October", that a leak forced the foundation "to bring
forward its announcement", and that disclosure "worked well" until "two days ago". The only "October 22" is a Getty photo
caption. Our evidence for 21 Oct, all checked: php.net "scheduled for Wednesday, 21 October 2026 at 14:00 UTC"
(php-net-advisory, 20261022T080901Z, df0b1bba...); GHSA 13:34:25Z (79647ef8...); GitHub release 14:06:46Z
(github-php-src-tag-php-8.5.12, 330630ed...); the Foundation blog "Published on Oct 21, 2026" and the move "from October
22nd, 14:00 UTC, to October 21st" (a1be057a...); Wiz "October 21, 2026: ... Public disclosure" (e3568b6f...). Note the
briefing's "all 14:00 UTC": that is the schedule; the stamps run 13:34 to 14:06. Where "22 October" does appear: ACSC,
"publicly announced on Thursday 22 October 2026 at 0100 AEDT" (9370af14...; that is 21 Oct 14:00 UTC), and Wiz's X thread,
"Apply the Oct 22 security release" (6c179776...). Suggested friendly note, only if the editor wants one: "The fixes
were released on 21 October; the entry might say so." Unchanged after 26 Oct.

**2. NCSC quote.** BBC (text.txt line 234, c88b8c5f...): "Where immediate remediation is not feasible, organisations
should consider taking the system offline until it can be fully mitigated," the NCSC said in a note (linked to the NCSC
page). The BBC entry was first published 06:30:26Z (labelled 07:30 BST, which is not the NCSC's 07:30 GMT) and last
edited 06:49:45Z (raw/initial-data.json, ee7445a5...). The NCSC page we captured at 08:09Z (a18ceeb0...) has the offline
advice as step 4 of 6 in other words and was last-modified 07:30:02 GMT (headers.json 642ad246...): 40 to 60 minutes
after the BBC entry. LBC's article, "21 Oct 2026, 15:41", updated about 16:29Z that day (125176f1...), carries the BBC's
exact sentence as the NCSC's. So the sentence was almost certainly on the NCSC page, or in an NCSC note, before the
change. CCCS AL26-026 (9e7f44cc...) matches only the opening ("Where immediate remediation is not feasible, organisations
should consider") and then says "isolating internet-facing applications"; the ending "take the system offline until it
can be fully mitigated" matches the NSA (8a8553ea...) and the NCSC. CERT-EU's opening differs ("Where that is not
feasible"), so "shared across Five Eyes and CERT-EU text" overstates. Cyber Express copies the BBC (not independent).
Conclusion: not a misquote, not shown to be an attribution error; an earlier NCSC copy (Wayback, archive.today, NCSC
change log) would settle it. Optional question, not a correction: "Could you tell us which NCSC text this line comes from?
Our 22 Oct 08:09 UTC capture words it differently and we would like to cite the version you saw." Unchanged after 26 Oct.

**3. Agencies.** The BBC (lines 232, 188) says the NCSC "as well as its counterparts in the EU and Australia, earlier urged
those who use PHP to apply the fixes" (true: ACSC "Apply available security updates"), quotes the NCSC, and reports the
NSA's X post saying take the system offline (true). It does not say the EU and Australia advise offline. ACSC gives no
offline advice; CERT-EU, CERT-FR and CCCS say isolate; NSA, CISA and (after mitigations) NCSC say offline; Italy's ACN
says consider taking sites offline (acn-it-php2shell line 70, 19fac2ed...), which our notes and agencies.json get wrong.
If a note is wanted: "Agencies agree on patching now; some also advise isolating or taking systems offline if patching is
not possible." Unchanged after 26 Oct.

**4. R-002.** BBC (lines 144, 284): Wiz "estimating that \"roughly 70%\" of the internet is affected, though the BBC is
unable to independently verify that figure." Wiz's blog headline and X post say "70% of the Internet" (e3568b6f..., 6c179776...);
the body says "powers 70% of all websites in the world". Only "roughly" inside quotation marks is not in Wiz's captured
words (it may come from an interview we do not hold, so unverified as an error). The BBC's caveat is right. Suggestion
(R-002's own, kept): "...with Wiz saying the flaws affect \"70% of the Internet\", a figure that matches surveys of how many
websites use PHP rather than a count of vulnerable systems, and that the BBC has been unable to independently verify."
Stands after 26 Oct.
## The twelve claims

| Claim | Status | Fact-check | Re-grade |
| --- | --- | --- | --- |
| scale-70pc-internet | unverified | not-shown, A1 | stands |
| scale-30m | reported | holds, A2 | stands |
| ai-found | reported | holds-in-part, A3 | stands (optional wording) |
| most-severe | reported | holds-in-part, A2 | changed: note adds the WSJ route (Wiz co-founder, via Substack cb3714dc...) |
| leak-video | reported | holds-in-part, A3 | changed: drop "around 20:00 UTC" as Calif's time |
| disclosure-22oct | contradicted | refuted, A0 | changed: remove the BBC as author; the BBC does not say it |
| no-exploitation | reported | holds-in-part, disputed | changed: status disputed, dated wording (below) |
| probing | confirmed | holds, A5 | stands (exploitation.json row 13 is stale) |
| vibe-code | unverified | holds-in-part, A1 | stands; a question to the BBC, not a correction |
| offline-ncsc | disputed | holds-in-part, disputed | changed (note): add the 06:30Z entry and LBC |
| offline-allies | contradicted | holds-in-part, status_fit "understated" | changed: replace with the BBC's actual sentence |
| affected-sites | reported | holds, A2 | stands; also cite the 07:55Z raw copy for Edinburgh, shops, BBC, Geneva |

**Mismatches.** (a) `no-exploitation`: status "reported" against fact-check tension "disputed"; the fact-check's own
`status_fit` says "ok", so nothing catches it. Proposed pair: status disputed, fact-check disputed. It was true when said
(Ryan Austin, Radio 4, about 07:00 UTC 22 Oct: "Not at the moment... it doesn't look like exploitation has taken off or
been widespread"; the claim text is the BBC headline, not his words). What changed: Amazon's honeypot hits (17 Oct),
NCSC NZ (21 Oct), and on 26 Oct CISA's KEV listing of both CVEs, still with no named victim. Dated wording: "As of about
07:00 UTC on 22 October, Calif's Ryan Austin told BBC Radio 4 ..." (b) `offline-allies`: "contradicted" against fact-check
"holds-in-part", status_fit "understated", and attributed to the BBC, which did not write it. (c) `disclosure-22oct`:
status contradicted is right as a fact; the BBC attribution is not carried (the fact-check says so).
## The four candidates

None becomes a point. All BBC wording below is checked against the capture.
- "Most severe... by AI": BBC says Wiz "describes the flaws as the \"most severe\" ever detected by AI". Wiz's blog is
  narrower, but the WSJ (relayed by Substack) quotes Wiz's co-founder with "the most severe AI vulnerability that was ever
  found". Probably an interview line, accurately attributed. Update our claim note.
- OpenAI "security issues": the BBC says "one of the most impactful security issues in recent memory"; the tweet says
  "vulnerabilities". One word, and OpenAI's blog (blocked) may use the BBC's. Too small.
- Foundation joined in July: the BBC says "got accepted into... Patch the Planet" in July 2026; the Foundation's audit
  with Calif began 30 July. Consistent.
- Calif in August, OpenAI and Wiz shortly after: Calif first (reported 11 Aug), the Foundation says OpenAI the same day,
  Wiz 24 Aug. Differences of days. Context only.
## Our side: no longer true or not true

1. claims.json `disclosure-22oct` (`by`, `sources`), attribution.json, graph.json, fractal.json, and the php-net-advisory
   note ("the BBC frames disclosure as 22 Oct"): the BBC does not say it.
2. claims.json `offline-allies` (`status`, `by`) and attribution.json; claim-review.json "offline-advice" (24 Oct, "agrees");
   agencies.json row ASD's ACSC ("the BBC's Australian counterparts framing is not supported"): the BBC said only that
   they urged applying the fixes, which ACSC did.
3. agencies.json rows NCSC UK and CCCS, and claims.json `offline-ncsc.note`: read as a BBC misquote; omit the 06:30Z
   entry time and LBC; "shared across Five Eyes and CERT-EU text" overstates.
4. claims.json `no-exploitation` (status; present tense after the KEV listing 26 Oct); exploitation.json row 12.
5. claims.json `leak-video` (the 20:00 UTC time) and `most-severe.note`.
6. Italy: sources.json acn-it-php2shell notes, agencies.json ACN row, `offline-allies.note` say "no offline advice"; the capture says otherwise.
7. exploitation.json row 13 says Amazon's post was not found; `probing` cites it as confirmed.
8. outreach.json R-002 channel "to find"; no BBC corrections page is yet a source in sources.json (PROJECT-002 step 1 captured
   pages sit in the source watch). No BBC capture is later than 22 Oct 08:05:59Z.
## What should stop the submission

The four-point submission as briefed. Fix items 1 and 2 first (the desk releases), recapture the live page (the BBC may have
changed it), then decide whether point 4 alone is worth the editor's time.
injection_seen: none.
