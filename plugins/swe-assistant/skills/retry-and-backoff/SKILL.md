---
name: retry-and-backoff
description: Use when the user is writing or designing retry logic for calls that can fail transiently — typically remote calls (HTTP requests, database queries, RPC calls, message-queue operations, third-party APIs) but also any operation where failure may be temporary. Triggers include phrases like "how do I retry this", "should I retry on failure", "what's a good backoff strategy", "exponential backoff", "this API call sometimes fails", "the server is occasionally returning 503", "I want to handle transient errors", "retry policy", "max attempts", "I keep getting timeouts", or asking about thundering herd, jitter, or when retries are dangerous. Walks through the retry discipline from The Missing Readme (Chapter 4) — when to retry and when not to, exponential backoff with jitter and a hard cap, the thundering-herd phenomenon and why naive backoff makes it worse, fail-fast-and-loudly for unrecoverable errors. For designing the receiving operation to be safe to retry, route to the idempotency skill. Do not trigger for non-transient logic errors, for code reviews, or for active incidents.
---

# retry-and-backoff

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Defensive Programming, subsections on retry and idempotency). The retry-with-jitter algorithm and thundering-herd terminology are widely-attested SRE practice; see also AWS Architecture Blog's classic write-up on backoff and jitter for the canonical pattern.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (a thoughtful retry policy avoids waking on-call at 2am)
- **Builds:** Leadership (designing client behavior that doesn't take down servers)

## What this skill is for

Remote calls fail. Networks have blips. Servers restart. Dependencies have momentary unavailability. A *useful* retry policy turns transient failures into invisible recoveries; a *naive* retry policy turns transient failures into outages, sometimes for the server being retried.

This skill fires when the user is writing or designing retry logic. The goal is to make the retry useful without making it harmful.

## The core mindset (lead with this)

**Retry transient failures. Fail fast on the rest. Always with backoff. Always with jitter. Always with a cap.**

- A retry is only useful if the failure was *transient*. Retrying a 400 Bad Request just produces more 400s.
- Naive retry without backoff can DDOS the very service you're trying to reach.
- All clients retrying at the same time = thundering herd. Jitter prevents this.
- Unbounded retries can hide real problems indefinitely. Always have a maximum.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's code if shared, route when a different skill fits better.**

### Step 1 — Diagnose

If the user shared code or described the call, work on that directly. Otherwise ask **one** question:

- *"What call are you retrying, and what kind of failure are you trying to handle?"*

### Step 2 — Classify the failure

Not every failure is retryable. The first question is *should* this be retried at all?

- **Retry these (transient):** network timeouts, 5xx errors (especially 502/503/504), rate-limit responses (429 — but respect the `Retry-After` header), connection refused, transient DB deadlocks.
- **Don't retry these (terminal):** 4xx errors except 429 (the request is wrong, retrying won't fix it), authentication failures, validation errors, business-logic rejections.
- **Be very careful retrying writes** — see the idempotency consideration below.

If the failure is terminal, **fail fast and loudly** — log it, surface a clear error, and let the caller decide. Don't loop on a request that will never succeed.

### Step 3 — Design the retry policy

Three required ingredients: backoff, jitter, cap.

#### Exponential backoff

Each retry waits longer than the last. Common formula:

```
delay = base * (2 ^ attempt)
```

Example with base = 100ms:

- Attempt 1: 100ms
- Attempt 2: 200ms
- Attempt 3: 400ms
- Attempt 4: 800ms
- Attempt 5: 1600ms

The exponential growth gives the failing service room to recover without being hammered.

#### Jitter (this is the critical part)

Without jitter, all retrying clients sync up and hit the server in waves — the **thundering herd**. The fix is to add a random jitter to each delay so clients spread out.

Two common patterns:

- **Full jitter:** `delay = random(0, base * 2^attempt)`
- **Equal jitter:** `delay = (base * 2^attempt) / 2 + random(0, (base * 2^attempt) / 2)`

Full jitter is more aggressive at spreading clients out and is usually what you want.

#### Cap

The exponential grows fast. Without a cap, the delay becomes minutes, then hours. Cap it:

```
delay = min(cap, base * 2^attempt) plus jitter
```

Typical caps: 30 seconds to a few minutes, depending on the operation.

#### Maximum attempts

After N retries with no success, stop trying. The point of retry is recovery from *transient* failures; if it hasn't recovered after 5–10 attempts with backoff, the failure isn't transient.

When you stop, surface the failure clearly to whatever called you — don't swallow it.

### Step 4 — Idempotency check

**Before adding a retry, ask: is the operation safe to repeat?**

A retry that re-creates a charge, double-sends an email, or double-writes a record is worse than the original failure. If the operation isn't idempotent, you need to either:

- Make it idempotent before retrying (route to [`idempotency`](../idempotency/SKILL.md) for how).
- Use an explicit at-least-once + dedupe strategy.
- Or accept that this operation can't be safely retried and fail fast.

This check is mandatory; skipping it is one of the most common production-bug sources.

### Step 5 — Implement (use a library if you can)

Most languages have well-tested retry libraries. Use them rather than rolling your own:

- Python: `tenacity`, `backoff`.
- Java: Resilience4j, Spring Retry.
- JavaScript: `p-retry`, `async-retry`.
- Go: `cenkalti/backoff`.
- Rust: `backoff`, `tokio-retry`.

These libraries handle backoff, jitter, and exception classification correctly. They also let you configure cap and max-attempts declaratively.

### Step 6 — Close

Confirm the policy: *"retry on [these errors] with exponential backoff + full jitter, capped at [N seconds], up to [M attempts], failing fast otherwise."* That sentence is your retry policy.

---

## Callout — The thundering herd

A piece of folklore worth installing as a vocabulary.

**The setup:** Many clients are using a shared dependency. The dependency has a momentary blip (database failover, deploy, network glitch). All clients see the failure at roughly the same time.

**Without jitter:** Each client uses the same backoff formula. Their delays are identical: 100ms, 200ms, 400ms... They retry *simultaneously,* hammering the just-recovering dependency, knocking it back down. Loop.

**The result:** A momentary blip becomes a sustained outage, kept alive by the very clients that were trying to recover.

**The fix:** Jitter, so clients spread their retries randomly across a window. The recovering service sees a gradual ramp-up of traffic instead of a wall.

This pattern has taken down many large systems. The fix is one line of code: add jitter.

---

## Callout — Fail fast and loudly

For the failures you *shouldn't* retry — and for the case after you've exhausted retries — the principle is:

- **Fail fast.** Don't waste time on operations that won't succeed.
- **Fail loudly.** Surface the failure with enough information that debugging is fast.

What "loudly" means in practice:

- Log the full error with stack trace, request context (sanitized of secrets), and timing information.
- Increment a metric (`error_count` by error type) so the failure is visible on dashboards.
- For unrecoverable application states, **let the application crash** rather than continuing in a corrupted state. A clean restart is almost always safer than a degraded process.

The opposite — failing slowly and silently — is how transient failures become chronic incidents. *"It just stopped working a few weeks ago and we didn't notice"* is the worst possible failure mode.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about retry classification, backoff policy, and idempotency in one message.
- **Work on the user's specific call if shown.** Walk through retry classification on their actual situation.
- **The idempotency check is mandatory.** If the user is retrying a write operation, surface this early — don't let them ship a double-charge bug.
- **Recommend a library.** Hand-rolled retry logic is almost always buggier than a library; surface the right library for their language.

## When NOT to use this skill

- The user is designing the *receiving* operation to be safe to retry — route to [`idempotency`](../idempotency/SKILL.md).
- The user has a non-transient logic error (their code is wrong, the call would never succeed) — help debug, don't retry.
- The user is in an active incident with a retry storm in progress — route to [`incident-response`](../incident-response/SKILL.md). The mitigation may be to *disable* retries, not tune them.
- The user is reviewing a PR — route to [`code-review`](../code-review/SKILL.md), with retry policy as the lens.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- AWS Architecture Blog: *Exponential Backoff and Jitter* (canonical write-up on the algorithm; widely cited).
- *Amazon Builder's Library* (https://aws.amazon.com/builders-library) — includes the foundational essay *"Timeouts, retries, and backoff with jitter"* which informs much of industry practice (and this skill). Also *"Making retries safe with idempotent APIs"* — pairs with [`idempotency`](../idempotency/SKILL.md).
