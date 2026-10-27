# The editor, 27 October 2026, about 15:16 UTC, in the projects desk's session: the desk acts as every member

The editor's own words (spoken, transcribed), filed verbatim.

> Okay, so if you need access to more repos, please do, because remember that you are going to be acting as, in a way, all the agents here, right? This is kind of a meta agent. So in fact, you might actually need the read write key, the vault key for some of these vaults. So for example, in this particular case, when you say the pulse agent should wire this up, as part of this project, you should start that pulse agent in a Sonnet separate agentic session, which hopefully should have access to your file system that you can share. And then you then can act in there, right? The key is that everything you do in those agents is then captured in an article, which describes all of these activities. So it's not an article per thing, but it's an article for a whole end-to-end flow.
> And remember that you need to brief what they do. And in a way, like, you know, this is, you are the projects at PHP newsroom, and when you act as one of the agents and you commit to a vault to say, hey, I was acting as this particular agent and here's what I did to you. So next time those agents come, you know, back from a schedule, they can read it and they can follow it up. So there should always be no surprises between multiple runs of agents here

## How the desk does it

- **One agent per member, sharing the file system.** Each member's step runs as a Sonnet subagent in this session, started with the Agent tool, sharing the desk's file system. It is never a new session: the editor's start prompt rules that out.
- **Each brief** names the member, its card and role, the step, and what it may touch.
- **The desk takes the access the work needs:** repositories by add_repo; vault keys by asking the editor, by name, each sealed to the desk's key `sha256:db7c00f5a94f1559`.
- **No surprises.** Whenever the desk acts as a member, it leaves a note where that member looks first on its next wake:
  - in that member's vault, a commit by the desk saying "projects@php.newsroom acting as <member>: what was done, and why";
  - in team, a message to the member (`records/messages/<member>/`);
  - a `To-<member>:` trailer on every release.
- **One article for the whole flow.** At the end of the project, a single article tells PROJECT-001 end to end: every member, every step, every catch. It is written from the project's log and report, not one article per step.
