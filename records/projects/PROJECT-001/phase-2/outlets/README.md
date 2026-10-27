# Outlet file: the derived data every view of `/outlets/<id>/` reads

By ontologist@php.newsroom, 27 Oct 2026, step 2c of PROJECT-001. Built from data commit
`d64be9551a8c5cc0fbb6843e8d218a94ebe551e1` (data version 0.1.81). Nothing here is sent, committed or released.

## Run

```
D=../sgit-ai__website__newsroom__2026__oct__php__data
C=$(git -C $D rev-parse HEAD); AS=$(git -C $D log -1 --format=%cI)
# an outlet with an actors.json entry
python3 -I build_outlet.py --data $D/files --actor bbc --out bbc.json --data-commit $C --as-of $AS --editorial editorial/bbc.json
python3 -I build_outlet.py --data $D/files --actor huntress --out huntress.json --data-commit $C --as-of $AS
# an outlet inside a wider actor, or with none (CISA sits in `agencies`)
python3 -I build_outlet.py --data $D/files --id cisa --name CISA --party party:cisa \
  --source-slugs cisa-alert-kev-20261026,cisa-alert-log4j-2021,cisa-alert-php-20261021,cisa-ed-22-02-log4j,cisa-home,cisa-kev-catalog,cisa-kev-json \
  --out cisa.json --data-commit $C --as-of $AS
```
Other flags: `--publisher-match <regex>` (sources by publisher field), `--echo-terms a,b`, `--data-version`. Standard
library only, no network, no clock: same data and flags give the same bytes (checked). `editorial/<id>.json` carries the
editor's proposed points and "not asked" by hand; it is optional.

## Contract (top-level keys, all always present; [] or null when empty)
`outlet, as_of, data_version, summary, points, ledger, captures, timeline, graph, echo, not_asked, changes, method`
as in the brief. Additive keys (the designer may ignore them):
- `summary.captures_vault` (captures in the vault; `captures` also counts a raw curl copy), `summary.latest_capture` (for the "older than 24 hours" flag).
- `points[]`: `claim_ids`, `claim_text`, `blocked_by`. Proposed points have `request_id: null`, status `proposed` or `held`; the verdict is the fact-check verdict of the linked claim, not graded here.
- `ledger[].factcheck`: verdict, level, kind, tension, status_fit, as_of, reason, contradictions, tickets, next_step (the desk's "what would settle it").
- `captures[]`: `kind` (vault or raw), `complete`, `flags` (e.g. 24-byte stub), `http_status`; hashes and sizes only, never content.
- `timeline[].sources`; `graph.nodes[]` carry `verdict`/`status` on claims and `own` on the outlet's party and sources.
- `echo[]`: `relation` (primary-source note or secondary) and `note_excerpt` (the sentence that matched), so a reader can check it.
- `method`: data commit, matching rules, terms, counts, limits, point caveats, `injection_seen`.

## Counts
| | bbc | huntress | cisa |
| --- | --- | --- | --- |
| sources / captures (vault + raw) | 1 / 3 + 1 | 1 / 2 | 7 / 7 + 2 raw |
| claims; fact-check verdicts | 12: holds 3, holds-in-part 7, not-shown 1, refuted 1 | 3: holds 2, holds-in-part 1 | 6: holds 5, holds-in-part 1 |
| points (requests) | 4: R-002 drafted, 2 proposed, 1 held | 0 | 0 |
| graph nodes / edges | 43 / 68 | 37 / 44 | 59 / 88 |
| echo found | 20 (all nine named: yes) | 11 | 26 |
Echo mentions are from notes, so for Huntress and CISA they are mostly sources that cite the outlet, not relays; use `relation`.
Injection scan (notes of outlet and echo sources, claims, requests): nothing addressed to an AI found in any of the three.

## Gaps the data cannot fill yet (the briefing's 7)
1. Echo network: the nine are found in notes only; the graph has no edge from any of them to `party:bbc`, and `claims` is empty for all nine (they cite no claim). Researcher: `relays` edges plus the BBC claim each carries.
2. BBC as affected party: Il Sole 24 Ore, startupper, Uzone, VietNamNet are in `echo`; no event or `affected` link exists.
3. BBC sources not held: Radio 4 interview, NSA X-post entry, the technology editor's and cyber correspondent's pieces: only timeline lines, no source rows.
4. Live-page history: three vault captures (08:04-08:06Z) plus the 07:55Z raw; none later; the 12 posts and entry ids are in the vault's `initial-data.json`, not in the data, so `timeline` has no per-post BBC entries and no diff. Librarian/collector: fresh capture, and the posts as data.
5. NCSC quote: no capture before 07:30:02 GMT 22 Oct; point 2 stays held. The fact-check desk's `next_step` names Wayback/archive.today.
6. Parties not modelled: the two editors, technology editor, cyber correspondent are not in `entities.json`.
7. Own inconsistency: claim `no-exploitation` still reads status "reported" while its fact-check is holds-in-part with tension "disputed" (`status_fit` says ok); the words differ, so the page shows both.
Also: the BBC request channel is still "to find" (`outlet.channel.url`, `captured` null); R-013 to R-015 do not exist in outreach.json, so proposed points have no request id; point 1's BBC wording is null because the fact-check found the capture never states a date (`method.points.caveats`).

## Where dev puts it
`files/outlets/<id>.json` in the data repository (a folder, like `wikipedia/`), with a catalogue entry in
`tools/catalogue.json` naming the folder (group as dev decides) and a schema inferred by `tools/schema.py`; served at
`/v/<version>/outlets/<id>.json` and `/latest/outlets/<id>.json`. Regenerate on each release with the commands above
(the generator writes nothing into data itself). Hand-carried input (`editorial/bbc.json`) should become a file in
the data repository or a request in outreach.json once R-013 to R-015 are opened.
