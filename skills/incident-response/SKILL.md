---
name: incident-response
description: Use when the user is in the middle of (or just been paged for) a production incident — something is broken, customers may be affected, and they need to act. Triggers include phrases like "the pager just went off", "prod is down", "we have an outage", "users are reporting", "I just got paged", "something broke after my deploy", "the dashboard is red", "I'm in the middle of an incident", "what do I do, this is on fire", or asking how to handle an incident in general (preparing for first on-call shift, asking what to do when paged, asking how to write a postmortem after an incident). Walks through the universal incident flow — acknowledge, triage, communicate, mitigate, resolve, postmortem — and the mindset that goes with it (stop the bleeding before you fix the wound; over-communicate; pull people in; blameless postmortem). Keep responses short and directive when an incident is active. Do not trigger for non-urgent debugging, code questions, or general operational planning — those go to operator-playbook or other skills.
---

# incident-response

## Source

**Starter skill** — built from common SRE practice (Google SRE Book conventions, widely-shared incident response playbooks). The Missing Readme Chapter 1 only gestures at incidents at this stage; deeper chapter material on operations and incidents will fold in when we get to it. Treat this skill as a living draft.

See [`JOURNEY.md`](../../JOURNEY.md) for the full stage map and [`operator-playbook`](../operator-playbook/SKILL.md) for the broader Operator-stage context.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (production debugging under pressure)
- **Builds:** Leadership (taking ownership when a system is broken)

## What this skill is for

The pager fired. Something is broken. The user is probably stressed, possibly tired, possibly first-time-on-call. This skill exists to give them a calm structure to hold onto when their brain wants to spiral.

It also fires for non-active prep — preparing for a first on-call shift, asking how to handle incidents in general — and walks through the same flow more reflectively.

## The core mindset (lead with this, every time)

**Stop the bleeding before you fix the wound.**

- Your first job is to **mitigate**, not to find the root cause. Restoring service buys time to investigate calmly.
- **Over-communicate.** Silence during an incident is read as "everything's fine" or "they don't know" — neither is what you want. Even "still investigating" every 10 minutes is golden.
- **Pull people in.** It is not bravery to handle a production incident alone. It is a mistake. The senior on-call partner exists for this.
- **The pager is not personal.** Even if it was your code, the system allowed it through review, deploy, and rollout. The incident is the system's, not yours.
- **Postmortems are about the system, not the human.** Always blameless.

## The flow (when an incident is active)

If the user just told you something is on fire, **do not lecture**. Walk them through these steps one at a time, ask short questions, and let them act between turns.

### 1. Acknowledge

- Acknowledge the page in your paging tool (PagerDuty, Opsgenie, etc.) so the rotation knows it's claimed.
- Open the incident channel (or create one — usually `#inc-<short-name>`).
- Post one line: *"Investigating page about X."* Even if you don't know what's happening yet.

### 2. Triage — what's the impact?

Quick questions to answer in under two minutes:

- **What's broken?** Which service, endpoint, feature?
- **Who's affected?** All users? A region? Logged-in users? A specific cohort?
- **Customer-facing?** If yes, severity goes up.
- **Data integrity at risk?** If yes, severity goes way up. Pull people in immediately.
- **Is it getting worse, stable, or improving?**

Set a severity level if your team uses them (SEV1/2/3 or P1/P2/P3 etc.). When in doubt, go higher — easier to downgrade than upgrade.

### 3. Communicate

- **Post in the incident channel** with the triage answers.
- **If customer-facing, update the status page** (or ask whoever owns it).
- **Tag the right people** based on severity. If SEV1/SEV2 (or unsure), pull in your on-call partner immediately.
- **Set a comms cadence** — "I'll post an update every 10 minutes even if nothing has changed." Then stick to it.

### 4. Mitigate (not fix)

The goal at this stage is to **restore service**, not to understand what's wrong. Common mitigations:

- **Roll back** the recent deploy. (If a recent deploy might be the cause and rollback is safe — usually yes.)
- **Disable the feature flag** for the new behavior.
- **Scale up** if it's load-related (more capacity, more replicas).
- **Route traffic away** from the affected region/instance/version.
- **Failover** to a backup if your system has one.

If mitigation works, you're now in **stable but unrooted-cause** state. That's fine. Take a breath. Communicate it.

### 5. Resolve (the actual fix)

Once stable, you can:

- Investigate the root cause without the pressure of active impact.
- Build the real fix (often a separate PR with proper review).
- Re-enable the feature flag, redeploy, etc., once the fix lands.
- Close the incident only when you're confident it won't recur immediately.

### 6. Postmortem

After the dust settles, write a postmortem. See callout below.

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
- **Share the postmortem broadly.** Other teams learn from your incident — that's how the org gets safer.

---

## Output style — *especially during active incidents*

- **Short, calm, directive.** Long paragraphs are wrong tone for someone whose pager is going off.
- **One step at a time.** Ask: *"What do you see right now?"* then *"What's the impact?"* then *"What can you mitigate?"* — don't dump the whole flow.
- **Validate the stress.** *"That sounds intense — let's take it step by step."* costs nothing and helps.
- **Default to pulling people in.** If the user is solo on something serious, suggest paging the on-call partner before going further.

For non-active situations (preparing for first on-call, learning the flow), be more discursive — walk through the structure and the mindset, give examples, take the time to teach.

## When NOT to use this skill

- The user is asking general questions about operations or observability with no active incident or on-call framing. Route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is asking how to *write* code for reliability (defensive programming, retries). That's operator-playbook territory.
- The user is debugging a non-production issue (test failure, local bug). Skip.
- The incident is fully resolved and the user is doing reflection only on the postmortem — okay to fire, but lean on the postmortem callout.
