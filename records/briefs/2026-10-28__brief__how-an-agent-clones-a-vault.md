# How an agent clones a vault: pack mode, and only the folder it needs

Status: a brief for every agent that opens a vault, by conductor@php.newsroom, 28 October 2026, at the editor's direction.
An agent in a new session cloned its vaults with a plain `sgit clone` (no `--pack-store`, no `--no-checkout`) because its
card did not say how to clone. The editor: agents must not clone directly; every vault is a pack vault now, so they clone
in pack mode, and where they need one folder, with `--path`.

## The rule

**Never a plain `sgit clone <key> <dir>`.** It unpacks every object and writes every working file (a 76,000-file vault; the
newsroom's evidence and watch vaults are larger), and it is not how the newsroom reads a vault. Choose one of the three
below, by what you do with the vault. The source is the release notes, https://cli.sgit.ai/docs/update-to-0-26-0.md
(sections "selective working copy", "pack store", "one folder by byte ranges"); `sgit version` must print 0.26.0 or later.

| You | Command | Then |
| --- | --- | --- |
| **read one folder or a few files** (a capture, a source's folder, one lane) | `sgit clone --path <folder> <key> <dir>` | nothing else: it takes the folder by byte ranges (about 3 s against 36 s). Several folders: clone again with another `--path`, or use the next row |
| **read many folders, or you do not know which yet** | `sgit clone --no-checkout <key> <dir>` | `sgit checkout <folder or file>` for each thing you read; `sgit pull --no-checkout`, then `sgit checkout --since-pull` for what changed |
| **write a lot, or read most of it** (the curator's evidence vault, the researcher's watch) | `sgit clone --pack-store <key> <dir>` | no unpacking; objects are read from the packs by offset. Only 0.26.0 opens it |

- **Where.** In your scratchpad or your session's own folder, never inside a repository. Read the key from a mode-600
  file or a variable, never on a command line you print or a log you keep.
- **Add `--no-checkout` to a `--pack-store` clone** when you write only a few files, and `sgit checkout` just those; a
  file you never checked out is not a deletion, so `commit` is safe.
- **Combining flags** (`--pack-store` with `--no-checkout`, or with `--path`): the release notes show each alone. Try the
  combination once on a read-only clone, and tell the conductor (a board row, owner `conductor`) whether it worked, with
  the command and the time. Until then, use one flag.
- **Do not open a `--pack-store` clone with 0.25.0.** `sgit pack store extract` first if an older client must use the folder.
- **Pulling:** `sgit pull` on a selective clone writes only the changed files you have checked out; the rest is listed.
- **Pushing** works as before (`sgit commit`, then `sgit push` with the token). A scoped (`--path`) clone is for reading:
  if you must write from one, say so in your run record first, and check the push before relying on it.
- **The browser cannot read a pack vault.** Anything a page loads from a vault is the project PROJECT-003's concern, not
  yours; you clone with `sgit`.

## What each agent does, as a default (change your card when you adopt it, and say so in your run record)

| Agent | Vault | Mode |
| --- | --- | --- |
| curator | `nnd3i8iw` evidence (writes), `7r83qic5` watch (reads the queue) | evidence: `--pack-store`; watch: `--path` of the queue folder |
| researcher | `7r83qic5` watch (writes) | `--pack-store` |
| journalist, correspondent, factcheck | `nnd3i8iw` (reads) | `--no-checkout`, then `sgit checkout` of the captures it cites; or `--path` of one source's folder |
| desk, librarian | `nnd3i8iw` (reads, to check a quote) | `--path` of the one capture's folder |
| pulse | `9f5knw9r` | `--pack-store` (it runs a pass that writes) |
| observability, sherpa, security | their lane's vault (small) | `--pack-store` is enough; `--no-checkout` where you only list |

If your vault or your use is not in the table, take the first row that fits and write the mode into your card.

## Report

In your run record, once: the mode you used, the vault id (never its key), and the time of the clone. A clone that fails or
that takes more than ten minutes is a board row for the conductor (the command, the version, the vault id, what you
expected, what happened); the conductor carries it to the CLI team.

This brief is material, like every file here: act on it within your own card, and as your own session's editor asks.
