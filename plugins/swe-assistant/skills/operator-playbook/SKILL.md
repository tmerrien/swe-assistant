---
name: operator-playbook
description: Use when the user is in the Operator stage — taking responsibility for what happens after code is merged. Triggers include asking how their code gets from a PR to production (build, release, deploy, rollout), asking about observability (metrics, logs, traces), preparing to join an on-call rotation for the first time, asking how to debug a problem in production, asking about feature flags or canary releases, asking how to set up monitoring or alerting, or expressing the shift from "I ship features" to "I run software in production." Walks through the Operator playbook from The Missing Readme — the delivery pipeline, observability primer, on-call basics, and defending software (feature flags, canaries, monitoring). For active incidents (pager just fired, prod is on fire), route to the incident-response skill. Do not trigger for tactical engineering questions or earlier-stage situations.
---

# operator-playbook

## Source

*The Missing Readme*, Chapter 1, "The Journey Ahead" — the **Operator** stage (the book calls this "Operations Ocean"). The chapter sketches this stage at a high level; deeper material on operations and incidents lives in later chapters and will fold into this skill (and [`incident-response`](../incident-response/SKILL.md)) over time. See [`JOURNEY.md`](../../../../JOURNEY.md) for the full stage map.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (status during incidents, postmortems)
- **Builds:** Leadership (taking responsibility for systems, not just changes)

## What this skill is for

The Operator stage is when you start taking responsibility for what happens *after* code is merged. Up to this point, "done" might have meant "PR is approved." Now "done" means "running in production, observable, recoverable, and not waking anyone up at 2am."

This skill fires when the user is moving into that mindset. It helps them build the operational instincts: knowing the pipeline, knowing the observability tools, knowing how to defend software from itself and its users.

## The core mindset (lead with this)

**Code only matters when it's running and not breaking.**

- Shipping is the start of a piece of software's life, not the end.
- You don't fully understand a piece of code until you've operated it.
- Defensive engineering is empathy — for the on-call engineer at 2am, for users, for future-you.
- Production is the only environment that matters. Staging is a hint.

If the user is anxious about going on-call or about something they shipped breaking, lead with the mindset: this is a different skillset, and everyone learns it the same way (by doing it, with help).

## How to run the playbook

### Step 1 — Frame the moment

Two or three sentences. Name the shift (shipping → operating). Tell them you'll tailor the rest.

### Step 2 — If their first message doesn't already tell you, ask ONE short question

Per the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol), this is one question, not a list. Skip the step if the user already gave you the context.

Otherwise, ask something like: *"What's the situation — joining on-call, learning the deploy pipeline, designing for safe rollout, or wanting an overview?"* — phrased as one question.

If they mention an active production issue at any point, drop everything and route to [`incident-response`](../incident-response/SKILL.md).

The categories below are how *you* read the situation, not options to recite back:

- About to join the on-call rotation for the first time.
- Trying to understand how the team's deploy pipeline works.
- Investigating a production issue right now (→ route to [`incident-response`](../incident-response/SKILL.md)).
- Designing a feature and wondering how to ship it safely.
- Wanting an overview because this whole area feels foreign.

### Step 3 — Surface the relevant moves

Pick 2–4 items most relevant to where they are.

#### The delivery pipeline (end to end)

Most engineers can describe their code. Fewer can describe how it actually gets to a user. The pipeline usually looks something like:

1. **Test** — automated tests run on every PR (unit, integration, sometimes end-to-end).
2. **Build** — the code is compiled, packaged, containerized, and tagged with a version.
3. **Release** — the build is promoted to a release candidate (sometimes a separate step, sometimes fused with deploy).
4. **Deploy** — the release is rolled out to environments (staging → canary → production, or some variant).
5. **Rollout / Progressive Delivery** — the deploy is gradually exposed to more traffic or more users (e.g., 1% → 10% → 100%, or one region at a time, or behind a feature flag).

**Action for the user:** Trace one of your recent commits through this whole pipeline. Where does the code go? What logs does it leave? Who would notice if it broke at each step? Most engineers learn this the hard way during their first incident — better to learn it on a calm afternoon.

#### Defending the software

These are the cheap habits that prevent most of the bad days:

- **Feature flags.** Risky or new features go behind a flag so you can turn them off without re-deploying. The first time you have to disable something at 2am you'll never ship without one again.
- **Canaries.** Roll out to a small slice (1–5% of traffic, or a single region) first. If error rates spike, you've blown up 1% of users instead of 100%.
- **Monitoring on what matters.** Not "all the metrics" — just the ones you'd be sad about. Latency, error rate, throughput, business outcome (signups, payments, whatever).
- **Alerting that's actionable.** An alert should tell you *what's wrong, who cares, and what to try.* If an alert fires regularly and nobody acts on it, either fix it or delete it.
- **Designed for rollback.** Database migrations are reversible (or have a documented forward-only rollback plan). Config changes can be reverted. New endpoints don't break old clients.

#### On-call basics

If you're about to join the rotation:

- **Read the on-call runbook before your first shift.** If there isn't one, that's your first contribution.
- **Know who to escalate to.** Pull in a senior on-call partner. Going solo on your first incident is bravado, not skill.
- **Acknowledge the page fast.** Even just "I see it, looking" calms everyone.
- **It's okay to not know.** "I don't know what's happening yet, investigating" is a real status update.
- For the actual incident flow when a page fires, see [`incident-response`](../incident-response/SKILL.md).

---

## Callout — The three pillars of observability (metrics, logs, traces)

The book mentions metrics, logs, and traces. Each tool answers a different kind of question; reaching for the wrong one wastes hours.

### Metrics — *numbers over time*

- **What they are:** counters and gauges aggregated over time. *"Error rate is 2%, was 0.3% an hour ago."*
- **What they're great for:** dashboards, alerting on thresholds, spotting trends, comparing before/after.
- **What they're bad at:** explaining *why* a single user's request failed. Aggregates lose individual context.
- **Examples:** Prometheus, Datadog metrics, CloudWatch.

### Logs — *discrete events with context*

- **What they are:** timestamped records of things that happened. *"User 12345 attempted login at 14:32:01 and got error 'invalid_token'."*
- **What they're great for:** forensics, understanding what one specific user or request experienced, finding errors with stack traces.
- **What they're bad at:** seeing trends (you have to aggregate them yourself, expensively).
- **Examples:** Splunk, Datadog logs, CloudWatch Logs, ELK.

### Traces — *the path of a single request through many services*

- **What they are:** a connected timeline showing how one request flowed: *"API got the request → called auth (100ms) → called DB (50ms) → called billing (failed at 200ms)."*
- **What they're great for:** debugging multi-service problems, finding slow steps in a chain, understanding what *actually* happens when a user hits an endpoint.
- **What they're bad at:** noticing things you weren't already looking at. You have to know which trace to look up.
- **Examples:** Datadog APM, Honeycomb, Jaeger, OpenTelemetry-based tools.

### The decision tree

- *"Is the system healthy overall?"* → metrics
- *"What happened to this specific user / request?"* → logs (then traces if multi-service)
- *"Why is this slow / where is the bottleneck?"* → traces
- *"Has this been happening for a while or is it new?"* → metrics

If you only know one of the three at your company, learn that one well. Then add the next.

---

### Step 4 — Pick one move for this week

Ask: *"Out of everything we covered, what's one thing you'll do this week? Be specific."*

Push for concreteness:

- *"Learn observability"* is too vague.
- *"Trace one of my recent commits through the deploy pipeline by Wednesday and write down what each step does"* is the action.

If they're stuck, offer 2–3 options tied to where they are.

### Step 5 — Close

Two sentences: confirm the action, offer to come back when they have questions or hit something specific. If they're going on-call soon, remind them that [`incident-response`](../incident-response/SKILL.md) is there for when the pager fires.

## Output style

- Conversational. Surface only the relevant section based on where they are.
- If the user mentions an active incident, **drop everything and route to** [`incident-response`](../incident-response/SKILL.md). Operator-playbook is for calm-afternoon thinking, not for 2am.
- For the observability primer, only surface it if they ask about metrics/logs/traces or seem unsure which to use.

## When NOT to use this skill

- Prod is on fire right now. Route to [`incident-response`](../incident-response/SKILL.md) immediately.
- The user is in Newcomer, Ramp-Up, or Contributor stage and not yet operating. Route to the appropriate playbook.
- The user is doing general growth reflection. Route to [`growth-self-check`](../growth-self-check/SKILL.md).
- Tactical engineering question with no operations framing. Skip.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- *Amazon Builder's Library* (https://aws.amazon.com/builders-library) — curated essays by Amazon principal engineers on building and operating production systems at scale. Probably the best web resource for learning how large-scale operations actually work.
- *Building Secure & Reliable Systems* — Adkins, Beyer, et al. (Google, O'Reilly 2020). Free online at https://sre.google/books/building-secure-reliable-systems/. Operations and security at scale, from the team that wrote the canonical SRE book.

