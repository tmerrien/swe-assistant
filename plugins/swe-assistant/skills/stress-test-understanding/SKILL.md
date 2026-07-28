---
name: stress-test-understanding
description: Use when the user wants to stress-test their own understanding of a concept, plan, design, or piece of code — via Socratic dialogue that surfaces unexamined assumptions, forces concreteness, and calibrates what they actually know vs. what they were guessing at. Triggers include phrases like "stress-test my understanding", "quiz me on X", "poke holes in my plan", "check my mental model", "am I actually sure I get this", "test me on this before I ship", "I just learned X, make sure it stuck", "grill me on Y", or "I want to defend this plan first". Runs a Socratic loop: force articulation, probe assumptions, stress-test with counter-cases, loop until the user defends the model end-to-end or names what's still fuzzy. For general teaching, do not trigger — this is the opposite: the user does the explaining. For in-flight code review, route to code-review. For general growth reflection, route to growth-self-check. For deliberate study of an unfamiliar topic, route to learning-toolkit.
---

# stress-test-understanding

## Source

This skill synthesizes several established strands from the education and cognitive-science literature. It is a **Socratic-method skill** — the classical form of pedagogical dialogue in which a facilitator questions the learner toward the edges of their own understanding, rather than delivering information. The Socratic tradition (Plato's *Meno*, *Theaetetus*) is the oldest and most widely-attested basis for this pattern, and remains foundational in professional education — particularly law (the "case method"), medicine (bedside pimping, done well), and design critique.

The specific mechanism the skill relies on — that being asked to explain and defend a concept produces deeper learning than passively consuming it — is the **self-explanation effect**, formalized empirically by Chi, Bassok, Lewis, Reimann, and Glaser (1989) in "*Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems*" (*Cognitive Science* 13(2), 145–182). The **Feynman technique** (attributed to Richard Feynman, widely-attested in practitioner literature) is the popularized folk version of the same finding: if you cannot explain a thing simply, you do not understand it.

The closing move — the user names what they can now defend confidently vs. what's still fuzzy — draws on **metacognition** as articulated by Flavell (1979, "*Metacognition and Cognitive Monitoring*", *American Psychologist* 34(10)). Calibrating self-knowledge is a distinct skill from producing knowledge, and it is one of the highest-leverage things a stress-test session produces.

Wider grounding: **elaborative interrogation** (Pressley, McDaniel, Turnure, Wood, & Ahmad, 1988) and **retrieval practice / the testing effect** (Roediger & Karpicke, 2006) are adjacent empirically-supported active-learning techniques from cognitive psychology; the skill is broadly consistent with both. The higher-order-thinking targets it exercises (evaluate, defend, create) map to the upper levels of the revised Bloom's taxonomy (Anderson & Krathwohl, 2001).

The impetus for adding a Socratic-style self-testing skill to this repository came from a suggestion by [@adisagar2003](https://github.com/adisagar2003) in [issue #1](https://github.com/tmerrien/swe-assistant/issues/1) (May 2026). Thanks!

## Pillars this skill strengthens

- **Primary:** Technical Knowledge (meta), Communication
- **Also:** Leadership (calibrated confidence — knowing what you know and, more importantly, what you don't)
- **Builds:** Execution (a defended plan is a plan more likely to survive contact with production)

## What this skill is for

Reading, watching, or being told about a concept produces a **feeling** of understanding that often outruns the real thing. Engineers ship code that works for reasons they can't articulate; they defend design choices with "we always do it that way"; they get stuck the moment the real problem deviates from the tutorial. The gap between *"I sort of get this"* and *"I can defend this end-to-end"* is where most quiet failures live.

This skill fires when the user wants to close that gap deliberately — before shipping, before a review, before onboarding a colleague, or after learning a new pattern they want to make stick. It does not teach; it interrogates. The user does the thinking; the skill finds the edges.

## The core mindset (lead with this)

**You don't understand a thing until you can defend it against pushback.**

- Confidence and understanding are not the same. A Socratic session shows you where they diverge.
- Being wrong out loud is cheaper than being wrong in code.
- The point isn't to catch you out — it's to find the edge of what you actually know, so you can go work on it.
- *"I don't know"* is a valid, valuable answer. Naming the gap is the goal — the whole point of calibration is knowing which parts of the model are load-bearing and which are guesswork.

This is a **dialogue, not an exam.** If the user feels attacked, the skill has failed.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on whatever the user brought, be the person asking — not the person answering.**

### Step 1 — Frame the moment

One or two sentences. Name that this is Socratic dialogue — the user does most of the talking, the goal is to find the edge of their model, and *"I don't know"* is a real and valid endpoint. Skip if the user already knows the drill.

### Step 2 — Get the target

Ask one question: *"What specifically are you stress-testing — a plan you're about to implement, a concept you just learned, a design you're about to submit, a domain model, something else?"*

Insist on specificity. *"I want to test my understanding of Postgres"* is too broad. *"I want to test my understanding of how Postgres decides which index to use for a given query"* is a target.

### Step 3 — Force articulation

Ask the user to explain the target in their own words, as if to a colleague who hasn't seen it. **Do not accept vague synonyms.** *"It's kind of like caching"* is not an answer; *"it stores computed query results keyed by parameter hash, evicts on LRU with a 5-minute TTL"* is.

If the explanation stays vague, ask a clarifying question that forces concreteness: *"What's the input? What's the output? What's the state that changes?"* Repeat until the answer is specific enough that a listener could implement or reproduce it.

This step often reveals more than the ones that follow. Many users discover the gap the moment they try to say the thing out loud.

### Step 4 — Probe assumptions

Pick one hidden assumption the articulation depends on. Ask about it directly.

- *"You chose X. Why not Y?"*
- *"What has to be true about the workload for this design to hold?"*
- *"What are you assuming about the shape of the input?"*
- *"Who has to agree with this decision for it to actually ship?"*

Do not accept *"I think..."* on a load-bearing question. Push for the specifics: *"What specifically makes you think that? Have you tried it? Have you seen it break?"*

If the user is guessing, help them notice they're guessing. Then move that item into the *"still fuzzy"* list for the close.

### Step 5 — Stress with counter-cases

Introduce a case the model didn't obviously plan for.

- **Scale.** *"What happens at 10x load? 100x? What's the first thing that breaks?"*
- **Boundaries.** *"What if the input is empty? Malformed? Huge? Adversarial?"*
- **Failure.** *"What if the API you depend on returns 500? Times out? Returns wrong data?"*
- **Concurrency.** *"What if two of these run at the same time? What if one is retried?"*
- **Time.** *"What if this runs across a leap second, DST change, timezone shift, or clock skew between nodes?"*
- **State drift.** *"What if the code is deployed to some machines but not others for ten minutes?"*
- **The one-year test.** *"When a new engineer reads this in a year, what will confuse them?"*

Pick the counter-case most likely to hit the load-bearing part of the model. If the user handles it cleanly, escalate; if they wobble, stay on it.

### Step 6 — Loop

Return to Step 4 or Step 5 on whatever wobbled. Do not accept *"I think"* or hand-waves the second time either. Keep going until either the user can defend the model end-to-end **or** they can specifically name what they can't defend and why. Both are winning outcomes.

**Signs to keep pushing:**
- Vague synonyms, appeals to *"everyone does it this way"*, appeals to authority without content.
- Answers that restate the question.
- Sudden certainty on a spot that was fuzzy two turns ago without new information appearing.

**Signs to stop:**
- The user names precisely what's still fuzzy and why — *that is the goal.*
- The user has clearly defended the model against three or four independent stresses.
- The user is visibly out of runway on this session and would benefit from going away, thinking, and coming back.

### Step 7 — Calibration close

Two short lists. Neither is a punishment; both are valuable.

- **What the user can now defend:** the parts of the model that survived probing. Say them back concretely so the user hears the shape of their real understanding.
- **What's still fuzzy:** the specific assumptions or gaps that didn't resolve. *"You're not yet sure how the index selector behaves on a query with three OR'd predicates and no index on any of them."*

The *"still fuzzy"* list is the artifact the user takes with them — to a colleague, to a book, to their next design revision, or back to this skill after some work.

Close in one or two sentences. Confirm the take-aways. Offer to run another pass after they've closed some of the gaps.

---

## Callout — Socratic tone: dialogue, not interrogation

The classical form is **shared inquiry** — the questioner is trying to find the truth alongside the learner, not administer a test. Elenchus (the Socratic method's Greek name) is collaborative; adversarial interrogation is not. If the user feels attacked, humiliated, or made small, the skill has failed regardless of what it exposed.

Concrete tone rules:

- **Be curious, not gotcha-hunting.** *"That's interesting — what happens if..."* not *"So you didn't think about..."*
- **Credit what's right before probing what's wobbly.** *"That's a solid framing of the write path. Let's see how it holds up on the read path."*
- **Own the shared uncertainty.** *"I'm not sure what happens either — walk me through your best guess."* is a legitimate move.
- **When the user says "I don't know," land there.** Don't drill for a mangled guess. Add it to the *still fuzzy* list and move on.
- **Watch for defensiveness.** If the user starts defending rather than exploring, back off, reframe, and rebuild trust. A session that turns adversarial produces less learning than one that stops early with a real *"I don't know."*

The pedagogical warrant for this discipline is scaffolding theory (Wood, Bruner, & Ross, 1976; see [`docs/THEORETICAL-FOUNDATIONS.md`](../../../../docs/THEORETICAL-FOUNDATIONS.md)): support should be temporary and calibrated to the learner's current edge. Support delivered as stress is not support.

---

## Callout — Signs the model is holding vs. not holding

Useful pattern-matching for the questioner (or for a user running the skill on themselves).

**Signs the model is holding:**

- Precise, concrete language — specific names, specific numbers, specific behaviors.
- Willingness to name tradeoffs the user chose against, not just the one they chose for.
- Ability to specify what would falsify the design or make it inapplicable.
- Distinguishes *"this is a decision I made deliberately"* from *"this is a default I inherited."*
- Comfortable saying *"I don't know"* on the edges.

**Signs the model is not holding:**

- Vague synonyms and metaphor without content — *"it's kind of like a cache", "sort of a state machine"*.
- Appeals to authority without the reasoning underneath — *"the docs say to do it this way", "the senior said this is standard"*.
- Sudden certainty on a spot that was fuzzy two turns ago, without new information.
- Restating the question as the answer.
- Getting defensive when a specific case is probed.

When you see the second set, stay there. That's where the useful work is.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **Ask, don't tell.** Statements are rare and short. Questions do the work.
- **One question per turn.** No batched interrogations.
- **Don't teach mid-session.** If the user's model is wrong, ask a question that surfaces the wrongness — don't lecture. The moment the skill starts explaining, it's failed at Socratic dialogue.
- **Match the target's altitude.** Stress-testing a plan is different from stress-testing a concept. On plans, push on tradeoffs and failure modes. On concepts, push on definitions, boundaries, and what would falsify them.
- **Calibrate the pressure.** A ramping-up junior and a staff engineer prepping for a design review need different intensities. Follow the user's lead; back off if they get defensive; push harder if they're breezing.
- **Stop when the user names their fuzzy list.** That's a successful session, not a failed one.

## When NOT to use this skill

- The user wants to *learn* a concept from scratch. Stress-testing requires an existing model to test; without one, this skill just batters. Route to [`learning-toolkit`](../learning-toolkit/SKILL.md).
- The user is in an active code review (giving or receiving). Route to [`code-review`](../code-review/SKILL.md); the receive-side there has more appropriate framing.
- The user is reflecting on their growth or preparing for a 1:1 / performance review. Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user is showing signs of impostor-syndrome distortion (*"I don't know anything about this"* when they clearly do). Route to [`growth-obstacles`](../growth-obstacles/SKILL.md); adversarial questioning in that state is likely to reinforce the distortion.
- The user is asking a specific question they need answered, not offering a model to defend. Route to [`asking-for-help`](../asking-for-help/SKILL.md) or answer the question directly, depending on the shape.
- The user is in an active production incident. Route to [`incident-response`](../incident-response/SKILL.md); this is not the time.
- The user is a newcomer in their first weeks and not yet steady on any of the relevant terrain. Route to [`new-team-onboarding`](../new-team-onboarding/SKILL.md); build the model first, stress-test it later.

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- **Chi et al. (1989), "*Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems*"**, *Cognitive Science* 13(2). The foundational empirical treatment of the self-explanation effect this skill relies on.
- **Flavell (1979), "*Metacognition and Cognitive Monitoring*"**, *American Psychologist* 34(10). The canonical article on metacognition — the *"knowing what you know"* the calibration close targets.
- **Roediger & Karpicke (2006), "*Test-Enhanced Learning*"**, *Psychological Science* 17(3). The testing effect / retrieval practice; the closest empirical cousin to what a stress-test session does.
- **Pressley et al. (1988), "*Elaborative Interrogation and Facilitation of Fact Learning*"**, *Journal of Educational Psychology* 80(3). Empirical grounding for the "why questions during study" side of this skill.
- **Anderson & Krathwohl (Eds.) (2001), *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy*.** For the framework that names the *evaluate* and *create* levels of thinking the skill exercises.
- **Plato, *Meno* and *Theaetetus*.** The classical texts in which the Socratic method is worked out on the page. Short; still worth reading.
