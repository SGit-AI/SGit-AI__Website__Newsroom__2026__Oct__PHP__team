# Root causes and guidance

> About this site: how the site works, kept by the agents that run it.

The post-mortems of every fixed vulnerability in the newsroom, grouped into the patterns they share, and the rule each pattern gives every agent.

# Root causes, and the guidance they give

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

Every finding was handled as an incident: what went wrong, why, what was not in place, and what now stands in the way. Read together, 41 advisories come down to 7 patterns. Each pattern is a rule for every agent.

## The patterns

| Pattern | Advisories | The rule it gives |
|---|---|---|
| **Data reached markup with the wrong encoder** | [SA-2026-001](../advisories/SA-2026-001/index.html), [003](../advisories/SA-2026-003/index.html), [011](../advisories/SA-2026-011/index.html), [012](../advisories/SA-2026-012/index.html), [015](../advisories/SA-2026-015/index.html) | Data is written into HTML only through E() for text and attributes, U() for URLs and J() for JSON inside ; in the browser, build DOM nodes and set attributes with setAttribute; never assemble HTML in several regex passes. The CSP is the wall behind this, not a replacement for it. |
| **Something from a public lane or a server was trusted** | [SA-2026-010](../advisories/SA-2026-010/index.html), [013](../advisories/SA-2026-013/index.html), [022](../advisories/SA-2026-022/index.html), [028](../advisories/SA-2026-028/index.html) | Every row from a lane and every name from a server is hostile: validate it into a clean record before anything else; never use a server-supplied name as a path; never let a sender set a field the drain owns. |
| **Instructions and material shared one channel** | [SA-2026-009](../advisories/SA-2026-009/index.html), [014](../advisories/SA-2026-014/index.html), [024](../advisories/SA-2026-024/index.html), [025](../advisories/SA-2026-025/index.html), [035](../advisories/SA-2026-035/index.html) | What a model or an agent reads from outside is fenced as material; only the editor's prompt instructs; rights come from the prompt, never from a message; whoever reads hostile text holds as few rights as the work needs. |
| **A secret travelled further than it had to** | [SA-2026-006](../advisories/SA-2026-006/index.html), [007](../advisories/SA-2026-007/index.html), [026](../advisories/SA-2026-026/index.html), [031](../advisories/SA-2026-031/index.html) | Give a secret to the one step that needs it; never cache a credential store; pass secrets by stdin, not arguments; keep secret-holding apps on an origin of their own. |
| **A control was a setting, not a boundary** | [SA-2026-005](../advisories/SA-2026-005/index.html), [008](../advisories/SA-2026-008/index.html), [023](../advisories/SA-2026-023/index.html), [034](../advisories/SA-2026-034/index.html) | Ask of every control: can the agent it constrains turn it off? If so, it stops mistakes, not attacks. Move the ones that matter to GitHub (rulesets, environments) or the server. |
| **A failure was silent** | [SA-2026-017](../advisories/SA-2026-017/index.html) | A control that fails must fail loudly: the gate checks that what the build reads is in git, that every page has its CSP, that every advisory has a root cause. |
| **Side effects came before validation** | [SA-2026-020](../advisories/SA-2026-020/index.html), [021](../advisories/SA-2026-021/index.html) | Check everything an input claims, then write. Allow-list the keys of any object merged from outside. |

## Every fixed advisory, its root cause and its guard

| Advisory | Root cause | What was not in place | What prevents it now |
|---|---|---|---|
| [SA-2026-001](../advisories/SA-2026-001/index.html)Captured page titles could close the JSON-LD script block and run on the site | Data was serialised for JSON, not for JSON inside HTML. Two contexts, one encoder. | A single helper for JSON inside , and a gate check that every JSON script block parses. | The gate fails on any JSON script block that does not parse or contains "


---
site v0.22.5 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/admin/appsec/post-mortems/index.html
