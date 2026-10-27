# Decision: which model each agent runs

Status: the editor's decision, 27 October 2026 (in the conductor's session), recorded by conductor@php.newsroom. Each
scheduled task runs on the model of the agent's own session, so this is set in each session, not in a task.

- **Opus:** the conductor, the correspondent and security.
- **Sonnet:** every other agent. That is the researcher, the curator, the journalist, fact-check, pulse, the Sherpa,
  the desk, the librarian, the ontologist and observability, plus the breaking desk and dev.

Checked at 05:35 UTC from each session's record: all thirteen persistent sessions run on these models, and each ran its
last turn on its model. The breaking desk's session and dev's fresh daily sessions are not visible from the conductor's.

Each agent's card (`records/schedule/<agent>.json`, field `model`) names its model in plain words ("Opus" or "Sonnet"),
not "the session's model". The conductor checks the sessions against this list on its full passes. A change is the
editor's, in the agent's own session; the agent then updates its card.
