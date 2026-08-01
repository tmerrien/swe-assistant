---
name: technical-design-process
description: Use when the user is working out WHAT to build, before or alongside writing it up — handed an ambiguous project, unsure where to start, trying to pin down the real problem, researching how others solved it, deciding whether to prototype, or struggling to find uninterrupted time to think. Triggers include "I've been asked to design X", "where do I even start", "I don't really understand the problem yet", "stakeholders disagree about what the problem is", "how do I research this", "should I build a prototype first", "how much should I polish this spike", "I can't get any deep work time", "maker's schedule", "how do I scope this", or "who do I need to circulate this to". Walks the design process from The Missing Readme (Ch. 10) — the spiral of solitary thinking and group discussion, defining the problem, doing research, running experiments, and protecting focus time. For structuring or writing the document itself, route to design-doc. For choosing a specific technology, route to choose-boring-technology.
---

# technical-design-process

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 10, "Technical Design Process."** The spiral framing (design alternates between solitary deep-thought work and collaborative group discussion, gaining clarity with each pass), the four thinking activities (define the problem, do your research, conduct experiments, give it time), and the widening circulation radius all come from this chapter.

**"Maker's Schedule, Manager's Schedule"** — Paul Graham (2009), http://www.paulgraham.com/makersschedule.html. Cited in the chapter as the anchor for why design work needs large protected blocks rather than the fragmented hour-by-hour calendar that managers run on.

For the design *document* — structure, template, review, pitfalls — see [`design-doc`](../design-doc/SKILL.md), which folds this chapter's writing material.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (the research and experimentation are how you learn the problem space)
- **Builds:** Leadership (defining a problem well, and aligning stakeholders on it, is leadership work)

## What this skill is for

Most bad designs aren't bad because the engineer chose the wrong pattern. They're bad because the engineer started designing before they understood the problem — or designed alone, in one pass, and only discovered what everyone else knew after implementation started.

The design process is the antidote, and it is **not a linear pipeline.** It's a spiral that alternates between two modes: solitary deep thought, and collaborative discussion. Each pass around adds clarity and detail. The design document is the accumulating record of that spiral, not a thing you write once at the start.

This skill fires when the user is somewhere in that spiral and needs to know what the next turn looks like — usually because they've been handed something ambiguous and don't know where to begin, or because they're stuck in one mode (thinking alone forever, or discussing endlessly without deciding).

## The core mindset (lead with this)

**Design is a spiral, not a line. The document is the record; the thinking is the work.**

- The first goal is not a solution — it's to **learn**. Certainty and clarity are what you're accumulating, and early on you have very little of either.
- **Alternate deliberately.** Solitary thinking generates; group discussion corrects. Doing only one of them produces either an unreviewed fantasy or a design-by-committee mush.
- **Writing surfaces unknowns.** Half the value of drafting is discovering the questions you didn't know you had. That's not a sign you started too early — it's the process working.
- **You will be wrong about things, and implementation will prove it.** The doc gets updated. A design document that stopped changing when coding started is abandoned, not finished.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual project, skip diagnosis when their first message already places them.**

### Step 1 — Frame the moment

One or two sentences. Name the spiral, and that the first job is to *learn*, not to solve. Skip if the user is already on a specific question.

### Step 2 — Locate them on the spiral (one question, only if needed)

The turns, roughly in order:

1. **Learning** — research, experimentation, brainstorming toward a preferred direction.
2. **Sanity check** — run the preferred direction past someone before investing in writing.
3. **Drafting** — writing surfaces unknowns; prototypes answer them and settle choices between viable alternatives.
4. **Proposal** — enough confidence to circulate for real feedback. Research and discussion continue.
5. **Wide circulation** — security, operations, adjacent teams, architects.
6. **Implementation** — surprises surface, design decisions continue, the document keeps getting updated.

If ambiguous, ask **one** question — e.g. *"Where are you — still working out what the problem actually is, exploring approaches, or do you have a direction you're ready to write up?"*

Two common stuck patterns worth naming when you see them:

- **Stuck solitary.** Weeks of thinking, nothing circulated. The fix is a sanity check *now*, however rough.
- **Stuck collaborative.** Endless discussion, no one has done the deep work. The fix is a protected block (Step 6) and a written position.

### Step 3 — Define the problem

This is where most design failures originate. Do not let the user skip it.

- **Understand the boundaries.** What's inside this problem and what's adjacent to it?
- **Ask stakeholders what *they* perceive the problem to be.** Not what solution they want — what problem they think exists. Different stakeholders will give you materially different answers, and that divergence is itself the finding.
- **Restate the problem in your own words, back to them.** If they don't recognize their problem in your restatement, you don't have it yet. This single move catches more misunderstandings than any other.
- **If there's more than one problem, establish priority.** Which one, if solved, makes the others smaller or irrelevant?
- **Ask: "what happens if we don't solve this?"** The answer sizes the problem honestly, and occasionally reveals that the right move is to not solve it.
- **Synthesize into a clear problem statement.** Think critically about what you've been told — stakeholders describe symptoms and preferred solutions, not root problems. Pay close attention to scope.
- **Write it down and circulate it.** The problem statement is your first artifact and your first alignment checkpoint. Getting agreement here is far cheaper than discovering disagreement after you've designed a solution.

See the *Callout — Problem-definition questions* below for the questions in usable form.

### Step 4 — Do your research

- **Look at how others solved similar problems.** Other companies, engineering blogs, open-source implementations. Most problems are not novel; the novel part is usually your constraints.
- **Go past blog posts.** Conference talks (slides and recordings), and academic papers — including the papers those papers cite. The reference chain is where the depth is.
- **Talk to people who know the problem space.** Inside your company and outside it. A twenty-minute conversation with someone who has already made this mistake is worth days of reading.
- **Consider alternatives and trade-offs explicitly**, not just the approach you already like.
- **Think critically about all of it.** Another company's solution encodes their constraints, their scale, and their org chart. Ask what's different about yours before borrowing.

If the research is converging on adopting a new technology, route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md) for that decision specifically.

### Step 5 — Conduct experiments

Prototypes turn arguments into evidence. When two approaches both sound reasonable, build enough of each to find out.

- **Write draft code, draft APIs, partial implementations.** Enough to make the idea concrete or to expose where it breaks.
- **Run performance tests** where the question is "will this be fast enough," and **A/B tests** where the question is "will users behave the way we think."
- **Circulate the prototype.** A prototype your team can poke at generates far better feedback than a paragraph describing the same idea.
- **Do not get attached to experimental code.** Its purpose is to illustrate or test an idea, then die. Don't write tests for it, don't polish it, don't let it become the implementation by accident. See the callout below.

### Step 6 — Give it time, and protect it

Design is the work that fragmented time destroys most completely.

- **You need large chunks, not scattered hours.** Paul Graham's *"Maker's Schedule, Manager's Schedule"* (http://www.paulgraham.com/makersschedule.html) is the canonical statement: managers run on hour-slot calendars, makers need half-day units, and a single meeting dropped in the middle of a maker's afternoon can cost the whole afternoon.
- **Find when *you* concentrate best** — early morning, late evening, whenever — and **block it on your calendar** as a recurring commitment. Protect it the way you'd protect a meeting with your director.
- **Cut the interrupts for the duration.** Close chat, close email, silence the phone. The point isn't discipline theatre; it's that deep design thinking has a long spin-up time and every interrupt pays it again.
- **Have your tools ready before you start** — whiteboard, notebook, paper. Hunting for a marker at minute three breaks the state you just spent twenty minutes entering.
- **Take breaks.** Sustained concentration is finite, and design problems notoriously resolve during the walk rather than at the desk.

### Step 7 — Circulate at a widening radius

Each turn of the spiral shares with a wider audience:

1. **One trusted person** — the sanity check, before you've invested in writing.
2. **Your immediate team** — rough draft, looking for direction.
3. **Reviewers and stakeholders** — the real proposal.
4. **The organization** — **security, operations, adjacent teams, and architects need to be made aware of changes that affect them.** This step is the one engineers most often skip, and it's where late, expensive objections come from.

Don't jump to step 4 with a first draft, and don't stay at step 1 until implementation.

### Step 8 — Keep going after implementation starts

Implementation surfaces surprises, and surprises are design decisions. The spiral doesn't stop at the first line of production code — it just gets tighter. Update the document as the design actually changes. See [`design-doc`](../design-doc/SKILL.md) for keeping the document alive.

### Step 9 — Pick one action, then close

Ask: *"What's the one move that takes you round the next turn?"* Push for concreteness.

- *"Do more research"* → too vague.
- *"Write the problem statement in three sentences and send it to the two stakeholders by Thursday"* → the action.
- *"Block 9–12 Tuesday and Thursday for design, and build the throwaway spike comparing the queue-based and polling approaches"* → the action.

Close in one or two sentences. If they're ready to write the thing up, route to [`design-doc`](../design-doc/SKILL.md).

---

## Callout — Problem-definition questions

Ask these of stakeholders, and of yourself. In roughly this order.

**To stakeholders:**

- *"What problem are you trying to solve?"* — note when the answer is actually a solution, and gently ask what it would fix.
- *"What happens if we don't solve this?"* — the honest sizing question.
- *"Who else is affected by this?"* — surfaces stakeholders you didn't know you had.
- *"What have you already tried?"* — prevents you rediscovering a dead end.
- *"How will you know it's solved?"* — turns a vague ask into something testable.

**Back to stakeholders, after listening:**

- *"Here's the problem as I understand it: [restatement]. Is that right?"* — **the single highest-value question in the whole process.** If they hesitate, you're not done.

**To yourself:**

- What's *in* scope, and what's adjacent but out?
- If there are several problems here, which one, if solved, shrinks the others?
- What am I being told is the problem that is actually a symptom?
- What constraints are real, and which ones are just how it's currently done?

Then write the problem statement — a few sentences, no solution in it — and circulate it before you design anything.

---

## Callout — Prototype discipline

Experimental code exists to answer a question and then be deleted. The failure mode is letting it quietly become the implementation.

**Do:**

- Build the smallest thing that answers the question — *"is this fast enough,"* *"does this API feel right,"* *"do these two approaches actually differ in practice."*
- Build competing prototypes when choosing between viable alternatives. Comparative evidence beats argument.
- Show it to people. A running thing generates real feedback; a description generates polite nods.
- Timebox it. A prototype with no deadline becomes a product with no tests.

**Don't:**

- Write tests for it. It isn't going to production.
- Polish it, refactor it, or handle edge cases. Every hour spent making throwaway code nice is an hour not spent learning.
- Get attached. The most dangerous prototype is the one that works well enough that shipping it starts to feel reasonable.

**The trap:** a successful prototype creates enormous pressure to ship it as-is — it demos well and it "already works." Name this risk out loud with your team before you start, and decide up front whether the prototype is throwaway or a genuine first increment. Both are legitimate; confusing them is not.

If prototype code does become the implementation, treat it as deliberate scope: it now needs tests ([`writing-tests`](../writing-tests/SKILL.md)), and the shortcuts you took are now [`technical-debt`](../technical-debt/SKILL.md) to be tracked rather than forgotten.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't recite the spiral stages as a menu.
- **Work on their actual problem.** If they describe the project, help them draft *their* problem statement — don't hand back a generic checklist.
- **Push back on premature solutions.** If the user's first message describes a solution rather than a problem, that's the thing to address, gently: *"What problem does that solve?"*
- **Don't let "do more research" become procrastination.** Research is bounded by the decision it serves. Ask what question the research is meant to answer.
- **Take the time problem seriously.** If the user genuinely cannot get uninterrupted hours, that's a real constraint worth engaging with — often a conversation to have with their manager, not a personal failing.
- **Calibrate.** A senior engineer who has scoped many projects doesn't need the problem-definition primer; they may just want a sparring partner on the trade-offs.

## When NOT to use this skill

- The user is structuring, writing, or reviewing the design document itself. Route to [`design-doc`](../design-doc/SKILL.md).
- The decision is specifically whether to adopt a new language, framework, database, or tool. Route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- The user is weighing a rewrite, a fork, or bypassing a team standard. Route to [`change-discipline`](../change-discipline/SKILL.md).
- The user is scoping a project they've already designed, or running it. Route to [`owner-playbook`](../owner-playbook/SKILL.md).
- The user is trying to learn an unfamiliar codebase or domain generally, not to design a specific change. Route to [`learning-toolkit`](../learning-toolkit/SKILL.md).
- The user wants their reasoning adversarially tested rather than developed. Route to [`stress-test-understanding`](../stress-test-understanding/SKILL.md).
- The change is small, local, and reversible. There's no design process to run — just build it.

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- **"*Maker's Schedule, Manager's Schedule*"** — Paul Graham (2009), http://www.paulgraham.com/makersschedule.html. Short essay; the canonical argument for why design work needs half-day blocks and why a single mid-afternoon meeting is more expensive than it looks.
