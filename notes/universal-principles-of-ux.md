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

**Correction to an earlier version of this entry.** A previous draft cited **EU DSA Article 25**, **FTC** enforcement, and **Canada's Bill C-27** as though all three bore on the maintainer's situation. Two do not apply and one is not law:

- **Bill C-27 died on the Order Paper in January 2025** when Parliament was prorogued; it never reached a vote, and the April 2025 election delayed reform further. Canada still operates under **PIPEDA**. Citing C-27 as binding was an error.
- **EU DSA Article 25** governs EU platforms; **FTC** action governs US commerce. Neither reaches an Ontario care marketplace serving Ontario users.

They remain useful as evidence that regulators internationally are converging on deceptive design as a legal rather than merely ethical matter — but as **context**, not as authority.

**What actually applies in Ontario today.** The local position is stronger than the foreign one:

- **PIPEDA** — consent must not be obtained through deception, and organisations must not mislead or deceive individuals in connection with obtaining consent.
- **PHIPA** — for products handling personal health information, consent must be meaningful. Consent obtained through a deceptive interface is plausibly not valid consent, which converts a dark pattern from a moral failure into a compliance one.
- **The Office of the Privacy Commissioner is actively examining this.** A late-2024 OPC sweep reviewed **145 Canadian websites and apps** specifically for deceptive design patterns. In November 2024 the federal, provincial and territorial Information and Privacy Commissioners issued a **joint resolution** urging organisations to avoid designs that influence, manipulate, or coerce users into decisions against their privacy interests.
- **OPC guidance on meaningful consent** is not binding law, but states regulator expectations and is relied on in investigations.

**On professional codes — a correction of emphasis.** An earlier draft treated the [ACM Code of Ethics](https://www.acm.org/code-of-ethics) as giving engineers solid ground that designers lack. That overstated it. The ACM Code is **voluntary and unenforceable**: membership is optional, there is no licensure for software engineers in most jurisdictions, and no disciplinary consequence follows a violation. Contrast a P.Eng in Ontario, governed by the *Professional Engineers Act* with a protected title and a real regulator — which most software engineers are not. **Nobody takes a vow leaving a computer science programme.**

The Code's clauses — **1.2 Avoid harm**, **1.3 Be honest and trustworthy** — remain worth knowing, but their value is **rhetorical rather than enforceable**. They help frame an argument; they do not settle one. The regulatory position does more work.

**On the designer/engineer split.** The earlier draft leaned on a distinction between the two that does not hold and that undercuts [`docs/LIMITATIONS.md`](../docs/LIMITATIONS.md) Section 8. Designers are engineers and engineers are designers; the person who ships the interface owns its consequences regardless of job title.

**Collides with — and exposes a hole.** The repository has essentially no professional-ethics content. Nearest neighbours are oblique: [`input-validation`](../plugins/swe-assistant/skills/input-validation/SKILL.md) (security, not ethics), [`incident-response`](../plugins/swe-assistant/skills/incident-response/SKILL.md) (blameless postmortems — an ethical stance toward colleagues, not users), [`change-discipline`](../plugins/swe-assistant/skills/change-discipline/SKILL.md) (judgment without an ethical dimension). Now recorded in `LIMITATIONS.md` Section 7.

**Verdict:** `fold` plus documentation fix (done), and the strongest standalone skill candidate in the section.

The situation is well-shaped for this repository: *"I have been asked to pre-check this box"*, *"make the cancel flow harder"*, *"default this to opt-in"*. A real recurring moment with a decision inside it.

**Design note for the eventual skill — from the maintainer.** It should be able to **raise the concern unprompted** when a design under discussion looks ethically off, not only answer when asked. That is [`docs/METHODOLOGY.md`](../docs/METHODOLOGY.md) Section 10.7 (surface what the user cannot see) applied to ethics, and it is arguably the highest-value application of that clause anywhere in the skill set — an engineer mid-implementation is exactly the person who will not think to ask.

**Open questions.**

- Teach Brignull's taxonomy (confirmshaming, roach motel, sneak into basket), or teach the test that catches novel patterns? The repository's standing preference is the test.
- Is this UX, or engineering ethics surfacing in interfaces? **Maintainer's answer: both.** It therefore does not need to wait for the *Consider* section to finish.
- Jurisdiction is a live problem for a skill meant to be portable. The Ontario position above is specific to one maintainer. A general skill would need to teach *find your regulator's position* rather than assert any particular one.

### 6. Words matter

**What it says.** Writing is the highest-return skill to invest in for UX. Good copy evokes emotion while removing ambiguity, and its absence is felt sharply. People do read on the web — differently: more task-oriented and goal-focused than in print, and expecting something closer to conversation because they can go back and forth with the system. Make copy digestible: simplify language, label content, keep it bite-sized, avoid burying links inside long paragraphs, make it scannable, use lists. Address users as **"you"** — it makes the copy about their goals rather than about the product. Edit ruthlessly at sentence and paragraph level, cutting to exactly what needs saying. Then **read it aloud**; if it sounds robotic, it is not finished.

**Strong cross-source convergence — the headline.** The read-aloud test is Paul Graham's, near-verbatim, from *Write Like You Talk* — already in [`READING-LIST.md`](../READING-LIST.md) and already cited in [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md). Graham derives it for essays; Pereyra derives it for interface copy. **Two independent sources, different surfaces, identical diagnostic.** Convergence of that kind usually indicates the test is load-bearing rather than a stylistic preference, and it is the strongest evidence so far that the writing material in this repository generalises beyond documents.

**Her central claim is better than her argument for it.** *"The best skill to invest in for UX is writing"* sounds like hyperbole until one notices that **most of an interface is words** — labels, buttons, errors, empty states, confirmations, permission prompts. The visual layer that receives most attention is frequently a container for text. She asserts the claim without making that observation, which is the thing that actually justifies it.

**Collides with — four skills and no owner.** The repository holds this discipline in pieces:

- [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) — the *learn to write* material: write clearly, reread from the audience's perspective, be concise, edit others' work to improve your own. Cites Strunk & White, Zinsser, and both Graham essays.
- [`commit-and-pr-hygiene`](../plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) — Beams' seven rules.
- [`logging`](../plugins/swe-assistant/skills/logging/SKILL.md) — what a human reads under pressure at 3am.
- [`working-with-managers`](../plugins/swe-assistant/skills/working-with-managers/SKILL.md) — short PPP bullets.

Four surfaces, one discipline, no skill that owns it. Interface copy would be a fifth. **Possible future consolidation:** a writing skill that these reference, rather than each carrying a fragment. Not yet justified — recorded so the pattern is visible if a sixth surface appears.

**A tension the principle does not address.** *"Evoke emotion while simultaneously removing all ambiguity"* treats as free something that is a trade. Evocative copy tends loose; unambiguous copy tends dry. Warmth and precision can coexist, but not without effort, and the principle does not say which yields when they conflict.

In high-stakes, low-attention contexts the resolution is clear: **precision wins, and warmth is a constraint on how precision is expressed rather than a competing goal.** An attendant confirming a shift or a person granting consent to share health information needs to be certain what they are agreeing to. That resolution is not in the source and would need adding to anything built from it.

**Meets the accessibility thread.** Plain language is among the central recommendations of W3C COGA (*Making Content Usable for People with Cognitive and Learning Disabilities*). This principle and the cognitive-accessibility material reach the same practices from different directions — simplify, chunk, scan, avoid burying meaning in prose. Worth noting because it means plain-language work serves two masters at once, which is a good argument when justifying the effort.

**Verdict:** `fold`. Two candidates:

1. **Extend `design-doc`'s writing section** to note that the read-aloud test and the concision discipline apply to interface copy as well as documents — cheap, and true today.
2. **Hold as the anchor** for an eventual consolidated writing skill, if the four-surfaces-no-owner pattern is judged worth resolving.

**Open question.** Is *"words are most of the interface"* an observation worth putting in front of an engineer explicitly? It is the kind of thing that sounds obvious once stated and is routinely ignored in practice — engineers reach for layout and component choices when the error message is what is actually failing the user.

### 7. Visual metaphors communicate the fastest

**What it says.** A good visual metaphor creates new meaning out of **mental models** — "the lens of our mind" — and lets an audience relate quickly by drawing on symbolism they already hold. Illustrated by Google Japan's interactive memorial after the 2011 tsunami, which let people leave messages in their own language, built around the cherry blossom. A short principle in the book.

**The durable part is the mechanism, not the medium.** *Visual metaphor* is one delivery vehicle; **borrowing an existing mental model rather than asking someone to construct a new one** is the general move, and this repository already runs on it:

- [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) argues that domain-aligned boundaries are the rare structural move that reduces dependency *without* a matching obscurity cost — and the stated reason is that the boundary matches a model people already carry. Same mechanism.
- The **principle of least astonishment** in the same skill is the same idea stated as a constraint: expectation comes from a model already held.
- *Naming that carries meaning* is listed there as an obscurity lever.

**The engineer's highest-frequency application is naming, not iconography.** Classes, endpoints, tables, error vocabulary. A good name borrows a model the reader has; a poor one forces them to build one. [*Elements of Clojure*](../READING-LIST.md) (Tellman), already on the reading list, is substantially about this.

**Two failure modes the principle omits.**

- **Metaphors leak, then expire.** The save icon is a floppy disk most users have never handled. A metaphor that stops matching reality does not degrade gracefully — it misleads, because users continue to trust the model it implied.
- **Metaphors are culturally located.** The cherry blossom works *because* it is culturally specific; that specificity is the reason the example succeeds. The same move fails outside its context. For a product serving a linguistically and culturally diverse population, this is a live constraint rather than a footnote.

**Pattern in the source — recording once, properly.** Principle 4's exemplar was Apple's pinch-to-zoom; principle 7's is a Google memorial experience. Both are consumer showcase work: expressive, well-resourced, emotionally driven. Pereyra's practice is consumer design (Google, Nickelodeon, FOX, Red Bull, Balenciaga), and it shapes which examples the book treats as exemplary.

**This is not a criticism of the book — it is a known transfer condition.** Anything built from this source for operational, high-stakes, or accessibility-sensitive software needs the examples re-derived rather than borrowed. Flagged here so later entries can reference this note instead of rediscovering it.

**Verdict:** `cluster` — with the *UI is not downstream* group, as further support that the visual layer carries genuine communicative weight. **Thin, and recorded as such:** the mechanism is already covered by `managing-complexity`, and the new contribution — apply it to visual symbol choice — is narrow. Not every principle in a hundred is load-bearing, and noting that is more useful than manufacturing depth.

**Open question.** Do the two omitted failure modes belong to this principle or to a later one? A book with a hundred entries may well cover metaphor decay elsewhere. Worth checking before adding them as original contributions.

### 8. Attractive products are more usable

**What it says.** The **aesthetic-usability effect**, from Kurosu and Kashimura (1995). People do not judge usability by how usable an interface actually is — they judge it by how it looks. We are biased toward believing attractive products work better even when they do not, and when they fail we continue to find them attractive and forgive their usability problems. Forgiveness has a limit: if something genuinely does not work, beauty will not save it.

**The evidence is unusually strong for a design claim — worth stating precisely.**

- **Kurosu & Kashimura (1995)**, Hitachi Design Center: 26 ATM interface variations, 252 participants. *Apparent* usability correlated more strongly with aesthetic properties (layout symmetry, colour harmony) than with *inherent* usability measured by task-completion efficiency.
- **Tractinsky (1997)** attempted to break it. He obtained the original layouts, translated them from Japanese to Hebrew, and imposed tighter methodological controls, expecting the effect to be culturally specific. It replicated — and the correlation was **stronger** in Israel than in Japan.
- **Tractinsky, Katz & Ikar (2000)**: r > 0.9 between pre-use and post-use perceptions, with aesthetics driving usability judgments **irrespective of performance outcomes**.

A replication designed to fail that did not is about as good as evidence gets in this literature. Note the object throughout: the effect concerns **perceived** usability. Attractive interfaces are not easier to operate; they are believed to be.

**The implication the book does not draw — a measurement hazard.** If aesthetics drives perceived usability independently of performance, then **usability testing conducted on an attractive prototype systematically under-reports problems**. Participants rate a polished mockup as easier than an equivalent ugly one, and forgive friction they would otherwise report.

This lands squarely on [`technical-design-process`](../plugins/swe-assistant/skills/technical-design-process/SKILL.md) **Step 5**, which currently says *"circulate the prototype — a running thing generates real feedback, a description generates polite nods."* That is true and incomplete: **the more polished the artifact, the more the feedback flatters it.** For research-led work this is not a subtlety, it is a validity threat to the primary instrument.

Practical consequences worth carrying into a fold:

- Test flows on deliberately low-fidelity artifacts when the question is *does this work*, and save polish for when the question is *does this appeal*.
- Treat "users liked it" from a high-fidelity prototype as weak evidence of usability.
- Watch for the inverse error too: an ugly prototype may be rated harshly for reasons unrelated to the flow being tested.

**Connects two principles the book leaves unconnected.** Principle 5 established that design is not neutral. Principle 8 establishes that beauty buys forgiveness. Together: **beauty can purchase forgiveness a product has not earned**, suppressing complaints about something that genuinely underserves people. Pereyra notes forgiveness has limits without observing that this is adjacent to the deceptive-design territory of principle 5. The link is worth making explicitly in anything built from either.

**Transfer condition** (see the note at principle 7). For consequence-bearing software, forgiveness is the wrong currency. If a worker misses a shift because a screen was confusing, goodwill toward the visual design does not undo the missed shift. The effect operates on **satisfaction**; care, medical, and financial software are judged on **outcomes**. The principle remains true there — it simply stops being something to rely on and becomes something to control for.

**Verdict:** `fold` into `technical-design-process` Step 5, as a validity caution on prototype feedback. This is the most immediately actionable entry in the section so far, because it changes how research is run rather than how an interface is drawn. Secondary `cluster` link to *UI is not downstream* — the effect is further evidence that visual quality does real work.

**Open question.** The literature includes work on boundary conditions for the effect (task complexity appears to moderate it). If a skill is built on this, is the honest statement *"aesthetics biases perceived usability"* or the narrower *"aesthetics biases perceived usability under conditions X"*? Worth checking before asserting the general form.

### 9. People remember the unusual

**What it says.** Follows Raymond Loewy's **MAYA** — *Most Advanced Yet Acceptable*: to sell something new make it familiar, and to sell something familiar make it surprising. Also invokes the **Von Restorff effect** (the isolation effect, von Restorff 1933): an item that stands out from a set is better remembered. Short and direct in the book.

**MAYA supplies the ceiling principle 4 lacked.** Principle 4 argued for surprising users with innovative solutions and set no upper bound. Loewy's formulation *is* the bound: advance to the edge of what people will accept, and stop there. **Acceptable is the constraint on advanced.** Read together, 4 and 9 are one principle — innovate, but only as far as the audience can follow.

**Self-correction.** The entry for principle 4 records a caveat presented as an addition to the source:

> *"In high-stakes, low-attention contexts, unfamiliarity has a cost that consumer contexts do not pay. A genuinely better solution that is unfamiliar to a stressed or hurried user still has to be learnable at the moment of use."*

That is **MAYA with a lower acceptability threshold**, not an original contribution. The book covers it three principles later. This is precisely the failure flagged at principle 7 — check whether the source handles something later before recording it as an addition. The observation stands; the attribution was wrong. What remains genuinely additive is only the narrower claim that **the acceptability threshold moves with stakes and attention**, which Loewy does not address.

**Von Restorff has a sharper engineering application than the book's framing.** The isolation effect is usually presented as a way to make things memorable. In this repository it already appears as a **failure mode**:

- [`logging`](../plugins/swe-assistant/skills/logging/SKILL.md) — log levels exist so WARN and ERROR stand out from INFO. Von Restorff by design.
- [`operator-playbook`](../plugins/swe-assistant/skills/operator-playbook/SKILL.md) — *"if an alert fires regularly and nobody acts on it, either fix it or delete it."* **Alert fatigue is the Von Restorff effect collapsing**: once everything is distinctive, nothing is.

**Tension with least astonishment, and its resolution.** Principle 3's territory says be predictable; Von Restorff says stand out. These are reconciled by **scarcity** — distinctiveness works only when rationed. The same rule appears in at least three unrelated places:

- Wood, Bruner & Ross on *marking critical features*: a tutor who marks every feature has marked none.
- [`docs/METHODOLOGY.md`](../docs/METHODOLOGY.md) Section 10.7, capping proactive surfacing at one or two items ranked by consequence.
- Alert and log-level discipline, above.

**Emphasis is a budget, not a technique.** That formulation is worth keeping; it generalises well beyond interfaces and is the transferable content of this principle.

**Verdict:** `fold`, attached to the principle-4 fold rather than standing alone — MAYA becomes the ceiling clause on *the best solution may not be the one anyone described*. Secondary note for [`logging`](../plugins/swe-assistant/skills/logging/SKILL.md) and [`operator-playbook`](../plugins/swe-assistant/skills/operator-playbook/SKILL.md): both already teach rationed emphasis without naming the effect that explains why it works.

**Open question.** Does the acceptability threshold in MAYA vary by audience expertise as well as by stakes? A power user tolerates more novelty than a first-time user, which would make MAYA a per-segment judgment rather than a single product-wide setting. Not addressed in the source.

### 10. First and last items are remembered most

**What it says.** The **serial position effect**, from Hermann Ebbinghaus's experimental work on memory. Items at the beginning or end of a sequence are recalled more easily than those in the middle, which makes ordering a real design decision rather than an arbitrary one. Do not bury important things in the middle. Not everything can be equally important: decide what you want people to remember or do, and place it first or last. An interaction model should **deliberately allow users to forget** the less important parts so there is room for what matters.

**A sharpening the principle omits — the halves are not interchangeable.** The effect decomposes into two mechanisms:

- **Primacy** — early items receive more rehearsal and reach long-term memory. **Durable.**
- **Recency** — late items are still in working memory. **Fragile**; it collapses under delay or interference.

That yields a rule the book does not state: **if you want something remembered later, put it first. If you want it acted on now, put it last.** The distinction matters whenever there is a gap between reading and acting.

**Explains existing repository conventions rather than adding new ones.** This is the entry's main value — several established practices turn out to be the serial position effect applied without naming it:

- [`commit-and-pr-hygiene`](../plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) — Beams' subject line first. Primacy.
- [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) — lead with the problem; the Introduction must stand alone because *"most readers will only read this section."* Primacy.
- **Skill descriptions** — situation first, routing and non-trigger clauses last, trigger phrases in between. Primacy and recency bracketing the least critical material, which is why trimming from the middle worked when all descriptions were brought under budget.
- [`working-with-managers`](../plugins/swe-assistant/skills/working-with-managers/SKILL.md) — **PPP** places *Problems* last. Under recency that is the correct slot for the item requiring action this week. Whether deliberate or inherited, the format is well-formed.

**The non-obvious half: designing for forgetting.** Nearly all design advice concerns what to make memorable. The instruction to *let users forget* is subtractive, and it is the third independent arrival at that shape in this section — after flow's *eliminate distraction* (principle 4) and rationed emphasis (principle 9).

**Synthesis across 9 and 10:** *emphasis is a budget, and forgetting is how you fund it.* Something can only be made memorable if other things are permitted to be forgettable. This is the strongest cross-principle idea the section has produced.

**Verdict:** `cluster`, and it clarifies the section's shape — see below.

---

### 11. Less is more

**What it says.** Presented by the author as a cliché and openly controversial — *"there is no right or wrong here. Sometimes less is more and sometimes it's not."* Sourced to **Ludwig Mies van der Rohe**, who held that elegance does not derive from abundance and that restrained decoration has more impact than plentiful decoration. Supported by **John Sweller**: overloading memory raises the error rate. So less is more where an interface requires complicated tasks — while other parts of an interface may legitimately inspire, create wonder, and prompt action.

**The strongest link to this repository's own foundations so far.** Sweller is already cited in [`docs/THEORETICAL-FOUNDATIONS.md`](../docs/THEORETICAL-FOUNDATIONS.md) Section 6, where cognitive load theory justifies the consistent skill body structure and the practice of surfacing only the situationally relevant skill. **This is the first UX principle resting on a source the project already holds as part of its own grounding** — which makes the transfer unusually well-supported.

**Sweller resolves the controversy the principle leaves open.** She cites him and then declines to adjudicate, but the framework adjudicates. Cognitive load is not one quantity:

- **Intrinsic** — the inherent difficulty of the task. Cannot be reduced without reducing the task.
- **Extraneous** — imposed by *presentation*. This is what "less is more" should target.
- **Germane** — the load that contributes to building understanding. Removing it is harmful.

**"Less is more" is therefore wrong as stated, which is precisely why it feels contested.** The defensible version: **reduce extraneous load, leave intrinsic alone, protect germane.** Undifferentiated minimalism strips germane load along with the rest, which is how a spare interface ends up incomprehensible. Anything built from this principle should carry the three-way distinction rather than the aphorism.

**The repository already applies this correctly without naming it.**

- [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md) — *sensible defaults make a large API feel small.* Defaults remove **presentation** burden while preserving capability. Extraneous load reduced, intrinsic untouched. Textbook.
- [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) — *the most reliable way to keep code flexible is to have less of it*, with **Muntzing** as the procedure: remove a component, check whether it still works, restore the last one that broke it. **Less-is-more with a falsification test attached**, which is a substantial improvement on the aphorism and worth keeping as the model for how the principle should be operationalised.

**Her second half is a load budget by zone.** Reduce load where the task is demanding; permit richness where it is not. That is Cluster B extended from attention to cognitive capacity — the same budgeting logic applied to a different scarce resource.

**Verdict:** `cluster` into **Cluster B**, where it supplies the **theoretical spine**. The cluster's members — writing (6), rationed emphasis (9), serial position (10), and load management (11) — are four applications of one constraint, and Sweller names the constraint. Notably the repository already cites him for the same purpose in a completely different domain, which strengthens the case made in the section summary below that Cluster B is domain-agnostic rather than UX-specific.

**Open question.** If Cluster B becomes a skill, does it cite Sweller directly or defer to `THEORETICAL-FOUNDATIONS.md` Section 6? The methodology requires claims to trace to sources; it does not say whether a skill may lean on the project's own grounding document rather than re-citing. Worth settling once, since it will recur.

---

## Consider — structure so far (through principle 15)

Recorded here because the build rule assembles candidates at section boundaries. Two clusters and three standalones have emerged. Updated as the section progresses.

**Cluster A — *UI is not downstream*** (principles 2, 3, and 7 in support)
The visual and interaction layer is where usability is decided, not decoration applied afterwards. Supported by principle 8, since the aesthetic-usability effect is further evidence that visual quality does real work.

**Cluster B — *Attention is finite; order and emphasis are how you spend it*** (principles 6, 9, 10, 11, 12)
Writing, rationed distinctiveness, sequence position, load management, and the minimalism debate are five faces of one constraint. The unifying line: **emphasis is a budget, and forgetting is how you fund it.** This cluster travels furthest beyond interfaces — it already describes log levels, alert discipline, commit subjects, design-doc introductions, and Output Protocol 10.7.

**Principle 11 supplies the theory.** Sweller's cognitive load theory names the constraint the other three apply, and this repository **already cites Sweller** in [`docs/THEORETICAL-FOUNDATIONS.md`](../docs/THEORETICAL-FOUNDATIONS.md) Section 6 — for skill body structure and selective surfacing, in a domain with no interfaces in it. A theory that independently grounds both a UX cluster and the project's own pedagogy is strong evidence the cluster is not UX-specific.

**Standalone A — problem definition** (principles 1 and 4+9 combined)
Folds into [`technical-design-process`](../plugins/swe-assistant/skills/technical-design-process/SKILL.md) Step 3, extended with *the best solution may not be the one anyone described*, bounded by MAYA.

**Standalone B — ethics** (principle 5)
The strongest independent skill candidate in the section, and arguably not UX at all. Does not need to wait for the section to finish.

**Standalone C — the measurement hazard** (principle 8)
Folds into `technical-design-process` Step 5 as a validity caution on prototype feedback. The most immediately actionable item so far.

**Note on Cluster B's reach.** It is the only cluster whose content is already load-bearing across the existing skill set without having been named, and now the only one with a theoretical anchor the project already holds. That makes it the most likely candidate to become something domain-agnostic that other skills reference, rather than a UX skill — echoing the open question first raised at principle 2, now with better evidence behind it.

**Cluster C — *Time is a design material*** (principles 13, 14, 15)

Three decisions about the user's time rather than their attention: **how fast you answer them** (13), **when you deliberately slow them down** (14), and **how long you have before they leave** (15). The cluster's spine is that all three are threshold effects — there is a value past which behaviour changes in kind, not in degree — and all three are consequently invisible to aggregate statistics. That last property is what makes the cluster transfer to engineering: it is the same lesson [`metrics`](../plugins/swe-assistant/skills/metrics/SKILL.md) teaches about histograms and averages, arrived at from the human side.

Note that 13 and 14 are a thesis/antithesis pair (speed as the goal; friction as a deliberate purchase), which makes this the second cluster whose members argue with each other — see the standing design note below.

---

### 12. Less is a bore

**What it says.** Robert Venturi's riposte to Mies, coined roughly two decades after *less is more* (*Complexity and Contradiction in Architecture*, 1966), arguing for personality and maximalism. The principle warns against applying minimalism everywhere, which is part of why so many applications now look alike. That homogeneity is also an opportunity: in a market where everything resembles everything else, difference attracts attention. The author closes: **"If a design is difficult to use, it's neither maximalist nor minimalist — it's just bad."** Design still has to function.

**11 and 12 are a deliberate pair, and the closer is the load-bearing sentence.** Neither principle stands alone. Presented together they are thesis and antithesis, and the resolution is in the final line: **usability is the floor; the minimal/maximal choice happens above it.** Anything built from either principle should carry the pair, not one half.

**Three principles now constrain each other in a structure the book does not map.**

- **Principle 3 sets the floor** — usability decides whether the thing works at all.
- **Principle 9 sets the ceiling** — MAYA: differentiate up to the limit of acceptability, no further. Loewy bounds Venturi exactly as he bounded principle 4's argument for innovation.
- **Principles 11 and 12 argue over the space between.**

That structure is more useful than any of the four individually and is a candidate for how a derived skill would be organised.

**Terminological trap — flag this hard.** Venturi's title argues **for** complexity. That is not Ousterhout's complexity, which [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) defines as *anything related to the structure of a system that makes it hard to understand and modify*. **Venturi means richness and ambiguity; Ousterhout means cost.** Same word, opposite valence, and both sources are now in play in this project. Any material drawing on both must keep them separate or it will produce incoherence.

**The transferable engineering content is innovation tokens.** [`choose-boring-technology`](../plugins/swe-assistant/skills/choose-boring-technology/SKILL.md) holds that novelty draws on a limited budget: spend it where it earns something and use boring conventions elsewhere. **Visual differentiation is a token spend.** That reframes the principle usefully — being different is not free, it is a purchase, and the question is whether *this* difference is worth what it costs in unfamiliarity. Which returns once more to Cluster B: a budget for a scarce resource.

**Note on homogenisation.** The convergence the principle observes has a specific cause for engineers: component libraries and design systems mean inheriting somebody else's visual decisions wholesale. That is efficient and it is also the mechanism producing sameness. Worth stating plainly, because for an engineer the choice is rarely *minimal or maximal* in the abstract — it is *accept the library's defaults or deviate from them*, which is the same decision wearing work clothes.

For anyone extending an **existing** design system rather than starting fresh, the live tradeoff is not minimalism versus maximalism at all: it is **consistency with what exists versus differentiation from it**, with an existing codebase weighting one side.

**Verdict:** `cluster` into **Cluster B**, paired with principle 11. The pair contributes the floor-and-ceiling structure above, and the innovation-token reframing is the part that transfers cleanly to engineering work.

**Open question.** Does the differentiation argument survive outside consumer markets? It assumes attention is contested and that being noticed has value. For internal tools, operational software, and products people use because they must rather than because they chose to, standing out may carry cost with no corresponding benefit — see the transfer condition recorded at principle 7.

---

## Standing design note — hold the disagreement, don't resolve it

*Raised at principle 12; governs every skill derived from this file and now generalized into the methodology.*

Principles 11 and 12 are not merely two sides of a table. **They complement each other in a conversation.** The value is not in deciding which is correct — it is in being able to raise the other side's argument at the moment a decision is being taken: *given situation X, which direction, and why?*

**This generalizes past 11/12.** Research and practice are full of people who disagree for good reasons. The real world is a gray area, and taking one side and closing the question forfeits what the other side knows. Carrying the whole spectrum of the argument is what makes a position usable across varied situations rather than only the one it was written for.

**Consequences for this file.** Every genuine disagreement already logged here is material to preserve rather than a defect to resolve:

- **Principle 4 vs. YAGNI** — surpassing expectations against not building what isn't needed.
- **Principle 6** — emotional warmth against precision in interface language.
- **Principle 8 vs. principle 3** — the aesthetic-usability effect against usability as ground truth; principle 8 is itself the measurement hazard.
- **Principle 12 vs. Ousterhout** — complexity as richness against complexity as cost.

**Where it went.** Promoted to [`METHODOLOGY.md`](../docs/METHODOLOGY.md) Design Principle 3.6, *Preserve productive disagreement*, grounded in Perry's scheme (1970) at [`THEORETICAL-FOUNDATIONS.md`](../docs/THEORETICAL-FOUNDATIONS.md) Section 4.2. The bounding condition recorded there matters as much as the principle: it applies where the disagreement is **real**, not to questions that merely have two describable sides.

**The mechanism a derived skill uses.** State the positions, name what each buys and costs, then ask which situation the user is in. The skill supplies the argument; the user makes the call.

---

### 13 — Provide feedback quickly

**What it says.** Draws on Walter J. Doherty and Ahrvind J. Thadani, *The Economic Value of Rapid Response Time* (IBM Systems Journal, November 1982), which reset the expected response-time requirement from ~2 seconds to **400ms**. The finding was not that faster is nicer but that **productivity rises more than in direct proportion to the drop in response time** — superlinear, not linear. When machine and user interact at a pace where neither waits on the other, throughput rises, work quality improves, and satisfaction goes up.

Jakob Nielsen's three thresholds:

- **0.1s** — feels instantaneous.
- **1s** — the user notices the delay but their flow of thought survives.
- **10s** — the outer limit of held attention.

Speed is framed as the ultimate usability metric, and often the thing people remember most.

**The part worth stating that the principle doesn't.** Nielsen's thresholds are not his — he traces them to Robert B. Miller (1968) — and he notes they have not changed in the decades since, because **they are properties of human perception and cognition, not of technology.** That makes them one of the very few UX constants: hardware gets faster, the thresholds do not move. An engineering target derived from them does not go stale.

**Collides with.** [`metrics`](../plugins/swe-assistant/skills/metrics/SKILL.md) most directly — it teaches histograms over averages and the SLO connection, but never says where target *values* should come from. Also [`on-call-shift`](../plugins/swe-assistant/skills/on-call-shift/SKILL.md) (SLI/SLO/SLA), [`tracing`](../plugins/swe-assistant/skills/tracing/SKILL.md), [`operator-playbook`](../plugins/swe-assistant/skills/operator-playbook/SKILL.md).

**The sharpest engineering transfer — thresholds are perceptual, so they bind per interaction, not on the average.** This is the one to lead with. Latency targets are conventionally set by what's achievable or by percentile habit (*p99 under 500ms*). Nielsen gives a target grounded in human limits instead. But because the limit is perceptual, **every individual interaction either cleared it or didn't** — there is no such thing as an averagely-interrupted train of thought. A service at p50 80ms and p99 4s is not fast with a rough edge; it drops one interaction in a hundred past the flow-of-thought limit, and those are the ones users remember. `metrics` already says the average lies and the tail matters; this explains *why the tail is where the human sits*.

**Second transfer — the thresholds tell you which kind of problem you have.** This is a design-decision rule, not a performance target:

- **Under ~1s** — a performance problem. Optimise.
- **1–10s** — a performance problem you also owe feedback on: the system must visibly indicate it is working.
- **Over 10s** — no longer a performance problem. It is an **architecture problem**: background the work, allow the user to leave and return, report progress against a known total. Making a 30-second operation into a 20-second one does not fix it; removing the user's obligation to wait does.

Engineers routinely treat the third case as the first and optimise into a wall.

**Third — Doherty cuts against the "fast enough" instinct.** The common engineering position is that nobody consciously perceives 300ms versus 100ms, so the work isn't worth it. Doherty's result is that conscious perception is the wrong instrument: user *behaviour* changes below the threshold — think time drops, exploration rises, throughput goes superlinear — without anyone reporting that the system feels different. **Latency work driven by complaints therefore systematically under-invests**, which is the same failure `metrics` already names as *users stop telling you because they've left*.

**Fourth — a genuine disagreement, logged under [Design Principle 3.6](../docs/METHODOLOGY.md).** Perceived latency can be bought without buying real latency: optimistic UI, skeleton screens, prefetching. **Both sides are real.** Optimistic UI legitimately satisfies the perceptual threshold and is the correct call for high-frequency, low-stakes, reliably-succeeding actions. It is also a claim about state that has not happened yet, and when the write fails the rollback lands *after* the user has moved on — worse than the wait would have been. *What decides it:* the failure rate of the underlying operation and the cost of reversing a wrong optimistic display. Cheap to reverse and rarely fails, show it optimistically; expensive to reverse or fails often, make them wait and say why. Fake progress bars sit on the far side of this and belong with principle 5 — that is deception, not perceived performance.

**Internal links.** Principle 9 (people remember the unusual) explains why slowness is disproportionately memorable — a stall is an anomaly and gets encoded as one. Principle 3 supplies the floor this sits on: speed cannot rescue a design that doesn't work. Principle 8 is the counterweight — an attractive slow product may be forgiven longer than it deserves, which is a measurement hazard, not a licence.

**Verdict:** `fold` into [`metrics`](../plugins/swe-assistant/skills/metrics/SKILL.md) — the most directly actionable engineering content in the book so far, and it lands in an existing gap rather than needing a new skill. Folded on logging.

**Open question.** The 400ms figure came from 1982 terminal transactions. The three Nielsen thresholds are perceptual and should hold; Doherty's specific number is an empirical result from a particular workload and probably should not be quoted as a universal target. Worth keeping the thresholds and the superlinearity claim, and treating 400ms as historical context rather than a number to put in an SLO.

---

### 14 — Friction isn't always bad

**What it says.** Unwanted friction should go, but not every interaction should be frictionless. Where consequences are serious, users should be made to slow down and attend to what they are about to do. Cites Böhme and Köpsell (CHI 2010) on users clicking through agreements without reading them. Closes on the designer's obligation: since what we build has tangible effects on people's lives, we should not exploit inertia, and should hold the line on security and safety.

**The study says something sharper than "people don't read," and it changes the engineering advice.** Rainer Böhme and Stefan Köpsell, *Trained to Accept? A Field Experiment on Consent Dialogs* ([CHI 2010](https://dl.acm.org/doi/10.1145/1753326.1753689)) — one dialog in 2×2×3 variations across **80,000 users** of a live privacy tool. The headline finding is **habituation**: users **"blindly accept terms the more their presentation resembles a EULA."** The resemblance itself is the failure mechanism. Two further results:

- **Politeness backfired.** Polite phrasing and buttons signalling a voluntary choice *decreased* consent, against what social psychology predicts.
- **Heuristic processing dominated systematic processing** — measured via response latency and whether users consulted help. People were not deciding; they were pattern-matching and moving on.

**The consequence, which the principle doesn't draw: a confirmation dialog inherits the trained reflex from every dialog that came before it.** Familiarity is not neutral — it is the thing that drains the gate of meaning. So *"are you sure? [OK]"* is not weak friction, it is close to no friction, and no amount of making it scarier fixes it. What works is friction that **cannot be habituated because it demands task-specific input**: typing the resource name. You cannot muscle-memory your way through `prod-cluster-eu-west-1`. [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) already recommends type-the-name; this supplies the mechanism, which is the difference between teaching it and cargo-culting it.

**And it applies to your own team, not just end users.** The `Are you sure? [y/N]` in a deploy script is trained away within a week; engineers add `--force` and alias past it. That is the same heuristic processing, in people who know exactly what the gate is for. `operational-tools` already warns that a bad tool is worse than none because it gives *the illusion of safety* — this is that failure with a named cause.

**Collides with.** [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) (the auth/RBAC callout), [`change-discipline`](../plugins/swe-assistant/skills/change-discipline/SKILL.md), [`progressive-rollout`](../plugins/swe-assistant/skills/progressive-rollout/SKILL.md) (gates), [`idempotency`](../plugins/swe-assistant/skills/idempotency/SKILL.md), and principle 5's ethics material.

**The rule the principle implies: friction should be proportional to irreversibility × blast radius, not to how dangerous the action feels.** Deleting one row of your own test data feels dangerous and isn't. Editing a config value feels routine and can be global.

**A genuine disagreement, logged under [Design Principle 3.6](../docs/METHODOLOGY.md).** The dominant usability position (Nielsen, Tognazzini) is that **undo beats confirmation** — a confirmation taxes the 99% who meant it, and gets habituated anyway, while undo costs nothing until it's needed and actually works. Against that: undo is often not implementable, and offering it where it doesn't really exist is worse than a gate. *What decides it:* **whether the action is genuinely reversible.** And engineering has a third move the UX framing misses — **change the reversibility instead of gating the action.** Soft delete with a retention window, expand-and-contract migrations, delayed execution: these convert an irreversible action into a reversible one, which beats both confirming and undoing. [`evolvable-data`](../plugins/swe-assistant/skills/evolvable-data/SKILL.md)'s expand-and-contract is exactly this — **friction as architecture**, imposed because the drop is irreversible, not because it feels risky.

**Pairs with 13 — the book's second explicit thesis/antithesis.** Principle 13 says speed is the ultimate usability metric; 14 says not always. The synthesis: **speed is the default, and friction is a deliberate purchase made where consequences are irreversible.** That two such pairs now exist is further support for Design Principle 3.6 being the right shape for derived skills — the book keeps arguing with itself on purpose.

**The ethics half, and a clean test for it.** *"Don't exploit inertia"* has a sharp operational form: **is the friction placed where the consequence is, or where the revenue is?** One-click to subscribe and seven screens to cancel is the same mechanism as a safety gate, aimed the other way. Böhme and Köpsell supply the mechanism principle 5 only asserts — this is *why* deceptive design works, and the absence of friction where consequence is high is as much a choice as its presence where consequence is low. This materially strengthens the ethics skill candidate (Standalone B).

**Verdict:** split, honestly. `fold` the engineering half into [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) — done on logging. `cluster` the ethics half with principle 5. Separately, 13+14 form **Cluster C — the pace of interaction is a design decision**, alongside Clusters A and B.

**Open question.** If habituation defeats any friction pattern once it becomes standard, then type-the-name is on a clock too — it is already common enough at GitHub, AWS, and Stripe that the reflex may be forming. Does that imply safety gates need periodic redesign, or is task-specific input structurally immune because the input can't be memorised? I suspect the latter, but the study's mechanism doesn't obviously guarantee it.

---

### 15 — First impressions matter

**What it says.** Drawing on Microsoft Research work by Chao Liu, Ryen W. White, and Susan Dumais: users who don't see or grasp a page's value within about ten seconds leave. The author's claim is that the impression is carried by **design rather than content**.

**The paper's mechanism is far more useful than the ten-second number.** *Understanding Web Browsing Behaviors through Weibull Analysis of Dwell Time* ([SIGIR 2010, pp. 379–386](https://dl.acm.org/doi/10.1145/1835449.1835513)). The move is to treat page abandonment as **system failure in reliability analysis** and fit dwell time with a Weibull distribution. What that reveals is significant **negative aging**: the hazard rate *falls* as time on page rises. A page is the opposite of a wearing machine part — the longer someone stays, the less likely they are to leave. The authors name the resulting behaviour **"screen-and-glean."**

So there are **two regimes, not a countdown**: a brief high-hazard *screening* phase, and — if it is survived — a low-hazard *gleaning* phase measured in minutes. The practical consequence is not "you have ten seconds" but **effort spent inside the screening phase has a structurally different return than effort spent anywhere else in the experience.**

**Citation hygiene — the study doesn't support the claim the principle attaches to it.** Liu, White, and Dumais establish the *shape* of abandonment, not its *cause*; nothing in a dwell-time distribution says whether people leave because of design or content. The claim that first impressions are visual is properly licensed by **Lindgaard, Fernandes, Dudek, and Brown (2006)**, *Attention web designers: You have 50 milliseconds to make a good first impression!* (*Behaviour & Information Technology*) — 50ms being far too short to read anything, which is exactly why it isolates the visual channel. **Right claim, wrong paper.** Anything derived from this principle should cite both and say which does which. Worth noting as the second citation-precision issue in the book, after principle 13's 400ms.

**The pattern worth naming — the book has now made the same statistical point twice.** Principle 13: latency thresholds are perceptual, so they bind per interaction and the average lies. Principle 15: abandonment hazard is front-loaded, so the average dwell time lies. **Both are threshold effects concealed by aggregate statistics**, and both are the lesson [`metrics`](../plugins/swe-assistant/skills/metrics/SKILL.md) already teaches — histograms over averages, the tail is where the human is. The reading keeps re-deriving the repository's own metrics discipline from the human side, which is good evidence the discipline is right rather than merely conventional.

**Collides with.** No skill cleanly, which is the finding — see the gap below. Adjacent: [`metrics`](../plugins/swe-assistant/skills/metrics/SKILL.md), [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md), [`new-team-onboarding`](../plugins/swe-assistant/skills/new-team-onboarding/SKILL.md).

**Engineering transfer — time-to-first-success is the hazard metric.** Everything shipped to other engineers has a screening phase: a library, an internal service, a CLI, a README, a first week on a team. The window is longer than ten seconds — perhaps ten minutes for a library — but the structure is identical: high early abandonment, then commitment. Concretely measurable and almost never measured: time from install to first successful call; whether the quickstart survives copy-paste; whether the first error message on misconfiguration is legible. Teams instrument the steady state and leave the screening phase dark, which is exactly backwards given where the hazard is.

**Why the screening phase is systematically under-served: curse of knowledge.** READMEs, quickstarts, and onboarding docs are written by the person with the most context — structurally the worst author for a screening-phase artifact, because they can no longer perceive the screen they are being asked to design. This is the same failure [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) already names as *the operator at 2am does not have the mental model*, and it argues for the same fix: have someone without the context walk it.

**The gap this exposes — and it is a real one.** Nothing in the repository owns **designing the first encounter with a thing you ship.** `new-team-onboarding` is deliberately the newcomer's own playbook and says so explicitly under *When NOT to use*: *"the user is asking about onboarding others… the content is reusable but the framing is different."* The repository has the receiving side and not the designing side. Skill candidate: **first-run experience** — READMEs, quickstarts, developer onboarding, first-error legibility, time-to-first-success as an instrumented metric. Holding to the build rule: recorded as a candidate, assembled at the section boundary, not built from one principle.

**Verdict:** `cluster` into **Cluster C**, and log the skill candidate above.

**Open question — a third contradiction, and unverified.** There is a research line holding that **prototypical** designs, ones resembling what people expect for their category, are judged more appealing in exactly these first milliseconds. If it holds, it collides head-on with principle 9 (the unusual is remembered) and principle 12 (differentiate to be noticed): **typicality may win the screening phase while distinctiveness wins the memory.** The deciding condition would be which risk dominates — abandonment or forgettability. I have not verified the attributions here, so this is flagged rather than logged; check before anything derived from it ships.

---

### 16 — UX design isn't timeless

**What it says.** Presents Dieter Rams' ten principles of good design (Braun, 1970s–80s) — innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough to the last detail, environmentally friendly, and as little design as possible. The author then rejects **principle 7** for UX specifically: the field and its practices endure, but no interface is timeless. How we interact with computers depends on the hardware and software available at that moment, so an interface is always a product of its time.

**The claim is true of some layers and false of others — and this book has already contradicted itself on it.** At principle 13 the note records that Miller's response-time thresholds *"have not changed in fifty years because they are properties of human perception and cognition, not of technology,"* and that a target derived from them does not go stale. Principle 16 says nothing in UX lasts. Both are right about different strata:

| Layer | Example | Half-life |
|---|---|---|
| **Human** | perceptual thresholds (13), serial position (10), cognitive load (11) | effectively fixed |
| **Concept** | undo, copy/paste, hyperlink, search, direct manipulation | decades |
| **Convention** | hamburger menu, pull-to-refresh, floating action button | ~a decade, platform-bound |
| **Expression** | skeuomorphism, flat, neumorphism, glassmorphism | a few years, fashion-driven |

The author's claim holds cleanly for **convention** and **expression** and fails for **human** and **concept** — copy-and-paste has survived every substrate change since the 1970s. This stratification is more useful than the principle as stated, because it says **where to invest**: effort in the top two layers compounds, effort in the bottom two is consumable by design.

**Rams isn't wrong; he was working a different layer.** A Braun radio's affordances are bounded by human hands, which do not change. Interfaces sit on a substrate that does. Logged as a [3.6](../docs/METHODOLOGY.md) disagreement whose **deciding condition is the layer** — Rams' longevity claim is sound for anything constrained by the body, and unsound for anything constrained by the platform.

**Collides with.** [`software-entropy`](../plugins/swe-assistant/skills/software-entropy/SKILL.md) directly — see the fold. Also [`choose-boring-technology`](../plugins/swe-assistant/skills/choose-boring-technology/SKILL.md), [`technical-debt`](../plugins/swe-assistant/skills/technical-debt/SKILL.md), [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md).

**The fold — a fourth driver of entropy that the skill is missing.** `software-entropy` names three causes of mess, and **all three require somebody to change something**: developers differ in style, stacks and requirements evolve, fixes accrete complexity. Principle 16 describes the opposite mechanism — **the artifact is untouched and the world moves under it.** Dependencies deprecate, platform conventions shift, browser defaults change, accessibility expectations rise, user expectations reset against whatever they used yesterday. **You can rot by standing still.** The mitigations differ too: linters, code review, and continuous refactoring all act on code being written, and none of them detects context drift.

**The design response is shearing layers.** Stewart Brand, *How Buildings Learn* (1994), extending Frank Duffy: a building is site, structure, skin, services, space plan, and stuff, each changing at a different rate, and an adaptive building **lets the differently-paced layers slip past one another rather than coupling them rigidly**. Brand later generalised this as *pace layering*. This is exactly the answer to principle 16: if the surface has a short half-life, the architecture's job is to make it **cheap to replace without disturbing what is slow.** That is [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md) and [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md)'s encapsulation arriving from architecture rather than from computer science — and it makes the UI's short lifespan an argument *for* clean boundaries rather than a reason to care less about it.

**Reframes an organisational argument worth having.** Teams treat a redesign as evidence the original design was wrong. Under this principle, redesign of the convention and expression layers is **scheduled maintenance**, budgeted like dependency upgrades. What *would* be a failure is a redesign that has to reach through into the concept or data layers because they were never separated.

**The trap.** *"Interfaces are products of their time"* is also the standard justification for chasing fashion. The condition that separates the two: does the change serve a **substrate shift** — touch arrived, screens shrank, a new accessibility requirement landed — or a **fashion cycle**? Substrate shifts justify rework. Fashion cycles spend the user's relearning budget, which principle 9 bounds with MAYA and principle 12 prices as innovation tokens.

**Resolves an apparent conflict with `choose-boring-technology`.** Boring technology says prefer long track records; principle 16 says interfaces are of their moment. These only conflict if the system is one layer. Once stratified the rule is clean: **boring substrate, disposable surface.**

**Verdict:** `fold` into [`software-entropy`](../plugins/swe-assistant/skills/software-entropy/SKILL.md) — done on logging. Not a Cluster C member: C concerns the *user's* time inside an interaction, this concerns the *artifact's* lifespan. Standing alone for now as the durability thread; likely to attract company later in the book.

**Open question.** Does the four-layer stratification above hold up, or is it my construction? The book supplies the claim and the Rams list but not the strata. Before anything ships on it, check whether an established layering already exists in the HCI literature — inventing a taxonomy the field already has under another name would be a citation failure of the kind principle 15 just exhibited.

---

### 17 — Nothing lasts forever

**What it says.** A digital design's longevity is guarded by whoever commissioned it. When the people on the client side turn over, the odds of the design surviving intact go to roughly nothing. The author's own read is that this is something to accept rather than fight.

**Maintainer's read, and I agree: this is a personal reflection rather than a working principle.** Logged for completeness. What follows is the small amount that does transfer, and an explicit note that it required no change to the skill set.

**The one transferable claim — and the repository already holds it.** If design survival is an organisational property rather than a quality property, then the thing that outlives turnover is **the written rationale, not the artifact**. [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) already says this twice and better: the document *"becomes valuable later, asymmetrically — decisive six months later when someone asks why the system works this way, or when a new engineer needs the context,"* and, on losing edit history, *"that history is often the most valuable part — it's what stops the team relitigating a settled decision next year."* Checked before writing; no addition warranted.

**The distinction worth keeping — 16 and 17 decay for different reasons and take different countermeasures.** Both say the work won't last, which makes them easy to collapse into one idea. They shouldn't be:

| | Cause | Countermeasure |
|---|---|---|
| **16** | context drift — the artifact is untouched, the world moves | shearing layers; make fast layers cheap to replace |
| **17** | ownership turnover — the artifact is fine, the guardian left | written rationale that survives the person |

Neither countermeasure helps against the other's cause. Clean boundaries do nothing when a new stakeholder wants a fresh look; a decision record does nothing about a deprecated dependency. **The pairing is the contribution here**, not principle 17 alone.

**A link back to existing skills.** [`software-entropy`](../plugins/swe-assistant/skills/software-entropy/SKILL.md) and [`changing-legacy-code`](../plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) both instruct the reader to find out *why* strange code exists before changing it. Principle 17 explains why that information is usually unavailable: **the person who held the reasoning moved on and it was never written down.** 17 is the supply side of the problem those two skills handle on the demand side. Worth knowing; not worth a skill edit.

**Verdict:** `context`. **The first principle in this reading to produce no change to the skill set** — recorded deliberately, since a reading practice that always finds something to add is not reading, it is confirmation bias with a commit history.

**Separate observation, not derived from this principle.** Grepping for it while checking the above: **Conway's Law appears nowhere in the repository** — not in any skill, not in the docs. Principle 17's mechanism is roughly its dynamic form (the system tracks the org, so when the org changes the system comes under pressure to change with it, independent of technical merit). That absence is a real gap and probably a significant one, but it is far too large to hang off a personal reflection at the end of a UX chapter. Logged here so it isn't lost.

---

---

## Consider — what the section produced

*Written at the section boundary, per the build rule. The Consider section ran principles 1–17.*

**Five new skills**, taking the repository from 44 to 49:

| Skill | Built from | Fires when |
|---|---|---|
| `interface-decisions` | Cluster A (2, 3, 7, 8) | building or changing a user-facing surface |
| `rationing-attention` | Cluster B (6, 9, 10, 11, 12) | deciding what to emphasize, in any medium |
| `interface-tradeoffs` | 11/12 pair, generalised via Design Principle 3.6 | a contested design call |
| `interface-copy` | Standalone from 6 | writing labels, errors, empty states |
| `design-ethics` | Standalone B (5, mechanism from 14) | a design that may work against its user |

**Folds completed at the boundary** (held per the build rule):

- `technical-design-process` **Step 3** — stakeholders are not users; establish context of use; the best solution may not be the one anyone described, bounded above by MAYA. *(principles 1, 4, 9)*
- `technical-design-process` **prototype callout** — the aesthetic-usability effect as a validity caution on prototype feedback. *(principle 8)*
- `design-doc` — the *UI/UX Changes* template section given its weight. *(principle 3)*

**Folds completed during the reading:** `metrics` (13), `operational-tools` (14), `software-entropy` (16).

**Two judgments worth recording.**

`rationing-attention` was deliberately built **domain-agnostic** rather than as a UX skill, following the note at principle 11: the constraint is cognitive, so it holds for logs, alerts, dashboards, and documents as much as for screens — and this repository was already applying it in four places without naming it. Interfaces are its primary worked domain, not its scope.

`interface-tradeoffs` is the only skill in the repository whose *shape* came from the maintainer rather than a source. It is Design Principle 3.6 given a situation to fire in.

**Built after the section closed:** [`first-run-experience`](../plugins/swe-assistant/skills/first-run-experience/SKILL.md) (from principle 15) — READMEs, quickstarts, first-error legibility, time-to-first-success as an instrumented metric. The gap was real and the repository had stated it itself: `new-team-onboarding` explicitly declined the designing side under *When NOT to use*, and that bullet now routes here. Two supporting finds at build time — `configuration` already argued that a config with no required values is the friendliest possible first run, the discipline operating unnamed; and Newton's 1990 tapping study (tappers predicted 50% recognition, listeners managed 3 of 120) turned out to be the cleanest available statement of why an author cannot review their own README.

**Also outstanding:** Conway's Law appears nowhere in the repository (noted at principle 17), and the four-layer durability stratification proposed at principle 16 is unverified against the HCI literature.

---

<!-- Next entry goes here. Keep the four-part shape. -->
