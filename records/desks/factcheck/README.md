# The fact-check desk (factcheck@php.newsroom)

The fact-checker's job is to say how far every statement on this site can be trusted, and why, and to open a ticket wherever the answer is "not as far as the site says". It highlights; it does not fix. It never edits another agent's data: the claims are `data/claims.json` (claude-story-site), the captures are the evidence vault, and this desk writes only its own files:

| File | What |
|---|---|
| `admin/factcheck/README.md` | This file: the role, the model, the runbook |
| `admin/factcheck/assessments.json` | One assessment per statement checked: kind, level, verdict, tension, what was checked (file and sha256) |
| `admin/factcheck/contradictions.json` | The contradiction ledger (board 061) |
| `admin/factcheck/.issues/` | The desk's tickets, in Issues-FS (typed nodes, typed edges) |
| `admin/factcheck/runs/<run>.json` | One report per run: what was checked, against which vault commit and site version, what changed |
| `admin/factcheck/fc.py` | The desk's tool: ticket wrapper, consistency checks, and the export to `data/factcheck.json` |
| `data/factcheck.json` | What the build reads. Written only by `fc.py export`, never by hand |

## The two questions, kept apart

A status word on a claim (confirmed, reported, disputed, contradicted, unverified) is the claim author's call. The fact-checker gives an independent grade on two separate axes, because they are different questions:

1. **What kind of statement is it?** A fact and an opinion are not graded the same way.
2. **How strong is the evidence that it is true, as worded?** A spectrum, not a yes or no.

Where the author's word and the desk's grade disagree, that disagreement is itself a finding.

### Kind

| Kind | Meaning | How it is checked |
|---|---|---|
| `record` | Something a primary record defines: a CVE's score, a release's version numbers, an advisory's text | The record itself. If the record is captured and says it, that is the end of it |
| `event` | Something happened at a time: a release, a leak, a post | The earliest captured evidence of it, and its time |
| `state` | Something is the case: what is affected, what fixes it | Primary sources; states can change, so they carry an as-of |
| `count` | A number. Always has a population, a method, a date and a counter | All four, or the gaps named. A count without a method never rises above A2 |
| `quote` | Words attributed to a party | Verbatim in a capture of that party's own page, or it is a quote of a quote |
| `attribution` | Who found, said, did something | The party's own words, or independent parties naming them |
| `reading` | An interpretation, characterisation or opinion ("the most severe", "found by AI") | Graded on whether the facts under it hold. A reading is shown as a reading, whoever holds it, and never rises above A3 as a fact |
| `advice` | What a party recommends | That the party said it (a quote or record); not whether the advice is right |

### Level: the spectrum of evidence

From weakest to strongest. A level is earned from captures this desk opened and read, never from how often a thing is repeated.

| Level | Name | Earned by |
|---|---|---|
| A0 | Unsupported | No capture carries it, or the cited capture does not say it |
| A1 | Weak signal | Second hand, unnamed ("researchers say"), a blocked capture, or a capture that only partly carries it |
| A2 | Reported | One named party says it, in a capture this desk checked |
| A3 | Echoed | Several outlets say it, but they trace to one origin. Ten outlets restating one headline are one source |
| A4 | Corroborated | Two or more independent parties say it, at least one of them checked in a capture |
| A5 | Confirmed | Two or more independent primary sources say it, each checked in a capture |
| A6 | Established | The authoritative primary record itself carries it (the CVE record, the release tag, the advisory), or this site counted it from a captured file |

### Verdict

`holds` (the evidence carries the statement as worded), `holds-in-part` (it carries a narrower or differently-worded statement; the note says which), `not-shown` (nothing checked carries it, which is not the same as false), `refuted` (a stronger source says otherwise; the level is then the strength of the refutation's absence, and is set to A0).

### Tension

`none`, `measures-differently` (the same word used for a different quantity: websites versus the Internet), `disputed` (sources disagree, no ruling), `contradicted` (a primary source says otherwise), `superseded` (a later capture of the same source changed it). An open contradiction caps the displayed level at A1, a dispute at A2, until a contradiction record marks it explained. That is the brief's rule: a contradiction is an edge that pulls the reading down until it is explained.

### Freshness

Counts and states are volatile. Each assessment records the capture it rests on and its time. A volatile statement whose newest capture is older than 24 hours is flagged stale on the site, and a stale flag on a count is a ticket for the collectors, not a downgrade.

### The display level, and the comfortable view

`display = min(level, cap from tension)`, with `refuted` shown as refuted whatever the number. The site shows the display level as a coloured badge with its code, so the grade never depends on colour alone. "Show me only what I can be very comfortable with" is the view filtered to A5 and A6 with verdict `holds` and no open tension.

## Mode 1: check against the vault (every run)

Assume the vault's captures are what they say they are; the job is whether the site's statements follow from them.

For each statement (the 70 claims first; then numbers, timeline, agencies, impact):
1. Open every cited source's capture in the vault clone: its `text` file first, then the rendered HTML if the text is thin. Record the file path and its sha256 from the source's provenance file.
2. Find the words that carry the statement. Record a verbatim excerpt of at most 25 words, or `absent`.
3. Check every quote in the claim and its note character for character. A quote that is not in the captured text is not a quote.
4. Decide kind, level, verdict, tension. Write the reason in one or two sentences.
5. Compare with the claim's status word. Overstated (status higher than the evidence) or understated is a `finding` ticket.
6. Where two statements on the site disagree with each other (a count on one page, a different count on another), open a `finding` with both locations.

Then the scripted cross-checks: `python3 admin/factcheck/fc.py check` (slugs cited exist, every claim has an assessment, assessments name sources the claim actually cites, quotes in notes are flagged for checking, counts that appear in more than one data file agree).

## Mode 2: go outside (where the evidence is thin)

For statements at A0 to A2, every open contradiction, and every stale count: search the web for better evidence: the party's own page, the primary record, an independent second party, a newer count. What is found is recorded as a `evidence` ticket: URL, retrieval time (UTC), the sha256 of the bytes fetched, a verbatim excerpt of at most 25 words, and what it would change. It is **not** cited on the site, and it does not move a level, until a collector captures it into a vault; that is the house rule for every outside source. The ticket is the request to capture it.

## Tickets, in Issues-FS

The desk's tracker is a full Issues-FS graph in `admin/factcheck/.issues/` (issues-fs-cli 0.3.0, `pip install issues-fs-cli`). Node types:

| Type | Statuses | Opened when |
|---|---|---|
| `finding` | open, acknowledged, fixed, wont-fix, superseded | Something on the site needs changing: an overstated status, a quote not in the capture, two pages that disagree |
| `contradiction` | open, explained, resolved | Two sources disagree about the same measure (mirrors a record in `contradictions.json`) |
| `gap` | open, captured, closed-no-evidence | A statement has no capture that carries it, and the desk could not find one |
| `evidence` | proposed, captured, rejected | Mode 2 found something outside the vault worth capturing |
| `run` | done | One per run, linking everything it opened |

Link types: `opened-by` / `opened` (ticket to run), `contradicts` (symmetric), `supports` / `supported-by` (evidence to finding, gap or contradiction), `supersedes` / `superseded-by`, `blocks` / `blocked-by`, `relates-to`. Every ticket carries `claims` (claim ids), `sources` (vault slugs) and `pages` (site paths) in its properties, so the build can put the ticket next to the thing it is about.

Type names are single words on purpose: issues-fs-cli 0.3.0 builds a label as the type name capitalised plus an index, and its own lookup cannot resolve a label whose type contains a hyphen (a type `evidence-gap` gives `Evidence-Gap-1`, which `issues-fs link` then reports as not found).

Other agents read the tracker; they do not write in it. To close a finding, fix the data in your own file and say so; the next run checks the fix and closes the ticket, or reopens it with why.

## The runbook (what a scheduled run does)

1. `git fetch origin dev factcheck/desk && git checkout -B factcheck/desk origin/factcheck/desk && git merge origin/dev`. Read `AGENTS.md`, `REALITY.md`, the newest brief, and `BRIEF-CORRECTIONS.md`.
2. Clone the evidence vault read-only with the public read key in `data/admin.json` (`sgit clone <read key> <dir>`), and note its head commit. Do the same for any other public vault the claims cite.
3. `python3 admin/factcheck/fc.py check --vault <dir>`: the scripted checks.
4. Mode 1 over every statement whose claim text, sources or status changed since the last run (`fc.py changed`), every statement whose sources gained a capture, and every open ticket. A full sweep at least once a day.
5. Mode 2 over the weak, the contested and the stale.
6. Update `assessments.json` and `contradictions.json`; open, update and close tickets with `fc.py ticket ...`; write `runs/<run>.json`.
7. `python3 admin/factcheck/fc.py export`, then `admin/build/release.sh "factcheck: <what moved and why>"` (with `RELEASE_TRAILER` set to the `Agent: factcheck@php.newsroom` line). The desk publishes to `dev` itself: the editor's explicit instruction of 22 October, recorded in the brief, is the exception AGENTS.md allows. `release.sh` takes in `origin/dev` first, runs the gate and verifies the live site; push `factcheck/desk` too, so the branch matches what shipped.
8. The run is done when the site's statements are either consistent with the evidence or carry an open ticket that says why not. That is the stable state: not "everything is right", but "nothing wrong is unmarked".

## Rules

- Grade the statement as worded, not the story it belongs to.
- Repetition is not corroboration. Trace every echo to its origin.
- Absence of evidence is `not-shown`, not `refuted`.
- An opinion is labelled with whose it is, and its facts are graded underneath it.
- Never raise a level on evidence this desk did not open. Never cite what is not captured.
- Record what was checked (file, sha256) so the next run, or a reader, can repeat the check.
- Highlight, do not fix. The fix belongs to the owner of the data.
