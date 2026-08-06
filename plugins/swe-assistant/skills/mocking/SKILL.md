---
name: mocking
description: Use when the user is deciding whether or how to mock a dependency in a test — reaching for a mocking framework, debating real vs. fake collaborators, writing or refactoring mocks, or noticing that their mocks have become complicated enough to be their own kind of bug source. Triggers include phrases like "should I mock this", "how do I mock X", "mocking framework", "mock object", "fake vs mock", "stub vs mock", "my mocks are getting complex", "this test has too many mocks", or asking which mocking library to use. Walks through the mocking discipline from The Missing Readme (Chapter 6) — start with inline mocks, don't write a shared mock class until you repeat logic, treat excessive mocking as a code-coupling smell, prefer refactoring to separate I/O from computation. For broader test-writing questions, route to writing-tests. For flaky tests caused by mocks-that-don't-behave, route to test-determinism. Do not trigger for code reviews or for general dependency-injection design.
---

# mocking

## Source

*The Missing Readme*, Chapter 6, "Testing" (Section: Test Tools, subsection on mocking libraries). The *"mocks are a coupling smell"* framing is widely-attested industry practice; see also Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests*.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (a clean test boundary is easier for the next person to read)

## What this skill is for

Mocks let you isolate the code under test by replacing its collaborators with controlled fakes. Used well, they make tests fast, focused, and deterministic. Used badly, they produce test suites where every change to production code breaks twenty unrelated tests — and where bugs hide because the mock doesn't behave like the real thing.

This skill fires when the user is about to reach for a mock — or when they've already reached for too many.

## The core mindset (lead with this)

**Mocks are useful, but heavy reliance on mocks is a code smell — it usually means the code under test is too tightly coupled to its collaborators.**

- A mock is the test admitting it can't easily exercise the real collaborator. That's sometimes unavoidable. It's also sometimes a hint to refactor.
- Every mock encodes an assumption about how the real thing behaves. When the real thing changes, the mock silently lies.
- The cheapest mock is the one you didn't need to write.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn.**

### Step 1 — Diagnose

Ask **one** question if it isn't obvious:

- *"What are you mocking and why — is the real thing slow, networked, hard to set up, or are you trying to control its behavior for a specific test case?"*

### Step 2 — Consider not mocking at all

Before reaching for a mocking library, check whether you can:

- **Use the real thing.** If the dependency is fast and pure (a hash function, a formatter, an in-memory data structure), just use it. Mocking adds nothing.
- **Use a real but in-memory variant.** An in-memory database (SQLite `:memory:`, H2, embedded Postgres), a tmpfs filesystem, an in-process queue. Often faster than a mock and *correct by construction.*
- **Refactor to remove the dependency.** Separate the pure computation from the I/O. If you can split *"figure out what to do"* from *"do it"*, the pure half is trivially testable without any mocks.

If none of those apply, then mock.

### Step 3 — Start with the simplest mock that works

In order of complexity, with a strong bias toward the top:

- **Inline mock in the test.** A small object or lambda that returns the values this one test needs. Zero shared infrastructure, zero risk of cross-test interference.
- **A test-specific fake** — a tiny implementation of the interface that supports just the cases the test family needs. Often a 20-line class.
- **A library-provided mock** (Mockito, unittest.mock, Sinon, gomock, mockall, etc.) — useful when you need rich interaction verification (*"was this method called with these arguments, this many times?"*).
- **A shared mock class** — only when you're literally repeating the same mocking logic across many tests.

**Don't write a shared mock until you've copied the same mock setup three times.** Premature shared mocks become their own little APIs that have to be maintained and that hide test intent behind indirection.

### Step 4 — Read the smell

If you're reaching for many mocks to test one piece of code, the code under test is probably too coupled to its collaborators. Common refactors:

- **Inject dependencies** so the test can pass in a simple stand-in instead of constructing the full collaborator graph.
- **Split I/O from logic.** A function that fetches from the database, transforms the result, and writes back is three functions. Test the transformation pure; test the I/O against in-memory variants; the orchestration is then a thin top-level function that needs barely any testing.
- **Introduce a narrow interface** at the seam. The production code depends only on the interface; tests substitute simple fakes. (See [`changing-legacy-code`](../changing-legacy-code/SKILL.md), Step 3 — same technique.)

### Step 5 — Keep mocks honest

A mock is a stand-in. When the real thing changes, the mock can silently disagree, and tests pass against a fiction.

- **Avoid mocking types you don't own.** Mocking external libraries' classes is particularly risky — when they update, your mock encodes an old contract. Where possible, wrap the external library in a thin interface *you own* and mock the wrapper.
- **Use contract tests for important seams.** A small test that runs against both the real collaborator and the mock, asserting they agree on the cases that matter, catches drift.
- **When in doubt, prefer the real thing or an in-memory variant.**

### Step 6 — Close

Confirm the move: *"You're using [inline mock / library mock / in-memory variant] because [the real thing is slow / networked / hard to control], and you've considered whether refactoring would let you skip the mock entirely."*

---

## Callout — Mocks as a coupling thermometer

A useful diagnostic: *count the mocks in a single test.* If you need to mock five things to exercise one function, the function is doing too much, or it's wired too tightly to its collaborators. The mocks aren't the problem; they're the symptom.

The fix is rarely *"better mocking"*. The fix is usually *"smaller, more focused functions with fewer collaborators each."*

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Work on the user's actual test if shared.** Walk through Step 2 (alternatives to mocking) on their specific situation.
- **Don't moralize about mocks.** They're a useful tool. The skill is when to reach for them and when not to.
- **Surface the refactor option when mocks pile up.** That's the highest-leverage move, even if it's the slowest.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is writing general tests, not specifically dealing with mocks. Route to [`writing-tests`](../writing-tests/SKILL.md).
- The user's mock-related test is flaky. Route to [`test-determinism`](../test-determinism/SKILL.md) — the mock may be hiding non-determinism.
- The user is reviewing a PR. Route to [`code-review`](../code-review/SKILL.md) with mocks as the lens.
- The user is designing a dependency-injection framework or testing strategy at the architecture level. Out of scope.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- *Unit Testing: Principles, Practices, and Patterns* — Vladimir Khorikov (Manning, 2020). One of the most rigorous treatments of test doubles in the field; argues hard for sociable tests over heavily-mocked solitary tests.
- *Growing Object-Oriented Software, Guided by Tests* — Steve Freeman & Nat Pryce (Addison-Wesley, 2009). The book that popularized *"mocking is design feedback."*
- *xUnit Test Patterns: Refactoring Test Code* — Gerard Meszaros (Addison-Wesley, 2007). The "Test Double" terminology (stub, mock, fake, spy, dummy) and the patterns and anti-patterns around each.
