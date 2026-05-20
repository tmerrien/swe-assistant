---
name: operational-tools
description: Use when the user is designing or building tools that help operators run their service or system — bulk-loading data, recovery actions, database resets, leadership elections, partition shifts, admin commands, debug dumps, or any other operator-facing utility. Triggers include "I need to build an admin tool for X", "how should I structure ops tooling for this service", "CLI or UI for this admin action", "should this be a script or a service", "how do I make this operable", "building a recovery tool", "admin command", "operator-facing tool", "self-describing API", "integrate with our internal tooling", "single pane of glass", or asking how the ops team should interact with the service. Walks through the operational-tools discipline from The Missing Readme (Chapter 4) — talk to the ops team first, prefer CLI and self-describing APIs (SRE conventions), abstract logic into a shared library so CLI and UI can share it, treat tools as production code, integrate with existing platform tooling. Do not trigger for end-user-facing CLIs, internal application libraries, build / dev tooling, or active incidents (route to incident-response).
---

# operational-tools

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Tools). Augmented with widely-attested SRE practice (CLI-first conventions, self-describing APIs, role-based access for destructive operations).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (the tool is the interface for the operator — design it as a UX)
- **Builds:** Leadership (services that ship with operator tooling are services other teams want to run)

## What this skill is for

A service or system that does its job correctly but can't be administered is not operable. Operators — SREs, on-call engineers, support staff, sometimes the developers themselves — need to perform recurring actions that aren't part of normal request handling: bulk-loading data, running recovery, resetting state, triggering leadership elections, shifting partition assignments, debugging stuck instances, and so on. Without tools, these become bespoke scripts, manual database edits, or "the one person who knows."

This skill fires when the user is designing or building those tools. Its job is to keep the tools usable, safe, and consistent with the wider operational environment.

## The core mindset (lead with this)

**Ops tools are the interface between your service and the people who keep it running. Design them for the operator, not for the developer who wrote the service.**

- The developer who wrote the service has the full mental model. The operator at 2am does not. Tools must work with the operator's level of context, not the author's.
- A tool that *exists* is far better than no tool — but only barely. A tool that's hard to use is often worse than no tool because it gives the illusion of safety while encouraging mistakes.
- **Talk to your ops team before you build.** They know what they actually need, in what order, with what error handling. Building the wrong tool wastes more time than not building one at all.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Diagnose

If the user named a specific tool to build, work on that. Otherwise ask **one** question:

- *"What operation does the tool need to support, and who's going to use it (SREs, on-call developers, support staff)?"*

### Step 2 — Apply the relevant practices

Walk through the practices below based on what the user is building. Don't dump all five if only one matters.

### Step 3 — One concrete next step

Often this is: *"go talk to the ops team about exactly what they need"* — and that *is* the right first step before any code gets written.

### Step 4 — Close

If the tool is non-trivial, mention that it deserves a [`design-doc`](../design-doc/SKILL.md). If it can take down production, mention the auth callout below.

---

## The five practices

### 1. Talk to the ops team first

The most common failure mode of ops tooling: built by developers, designed for the workflow the developer *imagines* operators have, ignored by operators who do something different.

- **Find the people who will actually run the tool.** SREs, on-call engineers, support, sometimes external partners.
- **Ask what they need, in what order, with what error handling.** Their existing scripts, runbooks, and one-off workarounds reveal the actual workflow.
- **Ask what tools they already have.** New tools that don't integrate with existing ones add fragmentation.
- **Ship a thin first version and iterate.** A v1 the ops team uses is infinitely more valuable than a v3 they don't.

If you don't have a dedicated ops team, the principle still applies: the operator might be future-you at 2am, or an on-call peer who didn't write the service. Build for them, not for you-now.

### 2. Prefer CLIs and self-describing APIs (the SRE convention)

SREs and ops engineers generally prefer command-line tools over UIs for ops work. Reasons:

- **Composable.** CLIs pipe into other CLIs (`tool list | grep ... | xargs tool fix`); UIs don't.
- **Scriptable.** Routine ops can be automated. UIs require humans-in-the-loop.
- **Reproducible.** A CLI command can be pasted in a runbook, into Slack, into a postmortem. A UI workflow can't.
- **Auditable.** CLI history shows exactly what was run; UI clicks are harder to capture.
- **Diffable.** Two CLIs invocations are easy to compare; two UI screens are not.

If you can only build one interface, build the CLI.

**Self-describing APIs** are the API equivalent of `--help`: the API exposes its own methods, parameters, and types in a discoverable form. Examples:

- **gRPC reflection** — clients can query the server for its method list and message types.
- **OpenAPI / Swagger documents** served by the application itself.
- **CLI subcommands with `--help` on every level**, listing options with types and defaults.

Self-description means operators can discover what's possible without reading source code. It pairs naturally with CLIs (they can introspect each other) and with monitoring/automation tools that can adapt to API changes.

### 3. If you build a UI, abstract the logic into a shared library

UIs have their place — for less technical operators, for visual workflows, for actions that benefit from confirmation dialogs. But:

- **The business logic must live in a shared library** that both the CLI and the UI call.
- **The CLI must continue to exist** for the use cases where it's better (composability, scripting, runbooks).
- **The UI is the presentation layer**, not the source of truth for what the tool does.

This pattern means:

- Bug fixes apply to both interfaces automatically.
- New operations show up in both interfaces with one implementation.
- Power users use the CLI; less technical users use the UI; both groups get the same correct behavior.

### 4. Treat tools as production code

Ops tools are production code. They:

- **Follow the same coding standards** as the rest of the codebase.
- **Get the same rigor in code review** — see [`code-review`](../code-review/SKILL.md).
- **Have tests** — including tests for failure modes (what happens when the underlying service is partially down).
- **Have logging** — see [`logging`](../logging/SKILL.md) and the audit callout below.
- **Have validated configuration** — see [`configuration`](../configuration/SKILL.md).
- **Are idempotent where possible** — see [`idempotency`](../idempotency/SKILL.md). Operators retry; tools must handle it.

The temptation to treat ops tooling as second-class ("just a script") leads to ops tools that break the worst possible way at the worst possible time.

### 5. Integrate with existing platform tooling

Don't build a one-off tool when the team already has a platform for ops work.

- **Existing CLI suites at your company** — many organizations have a unified CLI (`mycompany-cli`, `corp-tool`) that all services plug into. Adding a new subcommand to an existing tool is usually better than shipping a new binary.
- **Existing UIs / consoles** — admin portals, support tools, internal dashboards. If they exist, your tool's UI should live in them, not as its own page nobody bookmarks.
- **Existing monitoring / alerting** — tools that operators use should integrate with the systems where ops work already lives.
- **The "single pane of glass" goal** — operators should have one console (or as few as possible) that shows the state of everything they manage. Tools that fragment this goal create context-switching cost on every shift.

**Before building a new tool, ask:** *"Is there an existing tool we should add to instead?"*

---

## Callout — Common operational tool categories

Quick taxonomy. Most ops tools fall into one of these:

- **Data operations:** bulk import / export, migrations, repair (fix corrupted records), reindex, cache warm.
- **State operations:** reset to clean state (for staging environments), trigger leadership election, shift partition / shard assignment, drain a node before maintenance, freeze and thaw write traffic.
- **Debug operations:** dump current state, capture snapshot, trace single request through the system, force-flush internal queues, simulate failure.
- **Lifecycle operations:** create or destroy resources (test accounts, sandbox tenants), provision / deprovision capacity.
- **Investigation operations:** read records by ID without authentication (support workflows), search across normally-isolated data (with audit trail).

Knowing which category your tool falls into helps you reason about the right safeguards, audit requirements, and access controls.

---

## Callout — Auth and RBAC for destructive ops

The book doesn't make this explicit, but it's one of the most consequential design decisions in ops tooling.

**Some ops actions have huge blast radius.** *"Reset state"* can mean *"delete all customer data."* *"Shift partition"* can mean *"take production down for everyone in that region."* Tools that gate these actions only by *"the user has SSH access to the box"* are dangerous.

**Practices that matter:**

- **Role-based access control (RBAC).** Define roles (read-only, support, ops, admin) and require the right role for each operation. Many destructive operations should require an admin role, not just an operator role.
- **Confirmation for irreversible actions.** *"Type the cluster name to confirm"* prevents reflex-driven mistakes. Be explicit about what's about to happen.
- **Dry-run mode.** Most destructive tools should have a `--dry-run` flag that simulates the action without performing it. This is invaluable for both training and pre-flight validation.
- **Audit logs.** Every privileged operation should be logged: who, when, what, to which target, with what result. See [`logging`](../logging/SKILL.md) for the discipline. The audit log is the answer to *"who did this?"* — which someone will ask after every serious incident.
- **Multi-party approval for the most dangerous operations.** Some actions (deleting production data, changing global config) should require a second engineer to approve before they execute. The friction is intentional.

The principle: **the cost of a guardrail is much smaller than the cost of an accidental production deletion.**

---

## When to build a tool vs use existing infrastructure

Not every recurring operation needs a custom tool. A useful test:

- **Done weekly or more often** → build a tool. The cost amortizes.
- **Done occasionally but high-stakes** (data recovery, leadership election) → build a tool, *especially* because rare operations are where humans make mistakes.
- **Done once a year and low-stakes** → a documented manual procedure may be enough.
- **Already supported by existing platform tools** → use those instead of building.
- **Could be done by clients / users directly, with a small API change** → consider that path first.

When you do decide to build, treat the tool itself like a project — for non-trivial tools, a brief [`design-doc`](../design-doc/SKILL.md) is worth the time.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about audience, interface, integration, and auth in one message.
- **Push hard on "talk to ops first."** If the user is building without having talked to the operators who will use the tool, this is the most leveraged feedback you can give.
- **If the tool is destructive, surface the auth callout early.** Tools that can take down production deserve up-front discussion of safeguards, not retrofitted ones.
- **Recommend the CLI-first path** unless the user has a specific reason for UI-first. Most do not.
- **Encourage integration over fragmentation.** *"Is there an existing tool you could add to instead?"* is often the most useful question.

## When NOT to use this skill

- The user is building an **end-user-facing CLI** (developer tools, public CLIs) — different concerns. Skip.
- The user is asking about **internal application libraries** that aren't operator-facing. Skip.
- The user is asking about **build / dev tooling** (Webpack, Make, build pipelines). Different domain.
- The user is in an **active incident** that requires using existing ops tools — route to [`incident-response`](../incident-response/SKILL.md). Designing tools is a calm-afternoon activity.
- The user is **reviewing a PR for an ops tool** — route to [`code-review`](../code-review/SKILL.md) with the practices in this skill as the lens.
