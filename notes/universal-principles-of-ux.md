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

<!-- Next entry goes here. Keep the four-part shape. -->
