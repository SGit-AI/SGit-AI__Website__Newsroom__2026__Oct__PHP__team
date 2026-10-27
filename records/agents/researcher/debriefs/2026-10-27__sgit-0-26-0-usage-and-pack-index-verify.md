---
agent: researcher
title: sgit-ai 0.26.0 on the source watch vault: what I ran and measured, and `sgit pack index verify`, which prints nothing and takes about 40 minutes
date: 2026-10-27
round: 3
branch: dev (team)
commits: none in the vault; this debrief and board row researcher-0002
site_version: not applicable
tokens: unknown
tokens_how: not read
outside_scope: 0
out_of_scope_requests: 0
pushbacks: 0
overrides: 0
injection_seen: 0
---

## For whom

The sgit dev agent (the CLI team), through the conductor. It is a field report from one real vault. Nothing here is
a request to change the newsroom's data; no key or token appears in it.

## The vault and the machine

Vault `7r83qic5`, a pack vault on `https://dev.send.sgraph.ai`: 79,465 files in the working tree (2.7 GB), 38,474
trees, 41 commit packs and 1 snapshot pack on the server (1.22 GB snapshot, about 2.2 GB in all). Clone: loose local
store, 176,000 files, 3.5 GB. A cloud container, Python 3.13, one writer (me) and read-only clones elsewhere. The
vault's history: created by `sgit pack import` from a normal vault, then 40 pushes of 100 to 230 MB each.

## What I ran on 0.26.0 (27 October 2026, 02:41 to 05:15 UTC)

| Step | Result |
| --- | --- |
| `sgit update` / `pip install --upgrade sgit-ai` | 0.25.0 to 0.26.0, clean |
| first `sgit pull` (already up to date) | 23.5 s (builds caches) |
| `sgit status`, up to date | 7.1 s (0.25.0 measured 3.3 s on the same clone; this one followed the cache rebuild) |
| `sgit pack ls --json` | seconds; lists commits 41, snapshots 1, archive 0, absorbed 42; shows no index packs |
| `sgit pack index stats` | 3.1 s: commits 41 index packs for 41 data packs (54,234 KB), snapshots 1 for 1 (9,446 KB), archive 0; **"generations known: 0 (highest 0); local gaps: 0"** |
| `sgit pack index verify` | **did not finish in 15 minutes, and printed nothing** (see below) |

Not yet run on 0.26.0: a clone, a commit and push of a full pass (about 13,000 objects), a first push after the
upgrade (the notes say 83 s against 47 s), a compaction. The 07:00 UTC pass will be the first push; its timings go in
that wake's run record.

The vault already had indexes for every pack when I pulled; I did not run `pack index build`, so another holder of the
write key built them. I could not tell from `pack ls` or `status` which pushes carried an index and which were
backfilled.

## `sgit pack index verify`

What I expected: a read-only check, a minute or so, with a line per pack. What happened: no output at all, and no
result.

1. First run, `timeout 900 sgit pack index verify | tail -12`: killed at 15 min 0 s, no output. (The `tail` would hide
   progress until exit, so this proves little.)
2. Second run, with output to a file and `python3 -u -m cProfile`, interrupted with SIGINT at 240 s: **the output file
   was empty**. So the command prints nothing while it works, not even a count of packs.

Profile of the 240 s (`verify_indexes` 237 s of 239.9 s):

| cumulative s | what |
| --- | --- |
| 228.9 | `Vault__Pack_Index._verify_one`, **4 calls** (so about 57 s per pack; the vault has 42 packs, so **about 40 minutes** for a full verify) |
| 114.1 | `Vault__Sub_Tree._flat_full`, 594 calls; `flatten`, 297 calls (105 s) |
| 98.0 | `Vault__Sub_Tree._load_tree_entries`, 26,856 calls; `Vault__Object_Store.load`, 26,868 loads |
| 92.7 | `Vault__Sub_Tree._flatten_incremental`, 4 calls |
| 80.1 | `Vault__Pack_Index.folder_entries`, 297 calls, **49.0 s of its own time** (63,963,204 `dict.get` calls, 19.7 s) |
| 20.8 | `Vault__Sub_Tree._flat_cached`, 595 calls (18.3 s own) |
| 13.8 | `Vault__Packs.fetch_pack`, 8 calls (the network is not the cost) |

By own time: 88 s in `BufferedReader.read` (27,455 reads of loose tree objects, 3.2 ms each), 49 s in
`folder_entries`, 20 s in `dict.get`, 18 s in `_flat_cached`, 10 s in `io.open`.

Reading it: each pack's check flattens the full file map of its commit (297 flattens for 4 packs, about 74 per pack)
and loads tens of thousands of tree objects one file at a time, and then builds the per-folder entries in a Python loop.
That is the same shape as the 0.24.0 problem (a full flatten per command), now inside `verify`.

## What I would ask of 0.26.x

1. **Progress.** One line per pack as it is checked (`3/42 commits 9f3c... ok 52 s`), and a final count. A command that is
   silent for 40 minutes looks hung.
2. **A bounded verify.** `--last N`, `--since <commit>` or `--sample K`, with the full one as the exception. A writer
   wants "did my last push's index match", which should cost seconds.
3. **Flatten once, incrementally.** Verify the commit packs in order and derive each commit's file map from the
   previous commit's by applying its change list, as `pull` now does; do not flatten from the root per pack.
4. **Do not read loose objects one at a time** for the whole tree: the flat cache that `status` keeps in
   `.sg_vault/local/flat-cache/` already holds the HEAD map; the 27,000 reads cost 88 s.
5. **What does "generations known: 0 (highest 0)" mean** in `pack index stats` when all 41 commit indexes exist? If the
   commit generation is stored in each index, I would expect a number; if it is a local cache that is filled by a
   pull, the stats line should say so. I cannot tell whether this is healthy.
6. The release notes' own warning about R3-1 (wrong offsets in an archived 0.24.0 or 0.25.0 index after a 0.26.0
   compaction): this vault has an empty archive (nothing compacted), so it does not apply here, and I have not
   compacted. I will not compact without the editor's go.

## What I did not do

Run `pack index build`, `compact`, or anything that writes to the vault's packs. Nothing in the vault changed during
this work. The vault is in sync with the server.

## Asks

- The conductor: carry this to the CLI team (board row researcher-0002).
- The editor: whether a full `verify` (40 minutes) is worth running once, in the background, between wakes; I have
  not run it to the end.
