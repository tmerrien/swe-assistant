# Reading notes — *Universal Principles of UX* (Pereyra, 2023)

Working notes taken while reading. **Not a skill, and not a source of truth.** These accumulate so that the reading compounds — the point is to spot clusters and collisions early enough to build well, rather than reconstructing principle 4 from memory when we reach principle 40.

**Book:** Irene Pereyra, *Universal Principles of UX: 100 Timeless Strategies to Create Positive Interactions between People and Technology*. Rockport Publishers, March 2023. Volume 4, Rockport Universal series. ISBN 9780760378045.

**Structure:** 100 principles across four sections — **Consider · Empathize · Define · Validate** — each on a two-page spread.

**Reading plan:** *Empathize* and *Define* properly first (they map onto research-led product work); *Consider* and *Validate* skimmed and used as lookup. Notes here follow the order actually read, not the book's order.

---

## How to use this file

Each entry records four things:

- **What it says** — the principle, compressed. Paraphrase, never reproduced.
- **Collides with** — which existing skill it overlaps, extends, or contradicts.
- **Verdict** — one of:
  - `fold` — refines an existing skill; note which and how
  - `cluster` — belongs with other principles in a future skill; name the cluster
  - `context` — useful background, not skill material
  - `skip` — doesn't apply here
- **Open question** — anything unresolved, if there is one.

**Scope — decided.** Interface and experience design is treated as *within* software engineering, not adjacent to it; see [`docs/LIMITATIONS.md`](../docs/LIMITATIONS.md) Section 8. A `fold` verdict is therefore actionable rather than conditional. The narrower limit still holds: design as a discipline — brand systems, visual identity, design as a career — remains out of scope. The test for any entry here is whether an engineer owning a user-facing outcome would need it.

**Build rule:** no skill gets built from a single principle. Candidates are assembled at section boundaries, once a cluster is visible.

---

## Consider

### 1. The user comes first

**What it says.** Keep the user at the centre so that decisions aren't driven by a stakeholder's personal opinion or a designer's assumption. Three questions open every project:

- **Who is it for?** — the audience
- **Why will they use it?** — the goal
- **How will they use it?** — the context of use

Requires no method, only the dedication to do it: listen more, talk less, ask better questions, stay curious, be empathetic.

**Collides with.** [`technical-design-process`](../plugins/swe-assistant/skills/technical-design-process/SKILL.md), Step 3 (*Define the problem*). Same phase, same instinct — ask, restate, don't design before you understand.

**The gap it exposes.** The existing skill treats stakeholders as a source of *imperfect information*: it warns that "stakeholders describe symptoms and preferred solutions, not root problems." That's a claim about **accuracy**.

Pereyra's principle is about **authority** — whose view prevails when the user's need and the stakeholder's preference diverge. The skill never separates the two parties, and so has no answer for that conflict. Two distinct failure modes; only the first is currently covered.

**Also worth noting:** of the three questions, *context of use* is the one engineers skip. Who and why get asked, often badly. How-will-they-actually-use-it usually gets assumed, and it's the only one of the three that can't be answered from a meeting room.

**Verdict:** `fold` — a refinement to `technical-design-process` Step 3, not a new skill. Add the user/stakeholder distinction, and promote *context of use* to an explicit question rather than leaving it implied. Hold until the section is done in case it clusters with later principles on research.

**Open question.** The skill's Step 3 already routes stakeholder disagreement to *"if there's more than one problem, establish priority."* Does the user-versus-stakeholder conflict want the same treatment, or is it a different move — escalation rather than prioritisation?

---

### 2. Work on UX and UI simultaneously

**What it says.** Enters the UX-versus-UI debate: whether one person can or should do both, and how much foundational UX must be finished before visual work starts. UX is the blueprint — needs, wants, behaviours, contexts. Making the thing usable and digestible is complementary work, not a later phase. Done separately the two fall out of balance and the product ends up feeling either uncomfortable or illogical. The two should run together across the whole experience so that all effort moves in the same direction, producing something both usable and attractive.

**Collides with.** Three things at once:

1. **Advice given in this project two messages before this entry** — "principles before patterns; Pereyra first, Tidwell when you're laying out screens." That is a sequencing recommendation and this principle argues against sequencing. Partial hit: the advice was about which book builds judgment first, not about phase order in the work. Revision it does force — keep Tidwell within reach from the start as a lookup while sketching, rather than shelving it until some UX phase completes.
2. [`technical-design-process`](../plugins/swe-assistant/skills/technical-design-process/SKILL.md) — the spiral framing (alternate solitary and collaborative work rather than running phases in sequence), and Step 5's *prototype in parallel with review, don't wait for approval*.
3. [`agile-planning`](../plugins/swe-assistant/skills/agile-planning/SKILL.md) — the manifesto's *responding to change over following a plan*, and the anti-waterfall posture generally.

**The rationale gap.** The book justifies simultaneity by **coordination** — keeping two people's work pointed the same way. That argument does not apply to a solo builder doing both roles. A stronger rationale survives the solo case and the book does not lead with it:

> Visual constraints reveal flow problems and flow constraints reveal visual ones. You discover that a screen cannot hold the step you designed only when you try to lay it out. Concurrency makes that discovery cheap; sequencing turns it into rework.

That is the version worth carrying into a skill, because it holds whether the work is split across people or not.

**Emerging pattern — worth tracking.** Three unrelated sources now make structurally the same argument: the design spiral (Riccomini & Ryaboy, Ch. 10), the Agile Manifesto's anti-waterfall framing, and this principle. **Strict phase-gating is the recurring failure mode; the fix is always alternation.** If a UX skill eventually gets built, this may be its spine rather than a supporting point. Flagging at principle 2 so the pattern is visible if later principles reinforce it.

**Verdict:** `cluster` — process-shape cluster, provisionally with principle 1 and whatever else in *Consider* concerns how the work is sequenced. Not a standalone fold: as written it is a design-team-structure norm, and the repository's existing skills already make the anti-phase-gating argument in their own domains. What is genuinely new is the cheap-discovery rationale above.

**Open question.** If phase-gating keeps recurring as the failure mode across sources, is the right eventual artifact a UX skill at all — or a domain-agnostic one about alternation, which the existing skills would then reference? Hold until the section is finished.

---

<!-- Next entry goes here. Keep the four-part shape. -->
