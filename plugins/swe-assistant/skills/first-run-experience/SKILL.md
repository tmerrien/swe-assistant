---
name: first-run-experience
description: Use when the user is building or writing the thing someone else will encounter for the first time — a README or quickstart for a library or service they own, setup and install instructions, a CLI's first-run behaviour, or onboarding material for a new hire they will receive. Triggers include "nobody uses our library", "people keep asking the same setup question", "how do I document this service", "writing onboarding docs", "our getting-started guide is confusing", or noticing that new users get stuck where the author never does. Treats the first encounter as its own problem with its own failure mode — the author cannot perceive what the newcomer cannot see — and supplies time-to-first-success as the metric, the copy-paste test, and watching rather than asking. When the user is themselves the newcomer, route to new-team-onboarding. For operator tooling, route to operational-tools. For the wording of one message, route to interface-copy.
---

# first-run-experience

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principle 15 (*First impressions matter*).

The abandonment structure comes from **Chao Liu, Ryen W. White, and Susan Dumais**, *Understanding Web Browsing Behaviors through Weibull Analysis of Dwell Time* (SIGIR 2010). Modelling page abandonment as failure in reliability analysis, they find significant **negative aging** — the hazard rate falls as time on page rises — and name the resulting pattern **screen-and-glean**.

The **curse of knowledge** was named by **Camerer, Loewenstein, and Weber**, *The Curse of Knowledge in Economic Settings* (Journal of Political Economy 97(5), 1989). Its best-known demonstration is **Elizabeth Newton's** 1990 Stanford tapping study.

The application to engineering artifacts — READMEs, quickstarts, developer onboarding, time-to-first-success — is the maintainer's, drawn from the observation that this repository covers the *receiving* side of a first encounter ([`new-team-onboarding`](../new-team-onboarding/SKILL.md)) and not the designing side.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (time-to-first-success is an instrumentable metric, not a vibe)
- **Builds:** Leadership (whoever makes the thing adoptable determines whether it gets adopted)

## What this skill is for

Everything you ship to another engineer has a first encounter: a README, an install command, a first API call, a new hire's first week. That encounter behaves differently from everything after it, and it is systematically under-served because the person best placed to write it is the person least able to see it.

This skill fires when someone is building or writing that first encounter.

## The core mindset (lead with this)

**The person who knows the most is the worst possible author of a first encounter — and cannot tell.**

Newton's tappers drummed out well-known songs and predicted listeners would identify **50%** of them. Listeners got **3 out of 120**. The tappers heard the melody in their heads while they tapped and could not un-hear it.

You are the tapper. You see the working system while you write the README, and you cannot perceive the gap between what you wrote and what it says to someone who does not. This is not carelessness and more effort will not fix it — **only contact with an uninformed reader will.**

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Diagnose

Ask **one** question:

- *"What is the first thing you want someone to successfully do, and how long does it currently take them?"*

If they cannot answer the second half, that is the finding — go to *time-to-first-success* below.

### Step 2 — Locate the drop-off

Where do people actually stop? Repeated support questions are the cheapest available data and most teams already have them. The same question asked three times is a defect report about the first run.

### Step 3 — Apply what fits

Draw from the sections below. The copy-paste test is almost always worth naming; it is mechanical and it fails constantly.

### Step 4 — Close

One concrete step, usually: *find one person without context, watch them try it, and do not help.*

---

## The first minutes are a different problem

Liu, White, and Dumais found that abandonment is not spread evenly across a visit. There is a brief high-hazard **screening** phase, and if it is survived, a low-hazard **gleaning** phase that lasts far longer. The hazard rate *falls* with time — the opposite of a wearing part.

For engineering artifacts the window is longer than a web page's — perhaps ten minutes for a library, a few days for a new hire — but the shape holds:

- **Effort spent inside the screening phase has a different return than effort spent anywhere else.** Not "more important" loosely: a genuinely different failure rate.
- **Most teams instrument the steady state and leave the screening phase dark**, which is backwards given where the losses are.
- **The people who abandon never file a ticket.** Your feedback comes from survivors, so it systematically under-reports the problem this skill addresses.

## Time-to-first-success — the number to actually measure

The one metric worth having. Clock from *decided to try it* to *it did something useful for them*.

Concretely:

- **A library:** from `install` to the first successful call that returns real output.
- **A service:** from credentials issued to the first non-error response.
- **A CLI:** from installation to a command that does the thing they came for.
- **A new hire:** from day one to the first merged pull request.

Two properties make this worth the trouble. It is **measurable** — you can time it with a stopwatch and one volunteer, and instrument it properly later. And it is **falsifiable**: nobody argues with *"it took them fifty minutes and eleven of those were on credentials."*

For the SLI and instrumentation mechanics, see [`metrics`](../metrics/SKILL.md).

## The copy-paste test

The highest-yield mechanical check available, and it fails more often than anyone expects.

**Take your quickstart to a clean environment — fresh container, no dotfiles, no credentials, no cached anything — and paste every block in order, changing nothing.**

What this catches, routinely:

- A step that only works because of something in the author's shell.
- A version, path, or environment variable assumed but never stated.
- Blocks that are individually correct and wrong in sequence.
- Output that no longer matches what the command prints.

**If the quickstart matters, put this in CI.** A README block that runs on every commit cannot silently rot, and this is the one piece of documentation where staleness is fatal rather than annoying — it fails people during the screening phase, when they have the least reason to persist.

## Watch, don't ask

Find someone without the context. A new teammate, an engineer from another team, a friend in the same language. Then:

- **Give them the artifact and a goal. Say nothing else.**
- **Do not help.** The urge to help is enormous and it destroys the data. Where they stop *is* the result.
- **Write down every point of hesitation**, including ones you think are silly. A pause is a defect even when the information was technically present.
- **Never ask "was that clear?"** They will say yes. Ask what they would do next, and watch whether they do it. Observed behaviour survives politeness; stated preference does not.

One session with one uninformed reader typically finds more than a week of careful re-reading by the author, for the reason in the core mindset: re-reading is the tapper listening to their own tapping.

## The first error is part of the first run

For a large share of users, the first real experience of your system is a **failure** — a missing credential, a wrong version, an absent config file, a permissions problem.

That error message is usually the worst-written one in the entire system, because it sits on a path the author never walks. It is also the highest-stakes one, arriving when the user has the least invested and the least reason to keep going.

- Make the first-failure paths legible before polishing the happy path.
- **A configuration with no required values is the friendliest possible first run**; one that demands a decision per parameter is hostile. See [`configuration`](../configuration/SKILL.md).
- For the wording itself — what happened, why, what to do next — see [`interface-copy`](../interface-copy/SKILL.md). For what the API should return underneath, see [`input-validation`](../input-validation/SKILL.md).

## A README is a screening artifact, not a reference

Most READMEs are organised the way the author understands the system — architecture, philosophy, configuration table, then eventually how to use it. A reader in the screening phase needs, in this order:

1. **What is this**, in one sentence, in their vocabulary.
2. **Does it solve my problem** — the shape of the thing it is for, and honestly, what it is not for.
3. **How do I try it** — the shortest path to one working result.

Everything else is gleaning-phase material and can come after, or live elsewhere. Ordering matters more than completeness here; see [`rationing-attention`](../rationing-attention/SKILL.md), and note that first and last positions are the ones that survive.

## Onboarding a person is the same problem

A new hire's first week is a first-run experience with a longer window. The same failure produces it — written by whoever has the most context, never tested against someone who lacks it — and the same fixes apply: measure time to first merged PR, have the *last* new hire run the setup document rather than the person who wrote it, and treat repeated week-one questions as defects rather than as the cost of hiring.

[`new-team-onboarding`](../new-team-onboarding/SKILL.md) covers this from the newcomer's side. This skill covers designing it for them.

## Callout — Fast to success versus correct by default

A genuine tension, and it should be decided rather than drifted into ([Design Principle 3.6](../../../../docs/METHODOLOGY.md)).

**For fastest-path:** the entire purpose of the screening phase is getting someone to a working result before they leave. Every additional step is a place to lose them, and a quickstart that teaches best practice thoroughly frequently teaches it to nobody.

**For correct-by-default:** quickstarts get copied into production. A tutorial that disables TLS verification, hardcodes a secret, or skips error handling has published that pattern into every project that started from it.

**What decides it: will the shortcut be something they must *unlearn*, or something they will simply *add later*?**

- **Deferring is fine.** Omitting pagination, retries, or advanced configuration teaches nothing false — those get added when needed.
- **Teaching wrong is not.** `--insecure`, a plaintext credential in a code block, or a swallowed exception will be copied verbatim, and the person copying it has no way to know it was a simplification.

Where a shortcut would be unlearned, either do it properly or make the omission visible in the block itself — a one-line comment costs nothing and travels with the paste.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Work on their actual artifact.** Ask for the README or the quickstart; general documentation advice is close to useless.
- **Push the copy-paste test early.** It is concrete, cheap, and it usually finds something in the first attempt.
- **Push back on "I'll just re-read it."** Name the curse of knowledge and why re-reading cannot work. This is the most common wrong instinct here.
- **Do not write their README for them.** Diagnose the ordering, name the gaps, let them write it. See Design Principle 3.1.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- **The user is themselves the newcomer**, joining a team or learning a codebase. Route to [`new-team-onboarding`](../new-team-onboarding/SKILL.md) or [`ramp-up-playbook`](../ramp-up-playbook/SKILL.md).
- The artifact is an **operator-facing admin tool**. Route to [`operational-tools`](../operational-tools/SKILL.md), which has its own first-encounter discipline for the 2am case.
- The question is **the wording of one message or label**. Route to [`interface-copy`](../interface-copy/SKILL.md).
- The question is **API surface design** rather than the first encounter with it. Route to [`evolvable-apis`](../evolvable-apis/SKILL.md).
- The user is writing a **design doc, RFC, or ADR**. Route to [`design-doc`](../design-doc/SKILL.md) — different audience, different job.
- The surface is a **consumer-facing GUI onboarding flow**. Route to [`interface-decisions`](../interface-decisions/SKILL.md).
- The user is trying to **learn** something themselves rather than teach it. Route to [`learning-toolkit`](../learning-toolkit/SKILL.md).
