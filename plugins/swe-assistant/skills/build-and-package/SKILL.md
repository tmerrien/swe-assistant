---
name: build-and-package
description: Use when the user is setting up, evaluating, or debugging a build pipeline, or deciding how their software is packaged for release. Triggers include phrases like "how should our build work", "my build isn't reproducible", "different devs get different builds", "what goes in this package", "should we version these together", "how should we split our packages", "our JAR is huge", "JAR vs wheel vs crate", "meta-package", "installer vs library packaging", "should tests run in CI", or "how do I package this for release". Walks through the build phase from The Missing Readme (Chapter 8) — the five-step build pipeline (resolve deps, lint, compile, test, package), packaging discipline (contents, formats, versioning, splitting by resource type, meta-packages), and CI hygiene. For choosing libraries or version conflicts, route to dependency-management. For test authoring or flakiness, route to writing-tests or test-determinism. For publishing, deploying, or rolling out built packages, route to operator-playbook.
---

# build-and-package

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 8, "Delivering Software"** — the **Build** section. The five-step framing (resolve dependencies → lint → compile → test → package), the treatment of packaging as the build's real deliverable, and the discipline of splitting packages by resource type all come from here.

The CI hygiene material (green trunk, fast feedback, test-in-CI as non-negotiable) is widely-attested industry practice; the canonical treatment is Humble & Farley's *Continuous Delivery* (surfaced in this repository's [`READING-LIST.md`](../../../../READING-LIST.md), status: *to read*).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (a package that's easy to reason about is easier for the rest of the team to consume)
- **Builds:** Leadership (build discipline is one of the norms a senior engineer sets)

## What this skill is for

The build phase turns source code into something a machine other than the developer's laptop can actually run. Its output — the **package** — is what everything downstream (release, deploy, rollout) operates on. Sloppy builds and sloppy packages produce sloppy operations: mysterious failures on prod that don't happen locally, releases that can't be rolled back cleanly, half-shipped applications, and debug sessions that start with *"which version is this even running?"*.

This skill fires when the user is designing the build, changing how packages are structured, or debugging a build that's producing surprising results. It does not fire once the package is built and the question shifts to how it gets to users — that's the release/deploy/rollout territory.

## The core mindset (lead with this)

**The build's real deliverable is the package. Everything else is means to that end.**

- If the package is sloppy, the deploy will be sloppy, and the debug will be sloppy. Get the package right and a lot of downstream pain evaporates.
- The same source, built twice, should produce the same package. If it doesn't, you don't have a build — you have a lottery.
- Packages are versioned artifacts, not "the current state of `main`." Every package has a name, a version, and a checksum.
- Splitting one big package into several smaller ones is almost always cheaper than merging several small packages back into one.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's project if shared, skip diagnosis if the first message already tells you what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that the build's job is to produce a package that downstream steps can rely on. Skip if the user already has a specific question queued up.

### Step 2 — Diagnose (one question, only if needed)

Rough shapes the situation usually takes:

- **Designing** a new build pipeline or migrating tools (Bazel/Maven/Gradle/npm/poetry/cargo/Make).
- **Debugging** — the build works on one machine and not another, or produces different outputs on different runs.
- **Packaging decisions** — what goes in the package, one package or several, how to version, library vs. application.
- **CI hygiene** — the build is slow, or the team keeps merging red, or tests aren't running where they should.

If the message is ambiguous, ask **one** question — for example: *"What's the situation — designing the pipeline, debugging a build, deciding how to package, or tightening CI?"* Do not deliver this as a menu; use it as your read on what to surface next.

### Step 3 — The five-step build pipeline

If the user doesn't already have this mental model, offer it once:

1. **Resolve and link dependencies.** Every declared dependency (and its transitive closure) is fetched, version-resolved, and made available to the compiler. If this step is not deterministic — no lockfile, floating versions — nothing downstream can be. Route depth here to [`dependency-management`](../dependency-management/SKILL.md).
2. **Lint.** Static checks catch style, obvious bugs, and unsafe patterns before compilation. Cheap; run first so failures surface fast.
3. **Compile.** Source becomes runnable form (bytecode, native binary, minified/bundled JS, whatever your ecosystem calls it).
4. **Test.** Automated tests run against the compiled output. If tests are skipped in the build, they will be skipped in reality. See [`writing-tests`](../writing-tests/SKILL.md) and [`test-determinism`](../test-determinism/SKILL.md).
5. **Package.** The tested, compiled artifact — plus everything it needs to run — is bundled into a versioned, checksummed unit. This is the build's actual deliverable.

Each step earns its place by failing loudly and early. A build that only compiles is not a build; it's the first step of one.

### Step 4 — Packaging discipline

If the user is at the "what goes in this package" question, surface the two callouts below (*Callout — What's actually in a package* and *Callout — Split packages by resource type*). Pull the specific parts they need; don't dump both if only one applies.

The three moves that matter most:

- **Version every package.** Assign a unique identifier. Reuse of a version number is a category error — a versioned package that can change is no better than an unversioned one. **Semantic versioning** is the default. Details in [`dependency-management`](../dependency-management/SKILL.md).
- **Split packages by resource type.** Code, config, translations, docs, and media should be separate packages if they have separate lifecycles. Then any one of them can roll forward or back without dragging the others along.
- **Meta-packages** (packages of packages) are the way to ship a single "complete application" while preserving the separation. Useful when a customer wants one thing to install; internal services rarely need them.

### Step 5 — CI hygiene

If the user is asking about CI, keep it short — the depth belongs in a dedicated skill later. The non-negotiables:

- **The build runs on every commit.** Not on demand, not overnight — every commit. If a commit doesn't build, the team should know within minutes.
- **The tests run in the build.** A test that doesn't run in CI is a test that doesn't exist. Route flakiness questions to [`test-determinism`](../test-determinism/SKILL.md).
- **Trunk stays green.** Do not merge on top of a red build. The person whose commit turned trunk red owns fixing or reverting it.
- **Feedback is fast.** A build that takes an hour is a build people learn to work around. Split, parallelize, or cache until it's under ten minutes for the common path.

### Step 6 — Pick one action

Ask: *"What's the one thing you'll change this week?"* Push for concreteness. *"Make the build reproducible"* is too vague. *"Add a lockfile commit check to CI by Friday and delete the two floating dependency ranges in `pyproject.toml`"* is the action.

### Step 7 — Close

One or two sentences. Confirm the move. Offer to come back for the next specific question. If the next question is "how do I actually release this thing," name that release/deploy/rollout are separate skills (the release skill for publishing, [`operator-playbook`](../operator-playbook/SKILL.md) for the wider delivery pipeline framing until dedicated skills exist).

---

## Callout — What's actually in a package

A package is not just "the compiled code." Depending on what you're shipping, it can hold any combination of:

- **Binary or source code** — the thing that runs.
- **Dependencies** — either bundled in (common for applications) or expected to be resolved at install time (common for libraries).
- **Config files** — defaults, schemas, sometimes environment-specific overrides.
- **Release notes and changelogs** — so operators can figure out what changed.
- **Documentation** — READMEs, man pages, API references.
- **Media** — images, sounds, fonts, model weights.
- **Licenses** — required for many third-party dependencies; also required for your own code if others will run it.
- **Checksums or signatures** — so downstream systems can verify integrity.
- **Virtual machine or container images** — for anything that ships an entire runtime environment.

**Library packages** usually look like: JARs (Java), wheels (Python), crates (Rust), gems (Ruby), npm tarballs (JavaScript). Zipped archives with a manifest.

**Application packages** look like: OS-native installers (`.dmg`, `.msi`, `.deb`, `.rpm`, `setup.exe`), container images, or plain tarballs/zips for services that will be unpacked by an orchestrator.

The right choice is the one the downstream consumer already knows how to install. A `.deb` is worse than a tarball if your users don't run Debian.

---

## Callout — Split packages by resource type

The single most useful packaging discipline: **package different resource types separately so each can change on its own schedule.**

- **Code** changes when the software changes. Slow-ish cadence, tied to releases.
- **Config** changes far more often — new environments, tuning, feature-flag defaults. If it's in the same package as code, every config tweak requires a rebuild.
- **Translations / localization** change on a different clock again — usually when strings are added or a new locale ships.
- **Documentation** and **media assets** change independently of both.

Consequences of getting this right:

- A translation fix ships without rebuilding the app.
- A bad config change rolls back without touching the code.
- A hotfix to code doesn't ship stale translations.

For a shipped-to-customer application, you can still bundle everything into a **meta-package** (a package of packages) so the install experience is one artifact. Internal services rarely need the meta-package; they just consume the pieces.

The failure mode this prevents: an engineer needs to change one line of config, has to trigger the full build, and the build takes forty minutes. Multiply by a year of config changes.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Do not fire the whole Step 2 menu at the user.
- **Work on their project if they show it.** If they paste a `Dockerfile`, `pom.xml`, `pyproject.toml`, `package.json`, `Makefile`, or CI config, walk through *their* build, not a generic one.
- **Surface the ecosystem's actual tools.** `bazel query`, `mvn package`, `poetry build`, `cargo build`, `npm pack`, `docker build` — name what they'll actually type, not a generic "run your build tool."
- **Don't lecture the disciplined.** A senior engineer asking about meta-packages doesn't need the five-step pipeline primer.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is choosing between libraries or wrestling with a version conflict. Route to [`dependency-management`](../dependency-management/SKILL.md).
- The user's build is fine but the *tests* are flaky. Route to [`test-determinism`](../test-determinism/SKILL.md); also see [`writing-tests`](../writing-tests/SKILL.md) and [`mocking`](../mocking/SKILL.md).
- The user is asking how to publish the package once it's built — where to host it, immutability, changelogs to users. That's the release phase; until a dedicated skill exists, route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is asking about deploying the built package to environments, rolling it out, feature flags, canaries, blue/green. Route to [`operator-playbook`](../operator-playbook/SKILL.md).
- The user is designing configuration itself (schema, defaults, validation). Route to [`configuration`](../configuration/SKILL.md).
- There's an active incident triggered by a bad build or release. Route to [`incident-response`](../incident-response/SKILL.md); roll back first, tighten the build later.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- ***Continuous Delivery*** — Jez Humble & David Farley (Addison-Wesley, 2010). The canonical text on build pipelines, deployment pipelines, and the discipline of releasing on every commit. Directly foundational for the CI hygiene section above.
- ***Release It!*** — Michael T. Nygard (Pragmatic Bookshelf, 2nd ed. 2018). Stability and capacity patterns for production software; the packaging-and-deploy chapters are especially useful once you're shipping non-trivial services.
- ***Site Reliability Engineering*** — Beyer, Jones, Petoff, Murphy (Google, O'Reilly 2016). Free online at https://sre.google/sre-book/. Covers release engineering as a formal discipline.
- ***Git for Teams*** — Emma Jane Hogbin Westby (O'Reilly, 2015). Branching, review workflows, and how team-level version-control discipline shapes what a good build even looks like.
- ***Amazon Builder's Library*** (https://aws.amazon.com/builders-library). Practitioner essays on how AWS builds and ships at scale; several are directly on the build/release/deploy boundary.
