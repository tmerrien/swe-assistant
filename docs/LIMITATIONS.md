# Limitations

This document catalogs the limitations of *SWE Assistant* honestly. It distinguishes limitations of the **methodology** (see [`METHODOLOGY.md`](./METHODOLOGY.md)) from limitations of *this specific implementation* (the 36 skills currently in this repository). Both are presented openly because a project that does not name its limitations cannot be evaluated, and a project that overclaims cannot be trusted.

This document is intended to be revised as the project evolves, and as users — particularly faculty and researchers — identify limitations not yet captured here.

---

## 1. The specific skills are one author's interpretation

The 36 skills in this repository reflect one author's reading of one set of source materials. They are presented as an **existence proof** of the methodology — what the method produces in practice — not as authoritative content.

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

## 7. Coverage gaps within the chosen scope

Even within the project's chosen scope — early- to mid-career software engineering practice — the current 36 skills do not cover every recurring situation a learner may face. Known gaps include:

- Technical interviewing and job search.
- Salary negotiation and compensation discussions.
- Dealing with difficult or toxic team dynamics.
- Mental health and burnout in early-career engineering work.
- Imposter syndrome at level transitions (partially covered by `growth-obstacles`, but not specifically).
- Specific stack or language onboarding (the skills are stack-agnostic by design).
- Non-IC trajectories (engineering management, technical writing, developer relations).

Some of these gaps reflect deliberate scope choices; others reflect coverage the author has not yet built. The project's status documentation and contribution guidelines invite proposals for new skills.

---

## 8. Scope is software engineering only

The methodology is presented as a general framework for packaging professional wisdom for AI-mediated coaching, but the implementation addresses only software engineering practice. Related domains where the methodology might transfer — data engineering, machine-learning engineering, security engineering, product management, technical writing, scientific computing — are not addressed by this repository and would require separate implementations.

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

This limitation is documented honestly because the count is non-trivial and the critique is reasonable; users should know what design decision they're consuming.

---

## 13. Living document

This limitations document is itself incomplete. Users who identify additional limitations — particularly faculty evaluating the project for academic use, or researchers comparing it to alternative approaches — are invited to open an issue on the GitHub repository or contact the maintainer directly.

The project is more credible for naming its limitations than for hiding them. Additions and corrections to this document are welcomed in the same spirit as additions to the skills themselves.

---

*See also:* [`METHODOLOGY.md`](./METHODOLOGY.md) for the methodology that the limitations apply to; [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) for the theoretical grounding that supports plausibility (but not empirical validation); [`FOR-EDUCATORS.md`](./FOR-EDUCATORS.md) for practical guidance on use despite these limitations.
