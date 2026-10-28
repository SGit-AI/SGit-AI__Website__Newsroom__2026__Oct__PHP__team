# Decision: every agent starts on Sonnet in the new account, as a trial

Status: the editor's decision, 28 October 2026 (in the conductor's session), recorded by conductor@php.newsroom. It
replaces, for the first days in the new account, the split of 27 October (Opus for the conductor, the correspondent and
security; Sonnet for the rest: `2026-10-27__decision__which-model-each-agent-runs.md`).

- **Every new session is started on Sonnet,** including the three that were on Opus (the conductor, the correspondent,
  security) and dev. The two coordinator desks (breaking, projects) are the editor's call each time.
- **A card names the model the session actually runs on,** in plain words ("Sonnet"), set by the session when it
  registers (`schedule.py session register … --model Sonnet`). A card that still says Opus while its session runs on
  Sonnet is wrong.
- **What the conductor watches,** at each full pass, to tell the editor how the trial goes:
  - the agents that judge (security's reviews, the correspondent's catches, the journalist's and fact-check's verdicts):
    do they still catch what the earlier sessions caught, and do their findings hold up on a second look?
  - the agents that run to a script (the researcher, the curator, the Sherpa, observability, pulse): runs that
    finish, and the time and cost per run;
  - any run that stopped, or a release the gate refused, with the model it ran on.
- **Reversible at any time,** in the session itself: the editor changes its model and the agent updates its card.
  A reviewer that misses things goes back to Opus first.
