---
name: choose-boring-technology
description: Use when the user is evaluating, proposing, or being pulled toward adding a new technology to a stack — a language, framework, database, library, build tool, or deployment platform. Triggers include "should we use X", "I want to introduce X to our stack", "let's switch from X to Y", or "what's the best language for this project". Covers innovation tokens and the ecosystem-maturity criteria — packaging, tooling, libraries, hiring, performance, integrations. Skip for questions about a tool already chosen, for code reviews, or for the broader should-we-change-this question (route to change-discipline).
---

# choose-boring-technology

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code" (Section: Avoiding Pitfalls). The framework comes from **Dan McKinley's *Choose Boring Technology***: http://boringtechnology.club/ (originally a talk and essay, 2015), **read in full and folded** — the innovation-token budget, the bipartite cost model, the right-tool-for-the-job refutation, the shared-platform argument, the two adoption questions, and the mastery curve are all his. See also the related [`change-discipline`](../change-discipline/SKILL.md) for the broader pitfalls. The construct-versus-artifact framing and the easy/simple distinction are from **Rich Hickey's *Simple Made Easy*** (Strange Loop, 2011).

## Pillars this skill strengthens

- **Primary:** Leadership (technology decisions are leadership decisions), Technical Knowledge (evaluating ecosystem maturity honestly)
- **Also:** Communication (writing the proposal for the team), Execution (understanding the real cost of adoption)

## What this skill is for

Engineers love new technology. New tech is shiny, new tech promises to solve the frustrations of the current stack, new tech makes you feel like you're on the leading edge. And occasionally, new tech is genuinely the right answer.

But the most expensive engineering mistakes are made by teams that adopt new technology too eagerly. This skill fires when the user is in (or proposing to enter) a new-tech-evaluation moment, and gives them the framework to decide honestly.

## The core mindset (lead with this)

**Boring isn't bad. Boring is well-understood.**

McKinley regrets the word — he does not mean dull, he means *known*. The boring option may well be bad; the point is that **you can list the ways it will let you down.**

- Boring technology has known failure modes. When it breaks, the failure looks like things that have broken before, and you (or the people you can ask) know how to fix them.
- New technology has unknown failure modes. When it breaks, you and your team are inventing the recovery — usually under pressure, usually at the worst possible time.
- **Both categories exist in everything**; the difference is quantity. Mature software has a bug tracker full of known problems nobody will fix, *and* unknown ones. New software has more of both — more known unknowns you could at least test for, and many more unknown unknowns you cannot, because you do not know they are a category of thing that happens.
- The "boring" tech in your stack is the result of survival. It's still there because it works well enough that nobody had a reason to replace it. That history is information.

The trap: judging new vs. boring on **feature comparisons** rather than on **failure-mode and ecosystem maturity**. Features are visible in marketing; failure modes are invisible until they happen to you.

**A second trap, and the harder one: judging a technology by what it is like to *write*.** Hickey's framing (*Simple Made Easy*, 2011) is that we assess constructs by the experience of using the construct — how fast it gets us going, how pleasant the API feels, how little we have to learn — when **the thing that actually ships is the artifact**. Does the software do what it should? Can it be changed? Can it be debugged at 3am by someone who did not write it? **Assess constructs by their artifacts, not by their authoring experience.**

This sharpens what *boring* is doing here. Boring technology is **easy** in Hickey's sense — near at hand, familiar, already installed — and that is a real operational virtue, because known failure modes are what you want under pressure. But easy is not **simple** (one braid, an objective property), and a familiar tool can be deeply entangled. **What decides it — with the scales weighted, which an earlier version of this skill understated.** If the risk you are managing is *operational* — unknown failure modes, nobody to ask at 3am — favour boring. If the risk is *structural* — this choice will braid concerns together for years — a simpler-but-less-familiar construct can be the right call. But McKinley's position is that operating costs dominate in practice, so the structural benefit has to beat the **full** cost of operationalising a new thing, not merely exist. Being genuinely simpler is necessary and not sufficient. See [`managing-complexity`](../managing-complexity/SKILL.md).

**Hickey and McKinley are not actually opposed here, and it is worth seeing why.** Hickey warns that comfort with a construct hides its entanglement; McKinley warns that frustration with a tool means you *know* it. Both are making the same underlying point from opposite ends: **your emotional response to a technology is not evidence about its quality.** Comfort conceals braids; friction signals familiarity earned.

---

## Callout — "The right tool for the job" is the trap, not the goal

The single most useful line in McKinley's talk, and the direct answer to *"you can't stop me using the best tool for this job."*

Model it as a bipartite graph: business problems on one side, technologies on the other. Every edge you draw is a technology choice, and every choice carries an **ongoing maintenance cost** as well as a benefit. The total cost of your engineering operation is the sum of those maintenance costs minus the velocity you get back.

Which strategy wins depends entirely on **which term dominates in reality** — and McKinley's argument, from having run this at scale, is that **the operating costs dominate.** Getting started with a technology is easy; running it at a professional level is not. So the right shape is a *small* set of technologies spanning the whole problem domain.

The conclusion is genuinely counterintuitive and worth stating plainly to anyone arguing the point:

> **None of the tools you pick may be the "right tool" for any individual job — and they can still be the right choice for the total set of jobs.**

Per-job optimality is the wrong objective function. Optimising each edge locally produces a stack nobody can operate.

**There is also a positive benefit, not just an avoided cost.** McKinley's example: Etsy built activity feeds on Memcached rather than adding Redis, which cost real extra work up front because Memcached is ephemeral and they had to handle data simply not being there. Usage later grew roughly twentyfold and nobody noticed — because the shared stack was being scaled horizontally anyway, by people who had no idea that feature existed. **A shared platform means other people's capacity work covers you for free.** A bespoke dependency means it doesn't, and the bill arrives when your team has moved on — and people are markedly less willing to clean up someone else's mess than their own.

---

## Callout — Innovation Tokens

The core concept from McKinley's essay. Worth installing as a vocabulary.

**Every team has a small, finite budget of innovation tokens.** An "innovation token" is what you spend when you introduce a non-boring choice into your stack — a new language, a new framework, a new database, a new build system, a novel architecture pattern.

- **The budget is roughly three, and it is not an annual allowance.** McKinley's claim is that early in a company's life you get *about three* — not three per year, three. This matters: an annual refill quietly licenses a steady drip of adoptions, which is the behaviour the concept exists to prevent.
- Tokens are **non-recoverable** for the lifetime of the choice — once you adopt the new thing, it's in your stack, with its full ongoing cost, for years.
- **Tokens spent on tech adoption are tokens not spent on innovative features.** Every "let's use this new database" decision is, in effect, a decision *not* to ship something else novel during that period.

**The implication:** spend tokens on the choices that genuinely differentiate your product or unlock something the boring options can't. Don't spend them on "this language is more elegant" or "I prefer this framework's syntax." Those don't earn tokens.

**And spend them on what the company is actually for.** McKinley's framing is that the mission consumes tokens before engineering gets any — a company trying to reshape an industry has already committed one or two to that. What remains for infrastructure novelty is the remainder, not the whole budget.

The honest test: *"If we only get about three of these, is this one of them?"* If no, the boring option wins.

---

## Callout — Every tool seems bad at first, and that is information

A pattern worth naming because it drives a specific, common, expensive mistake.

When you first put a technology into production, your experience of it gets worse, because you are steadily discovering its problems. The naive reading of that experience is *this tool is bad, we should try a different one for the next thing.* Act on that repeatedly and you wake up running nine alerting systems, none of which anyone understands well.

The new tool is not better. **You are simply not yet aware of the ways it will fail you.** And by switching at the bottom of the curve you never reach the part past it — the state where the problems are still there but feel manageable, which is what mastery actually is.

McKinley's conclusion is deliberately provocative and holds up: **the tool you should probably be using is the one you complain about most, because complaint is a symptom of knowledge.** A team's loudest frustration is usually attached to the technology they understand best.

**How to use this in a conversation:** when someone proposes replacing a tool they find frustrating, ask whether they can list its main failure modes. If they can, that is mastery talking and the frustration is the price of it. If they can't, the frustration is unfamiliarity, and the replacement will reproduce it in a new shape.

**The same curve has a builder's side.** If you are the one shipping the tool rather than adopting it, the dip is a design problem — see [`first-run-experience`](../first-run-experience/SKILL.md) on learnability as intercept, slope, and ceiling. Teams abandoning tools at the bottom of the curve is partly a consequence of products that were never designed to teach while being used.

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

### 2. Ask McKinley's question, then write the list

**"How would we solve this problem without adding anything new?"**

This is the source's own gate and it is sharper than it looks. It immediately exposes the case where the actual problem is *"we would like to use this technology"* wearing a business problem's clothes — and when that surfaces, the conversation can simply stop.

Assuming a real problem, the answer is rarely that it can't be done. With a functioning system of any complexity you can usually get there on the existing stack, possibly via some awkward manoeuvres. So:

**Write down every awkward thing you would have to do.** Actually write the list. It resolves in both directions, which is what makes it worth doing:

- Often the list turns out to be shorter and duller than it felt, and the boring path wins.
- Sometimes the list is genuinely grim, and now you have a written case for adoption rather than an urge.

If the boring solution gets most of the benefit, the new tech isn't earning its token.

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
- **Prove it in production at low risk first**, then grow confidence. The failure shape is deciding to adopt and then rewriting the application on it in one move.
- **If the new thing is redundant with something you already run, commit to removing the old one.** The goal is replacement, not two overlapping technologies maintained forever — which is how a stack silently accumulates. Commit to the reverse too: if it doesn't work out, rewrite back on the old tools.
- Budget the innovation token explicitly against a total of about three, not an annual allowance.

## How to run

### Step 0 — Establish that this is a conversation

McKinley's practical prescription, and he notes it is beyond many engineering organisations despite sounding trivial: **adding technology has to be a conversation with other people.** Technology choices have global effects on a company, so they are not an individual engineer's call and not a single team's call either.

If the user is describing a decision they are making alone, or a team making one unilaterally, name that first. Handing individuals free rein over infrastructure reads as freedom and functions as the opposite — the person choosing is binding everyone, including their future colleagues, to the operational work that follows.

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

See [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- *Choose Boring Technology* — Dan McKinley (http://boringtechnology.club/). **Folded.** Short, and worth reading in full even though this skill now carries its substance — the Etsy anecdotes do argumentative work that a summary cannot.
- *Simple Made Easy* — Rich Hickey (2011). **Folded.** Source of the construct-versus-artifact framing above.
