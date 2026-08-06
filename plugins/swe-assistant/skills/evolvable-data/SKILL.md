---
name: evolvable-data
description: Use when the user is changing how data is stored or shaped — altering a schema, running a migration, backfilling or rewriting records, deciding between an explicit schema and a schemaless store, splitting a shared database, or worrying that a schema change will break downstream consumers or analytics. Triggers include "how do I migrate this schema", "will this migration break anything", "add a column safely", "how do I backfill", "should this be JSON or a real column", "schemaless", "we have a shared database", "another team reads our tables", "our migration is tied to the deploy", "gh-ost", "Flyway", "Liquibase", "change data capture", "our ETL broke when we renamed a column", or "how do I rename a column safely". Walks the evolvable-data discipline from The Missing Readme (Ch. 11) — isolate databases, use explicit schemas, automate migrations, decouple them from deploys, and keep schemas compatible for downstream readers. For service API contracts, route to evolvable-apis.
---

# evolvable-data

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 11, "Creating Evolvable Architectures"** — the *Evolvable Data* section. Isolating databases, using explicit schemas, automating schema migrations, decoupling migrations from application deployment, and maintaining schema compatibility for downstream consumers all come from this chapter, as does the observation that stored data has the **same compatibility problem as an API**.

**Named tooling** (gh-ost, pt-online-schema-change, Square's Shift, ORM-provided migration systems) and the **data warehouse / ETL / change-data-capture** framing are the chapter's, and are widely-attested current practice.

The deploy-time half of this material — two-phase migrations during a rolling deploy — is covered from the deployment angle in [`deployment-discipline`](../deployment-discipline/SKILL.md) and cross-linked rather than duplicated.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (schema changes affect people you may not know about yet)
- **Builds:** Leadership (data hygiene decisions are inherited for years)

## What this skill is for

Data outlives code. A service can be rewritten in a quarter; the data it wrote will still be there, still being read, possibly by systems nobody told you about. That asymmetry is why schema changes are the highest-consequence routine work most engineers do — and why "it's just adding a column" is where the trouble starts.

This skill fires when the user is changing stored data or its shape: altering a schema, running a migration, backfilling, choosing between explicit and implicit schemas, splitting a shared database, or trying to make a change without breaking a downstream consumer they can't see.

## The core mindset (lead with this)

**Stored data is an API. The reader and the writer change independently.**

- The code that writes a row and the code that reads it may be **different software, on different machines, deployed at different times, owned by different teams**. That's precisely the API compatibility problem — same rules, different tooling.
- **Migrations are not deploys.** Tying them together means a delicate, slow, hard-to-reverse operation runs on the schedule of a routine one.
- **Rollback has limits.** Code rolls back cleanly; data usually doesn't. A dropped column doesn't come back because you redeployed.
- **Schemaless doesn't mean no schema** — it means the schema is implicit, applied at read time, and enforced by nobody.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual schema or migration, skip diagnosis when their message already says what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that stored data is a contract between independently-changing readers and writers. Skip if the user has a specific change in hand.

### Step 2 — Ask who reads this data

If it isn't already clear, ask **one** question, and make it this one:

> *"Besides this application, what else reads this data?"*

The honest answer is usually longer than expected: other services, analytics and reporting, an ETL job into a warehouse, a change-data-capture stream, a dashboard someone built two years ago, a scheduled export. **Every one of those is a consumer of your schema**, and most of them will not be represented in your code review.

Rough shapes from here: **changing a schema** → Steps 5–7. **choosing a data model** → Step 4. **shared database problems** → Step 3. **no migration tooling** → Step 6.

### Step 3 — Isolate databases

**A database shared between applications is very hard to evolve**, because you lose autonomy — you can't change a schema, and sometimes can't even reason about read load, without knowing how everyone else uses it. In practice, shared databases become frozen.

- **Default to a database per application.** This is what makes changes cheap: you only reason about your own app's use of it.
- **Shared access is sometimes a legitimate intermediate step** — notably when breaking up a monolith, where sharing is a stage on the way to a properly isolated store rather than the destination.
- **Many databases cost real operations effort.** Early on it can be entirely sensible to co-locate several logical databases on one machine. The thing to protect is that *shared* databases eventually get isolated, split, or replaced — co-location is an operational choice, shared access is an architectural one, and conflating them is how the temporary becomes permanent.

If the user is stuck with a shared database they can't change: the practical move is Step 7's data-product idea — publish an explicit contract for outside readers so the internal schema can move independently.

### Step 4 — Use explicit schemas

Rigid columns and heavyweight change processes are what drove people to schemaless stores. But **schemaless does not mean no schema** — it means an *implicit* schema, supplied or inferred at read time, enforced by nothing and documented nowhere. The structure still exists; you've just moved responsibility for it from the database to every reader, forever.

In the complexity vocabulary of [`managing-complexity`](../managing-complexity/SKILL.md), that's a straight trade of a little write-time friction for a lot of **obscurity**, plus real data-integrity risk.

- **Prefer explicit, strongly-typed schemas.** They keep applications stable and keep the data usable by people who didn't write it.
- **Explicit schemas are harder to change — by design.** That friction is a feature: it's what forces the compatibility question to be asked before the data is wrong, not after.
- **The anti-pattern:** stuffing JSON into a `data` column, or a generic string-to-string map, to avoid declaring structure. It feels fast and is self-defeating — you've kept all the structure and thrown away all the enforcement.

**When schemaless genuinely is the right call:**

- **You're moving fast and don't yet know the shape** — early iteration, before the model is understood.
- **The data has little or no value**, and losing or malforming it is acceptable.
- **The data is legitimately non-uniform** — records genuinely have different fields, not just fields you haven't bothered to declare.
- **As a deliberate transition step** — temporarily relaxing to implicit schema can ease migrating *toward* a new explicit one.

The test for the first case: *have you learned the shape yet?* If yes, the reason has expired, and the schemaless store is now debt ([`technical-debt`](../technical-debt/SKILL.md)).

### Step 5 — Keep schemas compatible

The same classification as an API contract, because it *is* one:

- **Adding an optional/nullable column** — safe.
- **Adding a column with a default** — usually safe; watch for a table rewrite on large tables.
- **Removing or renaming a column** — breaking. **Renaming is a drop plus an add**, and it breaks every reader that selects it. This is the single most common way an analytics pipeline dies.
- **Narrowing a type or adding NOT NULL** — breaking for existing writers.
- **Changing the meaning of a column without changing its name** — the most dangerous, because nothing errors. Readers keep working and are quietly wrong.

**The safe path for anything breaking is expand-and-contract**, in the callout below.

### Step 6 — Automate migrations, and decouple them from deploys

**Use a schema migration tool**, and use it for *every* change. The value isn't convenience — it's that the tool forces you to track the complete history of the schema and gives you a defined path from any version to any other. Ad-hoc SQL run by hand against production has no history and no repeatability.

- If your company has an ORM or migration framework, **use it**. If not, agree one with your team.
- Once chosen, **all schema changes go through it.** A single hand-run `ALTER TABLE` breaks the guarantee that the tool's history matches reality.
- Work with your database team on schema evolution rather than around them.

**Do not couple database migrations to application deployment.** Tying them together is dangerous: schema changes are delicate, can have serious performance implications, and can take hours on large tables — while deploys are meant to be routine and fast. Separating them lets you choose *when* a schema change goes out, run it during low traffic, and abort without blocking a release.

**Tools worth knowing:**

- **Online schema change** for large tables without locking: GitHub's **gh-ost**, Percona's **pt-online-schema-change**. These let a DBA run a big migration without a production performance hit.
- **Versioning and diffing:** tools such as Square's **Shift** offer more sophisticated schema versioning, including diffing schemas and directing changes.
- **Rollback:** most migration tools support it — but **rollback only does so much.** Reversing an `ALTER` doesn't restore dropped data. Treat the down-migration as a convenience for the reversible cases, never as the safety plan for a destructive one.

### Step 7 — Protect downstream consumers

The consumers from Step 2 need protecting explicitly, because they usually can't defend themselves.

- **Data warehouses** — analytics/reporting databases fed by an **ETL** pipeline that extracts from production, transforms, and loads. A renamed column upstream silently breaks reports downstream.
- **Change data capture (CDC)** — an event-based approach that turns inserts, updates, and deletes into messages for downstream consumers. Powerful, and it propagates your schema — and your schema *changes* — to everyone subscribed.

Two defences:

**Validate schema changes before they hit production.**
- **As early as possible** — ideally at commit time, by inspecting the DDL statements in the change.
- **Execute the DDL in a pre-production integration environment**, then run integration tests that exercise downstream systems, to verify nothing breaks.

**Decouple internal schemas from external readers by publishing a data product** — an explicit, stable, deliberately-designed representation for downstream consumers, rather than letting them read your internal tables directly. Your internal schema is then free to change, because it isn't the contract. This is the data equivalent of putting an API in front of a database, and it's the durable fix for the shared-database problem in Step 3.

### Step 8 — Pick one action, then close

Ask: *"What's the one thing you'll do?"* Push for concreteness.

- *"Be careful with migrations"* → too vague.
- *"Add `region` nullable this week, backfill next, add NOT NULL once the backfill verifies"* → the action.
- *"Find out who reads the `orders` table before touching it — start with the warehouse ETL"* → the action.
- *"Move the hand-run SQL into Flyway so the schema history is real"* → the action.

Close in one or two sentences.

---

## Callout — Expand and contract

The standard safe pattern for any breaking schema change. Slower than one `ALTER`, and it's the difference between a routine change and an incident.

Renaming `user_name` to `username`:

1. **Expand** — add the new column alongside the old. Nullable, no constraint. Nothing reads it yet.
2. **Dual-write** — deploy code writing *both* columns. Old readers still work; new data is in both places.
3. **Backfill** — copy historical rows into the new column, in batches, monitoring load. Verify counts match.
4. **Dual-read, prefer new** — deploy code reading the new column, falling back to the old. Now you can confirm the new column is correct against live traffic before you rely on it.
5. **Stop reading old** — remove the fallback. The old column is now unused but still populated. **Stop here for a while.** This is the last fully-reversible point.
6. **Stop writing old** — remove it from writes.
7. **Contract** — drop the old column, once you're confident and downstream consumers have migrated.

Notes that matter:

- **Each step is a separate deploy.** That's what makes each one individually reversible.
- **Steps 5 and 6 want real time between them** — long enough for any consumer you forgot to surface. Days, sometimes weeks.
- **Step 7 is irreversible.** Everything before it can be walked back.
- Steps 1–4 are the same shape as the two-phase migration in [`deployment-discipline`](../deployment-discipline/SKILL.md), seen from the data side rather than the deploy side.

The pattern generalizes: adding a required field, splitting a table, changing a type, moving to a new store. **Expand, migrate, verify, contract** — with the irreversible step last and latest.

---

## Callout — Migration safety checklist

Run through before executing anything against production.

**Blast radius**
- Who reads this table, including analytics, ETL, CDC subscribers, and dashboards?
- Which of those consumers am I *guessing* about? Go verify at least the biggest.
- Is this change reversible? If not, what's the recovery plan — and has a restore actually been tested?

**Performance**
- How many rows? Will this lock the table, or rewrite it?
- Does the table need an online schema change tool (gh-ost, pt-online-schema-change)?
- Has it been timed against a production-sized dataset? Staging row counts routinely mislead.
- If it's a backfill: batched, rate-limited, resumable if interrupted?

**Correctness**
- Is the change in the migration tool, not hand-run SQL?
- Has the DDL been executed in a pre-production environment with integration tests exercising downstream systems?
- If adding a constraint: does existing data actually satisfy it? Check before, not during.

**Timing**
- Is this decoupled from the application deploy, so it can run on its own schedule?
- Is it going out at a sensible traffic hour, with someone watching?
- If this is high-inertia data, has it been announced to the teams that read it?

The recurring theme: **the expensive failures come from consumers you didn't know about and volumes you didn't test at.** Both are findable in advance, and rarely are.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Lead with who-else-reads-this; it's the question that surfaces the real risk.
- **Work on their actual schema.** If they paste a table or a proposed migration, classify *that* against Step 5 and walk the expand/contract steps for their specific columns.
- **Treat renames as removals.** Users routinely describe a rename as a small change. It isn't.
- **Ask about row counts early.** "Add a column" is trivial at ten thousand rows and an outage at two hundred million.
- **Name silent breakage.** Changing a column's meaning while keeping its name produces no error and wrong answers. Flag it whenever it appears.
- **Don't over-engineer small cases.** A single-consumer table in a low-traffic internal app doesn't need seven-step expand-and-contract. Match rigor to blast radius.
- **If the change is already out and something broke**, route to [`incident-response`](../incident-response/SKILL.md) first.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is changing a **service API contract**. Route to [`evolvable-apis`](../evolvable-apis/SKILL.md) — same compatibility logic, different tooling.
- The user is deciding **whether to add an abstraction** or where boundaries go. Route to [`managing-complexity`](../managing-complexity/SKILL.md).
- The user is asking about the **deploy mechanics** of shipping a change safely. Route to [`deployment-discipline`](../deployment-discipline/SKILL.md).
- A migration has **already broken production**. Route to [`incident-response`](../incident-response/SKILL.md) — stabilize first.
- The user is choosing a **new database technology**. Route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- The user is writing **validation logic** for incoming data. Route to [`input-validation`](../input-validation/SKILL.md).
- The user is designing **configuration**, not persisted application data. Route to [`configuration`](../configuration/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- ***Designing Data-Intensive Applications*** — Martin Kleppmann (O'Reilly, 2017). The definitive treatment. Chapter 4 ("Encoding and Evolution") covers backward and forward compatibility across Avro, Protocol Buffers, and Thrift, and makes the same core point this skill is built on: stored data and service APIs are the same evolution problem. Probably the single highest-value book on this list for anyone working with data at scale.
- ***Data Mesh: Delivering Data-Driven Value at Scale*** — Zhamak Dehghani (O'Reilly, 2022). The full architectural treatment of the **data product** idea in Step 7 — treating published data as a deliberately-designed product with owners and contracts, rather than a byproduct other teams scrape.
- ***Building Evolutionary Architectures*** — Neal Ford, Rebecca Parsons, Patrick Kua (O'Reilly, 2017). Includes evolutionary approaches to data and the integration points around it.
