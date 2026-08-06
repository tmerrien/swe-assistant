---
name: metrics
description: Use when the user is adding, choosing, or designing metrics in their code — deciding between counter / gauge / histogram, picking what to measure, integrating a metrics library, or thinking about SLOs and instrumentation. Triggers include "how do I add metrics", "should this be a counter or a gauge", "how do I measure latency", "what's a histogram", "tracking p99", "what metrics should I emit", "setting up Prometheus / Datadog / OpenTelemetry / StatsD", "instrumenting this service", "measuring this operation", "high cardinality", "metric labels", "SLO", or "I want to know if this is slow in production". Walks through the metrics discipline from The Missing Readme (Chapter 4) — the three common metric types (counter, gauge, histogram), what to measure (resource pools, caches, data structures, CPU and I/O operations, errors, remote calls), using standard libraries instead of rolling your own, and the cardinality and sampling gotchas. For comparing metrics vs logs vs traces (which to reach for when), route to operator-playbook. For active incidents, use the metrics rather than discussing how to write them.
---

# metrics

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Metrics). The three-pillars-of-observability framing (metrics / logs / traces) is in [`operator-playbook`](../operator-playbook/SKILL.md); this skill goes deeper specifically on metrics.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (metrics are how teams agree on what "healthy" means)
- **Builds:** Leadership (instrumented systems are operable systems; this raises the team's reliability bar)

## What this skill is for

Metrics are the numerical equivalent of logs — the difference is that metrics aggregate by design, so you can answer questions like *"what's the p99 latency over the last hour?"* without scanning every event. This skill fires when the user is designing what to measure, picking a metric type, or instrumenting code for the first time.

If you didn't measure it, you can't see it in production — and you can't set an SLO on it, alert on it, or build autoscaling around it. Instrumentation is the substrate for everything else operational.

## The core mindset (lead with this)

**If you don't measure it, you can't see it in production.**

- Metrics are how you find out something is wrong before users tell you (or before users *stop* telling you because they've left).
- The cost of adding a metric is small; the cost of debugging a production issue without one is enormous.
- **Match the metric type to the question.** Wrong type means the data exists but can't answer what you need.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's code if shared, route to the right skill when a different one fits better.**

### Step 1 — Diagnose

If the user shared code or a specific operation, work on that. Otherwise ask **one** question:

- *"What are you measuring, and what question do you want the metric to answer?"*

Skip if the first message already says.

### Step 2 — Pick the metric type

Use the decision rule below — it's almost always the first thing that needs resolving. Once the type is right, the implementation is mechanical.

### Step 3 — Pick the right things to measure

Walk through the relevant subset of the measurement checklist based on what the user's code does. Don't dump the whole list.

### Step 4 — Watch for the gotchas

Cardinality and sampling traps both come up before they're missed; surface the relevant one if their situation suggests it.

### Step 5 — Close

Confirm the change. If they're instrumenting a service end-to-end, mention `operator-playbook` for the broader observability picture.

---

## The three metric types — pick the right one

The single most useful thing this skill does. Most metrics confusion is using the wrong type for the question.

### Counter

A monotonically increasing number. Goes up, never down (except on process restart).

- **Use for:** total requests served, total errors, total bytes processed, total cache hits, total messages handled.
- **Derive rate from a counter** by computing the difference over time (`rate(http_requests_total[5m])` in PromQL). You can always derive rate; you can never derive a counter from a rate.
- **Wrong choice when:** the value should go down sometimes. Use a gauge instead.

### Gauge

A value that can go up or down — a snapshot of "right now."

- **Use for:** current memory used, current queue depth, current open connections, current temperature, current number of active users, current thread-pool size.
- **Sampled at the time of scrape** — between scrapes, the value can have changed many times. If you need the full distribution, that's a histogram.
- **Wrong choice when:** you actually want a total or a rate. Use a counter.
- **Wrong choice when:** you want to know the distribution (p50/p95/p99) of how the value changes. Use a histogram.

### Histogram

A distribution of values, bucketed for later percentile computation.

- **Use for:** request latency, response size, payload size, anything where the average lies and the tail matters.
- **Gives you percentiles** (p50, p95, p99, p999). Critical for SLOs — *"99.9% of requests under 200ms"* requires knowing the distribution, not just the average.
- **More expensive than counters/gauges** — has more buckets, more storage. Don't use for things where the average is fine.
- **Wrong choice when:** the value is a current snapshot (use gauge) or a running total (use counter).

### The decision in one sentence

*Total over time → counter. Value right now → gauge. Distribution of values → histogram.*

---

## What to measure (the checklist)

Walk through the categories that apply to the user's code. Don't try to instrument everything in one pass — start with what matters, add more as the system grows.

### Resource pools — gauge

Pools have a maximum capacity. The interesting questions are *"how full is the pool right now?"* and *"have we been at capacity recently?"*

- **Thread pools.** Active threads, idle threads, queued tasks. A thread pool at capacity with growing queue depth is a leading indicator of cascading failure.
- **Connection pools.** Active connections, idle connections, wait time for acquisition. Database connection-pool saturation is one of the most common production hangs.
- **Worker pools, channel buffers, semaphores** — all gauges.

### Caches — counter

- **Cache hits.** Counter incremented per hit.
- **Cache misses.** Counter incremented per miss.
- The *hit ratio* (hits / (hits + misses)) is derived from these. Don't store the ratio directly — store the counters and compute the ratio in your dashboard.
- A dropping hit ratio is often the first sign of a cache-eviction problem or a key-space change.

### Data structure sizes — gauge

- Current size of in-memory data structures: maps, lists, queues, deques, ring buffers.
- Unbounded growth in any of these is a memory-leak signal long before the OOM.

### CPU-intensive operations — histogram (timer)

- Time the operation; emit as a histogram (often called a "timer" in metrics libraries).
- **Pay special attention to serialization** — JSON encode/decode, Protobuf marshalling, database row mapping. These are CPU-bound and easy to underestimate.
- The shape of the distribution matters: a long tail (p99 much larger than p50) is the bug to investigate.

### I/O-intensive operations — histogram + data size

- **Time the operation.** I/O latencies are unpredictable and the average lies; use histograms.
- **Measure the data size as a separate histogram.** RPC payload sizes, file sizes, query result sizes. Large payloads correlate with slow latencies; having both lets you investigate the link.

### Errors and exceptions — counter

- Count each error type separately (`error_count{type="timeout"}`, `error_count{type="parse_error"}`).
- Track rate of errors over time — error spikes are the most useful early signal of incidents.
- Don't track the error rate as a gauge — store the count and compute the rate in your dashboard.

### Remote requests and responses — counter + histogram

- **Count** every request (and every response by status code).
- **Time** every response. Latency distributions of outgoing calls are usually the most important per-endpoint metric in the entire system.
- Knowing the latency of every remote call you make is what lets you build SLOs and identify *which* downstream is the slow one when something degrades.

---

## Callout — Cardinality (the production trap)

The most common way teams blow up their metrics infrastructure.

**Cardinality** = the number of unique combinations of label values for a metric. Every unique combination is stored as a separate time series; storage and query cost grow roughly linearly with cardinality.

```
http_requests_total{method="GET", status="200"}     ← low cardinality (10s of series)
http_requests_total{method="GET", status="200", user_id="12345"}  ← unbounded cardinality
```

The second example creates a new time series for every user. If you have a million users, that's a million time series for one metric. The metrics backend OOMs; queries become unusable; the bill from your monitoring vendor explodes.

**Rules of thumb:**

- **Never use unbounded IDs as labels.** Not `user_id`, not `request_id`, not `email`, not `trace_id`.
- **Use labels for values with a bounded, small set:** HTTP method (5–10), status code class (5), region (10), endpoint name (50–200), error type (10–50).
- **Per-user / per-request analysis belongs in logs and traces**, not in metrics. (See [`logging`](../logging/SKILL.md) and the [`operator-playbook`](../operator-playbook/SKILL.md) primer on which observability pillar to reach for.)
- **A typical safe upper bound** for any single metric's cardinality is in the low thousands of series. If you're approaching 10,000, redesign.

Many teams have learned this rule from the monitoring bill. Better to learn it from this callout.

---

## Callout — Sampling

Some metrics libraries (especially client-side aggregators like StatsD with sampling, or distributed-tracing libraries that double as metrics) **sample** — they record only a fraction of events for performance reasons.

**What this means:**

- Per-event accuracy is lower than 100% — some events are dropped.
- Aggregate stats (rates, distributions) are statistically representative *if the sampling is random and uniform.*
- Counts at very low traffic volumes can be misleading (a sampled "1 occurrence per minute" might actually be 0–10).

**When it matters:**

- Counts for rare events (errors at low traffic) — sampling under-counts these. Often you want unsampled counts for errors.
- High-percentile latencies (p99.9, p99.99) — sampling can miss the long-tail events these percentiles try to capture.

**Action:** read the docs of your specific metrics library. Know what's being sampled and what isn't. Disable sampling for metrics where you need every event counted (typically errors and important business events).

---

## Use standard libraries

Don't roll your own metrics library. The standards integrate with monitoring backends, dashboarding tools, and alerting systems out of the box.

Common choices by language:

- **Polyglot / cloud-native:** OpenTelemetry (the emerging standard, multi-language, vendor-neutral).
- **Prometheus client libraries:** prometheus_client (Python), micrometer (Java), prometheus/client_golang (Go), prom-client (Node.js).
- **Vendor SDKs:** Datadog client libs, New Relic, Honeycomb.
- **StatsD clients:** any language, simpler protocol, often used with `etsy/statsd` server.

If your company has a preferred library or backend, use that. If not, **start a discussion** to pick one — fragmented choices across services produce fragmented dashboards.

---

## Callout — The SLO connection

Metrics are the substrate for **Service Level Objectives** (SLOs) — explicit commitments about system behavior, like *"99.9% of API requests will complete in under 200ms over each 30-day window."*

- The objective requires a histogram of latencies (you can't compute "99.9% under X" without distribution data).
- The objective produces an **error budget** — the allowed amount of "not meeting the objective" over the window. Error budgets give teams a quantitative way to balance reliability work vs feature work.
- Without metrics, you can't have an SLO. With an SLO, you have a shared definition of "healthy" the team can act on.

Even informally, *"what would my SLO look like for this endpoint?"* is a useful design-time question. It forces you to think about what success looks like and what you need to measure to know.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about type, what to measure, and library choice all at once.
- **Work on the user's specific operation if shared.** Pick the right metric type for *their* code, not the catalog of options.
- **Surface only what fits.** A user instrumenting a remote call doesn't need the resource-pools section.
- **Surface the cardinality callout if labels are involved.** Many users don't yet know about this trap.
- **Recommend their language's idiomatic library** when relevant.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking about logging — route to [`logging`](../logging/SKILL.md).
- The user is asking about distributed traces — there's no dedicated skill yet; route to [`operator-playbook`](../operator-playbook/SKILL.md) for the comparative primer.
- The user is asking which observability pillar to use for a problem (logs vs metrics vs traces) — route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is in an active incident — route to [`incident-response`](../incident-response/SKILL.md). Metrics are a tool for that situation, not a topic to design during it.
- The user is reviewing a PR with metrics changes — route to [`code-review`](../code-review/SKILL.md) with metric quality as the lens.
