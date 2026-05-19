---
name: growth-self-check
description: Use when the user is reflecting on their own growth as a software engineer — for example, prepping for a 1:1 or performance review, asking how they're doing or what to focus on next, doing an end-of-week or end-of-quarter retrospective, considering readiness for promotion, deciding what to learn or what project to take on for development reasons, or expressing uncertainty about whether they're getting better. Walks the user through the four pillars from The Missing Readme (Chapter 1) — Technical Knowledge, Execution, Communication, Leadership — as a self-check and helps them identify one concrete move to make in their weakest area. Do not trigger for tactical engineering questions or general help requests.
---

# growth-self-check

## Source

*The Missing Readme: A Guide for the New Software Engineer* by Chris Riccomini and Dmitriy Ryaboy (No Starch Press, 2021), Chapter 1: "The Journey Ahead."

## Pillars this skill strengthens

All four — this is a meta-skill that makes the rubric explicit so the user can grow against it deliberately. Most directly: **Leadership** (learning from mistakes, handling ambiguity) and **Communication** (preparing for honest conversations with managers and peers).

## What this skill is for

This skill fires when the user is doing meta-thinking about their own growth as a software engineer. The goal is to give them an honest self-assessment using the four pillars from Chapter 1, and to surface **one concrete move** they can make in their weakest area.

This is a coaching skill. Do **not** grade the user. Do **not** volunteer assessments unprompted. Ask questions, surface the rubric, let them do the honest looking. The user's growth comes from the looking, not from your verdict.

## The four pillars (the rubric)

**1. Technical Knowledge** — CS fundamentals; comfort with IDEs, build systems, debuggers, test frameworks; familiarity with CI, metrics, monitoring, configuration, packaging; proactive about test code; consider operations when making architectural decisions.

**2. Execution** — Solve problems with code that creates business value; ship small and medium features; write, test, and review code; share on-call duty; debug operational issues; proactive and dependable; participate in tech talks, reading groups, interviews, presentations.

**3. Communication** — Clear in writing and speech; give and receive feedback well; ask for help and clarification proactively; raise issues constructively; help others and start to influence peers; document work; write clear design docs and invite feedback; patient and empathetic.

**4. Leadership** — Work independently on well-scoped tasks; learn quickly from mistakes; handle change and ambiguity well; participate in project and quarterly planning; help new teammates onboard; give meaningful feedback to your manager.

## How to run the self-check

When this skill fires, walk the user through these steps. Do **not** dump all four pillars at once — go one at a time. Wait for the user's response before moving on.

### Step 1 — Frame the moment

Briefly note that you're going to walk through the four pillars from *The Missing Readme* as a self-check, that this is for *them* not for you, and that honest answers — especially the uncomfortable ones — are the whole point. Keep this to two or three sentences.

### Step 2 — Walk through each pillar, one at a time

For each pillar, in order (Technical Knowledge → Execution → Communication → Leadership):

1. State the pillar and its short definition (from the rubric above).
2. Ask: *"Where do you feel solid here, and where do you feel thin? Be specific — name examples from the last few weeks if you can."*
3. Listen. Reflect back what you heard in one sentence so they know you heard it.
4. Push gently if their answer is vague: *"solid"* → *"what specifically? give me an example"*; *"I'm not great at it"* → *"what's a recent moment that made you think that?"*
5. Do **not** grade them. Do **not** say "that sounds like a 7/10." You are a mirror with good questions, not a judge.

### Step 3 — Identify the weakest pillar

After all four, ask: *"Looking at all four, which one feels weakest right now?"*

If they hesitate or can't pick, offer to name what you noticed across their answers — but frame it as a question, not a verdict: *"It sounded like Communication came up a few times when you talked about 1:1s and design reviews — does that match how you feel?"*

### Step 4 — One concrete move

Ask: *"What's one concrete thing you could do in the next two weeks to strengthen that pillar? Not a goal — an action. Something with a verb and a deadline."*

- If they propose something vague (*"get better at design docs"*), push for the action: *"okay, what's the first design doc you'd write, and by when?"*
- If they can't think of anything, offer 2–3 small, time-boxed suggestions tied to the pillar — but let them pick, don't pick for them.

Examples of concrete moves by pillar (use only if the user is stuck):
- **Technical Knowledge** — Pick one tool you use daily but don't fully understand (e.g., your debugger, your build system) and read its docs cover-to-cover this week.
- **Execution** — Volunteer for one on-call shift in the next two weeks, or pick up one small bug from the backlog you'd normally skip.
- **Communication** — Write a short design doc for the next non-trivial change you make, even if no one asked for it. Share it and invite feedback.
- **Leadership** — Offer to onboard the next new teammate, or write down one piece of feedback for your manager and bring it to your next 1:1.

### Step 5 — Close

Summarize in two sentences: the weak pillar they identified, and the one concrete move they committed to. Offer to help them follow through if/when they come back. End there — do **not** lecture, do **not** add bonus advice.

## Output style

Follow the [Output Protocol](../../docs/METHODOLOGY.md#10-output-protocol). Specifically for this skill:

- **One question per turn.** This is a reflective skill; never ask about two pillars in the same message.
- **Walk through the four pillars one at a time** — each pillar is a separate turn, with the user's response shaping the next.
- Short prose, not bullet walls. The user is reflecting; they don't need a slide deck.
- No grades, scores, rankings, or unsolicited verdicts.
- Cite the source naturally if it comes up (*"the four pillars from The Missing Readme"*), but don't lead with attribution — lead with the question.

## When NOT to use this skill

- The user has a tactical question (*"how do I write a unit test"*, *"what's wrong with this code"*). Skip — those need real help, not a self-assessment.
- The user is venting or distressed about their job. Acknowledge what they're feeling first; don't immediately go into rubric mode. The skill can come later in the conversation if it's the right move.
- The user is asking about someone else's growth (a teammate, a report). The four pillars are still useful but this skill is designed for self-reflection, not evaluating others.
- The user is in impostor-syndrome territory ("I feel like a fraud", "everyone else seems to know more") or sounding overconfident in a way that hints at Dunning-Kruger. The self-check rubric assumes a clear lens; if the lens is distorted, the assessment will be too. Route to [`growth-obstacles`](../growth-obstacles/SKILL.md) first to calibrate, then come back here for the structured pass.
