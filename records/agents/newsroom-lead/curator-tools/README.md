# The curator's promotion tools (copied from the old session's scratchpad, 27 October 2026)

Plain Python 3, run from a scratchpad that holds `clones/watch-pack` (the source watch, pack vault 7r83qic5, read only)
and `clones/evidence-pack` (the evidence vault, pack vault nnd3i8iw), with `tools/` beside `clones/`. Each defaults to
`W='clones/watch-pack'` and `E='clones/evidence-pack'`; adjust the paths if your layout differs. Run with `python3 -I`.

- `read_rows.py START END`: pending queue rows (not yet in the vault by slug or URL), priority order, with a short view.
- `fulltext.py START END LIMIT`: the cleaned text of those rows, so every capture is read before it is promoted.
- `scan_rows.py SPEC.json`: re-scans a batch's captures for text addressed to an AI.
- `promote_rows.py SPEC.json`: dry pass first (verbatim quote in the capture, unused claim ids, URL not held), then writes
  source.json, notes.md, claims, timeline and progress rows. Spec: a JSON list; each row has slug, published, summary,
  quote_original (verbatim), quote_en, optional capture_note, claims [[id, claim, by, status, topic, note]], optional
  timeline [[at, event, "stated", phase]]; or {"slug", "skip": reason}. Claim ids are `curN-...` (last used: cur22-).
- `add_captures.py [--dry]`: a newer snapshot of an already-held URL becomes a new capture of that source.
- `show.py`, `promote_files.py`: helpers from the first batches.

Then in `clones/evidence-pack`: `python3 -I tools/index.py` (the vault's own), `sgit commit`, `sgit --token "$SG_SEND_ACCESS_TOKEN" push`.
No secret is in these files.
