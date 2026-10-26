# Brief: the phone app, what do I need to know for the time I have, in two modes, with my vault

> About this site: how the site works, kept by the agents that run it.

Now (/now/): one page built for a phone, which can be added to the home screen.

# Brief: the phone app, what do I need to know for the time I have, in two modes, with my vault

Published 2026-10-22 18:20 UTC · `2026-10-22__brief__the-phone-app.md` · [all briefs](../index.html)

## Brief: the phone app, what do I need to know for the time I have, in two modes, with my vault

Status: accepted, by being sent. Author: Dinis Cruz, editor. A voice memo to the design agent on the evening of 22 October 2026, transcribed by otter.ai and reproduced verbatim, hesitations included ("vote" and "volt" are the transcriber's spellings of vault). What was built against it is listed after the memo.

### The memo

Okay, so this is to add to the website the website on the PHP vulnerability. We need to add a kind of a mobile website that I can run nicely on my mobile, which leverage my vote, so we need to add vault support, like we already have vote other websites. The votes that we already have support, and what we need to do is to think about that website from the point of view of updates from the point of view of what do I need to know, right? So it's basically use me to start with, and use the to use the the ability to what's called. to know what I've read before and where I am now, and you should add the the ability to a couple of things. Know what what do I need to know now? What do I need to look at? Like if I only if I only look at almost like the the one minute view, the five minute view, the 10 minute view, the half an hour view. It's almost like how much time do I can spend on this? What do I need to know? So it could be that there's nothing new to know. It could be that oh good, no new news, or hey, this has happened. This happened. We need to be aware of this. So we need to add it. And in here, we need to have two modes, which are very important. One mode is the mode of the one is the mode of the pure semantic graphs, which is the deterministic mode, and then you can have the agentic mode, right? And and the agentic mode should be leveraging the what's it called the volt the volt support to capture and to save safely an open router key that we should be using here. So we should be using. I should, you know, or we should allow the user to use open router, right? Or so I can add to it. So we need a workflow where I can add to it, and basically we need to add a chat session. So actually, we need to add two things. We need to add a chat session capability, and we need to add dynamically content created using an LLM, and for now let's use Sonnet for for the text, and let's use one of the Gemini models that we use to create infographics on this. And yeah.

### What was built against it

**Now** (`/now/`): one page built for a phone, which can be added to the home screen.

- **The question it answers:** what do I need to know now, for the time I have?

- **Time budgets:** one minute (headlines), five (the gist), ten (with connections), thirty (the lot). Each item costs its reading time; the list stops when the time is spent and says how many more are waiting.

- **What it measures against:** what you have read before. This is the same record as the rest of the site (`assets/reader-state.js`), so an item marked read here is read on every page.

- **A new release:** what changed comes back as *changed*.

- **Nothing new:** it says "Good: nothing new" and gives the situation in two lines.

- **First visit:** it shows the situation and the core facts, and one button starts the count from there.

- **Reading as:** choose your reader (board member, CTO and so on) and items written for that reader rank higher.

- **Deterministic mode:** the items, their order and their connections come from the data alone. Every item shows what it connects to: a fact to its sources and to the briefings that carry it, a question to the pages that answer it. The same data gives the same answer.

- **Agentic mode, with your OpenRouter key, kept in your vault:**

- **Write it:** a briefing for your time budget, by Claude Sonnet (`anthropic/claude-sonnet-5.5`).

- **Draw it:** an infographic, by Gemini (`google/gemini-3.1-flash-image`, the released version of the preview model the infographic generator uses).

- **Ask:** a chat, streamed, grounded in the site's 70 facts, what nobody knows yet, and what is new to you.

- **What the model is given:** only what the deterministic mode shows. Every factual sentence must cite an item id, and the page turns each into a link back to the item; an id the model invents shows with a question mark.

- **What each output shows:** which model wrote it, from how many items, the tokens and the cost, and "not checked by a person".

- **Models are settings:** any OpenRouter id works.

- **Your vault:**

- **Opening:** any sgit vault key opens it, a newsroom.sgit.ai reader vault included; or create a new vault with a vault-server access token, and the key is shown once to save.

- **Library:** opened in the browser with the same vault library the newsroom runs (`assets/vendor/sg-vault/v0.2.3`, vendored unedited with its hashes, loaded only when a vault is opened) through the newsroom's wrapper.

- **What it keeps:** everything goes under `/php-october/`, encrypted on the phone before it leaves:

- what each device has read, one file per device so devices never conflict

- your settings

- the OpenRouter key, in `secrets/`

- every chat

- every briefing and infographic, with the model, the items given and the cost

- **Where the keys live:** the OpenRouter key is never written to the browser's storage; it lives in the vault and in the tab's memory, and is sent only to OpenRouter. The vault key is kept for the tab's life, and on the phone only if you tick "remember".

- **Tested:** at iPhone size against the real vault server, with OpenRouter mocked because this session holds no OpenRouter key. A vault was opened, the key saved and read back, and a briefing, an infographic and a chat were written into the vault and read back from a fresh session.

### Not built yet

- Opening the vault with a passkey (Face ID or a fingerprint), as the newsroom's vault pane does: needs the newsroom's door design to cover this domain.

- A real OpenRouter run, which needs the editor's key: the first live briefing will show whether Sonnet keeps to the citation rule.

- Push notifications when something changes: today the app tells you when you open it; the feeds and email subscription tell you without opening anything.

- The semantic graph drawn as a graph on the phone: today each item lists its connections.

This brief is the file `admin/content/briefs/2026-10-22__brief__the-phone-app.md` in the repository, published as written.

← older: Brief: scheduled capture of the sources that move, raw to newer: → Brief: a fact-checker joins the team


---
site v0.22.35 · data as of 2026-10-26T17:09Z · vault commit 1dceaa1dfa7f · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__the-phone-app/index.html
