---
name: owner-playbook
description: Use when the user is in the Owner stage — trusted to drive small projects, design software, and think about the system rather than just code in it. Triggers include being asked to drive (or about to take on) a small project end-to-end, asking how to approach the design phase before coding, asking about exploring trade-offs or planning for system evolution, identifying flaws in the current architecture or build/deploy/test environment, asking how to balance new feature work with maintenance or refactoring, thinking about team process improvements they want to bring to a 1:1, or preparing for a longer-term performance review with peer feedback or a career conversation about future projects and aspirations. Walks through the Owner playbook from The Missing Readme — driving projects, system design thinking, critical analysis of the architecture, the maintenance vs new-work balance, team-process improvement, and career conversations. Routes to design-doc for design documents, code-review for review situations, growth-self-check for personal-growth reflection. Do not trigger for tactical engineering questions or earlier-stage situations.
---

# owner-playbook

## Source

*The Missing Readme*, Chapter 1, "The Journey Ahead" — the **Owner** stage (the book calls this "Competence Cove"). This is the final stage of Chapter 1's journey map. Future book chapters will deepen specific situations rather than add new stages. See [`JOURNEY.md`](../../JOURNEY.md).

## Pillars this skill strengthens

- **Primary:** Execution, Communication, Leadership
- **Also:** Technical Knowledge (architectural thinking, trade-off analysis)

## What this skill is for

The Owner stage is the shift from "I ship features that work" to "I think about the system and how it should evolve." You're trusted to drive small projects, expected to design before building, and starting to shape how the team itself works. Career conversations get longer-term: not just what you're doing this week, but where you want to be in two years.

This skill fires when the user is in (or asked about) that mode. It coaches the breadth — but routes aggressively to focused skills (design docs, code reviews, growth reflection) when those situations are the real ask.

## The core mindset (lead with this)

**Think about the system, not just your code in it.**

- A good Owner is curious about *why* things are the way they are — and willing to invest in changing them when the answer is "historical accident."
- The hardest skill at this stage is **judgment about where to spend time.** Refactor or ship? Improve the build or document the existing one? Push for a process change or let it ride? There's no formula; the practice is the job.
- **Driving a project means saying what's in and what's out, on paper, before the work starts.** That's harder than it sounds.
- **You influence the team now, just by paying attention.** Your reactions in standup, your comments in design reviews, your choice of what to refactor — these signals shape what your teammates think is normal. Use that intentionally.

## How to run the playbook

### Step 1 — Frame the moment

Two or three sentences. Name the shift (shipping → thinking about the system). Tell them you'll tailor.

### Step 2 — Ask where they are

Useful framings:

- About to take on a project to drive end-to-end?
- In the design phase of something — wondering how to think through it?
- Looking at the codebase or pipeline and seeing real problems, but unsure when/whether to push for fixes?
- Trying to figure out the maintenance vs new-feature balance?
- Have ideas about team process you want to bring to a 1:1?
- Performance review prep or career conversation with manager?

### Step 3 — Surface the relevant moves

Pick 2–3 sections. Don't dump.

#### Driving a small project

- **Scope first, code second.** Before any commits: write the goal, what's in scope, what's *out* of scope, the rough plan, the unknowns, the success measure. Half a page. This is your project's spine.
- **Get a second opinion on the scope before you start.** Manager, tech lead, a senior teammate. Five minutes of their time saves you weeks of building the wrong thing.
- **Cut the work into pieces you can ship.** A project that ships nothing for six weeks is a risk; one that ships small pieces every week is a feedback loop.
- **Communicate proactively.** A weekly note on what's progressed, what's next, what's stuck. Use the rhythm you set with your manager (see [`ramp-up-playbook`](../ramp-up-playbook/SKILL.md) status communication callout if needed).

#### Designing software (and writing it down)

- **Design before you build.** Even small projects benefit from 30 minutes of "what are the options here, and what are the trade-offs?" Big projects benefit from days.
- **Write a design doc** for anything that touches more than one component, has reasonable alternatives, or affects other people's code. The doc isn't paperwork — it's the artifact of your thinking, and it makes you a better thinker. **For how to write one, route to** [`design-doc`](../design-doc/SKILL.md).
- **Always have at least two options.** A design that considers only one solution looks like you didn't think hard enough. Even if Option A is obviously right, naming Option B and why it's worse is *evidence of judgment.*
- **Plan for evolution.** Ask: "what does this need to look like a year from now?" The answer might be "exactly the same." Often it isn't, and shaping the design for the likely future is cheap now and expensive later.

#### Seeing flaws (and what to do about them)

When you start spotting real problems in the architecture, build, deploy, or testing setup:

- **Write them down.** A list of "things I'd fix if it were up to me" is the seed of your future tech debt backlog.
- **Pick your battles.** Not every flaw is worth fighting now. Ask: cost of leaving it × likelihood of biting us vs. cost of fixing × disruption.
- **Bring the highest-leverage one to a 1:1 or a planning session** with a small concrete proposal. *"This thing is costing us X — here's a 2-day fix that would change Y. Worth doing this quarter?"* That's how junior-to-mid engineers earn the right to influence direction.

#### The maintenance vs new-work balance

This is one of the hardest judgment calls in engineering. A useful frame:

- **Maintenance work is invisible until it breaks.** Refactor, dependency upgrades, build cleanup, test cleanup, documentation. The team that ignores it becomes the team that can't ship.
- **New work is visible and counted.** Features get demoed; refactors don't.
- **Healthy teams allocate explicit time** to maintenance — usually 20–30% of capacity. If your team doesn't, it's quietly accumulating debt.
- **Your move:** when you spot maintenance that's worth doing, bundle it with adjacent feature work where possible (refactor the function while you're already changing it). For bigger items, bring them to planning with a concrete cost estimate.
- For *specific named debt* (where the team is actively paying interest, not just code you find ugly), route to [`technical-debt`](../technical-debt/SKILL.md) — it has the discussion framework and a proposal template. For frustration with code mess that isn't yet specific debt, [`software-entropy`](../software-entropy/SKILL.md) has the reframe.

#### Team process thinking

You're now paying attention to how the team works, not just what it ships. Things to notice:

- Do retros produce action items that actually happen, or do they evaporate?
- Are standups useful, or have they become reports to the manager?
- Are design reviews catching real issues, or are they rubber stamps?
- Is the on-call rotation fair?
- Are people getting feedback they can act on?

When you notice something, **bring it to a 1:1 with a small specific suggestion**, not a complaint. *"I've noticed retro action items don't get followed up on. What if one person owned tracking them across retros?"* That's a contribution. *"Retros suck"* is venting.

#### Performance reviews and career conversations

This stage is when career conversations get longer-term. For:

- **The actual self-assessment** (where am I solid, where am I thin) → use [`growth-self-check`](../growth-self-check/SKILL.md). It's designed exactly for this.
- **Performance review prep specifically** (gathering peer feedback, framing impact for the review) → growth-self-check covers the reflection; this playbook can help you frame impact in terms of project outcomes if you want.
- **Career aspirations conversations with manager:** the most useful thing you can do is **come with a hypothesis, not a question.** *"I think I'd grow most over the next year by leading a slightly bigger project — something like X. Does that match what you see?"* gets a much better response than *"What should I do next?"*

### Step 4 — Pick one move for this week

Ask: *"Out of everything we covered, what's one thing you'll do this week? Be specific."*

Push for concreteness:

- *"Be a better designer"* is too vague.
- *"Write a one-page design doc for the X change by Friday and share it with [tech lead]"* is the action.

### Step 5 — Close

Two sentences: confirm the action, offer to come back when they want a second pair of eyes (especially on the design or the project plan).

## Output style

- Conversational. Surface only the relevant section based on where they are.
- **Route aggressively.** Design doc questions → [`design-doc`](../design-doc/SKILL.md). Personal-growth reflection → [`growth-self-check`](../growth-self-check/SKILL.md). Code review questions → [`code-review`](../code-review/SKILL.md). Don't duplicate what other skills already do.
- For big trade-off questions ("should I refactor this or ship that?"), help them name the trade-off explicitly rather than answer for them. Owner-stage growth comes from making the call themselves with better frames.

## When NOT to use this skill

- The user is in earlier stages (Newcomer through Operator). Route to the appropriate playbook.
- The situation is specifically a code review, design doc, or self-reflection. Route to the dedicated skill.
- Tactical engineering question with no Owner-stage framing. Skip.
