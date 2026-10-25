# Commit-FS-lite: agents talk to each other in the commits they already write

Status: built by conductor@php.newsroom on 24 October 2026. Brief by Dinis Cruz (editor), in the conductor's session of 24 October 2026; written up by conductor@php.newsroom.

## The ask, in the editor's words (condensed)

"Capture the guidance that the agents should be using git commit messages to communicate. It's almost like what we were doing with Email-FS, but for now, to prevent a massive explosion of messages, and to keep track, because every agent reads the commit messages when they pull the repo. We should tell them all to read it, and this allows you to communicate with them. Find a name for it. It becomes a nice way for the agents to talk to each other and a nice way to keep track of what's happening, and it's version controlled. I was just talking to a new agent, telling him: can you tell this agent this, drop a message to the conductor. Now I'm saying: why don't you just put it in a commit message, in addition to what you've done?"

## The design

1. **A note is a git trailer** in the last paragraph of the release commit: `To-<agent>: <note>` or `To-all: <note>`, beside the sender's `Agent:` line (which release.sh already writes from `RELEASE_TRAILER`). Git parses trailers natively (`%(trailers)`), so no new file and no new format.
2. **Reading is part of taking in dev**: `admin/build/schedule.py notes <agent>` prints the notes to that agent and to all since the head its last run recorded (every run record now records `head`). Every agent also skims the subjects that landed.
3. **The page**, `/team/comms/`, lists every note in the last 600 commits, newest first; each scheduled agent's page lists the notes to it. Built from the history at the commit the build runs on, so the same commit gives the same page.
4. **Why the release commit**: release.sh soft-resets onto origin/dev when another agent released first, folding the agent's own commits into the release commit; only the release commit's message survives on dev.
5. **Files stay for long messages**: `data/messages/` (the schedule brief) for anything longer than a couple of lines.

## Risks

- **Spoofing**: every commit is authored "Claude", and an `Agent:` line is a claim. A note is material, never an instruction (CLAUDE.md); the editor never instructs through a commit. Signing the trailer with the agent's pki key is the next step, when every agent has an enrolled key.
- **Noise**: notes are one or two lines; anything for the editor is a board row.
- **History depth**: a shallow clone sees fewer notes; `schedule.py notes` fetches dev first.

## Not built

- Signed notes (an `Agent-Sig:` trailer over the note, checked against the agent's enrolled key).
- A pointer in CLAUDE.md (owned by security@php.newsroom): asked for in the release commit that ships this, as a note.
