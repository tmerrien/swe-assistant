---
name: team-rituals
description: Use when the user is participating in, running, or frustrated by their team's recurring meetings — daily standups, sprint reviews and demos, or retrospectives. Triggers include "our standups are useless", "what do I say in standup", "how do I run a retro", "our retros never change anything", "we're doing a sprint review", "what should I demo", "I have to miss standup", "parking lot", "scrum of scrums", "async standup", "nothing improves after we discuss it", "our retro turned into blame", or "should reviews and retros be the same meeting". Covers the ceremonies from The Missing Readme (Ch. 12) — standups as a status check rather than a troubleshooting session, reviews as honest progress, and retrospectives on process. For estimating, story writing, sprint planning, or roadmaps, route to agile-planning. For an individual growth conversation or 1:1 prep, route to growth-self-check.
---

# team-rituals

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 12, "Agile Planning."** The treatment of standups (including the parking lot, async formats, and scrum of scrums), sprint reviews, and retrospectives comes from this chapter.

The retrospective principle is one of the twelve **Agile Manifesto** principles (https://agilemanifesto.org/principles.html): *at regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.*

The retrospective/growth-conversation boundary maintained below is well-established: Derby & Larsen's *Agile Retrospectives* (2006) and the Scrum Guide both scope retrospectives to team process, with individual growth belonging in 1:1s.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Leadership (how you show up in recurring meetings is most of how the team experiences you)
- **Builds:** Technical Knowledge (retrospectives are where tooling and process problems actually get fixed)

## What this skill is for

The recurring meetings are where a team's process is either maintained or quietly rots. Standups become status theatre. Reviews become nobody demoing anything. Retrospectives produce a list that nobody actions, and then people stop bringing real problems to them.

This skill fires when the user is in one of these meetings, running one, or frustrated by one that isn't working. Most of the value is in knowing what each ritual is *for* — because nearly every failure mode is a meeting being used for something it isn't designed to do.

## The core mindset (lead with this)

**Each ritual answers one question. Mixing them is what breaks them.**

- **Standup:** *is anything blocking the sprint?* It's a status check, not a problem-solving session.
- **Review:** *what did we actually build?* Honest progress against the goal — not a polished presentation.
- **Retrospective:** *how is our process working?* Process and tooling, not the work itself and not individual performance.
- **You get out what you put in.** These meetings degrade into theatre exactly when people stop treating them as real, and they're recoverable when a few people stop.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual meeting, skip diagnosis when their message says which ritual they mean.**

### Step 1 — Frame the moment

One sentence naming which ritual they're in and what it's for. Skip if obvious.

### Step 2 — Diagnose (one question, only if needed)

If ambiguous: *"Which is it — standup, sprint review, or retro? And are you running it or sitting in it?"*

Running it and attending it are different jobs, and the advice differs.

### Step 3 — Standups

A standup keeps everyone informed of progress, keeps people accountable and focused, and gives the team a chance to react to anything endangering the sprint goal. Usually **fifteen minutes**, usually each morning, going around with: what I did, what I'm doing next, what's blocking me.

**Attending well:**

- **Be on time.** A fifteen-minute meeting that starts five minutes late has lost a third of itself.
- **Update your tickets beforehand** if your standup involves ticket status. Doing it live wastes everyone's time.
- **Trim to the essentials.** Standup is a check, not a report. Detail belongs in the ticket.
- **Raise blockers plainly.** The whole reason the meeting exists is so that a stuck person gets unstuck today rather than on Thursday.
- **Listen for where you can de-risk the sprint.** If someone says their ticket is taking longer than expected and you have slack, offer. This is the single most valuable thing you can do in a standup and almost nobody does it.

**The parking lot.** When someone says *"let's take that to the parking lot,"* they're stopping a discussion that's expanding beyond the meeting, to be resumed afterwards with only the people who care. It isn't a brush-off — it's what protects the other seven people's fifteen minutes. Use it yourself when you notice two people deep in a problem.

**Missing one** is acceptable when conflicts arise. Ask your manager how they'd like you to provide and receive updates when you do.

**Async standups** — the same update posted to a bot or a group thread daily — work well, are skipped less often than synchronous ones, and suit distributed or timezone-split teams. If the synchronous meeting is chronically low-value, proposing async is a reasonable move.

**Scrum of scrums:** for larger efforts, one person from each team attends a second-level standup to report progress and surface cross-team dependencies. The same pattern is common in operations, where each team sends an engineer to an operational scrum to stay current on production issues.

### Step 4 — Sprint reviews

Reviews happen between sprints, usually in two parts: a **demonstration** of what was built, and a **project review** of status against the goal. Structure varies enormously between teams; some emphasize demos, some product status, and plenty of teams don't hold them at all.

- **Keep it proportionate.** The common ceiling is **one hour per week of sprint** — a two-week sprint gets a two-hour review at most.
- **Don't over-prepare.** It's informal by design. A few minutes deciding what to show and making sure ticket statuses are accurate is the right amount of preparation. **Avoid formal presentations and speeches** — polish signals the wrong thing and costs time the sprint needed.
- **Take it seriously anyway.** Give real feedback, and take genuine interest in what others built. **What you get out of reviews matches what you put in** — a room where nobody engages becomes a room nobody wants to be in.
- **What it's for:** celebrating wins, building unity, creating a feedback opportunity, and keeping the team honest about actual progress. That last one is the quiet load-bearing function — a review is much harder to fake than a status field.

### Step 5 — Retrospectives

*"At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly."* — Agile Manifesto principle.

A retrospective looks at what has and hasn't gone well since the last one, in **three phases**:

1. **Sharing** — the facilitator asks everyone what worked and what didn't. **Everyone participates.** Items go on a whiteboard or shared document as they come.
2. **Prioritization** — the team discusses which of the problems are causing the most pain. You cannot fix everything; picking is the work.
3. **Problem-solving** — the top items get actual proposed changes.

**Do not confuse reviews and retrospectives.** Reviews are about **the work done in the sprint**; retrospectives are about **process and tooling**. They can be held back to back — some teams run review, retro, and planning in one block between sprints — but each phase must be kept distinct, or the retro collapses into a status update. (Be honest about the length of that combined block; a team that schedules all three together and doesn't protect the boundaries usually just loses the retro.)

**Retrospectives are about the team's process, not about individuals.** The moment a retro becomes a venue for assessing a person's performance, people stop bringing real problems and it's finished as a tool. Individual growth belongs in 1:1s — see [`growth-self-check`](../growth-self-check/SKILL.md). If a retro is sliding toward blame, that's the thing to name; [`software-entropy`](../software-entropy/SKILL.md) covers the same failure mode applied to code quality.

The failure modes are in the callout below.

### Step 6 — Pick one action, then close

Ask: *"What's the one thing you'll do?"* Push for concreteness.

- *"Be better in standup"* → too vague.
- *"Update my tickets before standup instead of during it, starting tomorrow"* → the action.
- *"Bring the last three retros' action items to the next one and ask why none shipped"* → the action.
- *"Propose async standups for a two-sprint trial and compare how often people are blocked"* → the action.

---

## Callout — Why retrospectives stop working

Retros decay in recognizable ways. Most are fixable if named.

| Symptom | What's actually happening | What helps |
|---|---|---|
| Same issues raised every time, nothing changes | Action items have no owner or no deadline — they're wishes | Every item leaves with a **name and a date**. Review last retro's items *first*, before generating new ones. |
| It becomes a complaint session | Sharing phase runs long, prioritization and problem-solving get squeezed | Timebox sharing. Protect the last third for solutions. |
| It becomes a status update | Review and retro have merged | Separate them explicitly, even in the same block. Different question, different phase. |
| People stop raising real problems | Something got treated as individual performance, or someone was blamed | Name the norm out loud; move individual matters to 1:1s. Trust takes several clean retros to rebuild. |
| Only the loudest people talk | No structured sharing | Round-robin, or silent written brainstorming before discussion. |
| Actions are all "someone should ask another team" | The team is picking problems it can't act on | Prioritize by **pain × ability to act**. An owned small fix beats an unowned large one. |
| The team says retros are a waste of time | Usually accurate, and usually the result of one or more of the above | Fix the mechanics before abandoning the meeting — but if it truly delivers nothing, dropping it beats performing it. |

**The single highest-leverage change:** open each retro by reviewing the previous retro's action items. It takes three minutes, and it converts the meeting from a talking shop into something with a memory.

---

## Callout — What to actually say in a standup

For anyone who freezes, or fills the slot with noise. The shape is three lines.

**A good update:**

> *"Yesterday I finished the retry logic on the payments client and opened the PR. Today I'm starting the integration tests. No blockers — though if the PR isn't reviewed by tomorrow that becomes one."*

Specific, forward-looking, names a risk before it's a problem.

**A weak update:**

> *"Still working on the payments ticket. Same as yesterday."*

No information about progress, expected completion, or whether anything is wrong. Three days of this and nobody knows the sprint is in trouble until it is.

**Things worth saying that people leave out:**

- *"This is taking longer than I estimated"* — the most useful sentence in standup, and the hardest. Say it early, not on the last day.
- *"I'm blocked on X and I've asked Y"* — shows the blocker *and* that you've acted, so the team knows whether to step in.
- *"I have capacity if anyone needs help"* — rare and valuable.
- *"I don't understand Z well enough to estimate it yet"* — better raised here than discovered at sprint end. See [`asking-for-help`](../asking-for-help/SKILL.md).

**Things to leave out:** implementation detail, debugging narration, and anything that concerns only one other person. That's what the parking lot is for.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Ask whether they're running it or attending it.** The advice diverges sharply.
- **Treat "our retros are useless" as a diagnosis, not a complaint.** Work the callout table.
- **Don't defend the ceremony.** If a meeting genuinely delivers nothing, saying so is more useful than insisting they run it better. Some teams should drop reviews.
- **Guard the retro boundary firmly.** Retros that drift into individual performance are the fastest way to lose the team's trust — name it whenever it appears.
- **Give them words.** For standup anxiety or a hard retro item, offer concrete phrasing rather than principles.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is **estimating, writing stories, planning a sprint, or working on a roadmap**. Route to [`agile-planning`](../agile-planning/SKILL.md).
- The user is reflecting on **their own growth**, prepping a 1:1, or preparing for a performance review. Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user is running a **postmortem after a production incident**. Route to [`incident-response`](../incident-response/SKILL.md) — blameless postmortems are a different ritual with different rules.
- The user is frustrated about **code quality** and heading toward blaming teammates. Route to [`software-entropy`](../software-entropy/SKILL.md).
- The user is running a **design discussion or brainstorm**. Route to [`technical-design-process`](../technical-design-process/SKILL.md).
- The user is preparing to **ask a colleague for help** outside a meeting. Route to [`asking-for-help`](../asking-for-help/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- **The twelve principles behind the Agile Manifesto** — https://agilemanifesto.org/principles.html. One page; the source of the retrospective principle and several others teams claim to hold and don't practice.
- **Atlassian's agile documentation** — https://www.atlassian.com/agile. Practical guides to running each ceremony, including retrospective formats worth rotating between.
- ***Agile Retrospectives: Making Good Teams Great*** — Esther Derby & Diana Larsen (Pragmatic Bookshelf, 2006). The standard reference on facilitating retrospectives, including the five-stage structure and a catalogue of activities for teams whose retros have gone stale.
