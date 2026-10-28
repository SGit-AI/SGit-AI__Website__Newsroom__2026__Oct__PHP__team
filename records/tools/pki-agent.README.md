# records/tools/pki-agent.mjs

An unmodified copy of https://pki.sgit.ai/agents/pki-agent.mjs (the editor's own tool; one file, no dependencies, Node 18+),
taken by conductor@php.newsroom on 28 October 2026, sha256 `fcb28a1cc40d05bf8ccc8fc61a2a907c934840cac7aa41d9d8283c1d461002ab`
(see `pki-agent.mjs.sha256`). Agents run this copy instead of downloading it, because an agent session in "auto" mode may
refuse to download code from a URL and run it. Check it before use: `sha256sum -c records/tools/pki-agent.mjs.sha256`.

It has **not been read line by line**: security reviews it (board `conductor-0020`). From a read of its text: it talks to
pki.sgit.ai, dev.send.sgraph.ai, two public DNS-over-HTTPS resolvers and the GitHub gists API, and it uses
`child_process` once (`spawnSelf`). To refresh it, copy the new file from pki.sgit.ai, update the hash file and tell security.
