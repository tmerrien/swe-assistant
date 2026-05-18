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

- [`new-team-onboarding`](./skills/new-team-onboarding/SKILL.md) — fires when you're in or about to enter the first weeks somewhere new.

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

- [`ramp-up-playbook`](./skills/ramp-up-playbook/SKILL.md) — fires when you're in the Ramp-Up phase: past first weeks, contributing in small ways, building context and the manager relationship.

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

- [`contributor-playbook`](./skills/contributor-playbook/SKILL.md) — fires when you're in the Contributor stage: trusted with bigger work, helping teammates, planning quarterly goals.
- [`code-review`](./skills/code-review/SKILL.md) — fires whenever you're giving or receiving a code review. Useful from Ramp-Up onward; especially central at this stage.

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

- [`operator-playbook`](./skills/operator-playbook/SKILL.md) — fires when you're in (or asked about) the Operator stage: delivery pipeline, observability, on-call prep, defending software in production.
- [`incident-response`](./skills/incident-response/SKILL.md) — fires when prod is on fire (or you've just been paged). Useful at any stage where you're on-call; central here.

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

- [`owner-playbook`](./skills/owner-playbook/SKILL.md) — fires when you're in (or asked about) the Owner stage: driving small projects, design thinking, balancing maintenance, team process, career conversations.
- [`design-doc`](./skills/design-doc/SKILL.md) — fires whenever you're writing or reviewing a technical design document (also known as RFC or ADR depending on the team). Useful any time you need to think before building.

---

## Beyond Stage 5

These five stages complete the journey from Chapter 1 of *The Missing Readme*. Beyond the Owner stage lies the broader senior / staff / principal arc — territory for future chapters and future books to map. Subsequent chapters of *The Missing Readme* will deepen the *situations* an engineer encounters (incidents, design, communication, career) rather than add new stages, and that material will fold into the existing skills as it arrives.

The journey is also not a one-way ladder. Every time you change company, team, or technology, you cycle back through earlier stages for those new contexts. Senior engineers who join a new company are still Newcomers there for a few weeks, even if they're Owners in their broader career.

---

## Attribution

The journey framework is from *The Missing Readme: A Guide for the New Software Engineer* by Chris Riccomini and Dmitriy Ryaboy (No Starch Press, 2021), Chapter 1: "The Journey Ahead." All credit belongs to the book's authors.
