---
name: managing-complexity
description: Use when the user is making a structural decision about code and wondering whether it makes the system harder to understand or change — adding an abstraction, building flexibility for a requirement they don't have yet, choosing where module boundaries go, or noticing a change rippled further than expected. Triggers include "should I add an abstraction here", "is this over-engineered", "YAGNI", "premature optimization", "this change touched twelve files", "everything is coupled to everything", or "where should this boundary go". Covers dependency, obscurity, and inertia; complexity as something you place rather than remove; YAGNI; and least astonishment. For evolving an API or a database schema specifically, route to evolvable-apis or evolvable-data.
---

# managing-complexity

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 11, "Creating Evolvable Architectures."** The design principles (YAGNI, principle of least astonishment, encapsulating domain knowledge) and the **inertia** dimension are from this chapter — inertia is the authors' own addition to the framework below.

**Complexity, dependency, and obscurity** are taken from John Ousterhout's *A Philosophy of Software Design* (Yaknyam Press, 2018), which *The Missing Readme* adopts explicitly. Ousterhout defines complexity as *anything related to the structure of a system that makes it hard to understand and modify* — a deliberately consequence-based definition rather than a metric.

**Domain-driven design** is Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003); the practical treatment is Vaughn Vernon's *Implementing Domain-Driven Design* (2013). **Muntzing** is named after Earl "Madman" Muntz, a mid-century television manufacturer who reportedly removed components from a working circuit one at a time until it stopped working, then replaced the last one.

The organisational-inertia material draws on **Melvin Conway**, *How Do Committees Invent?* (Datamation, April 1968), with empirical support from **Nagappan, Murphy & Basili**, *The Influence of Organizational Structure on Software Quality* (ICSE 2008) and **MacCormack, Rusnak & Baldwin**, *Exploring the Duality Between Product and Organizational Architectures* (*Research Policy* 41(8), 2012). The limits are real and recorded in [`notes/conways-law.md`](../../../../notes/conways-law.md): mirroring is prevalent within firms but **not universal**, and does not hold for open collaborative projects (Colfer & Baldwin, *Industrial and Corporate Change*, 2016).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (domain-aligned boundaries give the team shared vocabulary)
- **Builds:** Leadership (structural norms are inherited by everyone who touches the code afterward)

## What this skill is for

Code does not stay simple on its own. Requirements change, features accumulate, and the structure that made sense for the original problem slowly stops matching the current one. Keeping software easy to change is not a phase at the start of a project — it's a running effort against a natural drift toward tangle.

This skill fires when the user is making a structural decision *now*: whether to add an abstraction, whether to build for a requirement that hasn't arrived, where a boundary belongs, or what to do about a change that rippled much further than it should have. It gives them a vocabulary for what's actually wrong and a way to decide whether it's worth fixing.

## The core mindset (lead with this)

**Complexity is placed, not eliminated. Decide where you want to pay it.**

- Most "simplifications" are **transfers**. An indirection layer reduces dependency by increasing obscurity. Backward compatibility makes the caller's life simpler and the implementer's harder. Neither removes complexity; both move it somewhere you'd rather have it.
- **The question is never "is this complex?"** It's *"who pays, and is that the right person?"*
- **Not all complexity is worth removing.** Effort spent simplifying code that few things depend on and nobody changes is effort wasted. Inertia tells you where to spend.
- **The most reliable way to keep code flexible is to have less of it.** Flexibility built in advance for imagined requirements usually fits the real one badly and costs comprehension in the meantime.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual code, skip diagnosis when their message already says what they're deciding.**

### Step 1 — Frame the moment

One or two sentences. Name that complexity gets *placed* rather than removed, and that the useful question is where to put it. Skip if the user has a concrete decision on the table.

### Step 2 — Diagnose (one question, only if needed)

Common shapes:

- **About to add an abstraction** — and unsure whether it earns its keep.
- **Deciding whether to build flexibility** for a requirement that hasn't arrived.
- **A change rippled** much further than expected, and they want to know why.
- **Boundaries feel wrong** — unclear where a module or service should split.
- **Reviewing** something that feels over-engineered but they can't articulate why.

If ambiguous, ask **one** question — e.g. *"What's the decision in front of you — whether to add an abstraction, where to put a boundary, or why a change spread further than you expected?"*

### Step 3 — Name what kind of complexity it is

Two symptoms, from Ousterhout. Naming which one you have determines the fix, and they pull in **opposite directions** — see the transfers callout below.

**Dependency** — code relies on other code, APIs, or behaviors. Unavoidable and not bad in itself; the question is balance. Too much produces **tight coupling** and **change amplification** (one conceptual change forcing edits in many places).
*Symptom:* "I changed one thing and had to touch twelve files."
*Levers:* thoughtful API design, judicious abstraction, domain-aligned boundaries (Step 6).

**Obscurity** — important information isn't visible where it's needed, so developers can't predict how code behaves, what a change will break, or where a change belongs.
*Symptom:* "I had no idea that would happen" — action at a distance, undocumented gotchas, implicit ordering.
*Levers:* clear API contracts, standard patterns, explicit schemas, naming that carries meaning.

Ask which one the user actually has. Engineers reflexively reach for abstraction, which treats dependency — and *worsens* obscurity if that was the real problem.

### Step 4 — Check inertia before spending effort

**Inertia** is the third dimension, and the one that decides whether any of this is worth doing: *how entrenched is this software, and how likely is it to stay in use?* A service a dozen critical applications depend on has high inertia. A script one team runs quarterly does not.

Combine it with how often the code changes — the matrix is in the callout below. The short version: **high inertia and high change is where simplification pays**. Low inertia and low change can stay ugly, and choosing to leave it alone is a legitimate engineering decision rather than negligence.

**There is a second kind of inertia the code cannot show you.** A boundary that does not match how the organisation actually communicates tends to **regenerate after you move it**. Conway's observation (*How Do Committees Invent?*, Datamation, 1968) is that a system's structure copies the communication structure of the people who built it — so a module split between two teams who talk constantly will grow shortcuts back across the seam, and a module owned by two teams who never talk will keep drifting apart no matter how clean you make the interface.

The diagnostic to add here: **can this boundary actually move, or would the organisation rebuild it?** If the awkward seam sits exactly where two teams meet, refactoring is treating a symptom. That does not make the refactor wrong — sometimes a symptom is worth treating — but it changes how long you should expect the fix to hold, and it is worth saying out loud before anyone commits a quarter to it.

This is the step that keeps the rest of the skill from becoming an excuse to gold-plate everything.

### Step 5 — Apply YAGNI: don't build what you don't need

*You Ain't Gonna Need It.* Three traps, in rough order of how often they bite:

- **Premature optimization.** Performance work before there's evidence it's needed. Costs readability now for a benefit that may never materialize, and usually targets the wrong thing anyway.
- **Speculative flexibility.** Abstractions built so that *future* requirements will be easy to accommodate. This is the subtle one, because it feels responsible. In practice the imagined requirement arrives in a different shape, the abstraction fits it badly, and everyone paid comprehension cost in the meantime.
- **Features nobody asked for.** Every feature costs to build *and* to maintain forever, and you don't yet know if it's useful. Build the smallest version that tests the idea.

**Muntzing** is the discipline that follows: for everything you build, ask what is *absolutely* necessary and remove the rest. Take a piece out; if it still works, leave it out.

**On the tension with defensive programming:** [`defensive-programming`](../defensive-programming/SKILL.md) says anticipate what could go wrong; YAGNI says don't build for hypotheticals. Both are right, and the seam is this — **handle** the unexpected at runtime (validate input, fail clearly, clean up resources), but don't **architect for** the unanticipated (plugin systems, configuration hooks, generic layers for one caller). Robustness is cheap and local. Speculative structure is expensive and global.

### Step 6 — Apply least astonishment: don't surprise people

Things should behave the way whoever encounters them first expects — users *and* developers.

The developer-facing form is **implicit knowledge**: anything non-obvious someone must know to use your code correctly that isn't visible in the code itself. It reliably produces bugs and a steep learning curve. The two common violations are in the callout below.

Also: **use standard libraries and idiomatic patterns.** Writing your own square root is surprising; calling the standard one isn't. Novelty in a place where a convention exists is a cost paid by every future reader, for no benefit.

### Step 7 — Encapsulate domain knowledge

Group code by **business domain** — accounting, billing, shipping — rather than by technical layer alone. When software components map onto the business concepts they serve, changes stay focused: a billing rule change touches billing.

This produces **high cohesion** (things that change together live together) and **low coupling** (things that change independently are separated), and it's notable for being one of the few moves that reduces dependency *without* adding obscurity — because the boundaries match a model people already carry in their heads.

**Domain-driven design** is the full architectural treatment of this idea. Complete DDD is warranted only for genuinely complex domains, but the core concepts — bounded contexts, ubiquitous language, aggregates — sharpen boundary decisions well before you'd ever adopt the whole methodology.

### Step 8 — Pick one action, then close

Ask: *"What's the one change you'll make?"* Push for concreteness.

- *"Reduce complexity"* → too vague.
- *"Delete the `StrategyFactory` — there's one implementation and there has been for two years"* → the action.
- *"Move the tax rules out of `OrderService` into a `billing` module, since that's where they change from"* → the action.
- *"Leave it. It's a quarterly script nothing depends on"* → also a legitimate action.

Close in one or two sentences.

---

## Callout — The inertia × change-rate matrix

Inertia (how entrenched, how likely to stay in use) crossed with how often the code actually changes. This is a triage tool, not a maturity model.

| | **Changes often** | **Rarely changes** |
|---|---|---|
| **High inertia** (many dependents, load-bearing) | **Simplify here.** Highest return on effort — complexity is taxed on every change and every dependent. This is where the budget goes. | **Keep it clear, don't restructure.** Stable and depended-upon. Invest in documentation and explicit contracts; leave the structure alone. |
| **Low inertia** (few dependents, replaceable) | **Keep it simple, cheaply.** Churns a lot but nothing rests on it. Light-touch tidying; don't build architecture. | **Leave it alone.** Ugly is fine. Effort spent here buys nothing. |

Two things this is good for:

- **Justifying refactoring work** to a manager: *"this is in the top-left box"* is a concrete argument, where "the code is messy" is not.
- **Giving yourself permission not to fix things.** Early-career engineers tend to either gold-plate everything or nothing. This tells you which is correct where.

Inertia can also change under you — a prototype that quietly becomes load-bearing has moved boxes without anyone deciding it should. That's worth noticing before the next change lands.

---

## Callout — Complexity transfers, it doesn't disappear

Nearly every technique that "reduces complexity" moves it. Knowing the direction of transfer is what makes the decision deliberate rather than cargo-culted.

| Move | Reduces | Increases | Pays off when |
|---|---|---|---|
| Add an indirection layer between subsystems | Dependency, change amplification | Obscurity — behavior is now further from where you read it | Subsystems genuinely change independently and are owned by different people |
| Keep a change backward compatible | Complexity for **callers** | Complexity for the **implementer**, who now supports both paths | Callers are numerous, external, or hard to change |
| Add configuration instead of hardcoding | Rigidity for operators | Obscurity — actual behavior now lives outside the code | The value genuinely varies per environment (see [`configuration`](../configuration/SKILL.md)) |
| Split a service | Coupling, blast radius | Operational complexity, network failure modes, distributed debugging | The parts have genuinely different change rates or owners |
| Add an abstraction over two implementations | Duplication | Obscurity, plus a wrong abstraction if the two only *look* alike | You have two real implementations now — not one and an imagined one |

The pattern: **dependency and obscurity trade against each other.** Reducing coupling almost always means putting distance between cause and effect, and distance is obscurity. When someone proposes a simplification, the useful question is *"what does this make harder, and for whom?"* An answer of "nothing" usually means the trade hasn't been found yet.

**The main exception** is domain-aligned boundaries (Step 7), which reduce dependency without a matching obscurity cost — because the boundary matches a model people already have. That's why it's worth more than most structural moves.

**A second exception runs the other way: some of this was placed for you.** Note that three rows above turn on *who owns what* — different people, different owners. That is not incidental. The evidence for organisational shape driving system shape is stronger than most engineers realise: organisational metrics predicted failure-proneness in Windows Vista at 86% precision, beating code churn, complexity, and coverage (Nagappan, Murphy & Basili, ICSE 2008), and across matched product pairs, loosely-coupled organisations produced designs up to **eight times** more modular than tightly-coupled ones (MacCormack, Rusnak & Baldwin, *Research Policy*, 2012). Some of the complexity in front of you was transferred by an org chart before you arrived, and no amount of local cleverness removes it.

---

## Callout — Implicit knowledge: the two common violations

Implicit knowledge is what a developer must know to use your code correctly that the code itself doesn't tell them. Both of these are fixable, and both are the kind of thing found in [`code-review`](../code-review/SKILL.md).

**1. Ordering requirements** — calls must happen in a particular sequence, and nothing says so.

```
conn.configure(opts);
conn.authenticate();   // fails confusingly if configure() wasn't called first
conn.query(sql);
```

*Fixes:* make the type system enforce it (`connect()` returns an authenticated handle that is the only thing exposing `query`); collapse the sequence into one call; or fail loudly and specifically when called out of order — never silently misbehave.

**2. Hidden argument requirements** — the signature implies a wider range of valid input than the function actually accepts.

```
def schedule(delay_seconds: int)   # actually rejects negatives, and > 86400
```

*Fixes:* validate and raise a message naming the real constraint (see [`input-validation`](../input-validation/SKILL.md)); narrow the type so the constraint is unrepresentable; or document it *at the signature*, not in a wiki page.

The general test: **could a competent developer who hasn't read the implementation use this correctly on the first try?** If not, the missing knowledge is implicit, and it will produce bugs.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't recite the framework.
- **Work on their actual code.** If they paste a class or describe a module, diagnose *that* — name the dependency or obscurity you can actually see.
- **Ask "who pays?" rather than pronouncing.** The whole skill is a judgment frame; handing down a verdict skips the thinking it exists to prompt.
- **Be willing to say "leave it."** The inertia matrix exists so this is a real option. A skill that always recommends simplification is a checklist, not judgment.
- **Watch for reflexive abstraction.** If the user is reaching for a factory, a strategy pattern, or a plugin system for a single case, name the YAGNI concern directly.
- **Don't lecture the experienced.** A staff engineer asking where a bounded context should split doesn't need the YAGNI primer.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is designing or changing an **API contract** specifically. Route to [`evolvable-apis`](../evolvable-apis/SKILL.md).
- The user is changing a **database schema** or migrating data. Route to [`evolvable-data`](../evolvable-data/SKILL.md).
- The user is frustrated about accumulated mess and heading toward blaming people. Route to [`software-entropy`](../software-entropy/SKILL.md).
- The user wants to identify, prioritize, or make the case for paying down specific debt. Route to [`technical-debt`](../technical-debt/SKILL.md).
- The user is about to modify unfamiliar or untested code safely. Route to [`changing-legacy-code`](../changing-legacy-code/SKILL.md).
- The user is considering a rewrite or a wholesale replacement. Route to [`change-discipline`](../change-discipline/SKILL.md).
- The user is choosing a new technology. Route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- The user is working out what to build at all. Route to [`technical-design-process`](../technical-design-process/SKILL.md).

## Further reading

Surfaced as references — see [`READING-LIST.md`](../../../../READING-LIST.md) for tracked entries.

- ***A Philosophy of Software Design*** — John Ousterhout (2018). Source of the complexity definition and the dependency/obscurity split. Short, opinionated, and the most direct treatment of this material available.
- ***Building Evolutionary Architectures*** — Neal Ford, Rebecca Parsons, Patrick Kua (O'Reilly, 2017). Architecture designed for continuous change, including fitness functions for guarding structural properties over time.
- ***Domain-Driven Design*** — Eric Evans (2003), and ***Implementing Domain-Driven Design*** — Vaughn Vernon (2013). The full treatment of Step 7; Vernon is the more practical entry point.
- **"*Simple Made Easy*"** — Rich Hickey (2011), https://www.youtube.com/watch?v=SxdOUGdseq4. The distinction between *simple* (not intertwined — an objective property) and *easy* (familiar, near at hand — relative to you). Directly sharpens what this skill means by complexity.
- ***Elements of Clojure*** — Zachary Tellman (2019). Unusually deep on naming, indirection, and abstraction as complexity-management tools; valuable well beyond Clojure.
