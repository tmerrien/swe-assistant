---
name: idempotency
description: Use when the user is designing an operation that may be executed more than once with the same effect — typically an API endpoint, message-queue handler, webhook receiver, RPC handler, or any operation that might be retried by a client, replayed by a queue, or duplicated by a network. Triggers include phrases like "how do I make this idempotent", "is this operation idempotent", "what does idempotency mean", "I'm worried about double-charges", "deduplication", "exactly-once delivery", "the request might be sent twice", "webhook delivered twice", "client may retry", "how do I handle duplicate requests", "should this be a POST or PUT", or asking about request IDs, idempotency keys, or designing safe-to-retry operations. Walks through the idempotency discipline from The Missing Readme (Chapter 4) — what idempotency is and isn't, the HTTP-method-semantics framing, common patterns (idempotency keys, request IDs, state-based checks), and the failure modes when operations aren't idempotent but get retried. For the client-side retry mechanics (backoff, jitter), route to retry-and-backoff. Do not trigger for read operations (already idempotent by nature), code reviews, or general defensive coding.
---

# idempotency

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Defensive Programming, subsection on idempotent systems). The HTTP-method-semantics framing is from RFC 9110 and is canonical practitioner knowledge.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (idempotent APIs are easier to reason about and document)
- **Builds:** Leadership (designing for safe operation interactions raises the team's reliability bar)

## What this skill is for

When operations can be safely repeated, an enormous class of distributed-system bugs disappears. Network failures stop being scary. Retries (see [`retry-and-backoff`](../retry-and-backoff/SKILL.md)) become safe. Webhook replays stop causing double-charges. Message queues with at-least-once delivery stop requiring complex deduplication logic in every consumer.

This skill fires when the user is designing the *receiving* operation — the endpoint, handler, or processor that may execute the same request more than once. It explains what idempotency is, when it's required, and how to design for it.

## The core mindset (lead with this)

**If an operation will ever be retried, replayed, or duplicated, it must be idempotent — or the system has a bug waiting to fire.**

- *"Will it be retried"* is almost always *yes* in distributed systems. Networks fail, queues redeliver, clients re-issue.
- Idempotency is a **property of the operation as designed**, not of any individual call. You can't add it later by adding more retries.
- The cost of idempotency at design time is much smaller than the cost of debugging a double-execution in production.

---

## What idempotency actually is

A function (or API call, or message handler) is **idempotent** if calling it multiple times with the same arguments produces the same final state and observable result as calling it once.

The classic test:

> *f(x); f(x); f(x);* should leave the system in the same state as just *f(x);*

This is **not** the same as "the function doesn't change state." Setting a value is idempotent (the second `SET name=alice` does nothing new). Adding a value is **not** idempotent (the second `ADD 1 to balance` charges twice).

## The HTTP-method-semantics anchor

Most engineers know HTTP. The HTTP method semantics are the textbook example of the concept:

| Method | Idempotent? | Mental model |
|---|---|---|
| `GET` | ✅ Yes | Reads have no side effects. Calling twice = calling once. |
| `HEAD` | ✅ Yes | Same as GET, just no body. |
| `PUT` | ✅ Yes (by spec) | Replaces resource with the given representation. *"Set to X"* — twice doesn't matter. |
| `DELETE` | ✅ Yes (by spec) | Removes the resource. Already-deleted is the desired state. |
| `POST` | ❌ No (by convention) | Creates a new resource. Twice = two resources. |
| `PATCH` | ❌ No (in general) | Applies a delta. *"+5 to balance"* — twice changes the result. |

**When designing an HTTP endpoint:**

- *Reading data* → use `GET`. Idempotent by nature.
- *Setting a resource to a known state* → use `PUT`. Idempotent.
- *Creating a new resource where each call should produce one* → use `POST`. **Make it idempotent anyway** (see patterns below).
- *Deleting* → use `DELETE`. Idempotent (second DELETE returns 404 or 200 with no effect).

The point isn't the verb — it's that the *semantics* of the operation match the verb. A `POST` that handles duplicate-key conflicts gracefully is more idempotent than a `PUT` that doesn't handle them at all.

---

## Patterns for making operations idempotent

Four common patterns, in roughly increasing complexity.

### 1. State-based check (the simplest pattern)

Before performing the action, check whether the state already reflects the desired outcome. If so, return success without re-applying.

```
def mark_user_verified(user_id):
    user = get_user(user_id)
    if user.verified:
        return SUCCESS  # already done, no-op
    user.verified = True
    save(user)
    return SUCCESS
```

Works well for operations that put the system into a specific state (verified, deleted, archived). Calling twice produces the same final state.

### 2. Idempotency key (Stripe-style)

The client generates a unique key per logical operation and sends it with the request. The server:

1. Looks up the key.
2. If it's been seen, returns the previously-recorded response (without re-executing).
3. If it's new, executes the operation, records the response keyed by the idempotency key, and returns.

```
POST /charges
Idempotency-Key: a7f3e9c2-1d4b-4b8a-9c2e-...

{ "amount": 1000, "currency": "USD", "customer": "cus_123" }
```

Used by Stripe, Square, AWS, and many other APIs for safe POST. Engineers implementing webhook receivers should adopt this pattern.

**Implementation notes:**

- Store idempotency-key → response with a reasonable TTL (Stripe uses 24 hours).
- The response stored must be the *successful* response. Don't cache failure unless the failure is itself idempotent.
- Use a unique constraint or atomic compare-and-set to handle races where the same key arrives twice in parallel.

### 3. Natural deduplication via unique constraints

For operations that create resources with a natural unique identifier, let the database's unique constraint do the work:

```sql
INSERT INTO orders (external_order_id, ...) VALUES ('ord_abc123', ...)
ON CONFLICT (external_order_id) DO NOTHING;
```

The second insert is a no-op. The operation is idempotent as long as the external ID is reliably the same across retries.

### 4. Sequence numbers / version tokens

For state-machine operations, the client sends the version they're operating against. The server rejects if the version has moved on.

```
PUT /orders/123  If-Match: "v7"
```

If the order has moved past v7, the second PUT returns 409 (conflict), preventing accidental overwrites. The first PUT advances the version, so the retry sees the new version and the conflict resolution can be principled.

---

## Failure modes when operations aren't idempotent

Bugs that look like "weird production issues" are often missing idempotency:

- **Double charges.** Payment endpoint accepts POST without idempotency keys; client times out and retries; user is charged twice.
- **Duplicate emails.** Welcome-email handler runs twice because the message-queue retried after a client crash mid-processing.
- **Order duplication.** External order ID isn't unique-constrained; user clicks "Submit" twice, both pass.
- **State corruption.** Increment-style operations (counter += 1, balance -= amount) double-apply silently.
- **Phantom resources.** Resource-creation API doesn't dedupe; clients retry on timeout; cleanup later struggles to identify the "real" resource.

Each of these is fixable by retrofit, but the retrofit is much more expensive than the up-front design.

---

## Operations that are idempotent without effort

Some operations are inherently idempotent and don't need any special handling:

- **Reads** (GET, queries that don't mutate).
- **Pure functions** (computation without side effects).
- **Set-to-X operations** where X is the desired terminal state, not a delta.
- **Operations where the receiving system already deduplicates** (some queue services, some databases).

If your operation falls into one of these categories, you're already done. Note this in the API documentation so callers know they can retry freely.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's design if shared, route to retry-and-backoff for the client-side mechanics.**

### Step 1 — Diagnose

If the user described the operation, work on that. Otherwise ask **one** question:

- *"What operation are you designing — what does it do, and how can it get called more than once?"*

### Step 2 — Determine whether idempotency is required

Quick test:

- Is it a read? → Already idempotent. You're done. Document it.
- Is it a state-setter (mark verified, set status to X)? → Use the state-based check pattern.
- Is it a creator (new charge, new order, new email)? → It must be idempotent — use idempotency keys or unique constraints.
- Is it an incrementer (add to balance, append to log)? → It is *not* naturally idempotent; design it explicitly with one of the patterns above, or accept that it cannot be safely retried.

### Step 3 — Pick the pattern that fits

Map their operation to one of the four patterns. Help them draft the implementation in their language/stack.

### Step 4 — Document it

The operation's idempotency guarantee belongs in the API documentation. Callers need to know whether they can safely retry.

### Step 5 — Close

Confirm the pattern chosen and the one concrete code change. If they're also writing the client side, route to [`retry-and-backoff`](../retry-and-backoff/SKILL.md).

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Idempotency is a clear conceptual area; you usually only need one diagnostic question.
- **Use the HTTP-methods table early** if the user is designing a web API — it grounds the concept fast.
- **Work on the user's specific operation.** Apply a pattern to their actual design rather than walking the menu.
- **Be explicit when an operation is not idempotent and cannot easily be made so.** Some operations genuinely can't be retried; the right answer is to fail fast and surface the failure clearly (route to [`retry-and-backoff`](../retry-and-backoff/SKILL.md) for the fail-fast guidance).

## When NOT to use this skill

- The user is writing the *client-side* retry logic — route to [`retry-and-backoff`](../retry-and-backoff/SKILL.md).
- The operation is a read — already idempotent; help with whatever they actually need.
- The user is reviewing a PR — route to [`code-review`](../code-review/SKILL.md) with idempotency as a lens for state-changing endpoints.
- The user is in an active incident from a non-idempotent operation having fired twice — route to [`incident-response`](../incident-response/SKILL.md). The skill applies to design-time work, not firefighting.
