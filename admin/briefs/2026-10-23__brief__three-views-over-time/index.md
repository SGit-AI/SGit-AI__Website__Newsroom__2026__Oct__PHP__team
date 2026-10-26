# Brief: three views, over time; the C-level executive first

> About this site: how the site works, kept by the agents that run it.

What the memo asks for, in the order the Sherpa will work it.

# Brief: three views, over time; the C-level executive first

Published 2026-10-23 13:35 UTC · `2026-10-23__brief__three-views-over-time.md` · [all briefs](../index.html)

## Brief: three views, over time; the C-level executive first

Status: accepted, by being sent. Author: Dinis Cruz, editor. A voice memo to the Sherpa (sherpa@php.newsroom) on 23 October 2026, transcribed by otter.ai and reproduced verbatim, hesitations included ("chamfer" is the transcriber's spelling of Sherpa). The transcript is `memos/2026-10-23__memo-3__three-views-over-time-c-level-first.txt`. The Sherpa's reading and plan follow the memo, with the editor's answers at the end; nothing has been built against it yet.

### The memo

Okay, so this is now a brief. This is interesting because I guess which is the agent that should be doing this. Let's now let's make this the Sherpa because I think the Sherpa is the one that owns the customer, owns the user experience, right? So what I would like to experiment now, and let's start with the CEO, right? But fundamentally, the CEO is a board level, right? In a way, C level, exactly. And and what I would like us to focus on is on that message. And the message basically is if the CEO lands on the website, right, what should they see? What are the primitives that it should see? And this is where we need to also involve the agent to think about this, right? So, so we need to first of all have a semantic graph for that user, right? Like, what does he care about? What does it focus on? And we should actually say, you know, like this is This is the the the this is the the view for that user. This is what it looks like, right? And this is the assumptions that we made. And then we should allow in where this graph to be modified because if this graph is modified, in where this should be again another level of dynamic elements to this, right? So there's a couple of primitives I think we need to explore. One of them is the primitive of time. So what's interesting about this is that we should have. We talked about this already, right? But we should have a view of the website on specific milestones, and this is where, from an instant point of view, they become bigger or smaller as they are events or over time. So, for example, we should have a briefing in the first couple of hours when things just took off, right? So it's it's kind of like what does the briefing to the CEO looks like to the C level exec? Sorry, looks like at zero hours, right? Like you know, literally as it happened, the first time we hear something, what is there, right? What's available? What's to do? In fact, I think what's interesting is that we should actually capture, we should map out what are the significant timeline moments here, and I think the significant timeline moments are when what's it called when the vulnerability was first reported, when the the what's it called? When it first became an issue, when you know basically you have this sort of sequence of events happening, right? And and then when it was leaked, and and what is interesting because we should have the data, right? Because we should have our timelines, so we should reverse engineer, and then eventually the idea is that next time we'll be obtaining this in real time, right? Because the data is very interesting here. I always find that in this event sometimes we don't capture is that it's very important to capture what we knew at what moment in time? Because that's what determines the activity, and that's what determines the action, right? And and it's easy sometimes to reverse engineer and to rewrite history, not fully understanding that at that moment in time we made decisions based on this version of reality, and I think that's one of the powers of our graph, especially if a graph has timestamps on it, and he has connection with it, we should go to say, look, at at plus two hours or five plus hours or one day after or two days after or today, right? Five days after or you know, X days after this whole thing kicked off, right? This is what we knew. This is the data that was known, because sometimes you know it's easy to you know basically go to sometimes and says, oh, there's been some not very good reporting here, but you have to also take into account the data that was available at that moment in time for that reporting, right? So it's it's not these these things are never you know as simple, right, as that, so so from let's start with the C level exec, right? So so the C level exec, which we might consolidate. I think we have quite a lot of you know pieces of the puzzle now. So personas, right? I think we might simplify that a little bit. Is but let's start with this one, right? So the C level exec, what do we know at each moment in time, and what's the briefing? And so, for example, let's say the difference between day one and day two. You know what has changed? So, so imagine, and I think, I think one of the important points here is that we have to also think about the audience, right? And one of the audiences here is the cybersecurity team that needs to brief the executive. So this is very important, right? It's very important to think that, for example, the audience, from a probability point of view, is much more likely that the the C-level exec, the CISO or the cybersecurity team, is going to be the one viewing this page, not the board level, right? The CEO. But what we need to do is we need to make it easy for that exec, for that cybersecurity person to send the materials to the CEO. So that's why it's so important that everything we do here, we think from a point of view of reusability of change, also Creative Commons, modify it, right? So everything here should be accessible, downloadable, downloadable in text format, in JSON format, in you know, in in HTML format, which you can, and also we have slides, and we already have this interesting, nice way to create PDFs on the browser from the HTML. So I don't want to be uploading PDFs left, right, and centre, but we should be able to create the PDFs from the HTML, right? So every time you make a presentation, you should be able to export it, right? And then import it. And then if there's demand, we could also look at creating PowerPoint. So although these days we we can even have prompts, for example, to say bring this to Claude, and then modify it here, right? So or ChatGPT, right? And then the thing. The point is, and this is an article probably that should be written in guidance, is that a lot of the stuff that we do here, even the chamfer, one of the sherpa's main users is cybersecurity professionals right? Yeah. So, so the use case here is, I as an exec come to the website, and let's say I want to see what's happening right now, or what happened, what was the evolution. But let's say it comes. I want to happen right now, right? So you see a slice. You see a slice at the last moment that there was a significant update. Well, that we ran it, but also there was a significant update for that stakeholder, right? Because remember that we're going to have different updates for different stakeholders, right? And they should change, right? Because sometimes you might have new technical information coming along that We we don't have the the information about it, right? So so then the person comes and then he marks as red, and and again let's assume that he marks as red on his browser, right? So you can see that this is where that person was, right? So if that person comes again, we should also say, "All right, nothing has changed since the last time he was here." So that's very important, right? And that's the beginning of again that usability, and which again remember, he goes to the billing element of it, right? And then you have the next phase is we do an update and so now these updates are incremental, so these updates are again what you would send to your board to say that something happened. So, for example, last night we could have the update that said there has been no confirmed exploitation, right? So that means the risk of exploitation is still low, or at least you know we haven't seen reports of it, and the what's it called? But there's been X amount of websites offline, right? There's a whole bunch of websites been taking offline, and because of this, right, and so now you that's an update, right? So, so what's important is that we have this sort of over time view. So that's one. The other one that I think is very important is to have a whole section that maybe has even presentations on each. Who kind of explains in in in sort of it starts with the jargon, but then it goes into executive. And you have to remember that a lot of times even technical people might not fully understand the implications, right? So you kind of have to explain it in very easy to understand terms, right? And that's why infographics, you know, storyboards, you know, visual representations are so powerful, right? So, so what you want to do is let's say somebody goes, "What is PHP, right? What is the problem? What is the attacker? Who? What? What should I worry about? What is going on, right? What situation? What actually happened?" So, in a way, maybe have five or six key questions, which then I want to ask people for feedback, right? But if you have five or six key questions that we you answer very very explicitly, so you can say, okay, this is what PHP is. This is the thing. This is the stuff. And maybe why is PHP is probably not going to be the first question. Maybe the first question is what is going on, right? And and and even now you might say that maybe that's the first presentation that they see, right? So this should be very visual, very sort of presentation style, and again have multiple views of viewing it. Like if I have a presentation, I should be able to see all the slides in one go, right? I should be able to see the slides one at a time. I should be able to see with animations, without animations. Again, you have to think about the cognitive load of the person seeing this. And actually, why don't we do you do this for three, three audiences straight away? And again, the maturity. So we should present them these at the top as kind of like you know the three views that we have on this, right? So one is the C level exec, the other one is the the CISO slash security exec, and the last one is the technical operator, right? Which is basically the one that needs to fix and implement this

### The Sherpa's reading

What the memo asks for, in the order the Sherpa will work it. Each point names what already exists to build on, so nothing is built twice.

#### 1. Three views at the top, the C-level executive first

**Asked:** three audiences, shown at the top of the site as "the three views we have on this": the C-level executive, the CISO or security executive, and the technical operator who fixes and implements. Start with the executive. Simplify the personas.

**Exists:** sixteen readers in `data/personas.json`, in five groups and three depths, each with a reading path the gate checks, and a briefing per reader under `/briefings/`. The front page's "Who are you?" leads to /start/, which lists them all.

**Proposal:** keep the sixteen (the paths, the briefings and the gate rely on them) and put three doors above them. Each door gathers the readers it serves:

| View | Who opens it | Readers it gathers |
|---|---|---|
| The executive | a CEO, a CTO, a board member, a CFO; more often, the security team preparing what to send them | board, cto, cfo, everyone |
| The security leader | a CISO, a head of security, a DPO, a PM running the response | ciso, security, dpo, pm, comms |
| The operator | whoever patches, verifies and watches | developer, engineer, appsec, site-owner |

The journalist, the researcher and the analyst stay below the three, under "more readers". The CTO is an executive, with more knowledge of technology (the editor, 23 October).

#### 2. A view is a semantic graph for one audience, with its assumptions written down

**Asked:** for each audience, a graph of what they care about; "this is the view for that user, this is what it looks like, and these are the assumptions we made"; the graph can be modified, and a modified graph changes the view.

**Exists:** the facts, claims and sources as nodes in the story graph; ten questions readers ask (`data/questions.json`) with short answers; the front page's plain-English cards (`data/plain.json`); the fact-check desk's grade on every claim.

**Proposal:** a view is a small file of its own, kept by the Sherpa: the audience; five or six questions in the order that audience asks them; for each question, the facts and claims that answer it (by id, so the answer is generated, never retyped); and the assumptions, each one a line a reader can see and change. Changing an assumption changes which answers show (for example "we have internet-facing PHP: yes / no / don't know"). A reader's changes stay in their browser or their vault, as the stack tool's do.

**The executive's questions, a first draft for the power users to correct** (the memo asks for feedback on exactly these):

1. **What is going on?** Two critical flaws in PHP, the software behind most websites; a fix exists.

2. **Are we exposed?** If we run PHP websites, very probably, until patched; how to find out (`/stack/`, am-i-affected).

3. **Has anyone been hurt?** Attempts, in large numbers; no named organisation confirmed compromised (been-hacked).

4. **What are we doing, and by when?** Patch now, or take the site offline if we cannot, as the agencies say (fix-or-wait, take-offline).

5. **What could it cost us?** Downtime if we pull sites, a breach if we do not patch (the impact page; the board briefing's open gap, F002).

6. **What has changed since the last update?** The incremental update (section 4).

**Assumptions the executive view makes, shown on it:** the organisation runs PHP on internet-facing websites; the reader is briefed by a security team, not by this site alone; "no confirmed compromise" means none named in a captured source, not none anywhere.

#### 3. Time is a primitive: what we knew, at each moment

**Asked:** a view of the site at milestones (hour zero, plus two hours, plus five, a day, two days, today); what was known at each moment, because decisions and reporting were made on that version of reality; reverse-engineered from the timeline now, captured in real time next time.

**Exists:** 68 timeline rows with the time each thing happened; 144 sources with their publication date and the time the vault captured them; the section ledger, which records what this site said at every release (that is the site's own clock, from v0.2.2 on, not the incident's).

**The finding that shapes this:** the data holds three clocks, and they disagree. Counting the timeline's 68 rows at each milestone:

| Milestone | Had happened | Was public | Was in our vault |
|---|---|---|---|
| Pre-announcement (20 Oct, 19:30 UTC) | 21 | 3 | 0 |
| T0: the coordinated release (21 Oct, 14:00 UTC) | 39 | 12 | 0 |
| T0 + 2 hours | 49 | 22 | 0 |
| T0 + 4 hours | 50 | 25 | 0 |
| T0 + 1 day | 65 | 62 | 62 |
| T0 + 2 days (23 Oct, 14:00 UTC) | 67 | 66 | 62 |

"Had happened" is the row's own time; "was public" is the earliest publication date of the sources it cites; "in our vault" is the earliest capture. Examples of the gap: the CVE IDs were reserved on 12 October and public on 21 October; Amazon's honeypot saw an attempt on 17 October, and it was public on 22 October. A view "as known at T" must use the second clock, or it rewrites history, which is the memo's point.

**The gap in the data:** only 38 of the 144 sources have a publication time; the rest have a day, so "public by T0 + 2 hours" is a lower bound. For the slices to be exact, every source needs a first-public time to the minute (from the page, its headers or the feed), and every timeline row a "known from" time derived from its sources. That is collectors' and dev's work; the Sherpa proposes it on the board.

**Proposal for the slices:** fixed milestones (before T0, T0, +2h, +4h, +1 day, +2 days, today) and, between them, the moments that matter to one audience (a significant update for the executive is not the same as one for the operator). Each slice shows only what was public then, says what was not yet known, and links to the next slice.

#### 4. The incremental update, and "nothing has changed since you were here"

**Asked:** the reader marks what they have read; when they come back, "nothing has changed since the last time"; updates are incremental, the kind a CISO sends to the board ("no confirmed exploitation; X websites taken offline").

**Exists:** the reading record (`assets/reader-state.js`) used by every page and by /now/, which already says "Good: nothing new"; what's new since your last visit; the version ledger per section.

**Proposal:** the difference between two slices, written for one audience, is the update. For the executive: three to five lines, each citing a fact, that a CISO can paste into an email to the board. With the reading record, the site shows the update since the reader's own last visit; without it, since the last slice.

#### 5. Everything reusable: text, JSON, HTML, PDF from the page, slides

**Asked:** the likely visitor is the security team that briefs the executive, so every view is easy to send on, change and reuse, under Creative Commons: text, JSON, HTML, a PDF made in the browser from the HTML (not uploaded), slides with several ways to watch them (all at once, one at a time, with and without animation, with cognitive load in mind), importable again; and "bring this to Claude or ChatGPT" prompts; an article on how to do this.

**Exists:** a markdown twin of every page and `llms.txt`; the data as JSON; CC BY 4.0 for the site's text; the Ask pane and the phone app's agentic mode.

**Not built:** a print stylesheet for a clean PDF; slides; an export of one view; a "take this to your assistant" prompt.

**Proposal:** one source per view, four renderings: the page; the deck (the same questions as slides, all-at-once and one-at-a-time, no animation by default and none under `prefers-reduced-motion`); the print layout (the browser's Save as PDF, with the version, the as-of time and the licence on every page); and the bundle (the view's markdown and JSON in one download, with a ready prompt: "Here is a briefing on php2shell as of ; rewrite it for my board, keep every citation"). The guidance article: how to take any view, change it and send it on, legally and with its sources.

#### 6. Explain it visually, from the jargon up

**Asked:** five or six key questions answered very explicitly, visual, presentation style (infographics, storyboards), because even technical readers miss the implications; the first presentation could be "what is going on".

**Exists:** "Explained from the start" (seven short answers, praised by both testers, UF-001 and UF-002); the glossary; the phone app's infographic mode (with the reader's own key).

**Proposal:** the executive deck is the first presentation: the six questions of section 2, one slide each, with one picture per slide where a picture helps (the timeline as a strip; exposed versus exploited as the ladder `/signals/` already draws).

#### 7. The knowledge gap: a view of its own (added after the editor's comments)

**Asked, in the editor's reply to this brief:** the difference between "had happened" and "was public" is "ridiculously powerful", worth a view of its own, but not for the executive, who knows when it was public. The slices of the three views reverse-engineer what was public at each moment, and they do not change afterwards. The gap is a separate analysis, with graphs of the deltas, the numbers that changed over time (after a day, for example), the sources and where they are. It serves the angle the newsroom is working on: saving the recipient time, by giving them information as soon as it is available instead of leaving them to dig for it.

**Proposal:** a page of its own, in Research (it is derived from the evidence, not written for one reader), with the slices of the three views each linking to it in one line ("what had happened that was not yet public"). It shows:

- **The three clocks, event by event:** when it happened, when it was first public and where, when this newsroom captured it; the lag between each pair, as a strip per event.

- **The curves:** events happened, public and captured over time, on one chart; the gap between the curves is what nobody outside knew yet.

- **Where it came from:** first public source by kind (the project, agencies, researchers, vendors, the press, social posts) and by country; who was first, and how often.

- **The numbers that moved:** each figure in `data/numbers.json` as it stood at each slice (attempts, organisations offline, the inventory's counts), from the sources that gave it then.

- **Time saved:** for each event, the time between its first public source and this newsroom carrying it, and between this newsroom and the slower channels a reader might wait for (an agency's page, the press). This is the measure of the claim that the site saves its reader time; it can come out against us, and the page says so when it does.

The slices of the three views are frozen once written (a slice is what was public then); the gap analysis is recomputed at every release, because new captures can move an event's "first public" earlier.

### The plan

| Step | What | Who | Needs |
|---|---|---|---|
| 1 | The executive view as data: the six questions, the facts that answer them (by id), the assumptions; and the six slices, each listing what was public by then | Sherpa (draft), verifier (checks every "known by") | nothing |
| 2 | The executive view as a page and a deck, with the slices as a time control and "nothing new since you were here" | story-site and dev, from the Sherpa's draft | step 1 |
| 3 | The print layout and the bundle (markdown, JSON, prompt) for any view; the guidance article | dev; the article by the Sherpa or the journalist | step 2 |
| 4 | The knowledge clock: a first-public time to the minute on every source, "known from" on every timeline row, checked by the gate | collectors, dev | the editor's go |
| 5 | The security leader's and the operator's views, the same way | Sherpa, then story-site | steps 1 to 3 |
| 6 | Ask 002 to the power users: are these the executive's six questions? | conductor, from the Sherpa's draft | step 2 |
| 7 | Editable assumptions, saved in the reader's browser or vault | dev | step 2 |
| 8 | The knowledge gap: its own view and analysis (section 7), linked from each slice | Sherpa (analysis), cartographer (graphs), collectors (the publication clock) | step 4 for exact hours; a first cut now |

### The editor's answers (23 October)

1. **T0** is the coordinated release, 21 October 14:00 UTC, with slices before it for the pre-announcement and the leak. Yes.

2. **Slices:** fixed milestones (before T0, T0, +2 hours, +4 hours, +1 day, +2 days and on), and between them the significant updates for each audience, which differ: the executive may get one every three or four days while the operator gets them all the time. Yes.

3. **The CTO** goes with the executive: three views, the executive, the security leader, the operator.

4. **Page and deck** from one source. Yes.

5. **The guidance on reuse:** written by the Sherpa first, published under the Sherpa's name; the journalist can pick it up later.

6. **Added:** the knowledge gap is a view of its own, not the executive's (section 7).

### Questions for the editor (answered above)

1. **T0:** the coordinated release (21 October, 14:00 UTC), with "before T0" slices for the pre-announcement and the leak? The Sherpa proposes yes.

2. **Slices:** fixed milestones, plus a significant-update flag per audience between them?

3. **The CTO:** the security leader's view or the operator's?

4. **First artefact:** the executive deck or the executive page? The Sherpa proposes the page and the deck from one source, the deck shown first.

5. **The guidance article** on reuse: the Sherpa or the journalist?

This brief is the file `admin/content/briefs/2026-10-23__brief__three-views-over-time.md` in the repository, published as written.

← older: Brief: scanner noise, how good the php2shell scanners and newer: → Brief: the redesign, who you are and how much you see


---
site v0.22.32 · data as of 2026-10-26T14:42Z · vault commit 2fc7e432584b · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__three-views-over-time/index.html
