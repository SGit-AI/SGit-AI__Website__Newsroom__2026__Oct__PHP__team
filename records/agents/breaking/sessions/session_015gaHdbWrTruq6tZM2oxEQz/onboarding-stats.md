# Onboarding stats: breaking@php.newsroom, session session_015gaHdbWrTruq6tZM2oxEQz

By breaking@php.newsroom, 29 October 2026, at the editor's request: how long each stage of joining took, where the time
went, and what could be faster. Every time below is UTC, from file timestamps, `time` output and sgit's own log lines
(`scratchpad/logs/watch.log`, `evidence.log`). A number I could not measure says so. No key appears here.

## Summary

| | |
| --- | --- |
| Session start to registered and pushed | about 1 minute (22:43:46 to about 22:45) |
| Keys opened (QR read, open, signature check) | seconds (22:52) |
| Vault clones, all attempts | 22:53 to 23:16, **about 23 minutes** |
| of which the one clone that worked | 4 min 41 s (23:11:26 to 23:16:07) |
| of which five attempts that did not finish | about 18 minutes thrown away |
| Data actually fetched | watch 44.8 MB of 7,307 MB packed; evidence 1.4 MB of 738 MB |
| sgit | 0.27.0 (PyPI's newest); no release notes found for it (cli.sgit.ai/docs/update-to-0-27-0.md answers 404) |

## Stage by stage

| # | Stage | When | Took | Result |
| --- | --- | --- | --- | --- |
| 1 | Read repo, role, brief, runbooks | 22:43 to 22:44 | about 1 min | |
| 2 | `pki-agent keygen`, `keyqr`, public key file | 22:44:08 | seconds | fingerprint `sha256:fe23fb57187b02f5` |
| 3 | `schedule.py session register`, register, board row, release (gate 1,016 JSON files, 286 pages) | 22:44:19 to about 22:46 | about 1 min | pushed to dev |
| 4 | `pip install sgit-ai` | after the editor's word | seconds | 0.27.0 |
| 5 | Vault keeper's QR zip unpacked, `read-qr`, `open` | 22:52:46 | seconds | 2 keys, `signature: checks`, from the keeper (`956934e47063ceaa`), files mode 600 |
| 6 | Clone attempt 1: `--pack-store`, checkout on, both vaults in a loop | 22:53 to 22:59:19 | 6 min, stopped by me | watch not finished; 2.2 GB memory at about 2 min |
| 7 | Attempt 2: `--pack-store --no-checkout` (the editor's suggestion) | 22:59:30 to about 23:04:40 | 5 min 3 s, killed | 6.2 GB memory, still going; same "Fetching packs (65 pack(s), 6,085.6 MB)" |
| 8 | Attempt 3: `--pack-store --no-checkout --depth 1`, 100 s cap | about 23:05 | 1 min 40 s, killed by the cap | still fetching the 65 packs; user 15.7 s, sys 10.6 s |
| 9 | Attempt 4: `--path index` with a mistyped argument | | 0.3 s | usage error |
| 10 | Attempt 5: `--path index`, watch only, `timeout 280` | about 23:06 to 23:11 | 4 min 40 s, killed by my cap at the last step | pack fetch had finished (277.2 s); the working copy was never written, so the clone was unusable |
| 11 | Attempt 6: `--path index`, both vaults in parallel, no cap | 23:11:26 to 23:16:07 | evidence about 64 s, watch about 281 s | both in sync with the remote |
| 12 | Delete key files, register, release | 23:16 | about 1 min | pushed |

Wall time lost to the failed attempts (6 to 10): about 18 minutes. That is my own doing, below.

## The clone that worked: where its time went

| | watch `7r83qic5` | evidence `nnd3i8iw` |
| --- | --- | --- |
| Packs in the vault | 66 (7,307.3 MB) | 13 (737.8 MB) |
| Fetched (scoped, `--path index`) | 501 objects, 44.8 MB | 142 objects, 1.4 MB |
| Ranged requests | 525 | 127 |
| Pack fetch time | 278.7 s (277.2 s in the earlier attempt) | 59.0 s |
| Time per request | **0.53 s** | **0.46 s** |
| Effective speed | **0.16 MB/s** | 0.02 MB/s |
| Commits walked | 81 | 67 |
| Trees, blobs, checkout | 0.5 s, 0.0 s, 0.0 s | 0.1 s, 0.0 s, 0.0 s |
| CPU (user) | 22.4 s of 280 s | not recorded |

Everything after the fetch took under a second. The fetch is the whole cost, and it is waiting, not working: the process
used 22 s of CPU in 280 s on a 4-core machine, and the time per request (0.5 s) is about the vault host's round-trip time
(one `curl` to `https://dev.send.sgraph.ai/` took 0.69 s to first byte). So a scoped clone costs roughly
(number of requests) x (round trip), whatever the bytes.

## Is it a bandwidth thing? Mostly not, and a full download is no faster

What I could and could not measure:

- **Measured:** a single stream from PyPI ran at about 9 MB/s (362 MB in 40 s). That is a different route (it bypasses the
  agent proxy), so it is only a hint of the environment's size. The proxy blocks the usual speed-test hosts (403), so I
  could not time a bulk download from the vault host itself. **Not measured.**
- **Inferred, not measured:** the full `--pack-store` clone had reached 6.2 GB of memory at 5 minutes, close to the 6.0 GB
  of packs it reported, which suggests the packs download at roughly 20 MB/s, about 5 minutes for the watch vault. At
  9 MB/s it would be about 11 minutes.
- Either way a full download (about 5 to 11 minutes) and the scoped clone (4 min 41 s) take about the same time. The
  scoped clone fetches 135 times fewer bytes yet saves almost nothing, because it is bound by round trips. Your
  expectation (6 GB should download quickly) is right for the full download; the cost is that the full clone holds the
  packs in memory (6.2 GB of this machine's 16 GB, still growing when I killed it), and I did not see it finish.

## Optimisations to try

In order of what I expect them to save. Items 1 to 3 are for the sgit team, so I will put them on a board row for the
conductor to carry; items 4 to 6 are ours.

1. **Fetch the ranges in parallel.** 525 requests at 0.5 s each is 4.7 minutes; 16 at a time is about 20 to 30 seconds,
   and there are 4 idle cores. I believe the fetch is sequential (CPU idle, time per request equals the round trip), but I
   have not read sgit's code, so ask the team to confirm.
2. **Walk fewer commits to find a folder.** The log shows 99 "commits by ranges" fetches of about 1.1 MB each (30 MB of
   the 44.8 MB) for 81 commits, before any tree or blob. A scoped clone that wants only the latest `index` should not need
   the whole commit chain; a head-only or `--depth 1` form of `--path` would skip most of it.
3. **Make a killed clone resumable, or keep a cache across attempts.** Attempts 6 to 10 each started from nothing; the
   packs I had already fetched were not reused. Fetching 277 s of ranges and then losing them to a timeout at the last
   step (attempt 5) is the most expensive thing that happened.
4. **Keep the clone for the next run.** The vaults are cloned into the scratchpad and gone with the container. Whoever
   next runs the desk, or the researcher and the curator, repeats the 5 minutes. A `sgit pull` into a kept clone is
   cheaper; the card already says "clones/watch-pack ... sgit pull". For the breaking desk, where one run is the whole
   session, nothing is saved unless the clone survives between sessions.
5. **Do not clone what the run does not need.** The desk reads and writes the queue (`index`) and a few promoted files, so
   only the watch's `index` is needed; the evidence vault's scope `index` produced an empty working copy, so before the
   curator step I must widen it to the folder the promotion writes (`sgit fetch <folder>`), which will cost its own round
   trips (an estimate: the evidence vault is a tenth of the size, so about a minute).
6. **Start slow commands in the background with a log file from the first try**, and wait on the log. I lost time to caps
   and to a `for` loop that ran the vaults one after the other; in attempt 6 the two ran in parallel and the whole thing
   took as long as the slower one.

## What I did wrong (so it is not repeated)

- I started with a plain `--pack-store` clone of both vaults, although the researcher's and curator's cards, and the
  clone brief, name `--path index` for the watch. Reading the card's `clone_mode` first would have saved about 18 minutes.
- I stopped a clone with `pkill -f`, which killed my own shell; it needed a second run to find that out.
- I capped attempt 5 at 280 s when the previous run had shown the fetch taking 277 s.
- The suggestion `--pack-store --no-checkout` did not help here because the cost is the pack fetch, not the checkout.

## Things the numbers show that the team should know

- The watch vault grew between my attempts: 6,085.6 MB in 65 packs (about 23:05) and 7,307.3 MB in 66 packs (23:11). A
  pack of about 1.2 GB appeared in those minutes, from another writer or a repack, so the full-clone figure is moving.
  I did not look into it.
- Both clones ended "in sync with the remote". Nothing was pushed to either vault.
- sgit 0.27.0 has no release notes at the usual address; the 28 October brief says no notes, no dev version. 0.27.0 is
  PyPI's newest stable release, so I used it and noted it on board `breaking-0003`.

## What I could not measure

Bandwidth from the vault host; the release gate's time; the full clone's finish (I killed it); sgit's own timing log
(`perf/log.tsv`, mentioned in my role) is not in this container.
