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

### 3. UI makes or breaks usability

**What it says.** A product is first and foremost measured by how usable it is. Usability is commonly assumed to be UX's problem to solve, but the UI is what end users actually touch — so layout, typography, information hierarchy, interactions, accessibility, and information density are UI decisions, and they are what make or break usability. Usability is also frequently confused with user experience and with ease of use. It has to be held in view across the entire process, from wireframes through to the final interface.

**Collides with.**

- [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) — the *principle of least astonishment* callout and the *implicit knowledge* material are usability principles applied to code interfaces.
- [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md) — *sensible defaults make a large API feel small* is an information-density move, one of the six responsibilities this principle assigns to UI.
- [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) — designing tools an operator can actually use.
- [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) — the *UI/UX Changes* subsection of the template, which currently gets one short paragraph.

**Observation: the repository has usability ideas throughout and no name for them.** Least astonishment, implicit knowledge, defaults that shrink a surface, writing for the operator reading at 3am — these are all usability, distributed across skills that never use the word. The concept is missing, not the practice. If a skill is eventually built here, its contribution may be less about importing new material than about naming what is already present and connecting it.

**Tension with a decision taken outside this file.** Accessibility is listed here as a **UI responsibility**, sitting alongside layout and typography. This project recently moved accessibility references out to a separate context on the grounds that the skill set should not become accessibility-centred — a decision about emphasis and location rather than a denial that it is part of the work. The tension is mild but real: **a UI skill built from this source that omitted accessibility would misrepresent the source.** Recording it now so it is not discovered at build time.

**Cluster forming.** Principles 2 and 3 make one argument between them: principle 2 says do not sequence UX before UI; principle 3 says UI is where usability is actually won or lost. Together: **the visual layer is not decoration downstream of the real thinking.** That is a sharper thesis than "consider the user" and is currently the strongest candidate for what a *Consider*-derived skill would be about.

**Verdict:** `cluster` — with principle 2, under a provisional heading of *UI is not downstream*. Possible secondary fold into `design-doc`, whose *UI/UX Changes* template section would deserve more weight if this principle is taken seriously.

**Open question — check the page.** The principle asserts that usability is confused with *user experience* and with *ease of use*, but the paraphrase captured here does not include the distinction she draws between them. That distinction is load-bearing for the rest of the section. Confirm from the book before building on it.

---

### 4. Always surpass expectations

**What it says.** Look for the extra that makes an interaction memorable, which requires approaching the problem from an unfamiliar angle. A product must work first — but given how many apps exist, usable-and-forgettable is not enough. Two things produce a memorable, positive experience: features people do not expect (pinch-to-zoom at the 2007 Apple event), and getting people into a **state of flow** — Csikszentmihalyi, on complete immersion, and on involvement and focus making an activity more engaging.

**The reading that matters.** *"Features people won't expect"* does **not** mean features nobody needs. It means **unexpected solutions to needs people genuinely have**. Pinch-to-zoom did not arrive from nowhere: the need — zoom precisely and quickly on a small screen — was well established, and the existing answers were +/- buttons, double-tap, and scrollbars. What was surprising was the *solution*, not the problem.

That distinction settles two apparent conflicts:

- **No conflict with YAGNI.** [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) warns against *features nobody asked for* — speculative **problems**. This principle concerns non-obvious **solutions** to real problems. Different objects; the trap and the principle do not touch.
- **No conflict with principle 1.** Both make the same move: do not stop at what the user literally said. Principle 1 says do not let assumption override need. Principle 4 says do not mistake a stated request for the underlying need. Same target, approached from opposite sides.

*(An earlier version of this entry read the principle as licensing speculative features and logged it as read-critically. That was a misreading, corrected here.)*

**Collides with — and this is the strong one.** [`technical-design-process`](../plugins/swe-assistant/skills/technical-design-process/SKILL.md), Step 3:

> *"Ask stakeholders what **they** perceive the problem to be. Not what solution they want — what problem they think exists."* … *"note when the answer is actually a solution, and gently ask what it would fix."*

That is the same discipline, stated for engineering problems rather than interface ones. **Pereyra is not in tension with the repository here — she is the design-side statement of something it already holds.** The existing skill stops at *find the real problem*; this principle continues to *and the best solution to it may not be the one anyone described*. That continuation is the addition.

**The flow half.** Csikszentmihalyi's flow is genuine research (*Flow: The Psychology of Optimal Experience*, 1990) and points the same direction as principle 3 — eliminating distraction is a **subtractive** usability move. Not currently in [`READING-LIST.md`](../READING-LIST.md); add only if flow becomes load-bearing in a skill, per the standing rule against aspirational citation.

**One narrow constraint worth carrying.** In high-stakes, low-attention contexts — care, medical, emergency, financial — **unfamiliarity has a cost that consumer contexts do not pay**. A genuinely better solution that is unfamiliar to a stressed or hurried user still has to be learnable at the moment of use. This is a constraint on how an innovative solution is introduced, not an argument against innovating. Pereyra's practice is consumer work, so the constraint is not visible in the source and would need adding.

**Verdict:** `fold` — into `technical-design-process` Step 3, extending *find the real problem* with *and the obvious solution to it may not be the best one*. Also `cluster` on the flow material, which belongs with principles 2 and 3 under *UI is not downstream*.

**Open question.** Where does the search for a non-obvious solution actually happen in the existing process? Step 4 (*do your research*) and Step 5 (*conduct experiments*) are the plausible homes — prior art and prototyping are how you find solutions nobody described. If so, the fold may be a cross-reference rather than new text.

### 5. Design is not neutral

**What it says.** Draws on Harry Brignull's **dark patterns** / **deceptive patterns**, with emphasis on the less obvious cases — the slippery-slope and insidious ones rather than the flagrant. Since UI/UX design has no ethics code, the field depends on individual designers making the right moral call. Designs that deliberately hide true costs, trick people into decisions, or misrepresent information make their designer part of the problem. If you designed it, you are responsible for it.

**The claim that needs correcting.** *"There is no ethics code"* is true of **design** and false of **engineering** — which matters here, because [`docs/LIMITATIONS.md`](../docs/LIMITATIONS.md) Section 8 now places interface design inside software engineering.

The [ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics) (2018) applies to *"anyone who uses computing technology in an impactful way"*, and two of its general principles bear directly on this material:

- **1.2 — Avoid harm.**
- **1.3 — Be honest and trustworthy**, requiring transparency and full disclosure of a system's capabilities, limitations, and problems.

An engineer building an interface is therefore **not** in the code-less position Pereyra describes. This is more than a technicality: a designer relying on personal conscience is in a weak position arguing with a stakeholder, while an engineer citing a numbered clause of a professional standard is in a much stronger one.

**And it is increasingly law, not only ethics.**

- **EU Digital Services Act, Article 25** prohibits designing or operating an interface in a way that deceives or manipulates recipients, or that materially distorts or impairs their ability to make free and informed decisions. The Commission's **first formal DSA non-compliance decision (5 December 2025)** fined X €120 million, partly for deceptive design in the verification badge.
- **FTC** treats dark patterns as unfair and deceptive practices under the FTC Act, with ROSCA available for subscription-flow cases.
- **Canada, Bill C-27** — an organisation must not obtain or attempt to obtain consent by providing false or misleading information, or by using deceptive or misleading practices.

**Where this bites hardest.** In products handling health information under consent-based privacy law — PHIPA in Ontario, for instance — the ethical and legal arguments converge. Consent obtained through a deceptive interface is plausibly not valid consent, which makes a dark pattern a **compliance failure** rather than only a moral one. For a marketplace whose users include seniors and people with disabilities, the exposure is higher still, because the patterns that exploit hurry, confusion, or low confidence are exactly the ones those users are least protected against.

**Collides with — and exposes a hole.** The repository has **essentially no professional-ethics content**, and `LIMITATIONS.md` Section 7 does not list it among the coverage gaps (which name interviewing, salary, toxic dynamics, burnout, stack onboarding, and non-IC trajectories). The nearest neighbours are oblique:

- [`input-validation`](../plugins/swe-assistant/skills/input-validation/SKILL.md) — OWASP-anchored, but security rather than ethics.
- [`incident-response`](../plugins/swe-assistant/skills/incident-response/SKILL.md) — blameless postmortems, an ethical stance toward colleagues rather than users.
- [`change-discipline`](../plugins/swe-assistant/skills/change-discipline/SKILL.md) — judgment about changing things, with no ethical dimension.

**The gap grew when the scope decision was taken.** Deciding that interface design is engineering imported the surface where most user-facing ethical failures actually occur, without importing anything that addresses them.

**Verdict:** `fold` **plus a documentation fix**, and the strongest candidate in the section so far for eventually becoming its own skill.

1. **Immediate and cheap:** add professional ethics to the coverage-gaps list in `LIMITATIONS.md` Section 7. It is a genuine omission and naming it costs nothing.
2. **Skill candidate:** deceptive-pattern recognition is situation-shaped in the way this repository requires — *"I have been asked to add a pre-checked box"*, *"make the cancel flow harder"*, *"default this to opt-in"*. That is a real recurring moment with a decision in it, not a topic.
3. **The distinguishing content** would be the ACM clauses and the regulatory position. Not because the moral argument is insufficient, but because engineers are usually pushing back against someone with more authority, and *"this is manipulative"* loses that argument where *"this is an Article 25 problem and ACM 1.3"* does not.

**Open questions.**

- Brignull's taxonomy (deceptive.design) names specific patterns — confirmshaming, roach motel, sneak into basket, and so on. Does the eventual skill teach the taxonomy, or teach the test that catches novel ones? The repository's usual answer is the test, per the standing preference for judgment over checklists.
- Is this UX at all, or is it engineering ethics that happens to surface in interfaces? If the latter, it belongs outside the UX cluster entirely and does not wait on the *Consider* section finishing.

<!-- Next entry goes here. Keep the four-part shape. -->
