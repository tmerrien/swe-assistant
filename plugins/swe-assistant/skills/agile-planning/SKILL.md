---
name: agile-planning
description: Use when the user is planning or estimating work inside an agile process — writing or reviewing a user story, being asked for a story point estimate, breaking down or sizing work, grooming a backlog, scoping a spike, or contributing to a roadmap. Triggers include "how do I estimate this", "what's a story point", "sprint planning", "we always overcommit", "acceptance criteria", "should this be a spike", "our sprints never finish", or "scrum vs kanban". For standups, reviews, and retrospectives, route to team-rituals. For deciding what to build at all, route to technical-design-process.
---

# agile-planning

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 12, "Agile Planning."** The Scrum walkthrough (prework, stories, spikes, tasks, story points, backlog triage, sprint planning), the Kanban contrast, and the roadmap material come from this chapter.

**The Agile Manifesto** (Beck et al., 2001) is at https://agilemanifesto.org, with its twelve supporting principles at https://agilemanifesto.org/principles.html — the principles page is the more useful of the two and the more often skipped.

The **Eisenhower** line quoted below (*plans are useless, but planning is indispensable*) is from a 1957 address, collected in *The Papers of Dwight David Eisenhower*, Volume VI.

Practical framework detail is widely-attested industry practice; Atlassian's agile documentation (https://www.atlassian.com/agile) is the most accessible free reference, and its Kanban material is particularly good.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (breaking work down well requires understanding it)
- **Builds:** Leadership (estimation and scoping are how you become predictable to the people depending on you)

## What this skill is for

Software work has to be planned and tracked — teams need to know what they're doing now and to forecast what they can take on next. But most of what you need in order to plan is discovered *while building*, which is exactly why plans go stale and why agile methods exist.

This skill fires when the user is inside that machinery: writing a story, being asked for an estimate, breaking work down, sizing a sprint, or trying to work out why their sprints never finish. It's an introduction to the mechanics plus the judgment to use them without being used by them.

## The core mindset (lead with this)

**The process exists to ship useful software to happy customers. When the process becomes the point, it has failed.**

- The manifesto's very first value is **individuals and interactions over processes and tools** — and the most common way teams go wrong is obsessing over doing agile "correctly," which violates that value directly. Notice the irony when you see it.
- **Almost no team runs the textbook version.** Scrum, Kanban, Scrumban, or a local mashup — all fine. Experiment, measure the result, keep what works, drop the rest.
- **Estimates are forecasts, not commitments.** They're for deciding how much to take on, not for holding people to a number they invented before understanding the problem.
- **Plans are useless; planning is indispensable.** The value is in the thinking and the shared understanding, not in the artifact's accuracy.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual story or sprint, skip diagnosis when their message says what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that planning serves shipping, not the reverse. Skip if the user has a concrete question.

### Step 2 — Diagnose (one question, only if needed)

Common shapes:

- **Writing or fixing a story** — unclear what belongs in it.
- **Estimating** — asked for points and unsure how to arrive at a number.
- **Breaking work down** — a story too big to start.
- **Sprint keeps failing** — chronic overcommitment or churn.
- **Framework question** — Scrum vs Kanban, or adopting something new.
- **Roadmap** — quarterly or yearly planning.

If ambiguous, ask **one** question — e.g. *"What's in front of you — writing a story, estimating one, breaking one down, or something about how the sprint itself is going?"*

### Step 3 — Know which framework you're in

**Scrum** organizes work into **sprints** — fixed-length iterations, two weeks being most common. Each sprint opens with a planning meeting that divides work into user stories and tasks, progress is tracked in a ticketing system, a short standup happens daily, and the sprint closes with a review and retrospective that feed the next planning session.

**Kanban** has no fixed iterations. It defines **workflow stages** every item moves through — backlog, planning, implementation, testing, deployment, rollout — customized per team, and crucially **limits work in progress** by capping how many items may sit in each stage at once. The board makes in-flight work visible and bottlenecks obvious: if items pile up in testing, the team can move development work back to the backlog and free engineers to help clear testing.

Most teams run neither purely. **Scrumban** and local hybrids are normal, not a failure of discipline. What matters is whether the process is delivering; the mechanics are negotiable.

### Step 4 — Write stories that are actually stories

A **user story** describes a feature *from the user's perspective*, conventionally: **"As a `<user>`, I want `<capability>` so that `<benefit>`."**

**The common failure is a task wearing a story costume:**

> *"As a developer, I need to upgrade the shared plugin to version 8.7."*

That's a task. It names no user, no capability from their side, and no benefit — so it can't be prioritized against other user value, and nobody can tell why it matters. If the work genuinely is internal maintenance, **file it as a task and don't pretend**. Forcing everything into story format degrades the format for the work that needs it.

Two attributes carry most of the weight:

- **Estimate** — the guess at effort (Step 6).
- **Acceptance criteria** — how everyone knows it's done. This is the one people skip and the one that prevents the most disagreement, because "done" is otherwise negotiated after the fact.

Small stories often serve as the work ticket directly; larger ones link to implementation tickets or subtasks.

### Step 5 — Spike when the work is too unclear to estimate

A **spike** is a **time-boxed investigation** whose output is knowledge, not shipped behavior — a design sketch, a build-versus-buy recommendation, a trade-off assessment. Use one when a story is ambiguous or needs design before it can honestly be sized.

The time-box is the whole point: a spike without a deadline is just unbounded research. When the spike's output is a design, route to [`technical-design-process`](../technical-design-process/SKILL.md) and [`design-doc`](../design-doc/SKILL.md).

### Step 6 — Break stories into tasks

Split a story when you need to estimate it more accurately, share it between engineers, or track progress through it.

**The practical trick: write a very detailed description of the work, then read it back and extract every task you find in it.** Work that sounds atomic rarely is. *"Add a retry parameter to the network POST"* actually contains: agree the specification with product, write the code, unit test, integration test, deploy, and ramp it.

Smaller pieces are easier to understand, easier to estimate, and easier to hand off — which is most of why sprints are short in the first place.

### Step 7 — Estimate with story points

**Story points** are an agreed-upon sizing unit. A team has a **capacity** per sprint, and the sum of committed points must not exceed it — e.g. four engineers at ten points each gives forty points, and planning stops at forty.

Two common schemes:

- **Time-based** — one point ≈ one workday.
- **Complexity-based** — t-shirt sizing, typically 1 (XS), 2 (S), 3 (M), 5 (L), 8 (XL). The gaps widen deliberately: bigger work is estimated less accurately, and the scale should reflect that rather than implying false precision.

**Practitioners genuinely disagree here, and the argument is worth knowing rather than avoiding.**

*The case for complexity points:* the indirection is the point. An estimate expressed in days gets read as a commitment by anyone outside the team, and once "three days" is said aloud it becomes a date somebody is holding you to. Non-time units break that reflex, make uncertainty expressible through the widening scale, and stay meaningful when team members work at different speeds.

*The case for time-based points:* they are legible to everyone without translation, convert directly into forecasting, and require no calibration period before they mean anything. The complexity scale's protection is also partly a fiction — stakeholders ask "so how many days is that?" and someone answers.

*What decides it:* **whether your estimates are consumed outside the team.** If they are quoted back to you as commitments, the indirection is doing real work and complexity points earn their cost. If your team is small and stable and nobody outside reads the numbers, time-based is simpler and the indirection buys you little.

**The technique that actually improves accuracy is relative sizing.** People are poor absolute estimators and much better comparative ones. Assign points to work already finished, then size new work against it: *is this more or less like that three-pointer we shipped last month?* Planning poker formalizes this, but even just reviewing completed work calibrates you to your team's scale — which is the part that transfers.

Points are team-relative. They don't compare across teams, and using them to compare teams is a well-known way to corrupt them.

### Step 8 — Groom the backlog, then plan the sprint

**Backlog triage (grooming)** happens before planning: add new stories, close ones no longer relevant, update incomplete ones, and move higher-priority work to the top. A well-groomed backlog is what makes the planning meeting productive rather than exploratory.

**Sprint planning** is collaborative — engineers with product managers, working down the prioritized backlog until the sprint's capacity is full. **Base capacity on what previous sprints actually completed**, not on optimism, and refine it each time.

**Once planning is done, the sprint is locked.** Work that surfaces mid-sprint goes to the backlog for next time. This is what makes a sprint mean anything — and short sprints are what make it tolerable, since nothing waits more than a week or two.

**The obvious exception is operational work.** On-call load, incidents, and urgent production issues do not queue politely for the next sprint. Teams that pretend otherwise either break the rule constantly or quietly burn their on-call engineer's capacity. Plan for it explicitly — reserve capacity, or exclude the on-call engineer from sprint commitments. See [`on-call-shift`](../on-call-shift/SKILL.md).

### Step 9 — Contribute to roadmaps without over-trusting them

Longer-range planning still matters: customers have delivery dates, the business allocates headcount, and large technical projects need coordinating. Roadmaps typically run yearly, broken into quarters, with planning before each quarter.

> *"In preparing for battle I have always found that plans are useless, but planning is indispensable."* — Eisenhower

**No yearly or quarterly roadmap is ever fully accurate, and that isn't the point.** The value is that it makes the team think long-term about what they're building. Roadmaps are meant to evolve — requirements change and technical problems surface, which is what sprint planning, reviews, and retrospectives exist to absorb.

Two practical notes:

- **Communicate changes early.** When work gets shuffled or cut, teams depending on it need to know as soon as you do — not when they discover it.
- **Yearly planning is partly theater**, and it often drives resource allocation and headcount rather than actual engineering sequence. If a project you care about isn't on it, that's worth a conversation with your manager rather than a source of stress — ask where it stands at the end of the planning process.

### Step 10 — Pick one action, then close

Ask: *"What's the one thing you'll do?"* Push for concreteness.

- *"Estimate better"* → too vague.
- *"Rewrite the story with acceptance criteria and take it to grooming Thursday"* → the action.
- *"Size the next three stories against the auth work we finished last sprint"* → the action.
- *"Bring the overcommitment pattern to the retro with the last four sprints' completed-points numbers"* → the action, and route to [`team-rituals`](../team-rituals/SKILL.md).

---

## Callout — Why sprints fail, and what actually fixes it

Chronic sprint failure is the most common complaint about agile, and it usually has one of a few causes. Diagnosis matters, because the fixes differ.

| Symptom | Likely cause | Fix |
|---|---|---|
| Consistently finish 60–70% of committed points | Capacity set on optimism, not history | Set next sprint's capacity to the **average actually completed** over the last three or four. Painful once, then accurate. |
| Work constantly pulled in mid-sprint | Sprint isn't really locked | Push new work to the backlog. If it genuinely can't wait, that's a signal the sprint boundary doesn't fit this team's reality — consider Kanban. |
| On-call engineer never finishes their stories | Operational load isn't planned for | Reserve capacity or exclude the on-call engineer from commitments. This is not a personal performance issue. |
| Stories routinely underestimated | Absolute estimation, no calibration | Switch to relative sizing against completed work. |
| Everything is "almost done" for days | Stories too large, no task breakdown | Break down further (Step 6). Anything that can't finish inside one sprint is too big. |
| Nobody believes the estimates anyway | Estimates being used as commitments or performance measures | This is a management problem, not an estimation problem. Raise it — estimation cannot survive being used as a stick. |

The pattern: **most "we can't estimate" problems are actually capacity, scope-stability, or trust problems.** Estimating harder doesn't fix any of those.

---

## Callout — The manifesto, and how it gets misused

The four values (https://agilemanifesto.org):

- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

The often-forgotten closing line: *while there is value in the items on the right, we value the items on the left more.* The right-hand items are **not** worthless. Documentation, plans, and contracts all matter — the claim is about relative weight, not dismissal. People who cite the manifesto to justify not writing anything down are misreading it, and this repository's [`design-doc`](../design-doc/SKILL.md) exists partly because that misreading is common.

**The central irony worth naming:** agile became popular, and then teams became obsessed with implementing it correctly — adding ceremonies, tooling, certifications, and rules. That obsession violates the first value directly. A team following every Scrum practice precisely while nobody talks to each other has missed the point more completely than a team with no framework at all.

**The twelve principles** (https://agilemanifesto.org/principles.html) are more useful than the four values and far less read. They're a page long. Read them at least once — several are things teams claim to believe and don't practice, and they're the source of the retrospective principle in [`team-rituals`](../team-rituals/SKILL.md).

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Work on their actual story.** If they paste one, rewrite *it* — check for a real user, a real benefit, and acceptance criteria.
- **Don't defend the framework.** If the user's process is dysfunctional, engage with the dysfunction. "That's not real Scrum" is never useful.
- **Treat estimation questions as capacity questions.** The number is rarely the real problem.
- **Name the on-call exception unprompted** if the user describes sprint commitments and carries a pager.
- **Don't over-formalize small teams.** A three-person team doesn't need story points to know what they're doing this week.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking about **standups, sprint reviews, or retrospectives**. Route to [`team-rituals`](../team-rituals/SKILL.md).
- The user is working out **what to build or how to design it**. Route to [`technical-design-process`](../technical-design-process/SKILL.md) or [`design-doc`](../design-doc/SKILL.md).
- The user is being crushed by **operational load** during their on-call shift. Route to [`on-call-shift`](../on-call-shift/SKILL.md).
- The user wants to make the case for **paying down technical debt** in planning. Route to [`technical-debt`](../technical-debt/SKILL.md).
- The user is reflecting on **their own growth**, or prepping a 1:1 or performance review. Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user is **owning a project end to end** and wants the wider playbook. Route to [`owner-playbook`](../owner-playbook/SKILL.md); for OKRs and quarterly goals as a Contributor, [`contributor-playbook`](../contributor-playbook/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- **The Agile Manifesto** — https://agilemanifesto.org, and especially the **twelve principles** at https://agilemanifesto.org/principles.html. Both are very short. The principles page is the one worth actually reading.
- **Atlassian's agile documentation** — https://www.atlassian.com/agile. The most practical free reference on Scrum and Kanban mechanics; the Kanban material is especially good for teams moving that way.
- **A note on agile books:** most are overkill for an individual engineer — long, exhaustive across variants, and aimed at project and program managers. The manifesto plus a good practical reference covers what an engineer needs.
