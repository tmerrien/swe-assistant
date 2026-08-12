---
name: interface-decisions
description: Use when the user is building or changing something a person will look at and use — a screen, form, flow, dashboard, settings page, onboarding sequence, admin panel, or any user-facing surface. Triggers include planning UI work as a phase that happens after the logic is done, asking how to lay out a screen or structure a flow, saying the design will be "polished later" or handed to a designer at the end, asking whether a feature needs a mockup, wondering why a working feature confuses users, or choosing an icon or visual metaphor. Establishes the frame the rest of the interface skills build on — the interface is where usability is decided rather than where it is decorated, usability is the floor that aesthetics and distinctiveness sit above, and discovery is cheapest at the sketch. Also carries the validity caution that attractive prototypes attract more forgiving feedback. For contested calls like minimal versus rich, route to interface-tradeoffs. For what to emphasize on a crowded screen, route to rationing-attention. For button labels, errors, and empty states, route to interface-copy. Do not trigger for backend-only work with no human-facing surface, or for visual brand and identity work.
---

# interface-decisions

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principles 2 (*Work on UX and UI simultaneously*), 3 (*UI makes or breaks usability*), 7 (*Visual metaphors communicate the fastest*), and 8 (*Attractive products are more usable*), read against this repository's existing engineering material.

The claim that the interface layer is within software engineering rather than adjacent to it is a scope decision recorded in [`LIMITATIONS.md`](../../../../docs/LIMITATIONS.md) Section 8.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (the interface is a design surface with its own failure modes)
- **Builds:** Leadership (engineers who own the user-facing outcome rather than handing it off)

## What this skill is for

Engineers routinely treat the interface as the last layer — build the logic, get it working, then make it look acceptable. That sequencing is where a large share of usability failures are manufactured, because by the time the interface is drawn the structure it has to express is already fixed.

This skill fires when someone is about to build or change a user-facing surface. Its job is to set the frame before the specific decisions start.

## The core mindset (lead with this)

**The interface is where usability is decided, not where it is decorated.**

- A feature that works correctly and cannot be operated has not shipped.
- **Usability is the floor.** Aesthetics, brand, distinctiveness, and personality are all real considerations, and every one of them sits *above* the floor. A beautiful thing nobody can use is not a trade-off; it is a failure.
- **Discovery is cheapest at the sketch.** You find out the flow is wrong by drawing it in ten minutes, not by building it in two weeks. This is the same economics as a design doc or a spike — the interface is simply another place to be wrong cheaply.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): one question per turn, work on the user's actual surface if they describe one, route to the more specific skill when one fits.

### Step 1 — Diagnose

If the user described a specific screen or flow, work on that. Otherwise ask **one** question:

- *"What is the user trying to accomplish on this surface, and what is the smallest thing that would let them do it?"*

Skip if the first message already answers it.

### Step 2 — Check the sequencing

If the plan is *build it, then design it*, say so plainly and give the reason (below). This is usually the highest-leverage thing in the conversation and it is easy to miss because nothing is visibly broken yet.

### Step 3 — Apply what fits

Draw from the sections below. Do not walk all of them.

### Step 4 — Route

Most specific interface questions belong to a sibling skill. Route rather than half-answering.

### Step 5 — Close

One concrete next step. Usually: *sketch it before you build it, and show the sketch to one person who did not design it.*

---

## Interface and behaviour are worked together, not in sequence

The common shape — settle the behaviour, then draw the interface — treats the interface as an output of the design. It is more often an *input*, because drawing it is what reveals whether the behaviour makes sense.

- **The flow you cannot draw simply is usually not simple.** A screen that needs six explanatory sentences is reporting a structural problem, not a copywriting problem.
- **Sketching is a research method, not a production step.** Its value is the questions it surfaces while it is cheap to answer them.
- **Phase-gating design behind implementation removes the feedback.** By the time the interface is drawn, the data model, the API shape, and the state machine have all been fixed, and the interface has to express whatever they permit.

This is the same argument this repository already makes in other domains — write the design doc before the code ([`design-doc`](../design-doc/SKILL.md)), spike before committing ([`technical-design-process`](../technical-design-process/SKILL.md)), prototype before the migration ([`evolvable-data`](../evolvable-data/SKILL.md)). The interface is not an exception to it.

**If a designer is involved**, this argues for working alongside them from the start rather than receiving finished mockups. The engineer knows what is expensive; the designer knows what is confusing. Both facts are needed before either decision is locked.

## Usability is the floor

Everything else in interface work is a decision made *above* a floor that has to hold first.

- Can the user tell what this screen is for?
- Can they tell what to do next?
- Can they tell what happened after they did it?
- Can they recover when they get it wrong?

If any answer is no, that is the work. Distinctiveness, richness, minimalism, and brand personality are all arguments about the space above this line — see [`interface-tradeoffs`](../interface-tradeoffs/SKILL.md) — and none of them is a defence for failing it.

## Visual metaphors, and their one real constraint

Icons and visual metaphors communicate faster than text, which is why they are worth using — a recognised symbol is understood before a label is read.

The constraint is that **a metaphor only works if the referent is actually shared with your users.** The floppy disk survives because it became its own convention, not because anyone recognises the object. A metaphor drawn from your own domain knowledge, your own generation, or your own culture may communicate nothing to the person using it.

**The practical test:** could someone outside your team name what this icon does without a tooltip? If the answer requires a tooltip, the tooltip is doing the work and the icon is decoration. Pair icons with labels unless the symbol is genuinely conventional.

## Callout — Attractive prototypes get more forgiving feedback

The **aesthetic-usability effect**: people judge attractive things as more usable, somewhat independently of whether they are. This has a direct methodological consequence that matters more than the design advice:

**It contaminates your usability testing.** A polished prototype will receive kinder feedback than a rough one showing the same flow, and the difference is not information about the flow. Two working rules:

- **Test structure with low-fidelity artifacts.** Sketches and wireframes get you honest reactions to the flow, because there is no polish to be charmed by.
- **Be suspicious of positive feedback on a beautiful prototype.** Ask what the user would do next rather than whether they like it. Observed behaviour survives the effect; stated preference does not.

The inverse also holds and costs teams real work: a rough prototype can attract criticism aimed at its roughness rather than its structure. Say what you are testing before you show it.

See [`technical-design-process`](../technical-design-process/SKILL.md) for prototype discipline generally.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.**
- **Work on their actual screen or flow** if they describe one. Do not deliver the general lecture when there is a specific surface on the table.
- **Name the sequencing problem early** if the plan defers interface work. It gets more expensive every day it goes unsaid.
- **Route aggressively.** This skill sets the frame; the siblings hold the detail.
- **Do not produce the design for them.** Sketch prompts, questions, and constraints — not a finished layout. See Design Principle 3.1.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The decision is a **contested trade-off** — minimal versus rich, familiar versus distinctive, consistent with the design system versus differentiated. Route to [`interface-tradeoffs`](../interface-tradeoffs/SKILL.md).
- The question is **what to emphasize** on a crowded surface. Route to [`rationing-attention`](../rationing-attention/SKILL.md).
- The question is about **wording** — labels, errors, empty states, confirmations. Route to [`interface-copy`](../interface-copy/SKILL.md).
- The design may be **manipulative or deceptive**. Route to [`design-ethics`](../design-ethics/SKILL.md).
- The user is still working out **what problem to solve**. Route to [`technical-design-process`](../technical-design-process/SKILL.md).
- The work is **backend-only** with no human-facing surface. Skip. For operator-facing tools specifically, route to [`operational-tools`](../operational-tools/SKILL.md).
- The user is doing **brand or visual identity** work — logos, typography systems, colour palettes as identity. Out of scope; see [`LIMITATIONS.md`](../../../../docs/LIMITATIONS.md) Section 8.
