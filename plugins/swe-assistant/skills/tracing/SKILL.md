---
name: tracing
description: Use when the user is adding, configuring, or debugging distributed tracing — propagating trace context across service calls, setting up OpenTelemetry or an APM tool, understanding spans and trace IDs, or debugging a multi-service issue with traces. Triggers include "how do I add tracing", "propagate trace context", "trace headers", "spans", "why is this slow across services", or asking what tracing is and when it is useful. Covers verifying you propagate any required state when calling other services, span and trace vocabulary, OpenTelemetry as the modern standard, and when traces beat logs and metrics. For choosing between tracing, logs, and metrics, route to operator-playbook. For active incidents, use the traces rather than discussing how to instrument them.
---

# tracing

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Traces). The book treats this section briefly — its one specific ask is *verify that you are propagating any required state as you make calls to other services.* This skill expands from that anchor using widely-attested industry practice (OpenTelemetry conventions, span/trace vocabulary). The three-pillars-of-observability primer is in [`operator-playbook`](../../../../plugins/swe-assistant/skills/operator-playbook/SKILL.md); this skill goes deeper on the trace pillar specifically.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (traces are how teams see the full path of a request)
- **Builds:** Leadership (instrumented services are diagnosable services)

## What this skill is for

Distributed tracing answers a question no other observability pillar can: *for this one specific request, what was the full path through every service, and where exactly did the time go?* When a user reports *"the checkout was slow at 3:14pm,"* a trace can show that 800ms of the 950ms latency was in a third-party API call you didn't realize was on the critical path.

This skill fires when the user is instrumenting their service for tracing, debugging a multi-service issue, or trying to understand the basic vocabulary.

## The core mindset (lead with this)

**The whole value of distributed tracing comes from context propagation. Without it, you have N disconnected per-service traces instead of one end-to-end story.**

- The book's one ask — *verify you are propagating any required state when calling other services* — is the single most important practice. Without it, the rest is decoration.
- Tracing is most valuable for **multi-service** flows. For single-service profiling, dedicated profilers usually beat traces.
- A trace is the most expensive of the three observability pillars per event, which is why most teams sample (more on this below).

---

## Basic vocabulary

Worth installing before going further.

- **Trace** — the full record of a single request as it moves through one or more services. Each trace has a unique **trace ID**.
- **Span** — a single unit of work within a trace. An HTTP handler is a span; a database query inside that handler is a child span; an outgoing service call from the handler is another child span. Spans nest.
- **Parent / child relationship** — spans form a tree. The HTTP handler is the parent; the work it does (DB query, RPC call, computation) are children. The shape of the tree shows where time was spent.
- **Context** — the metadata (trace ID, current span ID) carried from one piece of code to the next. To propagate context across services, the calling service must include the context in the outgoing request (typically as HTTP headers); the receiving service must read those headers and continue the trace.
- **Sampling** — recording only a fraction of traces (typically 1–10% in high-traffic services). The recorded ones still have full fidelity; the unrecorded ones never existed in the trace store. Tail-based sampling can keep all error/slow traces.

---

## The book's ask: propagate context across service calls

**Verify that you are propagating any required state as you make calls to other services.**

In HTTP-based services, this means: when service A calls service B, A must include the W3C Trace Context headers (`traceparent`, `tracestate`) so B's instrumentation knows to continue the existing trace instead of starting a new one.

Most modern instrumentation libraries do this automatically — *if you use the library's HTTP client wrapper.* If you bypass it (`http.Client` raw in Go, `requests` in Python without the instrumented wrapper), context is dropped, and your trace splits in two with no connection between them.

**Common failure modes:**

- Using a raw HTTP client instead of the instrumented one. Trace splits silently.
- Spawning a worker thread / goroutine / async task without explicitly passing the context. Trace splits in the worker.
- Calling through a message queue without including context in the message metadata. Trace continues on the other end but isn't linked to the origin.
- Using a custom RPC protocol that doesn't have header support. Need to add context fields explicitly.

**The fix is almost always:** use the framework's instrumented client wrapper. If a wrapper doesn't exist, propagate context manually using the library's `context.Inject(headers)` and `context.Extract(headers)` pattern.

---

## How to actually add tracing

For most modern languages and services, the answer is **OpenTelemetry** — the vendor-neutral standard maintained by the CNCF. It supports virtually all backends (Jaeger, Tempo, Honeycomb, Datadog, New Relic, AWS X-Ray, etc.) with the same instrumentation code.

The minimum setup for a new service:

1. **Install the OpenTelemetry SDK** for your language.
2. **Configure an exporter** that sends traces to your team's tracing backend.
3. **Enable auto-instrumentation** for common libraries (HTTP framework, database client, HTTP client). For most popular stacks this is a few lines.
4. **Verify propagation** by making a multi-service call and checking that the trace shows up as a connected tree in your tracing UI. If you see two disconnected traces, propagation is broken (see failure modes above).
5. **Add custom spans** for important application logic (a payment-processing function, a long-running computation). Use `tracer.start_as_current_span("name")` or your language's equivalent.

For older services or unusual stacks, the work is more manual but the pattern is the same: capture context on the way in, propagate it on the way out, end spans cleanly.

---

## When traces beat logs and metrics

Each pillar answers a different kind of question. Use traces for:

- **"Why was *this specific request* slow?"** — the trace shows the full timeline.
- **"Where is the latency in this multi-service flow?"** — the tree of spans shows time per step.
- **"Which downstream is causing the problem?"** — child spans show which calls are slow.
- **"What happened during this one customer report?"** — given a trace ID (often surfaced in error responses or correlation IDs in logs), pull the full trace.

Use **metrics** instead for aggregate questions (*what's the p99 latency?* — see [`metrics`](../metrics/SKILL.md)). Use **logs** for per-event detail when you need full text or stack traces (see [`logging`](../logging/SKILL.md)). The three pillars are complementary; the comparative primer in [`operator-playbook`](../operator-playbook/SKILL.md) is the right reference for "which should I reach for?"

---

## Common gotchas

- **Sampling means most traces don't exist.** If you can't find a trace for a specific request, it was probably sampled out. Some backends support per-request tracing headers (`X-Cloud-Trace-Context`, `b3` debug flag) that force recording — useful when investigating a specific issue.
- **High-cardinality span attributes** have the same problem as high-cardinality metric labels — see the cardinality callout in [`metrics`](../metrics/SKILL.md). Don't put unbounded values (user IDs, raw request bodies) in span attributes.
- **Custom spans should wrap meaningful units of work**, not every function. Over-instrumentation produces noise; the goal is a useful timeline, not a function call trace.
- **Async work needs explicit context handling.** Spawning a task without passing context loses the trace there.
- **Don't log the trace ID separately** if you can include it in your structured logs — most modern logging frameworks have a way to inject the current trace ID into every log line, which lets you jump from a log to the trace in one click.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Diagnose

If the user shared code or named a specific situation, work on that. Otherwise ask **one** question:

- *"Are you setting up tracing for the first time, debugging a multi-service issue with existing traces, or trying to understand the concept?"*

### Step 2 — Match to the right material

- **Setting up for the first time** → the OpenTelemetry "how to actually add tracing" section.
- **Debugging a multi-service issue** → the "when traces beat logs and metrics" section, plus help interpreting the specific trace if shared.
- **Conceptual / first-time** → vocabulary section + the propagation ask.
- **Propagation isn't working** → common failure modes (raw HTTP client, async work, queues).

### Step 3 — One concrete next move

If they're setting up: install OpenTelemetry SDK + the auto-instrumentation for their main framework, then verify propagation with one multi-service call.

If they're debugging: identify the slowest span in the trace and dig into that service.

If they're learning: read one of their existing traces (if they have any) and try to map the span tree to the code path.

### Step 4 — Close

One sentence. Mention [`operator-playbook`](../operator-playbook/SKILL.md) for the broader observability context if relevant.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about setup, propagation, and sampling in one message.
- **The propagation ask is the lead.** Anything else is decoration without it.
- **Match the user's framework.** OpenTelemetry has slightly different APIs across languages; if the user mentions Python / Java / Go / Node, tailor to that.
- **Be honest about the source.** The book gives this section brief treatment; this skill expands from common industry practice. Worth noting if the user is going deep.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking about logging — route to [`logging`](../logging/SKILL.md).
- The user is asking about metrics — route to [`metrics`](../metrics/SKILL.md).
- The user is asking which observability pillar to use for a problem — route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is in an active incident — route to [`incident-response`](../incident-response/SKILL.md). Traces are a tool; the firefighting protocol is in that skill.
- The user is reviewing a PR — route to [`code-review`](../code-review/SKILL.md) with tracing instrumentation as the lens if relevant.
