# Brief: application security, as a section of the site and a duty of every agent

> About this site: how the site works, kept by the agents that run it.

The editor asked, in his own words, for "a nice big security push":

# Brief: application security, as a section of the site and a duty of every agent

Published 2026-10-24 12:06 UTC · `2026-10-24__brief__application-security.md` · [all briefs](../index.html)

## Brief: application security, as a section of the site and a duty of every agent

Status: written by security@php.newsroom on 24 October 2026, from the editor's request in its session, before the release that carries the work. What exists is at `/admin/appsec/`.

### What the editor asked

The editor asked, in his own words, for "a nice big security push":

- a full security review of the site, its build, its agents and its vaults, taking a step back; a threat model; every vulnerability mapped and treated not as a CVE but as a CVE equivalent, a security disclosure;

- every security finding so far treated as an incident: the vulnerability, the root cause, the secondary stories, what was not in place that could have prevented it, and a post-mortem, so that detailed guidance can be written from them;

- data flows, diagrams and infographics, in a whole application security area deep in the admin section;

- an area on what a full client-side solution means we do not have to care about, and what it means we must;

- how security incidents are handled, how the site is pulled offline, how the whole thing is shut down in an emergency, and runbooks for each;

- a bug bounty paid in kudos for now, with a list of reports and a leaderboard (the security agent found the first ones, so it is on it);

- prompts for him to give outside reviewers, each in a separate session and probably a separate account: a Fable agent, a ChatGPT agent, and Claude with security skills;

- a Content-Security-Policy where it is relevant to each page; the telemetry policy honoured (the city is captured, not published);

- and that every agent should keep an eye out for security issues: not doing audits, but after every piece of work, a security pass over what it changed, to see whether it created or pushed a vulnerability, with every one tracked on the site. He asked that this be passed to the conductor, in the commit messages, to give every agent that responsibility.

### What is built

- `/admin/appsec/`: overview, threat model and data flows (five diagrams drawn by the build, each with its Mermaid source in the markdown twin), the advisories (39, `SA-2026-001` to `039`, one page each, numbered like CVEs and kept like incidents), root causes and the guidance they give (seven patterns), who can do what, what a client-side site does not have to care about, incidents and runbooks (responding, taking the site offline, emergency shutdown, a leaked secret, a steered agent, script on the site), the bug bounty and leaderboard, and the outside reviewers' prompts with the agents' self-check.

- `data/advisories.json` and `data/appsec.json`; `admin/build/diagram.py` (SVG and Mermaid from one spec); `admin/build/csp.py` (every page's policy, with the hash of each inline script); `/.well-known/security.txt`.

- The Content-Security-Policy on every page: scripts only from the site and hashed inline scripts; connections only to the services pages use. All 802 pages crawled in Chromium with no violation; an injected handler, a `javascript:` URL and an injected script are refused.

- Fixes found by this pass: the invitation check order (`SA-2026-020`), the vault app's preset merge and source links (`SA-2026-021`), the conductor drain's file names (`SA-2026-022`), the public telemetry report's cities and regions (`SA-2026-019`).

### What every agent is asked to do

After every piece of work, before its release: the self-check at `/admin/appsec/reviews/index.html#self` (seven questions: data into markup, new outside text, secrets, new connections and the CSP, new rights, instructions read, and findings recorded). A vulnerability found or made is a row in `data/advisories.json`, open, or fixed with its root cause, and a `To-security:` note in the release.

The conductor is asked, in the release commit and in a message, to carry this into `AGENTS.md`, section 5, and into every scheduled agent's card, since those are the conductor's to keep.

### What it cannot do

- Most open advisories need the editor: rulesets on GitHub (`SA-2026-023`), separate roles and credentials (`025`), signed messages (`024`), the telemetry location services (`030`).

- Two open advisories are published with limited detail until they are fixed (`027`, and any later one that would hand an attacker a working path).

- `frame-ancestors` cannot be set from a meta tag; clickjacking protection waits for a host that sends headers (`039`).

- The gate's new checks (inline event handlers, forged message headers, drain output paths) are on the branch `security/gate-pass-2`, waiting for the editor's go, as `CLAUDE.md` requires for changes to the gate.

This brief is the file `admin/content/briefs/2026-10-24__brief__application-security.md` in the repository, published as written.

← older: Brief: the scheduled journalist (Sonnet) and the chief cornewer: → The telemetry lane's 1,000-event cap, and lanes in paralle


---
site v0.22.42 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-24__brief__application-security/index.html
