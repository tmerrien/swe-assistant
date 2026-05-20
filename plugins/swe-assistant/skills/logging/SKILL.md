---
name: logging
description: Use when the user is adding, reviewing, or designing logging in their code — choosing log levels, structuring messages, deciding what to include or redact, or setting up logging in a service. Triggers include "how do I log this", "what log level should I use", "is this safe to log", "how do I structure my logs", "logging in [language/framework]", "should I log this in info or debug", "my logs are too verbose / too sparse", "this should be redacted", "log aggregator", "structured logging", or "why does enabling verbose logging make this bug disappear". Walks through the logging discipline from The Missing Readme (Chapter 4) — using log levels appropriately, keeping log messages atomic so aggregators can correlate them, keeping logging fast (parameterized, async, no string concat in hot paths), and never logging sensitive data. Do not trigger for general defensive programming (route to defensive-programming), for input validation (route to input-validation), or for active incidents (use the logs to debug rather than discussing how to write them).
---

# logging

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Logging). The three-pillars-of-observability framing (metrics / logs / traces) and the use-cases for each are covered in [`operator-playbook`](../operator-playbook/SKILL.md); this skill goes deeper specifically on logging.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (logs are messages to other engineers)
- **Builds:** Leadership (well-designed logs raise the team's debuggability bar)

## What this skill is for

Most production debugging happens through logs. Whether the bug surfaces at 2am, in a customer report, or in a postmortem, the engineer reaching for the logs is rarely the engineer who wrote them. This skill fires when the user is designing logs for someone they've never met, who is under time pressure, with incomplete context.

Logging is also one of the easiest things to do *poorly* — too verbose, too sparse, in the wrong format, full of secrets, or so slow it changes the application's behavior. This skill helps the user avoid those failure modes.

## The core mindset (lead with this)

**Logs are for the person debugging this at 2am, not for you while you're writing it.**

- The author has full context; the reader has none. Every log message has to carry enough context to be useful in isolation.
- Logs are an interface contract with future-you, with on-call engineers you'll never meet, with auditors, and with anyone investigating a customer complaint.
- A log that's unused is wasted runtime. A log that's missing when needed is a wasted incident.
- Logs are *not* application logic. Don't compute things in log messages that the application needs anyway; log what the application already knows.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's code if shared, route to the right skill when a different one fits better.**

### Step 1 — Diagnose

If the user shared code, work on that. Otherwise ask **one** question:

- *"What are you logging — what code, what situation, and what would you want to know when something goes wrong?"*

Skip if the first message already answers it.

### Step 2 — Identify the issue

Most logging questions fall into one of four buckets. Identify which applies and surface only the relevant practice:

- **What level should this be?** → log-levels section.
- **How do I structure this so it's useful in aggregation?** → atomic-messages section + structured-logging note.
- **Logging is slow / changing my application's behavior?** → fast-logging section + Heisenbug callout.
- **Is this safe to log?** → sensitive-data section + redaction checklist.

### Step 3 — Apply the relevant practice

Walk through the one or two relevant sections from the reference below. Don't dump the whole thing.

### Step 4 — One concrete change

Ask the user to commit to one specific change in their code. *"Of these, which would you do first?"*

### Step 5 — Close

One sentence. Confirm the change, mention any related skill if relevant.

---

## The four practices

### 1. Use log levels deliberately

Logging frameworks let operators filter by importance. The level you pick determines whether anyone sees the message.

| Level | When to use | Audience |
|---|---|---|
| **TRACE** | Function entry/exit, full data dumps, per-iteration inside loops | Only enabled during deep local debugging |
| **DEBUG** | Detailed state useful when investigating an issue, but too noisy for normal operation | Developers debugging a specific problem |
| **INFO** | Normal-operation events: startup, configuration loaded, important state transitions, completed business operations | Operators monitoring healthy systems |
| **WARN** | Something unexpected happened but the system handled it (retry succeeded after one failure, deprecated API path used, fallback triggered) | Operators looking for early signals |
| **ERROR** | Something failed and a user or downstream system is affected. The operation could not complete | On-call attention worthy |
| **FATAL** | The application cannot continue. About to exit | Wake someone up |

**Use the appropriate criticality.** Levels are useful only if you actually distinguish between them. The common failure mode: everything logged as INFO or everything logged as ERROR, making filtering useless.

A useful test: *if INFO logs are dropped, would the team notice?* If yes, that's actually a metric or business event — log it. If no, it's probably DEBUG.

### 2. Keep log messages atomic

Each log message should be useful on its own. Don't split related information across multiple log lines that have to be correlated.

- **All relevant information in one line.** Log aggregators (Splunk, Datadog, ELK, CloudWatch) index per-line. Information split across lines is much harder to correlate, especially under high concurrency.
- **Don't assume log ordering.** In a distributed system or even a multi-threaded application, log lines can arrive out of order. System-clock timestamps don't reliably order events across machines.
- **Avoid newlines inside log messages.** A newline inside a "message" splits it into multiple log records as far as the aggregator is concerned. Strip newlines from interpolated values; for stack traces, use the logging framework's exception-logging API (which keeps the trace atomic).
- **If atomicity isn't possible, use a correlation ID.** Tag related log lines with a `request_id`, `trace_id`, or `transaction_id` so they can be stitched together later by querying the aggregator.

#### A note on structured logging

Most modern logging frameworks support **structured logging** — emitting logs as JSON or another machine-readable format rather than plain text, with fields like `level`, `timestamp`, `message`, `user_id`, `request_id`, plus any custom fields. This pairs naturally with atomic messages: one log record = one event = one queryable JSON object.

If your team's setup supports it, prefer structured logging. Aggregator queries become *"show me all ERROR logs for `user_id=12345`"* instead of grep-and-pray.

### 3. Keep logging fast

Logging runs in your application's hot path. Bad logging can dominate the runtime profile.

- **Use parameterized logging.** Most frameworks accept format strings with placeholders, deferring the actual string construction until they know the log is going to be emitted. String concatenation in the call itself is slow even when the message is filtered out by level.
  
  ```python
  # Bad — builds the string every time, even when DEBUG is off
  logger.debug(f"User {user_id} has balance {balance} after {n_txns} transactions")
  
  # Better — only formats if DEBUG is enabled
  logger.debug("User %s has balance %s after %d transactions", user_id, balance, n_txns)
  ```
  
  (Exact API varies by language/framework, but the principle is universal.)

- **Use asynchronous appenders.** For high-throughput services, configure the logger to buffer and write asynchronously. The synchronous path of your code shouldn't wait on disk I/O or network calls to the log aggregator.

- **Filter early.** Level checks should happen before the message-building work. Most frameworks do this automatically with parameterized logging, but if you have an expensive computation just for the log message (e.g., serializing a large object), guard it explicitly:
  
  ```python
  if logger.isEnabledFor(logging.DEBUG):
      logger.debug("Full state: %s", expensive_state_dump())
  ```

---

## Callout — The Heisenbug warning

**If you enable verbose logging to debug an issue and the bug disappears, the logging change itself might be the reason.**

The phenomenon: logging is not free. Adding more log statements slows the code. In code with race conditions or timing-sensitive bugs, the slowdown can change the interleaving enough that the bug stops manifesting. Disable the verbose logging, the bug returns.

This is one form of a *Heisenbug* — the act of observation changes the system enough that the observed behavior changes.

**What to do:**

- If a bug disappears when you enable verbose logging, suspect a race condition or timing issue. Don't conclude the bug is fixed.
- Try logging at a lower volume (more selective DEBUG statements) and see if the bug returns. If it does, the timing was the issue.
- Tools that can help: thread-sanitizer (TSAN), race detectors, deterministic replay debuggers, deliberately added delays to test the hypothesis.
- The actual fix is to fix the concurrency bug, not to ship the verbose logging.

Engineers who know to suspect logging-timing effects debug these issues much faster.

---

## 4. Don't log sensitive data

Logging sensitive data creates security risks (logs are read by more people than the application's data store) and can violate privacy regulations (GDPR, HIPAA, PCI-DSS, etc.).

### Things to never log (or to redact)

- **Credentials:** passwords, API keys, secret tokens, OAuth refresh tokens, session cookies.
- **Personally identifiable information (PII):** full names if not contextually needed, email addresses, phone numbers, addresses, SSNs / national IDs, dates of birth.
- **Financial data:** credit card numbers (full or even partial), bank account numbers, full transaction histories.
- **Health data:** medical records, diagnoses, prescriptions — anywhere subject to HIPAA or equivalents.
- **Full request bodies / response bodies** of authenticated APIs — they often contain the above without you noticing.
- **URLs with sensitive query parameters** — auth tokens in URL query strings are a classic exposure (`?access_token=...` shows up in every access log).
- **Authorization headers** — bearer tokens, basic-auth credentials.

### Redaction is necessary but not sufficient

Most logging frameworks support rule-based string replacement (redact known patterns like `credit_card=...`) or field-level masking in structured logs. **Configure them**, but treat them as a backstop, not a primary defense:

- The redaction rule has to know about the field. New fields get added by other engineers; the rules don't update themselves.
- Pattern-based redaction is bypassed by encoding (base64-encoded token in a URL escapes the pattern).
- Custom protocol formats are invisible to generic redactors.

**The primary defense is at the call site:** don't log the thing in the first place. Log a sanitized identifier (`user_id=12345` not `email=alice@example.com`) and look up the rest in the database if needed during investigation.

### A note on log injection

User input that ends up in logs can itself be an attack vector — *log injection*. An attacker submits input containing newlines and forged log lines; the logging pipeline records the attack as if it were normal log output. See [`input-validation`](../input-validation/SKILL.md) for the input-side counterpart — escaping control characters before logging untrusted strings.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about levels, structure, performance, and security in one message.
- **Work on the user's actual code if shared.** Walk through level choices on their specific log lines.
- **Surface only the relevant section.** Most logging questions are about one of the four practices; identify which and skip the others.
- **Be specific about the redaction list.** "Don't log sensitive data" is a generality; *"don't log the `Authorization` header"* is actionable.
- **If the user is asking about an active incident**, route to [`incident-response`](../incident-response/SKILL.md) — they should be *reading* logs, not designing how to *write* them.

## When NOT to use this skill

- The user is asking about general defensive practices (not specifically logging) — route to [`defensive-programming`](../defensive-programming/SKILL.md).
- The user is asking about input handling and validation — route to [`input-validation`](../input-validation/SKILL.md), which also covers log-injection.
- The user is asking about the broader observability stack (metrics vs logs vs traces) — route to [`operator-playbook`](../operator-playbook/SKILL.md) for the comparative primer.
- The user is in an active incident — route to [`incident-response`](../incident-response/SKILL.md). Logs are a tool for that situation, not a topic to design during it.
- The user is reviewing a PR with logging changes — route to [`code-review`](../code-review/SKILL.md) with logging quality as the lens.
