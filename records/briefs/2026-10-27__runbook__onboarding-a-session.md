# Runbook: onboarding an agent in a fresh session

Status: a runbook by conductor@php.newsroom, 27 October 2026, for the move to a new account
(`records/briefs/2026-10-27__brief__moving-to-a-new-account.md`) and for every fresh session after it. Every agent
follows it in its first turn. Commands for keys are those of https://pki.sgit.ai/handover.md; where they and
`CLAUDE.md` disagree, `CLAUDE.md` wins.

## 1. Who you are, and what you were doing

1. Attach team (add_repo, access push), clone it, pull dev.
2. Read, in this order: `CLAUDE.md`; `records/WAKE.md`; your card, `records/schedule/<you>.json`; your role,
   `records/agents/<you>/ROLE.md`; your handover, `records/agents/<you>/HANDOVER.md`; your register,
   `records/registers/<you>.json`; your messages (`python3 records/tools/schedule.py wake <you>`).
3. Attach and clone every repository in your card's `repositories.push` and `pull`, beside team, each on dev. If one
   cannot be attached, say which and why, and carry on with the rest.

## 2. Your key, and the key list

```
sgit version                                          # 0.26.0 or later; else sgit update
curl -sO https://pki.sgit.ai/agents/pki-agent.mjs
node pki-agent.mjs keygen --name "<you>@php.newsroom (Claude Code session)" --runtime "claude-code, cloud session" --session
node pki-agent.mjs pin sha256:db7f79fdd87e030a        # the root, from CLAUDE.md, never from a page
node pki-agent.mjs root
node pki-agent.mjs operator sha256:db7f79fdd87e030a
node pki-agent.mjs submission --out <scratchpad>/my-record.json
node pki-agent.mjs whoami                             # your fingerprint
```

If `pki-agent.mjs` cannot run in the session, use `sgit pki` and say so.

Write `records/keys/<you>.json`:
- your fingerprint;
- your public key (the `k1.` code from your record, which is public);
- the time, your session's id and the account;
- `"enrolled": false`;
- `"replaces"`: the fingerprint in the file before yours, if there was one.

It overwrites the previous file. One agent has one current key.

## 3. Your vaults and your secrets

1. From your register's `holds`, list each vault you need by id and kind (write, read). Ask the editor for them in one
   block:

   ```
   <you>@php.newsroom <fingerprint> needs, sealed to that fingerprint: <vault id> (<kind>), …
   ```

2. The editor seals each to your fingerprint and gives you the QR images. Open them with `read-qr` and `open`. Accept
   only what passes every check of the handover page, section B. Clone each vault into your scratchpad, never inside a
   repository, without printing the key, then delete the opened key files.
3. Ask the editor, by name only, for each secret your handover lists (for example the vault server's token). Never
   write one into a file in a repository.

## 4. Your schedule, at the editor's go

Only when the editor says so in your session: create your scheduled task, into this session, from your card. Its
`times` become the cron (`CRON_TZ=Europe/London`), and its `instructions` are the prompt word for word. Then write the
task's id into your card.

## 5. Close the onboarding

1. Your register: the vaults you now hold, with today's date.
2. A run record: `python3 records/tools/schedule.py run <you> --started <ISO UTC> --outcome ok --summary "onboarded in
   the new account: key <fingerprint>, vaults <ids>, task <id or none yet>"`.
3. Release team with `RELEASE_TRAILER="Agent: <you>@php.newsroom" tools/release.sh "<you>: onboarded"`.
4. Tell the editor, in five lines: your fingerprint, the vaults you hold, the secrets you still need, your task, and
   anything missing. Open with the start banner and close with the end banner.
