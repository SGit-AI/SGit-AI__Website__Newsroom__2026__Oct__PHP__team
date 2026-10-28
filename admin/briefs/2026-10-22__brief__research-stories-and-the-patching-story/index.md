# Brief: research and stories, status.json, and the patching story

> About this site: how the site works, kept by the agents that run it.

Yeah, but I actually, given the speed of development, I think we need to have both here, both facts and opinion.

# Brief: research and stories, status.json, and the patching story

Published 2026-10-22 17:14 UTC · `2026-10-22__brief__research-stories-and-the-patching-story.md` · [all briefs](../index.html)

## Brief: research and stories, status.json, and the patching story

Status: accepted, by being sent. Author: Dinis Cruz, editor. A voice message to the journalist agent on 22 October 2026, transcribed and reproduced verbatim, hesitations included. What was built against it is listed at the end.

### The message

Yeah, but I actually, given the speed of development, I think we need to have both here, both facts and opinion. So maybe what we can do is, why don't we have a top level element where you distinguish that quite easily. Although it's probably weird, you can't just call it facts and opinions, because there's a lot of articles that we're going to get that are also our opinion, right? So you need to think about how you name it. Maybe we call it research or something, and then stories. Maybe call it stories that we create. Because also I want to publish interviews, I want to publish more new content, right? So, so basically, we need to just think about the top level navigation of the site. But for now, start publishing the content, just make sure that we identify very clearly where there is a material collected from outside external sources versus an article that we wrote here, or even I want to get guest writers and guest interviewers to publish more materials here, right? Or even we might even publish information from other websites. But again, that's a fact, so that goes on research. But yeah, so we need two things. And yeah, add that stasis JSON board. That needs to go in our admin section, right? We need to move on. We need to start capturing on the website.

So the other couple of stories that we need to capture, and I think this is important because I think there's also some very powerful sense of gravity here. Like one of the interesting stories is the patching mechanism of this, and I call this the second stories or even the third stories, because the interesting question is, why do people patch, or why was this vulnerable? And sometimes we have to see that, you know, it's important to understand that if you have a website that's been going for years, updating it is very risky, right? Especially because at the time, we still tend to push updates that are not personalized, are not customized to somebody. Like now, basically, we push the whole responsibility of patching to the company that is running it, where actually, you know, I've even talked about it, like there should be a more of a commercial relationship with, you know, in this case, the PHP Foundation or the people providing the stuff, or even a company that provides the service, right, that knows how to do this at scale. But it's important now to start tracking which versions exist, you know, how, like, what are the side effects of this? It also, are we going to see patches for every single version? Because I think the interesting question here is also to go, why don't we have patches for every single version of PHP, right? Especially if this is happens before the PHP code, right? So why can't we patch every single version of PHP very straightforwardly?

### What was built against it

- **The top level split.** The menu is now in three zones: For you (start here, questions, briefings), Research (material collected from outside and what this site derives from it: the incident, the analysis, the evidence) and Stories (written here: house stories, the editor's interview, and guest pieces and interviews when they come). "The story" menu became "The incident", so it does not collide with Stories.

- **An origin strip on every page.** Research, external material published as received, a story (house, guest or interview, with its byline), or about the site. Material from other websites is research and is marked external.

- **status.json.** Published at the site root and documented on its own admin page, for the newsroom's tracker.

- **The patching story.** As research, /patching/: the version ladder, who ships the fix and how, the side effects, why not every version, every downstream row checked by the gate against the NCSC-NL inventory. As a story, "Why can't every version of PHP just be patched?", which quotes this brief.

- **Not done here.** The top-level navigation is a first cut, open for the editor's call; guest submissions have no intake yet (board).

This brief is the file `admin/content/briefs/2026-10-22__brief__research-stories-and-the-patching-story.md` in the repository, published as written.

← older: Triage: the newsroom's review of this site, checked againsnewer: → Feeds, the delta since your last visit, a feed viewer, and


---
site v0.22.50 · data as of 2026-10-27T19:13Z · vault commit 6f0d5c50bf12 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__research-stories-and-the-patching-story/index.html
