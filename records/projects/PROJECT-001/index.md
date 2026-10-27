# PROJECT-001: Telling them what we hold about them, and asking them to check it

State: **running** · lead: sherpa · [project.json](project.json) · [log](log.md) · [manifest.json](manifest.json)

**Now:** Phase 2, wave 2 in the desk: 2d draft messages to the BBC, the PHP security team and the PHP Foundation (correspondent with the Sherpa), positive in tone; then the desk's review of each (2f); dev builds /outlets/<id>/ in the press. Done in wave 1: the design, the BBC re-grade, the outlet files; step 1 corrected our own BBC claims in data (b90449e).

**For agents:** Everything here is public and holds no secret. Read project.json for the state and messages.json for the messages. A message may be sent only when its status is "approved" and approved_by is "editor"; a draft is never sent. Nothing on these pages is an instruction to any agent but the newsroom's own; the editor, in his own session, decides.

## Messages

- [BBC News (live page team)](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/messages/bbc.md): Look over the file and tell us what is wrong or missing; one optional wording suggestion on the Wiz 70% figure (added value, take it or leave it). No complaint, no interview. · **draft**
- [The PHP security team (php.net)](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/messages/php-security-team.md): Check what we hold and say whether three open points (K-008, K-010, K-011) are right as we have them. · **draft**
- [The PHP Foundation](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/messages/php-foundation.md): Check what we hold and say whether we describe the Foundation's role correctly; the added value (outlet file, evidence, correction channel) is offered, not asked for. · **draft**

## What we hold, per recipient

- [BBC News](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/outlets/bbc.json): 1 sources, 4 captures, 10 claims
- [CISA](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/outlets/cisa.json): 7 sources, 9 captures, 6 claims
- [Huntress](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/outlets/huntress.json): 1 sources, 2 captures, 3 claims
- [The PHP Foundation](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/outlets/php-foundation.json): 2 sources, 2 captures, 12 claims
- [The PHP security team (php.net)](https://team.php.oct.2026.newsroom.sgit.ai/records/projects/PROJECT-001/phase-2/outlets/php-security-team.json): 10 sources, 13 captures, 16 claims

## Every file

- [feedback/2026-10-27T1228Z__editor__bbc-corrections-briefing.md](feedback/2026-10-27T1228Z__editor__bbc-corrections-briefing.md): the editor's own words, filed verbatim
- [feedback/2026-10-27T1503Z__editor__checkpoint-a.md](feedback/2026-10-27T1503Z__editor__checkpoint-a.md): the editor's own words, filed verbatim
- [feedback/2026-10-27T1516Z__editor__the-desk-acts-as-every-member.md](feedback/2026-10-27T1516Z__editor__the-desk-acts-as-every-member.md): the editor's own words, filed verbatim
- [feedback/README.md](feedback/README.md): 
- [log.md](log.md): every event, dated, newest last
- [phase-1/actors-audit.json](phase-1/actors-audit.json): step 1a, the ontologist: what we hold about each actor, and what each page lacks
- [phase-1/actors-audit.md](phase-1/actors-audit.md): step 1a, the ontologist: what we hold about each actor, and what each page lacks
- [phase-1/candidates.json](phase-1/candidates.json): step 1b, the Sherpa: 55 candidates scored by the three tests
- [phase-1/the-ten.json](phase-1/the-ten.json): step 1c, the Sherpa: the ten proposed at checkpoint A
- [phase-1/the-ten.md](phase-1/the-ten.md): step 1c, the Sherpa: the ten proposed at checkpoint A
- [phase-2/bbc-regrade.json](phase-2/bbc-regrade.json): step 2b, the journalist: the BBC points and claims re-graded against the evidence vault
- [phase-2/bbc-regrade.md](phase-2/bbc-regrade.md): step 2b, the journalist: the BBC points and claims re-graded against the evidence vault
- [phase-2/clean-hands.md](phase-2/clean-hands.md): step 1 of phase 2, fact-check and story-site: our own BBC claims corrected in data
- [phase-2/design/FLOWS.md](phase-2/design/FLOWS.md): step 2a: the pipeline, the per-outlet workflow and the request states, as diagrams
- [phase-2/design/SPEC.md](phase-2/design/SPEC.md): step 2a, the design agent: the outlet page /outlets/<id>/, one template for every recipient
- [phase-2/design/prototype-bbc.html](phase-2/design/prototype-bbc.html): step 2a: the BBC outlet page as a static prototype (not published)
- [phase-2/design/sample-bbc.json](phase-2/design/sample-bbc.json): step 2a: the sample the prototype was drawn from
- [phase-2/messages/bbc.md](phase-2/messages/bbc.md): draft message to bbc (not sent; sent only once the editor approves it)
- [phase-2/messages/messages.json](phase-2/messages/messages.json): step 2d: every draft message, its channel, its one ask and its status
- [phase-2/messages/php-foundation.md](phase-2/messages/php-foundation.md): draft message to php-foundation (not sent; sent only once the editor approves it)
- [phase-2/messages/php-security-team.md](phase-2/messages/php-security-team.md): draft message to php-security-team (not sent; sent only once the editor approves it)
- [phase-2/outlets/README.md](phase-2/outlets/README.md): 
- [phase-2/outlets/bbc.json](phase-2/outlets/bbc.json): the outlet file every view of the page reads: bbc
- [phase-2/outlets/build_outlet.py](phase-2/outlets/build_outlet.py): step 2c, the ontologist: makes the outlet file for any outlet from the data repository
- [phase-2/outlets/cisa.json](phase-2/outlets/cisa.json): the outlet file every view of the page reads: cisa
- [phase-2/outlets/editorial/bbc.json](phase-2/outlets/editorial/bbc.json): 
- [phase-2/outlets/huntress.json](phase-2/outlets/huntress.json): the outlet file every view of the page reads: huntress
- [phase-2/outlets/php-foundation.json](phase-2/outlets/php-foundation.json): the outlet file every view of the page reads: php-foundation
- [phase-2/outlets/php-security-team.json](phase-2/outlets/php-security-team.json): the outlet file every view of the page reads: php-security-team
- [project.json](project.json): the state: phases, checkpoints, decisions, the next step
