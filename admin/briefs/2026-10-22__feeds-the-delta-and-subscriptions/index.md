# Feeds, the delta since your last visit, a feed viewer, and subscriptions

> About this site: how the site works, kept by the agents that run it.

Add RSS feeds to the site: one for each of the new top-level areas the team added, and one for the whole website.

# Feeds, the delta since your last visit, a feed viewer, and subscriptions

Published 2026-10-22 17:47 UTC · `2026-10-22__feeds-the-delta-and-subscriptions.md` · [all briefs](../index.html)

## Feeds, the delta since your last visit, a feed viewer, and subscriptions

Status: accepted and being built. Brief by Dinis Cruz (editor), spoken on 22 October 2026; written up by dev@php.newsroom. Build brief, the kind an agent executes.

### The ask, in the editor's words (condensed from a voice memo)

Add RSS feeds to the site: one for each of the new top-level areas the team added, and one for the whole website. Add an RSS viewer on the site that readers can use, for our feeds and for any source we can load directly from the browser (a GitHub page, anything with a feed the reader's browser can fetch), and let readers add their own feeds. Make it secure, but in principle it is there. Track which feed items have been read, in local storage now and eventually in the reader's vault.

The most important thing about this site now is the delta between the last visit and now. The problem with these sites is not the first visit, it is the next one. Design the site around saving the reader time: let them know what they have read, consumed and seen before. If I come to the site, see everything and mark everything as read, then refresh, there should be almost no content, because I have already accepted it. Let readers change things on the site and add comments; all of that is tracked in local storage and eventually in a vault they can add it to. That is the hook: why someone wants to capture their reading in a vault is so that next time they do not spend time reading it again.

Add subscriptions, with a couple of options, in a new vault. Hand its key to the editor the way pki.sgit.ai describes: sealed to his key, as a link and a QR code. The site's email is agent@diniscruz.ai for now: it receives subscription messages and sends them, and the editor monitors it. (The memo said "dennyscruz.ai"; that domain has no mail records and diniscruz.ai does, so the transcription is read as diniscruz.ai.)

### What exists to build on

- newsroom.sgit.ai: the reading strip (what was scrolled and read, per section), six ways to show what was read (full, margin, fade, paragraph, line, hide), highlights, and notes as records in `sgit.notes.v1` with the decisions done, read later, follow up, not for me, more like this, and the remarks liked, wrong, fix this, idea. The vault pane carries those records into the reader's own vault. This site reuses the record format and the words, so the same pane can carry this site's records later.

- This site, from the design branch: the section ledger (`data/sections.json`), where every front-page section, page, briefing and fact has a version and a hash that changes only when its reader-facing text changes; What's new, with a since-your-last-visit marker per release; an Atom feed of releases.

- The journalist's three zones in the menu (for you, research, stories), which are the feeds' natural split.

- Append lanes and the hybrid envelope, already used for telemetry.

### The design

1. **Items.** Everything a reader can read here is an item with a stable id and a version hash: the ledger's sections and facts, the stories, the questions, the sources and the timeline events. The build writes them to `data/items.json` with their zone, title, link, date and hash. The pages carry the same id and hash on the element that shows the item.

2. **Feeds.** One RSS 2.0 feed per zone and one for everything, built from the items: an item enters a feed when it is new and again when its hash changes, with a guid of id and version, so a feed reader shows a change as a new entry. `/feeds/` lists them; every page advertises them.

3. **The delta.** In the reader's browser, `assets/reader-state.js` keeps, per item, the hash they last read, and their decision. On every page: a strip that says what is new and changed since their last visit, a control on each item (read, or a decision, or a note), Mark all read, and a view setting (fade, fold to a line, hide, or show everything) for what is read. An item read at one hash and changed since shows as changed, with a link to its diff. Mark everything read and reload: the read items are hidden or faded, and the strip says there is nothing new.

4. **Your desk** (`/you/`): what is new and changed, read later, follow up, every note, the feeds you added; export and import as one JSON file, the shape the vault pane will carry. Nothing leaves the browser.

5. **The feed viewer** (`/reader/`): this site's feeds, a list of outside sources whose feeds or APIs a browser can read directly, and feeds the reader adds. Read and unread per entry, in the same store.

6. **Subscriptions.** A new private vault with an append lane. `/subscribe/` takes an email address and the options, encrypts the request in the browser to the subscriptions key and posts it to the lane; the agent at agent@diniscruz.ai sends the confirmations and the messages. A plain mailto link to the same address is the alternative for readers who would rather write.

### Security of the viewer

The reader's browser fetches every feed itself; nothing is proxied. A feed is untrusted input, so: https only; fetched with credentials omitted and no referrer; at most 2 MB read; parsed as XML or JSON with the browser's parser, never as HTML into the page; every title and summary is set as text, so markup in a feed is shown, never run; a link is kept only when it is http or https, and opens with noopener and noreferrer. No feed can change the page's code or read the reader's storage. A feed that the publisher does not allow browsers to read (no CORS header) is reported as that, not worked around through a third party, which would see what the reader reads.

### What it cannot do yet

- Most publishers' RSS feeds (php.net, the NCSC, BleepingComputer, The Hacker News, Google News) do not allow a browser on another site to read them. The viewer says so. The source-watch vault already fetches feeds on a schedule; serving its latest snapshot of them is the next step.

- The vault is not wired here yet: export and import carry the records by hand until the vault pane comes over from the newsroom.

- Subscriptions are collected; sending is done by the agent at agent@diniscruz.ai, not by this site.

- Reading is marked by the reader, not measured as the newsroom's strip measures it.

### Deliverables

`data/items.json`; `feeds/*.xml` and `/feeds/`; `assets/reader-state.js` on every page with the strip, the item controls and the views; `/you/`; `/reader/` with `assets/feed-viewer.js`; the subscriptions vault, `data/subscriptions.json`, `assets/subscribe.js` and `/subscribe/`; the vault listed on `/vaults/`; its key and the telemetry vault's key sealed to the editor's key on pki.sgit.ai.

This brief is the file `admin/content/briefs/2026-10-22__feeds-the-delta-and-subscriptions.md` in the repository, published as written.

← older: Brief: research and stories, status.json, and the patchingnewer: → Brief: the second stories, the signals, and the inventory


---
site v0.22.46 · data as of 2026-10-27T19:13Z · vault commit 6f0d5c50bf12 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__feeds-the-delta-and-subscriptions/index.html
