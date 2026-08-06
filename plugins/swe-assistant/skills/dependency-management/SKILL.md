---
name: dependency-management
description: Use when the user is adding, updating, or managing third-party dependencies — picking a library, evaluating whether to use one at all, debugging version conflicts, dealing with transitive dependencies, or designing how their project pins and scopes what it depends on. Triggers include phrases like "should I add this library", "we have a version conflict", "transitive dependency", "dependency hell", "semver", "semantic versioning", "should I pin this version", "we have a circular dependency", "vendoring", "shading", "what's a good versioning scheme", "I keep getting build errors after updating X", "the package broke after a minor update", "should I write this myself or use a library", "lockfile", "dependency tree", or asking about license obligations from a dependency. Walks through the dependency discipline from The Missing Readme (Chapter 5) — semantic versioning, the decision to take a dependency at all, transitive dependencies, vendoring vs. shading, deliberate declaration, pinning, narrow scoping, and protecting against circular dependencies. Do not trigger for general runtime API design, code reviews, or active production incidents caused by a bad dependency update (route to incident-response).
---

# dependency-management

## Source

*The Missing Readme*, Chapter 5, "Managing Dependencies." **Semantic Versioning** is anchored by the spec at https://semver.org. Python's equivalent is **PEP 440** (https://www.python.org/dev/peps/pep-0440/).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (a clear dependency policy is something the rest of the team can reason about)
- **Builds:** Leadership (you set the norms others inherit)

## What this skill is for

Modern software is mostly other people's code. A few well-chosen libraries save weeks of work; a few poorly-chosen ones cost months in conflicts, security patches, and rewrites. The discipline isn't "use libraries" or "write everything yourself" — it's deciding well, declaring clearly, and pinning narrowly so the next change doesn't surprise you.

This skill fires when the user is making a dependency decision: should we take this on, how do we pin it, how do we keep version conflicts under control, how do we get out of dependency hell once we're in it.

## The core mindset (lead with this)

**Every dependency is a long-term commitment to someone else's code.**

- A dependency is free to add and expensive to remove. Treat the decision accordingly.
- The version you pin today is the version you'll have to upgrade tomorrow. Plan for the upgrade.
- Transitive dependencies are real dependencies. Your dependency's bugs are your bugs.
- "It works on my machine" usually means "I haven't pinned my versions."

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's project if shared, route to focused content the user needs.**

### Step 1 — Diagnose

Ask **one** question if it isn't already obvious from their first message:

- *"What's the situation — adding a new dependency, debugging a version conflict, or designing how your project handles pinning and scoping?"*

Three rough modes:

- **Adding** a new dependency → Step 2 (the decision).
- **Debugging** a conflict or transitive issue → Step 5 (transitive dependencies).
- **Designing policy** → Step 3 (versioning) plus Steps 6–9 (the discipline).

### Step 2 — Decide whether to take the dependency at all

Before adding anything, run the checklist. Weight these by how risky and central the dependency is; for a small leaf dependency a few of these matter, for a load-bearing one all of them do:

- **Do you really need the functionality?** Or are you reaching for a library out of habit?
- **How well maintained is it?** Recent commits, active issue triage, more than one maintainer, real release cadence — or one person who hasn't touched it in eighteen months?
- **How easy would it be for you to fix it if something went wrong?** Public source, readable code, license that allows forking.
- **How mature is it?** A 0.x library that's three months old has very different risk than a 5.x library that's eight years old.
- **How often does it break compatibility?** Look at the changelog. A library that bumps major versions every six months is a maintenance burden, not a labor saver.
- **How well does your team understand it?** Adopting a library no one on the team has used means everyone is on the learning curve.
- **How hard is the code to write yourself?** For a 50-line utility, often easier to write and own.
- **What's the license?** Permissive (MIT, Apache-2.0, BSD) is usually safe; copyleft (GPL, AGPL) has obligations; "no license" means you can't legally use it at all (see the license callout below).
- **What's the ratio of code you use vs. code you don't?** A 200KB dependency for one helper function is a bad trade.

If the answers don't add up, the right move is sometimes to **write the small thing yourself**. *Not Invented Here* is a real failure mode; *Anything But Here* is the other one.

### Step 3 — Understand versioning (SemVer)

If the user is publishing a library or picking version pins, they need to think in SemVer.

A good versioning scheme is:

- **Unique** — never reuse a version number. Never republish changed code under an existing version. *Ever.*
- **Comparable** — humans and tools should be able to reason about which version came first.
- **Informative** — it should communicate prerelease vs. release and convey stability and compatibility expectations.

**Semantic Versioning** (https://semver.org) — `MAJOR.MINOR.PATCH`:

- **PATCH** — incremented for backward-compatible bug fixes.
- **MINOR** — incremented for backward-compatible new features.
- **MAJOR** — incremented for backward-incompatible changes.
- **MAJOR 0** (`0.x.y`) — explicitly *prerelease*. Anything goes between minor versions; treat with extra care.

**Prereleases** are appended with `-`: `3.0.0-rc.1`, `2.0.0-beta.4`. Identifiers are dot-separated alphanumerics. Prereleases can break compatibility without bumping major. Release candidates (`rc.N`) are the conventional final-prerelease step.

**Build metadata** comes after `+`: `2.12.7-alpha.2+1942`. This lets you trace a deployed artifact back to a specific build log.

**Wildcards / ranges** (`2.13.*`, `^1.2.3`, `~1.2.3`) — accept a range of versions. Useful for libraries you publish; dangerous for applications you ship (see Step 7).

Python is similar but governed by **PEP 440** (https://www.python.org/dev/peps/pep-0440/), with its own syntax for prereleases (`1.0a1`, `1.0rc1`) and post-releases. The shape is familiar; the details differ. If the user is in the Python ecosystem, send them to PEP 440 rather than SemVer for the authoritative rules.

### Step 4 — Recognize transitive dependencies

Your direct dependencies have their own dependencies. **Any change in any of them can affect your program.**

Practical actions:

- **Learn your build tool's "dependency tree" command.** `npm ls`, `mvn dependency:tree`, `pipdeptree`, `cargo tree`, `go mod graph`. When something breaks after a dependency update, this is usually the first thing to look at.
- **Look at the lockfile.** `package-lock.json`, `poetry.lock`, `Pipfile.lock`, `Cargo.lock`, `go.sum`. The lockfile is the source of truth for what you're actually shipping.
- **Audit periodically.** `npm audit`, `pip-audit`, `cargo audit`, GitHub Dependabot, Snyk and similar tools surface known vulnerabilities in transitive dependencies.

When two of your dependencies need different versions of the same transitive dependency, that's a **version conflict**. Resolution depends on your ecosystem: npm allows multiple versions side-by-side, Maven uses nearest-wins, Python is strict and forces you to pick one. Knowing the rules of your package manager is part of the job.

### Step 5 — Isolate dependencies when it makes sense

Not all dependencies need to live in your package manager. Sometimes the right move is to **vendor** or **shade**:

- **Vendoring** — copy a small, stable dependency directly into your repository. Use tools designed for it (`git subtree`, `git-vendor`, Go's `vendor/` directory). Good for: small, stable code; protection against upstream disappearing; avoiding tooling churn. The trade-off is that you own the maintenance burden — security patches included.
- **Shading** — repackage a dependency under a renamed namespace so it doesn't collide with the same library at a different version pulled in by someone else's app. Mostly relevant when you're *publishing a library* that uses a widely-shared dependency (e.g., a logging or JSON library) and you don't want to force-version your consumers.

These tactics are pragmatic, not dogmatic. They violate DRY by design. Use them sparingly, document why, and revisit the decision when the situation changes.

### Step 6 — Deliberately add dependencies

**Explicitly declare every library you use.** Never rely on a transitive dependency leaking through to your code.

- If your code imports `lodash`, declare `lodash` in your manifest — even if it's coming in transitively via some other dependency today. If that other dependency drops lodash in its next release, your code breaks for a reason that has nothing to do with your change.
- Don't rely on the IDE to add dependencies invisibly. Declare them in the build file (`package.json`, `pom.xml`, `pyproject.toml`, `go.mod`, `Cargo.toml`).
- Code-review manifest changes the way you'd review any other code.

### Step 7 — Pin versions

**Explicitly set every dependency's version.** Floating versions are how the same code builds differently on different days.

- For **applications you deploy** → pin exact versions and commit the lockfile. The build today should match the build six months from now.
- For **libraries you publish** → use a bounded range (e.g., `^1.2.3` or `>=1.2.3,<2.0.0`) so your consumers can resolve conflicts. Never use unbounded ranges.
- **Commit the manifest and the lockfile alongside the rest of your code.** This makes dependency changes explicit in version control, where they can be reviewed, blamed, and reverted. A surprise change to a transitive dependency that lands in code review is much cheaper than the same change discovered in production.

### Step 8 — Scope dependencies narrowly

Dependencies have **scopes** — when they apply (compile-time, runtime, test-only, build-only, etc.). Use the narrowest possible scope:

- A test framework should be `test`-scoped, not `compile`.
- A code-generation tool should be `build`-scoped, not shipped at runtime.
- An optional integration should be optional, not required.

Narrow scoping shrinks runtime binaries, reduces attack surface, and avoids the *"this test library is now in my production image"* class of mistake.

### Step 9 — Protect against circular dependencies

**Never introduce a circular dependency** (A depends on B which depends on A, possibly via several hops). Circular dependencies prevent clean build ordering, make refactoring brittle, and signal a design problem.

- Your build tool may already detect them; enable the check.
- If it doesn't, look for a plugin or linter that does — `madge` for JavaScript, `import-linter` or `pylint` for Python, enforce rules in Maven/Gradle, `go vet` patterns for Go.
- If you discover one in existing code, treat it as a design red flag. Extract the shared concept into a third module that both can depend on.

### Step 10 — Close

Confirm the move: *"You're adding [dependency] because [reason], pinning to [version], scoping as [scope]; or you're handling the conflict by [strategy]."* The user should be able to summarize their dependency policy in one sentence.

---

## Callout — Dependency hell, in one paragraph

You add library A. Library A needs library X at version 1.x. A few months later you add library B. Library B needs library X at version 2.x, which is not backward-compatible with 1.x. Your package manager either refuses to install (strict resolvers — Python, Maven nearest-wins) or installs both and hopes (npm). Now you're either stuck on old A, stuck on old B, forking one of them, or rewriting your own code to drop one. **The cheapest way out of dependency hell is not to walk in.** Step 2's checklist is how.

---

## Callout — License hygiene

Licenses bind the code you ship. Get them wrong once and untangling can be expensive:

- **Permissive** (MIT, Apache-2.0, BSD, ISC) — generally safe for commercial use. Apache-2.0 has an explicit patent grant, which matters for some companies.
- **Copyleft** (GPL, AGPL, LGPL) — your code may need to be released under the same license if you distribute. AGPL extends this to network use, which catches many SaaS companies off guard.
- **Source-available / non-commercial** (BSL, SSPL, Commons Clause) — read carefully; some forbid building competing services.
- **No license at all** — you legally cannot use the code. "It's on GitHub" is not a license.

Most build systems can produce a license report (`license-checker` for npm, `pip-licenses` for Python, `cargo-license` for Rust). Run one before shipping. Surprises here become legal problems, not just engineering problems.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't run the full Step 2 checklist as one wall of questions; pick the most relevant two or three for the user's situation.
- **Work on the user's actual manifest if shared.** If they paste a `package.json` or `pyproject.toml`, walk through *their* dependencies.
- **Surface the package manager's specific tools** (`npm ls`, `mvn dependency:tree`, `pipdeptree`, `cargo tree`) rather than generic advice.
- **Don't lecture if they're already disciplined.** A senior engineer asking about shading doesn't need the SemVer primer.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is debugging an API design or runtime issue that's *caused by* a dependency but isn't really about dependency management. Skip; help with the underlying issue.
- The user has an active production incident triggered by a bad dependency update. Route to [`incident-response`](../incident-response/SKILL.md); roll back first, postmortem the dependency policy later.
- The user is reviewing a PR that happens to add a dependency. Route to [`code-review`](../code-review/SKILL.md) with dependency hygiene as the lens.
- The user is doing greenfield design and hasn't reached the dependency stage yet. Skip until they do.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- **Semantic Versioning** (https://semver.org) — the spec. Short, readable, worth knowing by heart.
- **PEP 440** (https://www.python.org/dev/peps/pep-0440/) — Python's version-specification standard. Differs from SemVer in details that matter for the Python ecosystem.
