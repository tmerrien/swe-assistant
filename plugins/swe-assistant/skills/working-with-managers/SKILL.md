---
name: working-with-managers
description: Use when the user is handling the working relationship with their manager — preparing for a 1:1, writing a status update, setting or reviewing OKRs, drafting a self-review, or working out how to give their manager feedback. Triggers include "what should I bring to my 1:1", "my manager keeps cancelling our 1:1", "weekly status update", "how do I set OKRs", "writing my self-review", "how do I give my manager feedback", "how do I get promoted", or "my manager has no idea what I'm working on". Covers owning your 1:1, PPP status updates, OKRs, review preparation, and managing up. For judging whether you are actually growing, route to growth-self-check. For team retrospectives, route to team-rituals.
---

# working-with-managers

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 13, "Working with Managers."** The 1:1 discipline (you set the agenda, you do most of the talking, keep a shared running document), the **PPP** format and its update routine, the OKR guidance including the 60–80% calibration, the performance-review preparation advice, and the managing-up material all come from this chapter.

**SBI (Situation–Behavior–Impact)** is a feedback framework developed by the Center for Creative Leadership; the chapter recommends it for upward feedback.

**OKRs** (Objectives and Key Results) originate with Andy Grove at Intel and are set out in his *High Output Management* (1983).

The **promotion** guidance in Step 7 is from Chapter 14 of the same book.

## Pillars this skill strengthens

- **Primary:** Communication, Leadership
- **Also:** Execution (goals you understand are goals you can actually hit)
- **Builds:** Technical Knowledge (a manager who knows what you're working on can connect you to the people who know it)

## What this skill is for

The manager relationship runs on **mutual understanding**: you need to know what your manager needs so you can help them, and they need to know what you need so they can help you. Neither happens by default, and the half that most engineers neglect is the half they control.

This skill fires when the user is at one of the concrete moments where that relationship is actually built or lost — a 1:1 they haven't prepared for, a status update they're not sending, an OKR cycle they're guessing at, a self-review they're writing from memory, or a piece of feedback they need to give upward and are dreading.

## The core mindset (lead with this)

**Your manager cannot advocate for work they don't know about. Getting information upward is your job, not theirs.**

- **The 1:1 is yours.** You set the agenda, you do most of the talking. A 1:1 where your manager talks for thirty minutes about their priorities is a status meeting wearing a 1:1's name.
- **Silence reads as "nothing to discuss."** No agenda, no updates, no raised problems — managers reasonably conclude everything is fine. Then you're surprised at review time, and so are they.
- **Keep the record as you go.** Almost every failure in this chapter — the vague self-review, the forgotten win, the problem nobody knew about — is a record-keeping failure wearing a different costume.
- **Managing up is not politics.** It's making yourself legible to someone whose job includes representing you in rooms you're not in.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual agenda or draft, skip diagnosis when their message says which moment they're in.**

### Step 1 — Frame the moment

One or two sentences. Name that the flow of information upward is the user's to own. Skip if they have a concrete task.

### Step 2 — Diagnose (one question, only if needed)

The moments this skill serves:

- **A 1:1** — imminent, or not happening at all.
- **A status update** — due, or never sent.
- **OKRs** — being set, or unclear how they're judged.
- **A performance review** — self-review to write.
- **Feedback upward** — something to raise with the manager.

If ambiguous, ask **one** question — e.g. *"Which is it — a 1:1 coming up, a status update, goal-setting, review prep, or something you need to raise with them?"*

### Step 3 — Own the 1:1

A 1:1 should be **weekly or biweekly**, and it exists for critical topics, big-picture concerns, and the long-term relationship. It is explicitly **not a status update** — that's what Step 4 is for.

- **You set the agenda**, and you do a lot of the talking. Share a short bullet agenda beforehand so your manager can prepare.
- **Keep a running 1:1 document** holding past agendas and notes, shared with your manager, updated before and after each meeting. This single habit does more work than any other in this skill — it makes the relationship cumulative instead of a series of disconnected half-hours, and it becomes your review-prep source in Step 6.
- **Your manager may add items**, and should — but their agenda takes a back seat to yours.
- The topic bank is in the callout below. Personal conversation is normal and healthy; just don't let *every* 1:1 become a social visit.

**If you don't have 1:1s at all:** ask whether your manager runs them. Not all do, though it's common. Without a standing meeting, managers reasonably assume there's nothing to discuss — and you should have something most weeks.

**If your manager repeatedly cancels:** raise it. This is uncomfortable and worth doing anyway. It need not be a confrontation — it's precisely the kind of feedback a manager wants and needs, and Step 8 is how to deliver it.

**Set up 1:1s with people who aren't your manager, too.** Senior engineers you can learn from, especially if your company has no mentoring program. Bring an agenda to those as well; an unprepared "pick your brain" meeting wastes a senior person's time and won't get a second one.

### Step 4 — Send status updates

**PPP** — Progress, Plans, Problems — is a common lightweight format. Three sections, **3–5 short bullets each.**

It exists so your manager can spot problems early, notice where you're missing context, and connect you with the right people. It also feeds your 1:1 agenda and gives you a record of where you've been.

Share it wherever your team reads — email, Slack, a wiki — on whatever cadence your company uses (weekly or monthly are typical).

**Keep every past PPP.** That log is what makes each new one take under five minutes, and it's what saves you at review time. The derivation routine is in the callout below.

### Step 5 — Set OKRs

**Objectives and Key Results.** Your OKRs should ladder into your team's, which ladder into the company's — so start by working with your manager to understand the higher-level objectives, then derive yours from them.

**The most common mistake: writing key results as a to-do list.** A key result states *how you'll know the objective is met*, not *how you plan to meet it*. Written as tasks, they lock you into one plan and stop measuring the outcome you actually care about.

- ✗ *"Migrate the auth service to the new token format."* — that's a task.
- ✓ *"95% of active sessions issued under the new token format, with p99 auth latency unchanged."* — that's a result. It leaves you free to change approach.

**Keep the count low.** One to three per quarter is the sweet spot; more than five means you have no priorities.

**Understand the calibration** before you set them. OKRs are often deliberately set as *reach* or *stretch* goals, in which case hitting 100% means you aimed too low:

| Hit rate | What it usually means |
|---|---|
| **Above 80%** | Not ambitious enough — the goals were safe |
| **60–80%** | The intended zone for stretch goals |
| **Below 60%** | Unrealistic targets, or genuinely falling short of expectations |

**This only applies if your company treats OKRs as stretch goals.** Plenty of companies treat them as commitments, where missing 30% is a serious problem. **Ask which yours is** — the difference is enormous and it's rarely written down.

If your company sets goals only at team or company level, still have the conversation explicitly: *what am I being measured on this quarter, and how will we both know if I've done it?*

### Step 6 — Prepare the performance review

Typically annual or semi-annual. The usual shape: you self-evaluate, your manager responds, you discuss together, and you sign to acknowledge receipt. The questions are usually some version of:

- What have you done this period?
- What went well?
- What could have gone better?
- What do you want from your career — where do you see yourself in three to five years?

**Do not write this from memory.** Memory over twelve months is heavily weighted toward the last six weeks, and it systematically drops exactly the work that isn't tickets. Instead, mine your actual records:

- Your **PPP log** and 1:1 document (Step 3 and Step 4 — this is where they pay off).
- The **issue tracker**: milestones, epics, and stories you worked on.
- **Merged pull requests** and the reviews you gave.
- **Non-engineering contributions**, which engineers under-report almost universally: mentoring, interviewing, onboarding new hires, documentation, blog posts, internal talks, and the code reviews that made someone else's work better.

Then write it **honestly** — including what went badly. A self-review with no weaknesses reads as either low self-awareness or low candour, and neither helps you.

For the reflective half — *am I actually growing, and in which direction* — route to [`growth-self-check`](../growth-self-check/SKILL.md), which walks the four-pillar rubric. This step is about assembling the evidence; that skill is about judging it.

### Step 7 — Start the promotion conversation early

The common mistake is treating promotion as something that happens *to* you at review time. It isn't — it's a case someone has to build, usually your manager, using evidence you supplied.

**Start the conversation when you're roughly halfway there**, not when you think you've arrived. At the halfway point there is still time to close whatever gap exists; at the point you feel ready, the evidence for the last twelve months is already fixed.

The conversation is short and has three parts:

- *"I'm interested in moving to `<level>`. What does the bar actually look like here?"* — get the expectations stated. They're often written down somewhere you haven't been shown, and where they aren't, your manager's mental model is the real rubric.
- *"Where do you see me against that today?"* — this is the uncomfortable one and the whole point. You want the gap named while it's still closeable.
- *"What would you need to see?"* — turns the gap into work you can actually plan.

Then **feed the evidence back**, using the record from Steps 3 and 4. A manager arguing your case in a promotion committee needs specifics, and they will not remember what you didn't tell them.

Two calibrations worth keeping in mind:

- **Ladders differ everywhere.** Levels, titles, and what "senior" means vary enormously between companies, and a level at one is not a level at another. Ask about *this* company's bar rather than assuming a general one.
- **The answer may be "not yet, and here's why."** That's a successful outcome for this conversation — it's the information you wanted, delivered while you can still act on it.

For judging your own readiness rather than negotiating it, route to [`growth-self-check`](../growth-self-check/SKILL.md), whose four-pillar rubric and T-shape callout are the assessment half of this.

### Step 8 — Manage up: give your manager feedback

Your manager needs feedback as much as you do, and receives it from fewer people. Use **SBI**:

- **Situation** — when and where. *"In yesterday's planning meeting…"*
- **Behavior** — what was observably done or said, without interpretation. *"…the scope was set before the team estimated it…"*
- **Impact** — the effect it had, on you or the work. *"…so we committed to more than we could finish, and the team lost confidence in the estimate."*

The discipline is that **Behavior stays observable**. *"You steamrolled us"* is an interpretation and invites argument about your character judgment; *"the scope was set before the team estimated"* is a fact and invites a conversation about the process.

Three rules: **privately, calmly, and frequently.** The 1:1 is the natural venue. Frequency matters most — feedback saved up for a quarterly review arrives as an ambush, while small and regular feedback is just how you work together.

**The test:** is this the kind of feedback you'd want to receive? If not, rework it before delivering it.

### Step 9 — Pick one action, then close

Ask: *"What's the one thing you'll do?"* Push for concreteness.

- *"Communicate better with my manager"* → too vague.
- *"Start a shared 1:1 doc and put three bullets in it before Thursday"* → the action.
- *"Rewrite key result 2 as an outcome instead of a task, and check with my manager whether ours are stretch or commit"* → the action.
- *"Go through last quarter's merged PRs and PPPs tonight and list what I actually shipped"* → the action.

---

## Callout — The 1:1 agenda bank

Four categories worth rotating through. Not a checklist to run every week — pick what's live for you. Silence is the failure mode this exists to prevent.

**Big picture**
- What questions do you have about the company's direction?
- What questions do you have about recent organizational changes?

**Feedback** *(both directions — this is the richest category and the most skipped)*
- What could we be doing better?
- What do you think of the team's planning process?
- What is your biggest technical concern right now?
- What do you wish you could do that you currently can't?
- What is your biggest problem? What is the company's biggest problem?
- What roadblocks are you or others on the team hitting?

**Career**
- What career advice do you have for me?
- What should I improve on?
- What skills do you wish I had?
- Here are my long-term goals — how do you think I'm tracking against them?

**Personal**
- What's new in your life?
- Anything going on that your manager should be aware of?

A useful default when you have nothing pressing: *"What could we be doing better?"* and *"What roadblocks are you hitting?"* Both invite your manager to tell you something you don't know, which is most of the point.

---

## Callout — The PPP, and the five-minute update routine

**The format.** Three sections, 3–5 short bullets each:

```
## Progress
- Shipped the retry logic for the payments client; ramped to 100% Tuesday.
- Closed out the schema migration — old column dropped, no downstream breakage.

## Plans
- Start the rate-limiter design doc; aiming to circulate a draft by the 14th.
- Pick up the on-call handoff automation ticket.

## Problems
- Still blocked on staging access for the billing sandbox (asked infra 2 weeks ago).
- Integration tests take 40 minutes, which is slowing every change I make.
```

**The routine — derive the new one from the last one, in order:**

1. **Last PPP's Problems.** Solved? Move it to **Progress**. Still open? It stays in **Problems** — and a problem appearing three PPPs running is itself worth raising in your next 1:1.
2. **Last PPP's Plans.** Finished? Move it to **Progress**. Not finished? Either it stays in **Plans** for this period, or something blocked it — in which case that blocker belongs in **Problems**.
3. **Your calendar and upcoming work.** Add anything new you expect to do before the next update to **Plans**.

Done this way it takes under five minutes, because you're editing rather than remembering.

**Two things the log gives you beyond the update itself:** your 1:1 agenda often writes itself from the Problems section, and at review time you have twelve months of evidence instead of twelve months of vague recollection.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Work on their actual draft.** If they share an agenda, a PPP, an OKR, or a self-review paragraph, improve *that* rather than describing the format.
- **Test key results against the to-do-list trap** whenever OKRs come up. It's the single most common failure and it's easy to spot: if it describes an action rather than a state, it's a task.
- **Push back on memory-based self-reviews.** Ask what records exist before helping them write.
- **Take a cancelled-1:1 pattern seriously.** It's usually read as a personal slight and is more often a calendar problem — but either way it needs raising, and the user will likely be reluctant.
- **Don't coach them into confrontation.** Upward feedback should be framed as ordinary and low-drama, because that's what makes it deliverable.
- **Calibrate to the culture they describe.** Some managers want a weekly written update; others find it noise. The formats here are defaults, not requirements.

## When NOT to use this skill

- The user is assessing **whether they're actually growing** or which pillar to develop. Route to [`growth-self-check`](../growth-self-check/SKILL.md) — this skill assembles the evidence, that one judges it.
- The user's self-assessment is **distorted** — impostor feelings, or overconfidence. Route to [`growth-obstacles`](../growth-obstacles/SKILL.md) before any review or 1:1 prep.
- The user is running or fixing **team meetings** — standups, retros, sprint reviews. Route to [`team-rituals`](../team-rituals/SKILL.md).
- The user is doing **sprint-level planning or estimation**. Route to [`agile-planning`](../agile-planning/SKILL.md).
- The user is giving feedback **on code**. Route to [`code-review`](../code-review/SKILL.md), whose tone discipline is the peer-level version of Step 8.
- The user needs help **asking a colleague a technical question**. Route to [`asking-for-help`](../asking-for-help/SKILL.md).
- The user wants the wider **stage playbook** for where they are. Route to [`contributor-playbook`](../contributor-playbook/SKILL.md) or [`owner-playbook`](../owner-playbook/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- ***The Manager's Path*** — Camille Fournier (O'Reilly, 2017). The chapter on being managed is the most useful thing an individual contributor can read about what their manager is actually doing and what a good 1:1 looks like from the other side.
- ***High Output Management*** — Andy Grove (1983). Where OKRs come from, and the origin of the 1:1 as a structured practice — Grove treats it as the manager's highest-leverage activity.
- ***An Elegant Puzzle: Systems of Engineering Management*** — Will Larson (Stripe Press, 2019). How engineering organizations actually make decisions about headcount, team shape, and priorities — useful for understanding the constraints your manager is working inside.
- ***Managing Up*** — Mary Abbajay (Wiley, 2018). A full treatment of Step 8, including how to adapt to different managerial styles.
- ***Thanks for the Feedback*** — Douglas Stone & Sheila Heen (Penguin, 2014). The receive side; directly applicable to performance reviews.
