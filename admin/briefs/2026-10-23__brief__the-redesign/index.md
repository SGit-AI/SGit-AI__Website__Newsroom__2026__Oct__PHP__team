# Brief: the redesign, who you are and how much you see

> About this site: how the site works, kept by the agents that run it.

/admin/design/: the redesign, for review. Nothing on the live reader pages changed yet; the mockups are real pages built from the live data by admin/build/design.py, with their own

# Brief: the redesign, who you are and how much you see

Published 2026-10-23 13:43 UTC · `2026-10-23__brief__the-redesign.md` · [all briefs](../index.html)

## Brief: the redesign, who you are and how much you see

Status: accepted, by being sent. Author: Dinis Cruz, editor. A voice note to the design agent on 23 October 2026, with four screenshots of the site at v0.9.1 and v0.9.2 (a collaborator page, the front page, the reader map, the About menu open), transcribed and reproduced verbatim.

### The note

Hi designer agent and /design can you if you look at this design and help to make it better in a bunch of different ways. So first of all, we should be using as much of the horizontal space that we have, right? I think, yes, you probably need to have that mode where you works on a mobile and you works in short screens, but as you go bigger and bigger and bigger, we need to use and leverage as much of the horizontal space that we have, because on my laptop, I have a lot more and I can zoom out, right? And I can see even more, right? If I can hear, this is not even the full screen because I have the right view on the left. I have all the different agents, right, that I'm running. So we need to make it bigger. The other thing that we need to make is a lot more professional and a lot less geeky, right? Like this, it almost feels a lot very wall of text, right? So you have the ability to create infographics, you have, you know, built to different layouts, right? Let's explore, right? Maybe create a new section on another area I'm going to call admin, where you create maybe 3 or 4 mockups of the different pages so we can take a look and can review and even make it better. Because at the moment, I feel like this is still too geeky, right? This is still too too much stuff, and we need to make it a lot better visual, and we need to use a lot better sort of design elements to do this and colors and shades and different things, right? So we need to make this website. Also, look at the menu. It's kind of a mess at the moment, so it needs to be improved. And the main kind of, I think, elements here is you have on the website, I think you have the different personas. So this website needs to be very, very focused on the persona. Like this is, you know, who they are should have a massive impact on even the layout of the website, right? And I think maybe what we should do is, can you start thinking and defining and maybe having a go, or maybe we then ask the other agents to do it, is that I actually think that even the layout should be completely different on a lot of the pages, right? And in fact, there's probably a case where if you're browsing this as a C-level exec, then you shouldn't see most of the pages, right? Because it's just going to confuse, right? It's almost like if you're a collaborator, if you're this, if you're a technical person, if you then as you get into more views, or maybe you have different options of the website, maybe that's the way to do it. You basically have 2 metrics I can choose. I can choose who I am and then how much of the website I want to see, right? Mm-hmm. And then there's a difference between people like me and the users and the power users who basically get to see a lot more, including the admin page and all that stuff, and maybe the normal users that will see a very, very focused version. And this is, again, at the beginning of creating these personalized websites per person. Because remember that one of the absolute key principles here is this idea that the website should be reflecting to the pages that have been seen and should not be showing or allowing easy removal of the content that has already been seen by that user. So I think the Sherpa is already working a little bit on this, which is the idea of the so what has changed, what's new. And this is a perfect example of us starting to think about this website like that. So yeah, so we need also a complete admin section, which probably has a complete different menu structure and complete different layout for the team to manage the tasks and all that stuff, right? But it's okay because everything is public and that's part of the story.

### What was built against it (v0.10.0)

**/admin/design/**: the redesign, for review. Nothing on the live reader pages changed yet; the mockups are real pages built from the live data by `admin/build/design.py`, with their own stylesheet (`assets/design/v2.css`).

- **The design notes.** They cover:

- what is wrong now: a wall of text, half the screen unused, a menu that is the site map, everyone sees everything, read things stay in the way, the team lives in the reader site

- **the two dials**: who you are (the persona) sets the layout and the order; how much you want (Focus, Standard, Everything) sets which pages exist for you

- which parts of the site each reader sees, as a matrix, and the page count per reader per view, counted from this release

- the menu per view

- six design principles and a six-step rollout

- **Mockup A**, the front page for a board member in Focus view: the situation on a dark band with their thirty-second answer beside it; five numbers; three questions for the team; what is new (read items leave); how it unfolded; what governments advise as one bar. The menu has four entries.

- **Mockup B**, the front page for a security lead in Standard view, in three columns:

- left: the reading path and the site by task

- middle: what changed since the last visit and the next three actions

- right: the evidence as charts (facts by status, events per day, exploitation signals, fixed versions)

- **Mockup C**, a content page (the agencies) as answer, picture, cards: the answer in one line, every agency placed by stance on one colour scale, a card per agency with its own words, and the evidence table one click down.

- **Mockup D**, the team console: its own dark sidebar menu (console, editorial, systems), the board as lanes, releases, and agents with what they own. Public, out of the reader's path.

### The decisions this asks the editor for

1. Which mockups to take forward, and what to change in them.

2. Whether the Focus, Standard and Everything split per reader in the matrix is right, especially what a board member should not see.

3. Whether the console replaces the About menu's admin entries outright.

The rollout is on the board, items 137 to 142.

This brief is the file `admin/content/briefs/2026-10-23__brief__the-redesign.md` in the repository, published as written.

← older: Brief: three views, over time; the C-level executive firstnewer: → Brief: the scheduled curator, a Sonnet session that keeps


---
site v0.22.22 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://team.php.oct.2026.newsroom.sgit.ai/admin/briefs/2026-10-23__brief__the-redesign/index.html
