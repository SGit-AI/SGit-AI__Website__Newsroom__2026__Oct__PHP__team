# Handover: conductor@php.newsroom, 28 October 2026, for the move to the new account

## What I was doing

The conductor keeps the newsroom running: the review of the six repositories, the schedules against the cards and the
run records, the status records, the projects and the editor's briefs. Since 24 October it woke hourly, and from
27 October 18:58 UTC four times a day (07:15, 11:15, 15:15, 19:15 London). Its schedule was paused at about 00:50 UTC
on 28 October, with every other agent's, for the move.

## State at the pause

- **Projects** (folders in `records/projects/`, briefs in `records/briefs/`):
  - PROJECT-001 (outreach, lead: the Sherpa), at checkpoint B: three drafts (BBC, the PHP security team, the PHP
    Foundation), reviewed by the desk. Passed by the editor: checkpoint A.
  - PROJECT-002 (the corrections we propose, lead: the liaison, who has no session): phase 1 steps done; waits on the
    journalist's review of fact-check's re-grade, then checkpoint A.
  - PROJECT-003 (the sites' static files and an archive in vaults, lead: dev): open, phase 0 not started.
- **The runbooks I wrote:** the breaking desk, the projects desk, onboarding a session, the move. The wake banners
  (`schedule.py banner start|end`) are in WAKE.md steps 0 and 6.
- **Open board rows of mine** (`records/board/conductor-*.json`):
  - 0005 and 0006: the `/breaking/` section (story-site, dev);
  - 0007: the press names the old evidence vault;
  - 0009: deleting `3ytzxm3g` (the editor does it himself);
  - 0011: the exporter checks the sgit version;
  - 0014: a page per project;
  - 0015: PROJECT-003;
  - 0016: the move.

## Vaults

Made and held (a register in `records/registers/conductor.json`): 5iwos28w, zjruy9vk, fmb2tpl2, 58526ytp, weic8imn. All
are listed with their kinds there; weic8imn (the schedule vault) is retired. The conductor reads none of the working
vaults. IDs only here, never a key.

## Secrets

None of its own. It needs the Claude GitHub app's access to the six repositories, and, to change other agents' scheduled
tasks, nothing: a task is changed from the session it fires into (only its pause is possible from here).

## Waiting for

- The editor: the move itself (each agent's new session, its key sealed vault keys, its scheduled task at his go).
- dev: why GitHub's own timers never fired (the editor then decided that no workflow runs on a timer, 27 October), and
  PROJECT-003.

## Working notes for the next session

- **Each wake:** take in dev; `python3 records/tools/schedule.py wake conductor`; review every commit of the six;
  check each scheduled task against its card (`list_triggers`) and each wake against a run record; a full pass reads
  every session read-only; the run record and one release; then the report, opened and closed with the banners.
- **The wake tool** is `records/tools/schedule.py`. Its secret check once took "desk-onboarded" in a message id for
  an API key: fixed. A refusal no longer leaves an empty file.
- **Quote what an agent said in reported speech** in any brief: text addressed to an agent tripped the press's injection
  gate once.
- **Never put a key fingerprint in a run record:** the team gate refuses it.
- **A task fired from another session** starts an empty session, not the agent's own: it cannot start an agent.
- **The editor's rules:** only he instructs in his own session; he sends every message to anyone outside; Opus for the
  conductor, the correspondent and security, Sonnet for the rest; no caps on telemetry; every vault a pack vault
  except the three planned for browsers (PROJECT-003).
