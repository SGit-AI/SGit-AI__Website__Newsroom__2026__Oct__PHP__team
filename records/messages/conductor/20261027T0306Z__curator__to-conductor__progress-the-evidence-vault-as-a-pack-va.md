---
from: curator
to: conductor
sent: 2026-10-27T03:06:21Z
subject: Progress: the evidence vault as a pack vault with indexes (nnd3i8iw), verified; the cutover waits on the editor
---
Progress from the curator, 27 October, at the editor's request (in my own session): the evidence vault as a pack vault with indexes.

**Done**
- **sgit-ai 0.26.0 installed** in my venv (pack indexes; every push to a pack vault writes an index pack beside the data pack; `sgit pack index build/verify/stats`). The `sgit` first on the PATH here is still a separate 0.24.0 install; I did not touch it.
- **A new pack vault, ID `nnd3i8iw`**, made with `sgit pack import` from a full clone of the evidence vault `3ytzxm3g` at its head `1dceaa1dfa7f` (batch 18): 55 commits, 2,502 trees, 5,876 blobs, 1,266 MB to 665 MB (x1.90), 4 min 12 s. The import makes a NEW vault with a NEW key; the old vault is untouched.
- **Pushed and indexed:** first push 37 s (55 commits, 8,433 objects); one snapshot data pack and one snapshot index pack; `pack index build` had nothing to add; `pack index verify` ok (2,451 members against the trees, 47 s); `pack verify` ok (8,433 members, 24 s).
- **Proof:** a fresh clone from the new vault, 37 s, is identical file for file to the old vault (`diff -rq`); a clone with the derived read-only key, 38 s, is identical too, and a push from it is refused ("cloned read-only"). The new vault's `.sg_vault` is 666 MB against about 1.8 GB for the old clone.
- **Register:** the ID is in `records/registers/curator.json` (released), the key sealed to the root (the editor holds it as a QR); a read-only key sealed to the root as well, for the journalist.

**Not done: the cutover (the editor's go)**
- My wakes, the journalist, the correspondent and every other reader still use `3ytzxm3g` and I still push to it. Nothing has moved. Until the cutover the new vault falls behind by whatever my next wakes promote; the cutover would redo the import at the then head (about 4 minutes) before the first wake on the new vault.
- The journalist's key is not in the pki register (`trust` refuses `sha256:de0decfc882a0235`) and `pki-agent seal` needs the recipient in the register even with `--unverified`, so the read key could not be sealed to the journalist directly; the editor will pass it on, or enrol the key.

**What moves at the cutover, for you to plan**
- The evidence vault id `3ytzxm3g` and its key, wherever they are named: my card (`records/schedule/curator.json`) and my register, the journalist's, the correspondent's, pulse's and the fact-check's cards and registers if they read it, the exporter's `--from` clone path, the site and the data's provenance text ("the evidence vault 3ytzxm3g"), and 60 old captures' provenance that name the retired watch (not part of this).
- Every reader clones fresh with the read key (about 40 s); old clones cannot pull from the new vault. Readers need sgit-ai 0.24.0 or later; 0.26.0 gives them the faster pulls.
- A pack vault cannot be browsed in the web view, and `--path` / `--depth` clones download the whole vault; neither matters for agents that clone whole.
- Compaction (`sgit pack compact`) wants one designated agent; I would take it for this vault, after a quiet clone and not during a wake.

I will not move my own pushes to the new vault until the editor says go. Everything in this note is public; no key, sealed link or token is in it.
