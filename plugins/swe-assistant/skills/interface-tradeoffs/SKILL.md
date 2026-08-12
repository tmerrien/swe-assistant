---
name: interface-tradeoffs
description: Use when a user-experience or interface decision is genuinely contested and the user is choosing a direction — minimal versus rich, familiar versus distinctive, fast versus deliberately slowed, consistent with the design system versus differentiated from it, warm versus precise wording, or the expected solution versus the surprising one. Triggers include disagreeing with a designer or product manager about direction, "is this too plain", "are we allowed to break the pattern here", "which way should we go on this", or presenting one side of a known design argument and looking for agreement. States both positions, names what each buys and costs, identifies the condition that decides between them, then asks which situation the user is actually in. Do not trigger for settled questions with a better-supported answer, for purely technical architecture trade-offs, or when the user simply needs to know what to emphasize.
---

# interface-tradeoffs

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principles 3, 4, 9, 11 (*Less is more*, after Mies van der Rohe), 12 (*Less is a bore*, after Robert Venturi, *Complexity and Contradiction in Architecture*, 1966), 13, and 14, which the book presents as deliberate opposing pairs.

The skill's *shape* — hold both positions, supply the deciding condition, do not resolve — is [`METHODOLOGY.md`](../../../../docs/METHODOLOGY.md) **Design Principle 3.6**, *Preserve productive disagreement*, grounded in Perry's scheme of intellectual and ethical development (1970) at [`THEORETICAL-FOUNDATIONS.md`](../../../../docs/THEORETICAL-FOUNDATIONS.md) Section 4.2. That principle originated with this project's maintainer, from the observation that principles 11 and 12 are more useful held together than separately.

## Pillars this skill strengthens

- **Primary:** Communication, Technical Knowledge
- **Also:** Execution (a decision made knowing the counter-argument is a decision that survives review)
- **Builds:** Leadership (the ability to argue the other side is what makes someone credible in a disagreement)

## What this skill is for

Some interface questions have answers. These do not. Minimalism versus richness, familiarity versus distinctiveness, speed versus deliberate friction — competent practitioners hold opposing views on each, for defensible reasons, and the right answer depends on circumstances no general rule knows.

The failure this skill exists to prevent is not choosing wrongly. It is **choosing without knowing there was an argument** — which is how a design gets made on taste, defended on taste, and overturned on someone else's taste six months later.

## The core mindset (lead with this)

**The job here is not to pick a side. It is to know what each side buys, and to name the thing about your situation that decides it.**

- These arguments recur because **both positions are right somewhere**. A rule that resolved them permanently would be wrong half the time.
- **Whoever can argue the other side is the one who gets to make the call.** A design defended only by preference loses to the next person with a preference.
- The output of this skill is not a verdict. It is a **stated condition** — *"we are going minimal here because the user's attention is already committed to the task"* — which is a decision that can be written down, reviewed, and revisited when the condition changes.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Confirm the disagreement is real

**This step is load-bearing.** Not everything with two describable sides is contested. If one position is simply better supported, say so and stop — presenting a settled question as open is a failure of this skill, not its purpose.

Real: minimal versus rich, familiar versus distinctive, friction versus speed.
Not real: whether the interface should be usable, whether consent should be informed, whether errors should say what went wrong.

### Step 2 — Identify which tension is live

Match to the table below. If it is not there, the shape still applies: name both positions, name what each costs, find the condition.

### Step 3 — State both sides, then ask

Give each position its strongest form — including the one the user has already rejected. Then name the deciding condition and **ask which situation they are in.** One question.

### Step 4 — Check the bounds

Every one of these arguments happens between a floor and a ceiling. Confirm the floor holds before entertaining the argument at all.

### Step 5 — Close

Get the condition written down. *"We chose X because Y is true of our situation"* is the artifact — it belongs in the design doc or the PR description. See [`design-doc`](../design-doc/SKILL.md).

---

## The bounds — check these before arguing

Every tension below is an argument about the space between two fixed lines.

- **The floor is usability.** If the thing is hard to use, it is neither minimal nor rich — it is broken, and the argument is a distraction from the actual problem. Pereyra's own closing line on the minimalism debate. See [`interface-decisions`](../interface-decisions/SKILL.md).
- **The ceiling is MAYA** — Loewy's *Most Advanced Yet Acceptable*. Distinctiveness is bounded by what the audience will accept; past that line, novel reads as wrong rather than notable.

A great many design arguments dissolve once someone checks whether the floor holds.

## The standing tensions

### Minimal versus rich

**For minimal:** less to process, faster to learn, less to maintain, fewer states to test. Reduces load where load is expensive.

**For rich:** personality, differentiation, and expressiveness. Uniform minimalism is a large part of why current software looks interchangeable — and in a market where everything resembles everything, difference is what gets noticed.

**What decides it:** *is your risk that people bounce, or that people forget you?* Where attention is committed and the task is demanding — checkout, consent, an incident dashboard — minimal wins, because the load budget is already spent. Where you are competing for attention that has not been given yet, richness earns its cost.

**The engineer's version of this argument is usually different from how it gets phrased.** You are rarely choosing minimalism in the abstract; you are choosing whether to **accept the design system's defaults or deviate from them**. Deviation is an innovation-token spend ([`choose-boring-technology`](../choose-boring-technology/SKILL.md)) — it costs unfamiliarity and maintenance, so it needs to earn something specific.

> **Terminology warning.** Venturi's argument *for* complexity means richness and ambiguity. That is the opposite valence to complexity in [`managing-complexity`](../managing-complexity/SKILL.md), where it means cost — anything structural that makes a system hard to understand and modify. Both sources are in play in this repository. Do not let them collide.

### Speed versus deliberate friction

**For speed:** below roughly one second, a user's train of thought survives; productivity rises more than proportionally as response time falls. Friction taxes everyone, including the majority who meant to do the thing.

**For friction:** where an action is consequential, making someone slow down and attend is the point.

**What decides it:** **reversibility and blast radius** — not how dangerous the action feels. And check first whether the irreversibility can simply be removed: a soft delete with a retention window, a delayed execution with a cancel path, an expand-and-contract migration. **A reversible action needs no gate at all.** See [`operational-tools`](../operational-tools/SKILL.md) and [`metrics`](../metrics/SKILL.md).

### Familiar versus distinctive

**For familiar:** recognition is faster than comprehension. Conventional patterns are understood before they are read, and every deviation spends some of the user's relearning budget.

**For distinctive:** the unusual is what gets remembered. Convention is invisible, and invisible things do not get chosen.

**What decides it:** **is attention contested, and are your users captive?** Consumer products competing for a click need to be noticed. Internal tools, operational software, and anything people use because they must gain little from standing out and pay the unfamiliarity cost in full.

**Both sides have measurement behind them, and they genuinely point opposite ways.** Tuch et al. (*International Journal of Human-Computer Studies*, 2012) showed 119 real website screenshots at exposures as short as **17 milliseconds** and found that **prototypicality** — how much a page looks like what people expect for its category — already moves aesthetic judgment at that speed. The mechanism is **processing fluency**: things that are easier to process are experienced as more pleasant, and typicality is one of the properties that makes processing easy (Reber, Schwarz & Winkielman, 2004). Meanwhile the von Restorff effect is equally solid on the other side: what is *distinct* is what gets remembered.

So the honest statement is that **typicality is liked and distinctiveness is remembered**, and no design gets both for free. MAYA is the practitioner's compromise between exactly these two findings, which is a point in Loewy's favour.

> **One refinement worth carrying, because it is not the obvious guess.** At the very shortest exposures the dominant factor is not typicality but **visual complexity** — prototypicality is present at 17ms but weaker, and only becomes as influential as complexity when people are given longer to look. So if the risk is an instant bounce, **simplify first and conform second**. Typicality earns its keep over slightly longer encounters, not in the first blink.

### Warm versus precise wording

**For warmth:** copy that sounds like a person builds trust and makes a product feel considered.

**For precision:** ambiguity in an interface is a defect, and warmth tends to loosen language.

**What decides it:** **the stakes and the attention available.** In high-stakes, low-attention moments — a consent screen, a destructive confirmation, a shift someone is committing to — **precision wins outright**, and warmth becomes a constraint on *how* the precise thing is said rather than a competing goal. Elsewhere the two coexist with effort. See [`interface-copy`](../interface-copy/SKILL.md).

### The expected solution versus the surprising one

**For the expected:** it is understood immediately, and it is what was asked for.

**For the surprising:** the best answer to a real need is sometimes not the one anyone described — pinch-to-zoom solved a need nobody had articulated as a request.

**What decides it:** **does the unexpected solution serve a need you have actually observed?** A surprising solution to a real problem is innovation. A surprising solution to no problem is the thing [`managing-complexity`](../managing-complexity/SKILL.md) calls YAGNI, and it is bounded above by MAYA. The distinction is the *need*, not the novelty.

## Callout — When the user has already picked a side

Common and worth handling explicitly: someone arrives having decided, looking for support against a colleague.

Give them the strongest version of the argument they are opposing. Not to change their mind — they may well be right — but because **a position that has not survived its counter-argument is not yet a position.** Frame it as preparation: *"here is what they will say, and here is the condition that would make them right."*

If the deciding condition turns out to favour the other side, say so plainly. This skill is not a rhetoric service.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **Never resolve a genuine tension by fiat.** State both, supply the condition, ask. The user makes the call.
- **Do check whether the tension is real first.** Both-sidesing a settled question is the failure mode of this skill.
- **Give the rejected position its strongest form**, not a strawman that makes the user's existing view look better.
- **One question per turn** — usually the condition question.
- **Push the condition into writing.** A recorded rationale is what survives the next round of the same argument, and what stops it being relitigated.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The question is **settled**, not contested — whether to validate input, whether consent should be informed, whether an error should say what failed. Give the answer.
- The trade-off is **purely technical** — database choice, sync versus async, monolith versus services. Route to [`technical-design-process`](../technical-design-process/SKILL.md) or [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- The user needs to know **what to emphasize** rather than which direction to take. Route to [`rationing-attention`](../rationing-attention/SKILL.md).
- The disagreement is about whether a pattern is **manipulative**. That is not a legitimate two-sided design debate. Route to [`design-ethics`](../design-ethics/SKILL.md).
- The user is **starting** user-facing work and needs the frame rather than a specific call. Route to [`interface-decisions`](../interface-decisions/SKILL.md).
