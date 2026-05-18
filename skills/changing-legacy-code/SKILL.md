---
name: changing-legacy-code
description: Use when the user is about to modify existing code — especially code that is unfamiliar, untested, complex, or scary to touch — and wants to do it safely. Triggers include phrases like "I need to change this old code", "how do I refactor this safely", "this code has no tests how do I touch it", "I'm scared to change this", "about to modify a legacy system", "how should I structure this refactor", "how do I add a feature to this messy code", "should I rewrite this or work with what's there", or asking about safely changing existing code. Walks through Michael Feathers' Legacy Code Change Algorithm (identify change points, find test points, break dependencies, write tests, then make the actual change and refactor), the standard dependency-breaking techniques (extract methods, introduce interfaces, inject control points), the leave-cleaner-than-you-found-it discipline applied opportunistically, the incremental-PR rhythm, and pragmatism about when refactoring is worth the cost. Do not trigger for greenfield code, for tactical syntax or API questions, or for active code reviews (route to code-review).
---

# changing-legacy-code

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code." The five-step algorithm and dependency-breaking techniques come from **Michael Feathers, *Working Effectively with Legacy Code*** (Prentice Hall, 2004) — the canonical text on this topic. See [`READING-LIST.md`](../../READING-LIST.md) for the full reference.

## Pillars this skill strengthens

- **Primary:** Execution, Technical Knowledge
- **Also:** Communication (signaling intent through small commits and PRs)
- **Builds:** Leadership (modeling careful work on shared code)

## What this skill is for

Most production code is, in Feathers' famous definition, **legacy code: code without tests.** The fear of changing it is rational — there's no safety net to catch you when you break something. This skill fires when the user needs to change existing code and wants a structured way to do it without lighting things on fire.

It packages the well-tested algorithm for the task plus the smaller disciplines that make the algorithm actually work in practice (small commits, opportunistic cleanup, pragmatism about whether to refactor at all).

## The core mindset (lead with this)

**Legacy code is code without tests, not code that's old.**

- A piece of code written yesterday with no test is legacy. A 10-year-old module with thorough tests is not. Reframe accordingly.
- The fear of changing legacy code is rational and protective. Don't let bravado push you past it; use it as a signal that you need scaffolding first.
- **Tests are not just verification — they're scaffolding.** They let you change the code safely. The whole algorithm is about building the scaffold before doing the work.
- **Pragmatism matters.** Not every piece of legacy code needs the full treatment. Match the rigor to the risk.

---

## The Legacy Code Change Algorithm

The five steps, in order. The first four are about preparing the ground; the fifth is the actual change.

### 1. Identify change points

Where in the code do you actually need to make the change? Be specific. Often this is one or two locations, not "the whole module." Narrow the surface area first.

- *Useful question:* if your change works, what files and lines will have changed? List them.
- If you can't name the change points, you don't understand the change well enough yet. Step back and clarify.

### 2. Find test points

Where can you add tests that will catch breakage at (or near) the change points?

- Look for the **closest seam** to the change point — a function boundary, a class interface, an external API call — that's testable.
- The test point may be *further out* than the change point (e.g., you can test a higher-level function that calls the thing you're changing). That's fine, as long as the tests will actually catch your specific breakage.
- If you can't find any test points at all, you're in Feathers' "no seams" zone — Step 3 is exactly for this.

### 3. Break dependencies

Most legacy code is hard to test because it has dependencies that are inconvenient (databases, network calls, global state, time, randomness). You need to introduce **seams** — points where you can substitute the inconvenient real thing for a controlled fake.

**Three standard techniques:**

- **Extract methods.** Pull a large, complex method apart into smaller methods so each piece can be tested independently. The extracted methods often reveal what the original method *meant* to do.
- **Introduce an interface.** Define a small interface that captures only what the code actually needs from a complex collaborator. Tests can supply a simple implementation — incomplete but sufficient for the test.
- **Inject explicit control points.** For things that are hard to control by default (current time, randomness, scheduled callbacks), inject the source as a parameter or dependency. Tests can supply a fixed clock, a seeded RNG, a direct callback trigger.

### Anti-pattern — do **not** change access modifiers just to make tests easier

Making a `private` method `public` (or `protected`, or package-private just-for-tests) is a tempting shortcut. **Resist it.** It pollutes the production API forever to solve a test-only problem.

Better options:

- **Extract the inner logic** into its own class (or function) that's naturally testable at its proper level of abstraction.
- **Test through a public seam** that exercises the private method indirectly.
- If neither is reasonable, consider whether the private method should actually be its own class — that's often what the testability pain is telling you.

### 4. Write tests

Now that there are seams, **write tests that capture the current behavior** of the code you're about to change.

- These aren't tests of what the code *should* do — they're **characterization tests** of what it actually does today, including the quirks. The goal is a safety net for your refactor.
- Aim for tests at the change points and at the surrounding behavior that your change might disturb.
- Run them. They should pass against the unchanged code. If they don't, your understanding of current behavior is incomplete — fix that before going further.

### 5. Make changes and refactor

Now you can make the actual change. With the test net in place, you can:

- Make the change confidently. The tests will tell you immediately if something else broke.
- Refactor to improve the design — extract more methods, rename things, simplify control flow. The same tests verify nothing changed externally.
- Add **new tests** for the new behavior you introduced. Now both the old characterized behavior and the new behavior are covered.

Run the test suite **frequently** as you iterate — every few minutes, not at the end of the day. Cheap, fast tests run constantly are the whole point of the scaffold you just built.

---

## The smaller disciplines (alongside the algorithm)

### Leave code cleaner than you found it — opportunistically

The "boy scout rule" (attributed to Robert C. Martin / *Clean Code*): when you're already changing a piece of code, leave it slightly better than you found it. Rename the confusing variable. Pull the inline logic into a helper. Add the missing docstring.

**Be opportunistic, not crusading.** Don't go hunting for ugly code to fix — you'll lose the day. Clean what you're already touching, then move on.

**Separate cleanup commits from behavior changes.** If your work has two parts — *"extract `validateUser` from `signup`"* (no behavior change) and *"add email-confirmation step to signup"* (behavior change) — make them two commits. This is huge for reviewers and lifesaving for `git revert`.

For broader frustration with code mess, see [`software-entropy`](../software-entropy/SKILL.md). For mess that's risen to named technical debt that needs explicit work, see [`technical-debt`](../technical-debt/SKILL.md).

### Make incremental changes

- **Keep refactoring changes small.** A 200-line PR will get reviewed; a 2,000-line "refactor" PR sits open for a week and merges with regret.
- **Make separate PRs for each step of the algorithm** when the change is non-trivial. PR 1: "add tests around `processPayment`" (no behavior change, easy to review). PR 2: "extract `chargeCard` from `processPayment`" (no behavior change, easy to verify). PR 3: "use new payment provider in `chargeCard`" (the actual feature change, now isolated).
- **Smaller commits if the changes are hard to follow.** A PR that's hard to read at the diff level is a PR that won't get carefully reviewed.
- **Get buy-in from your team before a refactoring spree.** Unilateral large refactors create merge conflicts and political problems. A 10-minute conversation in standup is cheap insurance.

### Be pragmatic about refactoring

**Refactoring is not always wise, and not always a priority.** The cost can exceed the value:

- Code that rarely changes doesn't earn much by being refactored.
- Code that's about to be deleted shouldn't be refactored.
- Code that's "ugly" but doing a clear job that you don't fully understand yet — leave it until you understand it.

Match the rigor to the risk:

- **Critical or frequently-changed code** → full algorithm, characterization tests, careful steps.
- **Touched-occasionally code** → algorithm if non-trivial, lighter scaffolding if not.
- **About-to-be-deleted code** → don't refactor. Delete.

### Use an IDE

IDE refactoring tools (rename symbol, extract method, inline variable, change signature) are genuinely powerful and far less error-prone than doing those refactors by hand. Use them.

But know their limits:

- Automatic refactoring across reflection / dynamic dispatch / string-based references is unreliable. The IDE doesn't see those references.
- Anything that crosses a service boundary or uses serialized format → manual care.
- Run tests after every IDE refactor, even the "safe" ones.

---

## How to run

### Step 1 — Diagnose

Ask two questions:

- *"What are you trying to change, and what tests cover it today?"*
- *"How scared are you to touch it, on a scale of 'mild caution' to 'this could take down production'?"*

The answers tell you which steps of the algorithm to walk through and how much rigor to bring.

### Step 2 — Pick the right level

- **Low risk, well-tested area:** the user probably just needs the boy-scout reminder and a sanity check on PR structure. Skip the full algorithm.
- **Moderate risk, partial tests:** algorithm steps 2–5, plus a check that the test points are real.
- **High risk, no tests, scary code:** the full algorithm, especially the *break dependencies → characterization tests* loop.

### Step 3 — Walk through the relevant steps

For the steps that matter for their situation, ask the question for that step and help them answer it. Don't lecture — get them to do the thinking.

### Step 4 — Plan the commits and PRs

Before they touch code, sketch the commit/PR plan:

- *"What's PR 1, where does it stop?"*
- *"Is the behavior-change PR clearly separable from the cleanup?"*

For commit message and PR mechanics, route to [`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md).

### Step 5 — Close

Confirm the plan. Remind them to run tests after every IDE refactor, and to come back if they hit code where they can't find a seam.

## Output style

- **Be honest about pragmatism.** If their situation doesn't warrant the full algorithm, say so. The book and the algorithm are tools, not rituals.
- **Push them to find the seam themselves.** *"Where's the closest function boundary to your change point?"* teaches; *"add an interface around X"* doesn't.
- **Warn about the access-modifier trap.** If they mention "I can just make this public for the test," surface the anti-pattern explicitly.

## When NOT to use this skill

- The user is writing greenfield code — they don't have a legacy-code problem yet. Skip.
- The user is reviewing a PR (not authoring) — route to [`code-review`](../code-review/SKILL.md).
- The user is asking about commit messages or PR structure mechanics — route to [`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md).
- The user is doing a debt-paydown that needs management buy-in — route to [`technical-debt`](../technical-debt/SKILL.md), then come back here for the technique.
- The user has a tactical syntax/API question. Skip.

## Further reading

Surfaced as a primary reference but not yet folded in — see [`READING-LIST.md`](../../READING-LIST.md) for the full entry.

- *Working Effectively with Legacy Code* — Michael C. Feathers. The original source for the algorithm and the dependency-breaking techniques. Worth reading cover-to-cover; the depth far exceeds what this skill captures.
