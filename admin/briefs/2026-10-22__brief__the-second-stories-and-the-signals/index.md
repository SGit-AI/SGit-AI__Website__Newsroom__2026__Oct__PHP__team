# Brief: the second stories, the signals, and the inventory over time

> About this site: how the site works, kept by the agents that run it.

Yeah, can you continue? Especially that analysis of those products, fixed, not fixed.

# Brief: the second stories, the signals, and the inventory over time

Published 2026-10-22 17:50 UTC · `2026-10-22__brief__the-second-stories-and-the-signals.md` · [all briefs](../index.html)

## Brief: the second stories, the signals, and the inventory over time

Status: accepted, by being sent. Author: Dinis Cruz, editor. A voice message to the journalist and historian on 22 October 2026, transcribed and reproduced verbatim, hesitations included. What was built against it is listed at the end.

### The message

Yeah, can you continue? Especially that analysis of those products, fixed, not fixed. Now, but the other thing I would like you to focus on, and actually this is a mix of historian and journalist, is I really want us to start, again, creating those graphs for the second and third stories. And this is where you really sort of want to read a lot of some of the stuff I wrote recently in the articles on the newsroom.esquito.ai, where, for example, I think I wrote an article recently about that finding passwords is not the end of the world if you can't reach the story. If you can read a secret, you know, you still have to reach it, right? And I think that's very important. And the other angle here is the angle of the what's it called? The angle of the fixes. In fact, so the angle of, if you look at the SaaS apocalypse article that I also wrote, there's a lot of conversation there about the second stories, about what I look for and what for me will be signals, especially exploitation signals, patching signals, internal vulnerability signals, network protection signals. Because the most interesting question already is not how many websites have been exploited, which I guess they will start to grow, but how many websites were exposed that they were not exploited, right? And this is also a very important question, because I think what is important to say is, for example, the websites that are not exploited are websites that are, what's it called, basically don't have assets, right? So in a very brutal kind of frame of mind, they kind of don't matter, right? In the big sense of things, right? So they kind of are disposable for companies, because, and to be honest, they should, right? Because at the end of the day, like, you probably have more important assets to protect, right? So that's the one very important point here, because we need to understand that, because the interesting metric I would like to know is how many of the websites that do matter actually vulnerable, and also then, if they do matter, why they were vulnerable in the first place, why they're not protected by other technologies like WAFs and stuff like that, why they don't have defense in depth on this, right? And the interesting point here is you can almost tell that every company that will be popped with this is fundamentally admitting that they didn't have these things in place. So that's a very important understanding that we need to have, right? Because depends again when they you know, when it happens. But if you have a company that is already patched, so there's a patch for it, and they get exploited by the patch, and my understanding is the patch is out, right? So that means that they have bigger problems, right? They have a problem, CI pipeline problem, they have, you know, all these sort of other gaps in their environments, which we should be mapping out, and we should be looking at that as evidence.

### What was read

- [The key is not the risk](https://newsroom.sgit.ai/articles/the-key-is-not-the-risk.html) (21 October): "can the attacker reach the system it opens?", the reach question this brief means.

- [The attack surface you do not have](https://newsroom.sgit.ai/articles/the-attack-surface-you-do-not-have.html) (21 October), written on the day of these flaws.

- [Footprint and blast radius](https://newsroom.sgit.ai/articles/footprint-and-blast-radius.html) (2 October): reach, mandate, gap, barriers, and blast radius with its way back.

- [The SaaS apocalypse will be decided by inertia, not by AI](https://newsroom.sgit.ai/articles/saas-apocalypse-decided-by-inertia-not-by-ai.html) (21 September). As published, it argues about inertia and Wardley maps and does not discuss exploitation, patching or network signals; the four signal families here are taken from this brief, not from that article. If the signals discussion is in another piece, the editor can point to it.

### What was built against it

- **The inventory, hour by hour** (/patching/inventory/): the NCSC-NL list read from its public git history, 38 versions from 11:20 UTC on 21 October to 15:28 UTC on 22 October, with a chart of fixed, vulnerable and under investigation, every change of status, what kind of rows they are, and when each supplier was first recorded fixed. The reader checks itself against the vault's capture, and found one row the vault's export had missed (corrections).

- **The second stories** (/signals/): the ladder from websites using PHP to exploited sites holding something worth reaching, the four signal families with what each shows now, and the time each barrier became available with what a compromise after it would say.

- **The story** "Exposed is not exploited", by the journalist and the historian, which states this brief's argument in the editor's words and weighs it against the evidence.

This brief is the file `admin/content/briefs/2026-10-22__brief__the-second-stories-and-the-signals.md` in the repository, published as written.

← older: Feeds, the delta since your last visit, a feed viewer, andnewer: → Brief: scheduled capture of the sources that move, raw to


---
site v0.22.12 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__the-second-stories-and-the-signals/index.html
