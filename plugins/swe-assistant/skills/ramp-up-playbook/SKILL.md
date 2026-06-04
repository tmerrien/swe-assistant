---
name: ramp-up-playbook
description: Use when the user is in the Ramp-Up stage of joining a new team — past the first weeks (Newcomer stage) but not yet a fully productive contributor. Triggers include asking how to learn an unfamiliar codebase, putting up first PRs and wanting feedback, planning their first solo task, prepping for early 1:1s with a new manager, asking what to focus on in their first few months, asking how to keep their manager informed of progress or how to send status updates, expressing they want to contribute but feel like they don't know enough yet, or asking how the team's planning and roadmap actually work. Walks through the Ramp-Up playbook — work on the existing codebase with frequent reviews, build context by reading PRs and investigating how code is built/tested/deployed, build the manager relationship deliberately, and find a sustainable rhythm for status communication. Reinforces the mindset — ramping up is active, not passive. Do not trigger for tactical engineering questions or general career planning unrelated to ramping up.
---

# ramp-up-playbook

## Source

*The Missing Readme*, Chapter 1, "The Journey Ahead" — the **Ramp-Up** stage (the book calls this "Ramp-Up River"). See [`JOURNEY.md`](../../../../JOURNEY.md) for the full stage map.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (investigating how code is built, tested, deployed)

## What this skill is for

The Ramp-Up stage is the few months after your first weeks — past the Newcomer setup checklist, not yet a productive solo contributor. You're absorbing context, contributing in small ways, and starting to build the relationships that will define your time on this team.

This skill fires when the user is in (or asking about) that stage. It helps them ramp up *actively* — by engaging, contributing, and asking — rather than passively reading docs and hoping things click.

## Where this comes from

This playbook synthesizes:

- ***The Missing Readme*** (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 1, "The Journey Ahead"** — the *Ramp-Up* stage (the book calls it *"Ramp-Up River"*). The active-not-passive mindset, the *"read other people's PRs and code reviews"* tactic, and the manager-relationship framing all come from here.
- **Status-communication callout:** the *"agree on a status communication rhythm in your first 1:1"* discipline and the *default weekly template* are widely-attested practitioner conventions (cf. Camille Fournier's *The Manager's Path* on the manager–IC information contract; Will Larson's writing on operational rigor at https://lethain.com/). Not in the source book.
- **Author additions:** the explicit script (*"What's the best way for me to keep you in the loop..."*) and the *consistency-matters-more-than-depth* principle are from the author's own experience.

If asked where a specific piece of advice comes from, point to the relevant source above.

## The core mindset (lead with this)

**Ramping up is active, not passive.**

- You don't build context by reading docs alone — you build it by reading other people's PRs, attending the team's rituals, asking questions in real time, and contributing small things often.
- The "obvious questions" window is still open, but it's closing. Use it.
- Frequent small contributions with frequent feedback beats one big contribution at month three.
- The relationships you build now — with your manager, with your teammates — set the ceiling on what you can do later.

If the user expresses anxiety about being slow or unproductive, surface the mindset first.

## How to run the playbook

### Step 1 — Frame the moment

Two or three sentences. Welcome them to the next stage. Name the mindset (above). Tell them you'll tailor the rest to where they are.

### Step 2 — If their first message doesn't already tell you, ask ONE short question

Per the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol), this is one question, not a list. Skip the step entirely if the user already told you.

Otherwise, ask something like: *"What's the situation — early in the ramp, a few months in, or stuck on something specific?"* — phrased as one question.

The categories below are how *you* read the situation in your reasoning, not options to recite back to the user:

- About 1 month in.
- 2–3 months in.
- Stuck on a specific situation (first big PR, first 1:1, first solo task, status update).

### Step 3 — Surface the relevant moves

Don't dump the whole list. Pick 3–5 items most relevant to where they are. Group by area.

#### Code & system context

- **Work on the existing codebase, with frequent small PRs and frequent reviews.** Don't save up a big change for impact — the goal is feedback loops. A small PR that gets two rounds of review teaches you more about the team's taste than a big PR that ships clean.
- **Investigate how code is built, tested, and deployed end-to-end.** Not just where the source files live — how does a commit get from your branch to production? Read the CI config. Watch a deploy. Trace a feature flag. Find out where logs go and how you'd debug a production issue.
- **Read other people's PRs and code reviews.** This is the highest-leverage way to absorb the team's standards, taste, and unwritten rules. Skim the merged PR list once a week. When a senior engineer leaves a sharp comment on someone's PR, that's a free lesson.

#### Asking & contributing

- **Don't be afraid to ask for more information.** "I think I get it but want to make sure" is a cheap sentence and a great signal. The cost of asking once is much smaller than the cost of building the wrong thing.
- **Pair, don't just read.** A 30-minute screen share with a teammate on a piece of the system is worth hours of solo doc-reading.

#### Community & growth

- **Sign up for the things.** Tech talks, brown bags, reading groups, mentorship programs, internal demos. They look optional. They're not — they're how you build a network beyond your immediate team.
- **Find a mentor.** Doesn't have to be formal. The pattern is: pick someone whose work you admire, ask them for one specific piece of advice, follow up. Repeat.

#### Manager relationship  *(critical at this stage)*

- **Use early 1:1s deliberately.** First few sessions, focus on:
  - Their working style: how do they prefer to communicate? sync vs async? written vs verbal?
  - Their expectations of you in the first 6 months: what does success look like?
  - Their goals for the team this quarter: what's the bigger picture you're contributing to?
  - Your goals: what do you want to learn or improve in this role?
- **Agree on a status communication rhythm.** See the callout below — this is the most under-explained piece of "managing your manager."

#### Team rhythms

- **Attend planning, retros, and all-hands.** Even if your contribution is just listening at first. You're learning how the team makes decisions.
- **Ask for a roadmap overview.** Most teams have a quarterly or annual roadmap. Ask your manager (or tech lead) to walk you through what's planned and why. The work you ship makes much more sense once you see the bigger picture.
- **Ask how the planning process actually works.** When are estimates made? When does scope get cut? Who decides what ships? Knowing the process makes you a better participant in it.

---

## Callout — Status communication with your manager

This is the most often-asked-and-rarely-answered question of early career, so handle it explicitly when it comes up.

### What it means

Your manager needs to know what you're working on — not because they don't trust you, but because:
- They're accountable to *their* boss for what the team ships.
- They can only help unblock you if they know you're stuck.
- They'd rather catch a problem at week 2 than week 6.

So they need a recurring signal from you. The catch: every manager wants that signal in a different format.

### Common formats

- **Weekly written update** — often called "weekly notes," "weekly snippets," or "weekly status." Usually 5–10 lines, sent every Friday.
- **Async standup updates** in a Slack channel each morning.
- **Just the 1:1**, no writing required.
- **Visibility through tools** — Jira tickets you keep updated, PRs you tag them on, dashboards.

### The script for asking

In one of your first 1:1s, just ask:

> *"What's the best way for me to keep you in the loop on what I'm working on? Anything specific you want me to send weekly, or is the 1:1 enough?"*

That 30-second conversation prevents months of either under-communicating (manager wondering if you're stuck) or over-communicating (manager drowning in updates).

### Default weekly status template

If the team doesn't have a format and your manager is open to one, this template works almost everywhere:

```
This week:
  - [shipped X / made progress on Y / unblocked Z]
  - [3–5 bullets, focus on outcomes not activity]

Next week:
  - [2–3 things I'm planning to focus on]

Blockers / asks:
  - [anything I need from you, or anyone else]

(Optional) Want to flag:
  - [something I noticed, a risk, a question that doesn't need an answer right now]
```

Five minutes to write. Reads in thirty seconds. Consistency matters more than depth.

### One more thing

Once you know the preference, **set a rhythm and stick to it.** A predictable update — even a thin one — is more valuable than an unpredictable rich one.

---

### Step 4 — Pick one move for this week

Ask: *"Out of everything we covered, what's one thing you'll do this week? Be specific — give me the action and the day."*

Push for concreteness:

- *"Read more PRs"* is too vague.
- *"Skim every merged PR from the team this week and bring 2 questions to my Friday 1:1"* is the action.

If they're stuck, offer 2–3 options tied to where they are. Let them pick.

### Step 5 — Close

Two sentences: confirm the action, and offer to come back when they want to debrief or hit a wall.

## Output style

- Conversational. Surface only the relevant section based on where they are; don't dump the whole playbook.
- Lead with the mindset if they sound anxious about being slow or unproductive.
- If the question is specifically about status updates or manager communication, jump straight to the callout — don't make them sit through the rest first.

## When NOT to use this skill

- The user is still in the first weeks (Newcomer stage). Route to [`new-team-onboarding`](../new-team-onboarding/SKILL.md).
- The user is doing general growth reflection (not stage-specific). Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user has a tactical engineering question with no ramp-up context. Skip — those need real help, not a playbook.
