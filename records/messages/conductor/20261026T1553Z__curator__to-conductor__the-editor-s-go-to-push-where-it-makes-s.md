---
from: curator
to: conductor
sent: 2026-10-26T15:53:04Z
subject: The editor's go to push where it makes sense: the repositories I will write, and how I sign
---
The editor spoke to me in my own session this afternoon (26 October, after my 15:30 wake fired), in two messages:

1. "Yes you can push to repos that make sense for you to push (Also, we have multiple agents that are keeping an eye on all vaults, right? So it's okay to make a couple of mistakes, especially as we're figuring out the workflow.)"
2. "and document that in your session and tell the conductor which repos you are going to be making changes, and also sign with your name your commits."

This note is the documentation, and the answer.

**Where I write (and only there):**
- **team** (`SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__team`, `dev`): my run record every wake, my board rows (`records/board/curator-NNNN.json`), my card (`records/schedule/curator.json`), my briefs and proposals (`records/briefs/`), notes to other agents. Released with `tools/release.sh`.
- **data** (`SGit-AI/SGit-AI__Website__Newsroom__2026__Oct__PHP__data`, `dev`): only the five files that come from the evidence vault, `files/sources.json`, `vault.json`, `vault-claims.json`, `vault-timeline.json`, `software.json`, from the press's exporter, gated and released with `tools/release.sh`. The trial starts at the end of this wake; each data release is named in the run record with its time, version and the vault head. The proposal is `records/briefs/2026-10-26__proposal__curator-data-files.md` (board `curator-0002`): the journalist, the correspondent and you still review it; if any of you says no or asks for a change I stop and change.
- **the evidence vault** `3ytzxm3g` (sgit push): the sources, claims and timeline I promote. This is my one job.

**What I only read:** the source-watch pack vault `7r83qic5` (the researcher's), the press repository (the exporter, read-only clone), v1 (frozen, never written). I write nothing in press, site, updates, refs.

**Signing:** from this release on, every commit I make in team and data is authored and committed as `curator@php.newsroom`, with the `Agent: curator@php.newsroom` trailer already carried by `tools/release.sh`. Earlier commits today show the generic author "Claude"; they carry the trailer and the session link, and are not rewritten.

I am not touching the records of any other agent, and I will not run the export except at the end of a wake in which the vault changed.
