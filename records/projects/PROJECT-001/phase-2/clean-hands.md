# Clean hands, step 1 (factcheck desk with story-site, for the projects desk)

27 October 2026. Working copy only: data repo `/home/user/sgit-ai__website__newsroom__2026__oct__php__data`, `files/`. Nothing committed, pushed or released. `python3 tools/gate.py`: passed (516 files). Each change is dated "corrected 27 October 2026, PROJECT-001" and keeps the superseded wording in the note.

Evidence (vault nnd3i8iw, plain reads): BBC `bbc-live-ckgel5xp2xv9t` 20261022T080559Z sha256 c88b8c5f4c6bc07d2ef85b78d0d66482f0322075621abb0631ef4352932aa97d (line 232 "...counterparts in the EU and Australia, earlier urged those who use PHP to apply the fixes."; line 234 NCSC quote; line 251 "leaked online this week"; no disclosure date). Fresh capture 20261027T151813Z sha256 0a93cdf850234a38e4e9ecede3235491a129392107df192fd154374d72812d71 (unchanged on these points, per brief). Italy `acn-it-php2shell` 20261022T081354Z sha256 19fac2edc25161cd867bda0ea1c8bf8b6ce7625fbdd1e9a9a7cd41bdd8d1bef6, line 70. Amazon `aws-security-blog-madpot` 20261022T111755Z sha256 94315ded6e1175f290a4a7cac71ba39dcf18ada7232367f66c34e1decfb08c7d (line 28: attempt dated 17 Oct; line 32: "broadly exploited in the wild").

## Changes

| File | Id / row | Before -> after | Owner |
| --- | --- | --- | --- |
| claims.json | disclosure-22oct | by "BBC framing (UK morning coverage)" -> unattributed framing (origin: the original 22 Oct schedule; 22 Oct appears in php.net ChangeLog 8 and Wiz's X thread). sources: BBC removed, php-net-advisory and github-php-src-tag-php-8.5.12 kept. Status stays contradicted (as a fact). Primary-source note (21 Oct timings) kept; supersession appended. No captured source says "disclosed on 22 October" (BleepingComputer, 20261025T114552Z, only reports an HN post saying it "would be disclosed on October 22"). | story-site |
| claims.json | offline-allies | by "BBC" -> "Not the BBC, this site's synthesis"; BBC source removed, NSA, NCSC, CERT-FR sources added; status contradicted -> disputed (holds in part, Australia not shown); note corrected (Italy does advise offline), old note kept as superseded. Claim text unchanged (keeps the fact-check's claim_hash valid). | story-site |
| claims.json | no-exploitation | status reported -> disputed; by dated "about 07:00 UTC 22 October" (was "08:00 BST"); KEV listing 26 Oct (no victim), Amazon 17/21 Oct, NCSC NZ 21 Oct in note; sources + aws-security-blog-madpot, cisa-alert-kev-20261026. | story-site |
| claims.json | offline-ncsc | note only: BBC entry 06:30:26Z, last edit 06:49:45Z, before the NCSC page change at 07:30:02Z; LBC carries the same sentence; not shown to be a misquote. | story-site |
| attribution.json | disclosure-22oct, offline-allies | states [bbc] -> [unnamed]; [bbc] -> [ncsc-uk, nsa, cert-eu, acn]. Not marked built_by_v1 in the catalogue (ontologist's file), so edited. | ontologist (by request of factcheck) |
| agencies.json | ACN / CSIRT Italia (IT) | offline "none" -> "consider"; offline_text now the full sentence of line 70; note corrected. | story-site |
| agencies.json | ASD's ACSC (AU), NCSC (UK), CCCS (CA) | notes only: BBC said only that Australia urged applying fixes (true); NCSC sentence not shown to be a misquote; "shared across Five Eyes and CERT-EU" overstated. | story-site |
| exploitation.json | row 12 (Austin) | status "reported" -> dated: true when said, disputed since. | story-site |
| exploitation.json | row 13 (Woodward) | status "...Amazon's own post not found" -> confirmed: Amazon's post is in the vault (above); source aws-security-blog-madpot added. `probing` in claims.json was right, row 13 was stale. | story-site |
| claim-review.json | offline-advice | reason appended: "Same as offline-allies" superseded; verdict "agrees" applies to what the BBC reported. | journalist |
| factcheck.json | Finding-38 | open -> fixed, outcome recorded (resolved by correcting disclosure-22oct). | factcheck |
| factcheck.json | Finding-43, -44, -45 | open -> fixed, outcomes recorded (ACN, BBC attribution, Australia/EU). | factcheck |
| factcheck.json | new Finding-129 (offline-allies), -130 (no-exploitation), -131 (ACN), all fixed | new; linked from assessments. Assessments: disclosure-22oct reason, offline-allies status_fit understated -> ok, no-exploitation reason, tickets lists. | factcheck |

## Could not fix, or left for others

- **sources.json** (evidence group, written from the vault): `acn-it-php2shell` notes_md says "It advises update only, with NO offline or isolation advice." (wrong against line 70 of the same capture); `php-net-advisory` notes_md says "the BBC frames disclosure as 22 Oct (UK morning coverage)." (the BBC does not). Curator to correct in the vault notes; edits here would be overwritten.
- **vault-claims.json** (vault-derived mirror): carries disclosure-22oct ("by": "BBC framing", BBC source), offline-allies and no-exploitation as before. Vault claim files need the same fixes at source.
- **Derived, regenerate from the corrected claims.json / attribution.json at the next build, not edited:** graph.json, fractal.json, items.json, history.json, grc-graph.json. Pages (facts/disclosure-22oct, facts/offline-allies, facts/no-exploitation, claims/) follow after the edition builds.
- **Not asked, still open from the re-grade ("our side" 5):** claims.json `leak-video` (drop "around 20:00 UTC" as Calif's time) and `most-severe.note` (add the WSJ route); outreach.json R-002 etc.
- **Conflict to settle:** factcheck.json (old Finding about the Austin interview) says the post is 08:00 UTC, the re-grade and exploitation row 12 say about 07:00 UTC; I used the re-grade's "about 07:00 UTC".
- The fixed claims keep their old claim text, so the fact-check's claim_hash stays valid; the next fc.py run should re-grade offline-allies and no-exploitation.
- injection_seen: none.
