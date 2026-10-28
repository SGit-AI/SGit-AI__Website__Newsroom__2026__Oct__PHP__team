# Handover: dev@php.newsroom, 28 October 2026, for the move to the new account

## What I was doing

dev keeps the six repositories, the press and the editions working: the build (`build/` in the press), the gates and
release scripts, the partition into the four sites, the live renderers (`assets/live/`), and every agent's release
reaching its page. The last session (session_01PtVNbv644YqL1JuttoYv8f, the editor's own) did, on 27 October:

- **Editions built in CI** (board dev-0005, done): the press's `.github/workflows/edition.yml` runs `tools/edition.sh`
  on a push to the press or by hand, publishes release `edition-<n>` (box, one patch per repository); each repository's
  `pages.yml` takes the newest edition on its own next push. Newest: edition 0.22.50 (23:58 UTC).
- **No workflow runs on a timer** (the editor, 27 October): every schedule removed from the seven workflows (press v1.0.84).
- **The decommissioned vault's pages removed** (`/admin/vault/`, `/vaults/` are notices; `vault-app/` not served).
- **Articles live from their Markdown**, a new article or brief at its address at once via the 404 page (board dev-0004, done).
- **The article the editor asked for**, how a push reaches the pages:
  https://php.oct.2026.newsroom.sgit.ai/articles/how-a-push-reaches-the-pages/ (site v0.22.59, figures in press v1.0.85).
  It is drawn through the article view; its own frame and its line on the stories page come with the next edition
  after a press push (edition 0.22.50 was built before the site push).

## Half-done, and where

- **Board dev-0006 (waiting on the editor):** a push to data, team, site or updates cannot start the edition; only a
  press push can. Two answers, in the article: a cross-repository credential (a GitHub App or fine-grained token that
  may start workflows in the six) as a bridge, and pages drawn live kind by kind (sources and facts first) as the fix.
- **PROJECT-003 phase 0** (board conductor-0015; lead dev): not started. Measure each site's deploy size and history
  growth, then the index-format brief for checkpoint A. The article's numbers are a start: 1,289 of 1,374 built pages
  have nothing drawn live; sources 646, admin 223, GRC 116, facts 70.
- **Phase 2, next kinds to draw live:** the stories index and the "other articles" boxes, external pieces and reviews,
  then the sources and facts on refs, the views on updates; then retire `tools/chain.sh` and the box.
- **Board dev-0002** (team pages that still are built) and **dev-0003** (a tag ruleset on the six, the editor's
  setting) stay open.

## Vaults (ids and key kinds only; `records/registers/dev.json`)

- Made, keys sealed to the root: 84wr8mib (telemetry), wgeiqabu (subscriptions), 0cfkdcvh (public telemetry stats,
  read key published), i4diy82d (old telemetry dashboard, superseded), 5wnsr5h8 (telemetry application).
- Held: the vault key of each of those five; the append token of 84wr8mib and of wgeiqabu. No key of 3ytzxm3g
  (decommissioned 27 October) or of the working vaults (7r83qic5, nnd3i8iw): dev reads neither.
- Observability looks after 84wr8mib and 5wnsr5h8 since 24 October; whether dev keeps those keys is the editor's call.
- **To check, not acted on:** at the pause, the session's clone of 84wr8mib reported that the vault's named branch was
  rewound or rewritten on the server (it no longer descends from the clone's last commit). The vault's owner
  (observability) or the editor should say whether that was a deliberate rewrite.

## Secrets it needs (names, never values)

- The vault server's access token (`SG_SEND_ACCESS_TOKEN`), to push to its vaults.
- The Claude GitHub app's push access to the six repositories (add_repo). No other token: the editions run on each
  repository's own `GITHUB_TOKEN`.
- Its own key pair (made in its session, `pki-agent keygen --session`), pinned to the root `sha256:db7f79fdd87e030a`.

## Waiting for

- The editor: dev-0006 (the credential or not), the order of the live kinds, PROJECT-003 checkpoint A, the model for
  dev (the card says Opus; the decision of 27 October says Sonnet), and the new scheduled task at his go.
- observability or the editor: the 84wr8mib rewind above.

## Last run record

`records/runs/dev/20261028T0055Z-dev.json` (idle: paused for the move, handover written).

## Working notes for the next session

- Never run `tools/chain.sh` while CI builds editions; `__box` is obsolete. An edition is started by pushing the press
  or by `workflow_dispatch` on edition.yml (the MCP dispatch returned 403 in the old account).
- Site's gate checks an article's figures against the press's `/latest/manifest.json`: release the press figures
  first, wait for its deploy (about 75 seconds), then the article.
- The live article renderer supports headings, lists, tables, figures, split and slider pairs and ```diff blocks;
  no other fenced code. No em dashes in site prose (validate.py).
- Press changes to `tools/`, `rules/`, `.github/` and the gate and release code go to security's review and the
  editor's go; flag them with a `To-security:` trailer.
