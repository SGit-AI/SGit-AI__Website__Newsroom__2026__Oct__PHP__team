# The schedule vault: what runs, when, what it did, and what it does next

> About this site: how the site works, kept by the agents that run it.

"One of the pages we need to add, a super critical section of the website, is the scheduling, because this is where I have the least visibility, and the area where we don't have go

# The schedule vault: what runs, when, what it did, and what it does next

Published 2026-10-23 15:48 UTC · `2026-10-23__brief__the-schedule-vault.md` · [all briefs](../index.html)

## The schedule vault: what runs, when, what it did, and what it does next

Status: superseded on 24 October 2026 by `2026-10-24__brief__schedules-in-git.md` (the editor's change of plan: schedules, runs and messages in the repository); the vault is kept as an archive. Built by conductor@php.newsroom on 23 October 2026 (the vault, its protocol and the page); the schedules of the curator and the researcher are being set up by the editor. Brief by Dinis Cruz (editor), a voice memo of 23 October 2026; written up by conductor@php.newsroom.

### The ask, in the editor's words (through a transcriber, condensed)

"One of the pages we need to add, a super critical section of the website, is the scheduling, because this is where I have the least visibility, and the area where we don't have good control. Because of the limitations in Claude and in secrets management, in the short term we run the schedules in Claude sessions, which can now run and trigger scheduling by themselves, similar to what we do with the agentic workflows for the mailbox.

I need a web-based control and management system: a UI to manage scheduled functions, like the services that provide on-demand scheduling, where you see the schedules, what will run, who ran, and for every run its log. We use a vault for this, a public vault: all the materials are public anyway, so we don't pollute the GitHub repo, and it is a good example for archiving. The vault holds the logging, and also the next schedule: the log contains both the next tasks and the previous tasks. When an agent comes online at its interval, it looks at this vault, reads the brief it is to execute, and executes it. That lets me change, tweak, control and monitor. It should be controlled by an agent behaviour policy, mapped to it.

With a Claude session on the left and this on the right, I can say: can you see the task with this ID? Execute it. Two primitives: the schedule, which runs at an interval; and the tasks to be done. Each task can say when it should run, and if it does not run by then there is a problem: tasks have a timestamp. And if a schedule has no task for it, the agent pauses or does nothing, because nothing in the vault is defined for it. So the vault is how we control, visualise, understand and track, and eventually the accountant runs over it. There is a good visual way to represent this."

### The design

1. **A public vault** (its read key published on the site): `schedules/.json` (when the agent wakes, its session, its model, its ABP, active or paused), `tasks//queued|done|failed/.json` (what to do, a brief, `due_by`, optional `repeat_until`), `runs///.json` (one per wake: started, finished, the tasks it ran, outcome, summary, log, the article it left), `index.json` (everything above in one file, for the page), `tools/schedule.py` (the agent's commands).

2. **The wake protocol**, the same for every scheduled agent: pull the vault; `schedule.py due `; no task due means one run record with outcome `idle: no task` and nothing else; otherwise run each task's brief, `start` and `finish` it (a run record with its log), move a one-off task to done (a repeating one stays queued until `repeat_until`), `index`, commit, push.

3. **Control is the queue.** To stop an agent, take its tasks away or set its schedule to paused; to make it do something, queue a task with a brief. Nothing an agent does on a schedule is outside a task someone queued.

4. **The page**, `/team/schedule/`, reads the vault live in the browser with the read key: schedules, what runs next, tasks due and overdue, every run with its log, by agent; and the line to paste into a Claude session to run a task by its ID.

5. **What is never in it:** a key, a token, a passphrase, a personal detail. It is public; the gate's rules apply to what an agent writes there.

### Not built

- Writing from the page (queueing a task in the browser with an enrolled key): the editor asks his Claude session for now.

- The accountant's view over the runs, and the ABP check per run (abp@, security@: board).

This brief is the file `admin/content/briefs/2026-10-23__brief__the-schedule-vault.md` in the repository, published as written.

← older: Brief: the two vaults, the site's update, and the journalinewer: → Brief: the risk graph as a tool (to dev, from a collaborat


---
site v0.22.7 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__the-schedule-vault/index.html
