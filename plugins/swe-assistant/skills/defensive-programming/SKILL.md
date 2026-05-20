---
name: defensive-programming
description: Use when the user is writing new code (or hardening existing code) and wants to make it safer, more robust, or more resilient — but is not in a specifically tactical situation covered by a more focused skill. Triggers include phrases like "how do I make this function more robust", "what defensive practices apply here", "I want to harden this code", "what can go wrong with this", "what should I check for", "make this code safer", "how do I prevent bugs in this", "should I add null checks here", "should I use exceptions or return values", "what's the right way to handle errors here", or asking generally about defensive coding practices. Walks through foundational practices from The Missing Readme (Chapter 4) — null safety and the null-object/option-type patterns, variable immutability, type hinting and static type checking, exception design (use them, be precise, throw early and catch late), and resource cleanup. For external input handling specifically, route to input-validation. For retry logic on remote calls, route to retry-and-backoff. For designing retry-safe operations, route to idempotency. Do not trigger for code reviews (route to code-review) or for incident situations.
---

# defensive-programming

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Defensive Programming). This skill is the umbrella for foundational defensive practices; three focused spin-outs handle higher-stakes specific situations:

- [`input-validation`](../input-validation/SKILL.md) — when handling user, network, or external input (security-critical).
- [`retry-and-backoff`](../retry-and-backoff/SKILL.md) — when writing retry logic for remote calls.
- [`idempotency`](../idempotency/SKILL.md) — when designing operations for safe retry.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (defensive code is more readable for the next engineer)
- **Builds:** Leadership (modeling careful work raises the team's bar)

## What this skill is for

Defensive programming is the everyday discipline that prevents most production failures. The 2am incident often started weeks earlier with a missed null check, an unhandled exception, or a mutable variable touched from two threads. This skill fires when the user is writing or hardening code and wants to apply the foundational defensive practices — but is not in a specifically tactical situation that one of the spin-outs handles better.

## The core mindset (lead with this)

**Fail fast and loudly. Then fail gracefully where it matters.**

- **Catch failures at the boundary**, not after they've propagated. The cheaper an error is to find, the cheaper it is to fix.
- **Let the language and tools help.** Compile-time checks beat runtime checks. Static types beat dynamic surprises. Immutable variables can't be wrong.
- **Code is read more than it is written.** Defensive practices that make assumptions explicit help every future reader, including future-you at 2am.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, accept brief responses as complete, work on the draft if there is one.**

### Step 1 — Diagnose

If the user has a specific function/piece of code in mind, work on *that* — don't lecture them through the general principles. Ask **one** question if you need clarification:

- *"What are you writing or hardening — can you share the code or describe the function?"* (if not already shown)
- *"What kind of input does this take, and where does it come from?"* (if scope is unclear)

Skip the diagnostic entirely if the user already showed you the code.

### Step 2 — Route if a spin-out fits better

Before applying the general defensive practices, check if a focused skill is the right answer:

- Handling external input (user input, network payload, file upload, request body) → [`input-validation`](../input-validation/SKILL.md).
- Writing retry logic for a remote call → [`retry-and-backoff`](../retry-and-backoff/SKILL.md).
- Designing an operation that may be retried (API endpoint, message handler) → [`idempotency`](../idempotency/SKILL.md).
- Reviewing someone else's code → [`code-review`](../code-review/SKILL.md).

If the user is in a more general "make this safer" situation, continue.

### Step 3 — Surface 2–4 relevant practices

Pick the practices that fit the user's code, not the full menu. Common combinations:

- **A new function taking arguments** → null safety + type hinting + input validation pointers.
- **A long-lived function modifying state** → immutability + exception precision.
- **A function calling external resources** → exception design + resource cleanup + (route to retry).
- **A class or module being designed** → immutability + access modifiers + static types.

### Step 4 — Pick one concrete change

Ask the user to commit to one concrete improvement first, not a wholesale refactor. *"Of these, which one would you add first?"*

### Step 5 — Close

One sentence. Confirm the change, mention any focused skill the user might want next.

---

## The practices (reference material — surface as needed)

### Null safety

Null pointer exceptions are one of the most common bug sources in any language that allows nulls. Three complementary tools:

- **Check that variables aren't null** at the boundaries — at the start of methods that take potentially-nullable arguments. Reject the null at the door rather than carrying it into the function body.
- **Use the null object pattern** — return a meaningful no-op object instead of null when "nothing here" is a normal case. Callers don't have to special-case null.
- **Use option/maybe types** when the language provides them (Rust's `Option`, Kotlin's `?`, Java's `Optional`, Python's typing `Optional`). The type system forces callers to handle the absent case explicitly.

If your language supports `@NotNull` / `NonNull` annotations or nullability markers, use them. They turn "I assumed this wouldn't be null" into a compile-time check.

### Variable immutability

Whenever a variable doesn't need to change, declare it immutable (`const`, `final`, `val`, etc.).

- Prevents accidental modification by code far from the declaration.
- Makes parallel/concurrent code much easier to reason about — immutable variables can't be involved in a data race.
- Allows the compiler or runtime to make optimizations it can't make for mutable variables.

The default should be immutable; reach for mutable only when there's a reason.

### Type hinting and static type checking

Constrain the values your variables can take.

- **Use the most specific type possible.** If a variable can only hold three string values, make it an enum, not a string. The compiler then catches typos.
- **Use type hints even in dynamic languages.** Python `typing`, TypeScript, mypy, Pyright — they make assumptions explicit and catch a real class of bugs before runtime.
- **Type hinting can be added gradually.** You don't have to type-annotate the whole codebase at once. Start with new code and high-risk areas.

### Use exceptions (not magic return values)

Modern languages support exceptions. Use them.

- **Don't signal errors with sentinel return values** (`-1`, `null`, empty string). These get ignored by callers and become silent bugs.
- **Don't use return-tuples-with-error-codes** in languages where exceptions are idiomatic. They put the burden on every caller to remember the check.
- The exception is languages like Go where multi-return error handling is idiomatic — follow the language convention.

### Be precise with exceptions

Exception design is the most under-practiced part of the practice.

- **Use built-in exceptions when possible.** `ValueError`, `IllegalArgumentException`, `IOException`, etc. — they already exist and callers already know how to handle them.
- **Don't create custom exceptions if a built-in describes the problem.** Custom exception type proliferation is its own pain.
- **When you do create custom exceptions, be specific.** `PaymentDeclinedException` is useful; `BusinessException` is not. The whole point is for the catcher to know what happened.
- **Don't use exceptions for application logic.** Exceptions are for failures, not for control flow. Code should be *unsurprising*, not *clever*. Using exceptions to break out of a loop is confusing.

### Throw exceptions early, catch them late

- **Throw early.** Raise the exception as close to where the error was detected as possible. The stack trace then points at the actual problem instead of some downstream symptom.
- **Catch late.** Let the exception propagate up the call stack until you reach the layer that's actually capable of handling it. Catching too early often means swallowing the error or losing context.

### Clean up resources

Every resource you open — file, network socket, database connection, memory allocation — must be released, even when an exception occurs.

- **Use the language's automatic resource management** when available:
  - Python: `with` statement (context managers).
  - Java: `try-with-resources`.
  - C#: `using` statement.
  - C++: RAII (Resource Acquisition Is Initialization).
  - Go: `defer`.
- **For languages without automatic cleanup** (raw C, some embedded), use `try/finally` patterns and discipline.
- **Resource leaks compound.** A leak that's invisible during testing becomes a production outage after 10,000 requests.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask the user to choose from a menu of practices in a single message; ask, listen, then suggest.
- **Work on the user's actual code if they share it.** Don't lecture on principles when there's a draft to improve.
- **Surface 2–4 practices that fit their code**, not the full ten. The umbrella is reference; the conversation is focused.
- **Route to spin-outs decisively.** If their question is really about input validation, retry logic, or idempotency, hand it off in your first or second message — don't try to cover everything yourself.
- **Match the user's experience level.** A senior asking "should I add null checks here" likely wants a yes/no with reasoning, not a tutorial on null safety.

## When NOT to use this skill

- The user is handling external input — route to [`input-validation`](../input-validation/SKILL.md).
- The user is writing retry logic — route to [`retry-and-backoff`](../retry-and-backoff/SKILL.md).
- The user is designing a retry-safe operation — route to [`idempotency`](../idempotency/SKILL.md).
- The user is reviewing a PR — route to [`code-review`](../code-review/SKILL.md).
- The user is in an active incident — route to [`incident-response`](../incident-response/SKILL.md). Defensive-programming conversations are for the calm-afternoon work that prevents incidents, not the firefighting that responds to them.
- The user has a specific syntax/API question. Help directly.
