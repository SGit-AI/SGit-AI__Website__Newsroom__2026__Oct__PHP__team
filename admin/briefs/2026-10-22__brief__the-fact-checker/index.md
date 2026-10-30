# Brief: a fact-checker joins the team

> About this site: how the site works, kept by the agents that run it.

2. Mode one: follow the evidence in the vaults. Assume the captures are what they say; check whether each statement on the site follows from them, naming the file and hash read.

# Brief: a fact-checker joins the team

Published 2026-10-22 18:34 UTC · `2026-10-22__brief__the-fact-checker.md` · [all briefs](../index.html)

## Brief: a fact-checker joins the team

Status: accepted, by being sent. Author: Dinis Cruz, editor. A message to a new agent on the evening of 22 October 2026, reproduced verbatim (it was dictated). What it asks for, as work, is set out below the message; the desk it founded is `admin/factcheck/` and the page is /factcheck/.

### The message

Okay, so I would like you to join the team. as a fact checker. So you're whole job is to check the facts. And you need to be really thorough. You need to have no space for ambiguity. In fact, you need to actually map the ambiguity, right? You need to have a spectrum for evidence. You need to have a spectrum for what is actually a fact. What is an opinion? What is a fact that's conflicting information? And in a way, the ambiguity is one of the most important things we have here, right? Because that's the power of our data, right? Because an evidence will start small with a weak signal that then gets stronger and stronger and stronger. But also we can then basically qualify stuff . So I think there's two ways of, there's probably multiple, but there's two I'm thinking of, two main ways for you to operate. One of them is you need to be able to follow the facts with the evidence that's been provided, so the logic is with the data that we have in the vaults, and of course assume that that data is correct for now, right? There's no until we find evidence here, there's no point of thinking. But I'm saying is that if there's for example, a page that has a hash saying, hey, we got this from website XYZ, Because what I would like you to be able to do here is to be able to say, hey, from the web evidence on the website, from the evidence of the vaults, especially, because remember the vaults are also public, this has been verified, or this is weak. There's no evidence to show here. So you need to start entering. We need an issues FS kind of workflow. And there's, so read about issues FS, which is one of the workflows that we have. So we need a workflow where you could open tickets and you can basically say this needs fixing, or there's no data to support this, or etc. So your job is less about fixing stuff, it's more about highlighting things, right? And also here, keep an eye on, for example, evidence that is contradictory. So basically, by the time you finish your run, and we need to then configure you to run on a schedule, by the time you finish your run, the website, so the data set So the website for the data set should be on a stable state, i.e. we checked it, as far as you know, the data is consistent, or at least you identify the issue to be fixed until next time, right? But one thing that you can capture is you could also capture evidence. So you can say, hey, this part of the website says 25, here we already mapped data, 30, here's the new evidence. So it's almost like we need to start to have this weight, this maturity almost model for the data that we have and data that we collect. And then the second mode is for the bits of data where there is not a lot of evidence or you need to check. You could also go outside and see if you can find that evidence and then add it to the updates to be made on the website. So you can actually go, oh, by the way, you guys have this, but I just take a look at this. I just found this. Here's some more evidence. But the most important thing is for you to really challenge, so we can really present on a website, even color-coded on a website, the assurance and the certainty, and even be able to present, for example, views where you only say, show me only materials that I'm very comfortable or I have a strong assurance that this is facts. And there could be facts that you have 100%, right? Like there's a fact that there's a vulnerability out, that's 100%. There's a fact that, you know, there's a patch, right? All that stuff. So there's a lot of, so then it becomes a spectrum, right?

### What it asks for, as work

1. **A spectrum, not a label.** Two axes: what kind of statement it is (a record, an event, a state, a count, a quote, an attribution, an opinion, advice), and how strong the evidence is, from A0 (nothing carries it) through A1 (a weak signal), A2 (one named party), A3 (several outlets, one origin), A4 (independent parties), A5 (two primary sources) to A6 (the primary record itself: the CVE exists, the patch exists). Conflicting evidence is a third axis, tension, which pulls the displayed grade down until it is explained.

2. **Mode one: follow the evidence in the vaults.** Assume the captures are what they say; check whether each statement on the site follows from them, naming the file and hash read.

3. **Mode two: go outside.** For the weak and the contested, look for better evidence on the web, and record it as a request to capture, with its URL, time and hash: "you have 25, here is 30".

4. **Tickets, in Issues-FS.** Highlight, do not fix: a finding, a contradiction, an evidence gap, new evidence. Each names the claims, sources and pages it is about.

5. **A stable state at the end of every run.** Not that everything is right, but that nothing wrong is unmarked.

6. **On a schedule.**

7. **On the site, colour-coded, with a view of only what can be relied on.**

### A later instruction: the desk publishes to dev

The editor, at about 20:55 UTC on 22 October, during the desk's second run, verbatim:

yes you and desk should publish to dev, since or else we will have a number of bottle necks here

This is the editor's explicit exception that AGENTS.md allows to its rule that agents do not push to `dev`: the fact-check desk releases its own runs with `admin/build/release.sh`, like any release, through the gate.

### Board items opened by this brief

082 to 085, listed on the board.

This brief is the file `admin/content/briefs/2026-10-22__brief__the-fact-checker.md` in the repository, published as written.

← older: Brief: the phone app, what do I need to know for the time newer: → Talk to the site: a chat pane with tools, your OpenRouter


---
site v0.22.54 · data as of 2026-10-29T17:13Z · vault commit cd9375f1aefd · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-22__brief__the-fact-checker/index.html
