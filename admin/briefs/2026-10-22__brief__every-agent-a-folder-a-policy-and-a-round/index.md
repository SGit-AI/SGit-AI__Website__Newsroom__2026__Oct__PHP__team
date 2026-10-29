# Brief: every agent a folder, a policy and a round

> About this site: how the site works, kept by the agents that run it.

the findings below written by librarian@php.newsroom. The message was dictated and is reproduced verbatim.

# Brief: every agent a folder, a policy and a round

Published 2026-10-22 20:11 UTC · `2026-10-22__brief__every-agent-a-folder-a-policy-and-a-round.md` · [all briefs](../index.html)

## Brief: every agent a folder, a policy and a round

Status: accepted, by being sent. Author: Dinis Cruz, editor, in the librarian's session on 22 October 2026; the design and

the findings below written by librarian@php.newsroom. The message was dictated and is reproduced verbatim.

### The message

Great work. Now, can you take a step back and really do a massive push at mapping out every single agent that we have here, every role that exists, their exact scope and responsibility? Make sure that there's no overlapping responsibilities. Make sure that they have an agent behavior policy and see riskmandate.ai for what I mean by this. That is really focused on their area of expertise. So this is a behavior policy that defines which part of the website they can operate, which part of the content they're focusing on. So we make sure we don't have overlaps, including if I ask an agent to do something else that's outside their scope, they should push back, right? Because I have already a pile of agents on my thing here. It's going to be very easy for me to make mistakes, right? Or somebody else to make mistakes. So, you know, like here, you're already doing more stuff than the librarian. And if you look at the latest agents that we have added and they're adding stuff to the website, they're going to be a lot more there. So one of the things that we also need to make sure is that, and this is, you probably want to put this on claude.md or our .claude folder, which is we have to make sure that every agent, every time they finish a round of work, so basically every time the agent loop ends in Claude, they need to make sure that they update, they basically need to write an article that describes with screenshots, with everything they've done. So we have a section for that, for the agents to put that, which is also going to help you a lot. They need to make sure that they update all their tasks. They need to make sure they read the tasks and they plan for what they're going to do next. So they need to propose what's going to happen next. And they need to capture information like how many tokens were used, how many agent behavior policies, misses, and the grant that they have. So that needs to be mapped. And if they need more mandate and if they need more things, that needs to be connected. And they need to provide a detailed answer on basically everything they've done, right? And literally provide an explanation with screenshots and new features that they added or not, right? But it's very important that it's, again, a very fact-based approach. And that is really how we're going to be synchronizing this. So basically, the conductor should be able to just read all of that stuff, have a one page that, or one section, or one file across the board on every single agent folder. So again, every agent needs to have a folder, every folder needs to have this information design. Again, you can help with this. So make sure that, in a way, they also should be making your life easier, because part of your job is cataloging, right? Now, one of the things you should look here is that we have done this very extensively, really well, on the __ send repo, which is on one of the skills that you have. When I said I want to talk to the librarian agent, for example, usually you fire up that skill. So you should have a skill that allows you to go and see that. And if you look at the role definitions on that project, they're really good. And that's exactly what we want here. We want to have these super watertight roles that are super focused, that contains very explicit KPIs, very explicit areas of operation, and now very explicit agent behavior policies that fundamentally are defining the scope and the area of involvement and what they can and they can't do. And also it's going to be a way for us to prevent security vulnerabilities. And for example, let's say that one of them is infected with a prompt injection. We should make sure that we have a lot of protection against that. And there's already a security agent that's going to look at it, but we could also protect a lot of it using our basic agent behavior policies. So start mapping it out. Again, you can start by yours. And I really like the librarian on that __ send project. And take a look at it and then start mapping this out. And remember that everything here has to be JSON or Markdown, right? And it's all about transformation, it's all about graphs. And we already added an ontologist to the team. We have really powerful roles now. And this is also about showing how these roles scale, which is really cool.

### What exists to build on

- `admin/security/`: the security requirements, and the agent behaviour policy's grant (measured), draft mandate

 and delta, in the vocabulary of abp.sgit.ai v0.3.0, as used by riskmandate.ai.

- `data/team.json` (the roster, the conductor's), `data/admin.json` (the board, and a `roles` list),

 `data/roles.json` (the agents, the story site's): three registries of roles, none with a scope a check can read.

- `AGENTS.md` and `CLAUDE.md`: how to work, and the security short form.

- The SG/Send project's role definitions (`team/roles/*/ROLE.md`, read from a clone outside this repository): identity

 with "not responsible for", principles, responsibilities, workflows, integration, metrics, quality gates, tools and

 access with explicit write paths, escalation, a daily run that ends with a log and a push.

### The design

- One folder per member, human or agent: `admin/content/agents//` with `ROLE.md`, `policy.json`, `status.json`

 and `debriefs/`. In `admin/content/` because the build renders markdown only from there (a security rule).

- `policy.json` is the mandate in the abp vocabulary plus the scope: `writes` (exclusive), `appends` (shared files,

 own row or block only), `pages`, `vaults` with the key kind, `requires_go`, `never`, `pushback`, `untrusted_inputs`,

 `kpis`. The grant is security's, measured once for every session; the delta is computed by the build.

- `admin/build/agents.py` checks that no two members claim the same file or page, that every source file and page has

 an owner, and what a round wrote outside its member's scope. The gate runs the first two (check 4h).

- Every round ends with a debrief with screenshots and an updated `status.json`; a Stop hook in `.claude/settings.json`

 reminds a session once if its branch has commits and no debrief. `/admin/agents/rounds/` and `data/agents.json` are

 the one page and the one file the conductor reads.

### What the map found

Before this map, these were claimed twice or by nobody; the drafts resolve each one, for the editor to confirm:

| Thing | Before | In the drafts |
|---|---|---|
| The list of roles | three registries: `data/team.json`, `data/admin.json` roles, `data/roles.json` agents | the folders are the source; the three are to be derived from them (board) |
| `data/signals.json` | the journalist and the historian | the journalist; the historian appends |
| The patching and signals pages | the story site (team.json) and the journalist (layers.json) | the journalist, who owns their data |
| `data/history.json` and the context page | the story site | the historian |
| `data/layers.json` | credited to the journalist | the librarian (it is the catalogue) |
| The fractal graph (`data/arcs.json`, `/fractal/`) | built by the librarian in v0.5.2 | the cartographer (unfilled); handed over |
| The glossary, personas, plain English, interview | a design agent not on the roster | design@php.newsroom, now a member |
| The interview page | the editor and the design agent | design |
| `affected/software.html` | inside the story site's `affected/**` | the newsroom lead (the inventory is evidence) |
| `CLAUDE.md`, `.claude/` | nobody | security (they shape every session) |
| The ontologist | named by the editor; nothing in this repository | a folder with a proposed scope (`data/ontology.json`) |

### What it cannot do

- Bound a steered agent. The scope check and the gate are settings an agent with push rights can edit; only a GitHub

 ruleset on the protected paths is a boundary (`admin/security/abp/DELTA.md`), and only the editor can set one.

- Count tokens. A session cannot read its own token use; `status.json` records `null` and why, unless the platform

 shows a number.

- Make the drafts true. Each member confirms its folder and the editor agrees each policy; until then they are drafts.

This brief is the file `admin/content/briefs/2026-10-22__brief__every-agent-a-folder-a-policy-and-a-round.md` in the repository, published as written.

← older: Brief: the conductor takes the updates, and the site gets newer: → Brief: external collectors (ChatGPT, Perplexity and others


---
site v0.22.53 · data as of 2026-10-29T00:09Z · vault commit 6c07e190d81e · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__every-agent-a-folder-a-policy-and-a-round/index.html
