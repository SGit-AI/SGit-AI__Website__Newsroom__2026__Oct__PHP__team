# Handover: pulse@newsroom, for the move to a new account (27 October 2026)

Written by pulse@newsroom in its last turn in the old session (`session_019TV42nt6c1NL6MUTWVvpXG`). Nothing here is a key.

## What Pulse does
**Pulse: exploited vs. talked about.** For 26 tracked CVEs (the 20 KEV additions of 8 to 22 October, php2shell's two as the reference case, and four seen in the newsroom's captures) it keeps two records side by side, never combined (no score, no ranking, no patch advice): the **evidence** as a ladder of eight dated rungs (public PoC, a nuclei template that exploits, a merged Metasploit module, exploitation attempts by a named party, KEV, KEV ransomware flag, a national CERT report of compromises, a named victim), each rung with its capture; and the **attention** (news items, languages, front pages, agency alerts, offline advice). CVSS and EPSS are measurements, not rungs. A pass twice a day (07:22 and 14:52 London) captures about 440 pages, rebuilds `vulns/<CVE>/ladder.json`, `attention.json` and `index/gap.json`, commits and pushes. About 25 minutes; whole-pass 723 to 867 s on sgit 0.25 and 0.26.

## State at the last pass
- Vault `9f5knw9r` (pack mode), head `d2cc04c25606`, pass `20261027T145421Z`, in sync with the server. Last run record: `20261027T1453Z-pulse` (ok).
- **php2shell is on KEV** (catalog 2026.10.26, both CVEs added 2026-10-26, due 2026-10-29, ransomware Unknown): rungs 1, 4, 5 reached; 3, 6 and 8 not. The four named-victim leads (ČVUT, DMM, GMO, Valtec) are recorded in `vulns/CVE-2026-109618/claims.json` as not established or retracted.
- Every other tracked CVE: no change in rungs since 22 October. No tracked CVE has ransomware use Known.

## Half-done, and where
1. **Front-page, agency and offline counts are frozen.** They come from the retired source watch clone (`oq9gflln`, last commit 23 October 16:31 UTC, deleted from the host). The editor suggested reading php2shell's evidence from the site's curated data instead (team/data/refs), and capturing a short list of press homepages for the attention counts. Waits on the editor's go. Code: `tools/pulse_build.py`, `attention_for()`.
2. **Not yet tracked:** the KEV additions of 23 October, CVE-2026-110447 (Collabora) and CVE-2026-114625 (Arista VeloCloud); and CVE-2026-115560 (a third PHP flaw, the desk's board rows 301 and 302), which should be its own row. To add one: a row in `tools/pulse_seed.py`, run it, then the next pass fills it.
3. **Rung 2 (nuclei) is "not checked" for all 26.** Every GitHub search API call (78 of 441 per pass) is refused by the old session's proxy ("not available: sessions are bound to their configured repositories"). The same for the Metasploit and nuclei PR searches. Rung 3 still works from the module index. A new account may allow the API; if not, a source the proxy allows would need the editor's go.
4. **The /pulse/ page on the site is stale.** `export_pulse.py` still reads the retired vault `4klm5qlt`, and `data/files/pulse.json` (data repository) is from the 24 October export. The exporter belongs in the press, which needs security's review; point it at `9f5knw9r`, public read key in the vault's README. The correspondent's register still lists `4klm5qlt`.
5. **The en-US news count cannot say a feed was blocked,** so a blocked feed reads as a drop. Fix in `pulse_build.py`.
6. **Updates:** the editor suggested Pulse publish updates in the `updates` repository. It is not in Pulse's policy, and not attached: needs the editor's go and a scope change (librarian / abp).

## Vaults, by id and key kind (never a key)
- `9f5knw9r` vault key: Pulse's vault (pack mode, sgit-ai 0.26.0 or later; `sgit clone`, never clone-branch or clone-range). Its key is sealed to the root, and to the vault-of-vaults keeper `sha256:956934e47063ceaa`; the editor holds the images.
- `4klm5qlt` vault key: the retired first vault; nothing is written to it.
- `oq9gflln` read key (public): the retired source watch; not used.
- Team and data are repositories, not vaults. Pulse writes team (`records/`) and, once the exporter moves, data (`files/pulse.json`); never v1 (frozen).

## Secrets it needs, by name
The SG/Send access token for `dev.send.sgraph.ai`, from the editor (first push of a clone; sgit saves it in that clone's `.sg_vault/local`). Nothing else: no API key, and the checks use no credentials.

## To restart in the new account
1. Follow the onboarding runbook (`records/briefs/2026-10-27__runbook__onboarding-a-session.md`). `pip3 install sgit-ai --break-system-packages`; `sgit version` 0.26.0 or later.
2. Make a key pair (`pki-agent keygen --session`, pin `sha256:db7f79fdd87e030a`); write its public key to `records/keys/pulse.json`. Ask the editor to seal `9f5knw9r`'s key to it.
3. `sgit clone <key> ~/vault/pulse` (the card's steps use that path). Chromium is at `/opt/pw-browsers`; do not run `playwright install`. The tools are Python standard library plus `node tools/capture_batch.mjs`.
4. `pulse_seed.py` reads the news editions from a watch clone, but the 3,836 news pages already exist in the vault: do not re-seed unless adding a CVE (then point `PULSE_WATCH` at any clone that has `sources/us/aggregator/`, or add the rows by hand).
5. Run one pass by hand (`python3 tools/pulse_pass.py --news 170`), then, at the editor's go, create the two scheduled tasks from the card (`times`, `instructions` word for word) and put their ids in the card.

## Waits for, from whom
The editor: the decisions in items 1, 2, 3 and 6; the new key's vault seal. The press and security: item 4. The librarian: the register row on the site's `/team/vaults/` (this register now exists in team). Nothing waits on Pulse.
