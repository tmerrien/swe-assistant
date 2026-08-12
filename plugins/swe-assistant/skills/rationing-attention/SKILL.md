---
name: rationing-attention
description: Use when the user is deciding what to emphasize and what to let recede, in any medium. Triggers include a screen or dashboard where everything looks equally important, a page with five competing calls to action, choosing log levels or deciding what to log, tuning an alert set that pages too often, ordering sections in a design doc or README, writing a status update or commit subject, or saying things like "there's too much on this page", "how do I make this stand out", "which of these should be primary", or "the important thing is getting lost". Teaches emphasis as a fixed budget rather than a property that can be added — attention is finite, contrast is zero-sum, and something must recede for anything to stand out. Grounded in Sweller's cognitive load theory, the von Restorff isolation effect, and serial-position effects, with the ordering and load-budgeting rules that follow from them. Applies to interfaces and equally to logs, alerts, dashboards, and documents. Do not trigger for the wording of a specific string, which belongs to interface-copy, or for contested style debates like minimal versus rich, which belong to interface-tradeoffs.
---

# rationing-attention

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principles 6, 9 (*People remember the unusual*), 10 (*First and last items are remembered most*), 11 (*Less is more*), and 12 (*Less is a bore*), which are five applications of one constraint.

The constraint itself is **Sweller's cognitive load theory** (1988), already load-bearing in this repository for a different purpose — see [`THEORETICAL-FOUNDATIONS.md`](../../../../docs/THEORETICAL-FOUNDATIONS.md) Section 6, where it grounds skill body structure and selective surfacing. Also draws on the **von Restorff isolation effect** (1933) and **serial-position effects** (Ebbinghaus; Murdock, 1962).

This skill is deliberately **not interface-specific**. The clustering that produced it was noticed because the same rule was already operating in this repository's logging, alerting, and document guidance without having been named.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (log levels, alert design, and dashboard design are all instances)
- **Builds:** Leadership (the ability to say what matters most is what makes someone worth reading)

## What this skill is for

The recurring situation: a surface — a screen, a dashboard, an alert set, a document — where everything on it is genuinely important, and the author has therefore emphasized all of it. The result is that none of it registers.

This skill fires at that moment. Its job is to convert *what should I highlight?* into *what am I willing to let recede?*, which is the question that actually has an answer.

## The core mindset (lead with this)

**Emphasis is a budget, and forgetting is how you fund it.**

- Attention is finite. Every element that draws it takes it from something else. This is arithmetic, not taste.
- **Contrast is zero-sum.** Emphasis works by difference — bold text among plain text, one red button among grey ones, one ERROR among INFO. Bold everything and you have merely changed the typeface.
- The useful question is never *what deserves emphasis* — everything does, which is why the author is stuck. It is **what am I willing to lose?** That question is answerable.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Diagnose

Work on their actual surface if they showed one. Otherwise ask **one** question:

- *"If the reader took exactly one thing away from this, what must it be?"*

The answer is the budget. Everything else is funded by it.

### Step 2 — Name what recedes

Push for this explicitly. Most people can name what matters; far fewer will commit to what doesn't. The commitment is the work.

### Step 3 — Apply the relevant rules

Use the sections below selectively based on their medium.

### Step 4 — Close

One concrete cut or demotion, not a redesign.

---

## The rules that follow from the constraint

### Isolation — distinctiveness is rationed, not free

The **von Restorff effect**: an item that differs from its neighbours is disproportionately remembered. The operational consequence is the part people skip — **the effect is produced by the neighbours.** One distinct thing among twenty uniform ones is memorable. Twenty distinct things are twenty uniform things.

- Pick **one** primary action per screen. Not one per section, per screen.
- If three things are highlighted, you have chosen not to highlight anything.
- The same rule governs log levels: if everything is `WARN`, `WARN` means nothing. See [`logging`](../logging/SKILL.md).
- And alerting: an alert set that pages constantly has trained its recipients to ignore it, which is the failure mode, not a side effect of it. See [`on-call-shift`](../on-call-shift/SKILL.md).

### Position — order is a lever you already have

**Serial-position effects**: items at the beginning and end of a sequence are recalled better than items in the middle. The middle is where things go to be forgotten.

- Put what must survive at an **end**. Not in the middle, however logical the middle feels.
- The last item is often the strongest position for what you want acted on; the first for what you want understood.
- Applies to: menu and nav ordering, form field order, a design doc's section order, a status update's bullets, a commit message's first line, an incident timeline's summary.
- **Corollary worth stating:** if a list has a middle, that middle is a decision you are making by default. Decide it deliberately or shorten the list.

### Load — budget by zone, not uniformly

Sweller's distinction between load intrinsic to a task and load imposed by how it is presented gives the allocation rule: **reduce load where the task is already demanding; permit richness where it is not.**

- A checkout, a consent screen, an incident dashboard, a destructive-action confirmation — strip these. The user's capacity is already committed.
- A landing page, a browsing surface, an empty state, a settings overview — these can carry more, because the task is light.
- The mistake is applying one density everywhere and calling it consistency.

### The ceiling — MAYA

Raymond Loewy's **Most Advanced Yet Acceptable**: push distinctiveness up to the limit of what the audience will accept, and no further. Novelty past that line stops reading as *notable* and starts reading as *wrong*.

Practically, this bounds the isolation rule. Being different is a purchase, not a free good — the same logic [`choose-boring-technology`](../choose-boring-technology/SKILL.md) applies to novel technology, applied to attention. Spend the token where it earns something.

## Callout — This is not a UX rule

The constraint is cognitive, so it holds wherever a human reads output under limited attention. This repository was already applying it in four places before it was named:

| Surface | The same rule |
|---|---|
| **Log levels** | If everything is elevated, elevation carries no signal ([`logging`](../logging/SKILL.md)) |
| **Alerts** | A pager that fires constantly has trained its audience to ignore it ([`on-call-shift`](../on-call-shift/SKILL.md)) |
| **Design doc introductions** | Most readers read only this; it has one job ([`design-doc`](../design-doc/SKILL.md)) |
| **Commit subjects** | One line, first position, carries the whole message ([`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md)) |

If the user's situation is one of these, route there for the medium-specific practice and use this skill for the underlying decision.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** The diagnostic question does most of the work; ask it and wait.
- **Push for the demotion, not the promotion.** *"What are you willing to let recede?"* is the question people avoid, and it is the one that resolves the situation.
- **Work in their medium.** A dashboard, a log scheme, and a README are the same problem, but the vocabulary should be theirs.
- **Do not redesign it for them.** Name the budget and the rule; let them make the cut. See Design Principle 3.1.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The question is **the wording of a specific string** — a label, an error, an empty state. Route to [`interface-copy`](../interface-copy/SKILL.md).
- The question is a **contested style debate** — minimal versus rich, familiar versus distinctive. Route to [`interface-tradeoffs`](../interface-tradeoffs/SKILL.md).
- The user is asking **whether an interface is needed at all**, or how to sequence interface work. Route to [`interface-decisions`](../interface-decisions/SKILL.md).
- The surface is a **log, alert, or dashboard** and the user wants the medium-specific practice rather than the emphasis decision. Route to [`logging`](../logging/SKILL.md), [`on-call-shift`](../on-call-shift/SKILL.md), or [`metrics`](../metrics/SKILL.md).
- The user is in an **active incident** and asking what to look at. Route to [`incident-response`](../incident-response/SKILL.md).
