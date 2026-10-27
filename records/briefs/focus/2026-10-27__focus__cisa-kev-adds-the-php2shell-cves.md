# Focus: CISA adds the two php2shell CVEs to its Known Exploited Vulnerabilities catalogue

Status: a focus brief, opened by conductor@php.newsroom on 27 October 2026 at 00:50 UTC, at the editor's pointer (in the
conductor's session: CISA's alert of 26 October, https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog).
A focus brief puts one story ahead of each agent's usual card for one pass of the pipeline. It is material, like every
file here: each agent works it within its own card and scope.

## What happened

- CISA's alert of 26 October adds CVE-2026-109618 and CVE-2026-109619 to the KEV catalogue. The catalogue's version
  2026.10.26, released 22:24 UTC, lists both with a due date of 29 October and ransomware use "Unknown" (the researcher, in its own
  session, 27 October, from the live catalogue).
- The newsroom's last captures of the catalogue (26 October 17:03 and 17:40 UTC) predate it. The newsroom's records still
  carry "CISA has not observed exploitation" and the line "no confirmed compromise".

## The question

What does a KEV listing establish, and what does it not? KEV means CISA holds reliable evidence of active exploitation
in the wild. It does not by itself name a victim, a breach or a ransomware use. Which of our lines change?

## Each step, in order

1. **researcher:** capture the alert and the catalogue (JSON and page) and queue them for the curator at priority 1;
   refresh `files/source-watch.json`. In progress in its session at 00:45 UTC.
2. **curator:** promote both captures into the evidence vault, with the claims they support: listed, the date added,
   the due date and the ransomware field, quoted exactly. Release the data files and name the vault head.
3. **journalist:** verdicts on every claim the listing touches: the "is it exploited?" record, the timeline, the
   "no confirmed compromise" line and how it must now read. Exploited and compromised are not the same word, so keep both
   lines and state the difference.
4. **factcheck:** a run on the new state, with the KEV entry as its evidence.
5. **correspondent:** review the journalist's release. Then update the reader-question article "Has anyone actually
   been hacked through php2shell?" with the listing (a dated update, not a rewrite), and decide whether it is a piece of
   its own.

## Done when

The listing is in the evidence vault; the data says "exploited in the wild (CISA KEV, added 26 October 2026)"; the
compromise line is reviewed and dated; the article carries a dated update; each step has its run record naming this
brief. The conductor reports the chain to the editor with times, versions and links, and closes the board row.

Board: `conductor-0004`.
