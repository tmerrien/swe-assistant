---
name: choose-boring-technology
description: Use when the user is evaluating, proposing, or being pulled toward adding a new technology to a stack — a new programming language, framework, database, library, build tool, deployment platform, or any meaningful new dependency. Triggers include "should we use [X framework / language / tool]", "I want to introduce [tech] to our stack", "let's switch from X to Y", "what's the best language for this project", "evaluating [tech] for [purpose]", or asking about the trade-offs of any new-tech adoption decision. Covers the boring-technology framework from The Missing Readme (Chapter 3, citing Dan McKinley's Choose Boring Technology) — innovation tokens, the ecosystem-maturity criteria (packaging, tooling, libraries, hiring, performance, integrations), and whether the technology earns its token. Skip for in-stack technical questions (how to use a tool already chosen), for code reviews, or for the broader question of "should we change X" that isn't specifically about technology adoption (route to change-discipline).
---

# choose-boring-technology

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code" (Section: Avoiding Pitfalls). The framework comes from **Dan McKinley's *Choose Boring Technology***: http://boringtechnology.club/ (originally a talk and essay, 2015). See also the related [`change-discipline`](../change-discipline/SKILL.md) for the broader pitfalls.

## Pillars this skill strengthens

- **Primary:** Leadership (technology decisions are leadership decisions), Technical Knowledge (evaluating ecosystem maturity honestly)
- **Also:** Communication (writing the proposal for the team), Execution (understanding the real cost of adoption)

## What this skill is for

Engineers love new technology. New tech is shiny, new tech promises to solve the frustrations of the current stack, new tech makes you feel like you're on the leading edge. And occasionally, new tech is genuinely the right answer.

But the most expensive engineering mistakes are made by teams that adopt new technology too eagerly. This skill fires when the user is in (or proposing to enter) a new-tech-evaluation moment, and gives them the framework to decide honestly.

## The core mindset (lead with this)

**Boring isn't bad. Boring is well-understood.**

- Boring technology has known failure modes. When it breaks, the failure looks like things that have broken before, and you (or the people you can ask) know how to fix them.
- New technology has unknown failure modes. When it breaks, you and your team are inventing the recovery — usually under pressure, usually at the worst possible time.
- The "boring" tech in your stack is the result of survival. It's still there because it works well enough that nobody had a reason to replace it. That history is information.

The trap: judging new vs. boring on **feature comparisons** rather than on **failure-mode and ecosystem maturity**. Features are visible in marketing; failure modes are invisible until they happen to you.

---

## Callout — Innovation Tokens

The core concept from McKinley's essay. Worth installing as a vocabulary.

**Every team has a small, finite budget of innovation tokens.** An "innovation token" is what you spend when you introduce a non-boring choice into your stack — a new language, a new framework, a new database, a new build system, a novel architecture pattern.

- A team has maybe **2–3 innovation tokens per year** in a typical environment. More if the team is large and senior; fewer if it's small or early-career.
- Tokens are **non-recoverable** for the lifetime of the choice — once you adopt the new thing, it's in your stack, with its full ongoing cost, for years.
- **Tokens spent on tech adoption are tokens not spent on innovative features.** Every "let's use this new database" decision is, in effect, a decision *not* to ship something else novel during that period.

**The implication:** spend tokens on the choices that genuinely differentiate your product or unlock something the boring options can't. Don't spend them on "this language is more elegant" or "I prefer this framework's syntax." Those don't earn tokens.

The honest test: *"If I could only make one non-boring choice this year, would this be it?"* If no, the boring option wins.

---

## Why new technology costs more than it looks

The headline cost of adoption is "learning the new thing." That's the small one. The hidden costs:

- **Ecosystem immaturity.** The library you need may not exist yet, or may be one developer's side project. Failures cascade through the gap.
- **Documentation gaps.** When something breaks at 2am, Stack Overflow has the answer for the boring choice and silence for the new one.
- **Engineer availability.** Hiring engineers who already know the boring stack is much easier than hiring for the new one. Your team's hiring cost goes up.
- **Tooling.** IDE support, debuggers, profilers, monitoring integrations — all mature for boring choices, often patchy for new ones.
- **Compounding context cost.** Every new engineer onboarded has to learn the non-boring thing on top of the boring things. The cost recurs forever.

These costs don't show up in any single decision moment. They show up across years, and they're typically much larger than the benefit that motivated the adoption.

## The ecosystem-maturity evaluation

When evaluating *any* new piece of technology, especially a language or major framework, the question is not "is this technology good?" — it's "is the **ecosystem around it** mature enough for our needs?" Specifically:

- **Packaging system.** How do you install, version, distribute, and resolve dependencies? Is this well-trodden ground?
- **IDE / editor support.** Syntax highlighting, refactoring tools, debugging integration, type-checking integration, autocomplete. Mature for boring choices; often missing or broken for new ones.
- **Library ecosystem.** Does the library you need exist? Is it maintained? Does it have more than one contributor? When was it last updated?
- **Testing frameworks.** Is there a default testing story that the community converges on?
- **Support services.** Hosting, deployment platforms, observability vendors — does the new tech integrate with the things you already pay for?
- **Engineer market availability.** Can you hire people who already know it, or will every hire need 3–6 months to ramp?
- **Performance characteristics.** Do you know how it behaves under load, under failure, under unusual workloads? Or only in benchmarks?
- **Integration with existing tools.** Can it interoperate with the rest of your stack, or does adopting it cascade into needing 4 other new things?

A new technology can be brilliant on the language-level merits and still be a bad adoption choice if the ecosystem isn't ready.

## The decision framework

When the user is considering a new-tech adoption, walk them through:

### 1. State the underlying need

What specifically are they trying to do that the current stack can't?

- *"Faster requests"* — measure first; the current stack may be fine.
- *"Cleaner code"* — that's a refactoring need, not a tech-swap need ([`changing-legacy-code`](../changing-legacy-code/SKILL.md)).
- *"Modern features"* — what specific feature, and is it actually load-bearing for the product?
- *"The new thing is better"* — better at what, specifically, by how much, measured how?

If they can't state the need precisely, the urge isn't ready to become a proposal.

### 2. Identify the boring alternative

Before evaluating the new thing, ask: **what's the most boring possible solution to this need within the existing stack?** Often it's a small extension, a known pattern, or a library that's already in use elsewhere in the codebase. If the boring solution gets you 80% of the benefit, the new tech probably isn't earning its token.

### 3. Apply the 10× test (Horowitz, via [`change-discipline`](../change-discipline/SKILL.md))

Is the new tech genuinely **10× better** at the specific underlying need than the boring alternative? Not 2× or 3× — *dramatically* better, enough to overcome the compound costs of adoption.

If the honest answer is "no, more like 2× better but it feels nicer to work with" — that's a token-not-earned answer.

### 4. Evaluate ecosystem maturity, not the language merits

Run the eight evaluation criteria above (packaging, IDE, libraries, tests, support, hiring, performance, integration). Score each honestly. A new tech that scores low on any 2–3 of these is going to bite the team for years.

### 5. Plan the adoption, if it passes

If it survives the test, treat the adoption as a real engineering project:

- Write a [`design-doc`](../design-doc/SKILL.md). Name the underlying need, the boring alternative, the proposed adoption, the trade-offs, the success criteria.
- Pilot it on **one bounded part** of the system first. Don't migrate the whole stack on the first try.
- Define rollback criteria upfront — what would make you decide to back out, and at what point.
- Budget the innovation token explicitly. That's now spent for this year; spend the others wisely.

## How to run

### Step 1 — Diagnose

Ask:

- *"What specifically are you trying to add or evaluate?"*
- *"What's the underlying need it's meant to solve?"*

The answers tell you whether this is a tactical question (which tool of two should we use) or a real adoption decision (let's bring a new technology into our stack).

### Step 2 — Surface the boring alternative

Often the most useful thing this skill does is help the user see they hadn't considered the boring option. Ask: *"What does the existing stack offer that solves 80% of this?"*

### Step 3 — Apply the framework

If it's a real adoption decision, walk through the 10× test and the ecosystem-maturity criteria. Don't lecture — ask the questions and let them answer.

### Step 4 — Land on a decision

The decision is one of:

- **No** — boring alternative is good enough; save the innovation token.
- **Maybe — pilot first** — adopt on a bounded slice of the system, with rollback criteria.
- **Yes** — full adoption, with a design doc and an explicit plan.

Help them pick the right one and name the next concrete action.

### Step 5 — Close

If they're moving forward, route to [`design-doc`](../design-doc/SKILL.md) for the proposal. If they're not, the decision *itself* is the deliverable.

## Output style

- **Don't be dismissive of the new tech.** Many engineers love new tech for genuine reasons (it might solve a real frustration with the boring stack). Honor the underlying need; question the proposed solution.
- **The 10× test is the most useful question you can ask.** Get specific about what "better" means and by how much.
- **Innovation tokens is a vocabulary worth installing.** Mention the concept by name; engineers who pick up the term tend to make better tech decisions long after this conversation.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user has a **tactical question** about a tool that's already in the stack (how to do X with Postgres / React / whatever) — skip; help them directly.
- The user is asking about **non-technology change** — process change, standard change, code rewrite — route to [`change-discipline`](../change-discipline/SKILL.md).
- The user is in an **active incident** — route to [`incident-response`](../incident-response/SKILL.md).
- The user is doing a **personal side project** for learning — the innovation-token math doesn't apply; learning new tech *is* the point. See [`learning-toolkit`](../learning-toolkit/SKILL.md) instead.

## Further reading

Surfaced as the primary reference but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md).

- *Choose Boring Technology* — Dan McKinley (http://boringtechnology.club/). The full essay and the related talks. The innovation-tokens concept and much of the surrounding argument originate here; the essay is short, punchy, and worth reading in full.
