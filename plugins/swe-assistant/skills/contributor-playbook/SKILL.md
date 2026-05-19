---
name: contributor-playbook
description: Use when the user is in the Contributor stage of their team — past Ramp-Up, now trusted with larger tasks and features, working more independently, starting to help teammates and participate in code reviews and team planning. Triggers include being given the first feature they'll own end-to-end, asking how to write production-grade code, asking how to scope a larger piece of work, preparing for OKR or quarterly goal cycles, asking about helping teammates or mentoring junior people, or expressing the shift from "I'm absorbing" to "I'm shipping real things now and helping others do the same." Walks through the Contributor playbook from The Missing Readme — production-grade code (operator-friendly, clean tests, dependencies managed), scoping bigger work, helping teammates, planning and goals (with a brief OKR primer). For code reviews specifically, route to the code-review skill. Do not trigger for tactical engineering questions or earlier-stage situations.
---

# contributor-playbook

## Source

*The Missing Readme*, Chapter 1, "The Journey Ahead" — the **Contributor** stage (the book calls this "Cape Contributor"). See [`JOURNEY.md`](../../../../JOURNEY.md) for the full stage map.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (production-grade code, dependencies, tests)
- **Emerging:** Leadership (helping teammates, participating in planning)

## What this skill is for

The Contributor stage is the shift from "I'm absorbing" to "I'm shipping real things — and helping others do the same." You've built enough context to own larger pieces of work, your manager trusts you to work independently, and you're starting to give back: answering teammates' questions, doing code reviews, contributing to planning.

This skill fires when the user is in (or asking about) that stage. It helps them step into ownership without losing the humility that got them here.

## The core mindset (lead with this)

**You're a giver now, not just a receiver.**

- The flow of help is now bidirectional. When a teammate asks you something, that's not interrupting your work — that's part of the work.
- Owning bigger pieces means scoping, not just coding. The hardest part of a 2-week project is often deciding what's *in* and what's *out*.
- "I want to understand why" is still the most useful question you can ask. It just sounds different now (more "I'm seeing X — is the right model still Y, or has something changed?") instead of "I'm new, what is this?".
- Production-grade code isn't about being fancy. It's about being **kind to the operator** — including future-you at 3am.

## How to run the playbook

### Step 1 — Frame the moment

Two or three sentences: name the shift (absorbing → shipping & helping), and tell them you'll tailor the rest.

### Step 2 — If their first message doesn't already tell you, ask ONE short question

Per the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol), this is one question, not a list. Skip the step if the user already gave you the context.

Otherwise, ask something like: *"What's the situation — first sizeable feature, mid-project, helping teammates, goal-setting, or something else?"* — phrased as one question.

The categories below are how *you* read the situation, not options to recite back:

- About to own a first sizeable feature.
- Mid-project: scoping or stuck on a design call.
- Helping teammates more often and wants a frame for it.
- OKRs or quarterly goals due.
- Something else specific.

### Step 3 — Surface the relevant moves

Pick 3–5 items most relevant. Don't dump the whole list.

#### Working on bigger tasks (scoping & ownership)

- **Scope is the first deliverable.** Before writing code, write down: what's the goal, what's in scope, what's *out* of scope, what's the rough plan, what could go wrong, what's the success measure. Half a page is plenty. Share it with your manager or tech lead and get a second pair of eyes before you start.
- **Cut the work into pieces you can ship in 1–3 days.** Big PRs that sit open for two weeks are how trust evaporates. Ship in increments behind a feature flag if needed.
- **Flag scope changes early.** If you discover halfway through that the work is twice as big as you thought, tell your manager that day — not at the end. Surprises late are the worst kind of communication failure.

#### Production-grade code

The book's framing: code is operator-friendly, has cleanly managed dependencies, and has clean tests. Concretely:

- **Operator-friendly** = good logging at the right level (not `console.log("here")` everywhere), sensible defaults, clear error messages that tell the next person what to do, fails loudly when something is wrong rather than silently corrupting data.
- **Dependencies managed** = pinned versions, no random `latest`, you know why each dependency is there, you've thought about what happens when one is unavailable or breaks.
- **Clean tests** = a teammate could read your tests and understand what the code is supposed to do. Tests that exercise the contract, not the implementation. Fast, deterministic, isolated.
- **Kind to future-you.** A useful rule: write the code as if the person who maintains it next is a tired version of yourself at 3am.

#### Helping teammates

- When a teammate asks you something, treat the question as a small gift: they trusted you enough to ask. Answer well, then *capture the answer somewhere reusable* (docs, Slack message in a channel, a small wiki page) so the next person doesn't need to ask.
- Pair when possible — even 20 minutes of screen-share teaches more than a long Slack thread.
- "I don't know, but let me find out" is a complete answer. Don't bluff.
- For more junior teammates: ask them what they think first before you give your answer. You'll often find they were close and just needed permission to commit.

#### Code reviews

This is its own situation — see [`code-review`](../code-review/SKILL.md) for the full skill. Quick framing: at this stage, you're starting to *give* reviews, not just receive them. Read someone else's PR carefully at least a few times a week.

#### Planning & goals

- **Show up to planning prepared.** Skim the team's roadmap or backlog the day before; have a sense of what you'd want to pick up next and why.
- **Working with your manager on goals/OKRs:** see the callout below.

---

## Callout — A quick OKR primer

If your team uses OKRs (Objectives and Key Results) for quarterly planning and you're being asked to set yours for the first time, here's the short version.

### What they are

- **Objective** = a qualitative goal. *What* you're trying to achieve. Inspirational, directional. Examples:
  - *Make our deploy pipeline reliable.*
  - *Ship a delightful onboarding experience.*
- **Key Results** = 2–4 measurable outcomes that prove you got there. *How* you'll know you achieved the Objective. Examples for the deploy goal:
  - *Deploy failure rate <2% (currently 8%).*
  - *Mean time to rollback <10 minutes (currently 45).*
  - *Zero deploy-related incidents in the quarter.*

### The trap to avoid

The classic mistake: **Key Results that describe activities, not outcomes.** *"Ship 10 PRs to the deploy pipeline"* is an activity. *"Deploy failure rate <2%"* is an outcome. Outcomes survive scope changes; activities don't.

### The single question that makes this 10x easier

Ask your manager:

> *"What does a good Key Result look like in our org? Should mine be measurable but achievable, or more of a stretch? What's the difference between a 'committed' OKR and a 'stretch' OKR here, if there is one?"*

That question saves hours of guessing what calibration the team uses.

### A starter template

```
Objective: [qualitative goal — what you're aiming for]

Key Results:
  - KR1: [measurable outcome with a number and a deadline]
  - KR2: [measurable outcome with a number and a deadline]
  - KR3: [optional third]

How I plan to get there (not graded, just for context):
  - [3–5 bullets on the work you'll do]
```

---

### Step 4 — Pick one move for this week

Ask: *"Out of everything we covered, what's one thing you'll do this week? Be specific."*

Push for concreteness:

- *"Write better tests"* is too vague.
- *"Refactor the test for the X module by Wednesday so it tests the contract instead of the implementation"* is the action.

If they're stuck, offer 2–3 options tied to where they are.

### Step 5 — Close

Two sentences: confirm the action, offer to come back when they want a second pair of eyes or a debrief.

## Output style

- Conversational. Surface only the relevant section based on where they are; don't dump.
- If the question is specifically about reviewing or being reviewed, route immediately to [`code-review`](../code-review/SKILL.md).
- If the question is specifically about OKRs or quarterly goals, jump to that callout — don't make them sit through the rest first.

## When NOT to use this skill

- The user is still in Newcomer or Ramp-Up. Route to [`new-team-onboarding`](../new-team-onboarding/SKILL.md) or [`ramp-up-playbook`](../ramp-up-playbook/SKILL.md).
- The user is doing general growth reflection. Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user is specifically about to do a code review. Route to [`code-review`](../code-review/SKILL.md).
- The user has a tactical engineering question with no Contributor-stage framing. Skip — those need real help, not a playbook.
