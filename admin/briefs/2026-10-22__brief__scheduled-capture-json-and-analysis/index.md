# Brief: scheduled capture of the sources that move, raw to JSON to analysis, and contradictions as the product

> About this site: how the site works, kept by the agents that run it.

The evidence vault's last capture is 11:34 UTC on 22 October.

# Brief: scheduled capture of the sources that move, raw to JSON to analysis, and contradictions as the product

Published 2026-10-22 18:03 UTC · `2026-10-22__brief__scheduled-capture-json-and-analysis.md` · [all briefs](../index.html)

## Brief: scheduled capture of the sources that move, raw to JSON to analysis, and contradictions as the product

Status: accepted, by being sent. Author: Dinis Cruz, editor. A message to the design agent on the evening of 22 October 2026, reproduced verbatim, after the review of how 24 outlets present the story. Priority: critical. What it asks for, as work, is set out below the message, followed by the board items it opens.

### The message

Can you capture the instruction that it is super critical that we start to do a scheduled call to those sites that have dynamic data, where we capture the raw data, then convert it to json (with time stamps) which should then trigger an data science analysis of it Note that those contradictions (in the different reporting storing) are very important, since they really shown the power of our methodology and workflows Our key principle for our graphs is "meaning through connectivity" where "facts" and "stats" all have a spectrum of evidence

### Why now

The evidence vault's last capture is 11:34 UTC on 22 October. By the evening the story had moved on in ways the site could not show:

- a minister's count of UK government services down

- Japanese banks and airlines offline

- Amazon's "broadly exploited in the wild"

- a community tracker with 50 sites dark and back up, against our 10

Every one of those lives on a page that changes during the day. A single capture of a page that changes is a fact about one minute. The story is in the series.

### What it means, as a pipeline

Five stages. Each one writes to a vault, each one is triggered by the one before, and none of them edits what an earlier stage wrote.

1. **Schedule.** A watch list of the sources whose content changes (below), each with a cadence: every 15 minutes while a story is breaking, hourly after that, daily once it settles. The source watch vault (`oq9gflln`) already runs scheduled checks; this extends it rather than starting a second scheduler.

2. **Capture the raw data.** On every run, fetch the page as served and as rendered, its text, a screenshot and its headers, and hash every file, exactly as the evidence vault does. Where a source publishes data (JSON, CSV, a git repository, an RSS feed), fetch the data itself, not the page around it. Write a new stamped capture folder only when the content hash changes; otherwise append one line to that source's check log saying it was checked and unchanged. Blocks are recorded as captures too.

3. **Convert to JSON, with timestamps.** One parser per source turns each raw capture into rows. Every row carries:

- three times: `observed_at` (our capture), `published_at` (what the source says) and `source_updated_at` (the source's own "last updated", where it has one)

- the capture's hash, so every number points back to the bytes it was read from

- the parser's version, so a parser fix can re-run over old captures and say what changed

 Rows are appended to a time series per source, never overwritten.

4. **Analyse.** A new JSON series triggers the analysis.

- **Within one source:** what changed since the last run, with rates (sites going dark per hour, products moving from vulnerable to fixed, attempts per hour where a party publishes a count).

- **Across sources measuring the same thing:** line them up on one time axis and on one unit. Where they disagree, record a **contradiction** (next section) instead of picking a winner.

- **Output:** charts and a written summary per run into the vault, and a short "what changed since the last run" that the site's what's-new page and the briefings can carry.

5. **Publish as graph and pages.** The site is rebuilt from the analysis outputs. Every chart, number and sentence it publishes links to the series, the series to the captures, and the captures to their hashes.

### Contradictions are the product

The editor's point: the places where the reporting disagrees are where this methodology shows its worth, so they are recorded, not resolved away. A contradiction is a first-class record with:

- the two (or more) statements

- who made each, and when

- the captures they come from

- what each actually measures

- the site's reading of why they differ

- its status: open, explained, or resolved, and by what evidence

The coverage review of 22 October already found these, as seeds for the ledger:

| Measure | One source says | Another says | Why they may differ |
|---|---|---|---|
| How much of the web | 70% of the Internet (Wiz headline, CNN headline) | 70% of websites use PHP (Wiz body, php2shell.com) | A share of websites restated as a share of the Internet; neither says how it was measured |
| Is it exploited? | "now being broadly exploited in the wild" (Amazon, via its blog and Tenable) | officials in Germany, the Netherlands and Japan "have not seen one succeed" (The Next Web); CISA "has not observed exploitation ... as of the time of publication" | Attempts against sensors and honeypots versus a confirmed compromise of a named organisation; different times |
| Which versions | every version since PHP 5.4 (Cloudflare, Wiz) | 8.2 to 8.5 (the CVE records); backports for 7.4 to 8.1 (php.net) | Affected versus supported versus patched; the CVE record lists only supported branches |
| How many still unpatched | "90% of systems at risk are yet to" fix (BBC, attributed to researchers) | 1.57 million of about 2.6 million hosts unpatched on 21 October (Censys via The Hacker News) | Different populations, different dates, unnamed method |
| UK government services down | 32 unavailable and 4 partly (a minister, via the BBC) | "dozens of UK government services" (The Register) | Probably the same count; needs the Hansard record |
| Sites taken offline | 10 operators (this site's impact ledger) | 50 sites, 2 still dark (PHPocalypse Tracker) | Breadth of collection; this site requires a captured source per row |
| Severity | CVSS 10.0 (the leak, 20 October) | CVSS 9.2 (the CVE records) | The leaked score was wrong; recorded on the leak page |

### Meaning through connectivity, and a spectrum of evidence

The principle for every graph on this site: **meaning through connectivity**. A node means what its edges say about it.

- A fact or a stat is not true or false in isolation. It sits on a **spectrum of evidence**, and its place on the spectrum is read from its connections: how many captures support it, how primary they are, whether they agree, whether anything contradicts it, and how recently it was checked.

- Concretely, the five status words become points on that spectrum rather than labels. From weakest to strongest:

- unverified

- reported once

- reported by several, all citing one origin

- corroborated by independent parties

- confirmed by two primary sources

- counted by this site from a captured file

 A contradiction is an edge that pulls the reading down until it is explained.

- **Edges are typed:**

- *cites*

- *restates* (the same claim passed on)

- *measures differently* (the same word, a different quantity)

- *contradicts*

- *supersedes* (a later capture of the same source)

- *derives from* (a number computed from another)

 "Restates" matters as much as "contradicts": ten outlets repeating one Wiz headline is one source, not ten, and the graph must show that.

- **Stats carry their series**, not just their latest value, so a graph of a number is a line with every point linked to its capture.

### Watch list to start with

Sources that changed during 22 October and publish something parseable, in priority order:

1. **NCSC-NL php2shell repository**: the software list and README, from its git history; already read hour by hour on /patching/inventory/.

2. **PHPocalypse Tracker**: the sites dark and back up, with times and verification notes.

3. **CISA KEV catalog** (JSON): the first entry for either CVE is the official "exploited" signal.

4. **The CVE and NVD records** (JSON) for both CVEs: score, affected ranges, references added.

5. **php.net**: the advisory and the ChangeLog, for a follow-up release or a statement on the incomplete-fix report.

6. **Amazon's and Cloudflare's posts, and Matthew Prince's posts on X**: the attempt counts.

7. **The BBC live page and the follow-up story**; The Register's and The Next Web's follow-ups: impact counts by country.

8. **Tenable's FAQ change log and SOCRadar's update lines**: as a cheap index of what changed elsewhere.

9. **The national agencies' pages** in the agencies table: for edits to the offline advice.

10. **oss-security**: the thread on the incomplete-fix report.

### What this brief does not change

Capture rules stay as they are: capture, don't paraphrase; captures are only ever added; third-party pages are held privately and never republished; blocked fetches are recorded; no keys in any file. A number from a scheduled run reaches the site only through the same claim, status and source discipline as everything else.

### Board items opened by this brief

057 to 063, listed on the board.

This brief is the file `admin/content/briefs/2026-10-22__brief__scheduled-capture-json-and-analysis.md` in the repository, published as written.

← older: Brief: the second stories, the signals, and the inventory newer: → Brief: the phone app, what do I need to know for the time


---
site v0.22.53 · data as of 2026-10-29T00:09Z · vault commit 6c07e190d81e · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__scheduled-capture-json-and-analysis/index.html
