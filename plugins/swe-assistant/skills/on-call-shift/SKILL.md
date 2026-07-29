---
name: on-call-shift
description: Use when the user is on call, about to go on call, or thinking about how their on-call shift works — the day-to-day of holding the pager, not an active incident. Triggers include phrases like "I'm on call this week", "my first on-call shift", "how do I prepare for on-call", "I'm drowning in support requests", "how do I prioritize on-call work", "what's a P1 vs a P2", "on-call handoff", "SLI vs SLO vs SLA", "on-call is burning me out", or "someone filed a vague support request". Walks through the on-call discipline from The Missing Readme (Ch. 9) — how on-call actually works, availability, paying attention, the P0–P4 priority ladder, communicating clearly, tracking work in tickets, the support-request lifecycle, and not being a hero. For an active production incident, route to incident-response. For the broader Operator-stage picture, route to operator-playbook.
---

# on-call-shift

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 9, "Going On-Call."** The structure of this skill follows the chapter: how on-call works (ad hoc support as the bulk of the job, incidents as the interrupt, handoffs at rotation boundaries), the five on-call skills (make yourself available, pay attention, prioritize work, communicate clearly, track your work), the support-request lifecycle, and the *don't be a hero* warning. The **P0–P4 priority ladder** and the *impact determines priority* rule come from here.

The **SLI / SLO / SLA** distinction is standard practice, canonically formalized in *Site Reliability Engineering* (Beyer, Jones, Petoff, & Murphy, Google/O'Reilly 2016; free at https://sre.google/sre-book/) — Chapter 4, "Service Level Objectives." The chapter's own Level Up section points at SRE chapters 4, 11, 13, 14, and 15 for deeper treatment of on-call specifically.

For the active-incident flow this skill hands off to, see [`incident-response`](../incident-response/SKILL.md), which folds the same chapter's incident material.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (knowing your service's health signals well enough to spot deviation)
- **Builds:** Leadership (the on-call is the team's face to everyone who depends on the service)

## What this skill is for

Most engineers imagine on-call as *waiting for the pager*. In practice, the pager is the rare part. The bulk of an on-call shift is **ad hoc support** — bug reports, "why is the service doing this," usage questions, one-off requests — punctuated by occasional operational incidents that stop everything else.

That means being good at on-call is mostly a **triage, communication, and record-keeping** skill, not a heroic-debugging skill. This skill fires when the user is holding the pager (or about to), and helps them run the shift deliberately rather than reactively. It does not fire when something is actively on fire — that's [`incident-response`](../incident-response/SKILL.md).

## The core mindset (lead with this)

**Fast response is expected. Fast resolution is not.**

- An acknowledgment within minutes beats a solution within hours, every time. *"I see this, looking into it, I'll update you by 3pm"* is a complete and correct first response.
- Most of the shift is support, not firefighting. Plan for interruption, not for heroics.
- **Impact determines priority.** Not who asked, not how loudly, not how interesting the problem is.
- If you didn't write it down, it didn't happen. Chat is for talking; tickets are for remembering.
- **Don't be a hero.** The rotation exists so that no single person absorbs the whole load. Burning yourself out helps nobody, including the service.

If the user is anxious about a first shift, lead with the mindset — especially the first bullet. Most first-shift anxiety is a fear of not knowing the answer fast enough, and the job doesn't actually require that.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual shift or ticket if they share one, skip diagnosis when the first message already says what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that on-call is mostly triage and communication, and that the bar is *fast response*, not *fast resolution*. Skip if the user has a specific question queued.

### Step 2 — Diagnose (one question, only if needed)

Rough shapes the situation takes:

- **First shift / preparing** — never done this, wants to know what to expect and how to get ready.
- **Mid-shift, overloaded** — too many requests, unclear what to work on first.
- **A specific request** — one ticket they're unsure how to handle or prioritize.
- **Handoff** — starting or ending a rotation and wanting to do the handoff well.
- **Sustainability** — the rotation is burning them out.

If ambiguous, ask **one** question — e.g. *"Where are you — preparing for a first shift, in the middle of one and swamped, or working out how to handle a specific request?"*

**If they mention something actively broken, drop everything and route to [`incident-response`](../incident-response/SKILL.md).**

### Step 3 — Know the shape of the job

If the user hasn't done this before, set expectations:

- **Ad hoc support is the bulk of it.** Bug reports, behavior questions, usage questions, access requests. Triage first, then work the most urgent.
- **Incidents interrupt everything.** When an operational incident lands — by automated alert or by a support engineer escalating — it takes precedence over all queued support work. See [`incident-response`](../incident-response/SKILL.md).
- **Pages arrive through whatever channel your team configured** — chat, email, SMS, phone call. Know which of these actually wakes you up, and test it before your shift.
- **Every rotation begins and ends with a handoff.** The outgoing on-call summarizes open incidents and gives context on in-flight tasks. If your team doesn't do this, proposing it is a high-value, low-cost contribution — and much of it can be automated (a bot that posts open incidents and unresolved tickets at rotation boundaries).

### Step 4 — Make yourself available

**Expect to be interrupted, and plan the shift accordingly.**

- **Don't schedule deep work during your shift.** Accept up front that you'll get less heads-down work done. Fighting this produces both bad support and bad feature work.
- Pick up **interruption-tolerant work** instead: small bug fixes, doc improvements, test backfill, ticket cleanup, runbook writing. Work you can drop mid-sentence.
- If you had a deadline that collides with your shift, raise it with your manager *before* the shift, not during.

### Step 5 — Pay attention

Context is what makes debugging fast when it counts. Build it *before* you need it.

- **Read the operational channels.** Deployment announcements, config-change notices, release notes, ops chat rooms, operational scrum digests, meeting notes on ongoing incidents and scheduled maintenance. Most "mystery" behavior has an announcement behind it from four hours ago.
- **Keep dashboards visible.** Up in a background window or on a nearby screen. The point isn't to stare at them — it's to build a **baseline for normal** so that when something is off, the odd graph jumps out at you. You cannot recognize abnormal without having absorbed normal.
- **Build an on-call resource kit** before your shift — see the callout below. Then share it with the team so others improve it.

### Step 6 — Prioritize the queue

**Work the highest-priority item first, then work down the list.**

- When something new arrives, **triage it immediately** — that's a fast classify-and-park, not a fix. Then either set it aside or, if it's an emergency, start on it.
- **If the new item outranks your current one but isn't critical, finish what you're on** — or at least get it to a clean stopping point — before switching. Context switching has real cost; pay it deliberately.
- **When you can't tell how urgent something is, ask about impact.** *"What's blocked by this? How many users are affected? Is there a workaround?"* Impact determines priority.
- **If you disagree with an assigned priority, take it to your manager** rather than quietly reordering. Priority disagreements are usually information gaps, and they resolve fast when surfaced.

The P0–P4 ladder is in the callout below. Also learn your service's **SLIs, SLOs, and SLAs** — they're the formal statement of what "impaired" means for your service, which is exactly what the ladder is asking you to judge. Second callout below.

### Step 7 — Communicate clearly and track everything

**Communication:** be polite, direct, responsive, and thorough. **If you don't know, say so** — a fast *"I don't know yet, investigating"* is far better than silence while you look competent in private.

**Tracking** is the part most people skip and later regret:

- **Write updates in the ticket as you work**, not after. Future-you (or the next on-call) will read this at 3am.
- **Always include timestamps.** Correlating your notes against logs and dashboards later is impossible without them.
- **Record the actual mitigation and resolution in the ticket.** If the issue recurs, that's the difference between a five-minute fix and a five-hour re-investigation.
- **Chat is not a record.** Transcripts are near-unreadable after the fact. Summarize into a ticket or doc.
- **Redirect misfiled requests** to the right channel or team. Being the router is part of the job; silently absorbing everything is not.
- **Close finished tickets.** Dangling tickets clutter the on-call board and skew the team's support metrics.
- **For unresponsive requesters:** say you'll close in 24 hours due to lack of response — then actually close it.

### Step 8 — Don't be a hero

Taking on too much during a shift is the standard route to burnout, and burnout costs the team far more than the tickets you didn't personally close.

- Hand off work at the end of your shift instead of carrying it. That's what the handoff is *for*.
- Escalate and pull people in. Solo-handling something serious is bravado, not skill.
- If the rotation is structurally unsustainable — too few people, too many pages, no recovery time — that's a team-health problem worth raising with your manager, not a personal endurance test. Recurring pages that nobody fixes are a form of [`technical-debt`](../technical-debt/SKILL.md).

### Step 9 — Pick one action, then close

Ask: *"What's the one thing you'll set up before (or during) this shift?"* Push for concreteness.

- *"Be more organized"* → too vague.
- *"Build the on-call bookmark folder with links to the four service dashboards, the runbook, and the log query — before Monday"* → the action.
- *"Go back through today's three tickets and add timestamped resolution notes before I hand off"* → the action.

Close in one or two sentences. If they're about to start a first shift, remind them that [`incident-response`](../incident-response/SKILL.md) is there for when the pager actually fires.

---

## Callout — The P0–P4 priority ladder

A standard severity ladder for triaging on-call work. Teams vary in naming (some use SEV1–SEV5, some invert the numbers) but the shape is near-universal.

| Level | Meaning |
|---|---|
| **P0** | **The Big One.** Catastrophic — the whole system, or something existential (data loss, security breach, total outage). All hands. |
| **P1** | **Critical impact.** Service unusable in production. |
| **P2** | **High impact.** Service use severely impaired. |
| **P3** | **Medium impact.** Service use partially impaired. |
| **P4** | **Low impact.** Service fully usable — cosmetic issues, minor annoyances, questions. |

**How to use it:**

- **Impact determines priority.** Not the requester's seniority, not their tone, not how interesting the bug is.
- **When unsure between two levels, go higher.** Downgrading is cheap; discovering at hour three that a P3 was a P1 is not.
- **Ask about impact when the request doesn't say.** *"What's blocked? How many users? Is there a workaround?"* A workaround usually drops something a full level.
- **P0 and P1 are incidents, not support requests.** Route to [`incident-response`](../incident-response/SKILL.md) and stop working the queue.
- **Learn your team's actual ladder.** If they use SEV1–3 or a custom scheme, use theirs — the vocabulary matters more than the specific scale, because priority is a shared-language problem.

---

## Callout — SLI vs. SLO vs. SLA

Three related terms that get used interchangeably and shouldn't be. Knowing which is which tells you what "impaired" formally means for your service — the exact judgment the priority ladder asks you to make.

- **SLI — Service Level Indicator.** *The measurement.* A metric that indicates the health of your service: request latency at p99, error rate, availability, throughput, freshness of a data pipeline. It's a number you actually emit. See [`metrics`](../metrics/SKILL.md) for how to instrument these.
- **SLO — Service Level Objective.** *The internal target on that measurement.* "99.9% of API requests complete in under 200ms, measured over a rolling 30-day window." An SLO is a commitment the team makes to itself; missing it triggers internal action (stop feature work, fix reliability), not legal consequence.
- **SLA — Service Level Agreement.** *The external contract, with consequences.* "99.5% monthly availability or the customer gets a service credit." SLAs are business agreements; they're typically set *looser* than the corresponding SLO, so that the team notices a problem (SLO breach) well before a customer is entitled to compensation (SLA breach).

**Why this matters on call:**

- **Your SLIs are what you watch.** They're the graphs whose baseline you should know cold.
- **Your SLO is the line that turns "degraded" into "act now."** It converts a judgment call into a threshold.
- **Your SLA is why some incidents are business emergencies** even when the engineering impact looks modest.
- **Error budget** is the derived idea worth knowing: if the SLO allows 0.1% failure, that 0.1% is a budget you can spend on risk (deploys, experiments). Burning it fast is itself a signal.

If your service has no documented SLOs, finding out what the team *implicitly* treats as healthy — and writing it down — is a genuinely valuable contribution.

---

## Callout — The support-request lifecycle

Five steps. Most badly-handled requests skip step 1 or step 5.

1. **Acknowledge.** Confirm you've seen it, fast. Then ask whatever you need to actually understand the problem — repro steps, affected users, when it started, what changed. Don't start debugging a problem you've assumed the shape of.
2. **Set an update expectation.** *"I'll update you by 2pm."* This single move prevents most follow-up pestering, because the requester now knows silence isn't neglect.
3. **Investigate, updating as you go.** Post progress in the ticket at the cadence you promised — including *"no progress yet, still looking."* Update the ticket, not just the chat thread.
4. **Ask the requester to confirm the fix.** You are not the authority on whether their problem is solved; they are. *"Can you confirm this is working for you now?"*
5. **Close it.** Explicitly, with the resolution recorded in the ticket. If the requester has gone quiet, state that you'll close in 24 hours for lack of response, then do it.

The recurring theme: **the requester's uncertainty is as costly as the bug.** Steps 1, 2, and 4 exist entirely to manage that, and they're nearly free.

---

## Callout — The on-call resource kit

Build this *before* your shift. At 3am with a pager going off, you will not be in a state to go hunting for links.

A dedicated browser bookmark folder (or a pinned doc) containing:

- **Direct links to every dashboard** for the services you're covering.
- **Runbooks** for your services — the documented "if X is happening, do Y" procedures.
- **Log access instructions** — the exact query or command, not just the tool's URL. *"Here's how to grep the last hour of errors for service Z"* beats *"Splunk is at this URL."*
- **The important chat rooms** — ops, incident channels, the teams you depend on.
- **Troubleshooting guides** and past postmortems for recurring issues.
- **Escalation contacts** — who's the senior on-call partner, who owns each upstream dependency, and how to reach them out of hours.

Then **share it with the team.** A resource kit that lives in one person's browser helps one person; the same kit in a shared doc gets corrected, extended, and inherited by the next on-call. If your team has no runbook at all, writing the first one is the highest-leverage thing a new on-call can contribute.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't recite the Step 2 menu.
- **Route active fires immediately.** Any hint of something currently broken → [`incident-response`](../incident-response/SKILL.md), no preamble.
- **Work their actual ticket.** If they paste a support request, help them triage *that* — assign a priority, identify the missing impact information, draft the acknowledgment.
- **Calibrate to experience.** A first-timer needs expectation-setting and the resource kit. A veteran asking about handoff automation does not need the P0–P4 primer.
- **Take burnout seriously.** If the user is describing an unsustainable rotation, don't optimize their ticket-handling — engage with the sustainability problem.

## When NOT to use this skill

- Something is actively broken right now. Route to [`incident-response`](../incident-response/SKILL.md) immediately.
- The user wants the broader Operator-stage picture — delivery pipeline, observability, what it means to own production. Route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is instrumenting metrics, logs, or traces rather than consuming them on a shift. Route to [`metrics`](../metrics/SKILL.md), [`logging`](../logging/SKILL.md), or [`tracing`](../tracing/SKILL.md).
- The user is building operator-facing tooling (admin commands, recovery scripts). Route to [`operational-tools`](../operational-tools/SKILL.md).
- The user is writing a postmortem for a resolved incident. Route to [`incident-response`](../incident-response/SKILL.md), which carries the postmortem material.
- Recurring pages point at an underlying reliability problem the user wants to make the case for fixing. Route to [`technical-debt`](../technical-debt/SKILL.md) for framing the proposal.
- The user is asking about general career growth or their next level. Route to [`growth-self-check`](../growth-self-check/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- **"*What Happens When the Pager Goes Off?*"** — *Increment* magazine, on-call issue. https://increment.com/on-call/when-the-pager-goes-off/ — practitioner accounts of the actual experience of being paged, across several companies.
- ***Site Reliability Engineering*** — Beyer, Jones, Petoff, & Murphy (Google, O'Reilly 2016). Free at https://sre.google/sre-book/. The chapter's Level Up section points specifically at **Ch. 4** (Service Level Objectives), **Ch. 11** (Being On-Call), **Ch. 13** (Emergency Response), **Ch. 14** (Managing Incidents), and **Ch. 15** (Postmortem Culture). Ch. 11 is the single best treatment of on-call as a discipline in print.
