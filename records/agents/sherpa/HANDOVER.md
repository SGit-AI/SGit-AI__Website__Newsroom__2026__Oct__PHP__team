# Handover: the Sherpa (sherpa@php.newsroom), 27 October 2026

Written in the old account's session (`session_011Lh927SsvmNuc6chyy3LaS`) before the move. Read with the card
(`records/schedule/sherpa.json`), `ROLE.md`, `records/sherpa/README.md` and the register (`records/registers/sherpa.json`).
No key or token is written here.

## What I was doing

The readers' side of the site: draining the collaborators' lane and my inbox lane every two hours, recording what readers
send (`records/sherpa/feedback.json`, UF-001 to UF-007), the friction log (`friction-log.json`, F001 to F040), the
collaborators' ideas (CI-001 to CI-003), briefs to the owners, and the live phone-width walks at 11:45 and 17:45. Since 25
October also: the interviews and outreach brief (`records/briefs/2026-10-25__brief__interviews-and-outreach.md`, board 331
to 334), the page and brief for a reader's own assistant (`/sherpa/for-your-claude/`, press v1.0.56), and a read-only review
of PROJECT-001 phase 1 (in my run record `20261027T1401Z-sherpa`).

## Half-done, and where

- **The 17:45 full pass of 27 October was not run** (the schedule paused at 16:51 UTC). The first wake in the new account
  should do a full pass: read everything released since the 11:45 pass (run `20261027T1149Z-sherpa`), walk the front page,
  `/on/<date>/`, `/start/`, `/agencies/`, `/feedback/`, `/sherpa/for-your-claude/` at 390px.
- **Open frictions the owners have not answered:** F037 (front page headline 792px down on a first visit), F038 ('Your
  reading' above every headline), F039 (the 'is live: reload' line makes the sticky header 80px), F040 (/on/<date>/ answers
  404 to anything that does not run the page's script). All in `friction-log.json`, owner story-site (also dev).
- **`records/sherpa/make_inbox.py`**: makes an inbox vault with an append lane (the postmaster convention). Path patched for
  the split on 27 October, not run since: run it only at the editor's go.
- **Board rows still open that are mine:** 122 to 125, 192 to 194, 196, 197, 264 (old v1 rows: most are stale or answered
  by what shipped; triage them), 334 (waiting on the editor's choice of the interview first wave), `conductor-0012`
  (PROJECT-001: the projects desk runs it; I reviewed phase 1 read-only).

## Vaults I read or write (by id; keys never here)

| Vault | What | Key kind | How I hold it |
| --- | --- | --- | --- |
| 58526ytp | the collaborators' lane (the site's feedback form writes to it, encrypted in the reader's browser) | vault key | from the editor, sealed; a clone in my scratchpad, outside every repository |
| d6zak0o3 | my inbox lane (senders: riskmandate, editor; recipient fingerprint sha256:3b964d5e3abf03c0) | vault key | I made it; its key is sealed to the root (24 October); a clone in my scratchpad |

Everything the lanes need (the enum key, the passphrase, the key pair that decrypts what arrives) is derived from the vault
key or kept inside the vault (`build/postmaster.py` in the press): the vault key is the whole boundary.

## Secrets I need, by name

- **The vault server token** (`SG_SEND_ACCESS_TOKEN`), to commit and push the two vault clones.
- **The vault key of 58526ytp** and **the vault key of d6zak0o3**, each sealed by the editor to my new key.
- Nothing else. My own `pki-agent` key pair (`sha256:2de83f17e539954f`) dies with this session: make a new one, pin the root
  `sha256:db7f79fdd87e030a` from CLAUDE.md, and write `records/keys/sherpa.json`.

## How a wake runs (so the new session does not rediscover it)

1. `git merge --ff-only origin/dev` in team and the press; `python3 records/tools/schedule.py wake sherpa`; start banner.
2. Clone the data repository's `files/contributors.json` to a scratch folder and set `NEWSROOM_DATA_FILES` to it; run the
   press's `build/collaborators_drain.py --vault <clone of 58526ytp>` and `build/conductor_drain.py --vault <clone of d6zak0o3>
   --fingerprint sha256:3b964d5e3abf03c0`. The Sherpa does not write the data repository: an enrolment that changes the
   copy goes to the editor and the conductor, who keep the file.
3. `sgit commit` and `sgit push` the collaborators clone if anything was drained (the inbox clone too).
4. New feedback becomes `UF-nnn` in `records/sherpa/feedback.json` only if it may be published (the editor's word, or the
   sender's consent); a join request is never published. Check each point in Chromium on the live site.
5. Run record (`schedule.py run sherpa`), release with `tools/release.sh` (`RELEASE_TRAILER="Agent: sherpa@php.newsroom"`),
   end banner.

## What I wait for, and from whom

- **The editor:** the first wave of interviews and their formats (board 331); PROJECT-001 checkpoint A (the ten names, and my
  answers to his five questions in run `20261027T1401Z-sherpa`); a power-user invitation for the collaborator of CI-001 to
  CI-003; the subscriptions lane key (wgeiqabu) if the Sherpa is to monitor it; re-sealing the `riskmandate` token to the
  RiskMandate agent's own key; whether the collaborators vault's signed messages may be published; the consent checkbox on
  the feedback form.
- **Dev:** `sherpa-0001` is done (press v1.0.41); F039 and F040 with story-site; a generic 'plain pages' area (my proposal in
  the 27 October session, not yet a board row).
- **The conductor:** the notes that ask me to file project feedback under `records/projects/` are outside my write scope; I
  have not acted on them. The editor decides.

## The old scheduled task

`trig_01Jq9e42ZLsawRCoJnLyvydp` ('Sherpa: drain the lanes, and the twice-daily pass'), every two hours at :45 from 07:45 to
21:45 London, bound to the old session, paused at 16:51 UTC on 27 October. In the new account create it again from the
card's `times` and `instructions`, word for word, at the editor's go, and record the new id in the card.

## Last run record

`records/runs/sherpa/20261027T1557Z-sherpa.json` (idle, the 15:45 wake) and the handover's own, `20261027T1700Z-sherpa`.
