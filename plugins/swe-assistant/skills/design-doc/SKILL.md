---
name: design-doc
description: Use when the user is about to write, currently writing, or reviewing a technical design document — also called an RFC (Request for Comments), ADR (Architecture Decision Record), tech spec, or one-pager depending on the team. Triggers include phrases like "I need to write a design doc", "drafting an RFC", "asked to write up the design before building", "reviewing this design doc", "got design feedback I don't know what to do with", "what should go in a design doc", "should I write a design doc for this", or asking how to structure their thinking before building something non-trivial. Walks through what a design doc is and isn't, when to write one, the standard structure (context, problem, goals, options considered, recommendation, trade-offs, plan), how to invite useful feedback, and the common pitfalls (writing the solution before the problem, single-option docs, no clear ask, burying trade-offs). Useful at any stage from Contributor onward; central to the Owner stage. Do not trigger for general writing help, code documentation, or non-technical documents.
---

# design-doc

## Source

Informed by *The Missing Readme*, Chapter 1, "The Journey Ahead" (Owner stage), plus widely-shared industry practice (Google design doc culture, Amazon 6-pagers, ADR conventions). The book mentions writing design docs as part of the Owner stage; this skill expands on it because design docs are one of the highest-leverage written artifacts in engineering and the format is genuinely teachable.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (showing you understand the trade-offs)
- **Builds:** Leadership (driving alignment so the project can move)

## What this skill is for

A design doc is **the artifact of thinking before building.** It's where you and your reviewers agree on what you're going to build and why, *before* you spend two weeks implementing it.

This skill fires whenever a user is in (or thinking about being in) that situation: writing a design doc, reviewing someone else's, deciding whether one is even needed, or stuck in the middle of drafting one.

## The core mindset (lead with this)

**The doc is the artifact of your thinking — not paperwork.**

- The biggest reward isn't the doc itself, it's that *writing it forces you to think the design through.* Half the bugs in your eventual code get killed in the design doc, before they exist.
- A good design doc is **shorter than you think and more honest than feels comfortable.** Name the trade-offs, name the things you're unsure about, name the option you didn't pick and why.
- The audience is your team and your future self. Both of them are smart but busy. Optimize for *easy to skim*, not *exhaustive.*

## How to run — diagnose the mode first

This skill serves two very different users and *must distinguish between them* before doing anything else. The fix for *"this skill was underwhelming for a real ADR"* is in this section.

The expertise-reversal effect (Kalyuga, 2007) is robust empirical research showing that instructional scaffolding which helps novices actively *hurts* experts. The senior engineer writing an ADR for a decision they've largely made does not need to be walked through "what's a design doc?" — they need a sparring partner on the specific trade-offs. The junior writing their first design doc does need the scaffold. Diagnose which one you have before you respond.

### Step 1 — Diagnose with one question

If the user's first message doesn't make it obvious, ask **one** question:

- *"Is this an ADR / spec to **align reviewers on a decision you've already made**, or are you using the doc to **think through a decision you haven't made yet**?"*

Two modes, very different responses:

**Mode A: Alignment doc (decision largely made).** Typical user: a senior or mid-level engineer who's done the thinking, often facing an ADR template they have to populate. They want a sparring partner on the trade-offs, not a tutorial.

- Skip the template walkthrough. Don't lecture about structure.
- Ask: *"What's the decision, what are you considering, and what's the part you're least sure about?"* — get to the substance.
- Engage with the **trade-offs** they name. Push on: *"What breaks if you're wrong about X?"*, *"What's the smallest reversible version of this?"*, *"What's the unstated assumption?"*
- Offer your read on what's strong and weak in their reasoning. Be willing to disagree — a sparring partner that only nods is useless.
- Use the structure, template, and pitfalls sections below as *reference material* you draw on selectively, not as a script.

**Mode B: Thinking doc (decision not yet made, or first design doc).** Typical user: a junior engineer being asked to write one for the first time, or anyone working through a genuinely open design question.

- Walk through the structure. The template below is the scaffold.
- Lead with the *Problem* section (most stuck-on-design-doc moments are people who jumped to *Solution* before they understood the *Problem*).
- Push for at least two alternatives (Step 4 of the template). Single-option docs come from incomplete thinking.
- Take your time on the diagnostic — multiple turns, one question at a time.

If you can't tell from one question, default to **Mode A** for anyone who shows comfort with technical decisions in their first message, **Mode B** for anyone who asks *"what should I write?"* or *"what goes in a design doc?"*.

---

## When to write a design doc (and when not to)

**Write one when:**
- The work touches more than one component or service.
- There are reasonable alternative approaches and the choice isn't obvious.
- The change affects other people's code, on-call life, or downstream systems.
- You'll spend more than ~3 days building it.
- Reviewers would benefit from seeing the *why* before the *what*.

**Skip it (or just write a paragraph in the PR description) when:**
- The change is local, small, and reversible.
- The design is a tiny variation on an established pattern in the codebase.
- A spike / prototype would teach you more than a doc would (in which case: spike first, *then* write the doc).

When in doubt, write it. Even a one-pager pays for itself.

## The standard structure

Length expectations: **1–3 pages for most things; up to 5 for a meaningful project.** Past that, almost no one reads the whole thing.

```
# [Title — what this is, in plain English]
Author: [your name]   Status: Draft / In Review / Approved / Implemented
Date: [today]   Reviewers: [names]   Stakeholders: [names]

## Context
[2–4 sentences. Why are we even talking about this? What changed, what's the problem
from the team's or business's perspective? Assume the reader knows the codebase but
not necessarily this corner of it.]

## Problem
[Specific. Not "improve X" — "Today, the X service has Y behavior, which causes Z
for users. We need it to do W instead." If you can't describe the problem in two
or three sentences, you don't understand it well enough to design yet.]

## Goals
- [What this work is trying to achieve. Outcomes, not activities.]
- [2–4 bullets, ranked by importance.]

## Non-goals
- [Equally important. What this work is *not* trying to do, even though
  someone might assume it is.]
- [Naming non-goals prevents scope creep and confusing reviewers.]

## Proposed solution
[The actual design. Diagrams welcome. Code snippets welcome where they clarify.
Walk through how the proposed thing works — the data flow, the API surface,
the failure modes, the rollout plan.]

## Alternatives considered
[**This section is what makes the doc credible.** For each plausible alternative:]

### Alternative A: [name]
- Approach: [one paragraph]
- Pros: [bullets]
- Cons: [bullets]
- **Why not chosen:** [the actual reason]

### Alternative B: [name]
[same shape]

[Naming 2–3 alternatives — even ones you ruled out quickly — shows you thought
about it. A doc with one option looks like a foregone conclusion.]

## Trade-offs of the proposed solution
[Be honest. Every design has costs. Name them up front so reviewers don't
have to dig for them. This builds trust.]

## Risks and open questions
- [What could go wrong, and what's the mitigation]
- [What you're explicitly unsure about and want input on]

## Plan
- [Milestones with rough dates. Don't over-precisify; give reviewers a sense of shape.]
- [Who's doing what, if not just you.]

## Appendix (optional)
[Things that didn't fit but are useful — benchmarks, prior discussions, links to
related docs.]
```

## Writing it well

- **Lead with the problem, not the solution.** A reviewer should understand *why* before they encounter the *what*. Solutions out of context are unreviewable.
- **Be specific about what you want from reviewers.** End the intro section with: *"What I most need feedback on: X, Y, Z."* Otherwise you'll get random comments and miss the comments you needed.
- **Diagrams are worth their weight.** A simple boxes-and-arrows sketch saves three paragraphs. Don't over-engineer them — pen-and-paper photo or a `mermaid` diagram in markdown is fine.
- **Write in declarative voice, not hedged.** *"The service will accept requests at /v2/foo."* not *"I think we could maybe have the service accept..."* You can hedge in the *Open questions* section; the body should be confident.
- **Cut everything you can.** Reread the draft and delete anything that doesn't change a reviewer's mind or affect the design.

## Inviting useful feedback

- **Share early, share twice.** First share at "rough draft, looking for direction" stage. Second share at "I think this is right, looking for holes." Most people skip step one and miss the most valuable feedback.
- **Tag specific reviewers and tell them what you want.** *"@Alice, I'd love your eye on the data model section. @Bob, the rollout plan is the part I'm least sure about."* Random "any thoughts?" gets random thoughts.
- **Be explicit about timeline.** *"Hoping for feedback by Wednesday so I can start building Thursday."* Otherwise it sits.
- **Reply to every comment.** Same rule as code review — every comment deserves a reply, even if it's *"good catch, updated."* Unresolved comments make reviewers think you're ignoring them.

## Common pitfalls

- **Writing the solution before the problem.** The doc reads like a sales pitch and reviewers can't engage with it.
- **Single-option docs.** Looks like you didn't think hard. Even bad alternatives strengthen the doc when you name why they're bad.
- **No clear ask.** Reviewers don't know what kind of feedback you want, so you get either nothing or unhelpful nits.
- **Burying the trade-offs at the end** (or worse, not naming them). Reviewers will find them anyway and trust you less for not surfacing them.
- **Over-length.** A 12-page design doc that nobody reads is worse than a 2-page one that everyone reads.
- **Writing it after the fact.** Then it's documentation, not a design doc. Useful, but it doesn't get you the thinking-out-loud benefit.
- **Not updating the status.** A doc that says "Draft" but is being implemented confuses everyone. Promote it to "Approved" when alignment is there.

## A note on team variants

Different teams use different names and conventions:

- **Design Doc / Tech Spec** — the most common form, what this skill describes.
- **RFC (Request for Comments)** — same shape, lighter weight, more conversation-oriented. Common at IETF, Rust, and some companies.
- **ADR (Architecture Decision Record)** — much shorter, decision-focused. Captures *one decision* and the trade-offs that led to it. Useful as a complement to design docs, not a replacement.
- **6-pager (Amazon-style)** — narrative prose, no bullets, presented before discussion in a meeting. Specific to Amazon and a few others.

If your team has a template, use it. The structure above is a sensible default if there isn't one — adapt to local conventions where they differ.

## Output style

- **Always diagnose the mode first** (see *How to run — diagnose the mode first* above). Skipping the diagnosis is the failure mode this skill exists to avoid.
- **In Mode A (alignment doc, decision made):** engage on substance, not structure. Be a sparring partner, not a tutor. Be willing to push back on the user's reasoning. Don't lecture about the template.
- **In Mode B (thinking doc):** walk the structure. Often they're stuck on the *Problem* section because they jumped to *Solution* — gently push them back.
- If the user is **stuck mid-draft**, ask which section they're on and what's blocking them. Don't lecture about the whole structure.
- If the user is **reviewing someone else's**, route the response style toward [`code-review`](../code-review/SKILL.md) tone (questions, not commands; suggest don't dictate; label severity).
- If the user got **feedback they don't understand**, ask them to share the specific comment. Help them parse it before deciding how to respond.

## When NOT to use this skill

- The user is asking how to write *general* documentation (READMEs, user guides, API docs). Skip — different shape entirely.
- The user is asking about *code* documentation (docstrings, inline comments). Skip.
- The user wants help writing prose for a non-technical document (email, blog post, status update). Skip.
- The user is reviewing a *PR* (code change, not design). Route to [`code-review`](../code-review/SKILL.md).
