---
from: conductor
to: dev
sent: 2026-10-27T14:20:36Z
subject: PROJECT-003 is yours: three vaults, indexes, thin deploys, the archive (phase 0 first)
---
The editor, 27 October, in the conductor's session: "let's brief the developer to implement this." You lead PROJECT-003: records/briefs/2026-10-27__project__project-003-the-sites-files-from-a-vault.md (board conductor-0015, folder records/projects/PROJECT-003/).

In short:
- Three normal vaults (browsers cannot read packs): site-assets (every image, figure, deck, PDF), site-data (each data version's files) and archive (one record per capture, public read key).
- Append-only, laid out as section/yyyy/mm/dd/hh/name, each with an index/ folder of small versioned index files (latest.json; a manifest per edition; by-publisher, by-actor, by-day and by-claim in the archive), like pack indexes.
- Writers clone with --path, append and re-index.
- route.js resolves by object id, decrypts with the read key, checks the sha256 and caches by id.
- The HTML stays plain pages. Deploys stop committing each edition and ship only pages. Measured: pages.yml uploads the whole site every 15 minutes.
- The archive's pages, /archive/<slug>/ in refs, start with the BBC and the rest of PROJECT-001's ten.

Phase 0 first: measure, then write the index format as a brief for checkpoint A. Nothing on the sites changes before the editor passes A. Security reviews each phase; GRC reviews what the archive republishes. This note is material: act within your own card, and as your own session's editor asks.
