---
name: test-determinism
description: Use when the user has a flaky test (passes sometimes, fails sometimes) or is writing a test that touches sources of non-determinism — time, randomness, the network, the filesystem, sockets/ports, shared state, or test order. Triggers include phrases like "my test is flaky", "intermittent failure", "the test passes locally but fails in CI", "I get random failures", "flaky test", "non-deterministic test", "the test fails when I run them in parallel", "tests depend on order", "should I use sleep in my test", "how do I test time-dependent code", "I'm using time.now in my test", "the test leaves files behind", "port already in use in test", "tests don't clean up after themselves", "intermittent CI failures", "rerun until green", or asking how to make a test reliable. Walks through the determinism discipline from The Missing Readme (Chapter 6, Determinism in Tests) — disable or fix flakies immediately, reproduce by looping, inject clocks for time, avoid sleeps and timeouts, close resources with try-with-resources / with-blocks, bind to port zero, generate unique paths, isolate and clean up state, and never depend on test order. For general test-writing or coverage questions, route to writing-tests. For mocking-specific questions, route to mocking. Do not trigger for active production incidents (route to incident-response).
---

# test-determinism

## Source

*The Missing Readme*, Chapter 6, "Testing" (Section: Determinism in Tests). The *"inject the clock"* and *"port zero"* patterns are widely-attested industry practice with their roots in *xUnit Test Patterns* (Meszaros, Addison-Wesley 2007).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (flaky tests teach the team to ignore the build, which is contagious)
- **Builds:** Leadership (the engineer who tracks down the flake protects everyone)

## What this skill is for

A flaky test — one that passes some runs and fails others — is one of the most damaging things in a codebase. It teaches the team to ignore red builds, which means the day a real bug breaks the build, no one notices. Fix flakies fast, and write new tests so they don't become flakies.

This skill fires when the user has a flaky test, or is about to write code that risks producing one.

## The core mindset (lead with this)

**Intermittently failing tests must be disabled or fixed immediately.**

- A flaky test is worse than no test. A test you can't trust trains the team to ignore failures.
- Most flakiness has the same handful of causes: time, randomness, the network, shared state, leftover files/sockets/processes, or test order. The fixes are well-known.
- *"Re-run and hope"* is not triage. If a test is flaky, it stays flaky until you eliminate the non-determinism or accept it isn't a test.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn.**

### Step 1 — Diagnose

Ask **one** question if it isn't obvious:

- *"What does the flaky test do, and what's the failure mode when it fails — timeout, assertion mismatch, resource error, something else?"*

### Step 2 — Reproduce it

A flake you can't reproduce, you can't fix. Run the test in a loop until it fails:

```bash
# Bash one-liner — replace with your test runner
for i in $(seq 1 200); do ./run_test.sh "$TEST_NAME" || break; done
```

Most IDEs also have a *"run until failure"* option. If the failure shows up in 1 of 50 runs locally, you have a reproducer. If it shows up only on CI, run the loop on CI too — CI machines are usually slower and more contended, which makes some flakes only visible there.

If you can reproduce, you can fix. If you genuinely cannot reproduce after sustained effort, **disable the test** (with a tracking issue) rather than letting it keep eroding trust.

### Step 3 — Walk down the usual suspects

Most flakes are one of these. Surface the most likely first based on the test's symptom.

#### Time

- Code reads the system clock; the assertion compares against a value the test computed earlier. The two clocks drift across the test run.
- **Fix: inject the clock.** Make the production code take a `Clock` (or equivalent) as a parameter instead of calling `time.now()` / `System.currentTimeMillis()` / `DateTime.UtcNow` directly. Tests pass in a fixed or controllable clock.

#### Randomness

- Code uses an RNG; the test happens to fail on a specific seed.
- **Fix: seed the RNG in tests, or inject the RNG.** Same pattern as the clock.

#### Sleeps and timeouts

- The test sleeps *"long enough"* for an async operation to complete. On a loaded CI machine, *"long enough"* isn't.
- **Fix: don't sleep.** Wait for a signal — a callback, a state change, an event, a future, a polling check with a generous timeout. If you genuinely can't, increase the timeout and document why, but treat the sleep as a smell.

#### Network calls

- The test calls a remote service that has its own variance — timeouts, transient errors, rate limits, DNS hiccups.
- **Fix: don't call the network from unit tests.** Mock the network call (see [`mocking`](../mocking/SKILL.md)), or refactor so the network-touching code is its own thin layer that integration tests exercise.

#### Shared state between tests

- One test mutates a global, a singleton, a database row, or a file. The next test sees the mutation.
- **Fix: isolate.** Use setup/teardown to reset state. Use containers or fresh test databases per run. Treat global mutable state as a test-suite bug, not a quirk to work around.

#### Resource leaks

- Sockets, file handles, database connections, threads, processes left open between tests. Eventually you run out of resources or hit *"port already in use."*
- **Fix: use language-native resource management.** `try-with-resources` (Java), `with` blocks (Python), `using` (C#), `defer` (Go), RAII (C++/Rust). For resources shared across tests, close them in suite-level teardown.

#### Port collisions

- Tests bind to a hard-coded port. Run two tests in parallel and one fails with *"address already in use."*
- **Fix: bind to port zero.** The OS picks a free port. Read the actual port back after binding and use it for the rest of the test.

#### File / database path collisions

- Tests write to a hard-coded path. Parallel runs collide; sequential runs see leftover data.
- **Fix: generate unique paths per test** (temp-directory APIs, UUID suffixes). Clean them up in teardown.

#### Test order dependence

- Test B passes only if Test A ran first (because Test A left state Test B reads).
- **Fix: each test sets up its own world.** Run tests in random order in CI to catch this early.

### Step 4 — Clean up no matter what

Cleanup must happen whether the test passed or failed:

- Use language-native finalization (`try/finally`, `with`, `defer`, fixtures with teardown).
- Resources shared across the whole suite get closed in suite-level teardown.
- **Do not** rely on the test's happy path to clean up — failed tests leave the most debris.

For test machines that accumulate cruft over many runs, **rebuild the environment** between suite runs. Containers or VM snapshots make this cheap; they're slower than setup/teardown but bullet-proof.

### Step 5 — Close

Confirm: *"You eliminated the non-determinism by [injecting the clock / binding port zero / cleaning up in teardown / etc.]. Run the loop again to confirm it stays green across 200+ runs."*

If you couldn't fix it, **disable the test with a tracking issue** rather than letting it stay flaky. A red build everyone ignores is worse than a missing test.

---

## Callout — Why flakies are corrosive

A flaky test doesn't just waste the time of the engineer who has to re-run it. It changes the team's relationship with the build. *"Just re-run, it's probably flaky"* becomes the response to every red build — including the ones that flagged a real bug.

Teams with disciplined determinism trust their build. Teams without it learn to ignore it. The cost of one untreated flake is small. The cost of the cultural shift it produces is enormous.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't run through all eight suspects at once; pick the most likely two or three for the user's symptom.
- **Work on the user's actual test if shared.** Walk Step 3 on *their* code.
- **Make reproduction the first ask.** A flake you can't reproduce can't be debugged.
- **Surface disabling as a legitimate option** when the fix isn't feasible right now — better than a red build everyone ignores.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is writing tests for the first time on a new feature with no specific flakiness concern. Route to [`writing-tests`](../writing-tests/SKILL.md).
- The user is asking about mocking specifically. Route to [`mocking`](../mocking/SKILL.md) (but note that a misbehaving mock is a common cause of flakes).
- The user is in an active production incident. Route to [`incident-response`](../incident-response/SKILL.md).
- The user is reviewing a PR. Route to [`code-review`](../code-review/SKILL.md).

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- *Unit Testing: Principles, Practices, and Patterns* — Vladimir Khorikov (Manning, 2020). Includes substantial material on test isolation, what makes a "good" unit test, and how integration tests should differ.
- *xUnit Test Patterns: Refactoring Test Code* — Gerard Meszaros (Addison-Wesley, 2007). The patterns ("Inject the Dependency," "Test Resource," "Lonely Test") that this skill applies. Also the canonical naming for the anti-patterns flakies usually are.
- *Working Effectively with Unit Tests* — Jay Fields (Leanpub, 2014). Pragmatic modern guidance, including substantial coverage of test isolation and cleanup discipline.
