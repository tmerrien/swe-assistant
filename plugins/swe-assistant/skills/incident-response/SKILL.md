---
name: incident-response
description: Use when the user is in the middle of — or has just been paged for — a production incident, where something is broken, customers may be affected, and they need to act. Triggers include "the pager just went off", "prod is down", "we have an outage", "users are reporting", "something broke after my deploy", or "how do I write this postmortem". Walks triage, coordination, mitigation, resolution, and follow-up, plus the mindset — stop the bleeding first, over-communicate, pull people in, blameless postmortems, not done until the follow-ups are. Keep responses short and directive while an incident is active. For holding the pager when nothing is on fire, route to on-call-shift. Do not trigger for non-urgent debugging.
---

# incident-response

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 9, "Going On-Call"** — the incident-handling section. The five-phase structure this skill follows (**triage → coordination → mitigation → resolution → follow-up**) comes from that chapter, as does the rule that **an incident is not done until every follow-up task is complete.**

The flow is reinforced by, and largely agrees with, common SRE practice — see the *Where this comes from* section below for the full citation list.

For the day-to-day of holding the pager when nothing is broken — support queues, priority ladders, handoffs, sustainability — see [`on-call-shift`](../on-call-shift/SKILL.md), which folds the rest of the same chapter. See [`JOURNEY.md`](../../../../JOURNEY.md) for the stage map and [`operator-playbook`](../operator-playbook/SKILL.md) for the broader Operator-stage context.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (production debugging under pressure)
- **Builds:** Leadership (taking ownership when a system is broken)

## What this skill is for

The pager fired. Something is broken. The user is probably stressed, possibly tired, possibly first-time-on-call. This skill exists to give them a calm structure to hold onto when their brain wants to spiral.

It also fires for non-active prep — preparing for a first on-call shift, asking how to handle incidents in general — and walks through the same flow more reflectively.

## Where this comes from

This skill synthesizes:

- ***The Missing Readme*** (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 9, "Going On-Call"** — the primary anchor. The five-phase incident structure (triage, coordination, mitigation, resolution, follow-up), the *stop the bleeding* mitigation list (roll back, fail over, disable the feature, add resources), and the *not-done-until-follow-up-is-done* rule.
- ***Site Reliability Engineering*** (Beyer, Jones, Petoff, & Murphy, Google/O'Reilly 2016), free online at https://sre.google/sre-book/table-of-contents/ — the *mitigate before you understand* discipline and the formal incident-command structure. Chapter 9's own Level Up section points at **Ch. 13** (Emergency Response), **Ch. 14** (Managing Incidents), and **Ch. 15** (Postmortem Culture) specifically.
- ***The Site Reliability Workbook*** (Beyer et al., Google/O'Reilly 2018) — practical guidance on running incidents and writing postmortems.
- **Blameless postmortem culture** — anchored in John Allspaw's foundational *"Blameless PostMortems and a Just Culture"* (Etsy, 2012) at https://www.etsy.com/codeascraft/blameless-postmortems/. The *"humans will make mistakes; systems can be designed to absorb them"* framing is the canonical statement of the principle.
- **"*What Happens When the Pager Goes Off?*"** — *Increment* magazine, on-call issue: https://increment.com/on-call/when-the-pager-goes-off/. Practitioner accounts of what being paged actually feels like across several companies. Surfaced from Chapter 9's Level Up section.

If asked where a specific piece of advice comes from, point to the relevant source above.

## The core mindset (lead with this, every time)

**Stop the bleeding before you fix the wound.**

- Your first job is to **mitigate**, not to find the root cause. Restoring service buys time to investigate calmly.
- **Over-communicate.** Silence during an incident is read as "everything's fine" or "they don't know" — neither is what you want. Even "still investigating" every 10 minutes is golden.
- **Pull people in.** It is not bravery to handle a production incident alone. It is a mistake. The senior on-call partner exists for this.
- **The pager is not personal.** Even if it was your code, the system allowed it through review, deploy, and rollout. The incident is the system's, not yours.
- **Postmortems are about the system, not the human.** Always blameless.
- **The incident is not over when service is restored.** It's over when the follow-up tasks that stop it recurring are actually done.

## The flow (when an incident is active)

If the user just told you something is on fire, **do not lecture**. Walk them through these steps one at a time, ask short questions, and let them act between turns.

The five phases from *The Missing Readme* Ch. 9 are **triage → coordination → mitigation → resolution → follow-up**. The steps below expand that, splitting out acknowledgment (the thing to do in the first thirty seconds) and treating coordination as two distinct jobs: *escalating to whoever can fix it* and *keeping everyone else informed*.

### 1. Acknowledge

- Acknowledge the page in your paging tool (PagerDuty, Opsgenie, etc.) so the rotation knows it's claimed.
- Open the incident channel (or create one — usually `#inc-<short-name>`).
- Post one line: *"Investigating page about X."* Even if you don't know what's happening yet.

### 2. Triage — what's broken, how bad, and who can fix it

Three questions. Answer them in under two minutes:

**What's the problem?**

- Which service, endpoint, or feature is broken?
- Is it getting worse, stable, or improving?

**How severe is it?**

- **Who's affected?** All users? A region? Logged-in users? One cohort?
- **Customer-facing?** If yes, severity goes up.
- **Data integrity at risk?** If yes, severity goes way up. Pull people in immediately.

Set a severity level using your team's ladder (P0–P4, SEV1–3, whatever they use — the [`on-call-shift`](../on-call-shift/SKILL.md) skill has the P0–P4 ladder in full). **When in doubt, go higher** — downgrading is cheap.

**Who can fix it?** This is the third leg of triage and the one people forget. If it isn't you, your job shifts from *fixing* to *coordinating* — go to step 3 immediately rather than burning twenty minutes proving you can't fix it yourself.

### 3. Coordinate — escalate, then keep everyone informed

Two distinct jobs here. Both matter.

**Escalate to whoever can actually fix it.** If the problem is in a system you don't own or can't safely change, your most valuable action is getting the right person online — not continuing to investigate alone. Page the owning team. Pull in your senior on-call partner. This is the single highest-leverage move an on-call makes, and hesitating on it is the most common way incidents get long.

**Keep everyone else informed.**

- **Post in the incident channel** with the triage answers.
- **If customer-facing, update the status page** (or ask whoever owns it).
- **Set a comms cadence** — *"I'll post an update every 10 minutes even if nothing has changed."* Then stick to it. Silence reads as either "it's fine" or "nobody's on it."
- **Say when you don't know.** *"Still investigating, no root cause yet"* is a real and useful update.

### 4. Mitigate (not fix)

The goal at this stage is to **get things stable as quickly as possible** — not to understand what's wrong. Common mitigations:

- **Roll back** the recent deploy. (If a recent deploy might be the cause and rollback is safe — usually yes.)
- **Disable the misbehaving feature**, usually via feature flag. See [`progressive-rollout`](../progressive-rollout/SKILL.md).
- **Fail over** to another environment, region, or replica.
- **Add resources** if it's capacity-related — more instances, more replicas, a bigger pool.
- **Route traffic away** from the affected region, instance, or version.

If mitigation works, you're now in **stable but unrooted-cause** state. That's fine — it's the intended destination of this phase. Take a breath. Communicate it.

### 5. Resolve — address the underlying issue

Once stable, the pressure is off and you can do real engineering:

- Investigate the root cause without active impact bearing down on you.
- Build the real fix (usually a separate PR with proper review — see [`code-review`](../code-review/SKILL.md)).
- Re-enable the feature flag, redeploy, restore the failed-over traffic once the fix is live.
- Stand down the incident only when you're confident it won't immediately recur.

### 6. Follow up — and don't call it done early

**The incident is not finished when service is restored. It is finished when the follow-up tasks are complete.**

- **Investigate the root cause properly** — why did this happen, and why did the system permit it?
- **Run a postmortem** if the incident was severe. Blameless, always. Template in the callout below.
- **File follow-up tasks** for the changes that prevent recurrence — each with a named owner and a due date.
- **Track them to completion.** This is the step that actually separates teams that get more reliable over time from teams that keep having the same outage. An action-item list nobody closes is a list of wishes.

If the follow-up work keeps getting deprioritized against feature work, that's a case to make deliberately — see [`technical-debt`](../technical-debt/SKILL.md) for framing the argument.

---

## Callout — Blameless postmortems

The single most important word in postmortem culture is **blameless.** Not because nobody made a mistake, but because the system shouldn't have *allowed* a single mistake to take production down.

### The principle

- Humans will make mistakes. That's not a fixable problem.
- Systems can be designed to absorb, catch, or contain those mistakes. That *is* fixable.
- A postmortem that ends with *"X should have been more careful"* has learned nothing. A postmortem that ends with *"the deploy pipeline should refuse to deploy without a passing migration test"* has learned something.

### A simple template

```
# Postmortem: [short incident name]

## Summary
[2-3 sentences: what happened, who was affected, how long]

## Impact
- [users affected, region, duration]
- [revenue / SLA impact if known]

## Timeline
- HH:MM — page fires
- HH:MM — acknowledged by [name]
- HH:MM — root cause hypothesized
- HH:MM — mitigation applied
- HH:MM — service stable
- HH:MM — incident closed

## Root cause
[the thing in the system that allowed this to happen — not the human]

## What went well
[honest list — fast triage, good comms, etc.]

## What went poorly
[honest list — late comms, missing runbook, alert fatigue, etc.]

## Action items
- [ ] [specific change, with an owner and a due date]
- [ ] [specific change, with an owner and a due date]
```

### The non-negotiables

- **Names without blame.** Use names for who did what (because that's accurate), but never frame their actions as the cause.
- **Action items have owners and deadlines.** Otherwise they're wishes, not changes.
- **Timestamps throughout.** The timeline is the most-reread part of any postmortem; without timestamps it can't be correlated against logs or dashboards.
- **Share the postmortem broadly.** Other teams learn from your incident — that's how the org gets safer.
- **The incident closes when the action items close.** Not when the postmortem is published.

---

## Output style — *especially during active incidents*

- **Short, calm, directive.** Long paragraphs are wrong tone for someone whose pager is going off.
- **One step at a time.** Ask: *"What do you see right now?"* then *"What's the impact?"* then *"What can you mitigate?"* — don't dump the whole flow.
- **Validate the stress.** *"That sounds intense — let's take it step by step."* costs nothing and helps.
- **Default to pulling people in.** If the user is solo on something serious, suggest paging the on-call partner before going further.
- **Push timestamped notes.** Remind them to note what they did and when, as they go. It's nearly free during the incident and invaluable in the postmortem.

For non-active situations (learning the flow, writing a postmortem after the fact), be more discursive — walk through the structure and the mindset, give examples, take the time to teach.
- **Proactive surfacing is suspended while the incident is live.** Output Protocol 10.7 asks skills to close by naming an adjacent concern the user hasn't raised. During an active incident that is wrong — it competes for attention the user does not have, and every sentence that isn't the next action is a cost. Surface only what changes what they do *right now* (an unnoticed data-integrity risk, a person who must be paged). Once service is stable, 10.7 resumes normally: the follow-up tasks, the postmortem, the teams who should hear what happened.

## When NOT to use this skill

- Nothing is on fire and the user is asking about the *day-to-day* of being on call — the support queue, prioritizing requests, shift handoffs, on-call burnout, preparing for a first shift. Route to [`on-call-shift`](../on-call-shift/SKILL.md).
- The user is asking general questions about operations or observability with no active incident. Route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is asking how to *write* code for reliability (defensive programming, retries). Route to [`defensive-programming`](../defensive-programming/SKILL.md) or [`retry-and-backoff`](../retry-and-backoff/SKILL.md).
- The user is debugging a non-production issue (test failure, local bug). Skip.
- The user wants to make the case for fixing the reliability problem behind repeated incidents. Route to [`technical-debt`](../technical-debt/SKILL.md).
- The incident is fully resolved and the user is doing reflection only on the postmortem — okay to fire, but lean on the postmortem callout.
