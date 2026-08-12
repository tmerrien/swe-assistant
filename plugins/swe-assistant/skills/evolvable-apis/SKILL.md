---
name: evolvable-apis
description: Use when the user is designing an API or changing one that already has callers — adding or removing fields and methods, worrying about breaking clients, deciding whether a change needs a new version, or formalizing an interface that is currently hand-written JSON. Triggers include "will this break clients", "is this a breaking change", "should I version this API", "how do I deprecate this endpoint", "OpenAPI", "protobuf", or "we have no API spec". Covers keeping the surface small, publishing a machine-readable schema, keeping changes compatible, and versioning deliberately. For database schemas and migrations, route to evolvable-data. For SemVer mechanics, route to dependency-management.
---

# evolvable-apis

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 11, "Creating Evolvable Architectures"** — the *Evolvable APIs* section. Keeping the surface small, publishing well-defined service schemas, maintaining compatibility, versioning deliberately, and versioning documentation alongside the API all come from this chapter.

The chapter refers back to **Chapter 5** for semantic-versioning mechanics, which this repository covers in [`dependency-management`](../dependency-management/SKILL.md); that material is cross-linked rather than repeated here.

**Named tooling** (OpenAPI, Protocol Buffers, Thrift, IDLs) is the chapter's, and is widely-attested current practice.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (an API is a contract, and versions are how you talk to consumers about change)
- **Builds:** Leadership (API conventions outlive whoever set them)

## What this skill is for

An API is a promise to people you often can't contact. Once something has callers, every change is a change to code you don't own and can't test — and the further outside your team those callers are, the less able you are to fix what you break.

Changing an API is *easy to do and hard to do well*. This skill fires when the user is designing one, or about to change one that already has consumers, and needs to work out what's safe, what needs a version, and how to make the next change easier than this one.

## The core mindset (lead with this)

**Every field you add is a promise you have to keep. Add fewer.**

- **Compatibility is what buys independence.** If clients and servers can deploy on their own schedules, you can ship. If they can't, every release becomes a coordination problem.
- **Removing is far harder than adding.** Design assuming you'll never get anything back out.
- **Versioning is a real cost, not a free escape hatch.** Every live version is maintenance, backported fixes, and a matrix your team has to hold in their heads. Version deliberately, not reflexively.
- **How much rigor you need scales with how hard your callers are to change.** A public customer-facing API and an internal endpoint between two services you deploy together are not the same problem — see the inertia framing in [`managing-complexity`](../managing-complexity/SKILL.md).

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual API, skip diagnosis when their message already says what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that the constraint is who the callers are and how hard they are to change. Skip if the user has a specific decision queued.

### Step 2 — Ask the question that determines everything else

If it isn't already clear, ask **one** question — and make it this one:

> *"Who calls this API, and how hard would it be for them to change?"*

The answer sets the rigor for every subsequent step:

- **External / customer-facing** — highest inertia. Formal schema, strict compatibility, real versioning, versioned docs, long deprecation windows. You have the least control and the most obligation.
- **Internal, other teams** — moderate. Schema and compatibility matter; versioning can be lighter and deprecation faster because you can talk to every consumer.
- **Internal, your team, deployed together** — lowest. Keep it clean, but formal versioning is usually overhead you don't need.

Common shapes from here: **designing new** → Step 3. **Changing existing** → Step 5. **No formal spec at all** → Step 4. **Choosing a versioning scheme** → Step 6.

### Step 3 — Keep the surface small

YAGNI applies directly (see [`managing-complexity`](../managing-complexity/SKILL.md)):

- **Only add methods and fields you need right now.** Not ones you expect to need. Each one is permanent in practice.
- **Prune what generators produce.** Bootstrapping from a framework, scaffold, or code generator typically emits a wide surface of fields and endpoints you never asked for. Delete what you're not using *before* it ships — once it's published, someone will depend on it.
- **Use sensible defaults to make a large API feel small.** If a method has many fields, defaulting the ones most callers don't care about lets them focus on the few that matter. This is how a rich API stays approachable — the complexity is present but not imposed on every caller.

A useful check: *if I had to remove this field in a year, could I?* If the honest answer is no, be surer you want it.

### Step 4 — Expose a well-defined, machine-readable schema

An evolvable service declares its **request and response schemas, its methods, and its errors** — in a form machines can read, not just prose.

- **RESTful services:** OpenAPI is the default.
- **Non-REST:** Protocol Buffers, Thrift, or another IDL.
- **Use your company's API definition framework if one exists.** Consistency across services is worth more than picking the theoretically best tool.
- **If your team hand-writes REST/JSON with no formal definition step**, retrofitting OpenAPI is high-value and can usually be done incrementally, starting with the endpoints that have the most external consumers.

**Publish the schema**, because that's what unlocks the real benefit: generated clients, and **automated compatibility testing of both client and server code** against the same contract. A schema that only lives in your repo is documentation; a published one is enforcement.

Errors are part of the contract too. Specify what callers get for malformed input, constraint violations, and unexpected internal failures — see [`input-validation`](../input-validation/SKILL.md).

### Step 5 — Keep changes compatible

Compatibility is what lets client and server versions evolve independently. Two directions, and you usually need both:

- **Backward compatible** — new server handles requests from old clients.
- **Forward compatible** — old server (or old client) tolerates data produced by the new one, typically by ignoring fields it doesn't recognize.

The safe/unsafe classification is in the callout below. The one-line version: **adding optional things is safe; removing, renaming, narrowing, or requiring is not.**

Note that this is the *same* problem as a rolling deploy, where old and new code run simultaneously — see [`deployment-discipline`](../deployment-discipline/SKILL.md), and [`progressive-rollout`](../progressive-rollout/SKILL.md) if the change is being ramped behind a flag.

### Step 6 — Version deliberately

Eventually you need a change no compatibility trick covers — a genuinely required new field, a restructured resource, a removed capability. That's what versions are for.

**What versioning buys you:**

- Freedom to make incompatible changes without breaking existing callers.
- A vocabulary for talking to consumers — they can tell you what they're on, you can tie new capability to a new version.
- Room to set less stringent compatibility guarantees within a version, because the escape hatch exists.

**What it costs — be honest about this before adopting it:**

- Old major versions must be **maintained**, and bug fixes **backported** to them.
- Developers must track which version supports which features.
- Without good tooling, version management lands on engineers as ongoing manual work.

**Choosing a scheme:** semantic versioning is the common default (mechanics in [`dependency-management`](../dependency-management/SKILL.md)), but plenty of companies use dates or other numeric schemes, and there are several places to put the version (URL path, header, media type, query parameter). Every option has trade-offs and every option has people with strong opinions.

**Use your company's standard if it has one.** If it doesn't, ask your manager or tech lead what they'd prefer rather than inventing one alone — this is a decision whose value comes almost entirely from consistency.

**Version the documentation alongside the API.** Developers stuck on an old version need accurate docs for *that* version. Committing API documentation into the main code repository is the practical trick: docs and code move together, and [`code-review`](../code-review/SKILL.md) catches documentation that's drifted from behavior.

### Step 7 — Pick one action, then close

Ask: *"What's the one thing you'll do?"* Push for concreteness.

- *"Make the API better"* → too vague.
- *"Delete the six fields the generator added that nothing reads, before this ships Friday"* → the action.
- *"Add the field as optional with a default, dual-read for two releases, then make it required in v2"* → the action.
- *"Write the OpenAPI spec for the three externally-called endpoints and wire it into CI"* → the action.

Close in one or two sentences.

---

## Callout — What's safe to change, and what isn't

Assumes consumers you can't upgrade in lockstep. The more external the caller, the more strictly this holds.

**Generally safe (backward compatible):**

- Adding an **optional** field to a request, with a sensible default when absent.
- Adding a field to a response — *provided* consumers ignore unknown fields. Verify this; strict parsers and generated clients sometimes reject them.
- Adding a new endpoint, method, or enum value **that old clients never receive**.
- Relaxing a validation constraint (accepting more than before).
- Making a required request field optional.

**Not safe (breaking):**

- Removing or renaming any field, endpoint, or method. **Renaming is remove + add**, and it breaks exactly like a removal.
- Making an optional request field required.
- Changing a field's type, or narrowing its accepted range.
- Changing the meaning of an existing field while keeping its name — **the worst of all**, because nothing fails loudly. Callers keep working and quietly do the wrong thing.
- Adding a new enum value that **old clients will receive** and don't know how to handle.
- Changing error codes, status codes, or pagination behavior that callers branch on.

**Genuinely ambiguous, and worth checking rather than assuming:**

- Tightening validation. Formally breaking, but often the right call if the previously-accepted input was invalid anyway — check your logs for whether anyone actually sends it.
- Changing default values. Silent behavior change for every caller relying on the default.
- Field ordering and null-vs-absent, which matter in some serialization formats and not others.

**The safe path for a change that must break:** add the new thing alongside the old, migrate callers, deprecate with a real timeline and real telemetry on who's still calling, then remove. The removal is the last step, not the first.

---

## Callout — Making a required field additive

The most common breaking change engineers propose, and it has a standard resolution worth knowing.

**The problem:** you need callers to supply something they currently don't. Adding it as required breaks every existing caller immediately.

**The staged approach:**

1. **Add it optional**, with a default that preserves today's behavior. Nothing breaks; new callers can start supplying it.
2. **Measure.** Log how many requests omit it, and which callers those are. This tells you whether step 4 is even reachable.
3. **Migrate callers**, loudest and largest first. For internal consumers, this is a conversation; for external ones, deprecation notices and a timeline.
4. **Make it required** — in a new version if consumers are external or numerous, in place if you've confirmed everyone supplies it.

Steps 2 and 3 are the ones people skip, and they're the ones that make step 4 safe rather than hopeful. If you can't measure who omits the field, you can't know whether requiring it is safe — and *that* is the thing to fix first.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Lead with the who-calls-this question; it determines everything downstream.
- **Work on their actual API.** If they paste a schema, endpoint, or proposed change, classify *that* against the safe/unsafe callout rather than reciting it.
- **Don't over-prescribe versioning.** For an internal API between two services deployed together, formal versioning is usually overhead. Say so.
- **Push back on speculative fields.** "We might need it later" is the exact instinct this skill exists to interrupt.
- **Name silent breakage explicitly.** Changing a field's meaning while keeping its name is the most dangerous change and the least likely to be noticed. Call it out whenever it appears.
- **Respect existing conventions.** If the company has a versioning standard, the answer is to follow it, even if another scheme is theoretically nicer.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is changing a **database schema** or migrating data. Route to [`evolvable-data`](../evolvable-data/SKILL.md) — same compatibility logic, different tooling.
- The user is asking about **SemVer mechanics** or third-party library versions. Route to [`dependency-management`](../dependency-management/SKILL.md).
- The user is deciding **whether to add an abstraction** or where a boundary goes. Route to [`managing-complexity`](../managing-complexity/SKILL.md).
- The user is rolling out a change gradually behind flags or canaries. Route to [`progressive-rollout`](../progressive-rollout/SKILL.md).
- The user is designing **operator-facing tooling** rather than a service API. Route to [`operational-tools`](../operational-tools/SKILL.md).
- The user is writing **validation logic** for untrusted input. Route to [`input-validation`](../input-validation/SKILL.md).
- The user is designing an operation that must be safely retryable. Route to [`idempotency`](../idempotency/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- ***Designing Data-Intensive Applications*** — Martin Kleppmann (O'Reilly, 2017). Chapter 4 ("Encoding and Evolution") is the best available treatment of schema evolution and compatibility, and it covers APIs and data storage as the same problem — which is the connection this skill and [`evolvable-data`](../evolvable-data/SKILL.md) are built on.
- ***Building Evolutionary Architectures*** — Neal Ford, Rebecca Parsons, Patrick Kua (O'Reilly, 2017). Architecture for continuous change, including automated fitness functions that guard properties like compatibility.
- **Public proposal archives** — Python PEPs, Kafka KIPs, Rust RFCs. All three communities debate API compatibility in public; KIPs in particular are unusually explicit about compatibility and migration. See [`design-doc`](../design-doc/SKILL.md).
