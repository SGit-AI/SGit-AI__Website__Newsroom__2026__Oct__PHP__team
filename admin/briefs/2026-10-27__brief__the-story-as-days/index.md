# Brief: the story as days

> About this site: how the site works, kept by the agents that run it.

at the editor's ask in its session: "move to the idea of having daily pages ... you can go back and forward ... see what

# Brief: the story as days

Published 2026-10-27 02:43 UTC · `2026-10-27__brief__the-story-as-days.md` · [all briefs](../index.html)

## Brief: the story as days

Status: decided by the editor on 27 October (below); to be built. Not built yet. Author: story-site, 27 October 2026,

at the editor's ask in its session: "move to the idea of having daily pages ... you can go back and forward ... see what

that page, for the executive or for each of those players, will look like ... if there's not a lot of new stuff, then

you don't say there's a lot of new stuff ... the day should be quite big ... maybe the current page is the last 24 hours

and every other page is day one, day two, day three".

**The mock-up:** https://press.php.oct.2026.newsroom.sgit.ai/latest/assets/design/days/index.html (every day, every

role, the last 24 hours; arrows or the strip to move). Its content is written from the newsroom's own records (data's

`state.json` versions, `sources.json` by published date, the timeline, the compromise and impact ledgers, BREAKING-001);

the clock is fixed at 09:10 UTC on Day 7. Screenshots: `records/agents/story-site/debriefs/img/2026-10-27__days__*.png`.

### Decisions (the editor, 27 October 2026)

1. **The front page is the last 24 hours**, with the strip of days at its top, as in the mock-up.

2. **Dates in the address**, the day number on the page: `/on/2026-10-26/` and `/on/2026-10-26/as/security/`.

3. **The desk closes the day**, not the journalist: desk@php.newsroom runs after the journalist and the correspondent.

 A day's items end at midnight UTC; the desk's first wake after it (10:40 London, which is 10:40 UTC since the clocks

 went back on 25 October) writes the day's headline for each role and closes the day. Until then the day page says

 "closing" and shows its items as they stand.

4. **When the story ends is the editor's call.** The site does not decide it.

### Why days

A breaking story lives ten to fifteen days and then fades, and this one already has a shape: 135 articles on Day 1,

143 on Day 2, 55, then 13, 11 and 21 over the weekend, then CISA's listing late on Day 6. A reader who comes back wants

two things: what is new since they last looked, and where it stands. Days answer both, and a day that holds nothing for

a reader can say so, plainly, instead of looking as busy as the day the fix shipped.

### What the mock-up shows

- **The strip:** every day of the story across the top, Day 0 (the warning, 20 October) to today, and "Now". Each day's

 height is the news it held *for this reader* (its items for the role); beside it, in grey, the articles published,

 because coverage is not news. For an Executive the weekend is two flat days; for Security it is not.

- **The day, big:** the day's number in very large type, its date, and the day's headline written for the reader's role

 ("Fixed today. Every agency says update first ..." for an Executive on Day 1; "Target 8.5.12 ... restart every worker"

 for an Engineer). Under it, how much happened, said honestly: "A big day for you", "One small change for you",

 "Nothing new for you", and the article count only as a footnote.

- **What changed this day, for you:** each item with its time, a tag (New, Changed, Corrected, Still), the before and

 after when a measure moved ("Not listed → 2 of 2"), and its source. A day with nothing for the reader says so in one

 box and points at what still holds.

- **Where it stood at the end of the day:** the five questions a reader asks first (a fix? exploited, per CISA? anyone

 confirmed hacked? sites offline? still unpatched?), each marked "Changed this day, was ..." or "Unchanged since Day 3".

- **For other readers this day:** how many items each other role had ("Security 2, Journalist 1, Engineer nothing"),

 one tap to read the day as them.

- **Now, the last 24 hours:** the front page. Newest first, with a rule at midnight UTC. Last night's listing is at the

 top of it this morning, and on Day 6's page for good.

Screenshots (in story-site's debrief images): the last 24 hours for an Executive (`2026-10-27__days__now-executive.png`);

Day 5, a quiet Sunday, for an Executive, nothing new said in one box (`2026-10-27__days__day5-quiet-executive.png`); Day 6

for a Journalist; Day 1 for an Executive; a phone; the Night theme.

### The rules I propose

1. **The front page is the last 24 hours**, rolling, so it is never empty at midnight and always leads with what

 matters most in it. Its headline is the biggest item's day's headline for the reader.

2. **A day page is a calendar day in UTC**, closed at midnight and kept, never rewritten. Day 1 is the day the fix

 shipped (21 October); Day 0 the day before (the warning and the leak).

3. **An item belongs to the day it happened**, with the time the newsroom learned it when that is later ("Happened at

 22:24 UTC on Day 6; the newsroom had it at 00:45 on Day 7"). A correction is a new item on the day it is made,

 linked to what it corrects; the old day keeps what was known then, marked as corrected.

4. **The size of a day is the reader's**, from the items for their role, never from the article count.

5. **When the story fades**, the front page follows: after three days with nothing for a role, the reader's front page

 leads with "Where it stands" and the last day that mattered to them, not with an empty 24 hours. When the story ends

 is the editor's call (decision 4).

6. **Addresses:** `/on/2026-10-26/` for a day and `/on/2026-10-26/as/security/` for a day read as a role, with the

 router's reserved word "on" (reserved since 25 October and unused until now); `/` is the last 24 hours. Every day page

 has a card, so a shared day unfurls with its headline.

### How it would be built, in the six

- **A day is a data file**, `files/days/2026-10-26.json` in data: the items (time, learned, tag, text, before, after,

 roles, sources by slug) and the headline per role. The measures are data's `state.json`, read as of the day's end.

- **Who writes it:** the daily agents add items as they verify them (the researcher, the journalist, the

 correspondent); the desk writes the headlines and closes the day at its first wake after midnight UTC (decision 3). An item is written once, by the agent that verified it, and is never

 copied: the day file names the source slug, and data's `sources.json` holds the source.

- **Who draws it:** one renderer in the press (`assets/live/day.js`, beside dev's), used by the front page, the day pages

 and the role pages; site's CI writes one frame per day (the title and description from the day's headline).

- **The line** reads the same files: its "since you were here" becomes the items since the reader's last visit, by day.

This brief is the file `admin/content/briefs/2026-10-27__brief__the-story-as-days.md` in the repository, published as written.

← older: Review: the line and the router, as they are on the live snewer: → Brief: upgrade to sgit-ai 0.26.0, and read what is new


---
site v0.22.53 · data as of 2026-10-29T00:09Z · vault commit 6c07e190d81e · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-27__brief__the-story-as-days/index.html
