# Limitations

This document catalogs the limitations of *SWE Assistant* honestly. It distinguishes limitations of the **methodology** (see [`METHODOLOGY.md`](./METHODOLOGY.md)) from limitations of *this specific implementation* (the 49 skills currently in this repository). Both are presented openly because a project that does not name its limitations cannot be evaluated, and a project that overclaims cannot be trusted.

This document is intended to be revised as the project evolves, and as users — particularly faculty and researchers — identify limitations not yet captured here.

---

## 1. The specific skills are one author's interpretation

The 49 skills in this repository reflect one author's reading of one set of source materials. They are presented as an **existence proof** of the methodology — what the method produces in practice — not as authoritative content.

**Specific implications:**

- Faculty are expected to disagree with specific skills. Disagreement is not a failure mode; it is the intended response. The skills are a worked example, not a curriculum.
- Different authors applying the same methodology to the same situations will produce different skill bodies. This is a feature of the methodology, not a bug.
- A faculty member may adopt the methodology while rejecting most or all of the current skill content. The methodology and the implementation are separable artifacts.
- Where the project's documentation invites use, this invitation extends to forking, modifying, replacing, and producing alternative implementations — not only to consuming the current one.

---

## 2. No empirical validation

The project has not been subjected to formal empirical evaluation. Specifically:

- No measurement of learning outcomes in users who adopt the skills.
- No controlled comparison with alternative pedagogical approaches (traditional reading lists, instructor-led teaching, unstructured AI assistance).
- No long-term follow-up on whether internalization (the design goal stated by Principle 1) actually occurs.
- No measurement of trigger accuracy at scale beyond the author's own verification process.

The methodology rests on theoretical principles drawn from cognitive and educational research (see [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md)). Those principles support the *plausibility* of the approach; they do not constitute evidence that *this implementation* (or any implementation of the methodology) produces the intended outcomes. The empirical question is open.

Establishing empirical support would require controlled study in actual courses with appropriate ethical review (IRB or equivalent), validated assessment instruments, and replication across institutions and student populations. None of that work has been done. Faculty who wish to use the project in research are encouraged to make contact.

---

## 3. Source selection bias

The current skills draw heavily from a small set of sources, most notably *The Missing Readme* (Riccomini & Ryaboy, 2021). Many traditions and perspectives are not represented:

- **Academic software engineering research.** The skills draw primarily from practitioner literature rather than peer-reviewed CS-education or SE research.
- **Alternative paradigms.** Functional programming, formal methods, embedded engineering, security engineering, and machine-learning engineering are largely absent.
- **Non-Western and non-Anglophone engineering cultures.** All sources are English-language and reflect predominantly North American / Western European engineering norms.
- **Marginalized perspectives.** The literature drawn from is dominated by canonical voices in the industry; perspectives from underrepresented groups in engineering are not specifically surfaced.

This is a limitation of *this implementation*, not the methodology. An adopter could apply the same methodology drawing from a different source base and produce a substantially different — and arguably more representative — skill set.

---

## 4. AI dependency for primary intended use

While each `SKILL.md` is a readable standalone document and can be used as plain reference material, the primary intended mode of use — auto-triggered coaching during conversation — requires Anthropic's Claude (via Claude Code or Claude Cowork). This couples the work to a specific commercial AI product.

**Implications:**

- Users without access to Claude cannot use the auto-triggering mechanism.
- The skill format may not be directly portable to other AI platforms (OpenAI, Google, open-source LLMs) without translation work.
- Continued usability depends on Anthropic maintaining the plugin format and the relevant runtime.
- Institutional adoption may face procurement, data governance, or AI-policy constraints that vary by institution.

The methodology generalizes beyond Claude — situation-triggered coaching could be implemented in any sufficiently capable LLM platform — but the specific implementation does not. A future direction is platform-neutral skill formats.

---

## 5. No assessment instrument

The project does not include any instrument for measuring whether learners using the skills have actually developed the relevant competence. Educators wishing to assess outcomes must develop or adapt their own assessments.

Possible assessment approaches include:

- Code-review quality rubrics (for `code-review` skill outcomes).
- Design-document quality assessments (for `design-doc` outcomes).
- Self-assessment instruments using the four-pillar rubric (for general competence development).
- Behavioral observation in subsequent project work.

None of these are provided in this repository.

---

## 6. Trigger description bootstrap problem

Trigger descriptions are written and verified by the author against a small set of imagined prompts. In practice, descriptions are reliably accurate only after they have been tested against many real-world conversations. New skills typically over-fire or under-fire until refined through use.

The methodology describes the refinement loop (see [`METHODOLOGY.md`](./METHODOLOGY.md), Section 8) but does not automate it. Adopters should expect to revise descriptions based on observed misfires; the current skills will likewise improve as use accumulates.

---

## 6a. Proactive prompting is theoretically motivated but empirically untested

Section 10.7 of [`METHODOLOGY.md`](./METHODOLOGY.md) requires skills to surface adjacent concerns the user has not asked about. The rationale is principled — a learner in unconscious incompetence cannot request help with a gap they cannot perceive, so a purely reactive system cannot serve the transition the methodology treats as most valuable — and it is grounded in an established scaffolding function (*marking critical features*; Wood, Bruner, & Ross, 1976).

Neither the rationale nor the grounding establishes that the practice works as implemented here. Specific open questions:

- **The volume limit is a judgment, not a finding.** "One or two items, ranked by consequence" is a plausible reading of what keeps marking selective; it is not derived from evidence about how many unsolicited prompts a learner can absorb before disregarding all of them.
- **Expertise calibration is unmeasured.** The methodology instructs skills to attenuate proactive prompting for demonstrated expertise, per the expertise-reversal effect (Kalyuga, 2007). Whether an LLM reliably infers expertise from conversational signals — and whether it attenuates correctly when it does — has not been tested.
- **Reactance is not accounted for.** Unsolicited advice can produce resistance rather than reflection, and the conditions under which proactive prompting helps versus irritates are not established for this format.
- **It may worsen a documented risk.** A system that volunteers considerations the user had not reached could deepen the cognitive-offloading concern described in Section 1 of [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) — outsourcing not only answers but the noticing that should precede them. The methodology's response is to surface considerations rather than conclusions, but whether that distinction survives contact with real use is unknown.

This limitation is recorded because the change is recent, affects every skill in the repository simultaneously, and is more speculative than most of the methodology it sits inside.

---

## 7. Coverage gaps within the chosen scope

Even within the project's chosen scope — early- to mid-career software engineering practice — the current 49 skills do not cover every recurring situation a learner may face. Known gaps include:

- Technical interviewing and job search.
- Salary negotiation and compensation discussions.
- Dealing with difficult or toxic team dynamics.
- Mental health and burnout in early-career engineering work.
- Imposter syndrome at level transitions (partially covered by `growth-obstacles`, but not specifically).
- Specific stack or language onboarding (the skills are stack-agnostic by design).
- Non-IC trajectories (engineering management, technical writing, developer relations).
- ~~**Professional ethics.**~~ **Partially closed.** [`design-ethics`](../plugins/swe-assistant/skills/design-ethics/SKILL.md) now covers deceptive interface patterns, the limits of the ACM Code, and how an engineer raises the objection. What remains uncovered: ethics outside the interface — data retention, model and algorithmic harm, workplace conduct, whistleblowing. The skill is also **jurisdictionally anchored to one maintainer's position** (Canada/Ontario) and teaches *find your regulator* rather than asserting a general regime; adopters elsewhere should expect to replace that section.

Some of these gaps reflect deliberate scope choices; others reflect coverage the author has not yet built. The project's status documentation and contribution guidelines invite proposals for new skills.

---

## 7a. The career model stops well short of a full career

[`JOURNEY.md`](../JOURNEY.md) presents five stages — Newcomer, Ramp-Up, Contributor, Operator, Owner — adapted from Riccomini and Ryaboy. That map is inherited wholesale from one book, and it is narrower than its five-stage presentation suggests.

- **It covers roughly junior through senior, gesturing at staff.** The arc beyond that — staff, principal, distinguished, and the very different work those roles involve — is out of scope. An engineer who has reached the Owner stage has not finished the journey; they have finished *this map*.
- **It is a single-track individual-contributor model.** Engineering management, technical program management, developer relations, architecture, and research tracks diverge from it early and are not represented (see also Section 7).
- **Stage boundaries are not empirical.** They are a pedagogically useful carving, not a validated developmental sequence. No evidence is offered — here or in the source — that engineers move through these stages in this order, or that the boundaries fall where the model places them.
- **Level vocabulary does not transfer between companies.** What one organization calls "senior" another calls "mid," and the ladders differ enough that a stage name is a rough orientation rather than a portable claim.

The stages remain useful for their actual purpose: tagging which skills tend to matter when, and noticing when a stage is under-served. They should not be read as a complete or authoritative account of an engineering career, and the repository does not have the sources to make one.

---

## 8. Scope is software engineering only

The methodology is presented as a general framework for packaging professional wisdom for AI-mediated coaching, but the implementation addresses only software engineering practice. Related domains where the methodology might transfer — data engineering, machine-learning engineering, security engineering, product management, technical writing, scientific computing — are not addressed by this repository and would require separate implementations.

**What "software engineering" is taken to include.** Interface and experience design is treated as *within* that scope, not adjacent to it. This is a deliberate position and worth stating, because an earlier reading of this section treated user-facing design as out of scope.

The repository already contains a substantial amount of interface-design material. [`operational-tools`](../plugins/swe-assistant/skills/operational-tools/SKILL.md) is entirely concerned with designing tools that operators can actually use; [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md) treats an API as a surface that other people consume and warns about implicit knowledge; [`logging`](../plugins/swe-assistant/skills/logging/SKILL.md) concerns what a human reads under pressure; [`configuration`](../plugins/swe-assistant/skills/configuration/SKILL.md) concerns what an operator must reason about; [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) carries the principle of least astonishment.

The boundary previously implied was therefore not *design versus engineering*. It was **interfaces for developers and operators count as engineering; interfaces for end users do not** — a distinction that does not survive being stated plainly. Audience, goal, context of use, and not surprising people are the same considerations on either side of it.

The practical case is stronger still for the engineers this project is written for. An engineer at a small company owns outcomes end to end and makes interface decisions whether or not anyone calls them design. Withholding that material describes a team structure most of the intended audience does not have.

This does **not** extend the scope to design as a discipline — brand systems, visual identity, and design practice as a career remain outside it. The claim is narrower: an engineer who owns a user-facing outcome is doing interface design as part of engineering, and the project should serve that.

The four-pillar competence rubric used here (Technical Knowledge, Execution, Communication, Leadership) is plausibly transferable across many engineering disciplines but has not been validated outside the context of *The Missing Readme*'s framing.

---

## 9. Author position

This project is built by a single contributor: a final-year computer science student who has not yet held a full-time software engineering position at the time of authorship. The work draws heavily on cited sources rather than on first-hand expertise in many of the situations the skills address.

This is acknowledged as both a transparency note and a limitation:

- The author's interpretations of source material may differ from how a more experienced practitioner would render the same ideas.
- The author's experience-based intuitions about which situations matter most, and which framings land most usefully, are limited.
- AI tools (Claude) were used extensively in drafting and refining the skill bodies, the supporting documents, and this limitations document itself. The author's editorial judgment was exercised throughout; nonetheless, the AI's framings and biases are present in the work.

A more experienced practitioner adopting the methodology, or a research team with substantial industry experience, would likely produce different and arguably stronger content.

---

## 10. Format constraints

The Markdown skill format with YAML frontmatter is well-suited to the AI-coaching use case but constrains what the skills can do:

- No interactive elements (quizzes, code execution, embedded video).
- No adaptive sequencing (one skill body, regardless of the user's prior history).
- No personalized content (the skill is the same for every user).
- Limited multimedia (text and inline diagrams only).

A richer format — interactive notebook, dedicated web application, or platform-integrated tooling — could support pedagogical patterns the current format cannot. Whether the gains would justify the additional development cost is an open question.

---

## 11. Cultural and linguistic constraints

All content is in English. All cited sources are English-language and predominantly North American or Western European in origin. The skills' framings of professional behavior (e.g., 1:1 meeting culture, code-review norms, manager relationships) reflect cultural assumptions that are not universal.

Adopters in other cultural contexts may need to substantially modify both content and framings. Translation alone is not sufficient.

---

## 12. Skill count and the depth-vs-breadth question

User feedback has at times suggested the plugin contains *too many skills* — that a smaller, more thoroughly developed set would be more useful than the current breadth. The most explicit version: *"I would narrow the list either by collapsing multiple skills into a single skill, or parking a multiple of these for an extended period of time. I think 10 would be a large plugin."*

This critique was taken seriously but the project has not, at the time of writing, acted on the count-reduction prescription. The reasoning:

- The classical evidence for choice-overload (Iyengar & Lepper, 2000) and decision-latency cost (Hick's Law) applies primarily to **user-facing menus** where the user must scan and choose. Auto-triggered skills like the ones in this plugin bypass this mechanism — the system selects the skill for the user based on situational match, not the user from a list. The "too many to choose from" cost largely does not apply.
- However, the **depth** concern *within* the feedback is well-founded: thin or under-developed skills hurt perceived quality and provide little value when they fire. Per-skill thoroughness — substantive content, visible source attribution, multiple use-case considerations, mode-branching where novices and experts need different treatment — is the better-supported response than reducing count.
- A focused **depth audit** of the current skills (which ones genuinely earn their keep, which have become redundant with later additions, which need substantially more content) is a credible piece of future work and is welcomed as a contribution from any user or fork.

The choice not to consolidate is consistent with the project's worked-example positioning (Section 1 above): the skill set is offered as one author's implementation, not as a curated curriculum. Forks that prefer a different breadth/depth balance are exactly the kind of derivative the methodology supports.

### The count has a measured runtime cost, not just a rhetorical one

The argument above is about pedagogy. There is also a hard constraint, measured against Claude Code 2.1.220:

The runtime sends Claude a **skill listing** — each skill's name plus its `description` — and caps that listing's size. Two settings govern it: `skillListingMaxDescChars` (default **1536**, a per-skill cap) and `skillListingBudgetFraction` (default **0.01**, the share of the context window the whole listing may occupy, computed as `contextTokens x fraction x 4 chars`).

**When the listing exceeds the budget, descriptions are not shortened — they are dropped whole, skill by skill, in priority order.** A skill that does not fit is sent as **name only**. Since triggering is a semantic match against the description, a name-only skill is effectively unmatchable except by exact name. Already-activated and bundled skills are protected; the rest compete.

At 49 skills the full listing is **50,174 characters (~12,500 tokens)**. Against the default 0.01 fraction that is an 8,000-character budget, and roughly **42 of 49 skills would be sent without descriptions**. Fitting all of them requires a fraction of about **0.063**, which spends ~6.3% of a 200k context on the skill listing *on every turn*.

This is the real cost of breadth, and it is worth stating plainly:

- **Every skill added taxes every conversation**, whether or not it fires.
- **The failure mode is silent.** A skill dropped from the listing does not error; it simply never triggers, and nothing in the transcript indicates that it should have.
- **Description length is therefore a shared resource**, not a per-skill decision. The mean description in this repository is roughly 1,000 characters; halving that would halve the listing cost.
- At the current size there is **under 2,000 characters of headroom** before the next increase is needed.

None of this changes the pedagogical argument above, but it does mean the depth-versus-breadth question has a measurable second axis. An adopter running a much larger skill set should expect to either raise the fraction deliberately or write substantially shorter descriptions.

This limitation is documented honestly because the count is non-trivial and the critique is reasonable; users should know what design decision they're consuming.

---

## 13. Living document

This limitations document is itself incomplete. Users who identify additional limitations — particularly faculty evaluating the project for academic use, or researchers comparing it to alternative approaches — are invited to open an issue on the GitHub repository or contact the maintainer directly.

The project is more credible for naming its limitations than for hiding them. Additions and corrections to this document are welcomed in the same spirit as additions to the skills themselves.

---

*See also:* [`METHODOLOGY.md`](./METHODOLOGY.md) for the methodology that the limitations apply to; [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) for the theoretical grounding that supports plausibility (but not empirical validation); [`FOR-EDUCATORS.md`](./FOR-EDUCATORS.md) for practical guidance on use despite these limitations.
