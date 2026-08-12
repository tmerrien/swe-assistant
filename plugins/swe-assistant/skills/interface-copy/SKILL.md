---
name: interface-copy
description: Use when the user is writing or revising the words inside a product — button labels, error messages, empty states, confirmation dialogs, permission prompts, form labels and helper text, tooltips, or notification copy. Triggers include asking what an error should say, what to call a button, what to show when a list is empty, saying a screen "feels off" or "sounds robotic" without knowing why, or reaching for a layout change when the text is what is failing. Leads with the observation engineers routinely miss — most of an interface is words, so the writing largely is the design. Covers scannability, addressing the user as "you", the read-aloud test, error messages that say what happened and what to do next, and when precision must beat warmth. Do not trigger for design docs, commit messages, or status updates, which have their own skills, or for marketing copy.
---

# interface-copy

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principle 6 (*Words matter*).

The **read-aloud test** arrives here by an unusually strong route: Paul Graham derives it for essays in *Write Like You Talk* (http://paulgraham.com/talk.html), and Pereyra derives it independently for interface copy. Two sources, different surfaces, identical diagnostic. Graham is already cited in [`design-doc`](../design-doc/SKILL.md) and listed in [`READING-LIST.md`](../../../../READING-LIST.md).

Plain-language practice converges with **W3C COGA**, *Making Content Usable for People with Cognitive and Learning Disabilities* — noted because it means this work serves accessibility and clarity at once, which is a useful argument when justifying the time.

The warmth-versus-precision resolution below is the maintainer's addition; the source raises the tension and does not settle it.

## Pillars this skill strengthens

- **Primary:** Communication
- **Also:** Execution (clear copy removes support load and error recovery cost)
- **Builds:** Leadership (whoever writes the words shapes what the product appears to be)

## What this skill is for

Engineers write interface text constantly — every button, every error, every empty state — and almost never treat it as a design task. When a screen is confusing, the instinct is to reach for layout, hierarchy, or a component change. Frequently the words are what failed.

This skill fires when someone is writing or revising text inside a product.

## The core mindset (lead with this)

**Most of an interface is words.**

- Labels, buttons, errors, empty states, confirmations, prompts, helper text. The visual layer that receives most of the attention is very often a container for text.
- That makes writing the highest-return interface skill to invest in, and the one most likely to be delegated to whoever happens to be typing.
- **The words are not applied to the design afterwards.** In most products they largely are the design.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Get the actual string

If they have not shown it, ask for it. Work on their text, not on the general principle.

- *"What does it say right now, and what is the user doing when they see it?"*

The second half matters as much as the first: the same words succeed or fail depending on what the user was trying to do.

### Step 2 — Apply the relevant test

Usually one of: does it say what happened and what to do next; does it survive being read aloud; is it precise enough for the stakes.

### Step 3 — Revise with them, not for them

Offer the diagnostic and one alternative as an illustration. Do not hand back finished copy for the whole screen — see Design Principle 3.1.

### Step 4 — Close

One concrete revision.

---

## The practices

### Address the user as "you"

*"Your shifts"*, not *"My shifts"* or *"User shifts"*. Second person makes the copy about the reader's goals rather than about the product's model of them. It is a small change that reliably shifts the register.

### Write for scanning, because that is what happens

People read on screen differently — more task-driven, more goal-focused, and rarely linearly.

- Simplify the language. Shorter words, shorter sentences.
- Keep it bite-sized. Chunk it.
- Label things; use lists where a list is what you mean.
- **Do not bury links inside long paragraphs** — a link is an action, and actions should be findable.

### Cut, then read it aloud

Edit at the sentence and paragraph level down to exactly what needs saying. Then **read the result out loud.** If it sounds like a person talking, it is finished. If it sounds robotic, legalistic, or like a system announcing itself, it is not.

This is the single most useful test here, and its independent arrival from essay writing and interface writing is good evidence it is load-bearing rather than a stylistic preference.

### Error messages have three jobs

The most commonly botched surface, and the one where users are least able to absorb a failure.

1. **What happened**, in the user's terms — not the exception name.
2. **Why**, if knowing helps them.
3. **What to do next.** An error that names a problem and offers no action has done half a job.

Avoid blame (*"you entered an invalid date"* → *"dates need to be in DD/MM/YYYY format"*). Avoid apology as a substitute for information — *"Something went wrong"* is not an error message, it is a shrug. If a support code is genuinely needed, give it *and* the human sentence.

See [`logging`](../logging/SKILL.md) for the parallel discipline aimed at the engineer at 3am, and [`input-validation`](../input-validation/SKILL.md) for what the API should return underneath.

### Empty states are onboarding

The first screen a new user sees is frequently empty, and an empty list that says *"No results"* has wasted the single best teaching moment in the product. Say what goes here, why it is empty, and what to do to change that.

## Callout — Warmth versus precision, and which yields

Interface copy is often asked to be warm *and* unambiguous, as though these were free of each other. They are not: evocative language tends to loosen, and precise language tends to dry out. They coexist, but only with effort, and sometimes they genuinely conflict.

**The resolution: in high-stakes, low-attention moments, precision wins outright, and warmth becomes a constraint on how the precise thing is said rather than a competing goal.**

Someone granting consent to share health information, confirming a shift they will be held to, or approving an irreversible action needs to be **certain** what they are agreeing to. Charm that introduces the smallest ambiguity there is a defect. Elsewhere — empty states, success messages, onboarding — warmth is cheap and worth having.

Practical version: **write the precise sentence first, then warm it without touching its meaning.** If warming it changes what it commits the user to, stop and keep the precise one.

## Callout — Plain language does double duty

The scannability practices above are also among the central recommendations of **W3C COGA** for people with cognitive and learning disabilities: simplify, chunk, make scannable, avoid burying meaning in prose.

This matters practically. Plain-language work is sometimes treated as a nice-to-have that loses to schedule pressure. It is simultaneously clarity work and cognitive-accessibility work, and that is a stronger argument for the time than either alone.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **Always ask for the actual string** before advising. Generic copy guidance is nearly useless.
- **Ask what the user is doing when they see it.** Context determines whether copy works far more than the words do.
- **Read it aloud, out loud, in your response.** Show the test being applied rather than describing it.
- **Offer one revision as an illustration**, not a full rewrite of their screen.
- **If the stakes are high, say precision wins** and do not soften it.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is writing a **design doc, RFC, or ADR**. Route to [`design-doc`](../design-doc/SKILL.md).
- The user is writing a **commit message or PR description**. Route to [`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md).
- The user is writing a **status update to a manager**. Route to [`working-with-managers`](../working-with-managers/SKILL.md).
- The user is writing **log lines**. Route to [`logging`](../logging/SKILL.md).
- The copy's purpose is to **pressure, shame, or obscure** — confirmshaming, false urgency, a deliberately confusing opt-out. Route to [`design-ethics`](../design-ethics/SKILL.md).
- The user is writing **marketing or brand copy**. Out of scope; see [`LIMITATIONS.md`](../../../../docs/LIMITATIONS.md) Section 8.
