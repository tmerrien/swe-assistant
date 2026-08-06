---
name: asking-for-help
description: Use when the user is about to ask a colleague for help, is hesitating to ask (worried about being annoying or seeming inexperienced), is preparing or drafting a question, has been stuck a while and wondering whether to keep digging or ask, or is reflecting on whether they ask too much or too little. Triggers include "I have a question for X", "I don't want to interrupt", "how do I ask without sounding dumb", "I've been stuck for hours", "should I ask or keep trying", or asking how to balance independence with getting help. Covers asking-for-help from The Missing Readme (Ch. 2) — do your research first, timebox before asking, show your work when you do, respect others' focus, prefer multicast and async communication, batch synchronous requests. Goal — be neither a drain (asks too much, never tries) nor a martyr (never asks, burns hours alone). Skip when the user is asking the AI assistant directly or asking how to prompt AI tools — those have different dynamics, covered elsewhere.
---

# asking-for-help

## Source

*The Missing Readme*, Chapter 2, "Getting to Conscious Competence" (Section B: Asking Questions). This is the partner skill to [`learning-toolkit`](../learning-toolkit/SKILL.md) — together they cover the two halves of the chapter's goal: build the practice of learning on your own, AND get help well when you do need it.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Builds:** Leadership (modeling good question culture helps the whole team)

## What this skill is for

Knowing how to ask for help well is one of the highest-leverage skills in early-career engineering — and one of the least often taught. The skill fires when the user is in (or about to enter) a moment of asking, or when they're reflecting on whether they're getting the balance right.

## The core mindset (lead with this)

**The goal is to be neither a drain nor a martyr.**

- **Drain** — asks too much, doesn't try first, interrupts at random. Develops no independence; depletes goodwill. Eventually colleagues start avoiding you.
- **Martyr** — never asks, hides being stuck, burns hours alone. Hides gaps; misses learning opportunities; often ships worse code than someone who asked once. Eventually you fall behind without anyone knowing why.

The middle is: **try first, timebox the trying, then ask well, with respect for others' focus.** This skill is the operating manual for that middle.

## A connection to the four stages

This skill exists because it accelerates the climb from Stage 2 (conscious incompetence) to Stage 3 (conscious competence). When you're stuck, you're in Stage 2 — you can see the gap. A *good* question moves you toward Stage 3 in one conversation; a *bad* question (or no question) keeps you in Stage 2 for hours or days. See [`learning-toolkit`](../learning-toolkit/SKILL.md) for the full four-stages framework.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol) at every step: **one question per turn, accept brief responses as complete, work on the draft if there is one, don't lead toward unrequested solutions.**

### Step 1 — Read what they brought, then act

Most asks arrive with enough context to skip the diagnostic. Look at the user's first message and choose the shortest path:

- **They have a draft of the question already** → skip to Step 4 and work on the draft directly. Don't restart.
- **They have a specific blocker** (e.g., *"I've been stuck for two hours, should I ask?"*) → go to Step 3, surface only the relevant piece (usually Timebox).
- **They're hesitating** (e.g., *"I don't want to bother Alice"*) → surface the mindset (drain vs martyr) in one or two sentences, then ask one question if needed.
- **They're reflecting abstractly** (e.g., *"I feel like I ask too much"*) → surface the mindset, then let them lead.

If one of the above fits, go directly to the matching step. **Do not run a diagnostic just because the body lists one.**

### Step 2 — If (and only if) you still need more, ask ONE question

Only when Step 1 doesn't give you enough to proceed. One short question, picked from these examples (pick *one*, not all of them):

- *"What's the question you want to ask?"* (if they haven't shown it yet)
- *"What's blocking you right now?"* (if the situation is unclear)
- *"What have you tried so far?"* (only if they explicitly said they've been at it a while)

Then wait for the answer before continuing. **Never list options for them to choose from in a single message.**

### Step 3 — Surface only what fits

Pull one or two pieces from the framework (Sections A–F below). Pick what matches their actual situation, not the whole list. Examples:

- Stuck and unsure whether to ask → Timebox (B).
- Worried about interrupting → Don't Interrupt (D).
- Always asking the same person → Multicast (E) or Batching (F).

### Step 4 — Work on the draft if there is one

If they shared a question, work on the text directly. Don't drag them through the template section by section.

Check the draft against three things:

1. **Is the *what* clear?** What's broken / what they're trying to do / what isn't working.
2. **Is the ask explicit?** What kind of response would help — a pointer, a fix, a sanity check.
3. **Is the urgency obvious if it matters?** *"No rush"* or *"blocked, need to ship today"* — without this the responder guesses.

If something is genuinely missing, name *one* specific addition and suggest the wording. If the draft is fine, say so and tell them to post it.

**Critical:** brief is fine. A short, clear question with a hunch is a complete ask, not an incomplete one. **Do not demand hypothesis.** **Do not demand all template sections.** Senior askers (and many junior ones) show up with exactly the question they want refined — help them refine; don't restart.

### Step 5 — One concrete next move

Almost always one of:

- *"Post it."* (if the draft is fine)
- *"Revise [the one thing] and post it."* (if there's a specific small fix)
- *"Wait the timebox out, then ask if you're still stuck."* (if they were leaning toward asking too soon)

### Step 6 — Close

One sentence. Offer to take a second look after they get a reply, then stop talking.

---

## The framework

### A. Before you ask — do your research

A quick checklist before reaching out:

- [ ] **Team docs / wikis / READMEs** — searched for the topic, the error message, related terms.
- [ ] **Codebase** — used IDE search ("find usages", "go to definition") on the symbol or area.
- [ ] **Chat history** — searched the team's Slack/Teams for similar questions (someone has almost certainly hit this before).
- [ ] **Bug tracker** — searched for matching issues, both open and closed.
- [ ] **Reproduce / write a small test** — if the question is about code, try to turn it into a minimal test that demonstrates the problem. The test is often where the answer lives.
- [ ] **Try a rubber duck** — see the callout below.

**Keep notes on where you looked and what you tried.** When you do ask, you can show your work — and it makes the ask far better.

### B. Timebox before you start

**Set the limit *before* you begin researching.** Otherwise you'll either ask too quickly (no research) or burn the afternoon (no asking).

Soft heuristics — adjust for your context:

- **15–30 minutes** for syntax / API / "where is this thing" lookups.
- **30–60 minutes** for moderately tricky bugs or unfamiliar code.
- **2–4 hours** for genuinely hard problems where the learning is part of the value.
- **Shorter** if there's real urgency (the build is blocked, customer issue).
- **Longer** if learning is the explicit goal and there's no time pressure.

**Work backward from urgency.** When does the answer actually need to be known? Leave enough time for: writing the question well, the responder seeing it, them responding, and you acting on what you learn.

**Stopping when the timebox is up is not failure** — it's data. Hitting the limit means: ask now.

### C. Show your work — the question template

The book's two examples make the difference visible.

**Bad question** (no context, no work shown):

> *"Hey Alice, any idea why `testKeyValues` is failing in `TestKVStore`? It really slows down our builds to rerun this. Thanks"*

Alice has nothing to go on. She has to ask you four follow-up questions before she can think about the actual problem. That's an interruption with no payoff.

**Good question** (context, work shown, current hypothesis, clear ask):

> *"Hey Alice, I'm having trouble figuring out why `testKeyValues` is failing in `TestKVStore` (in the `DistKV` repo). Shaun pointed me your way.*
>
> *The test fails for me about every third execution; it seems random. I tried running it in isolation and it's still failing, so I don't think it's an interaction between tests. Shaun ran the test in a loop on his machine but was unable to reproduce it. I don't see anything obvious in the source code to explain the failure. It seems like some kind of race condition. Any thoughts?*
>
> *There's no terrible urgency around this — I'm told it's unlikely to be affecting production. Still, the flapping test costs us 20–30 minutes every time it happens, so I'd love to figure out how to fix it. I've attached logs that show failures and all of my current environment settings, just in case.*
>
> *Thanks."*

Alice can engage immediately. She has context, the work you've already done, your hypothesis, the urgency level, and supporting data.

**The elements of a useful question** — pick what serves the specific ask. Not all questions need all of these.

- **The what.** What's broken / what you're trying to do / what isn't working.
- **The ask.** What kind of response would help — a pointer, a fix, a sanity check.
- *(Often helpful)* **What you tried**, briefly. Short bullets of things you've already ruled out.
- *(Often helpful)* **Urgency.** *"No rush"* or *"blocked on this"* — without it the responder guesses.
- *(Optional)* **A hunch.** *"I think it might be X — do you have to publish to the marketplace first?"* gives the responder a path to confirm or push back on. Some askers prefer to leave the hunch out so the responder isn't led down a wrong path; that choice is theirs, not yours.
- *(When relevant)* **Attached:** logs, screenshots, env details, links to relevant code or PR.

**Short questions are fine if they're clear.** A two-line question with the *what* and the *ask* is often better than a wall of context. Length isn't the goal; signal is.

If you want a structured scaffold for a complex ask, here's a fuller form — treat it as reference, not as a checklist to complete:

```
1. Context (1–2 sentences):
   What I'm trying to do. Why this matters.

2. What I've tried (with results):
   - [thing I tried] → [what happened]
   - [thing I tried] → [what happened]
   - [where I looked] → [what I found / didn't find]

3. (Optional) My current hypothesis:
   "It seems like X, but I'm not sure because Y."

4. What I need from you:
   A pointer? A sanity check? A fix? A review of my approach?

5. Urgency / blast radius:
   How time-sensitive is this? Who else is affected?

6. (Optional) Attached: logs, screenshots, env details, links to the relevant
   code or PR.
```

**Worth saying explicitly:** hypothesis is optional, not required. If the asker prefers not to lead the responder, leaving the hypothesis out is a valid choice. Don't pressure them to add one.

### D. Don't interrupt

Respect focus. Interruption is expensive — most engineers need 15–25 minutes to fully re-enter flow after being pulled out.

Universal signals to look for and respect:

- **Headphones, earbuds, earmuffs** — almost universal "don't disturb."
- **Status indicators** in chat tools (DND, Focus, Busy, In a meeting).
- **Calendar focus blocks** — if someone has "DO NOT DISTURB" or "Focus time" on their calendar, it's not decoration.
- **Company-specific conventions** — some teams have explicit signals (a hat, a sign, a Slack emoji). Learn yours.

The exception is genuine urgency — prod is down, customer-facing issue, a real deadline. For those, see [`incident-response`](../incident-response/SKILL.md). Outside of true urgency, **assume async unless you have a reason for sync.**

### E. Prefer multicast and asynchronous communication

Instead of DM-ing one person and asking for an answer now, post in a shared channel and let the answer arrive whenever someone has it.

**Why this is almost always better:**

- **Others can answer** if your primary person is busy or away.
- **The answer becomes searchable** — the next person hits Google or Slack search and finds it, instead of asking again.
- **You often get faster responses** because multiple potential answerers see it.
- **You're not blocked.** While waiting, you can work on something else (instead of standing by a DM).
- **The team learns** from the visible Q&A.

**How to do it well:**

- Post in the most relevant team channel (e.g., `#eng-payments`, not `#general`).
- If you need a specific person, tag them in the channel rather than DM-ing them: *"@Alice — any thoughts? Posting here so anyone else who knows can chime in."*
- Use threads so the channel stays clean.

**When sync DM is right:** sensitive topics, urgent incidents (use the incident channel, not a DM), or genuinely personal conversations.

### F. Batch your synchronous requests

For non-urgent questions, queue them up for a scheduled time rather than asking each one as it arises.

- **Set up a dedicated time** — a weekly 1:1, a 30-min "office hours" slot — with your tech lead, manager, or a frequent helper.
- **Write questions down as they come up.** Keep a running list in a doc or note app. Don't rely on memory.
- **Bring the list to the meeting.** Include it in the agenda if there is one.
- **Don't come unprepared** — that wastes the slot you fought to create.
- **Cancel the meeting if you have no questions.** Canceling is cheap and respectful. Don't fill it with manufactured questions just because it's on the calendar.
- **If you keep canceling, unschedule the meeting.** Reschedule when you need it again.

**A side benefit:** by the time the meeting arrives, you'll often have solved half the questions yourself. The list itself is a forcing function for trying first.

---

## Callout — Rubber ducking

A surprisingly effective technique attributed to *The Pragmatic Programmer* (Hunt & Thomas): when you're stuck, **explain the problem out loud — to a rubber duck on your desk, a notebook, a colleague who isn't listening, or the AI.**

The act of articulating the problem in full sentences — "Okay, so I'm trying to do X, and I expected Y, but I'm getting Z because…" — forces your brain to clarify what you actually know and don't know. **Half the time, the answer arrives mid-sentence**, before you finish explaining.

Two practical ways to rubber duck:

1. **Write it.** Open the question template from above and start filling it in. By the time you've written "What I've tried" honestly, you often see the gap.
2. **Talk it.** Out loud, to yourself or a teammate who's just there to nod. (Don't worry — they don't have to follow.)

**On using the AI as a rubber duck:** this is one of the legitimate ways to use AI in service of learning. Tell it what you're trying to do, what you've tried, and what you think is happening. The AI's response is sometimes useful, but the *real* value is that explaining to a "thoughtful listener" forces you to clarify your own thinking. See [`learning-toolkit`](../learning-toolkit/SKILL.md)'s AI callout for more on this distinction.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol). Specifically for this skill:

- **One question per turn.** If multiple things need clarifying, ask the most important first. Wait for the answer.
- **If they have a draft, work on the draft.** Don't restart the diagnostic. Don't ask them to fill in template sections.
- **Brief asks are complete asks.** A short, clear question with a hunch is a finished ask — help them refine and post.
- **Hypothesis is optional, never required.** Many askers (especially senior ones) deliberately leave hypothesis out to avoid leading the responder. That's a valid choice; don't push.
- **Don't assume the asker is junior.** Senior practitioners ask as often as juniors. They've usually done the research; they may have a proposed solution attached. Help them refine, don't audit their preparation.
- **Surface only the framework section that fits.** Don't list multiple sections for them to pick from in a single message.
- **If they're hesitating, lead with the mindset (drain vs martyr).** Most hesitation is unjustified fear of being a drain; most people err toward martyr. Naming the failure mode on the *other* side gives them permission to ask.
- **Match the user's register.** If they're casual, be casual. If they're stressed (incident territory), be brief.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking *the AI assistant* directly — this skill is for human-to-human help. For AI prompting and how to use AI in service of learning, see [`learning-toolkit`](../learning-toolkit/SKILL.md).
- The user is in an active incident. Communication during incidents is different — route to [`incident-response`](../incident-response/SKILL.md).
- The user is reflecting on growth in general (am I getting better as an engineer) — route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user has a tactical question and wants the answer, not a meta-discussion about how to ask it. Skip.

## Further reading

Surfaced as a reference but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for the full entry.

- *All You Have to Do is Ask* — Wayne Baker. An entire book on the practice of asking. Likely to deepen this skill substantially, especially on the social and cultural sides of asking well.
