# The desk's helper scripts

Standard library and playwright only; none holds a key. Kept here because they lived only in the desk's session.

- `findquote.py VAULT_CLONE SLUG "phrase"`: finds a phrase in a source's saved copies (`sources/<slug>/captures/*/text.txt`) in a read-only clone of the evidence vault, and prints the file, its sha256 and the words around it. Run with `python3 -I`.
- `checkquotes.py VAULT_CLONE data/files/outreach.json`: for every request's quoted words, checks the capture's sha256 and that the words are in it character for character, and sets `quote_checked`. It also checks the claims named exist (reads `claims.json` beside the file). Run it before any request is called ready: publishers reword (AWS and CNN did). The file paths in `outreach.json` name captures by the old vault's layout; re-check them against nnd3i8iw (sgit 0.26.0) and re-cite if a hash differs.
- `shot.py URL OUT.png [selector]`: a reader's view of a page, for debriefs and for checking what a page really shows now (the markdown twins are built earlier and can differ from the live page).
