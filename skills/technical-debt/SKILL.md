---
name: technical-debt
description: Use when the user is identifying, prioritizing, proposing, or trying to communicate about technical debt — work owed to fix shortcomings in existing code that the team is actively paying interest on. Triggers include phrases like "this is technical debt", "we have so much tech debt", "how do I get the team/manager to let us refactor X", "should we clean this up before adding the new feature", "is this technical debt or just code I don't like", "how do I prioritize debt vs features", "how do I write a proposal to fix this", or asking about the debt matrix or how to estimate the cost of debt. Walks through the principal/interest model, Fowler's technical debt quadrant (deliberate vs inadvertent × reckless vs prudent), the discipline of not over-using "technical debt" as a label, paying down debt incrementally (small commits and PRs rather than big-bang refactors), the 5-step framework for proposing and discussing debt payoff (state factually, describe risk and cost, propose solution, discuss alternatives, weigh trade-offs), and the warning that you'll often be asked to prove the benefits after the work. Do not trigger for generic frustration about messy code (route to software-entropy), for code reviews, or for tactical engineering questions.
---

# technical-debt

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code." The 2×2 quadrant is **Martin Fowler's "Technical Debt Quadrant"** — see https://martinfowler.com/bliki/TechnicalDebtQuadrant.html for the original.

## Pillars this skill strengthens

- **Primary:** Communication (writing and discussing debt proposals), Leadership (prioritization, advocacy)
- **Also:** Execution (actually paying down debt incrementally), Technical Knowledge (recognizing what crosses the line into debt)

## What this skill is for

"Technical debt" gets thrown around to mean any code anyone doesn't like. This skill fires when the user is actually working with the concept — identifying real debt, deciding what to pay down, or trying to make the case for fixing something. The work here is precision: real debt has a specific definition and a specific cost; treating everything as debt cheapens the language and makes it harder to get the actually-important debt addressed.

## The core mindset (lead with this)

**Real technical debt is code where the team is actively paying interest, or where there's a meaningful risk of triggering a critical problem.**

- *Not* technical debt: code you find ugly. Code in a style you wouldn't have chosen. Code that "could be cleaner."
- *Is* technical debt: code where every change takes longer than it should because of a shortcut taken earlier. Code where each new use of a component replicates and entrenches a workaround. Code where a fix has been deferred and now the risk of a serious failure is real.

**Don't dilute the term.** Calling everything "tech debt" weakens the phrase. When you say "this is technical debt and we need to address it," people should trust that you mean it — and that trust only exists if you don't use it casually.

## The principal/interest model

The debt metaphor is precise on purpose.

- **Principal** = the original shortcoming. The piece of code that was written quickly, or wrongly, or before the team understood the problem. Fixing it is the principal repayment.
- **Interest** = what gets paid every time someone touches that area. The extra time to make a change. The workarounds that complicate later changes. The bugs that keep recurring because the underlying issue hasn't been fixed.
- **Compounding** = when workarounds get replicated and entrenched. Now the original shortcoming is woven through five files instead of one, and fixing it has gotten more expensive.

**Useful diagnostic:** if you can't point at the interest being paid (slower changes, more bugs, risk of a known critical failure), it might not be debt — it might just be code you don't love. See [`software-entropy`](../software-entropy/SKILL.md) for the natural messiness that doesn't always rise to debt.

---

## Callout — Fowler's Technical Debt Quadrant

A 2×2 from Martin Fowler that helps you reason about debt by asking two questions: *did we know what we were doing?* and *did we mean to take this shortcut?*

|                    | **Reckless**                                   | **Prudent**                                                  |
|--------------------|-----------------------------------------------|-------------------------------------------------------------|
| **Deliberate**     | *"We don't have time to do design."*           | *"We need to ship this now, we'll do it properly later."*    |
| **Inadvertent**    | *"What's layering?"*                            | *"Now we know how we should have done it."*                  |

### Each quadrant explained

- **Deliberate + Prudent.** The team consciously took on debt with eyes open, because the alternative was worse (a missed market window, an unfixable customer issue). This is the "good" debt, *as long as the team actually goes back and pays it down.* If you take on prudent-deliberate debt and never repay, it silently becomes reckless.
- **Deliberate + Reckless.** The team deliberately skipped doing things right — not because of a real constraint, but because the team didn't want to or didn't know to do better. Most dangerous quadrant. The shortcut becomes culture.
- **Inadvertent + Prudent.** The team did their best and only later, with more knowledge, realized there was a better approach. *"We learned something."* This is debt that comes from honest growth. The fix is folding the lesson into the code as you get a chance.
- **Inadvertent + Reckless.** The team didn't even know enough to know they were taking on debt. Often a junior team or a domain new to everyone. The fix isn't (just) refactoring; it's training and code review and pairing — see [`learning-toolkit`](../learning-toolkit/SKILL.md) and [`code-review`](../code-review/SKILL.md).

### Why this matters

The quadrant guides what to *do* about a piece of debt:

- *Prudent debts* are paid down on schedule. Plan the work.
- *Reckless debts* require a culture or process change, not just code changes — otherwise they recur.
- *Deliberate debts* should be tracked and revisited.
- *Inadvertent debts* should be turned into shared lessons (a tech-talk, a doc, a pairing session).

---

## Some debt is unavoidable

You can't prevent every inadvertent mistake. The goal isn't *zero debt* — that's both impossible and (often) the wrong economic choice. The goal is **manageable, named, prioritized debt.**

A team that has a clear list of its top 5 debts, with rough cost-of-interest estimates and a plan for the top 2, is in much better shape than a team that pretends it has no debt.

## How to address debt — small, continuous, in-flight

**The wrong move:** wait until the world stops, declare "refactoring week," and try to fix everything at once. The world rarely stops, and large refactors create their own risks.

**The right move:** make minor changes and clear things up as you go.

- When you're already touching a piece of code, **leave it slightly better than you found it.** (Same principle as the continuous-refactoring move in [`software-entropy`](../software-entropy/SKILL.md), applied to specific debt.)
- Use **small independent commits and pull requests.** A 50-line cleanup PR will get reviewed; a 5,000-line "refactor" PR sits open forever and accumulates merge conflicts.
- **Bundle cleanup with adjacent feature work** when you can. *"While I was adding the new field, I also pulled the validation into its own function — separate commit, easy to review on its own."*
- For larger debt that can't be done in-flight, propose it deliberately. See the framework below.

## The 5-step framework for discussing debt

Whenever you want the team to invest in paying down a specific debt, walk through these five steps — preferably in writing, so the proposal can be evaluated thoughtfully rather than in a hallway.

### 1. State the situation factually

What is the debt? Where is it? What was the original shortcoming? Avoid loaded language. *"The auth helper has a copy of the user-validation logic that's now duplicated in three callers"* not *"the auth code is a mess."*

### 2. Describe the risk and the cost

This is the section that gets the proposal taken seriously. Specifically:

- **Cost of interest right now** — how is the team paying for this debt today? *"Every change to user validation requires updates in three files; we missed one in PR-1234 which caused incident X."*
- **Risk of leaving it** — what bad thing might happen if it stays? *"If validation drifts further out of sync, the next regression could be silent and customer-facing."*
- **Quantify where you can.** Estimated time tax, recent incidents related to this debt, frequency of touching the affected code.

### 3. Propose a solution

A specific, scoped fix. Not "refactor the auth code" — *"extract the validation into a shared function, update the three callers, migrate the tests. Estimated 2 days of work."* Show that you've thought it through.

### 4. Discuss alternatives

At least one or two. Just like with [`design-doc`](../design-doc/SKILL.md), naming alternatives shows you've considered the space:

- **Do nothing** (always include this — sometimes it's the right answer for now).
- A cheaper partial fix.
- A more thorough refactor.

For each, name the cost and the trade-off.

### 5. Weigh the trade-offs

Be honest about what your proposal costs (time away from features, risk of introducing bugs during the refactor) and what it pays for (lower future maintenance, lower regression risk). Don't sell — show the math.

### A writeable template

```
# Tech debt proposal: [short name]
Author: [your name]    Date: [today]
Status: Draft / In Review / Approved / Implemented

## Situation (facts)
[Where is the debt? What was the original shortcoming?
Plain factual description, no judgment.]

## Cost and risk
- Cost right now: [how the team pays interest today, with examples]
- Risk if left: [what bad thing might happen]
- Quantification (if available): [time tax, recent incidents, frequency]

## Proposed solution
- [Specific scoped fix, with rough estimate]
- [Implementation plan in 2–4 milestones if non-trivial]

## Alternatives considered
- **Do nothing:** [why this might be okay; why I don't think it is here]
- **[Cheaper alternative]:** [what it gets us, what it leaves]
- **[More thorough alternative]:** [what it gets us, what it costs]

## Trade-offs of the proposed solution
- Costs: [time, opportunity cost, risk of introducing bugs]
- Pays for: [maintenance reduction, risk reduction, capability unlocks]

## Success metrics (how we'll know it worked)
- [Specific, measurable. See callout below.]
```

---

## Callout — Expect to be asked about the benefits later

**You'll often be asked to demonstrate the benefits *after* the work is done.** This is normal, not unfair. Plan for it:

- **Define success metrics in the proposal.** Examples: change-related bug rate in the affected area, time-to-add-a-new-feature in that domain, build time, test runtime, number of files touched per typical change, on-call pages tied to the debt area.
- **Capture the baseline before you start.** *"In the last 3 months, this area had 7 bug reports and required touching 4 files per typical feature add."*
- **Measure again after.** Be ready with the numbers when someone asks.
- **If a metric didn't move, say so honestly.** "We didn't see the bug rate drop yet — it might still be early, or the refactor didn't actually attack the root cause" is far more credible than spin.

The engineers who pay down debt *and* show the receipts get to pay down more debt next time.

---

## How to run

### Step 1 — Diagnose: is this actually debt?

Ask the user: *"What's the specific cost the team is paying right now? And what's the risk if it stays?"*

If they can answer concretely, it's debt — proceed.

If they can't (it's just "ugly code" or "I don't like the style"), surface the [`software-entropy`](../software-entropy/SKILL.md) framing and the don't-dilute-the-term principle. Most "tech debt" isn't actually debt.

### Step 2 — Place it on the quadrant (briefly)

Just to surface what kind of debt it is and what the right approach is:

- Prudent debt → plan the payoff.
- Reckless debt → also fix the culture/process.
- Deliberate → schedule the revisit.
- Inadvertent → fold in the lesson team-wide.

### Step 3 — Decide: in-flight or proposal?

- **Small debt** that can be addressed while doing nearby feature work → leave it slightly better than you found it. No proposal needed.
- **Recurring or large debt** that needs explicit time and buy-in → write the proposal. Use the 5-step framework.

### Step 4 — If proposal: walk through the template

If they're writing a proposal, work through the template section by section. Push for specificity in the *Cost and risk* section especially — that's where most proposals are weakest.

### Step 5 — Plan the success metrics

Before they submit, make sure they've defined how they'll know the work worked. Refer to the callout above.

## Output style

- Skeptical, in a friendly way. Most claims of "technical debt" don't survive the "what's the interest being paid?" question. That's good — the discipline of asking it protects the term.
- For proposal-writing, **work on the actual draft with them** rather than lecturing about the framework. Apply the template to their situation.
- When the answer is "do nothing for now," say so. Not all debt is worth paying down right away. Help them decide which.

## When NOT to use this skill

- The user is just expressing frustration with messy code — route to [`software-entropy`](../software-entropy/SKILL.md) for the reframe.
- The user is reviewing a *current* PR — route to [`code-review`](../code-review/SKILL.md).
- The user is asking about balancing maintenance vs new work *in general* — that's [`owner-playbook`](../owner-playbook/SKILL.md) territory; this skill is for specific named debt.
- The user is asking how to refactor *while in the middle of doing it* — that's a tactical question, not a debt decision. Help them refactor.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../READING-LIST.md) for full entries.

- *Refactoring: Improving the Design of Existing Code* — Martin Fowler. The "code smells" vocabulary in this book sharpens the discipline of *recognizing* debt — distinguishing real structural problems from code you just don't like. The skill's diagnostic ("can you name the interest being paid?") gets much sharper with code-smell language.
- *The Mythical Man-Month* — Frederick P. Brooks Jr. Two relevant ideas: **Brooks's law** for thinking about why "throw more people at the debt" rarely works, and the general framing of essential vs accidental complexity that informs which debt is worth paying down at all.
