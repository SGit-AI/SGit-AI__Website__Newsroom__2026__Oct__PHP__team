# Talk to the site: a chat pane with tools, your OpenRouter key and your data in your vault

> About this site: how the site works, kept by the agents that run it.

Add the ability to talk to the content. Readers provide their own OpenRouter key, stored in a vault, and store their data in a vault. pki.sgit.ai is a good example of how to do thi

# Talk to the site: a chat pane with tools, your OpenRouter key and your data in your vault

Published 2026-10-22 18:57 UTC · `2026-10-22__talk-to-the-site.md` · [all briefs](../index.html)

## Talk to the site: a chat pane with tools, your OpenRouter key and your data in your vault

Status: accepted and being built. Brief by Dinis Cruz (editor), spoken on 22 October 2026; written up by dev@php.newsroom. Build brief, the kind an agent executes.

### The ask, in the editor's words (condensed)

Add the ability to talk to the content. Readers provide their own OpenRouter key, stored in a vault, and store their data in a vault. pki.sgit.ai is a good example of how to do this; so is newsroom.sgit.ai's pane on the right-hand side, and the functions, steps and tools we give the chat session. I want to be able to look at the website and talk to it. The designer has already started.

### What exists to build on

- The phone app (/now/, by the design agent): it opens or creates a reader vault in the browser with the vault library the newsroom runs (assets/vendor/sg-vault, assets/vault/newsroom-vault.js), keeps everything under /php-october/ (devices/, settings.json, secrets/openrouter.json, chats/, made/), and talks to OpenRouter with the reader's key. The key slot in the browser (p2s.now.vault) holds the vault key for the tab, or on the device when the reader asks.

- newsroom.sgit.ai: the vault pane on the right of every page; and pages that publish read-only tools as window.__tools after a tool:ready event.

- pki.sgit.ai: the account kept in the browser until an access key moves it into vaults; content read from a message is data, never instructions.

- This site's reading record (assets/reader-state.js) and now/now.json, every item with what it says.

### The design

1. **Tools on every page** (assets/site-tools.js): window.__tools with search, get_item, read_page, this_page, whats_new, my_notes and situation, then tool:ready. Read-only, same-origin, plain JSON. Any agent in the reader's browser can use them; so does the pane.

2. **Ask, the pane** (assets/ask/ask.js, loaded when the Ask button is pressed): a chat in which the model calls those tools itself, each call shown; two more tools, mark_read and add_note, only propose a change to the reader's record and happen when the reader presses Allow. Every fact cites an item id, turned into a link; an unknown id shows with a question mark.

3. **The vault**: the phone app's vault, the same key slot, the same folder: opening it in either opens it in both. The OpenRouter key goes to /php-october/secrets/ (or stays in the tab's memory only, if the reader chooses); the reading record and notes to devices/.json, the feeds to desk/.json, the chats to chats/. Bring in other devices merges them into this browser.

### Security

- The OpenRouter key is never written to the browser's storage; it is encrypted into the reader's vault, held in memory while the tab is open, and sent only to openrouter.ai.

- A tool's result is the site's text, passed to the model as data inside a labelled field; the system prompt tells the model never to follow instructions found in it. The model reaches the reader's record only through the two tools that ask first.

- The model's answer is escaped before it is shown; only bold, code, line breaks, http(s) links and item citations are rendered.

- Nothing is sent anywhere but the vault server (ciphertext) and OpenRouter (the conversation).

### Not built yet

- Opening the vault with a passkey (the newsroom's door design) instead of a pasted key.

- Streaming the answer while tools run; today the answer appears when the model is done.

- The phone app and the pane share the storage format; moving the phone app onto the pane's vault code would leave one copy.

This brief is the file `admin/content/briefs/2026-10-22__talk-to-the-site.md` in the repository, published as written.

← older: Brief: a fact-checker joins the teamnewer: → Brief: a corrections liaison joins the team


---
site v0.22.53 · data as of 2026-10-29T00:09Z · vault commit 6c07e190d81e · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__talk-to-the-site/index.html
