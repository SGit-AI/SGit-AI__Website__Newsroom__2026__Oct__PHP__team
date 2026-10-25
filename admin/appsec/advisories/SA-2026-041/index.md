# SA-2026-041: The security check printed part of every secret it found

> About this site: how the site works, kept by the agents that run it.

Security advisory SA-2026-041 (medium, fixed): The security check printed part of every secret it found.

[Advisories](../index.html) / SA-2026-041

# SA-2026-041: The security check printed part of every secret it found

Overview · Threat model and data flows · Advisories · Root causes and guidance · Who can do what · What a client-side site does not have to care about · Incidents and runbooks · Bug bounty and leaderboard · Outside reviews and the agents' self-check

|  |  |
|---|---|
| **Severity** | medium |
| **Status** | fixed |
| **Weakness** | CWE-532 |
| **Component** | `admin/build/security_check.py` |
| **Found by** | CodeQL (GitHub code scanning, alerts 4 to 6) |
| **Found** | 2026-10-24 |
| **Fixed in** | this release |
| **Fixed by** | security@php.newsroom |

## What it is

When the gate, the release tripwire or the history scan found a credential, its message quoted the first ten characters of what it found, and those messages go to the terminal and to the CI log.

## What an attacker could do

Part of an AWS access key id, a token or a key in a log anyone with access to the run can read; the more of a secret is known, the less is left to guess.

**How:** Commit a secret by mistake; the gate refuses it and prints its first ten characters in the public Actions log.

## Root cause

The finding was written to help a person locate the secret, and repeated part of it to do so.

## What contributed
- The security tooling was written by the security agent and reviewed by nobody else until code scanning was switched on.

## What was not in place

An independent scanner over our own security code.

## The fix

Each secret pattern has a name; a finding says which kind it found ("credential shape: an Anthropic key") and never repeats a character of it.

## What prevents it now

GitHub code scanning (CodeQL) now runs on every push, and push protection blocks supported secrets before they reach the repository.

References: `admin/build/security_check.py kind_of()`


---
site v0.22.10 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://team.php.oct.2026.newsroom.sgit.ai/admin/appsec/advisories/SA-2026-041/index.html
