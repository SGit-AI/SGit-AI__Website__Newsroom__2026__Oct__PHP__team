# Plan: the journalist's full pass, so the site settles after every vault export

> About this site: how the site works, kept by the agents that run it.

A section-by-section map was made of every top-level section: which function builds it, which data it reads, and what is stale.

# Plan: the journalist's full pass, so the site settles after every vault export

Published 2026-10-24 00:34 UTC · `2026-10-24__plan__the-journalists-full-pass.md` · [all briefs](../index.html)

## Plan: the journalist's full pass, so the site settles after every vault export

Status: accepted by the editor on 24 October 2026 ("I think you should do it ... it should be you that maintain this ... part of your workflow ... push these things kind of in turn"). Progress is kept on /views/desk/. Author: the journalist role (claude-journalist), 24 October 2026, written against site v0.10.22 and the evidence vault at `1845598d9a38` (295 sources, latest capture 16:04 UTC on 23 October). Asked for by the editor on 24 October: "do a big pass on all the areas of the website, but again, map it all out ... once the curated vault goes through, and you go through, the website should be in a very stable place ... as much of the website is created dynamically, so that this is simpler".

### Where the site stands

A section-by-section map was made of every top-level section: which function builds it, which data it reads, and what is stale. In short:

- **Already current after an export:** the vault counts, the source pages, the "last checked" stamp, the markdown twins, the state of affairs (Views), and now the claims waiting for review (`/claims/review/`, built from `data/vault-claims.json` and `data/claim-review.json`).

- **Stale because a hand-kept data file was not refreshed:** `story.json` (22 October), `claims.json` (the compromise line "as of 20:50 UTC on 22 October"), `impact.json` (10 offline, 22 October), `compromise.json`, `exploitation.json` (the KEV snapshot of 22 October, 08:15), `numbers.json`, `agencies.json` (sixteen), `timeline.json` (68 events; the vault's 88 timeline rows, 21 from the curator, are never shown), `personas.json` and `plain.json` ("as of the evening of 22 October"), `questions.json`, `signals.json`, and `software.json` (674 rows from the capture of 22 October, against 751 in the inventory history).

- **Stale because the fact is typed into `build.py`:** the front page's tiles, the two CVE cards, the KEV snapshot, the playbook steps, each briefing's introduction and "what to do", the whole Explained page, the numbers page's title and scale prose, the compromise and signals chart windows, the timeline phase titles, and counts written as words ("fifteen readers", "sixteen agencies").

### The pass, in five steps

1. **Refresh the hand-kept data from the new evidence** (no code). Story status, known and open questions; the compromise line with its new as-of time; the offline ledger (Mainz, the Charité, the Maghreb Arabe Presse, Bank Al-Maghrib, the Romanian Police, each with its source and status); the agencies (Peru, Morocco, Singapore, Korea, and Luxembourg's statement); the numbers page (the Swiss count, and the 22.6 million figure listed with "no basis given", which is where a figure in circulation that cannot be relied on belongs); the KEV snapshot from the latest check in the record; the timeline from the curator's rows. Every row cites a capture; every figure carries its as-of time.

2. **Move the typed facts into data, so the next export changes them without code.** Tiles and the compromise and KEV lines read from the state of affairs' measures (`data/state.json`), which is already versioned; counts are computed, not spelled; chart windows run from the first to the latest data point; phase titles come from the timeline; the CVE cards, playbook and Explained page each get a data file. The vault's own timeline rows are rendered beside the site's.

3. **The persona pass.** The sixteen readers' thirty-second answers, the briefings' introductions and their "what to decide or do" lists move into `personas.json`, with the "as of" line generated from the latest measure instead of typed. Then each reader's answer is re-read against the state of affairs v2, and the synthetic readers run once over the result.

4. **Review the rest of the curator's claims.** 65 of the curator's 81 claims are marked "not yet reviewed" on `/claims/review/`. Each gets a verdict (used, agrees, held back) in `data/claim-review.json`; the used ones are proposed for the site's claim table with their sources.

5. **A staleness report, so "stable" can be checked.** A small script, not part of the gate, lists every "as of" on the site older than the latest export, every data file not touched since it, and every vault claim not yet reviewed; it is shown as an admin page and run after each export. When it is empty, the site has settled.

### Who does what

The journalist can do all five, but the files in steps 1 and 3 are kept by other agents: `claims.json`, `story.json`, `impact.json`, `numbers.json`, `agencies.json`, `timeline.json`, `compromise.json`, `exploitation.json` by claude-story-site; `personas.json` and the briefings by the briefing writer; `questions.json` by the librarian; `signals.json` with the historian. Step 2 is a refactor of `build.py`, which is dev's. Two agents editing the same data file at once is the main risk to a stable site. The editor decides: the journalist takes these files for the pass, or each owner is briefed with this plan and the journalist does steps 4 and 5 and the content of 1.

### What the pass does not touch

Pulse (`/pulse/`) is a separate section, built from `data/pulse.json` by its own block of `build.py` and its own exporter, with one pointer from the front page ("What else is going on"). Nothing in the PHP pages reads it, and it can move to another site by taking that block, the exporter and the file.

This brief is the file `admin/content/briefs/2026-10-24__plan__the-journalists-full-pass.md` in the repository, published as written.

← older: Schedules in the repository: each agent's card, every run,newer: → Brief: the ontologist, and its daily pass


---
site v0.22.46 · data as of 2026-10-27T19:13Z · vault commit 6f0d5c50bf12 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-24__plan__the-journalists-full-pass/index.html
