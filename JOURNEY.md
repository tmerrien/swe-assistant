# The Journey

The path from joining a team as a new engineer to becoming a strong player. Lifted from *The Missing Readme*, Chapter 1, "The Journey Ahead" — with conventional stage names instead of the book's playful ones (the original names are kept in parentheses for traceability).

## Why this map exists

Different stages of the journey call for different kinds of help. A Newcomer needs setup checklists and the courage to ask basic questions; someone three years in needs different skills entirely. By naming the stages, every skill in this assistant can be tagged with the stage(s) it's most useful at — and we can notice when a stage is under-served.

The stages are not a ladder you climb once and leave behind. Every time you change company, team, or role, you cycle back to Newcomer for a while — even senior engineers do.

---

## Stage 1 — Newcomer  *(book: "Peak Newb")*

The first weeks at a new company, team, or role.

**The mindset:** *Understand the system and the people, not to impress.* Speed matters less than learning the steps. Asking many "obvious" questions early is an asset, not a liability.

**What good looks like at this stage:**

- Onboarding meetings attended; dev environment and system access set up.
- Comfortable with the team's regular processes and meetings (standup, planning, retro, demos, all-hands).
- Codebase docs read; documentation gaps captured and filled where possible.
- New hire program used — or, if none exists, asked manager for the org chart, the relationships between departments, and who reports what to whom. Notes taken.
- Onboarding steps documented as you went, creating the playbook for the next person. (If your company has no onboarding process, you are now creating one.)
- First small, low-stakes changes shipped — chosen to learn the workflow (clone, branch, change, test, review, merge, deploy), not to impress.
- IDE set up with the team's code formatting conventions.
- Manager has added you to all relevant team and company meetings.

**Skills for this stage:**

- [`new-team-onboarding`](./plugins/swe-assistant/skills/new-team-onboarding/SKILL.md) — fires when you're in or about to enter the first weeks somewhere new. **Start here.**
- [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md) — the "obvious questions" window is open now and closing. Fires when you're hesitating to ask.
- [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md) — fires when you're deliberately learning the codebase, the domain, or the tooling.
- [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md) — fires when the newness tips into feeling like a fraud — common and predictable at this stage.

---

## Stage 2 — Ramp-Up  *(book: "Ramp-Up River")*

The next few months after the first weeks. You've finished the setup; now you're absorbing context and starting to contribute in small ways while still leaning heavily on the team.

**The mindset:** *Ramping up is active, not passive.* Read PRs, attend rituals, ask questions in real time, contribute small things often. You don't build context by reading docs alone — you build it by engaging with the work and the people doing it.

**What good looks like at this stage:**

- Working on the existing codebase, with **frequent reviews** from teammates. Small PRs, often, with feedback loops you actually use.
- Investigating how code is **built, tested, and deployed** end-to-end (not just where the source files live, but how they get to production).
- Reading other people's PRs and code reviews to absorb the team's standards, taste, and unwritten rules.
- Comfortable asking for more information when something doesn't make sense. The "obvious questions" window is closing — use it.
- Signed up for tech talks, brown bags, reading groups, mentorship programs, anything that connects you to the broader engineering community at the company.
- **Manager relationship deliberately built:** working style understood, expectations clear, goals discussed, first 1:1s used well, and — critically — a sustainable rhythm for status communication agreed on. (Don't guess what the manager wants. Ask.)
- Attending planning sessions, retrospectives, and all-hands. Has asked for an overview of the team's roadmap and the development planning process so the work being shipped makes sense in context.

**Skills for this stage:**

- [`ramp-up-playbook`](./plugins/swe-assistant/skills/ramp-up-playbook/SKILL.md) — fires when you're in the Ramp-Up phase: past first weeks, contributing in small ways, building context and the manager relationship. **Start here.**
- [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) — fires whenever you're giving or receiving a review. Reading others' reviews is how you absorb the team's standards.
- [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) — fires when writing a commit message or preparing a PR — the small-PR rhythm this stage runs on.
- [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) — fires when you're about to touch unfamiliar or untested code, which at this stage is most code.
- [`software-entropy`](./plugins/swe-assistant/skills/software-entropy/SKILL.md) — fires when the mess starts to frustrate you, before it curdles into blame.

---

## Stage 3 — Contributor  *(book: "Cape Contributor")*

The team trusts you with bigger work, and you're starting to give as well as receive.

**The mindset:** *You're shipping real things now — and you're also a giver, not just a receiver.* The shift from Ramp-Up to Contributor is the shift from "I'm absorbing" to "I'm contributing meaningfully *and* helping others do the same."

**What good looks like at this stage:**

- Working on **larger tasks and features**, not just small PRs. Owning a piece of work end-to-end (scoping, building, shipping, monitoring).
- The team trusts you to **work more independently**. Your manager doesn't need to check on you daily; you flag things proactively when you need help or when scope is shifting.
- Writing **production-grade code**: operator-friendly (good logging, sensible defaults, fails clearly), with cleanly managed dependencies and clean tests that someone else could maintain.
- **Helping teammates.** Answering their questions, pairing on tricky problems, sharing what you've learned. The receiving-help flow now goes both ways.
- **Active in code reviews** — both giving them and being asked for ideas/feedback. Your reviews are useful enough that teammates seek them out.
- Still **asking questions when confused**. The "obvious questions" window is gone, but "I want to understand why" never closes.
- **Participating in team planning** — including OKR or quarterly goal-setting cycles with your manager. You're starting to shape the work, not just receive it.

**Skills for this stage:**

- [`contributor-playbook`](./plugins/swe-assistant/skills/contributor-playbook/SKILL.md) — fires when you're in the Contributor stage: trusted with bigger work, helping teammates, planning quarterly goals. **Start here.**
- [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) — central at this stage — your reviews should now be useful enough that teammates seek them out.
- [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md) — fires when you're handed something ambiguous and have to work out what to build.
- [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md) — fires when the thinking needs writing down for others to review.
- [`agile-planning`](./plugins/swe-assistant/skills/agile-planning/SKILL.md) — fires when estimating, writing stories, or sizing a sprint — you're shaping the work now, not just receiving it.
- [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md) — production-grade code means tests someone else could maintain.
- [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md) — fires when you need to identify, prioritise, or make the case for paying debt down.

---

## Stage 4 — Operator  *(book: "Operations Ocean")*

You start taking responsibility for what happens *after* code is merged. Delivery, deployment, observability, on-call, incidents — the whole "code in users' hands" half of engineering.

**The mindset:** *Code only matters when it's running and not breaking.* Shipping is the start of a piece of software's life, not the end. You're now responsible for what happens next.

**What good looks like at this stage:**

- Understands the **delivery pipeline** end-to-end: how code goes from a merged PR through testing, build, release, deployment, and rollout to actual users.
- Comfortable **debugging live software** using metrics, logs, and trace tools — knows which one to reach for when, and what each can and can't tell you.
- May have **entered the on-call rotation** (or is preparing to). Knows what to do when the pager fires.
- **Watches how their code behaves in users' hands** — checks dashboards after a deploy, reads error reports, notices when something is degrading before customers do.
- **Defends the software** — uses feature flags for risky changes, ships behind canaries, sets up monitoring and alerting on what matters, designs for rollback.
- Treats incidents and postmortems as **learning, not blame**.

**Skills for this stage:**

- [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md) — fires when you're in (or asked about) the Operator stage: delivery pipeline, observability, on-call prep, defending software in production. **Start here.**
- [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md) — fires when prod is on fire, or you've just been paged.
- [`on-call-shift`](./plugins/swe-assistant/skills/on-call-shift/SKILL.md) — fires for the rest of on-call — the support queue, prioritisation, handoffs, and not burning out.
- [`metrics`](./plugins/swe-assistant/skills/metrics/SKILL.md) — · [`logging`](./plugins/swe-assistant/skills/logging/SKILL.md) · [`tracing`](./plugins/swe-assistant/skills/tracing/SKILL.md) — the three observability instruments. Learn whichever your company actually uses, first.
- [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) — · [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) · [`deployment-discipline`](./plugins/swe-assistant/skills/deployment-discipline/SKILL.md) · [`progressive-rollout`](./plugins/swe-assistant/skills/progressive-rollout/SKILL.md) — the delivery pipeline, one skill per phase.
- [`operational-tools`](./plugins/swe-assistant/skills/operational-tools/SKILL.md) — fires when you're building the tooling operators will actually use.

---

## Stage 5 — Owner  *(book: "Competence Cove")*

The team trusts you to drive small projects end-to-end. You design, you decide, you write down trade-offs, and you start thinking about the system — not just your code in it.

**The mindset:** *Think about the system, not just your code in it.* You're now responsible for what gets built and why, not only how. That includes thinking about how the system needs to evolve, what's been neglected, and how the team works together.

**What good looks like at this stage:**

- The team **counts on you to drive a small project** — scope it, plan it, ship it, run it.
- Comfortable **writing technical design documents** and helping with project planning. The doc is the artifact of your thinking, not just paperwork.
- **Designs software**, exploring trade-offs and planning for how the system will need to evolve over time. You don't just solve the problem in front of you — you solve it in a way that doesn't break the next problem.
- **Sees flaws in the current architecture, build, deploy, and testing environment.** Critical eye on the system, not just the change.
- **Balances regular work with necessary maintenance and refactoring.** Knows when to pay down debt and when to ship. Doesn't pretend tech debt doesn't exist; doesn't pretend it's the only thing that matters.
- **Thinks about team processes** — what's working, what isn't — and brings ideas to 1:1s with the manager. You're starting to shape how the team works, not just what it ships.
- **Doing longer-term goal setting and performance reviews** with the manager. Understands the review process, gathers peer feedback deliberately, discusses career aspirations — what you want next, what projects excite you, where you want to grow.

**Skills for this stage:**

- [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md) — fires when you're in (or asked about) the Owner stage: driving small projects, design thinking, balancing maintenance, team process, career conversations. **Start here.**
- [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md) — · [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md) — the design document, and the spiral of thinking and discussion that produces it.
- [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md) — fires when deciding where a boundary goes or whether an abstraction earns its keep — the structural judgment this stage is trusted with.
- [`evolvable-apis`](./plugins/swe-assistant/skills/evolvable-apis/SKILL.md) — · [`evolvable-data`](./plugins/swe-assistant/skills/evolvable-data/SKILL.md) — designing so that today's decisions don't trap tomorrow's.
- [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md) — · [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md) — judgment about rewrites, standards, and new technology.
- [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md) — fires when standups, reviews, or retros need fixing — the team-process improvement this stage brings to 1:1s.

---

## Skills that aren't stage-bound

Most skills in this assistant attach to a **situation** rather than a career stage — they fire the first time you hit that situation, whether that's week two or year ten. The stage lists above name the skills that are *characteristic* of each stage; these are the rest, grouped by the kind of moment they serve.

**Writing and changing code**

- [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md) — hardening code — null safety, immutability, exception design, resource cleanup.
- [`input-validation`](./plugins/swe-assistant/skills/input-validation/SKILL.md) — handling anything from outside the trust boundary.
- [`idempotency`](./plugins/swe-assistant/skills/idempotency/SKILL.md) — designing an operation that might be executed more than once.
- [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md) — calling something remote that can fail.
- [`configuration`](./plugins/swe-assistant/skills/configuration/SKILL.md) — deciding what belongs in config, and how it's validated.
- [`dependency-management`](./plugins/swe-assistant/skills/dependency-management/SKILL.md) — taking on, pinning, or untangling third-party code.
- [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) — modifying code that's unfamiliar, untested, or frightening.

**Testing**

- [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md) — deciding what to test and how much.
- [`mocking`](./plugins/swe-assistant/skills/mocking/SKILL.md) — deciding whether and how to fake a collaborator.
- [`test-determinism`](./plugins/swe-assistant/skills/test-determinism/SKILL.md) — diagnosing or preventing flaky tests.

**Structure and change**

- [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md) — deciding where complexity should live.
- [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md) — naming, prioritising, and proposing payoff.
- [`software-entropy`](./plugins/swe-assistant/skills/software-entropy/SKILL.md) — when the mess is becoming a grievance.
- [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md) — rewrites, forks, and bypassing standards.
- [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md) — adopting anything new into the stack.
- [`evolvable-apis`](./plugins/swe-assistant/skills/evolvable-apis/SKILL.md) — · [`evolvable-data`](./plugins/swe-assistant/skills/evolvable-data/SKILL.md) — changing a contract that other people depend on.

**Working with people**

- [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md) — before you ask, or when you're avoiding asking.
- [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) — giving or receiving review.
- [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) — the artifacts around a change.
- [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md) — · [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md) — thinking a design through, and writing it down.
- [`agile-planning`](./plugins/swe-assistant/skills/agile-planning/SKILL.md) — · [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md) — planning the work, and the meetings around it.

**Learning and self-assessment**

- [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md) — learning a codebase, tool, or domain deliberately.
- [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) — checking whether you actually understand something, or only feel that you do.
- [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md) — reflecting on your own growth — 1:1s, reviews, development planning.
- [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md) — when self-assessment has gone wrong in either direction.

---

## Beyond Stage 5

These five stages complete the journey from Chapter 1 of *The Missing Readme*. Beyond the Owner stage lies the broader senior / staff / principal arc — territory for future chapters and future books to map. Subsequent chapters of *The Missing Readme* will deepen the *situations* an engineer encounters (incidents, design, communication, career) rather than add new stages, and that material will fold into the existing skills as it arrives.

The journey is also not a one-way ladder. Every time you change company, team, or technology, you cycle back through earlier stages for those new contexts. Senior engineers who join a new company are still Newcomers there for a few weeks, even if they're Owners in their broader career.

---

## Attribution

The journey framework is from *The Missing Readme: A Guide for the New Software Engineer* by Chris Riccomini and Dmitriy Ryaboy (No Starch Press, 2021), Chapter 1: "The Journey Ahead." All credit belongs to the book's authors.
