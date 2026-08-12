---
name: design-doc
description: Use when the user is about to write, is writing, or is reviewing a technical design document — also called an RFC, ADR, tech spec, or one-pager depending on the team. Triggers include "I need to write a design doc", "drafting an RFC", "asked to write up the design before building", "what should go in a design doc", "should I write one for this", or "our design docs go stale". Covers when a change is consequential enough to warrant a doc, the standard structure, writing for your audience, inviting feedback, and keeping the document alive once implementation starts. For working out WHAT to build — problem definition, research, prototyping, thinking time — route to technical-design-process. Do not trigger for general writing help or code documentation.
---

# design-doc

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 10, "Technical Design Process"** — the *Writing Design Documents* section. The threshold for when a change warrants a design document, the write-for-your-audience discipline, and the keep-it-current material (including the two abandonment pitfalls and version-controlling the document alongside the code) come from there. Chapter 1, "The Journey Ahead" also frames design docs as Owner-stage work.

The document template — Introduction through Appendix, including the *Design and Architecture* subsections — is the structure that chapter proposes, with per-section guidance drawn from it.

Supplemented by widely-shared industry practice (Google design doc culture, Amazon 6-pagers, ADR conventions) for the review mechanics and the non-goals convention, which the book does not prescribe in detail. Public proposal archives — Python PEPs, Kafka KIPs, Rust RFCs — are surfaced by the chapter as worked examples.

One section, *"Often, nobody reads it. Write it anyway,"* reflects the maintainer's own professional experience and is labeled as such in place.

For the *process* that produces the document — defining the problem, research, prototyping, protecting thinking time — see [`technical-design-process`](../technical-design-process/SKILL.md), which folds the rest of Chapter 10.

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

**Document consequential changes.** *The Missing Readme* (Ch. 10) gives three tests — any one of them means a design document is warranted:

- The project will require **at least a month** of engineering work.
- The change will have **long-lasting implications** for extending and maintaining the software.
- The change will **significantly impact other teams**.

Those thresholds describe a *formal* design document — the kind that gets circulated to security, operations, and architects. Common industry practice sets a lower bar for a *lightweight* one, and both are useful. A pragmatic reading:

**Write a full design doc when** any of the book's three tests fires.

**Write a one-pager or ADR when:**
- The work touches more than one component or service.
- There are reasonable alternative approaches and the choice isn't obvious.
- The change affects other people's code, on-call life, or downstream systems.
- Reviewers would benefit from seeing the *why* before the *what*.

**Skip it (or just write a paragraph in the PR description) when:**
- The change is local, small, and reversible.
- The design is a tiny variation on an established pattern in the codebase.
- A spike / prototype would teach you more than a doc would (in which case: spike first, *then* write the doc — see [`technical-design-process`](../technical-design-process/SKILL.md)).

The distinction that matters is **consequence, not calendar time.** A three-day change that locks in a data model for five years deserves a document; a month of mechanical migration work following an established pattern may not.

When in doubt, write something. Even a one-pager pays for itself.

## Know why you're writing

Before drafting, be explicit about two things:

- **The goal.** Are you seeking a decision, gathering feedback on an open question, recording a decision already made, or informing people who'll be affected? Each produces a different document.
- **The audience.** Your team already knows the codebase. Security and adjacent teams don't. Architects want the trade-offs, not the implementation detail. Write for whoever actually has to act on it.

**On learning to write:** write clearly, then **reread from your target audience's perspective**. It does not matter whether *you* find it clear — it matters whether *they* do. Be concise. And read what others have written, deliberately: ask how you would edit it, what's extra, what's missing. Editing other people's documents is the fastest way to improve your own.

Technical writing is a learnable skill with a small canon worth knowing: Strunk & White's *The Elements of Style* and Zinsser's *On Writing Well* for prose generally, and Paul Graham's short essays *"How to Write Usefully"* (http://paulgraham.com/useful.html) and *"Write Like You Talk"* (http://paulgraham.com/talk.html) — the latter being an unusually good corrective for engineers whose documents come out stiff. Full entries in [`READING-LIST.md`](../../../../READING-LIST.md).

## The standard structure

**Use your team's template if they have one.** The structure below is the default when there isn't one, and it is a *base proposal* — sections get merged, dropped, or added depending on the change. A pure backend change has no UI/UX section; a library has no persistence layer. Adapt rather than padding empty headings.

**Length:** a full document for a consequential change typically runs several pages — the *Design and Architecture* section alone is usually the bulk. For the lighter one-pager or ADR case (see *When to write* above), keep the same section order and collapse to Introduction, Motivation, Potential Solutions, Proposed Solution, and Unresolved Questions.

At a minimum, a design document should cover **the current design, the motivation for changing it, the potential solutions, and the proposed solution** — with enough detail on the proposal to be actionable: diagrams, algorithms, public APIs, schemas, trade-offs against the alternatives, assumptions, and dependencies.

```
# [Title — what this is, in plain English]
Author: [your name]   Status: Draft / In Review / Approved / Implemented
Date: [today]   Reviewers: [names]   Stakeholders: [names]

## Introduction
[Introduce the problem and say why it's worth solving. One paragraph summarizing
the proposed change. Then a short reading guide pointing different audiences at the
sections they care about — security engineers here, operations there, data
scientists elsewhere. Most readers will only read this section; make it stand alone.]

## Current State and Context
[Describe the architecture being modified. Define terminology, and explain what
systems with nonobvious names actually do. How is the issue being addressed today?
Are there workarounds in play, and what do they cost?]

## Motivation for Change
[Teams always have more projects than capacity. Why this problem, and why now?
Describe the benefits and tie them to business needs. Be careful not to overpromise —
an oversold doc is a credibility debt you pay later.]

## Requirements
[What an acceptable solution must satisfy. Usually broken out:]

### User-facing requirements
[Usually the bulk. What the change means from the user's perspective.]

### Technical requirements
[Hard constraints — typically interoperability concerns or internal guidelines.
Service level objectives belong here.]

### Security and compliance requirements
[Broken out separately — even though they could be filed above — specifically so
security gets explicitly discussed rather than assumed. Data retention and access
policies usually live here.]

### Other
[Critical deadlines, budgets, and anything else that constrains the solution.]

## Potential Solutions
[Reasonable alternative approaches, and why you dismissed each. This section is as
much a tool for you as for the reader: it forces you past your first idea. It also
preempts "why not do X?" comments — and if you dismissed something for a bad reason,
this is where a reviewer catches it.]

## Proposed Solution
[The approach you settled on, in more detail than the Introduction. Diagrams that
highlight what changes. If the proposal has multiple phases, explain how the design
evolves from phase to phase — here and in every section below.]

## Design and Architecture
[Normally the bulk of the document. All the technical detail worth discussing: key
libraries and frameworks, implementation patterns, and any departure from common
company practice.]

### System Diagram
[Main components and how they interact. Highlight new and changed components, or
give before/after diagrams. Accompany the diagram with prose walking the reader
through the changes — a diagram alone is not an explanation.]

### UI/UX Changes
[Mock-ups, used to walk through a user's activity flow. No visual component? This
section covers developer experience instead — how the library feels to call, how the
CLI feels to use. The goal is to think through the experience of whoever interacts
with your change.

This section is routinely treated as optional decoration and is frequently the one
that would have caught the real problem. A flow you cannot sketch simply is usually
not simple, and finding that out here costs minutes rather than weeks. See
`interface-decisions`.]

### Code Changes
[The implementation plan. What existing code changes, how, and when. Any new
abstractions being introduced.]

### API Changes
[Changes to existing APIs and any new ones. Backward and forward compatibility, and
versioning. Include error handling: what the API returns for malformed input,
constraint violations, and unexpected internal errors.]

### Persistence Layer Changes
[Storage technologies introduced or modified — databases, file and filesystem
layouts, search indices, data transformation pipelines. All schema changes, with a
note on backward compatibility for each.]

## Test Plan
[How you'll verify the change — not every test enumerated in advance. Cover sourcing
or generating test data, the use cases that must be covered, the libraries and
strategies you expect to lean on, and how you'll validate the security requirements.]

## Rollout Plan
[How you'll avoid complicated deployment-ordering requirements. Which feature flags
control the rollout, and which deployment patterns apply. Critically: how you'd find
out the change isn't working, and how you'd roll back.]

## Unresolved Questions
[Pressing questions the design hasn't answered. This is how you solicit input, and
how you state your known unknowns. A doc with an empty section here is usually
hiding something.]

## Appendix
[Extra detail of interest, references to related work, further reading.]
```

**A common addition from practice:** many teams add a **Non-goals** subsection under *Requirements* — what this work explicitly is *not* trying to do, even though a reader might assume it is. It costs two lines and prevents a surprising amount of scope confusion.

Cross-references for the sections that have their own skills: [`writing-tests`](../writing-tests/SKILL.md) for the test plan, [`progressive-rollout`](../progressive-rollout/SKILL.md) and [`deployment-discipline`](../deployment-discipline/SKILL.md) for the rollout plan, [`input-validation`](../input-validation/SKILL.md) for API error handling, and [`dependency-management`](../dependency-management/SKILL.md) for the dependencies you're taking on.

## Learn from public design documents

Some engineering communities conduct design in the open, which means there are large public archives of real proposals — including the arguments, the objections, and the revisions. Reading a few is the fastest way to calibrate depth and tone:

- **Python Enhancement Proposals (PEPs)** — https://peps.python.org/. Decades of language design, with an unusually disciplined house style.
- **Kafka Improvement Proposals (KIPs)** — https://cwiki.apache.org/confluence/display/KAFKA/Kafka+Improvement+Proposals. Distributed-systems proposals with heavy attention to compatibility and migration.
- **Rust RFCs** — https://github.com/rust-lang/rfcs. Notable for explicit *Drawbacks*, *Rationale and alternatives*, and *Unresolved questions* sections in every RFC.

Read the discussion threads too, not just the accepted text. The objections a proposal survived tell you more about what makes a document persuasive than the final version does.

For a company-scale worked example with a reusable template, WePay published both an account of their design-doc practice (https://wecode.wepay.com/posts/effective-software-design-documents) and the template itself (https://github.com/wepay/design_doc_template).

For *reviewing* someone else's design rather than writing your own, see [`technical-design-process`](../technical-design-process/SKILL.md) — contributing to others' designs, and running the discussions where that happens, live there.

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

## Callout — Often, nobody reads it. Write it anyway.

*This section reflects the maintainer's own professional experience rather than the cited literature, and is labeled as such. It is offered as a corrective to the (accurate but incomplete) picture the rest of this skill paints.*

In practice — and especially at startups — you should expect that **most of your design documents will go largely unread.** Reviewers skim the introduction. Stakeholders read the section they were pointed at, if that. Some documents get no comments at all.

This is worth knowing up front, because the alternative is discovering it after your third carefully-structured document lands with a thud and concluding the whole practice is theatre. It isn't. Three things remain true:

- **The thinking is the deliverable.** Most of the value is extracted while writing, before anyone reads a word. The unknowns you surface, the alternative you talk yourself out of, the API error case you notice while documenting it — those pay for the document by themselves.
- **Write it as if it will be read.** The discipline of writing for a real audience is what forces the clarity. A document written carelessly because "no one will read it anyway" loses the thinking benefit too — the sloppiness goes all the way down.
- **It becomes valuable later, asymmetrically.** Unread on Tuesday, decisive six months later when someone asks why the system works this way, or when a new engineer needs the context, or when the decision is challenged and you have the reasoning written down with a date on it.

**The important corollary:** a design document is **not a substitute for actually telling people.** Writing and circulating a document is not the same as communicating a change. If a proposal affects another team, tell them — in the channel they read, in a meeting, in person. The document supports that conversation and outlives it; it does not replace it. Assuming otherwise is how teams get surprised by changes that were "documented."

## Keeping the document alive

A design document's job doesn't end when implementation starts — implementation is exactly when the design meets reality and changes. Two failure modes (both from Ch. 10):

- **The document is abandoned.** It's circulated, approved, and never touched again. Six months later it describes a system that doesn't exist, and the next engineer trusts it and is misled. An out-of-date design doc is worse than none, because it carries false authority.
- **The document is updated but the history is lost.** Someone edits in place, and the record of *what was originally proposed and why it changed* disappears. That history is often the most valuable part — it's what stops the team relitigating a settled decision next year.

The practices that prevent both:

- **Update as you go**, not in a cleanup pass at the end. The moment the design changes, the document changes.
- **Version-control the document.** This solves the lost-history problem directly: every change is a diff with an author, a date, and a message. It is the single highest-leverage habit here.
- **Keep it in the same repository as the code it describes.** Then it travels with the code, shows up in the same searches, and — critically — can be updated in the same pull request as the change it documents.
- **Enforce it in code review.** When reviewing a PR that changes behavior the design doc describes, ask whether the doc was updated. This is how the habit becomes a team norm rather than one person's discipline. See [`code-review`](../code-review/SKILL.md).
- **Keep the status field current** (Draft / In Review / Approved / Implemented) so readers know what they're looking at.

## Common pitfalls

- **Writing the solution before the problem.** The doc reads like a sales pitch and reviewers can't engage with it.
- **Single-option docs.** Looks like you didn't think hard. Even bad alternatives strengthen the doc when you name why they're bad.
- **No clear ask.** Reviewers don't know what kind of feedback you want, so you get either nothing or unhelpful nits.
- **Burying the trade-offs at the end** (or worse, not naming them). Reviewers will find them anyway and trust you less for not surfacing them.
- **Over-length.** A 12-page design doc that nobody reads is worse than a 2-page one that everyone reads.
- **Writing it after the fact.** Then it's documentation, not a design doc. Useful, but it doesn't get you the thinking-out-loud benefit.
- **Not updating the status.** A doc that says "Draft" but is being implemented confuses everyone. Promote it to "Approved" when alignment is there.
- **Abandoning it once coding starts.** See *Keeping the document alive* above — this is the most common failure of all, and it quietly poisons the doc for every future reader.

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
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is still working out **what to build** — pinning down the problem, researching prior art, deciding whether to prototype, or struggling to find uninterrupted thinking time. Route to [`technical-design-process`](../technical-design-process/SKILL.md).
- The user is asking how to write *general* documentation (READMEs, user guides, API docs). Skip — different shape entirely.
- The user is asking about *code* documentation (docstrings, inline comments). Skip.
- The user wants help writing prose for a non-technical document (email, blog post, status update). Skip.
- The user is reviewing a *PR* (code change, not design). Route to [`code-review`](../code-review/SKILL.md).
- The decision is specifically about adopting a new technology. Route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
