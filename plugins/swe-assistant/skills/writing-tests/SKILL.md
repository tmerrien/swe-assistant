---
name: writing-tests
description: Use when the user is writing tests for code they own — deciding what to test, how much, how to keep tests clean and maintainable, which test type fits a situation, or thinking about coverage targets. Triggers include "how should I test this", "what should I test", "how much test coverage do I need", "TDD", or "the test framework is making me write too much boilerplate". Covers taking responsibility for testing your own code, the test-type taxonomy, writing clean tests with the same care as production code, not chasing coverage percentages, and using a risk matrix to focus effort. For mocking specifically, route to mocking. For flaky tests, route to test-determinism. Do not trigger for code reviews of test PRs.
---

# writing-tests

## Source

*The Missing Readme*, Chapter 6, "Testing." Test-driven development (TDD) is anchored by Kent Beck's *Test-Driven Development: By Example* (Addison-Wesley, 2002) and is widely-attested industry practice.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (tests document how code is meant to be used)
- **Builds:** Leadership (taking responsibility for the quality of what you ship)

## What this skill is for

A test suite is the safety net under every change you'll ever make to the code. It catches regressions, documents intent, and forces honest API design. The discipline isn't *"write all the tests"* — it's writing the tests that matter, treating them with the same care as production code, and resisting the pressure to chase coverage numbers instead of confidence.

This skill fires when the user is writing tests for code they own.

## The core mindset (lead with this)

**Tests exist to give you confidence that the code behaves as expected — and to keep that confidence as the code changes.**

- Tests aren't homework. They're how you go fast tomorrow without breaking yesterday.
- The team that writes the code is responsible for testing the code. *"QA will catch it"* is not a plan.
- Untested code is technical debt the moment it ships.
- A test that doesn't fail meaningfully isn't a test; it's a liability.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual code if shared, route to focused skills when they fit better.**

### Step 1 — Diagnose

Ask **one** question if it isn't already obvious:

- *"What are you testing — a new feature, a bug fix, or an existing piece of code that doesn't have coverage yet?"*

### Step 2 — Pick the right test type

The test type matches the question you want answered.

- **Unit** — small, fast, focused on one function or class. Run on every save. The bulk of any healthy test suite.
- **Integration** — slower, more setup; verify that components work together (the function with the database, the service with the queue). Run on every PR.
- **System / end-to-end** — full pipeline tests, sometimes against a real or near-real environment. Synthetic-monitoring scripts in production are this category. Run sparingly; they're expensive and flakier.
- **Performance** — load and stress tests for capacity planning and SLO definition. Run on demand or on a schedule, not on every PR.
- **Acceptance** — performed by (or representing) the customer. Validates that the feature does what was asked for. Often manual or scripted UI tests.

Most code needs unit + integration. System and performance are reserved for the surfaces where they earn their cost.

**Test-driven development (TDD)** — write the test first, then write the code that makes it pass. TDD forces you to think about behavior, interface, and integration before implementation. You don't need to adopt it religiously, but the discipline of writing a failing test before the code is a useful default, particularly for bug fixes (write the test that reproduces the bug *first*, then fix the bug).

### Step 3 — Write tests as code

Tests are code. They live in the codebase, they have to be read, they have to be maintained. Treat them accordingly:

- **Use good programming practices.** Naming, separation of concerns, no duplication, no hard-coded magic values.
- **Document what they test and why.** A short docstring per test pays for itself the first time someone else has to debug one.
- **Keep test dependencies separate from production dependencies.** Use your build system's test scope so the testing library doesn't ship to production. (See [`dependency-management`](../dependency-management/SKILL.md), Step 8.)
- **Test fundamental behavior, not implementation details.** A test that breaks when the *implementation* changes but the behavior doesn't is a test that gets deleted next time someone needs to refactor.

### Step 4 — Don't overdo it

Tests cost time to write and maintain. The goal is the highest-value coverage, not the highest coverage number.

- **Use a risk matrix.** Focus on the high-likelihood, high-impact areas first. Auth, payments, data integrity, anything that runs in a loop processing money or user data. Low-risk or throwaway code earns very few tests.
- **Coverage is a guide, not a rule.** 65–85% is a healthy band for most codebases. Above that you start spending more time on tests than they return; below it, you're flying blind.
- **Don't handcraft tests for generated code.** Web-framework scaffolding, OpenAPI clients, ORM glue — exclude them from coverage instead of writing meaningless tests against them. If you really need to test generated code, test the *generator*.
- **One big rule:** *you should not need to fix the tests when the code is not broken.* If a refactor that preserves behavior requires test changes, the tests were over-fitted to the implementation.

### Step 5 — Work with QA, if you have one

Some companies have a QA team that helps verify stability. Even when they exist, **never throw code over the fence.** Modern QA doesn't write your unit tests — they typically cover system-level, exploratory, and acceptance testing.

- If QA is **embedded in your team**, they're likely at standup and sprint planning. Loop them in early; the cheapest way to test something is to know what they'll test before you build it.
- If QA is **centralized**, find out the request process (ticket, form, sync) and the typical turnaround. Plan for it.

### Step 6 — A few tooling notes

- **Test framework.** Use your language's standard. Read the docs on setup/teardown carefully; teardown is *not* guaranteed to run on crashes. Running tests one at a time is safer; parallel is faster but invites shared-state bugs. Reports usually land in `target/`, `build/`, `test-results/`, or wherever your runner writes — if you can't find them, check the runner's docs.
- **Linters and style checkers.** Set them up in the IDE so style violations are flagged at write time, not at code-review time.
- **Code-coverage tools.** Useful for spotting untested high-risk code. Easily abused as a vanity metric. Configure them to ignore generated code, otherwise coverage looks worse than it is.
- **Static analysis / complexity tools.** Sudden spikes in cyclomatic complexity are a useful red flag. Individual high-complexity functions are usually worth refactoring before adding more behavior to them.

Every tool comes with overhead. Don't add a new test tool until the team is bought in and the complexity it adds is justified.

### Step 7 — Close

Confirm the move: *"You're writing [unit / integration / etc.] tests for [the new code], focused on [the behaviors that matter most], at [reasonable coverage]."* The user should have a concrete plan, not a coverage target.

---

## Callout — A test that doesn't fail meaningfully is a liability

If a test cannot tell you something useful when it fails, it's net negative — it costs maintenance and gives false confidence. Two common shapes of meaningless tests:

- **The tautology.** `assertEquals(getName(), getName())` — passes by construction. Almost always reachable by deletion.
- **The implementation-shape test.** Asserts the function called helper A, then helper B, then helper C. Breaks the moment someone refactors the implementation, even when the behavior is unchanged.

The fix in both cases is to step back and ask: *"What user-visible (or caller-visible) behavior would I want a regression alarm on?"* Then write that.

---

## Callout — Pragmatism on legacy quality-tool warnings

Just because a tool finds a quality issue doesn't mean it's actually a problem, or that it's worth fixing immediately. With a codebase that fails a fresh round of quality checks: **don't let it get worse, but avoid a disruptive stop-the-world cleanup project.** Use [`technical-debt`](../technical-debt/SKILL.md) to prioritize what to pay down and what to live with.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't dump all six steps as one wall of text; surface the ones that fit the user's situation.
- **Work on the user's actual code or test file if shared.** Walk through Step 3's clean-tests checks on *their* code.
- **Don't push TDD as ideology.** Surface it as a useful default; respect the user's choice if they prefer write-after.
- **Surface coverage advice carefully.** *"You should aim for 80%"* is the kind of advice that creates the problem this skill is designed to prevent. Surface the *risk matrix* framing instead.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking how to mock something specifically. Route to [`mocking`](../mocking/SKILL.md).
- The user has a flaky / intermittently failing test. Route to [`test-determinism`](../test-determinism/SKILL.md).
- The user is reviewing a test PR rather than writing one. Route to [`code-review`](../code-review/SKILL.md).
- The user is asking about testing strategy at the architecture / org level. Out of scope for this skill.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- *Test-Driven Development: By Example* — Kent Beck (Addison-Wesley, 2002). The canonical TDD text; intended to be worked through, not just read.
- *Unit Testing: Principles, Practices, and Patterns* — Vladimir Khorikov (Manning, 2020). Modern, opinionated; rigorous on the difference between testing behavior and testing implementation, and on the *"mock everything"* anti-pattern.
- *The Pragmatic Programmer* — Andrew Hunt & David Thomas (20th Anniversary Edition, Addison-Wesley 2019). Cross-cutting practitioner classic; source of *"DRY,"* *"broken windows,"* *"tracer bullets,"* and a substantial modern testing chapter.
- *Explore It!* — Elisabeth Hendrickson (Pragmatic Bookshelf, 2013). The complement to automated testing: structured exploratory testing for finding what your test suite missed.
- *Working Effectively with Unit Tests* — Jay Fields (Leanpub, 2014). Pragmatic, modern, opinionated.
- *xUnit Test Patterns: Refactoring Test Code* — Gerard Meszaros (Addison-Wesley, 2007). The pattern-language reference for test design and the bad-smells that wreck test suites.
