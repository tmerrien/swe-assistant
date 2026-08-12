# Theoretical Foundations

This document situates *SWE Assistant* within the educational, cognitive, and software-engineering literature it draws on. It grounds the **methodology** the project proposes — situation-triggered AI-coaching skills with strong source attribution — rather than the specific content of any individual skill in this repository. The 49 skills shipped here are one author's implementation; the methodology is intended to be applied by others, with different sources, different framings, and different content.

---

## 1. The problem context

Two trends in software engineering education are converging in ways that the existing toolkit does not yet address well.

**The first** is a long-standing pattern in professional education: learners can be exposed to expert practice through reading and instruction without the practice actually appearing in their day-to-day work. Reading a book on code review does not reliably produce better code reviews; the lessons remain in the highlights rather than in the hands. This gap — sometimes characterized as the gap between *knowing-that* and *knowing-how* (Ryle, 1949) — is foundational to the entire literature on professional skill development.

**The second** is the rapid integration of large language models into software engineering work. AI assistants can now produce competent-looking code without the user developing a corresponding mental model. This creates a real risk that learners can ship work without building the understanding that traditionally accompanied that work — what some authors have termed *cognitive offloading at the expense of skill acquisition* (Risko & Gilbert, 2016; Gerlich, 2025).

The methodology this project proposes treats both problems as instances of the same underlying issue: **expert practice needs to be surfaced at the moment of action, in a form that prompts the learner's own thinking rather than substituting for it.**

---

## 2. Stages of competence — Broadwell's framework

The project's framing of *what* is being developed comes from Broadwell's (1969) four-stage model of competence:

1. **Unconscious incompetence** — the learner does not know what they do not know.
2. **Conscious incompetence** — the learner can identify the gap.
3. **Conscious competence** — the learner can perform the practice with effort and attention.
4. **Unconscious competence** — the practice is internalized and performed without deliberate attention.

This framework provides the central design goal for the methodology: **accelerate the climb from Stage 1 to Stage 3.** Stage 4 (automaticity) is a function of accumulated practice and cannot be taught directly; Stage 2 → Stage 3 is teachable, and Stage 1 → Stage 2 is in many ways the highest-leverage transition because learners trapped in Stage 1 cannot ask for help with gaps they cannot see.

The skill format used by this project is designed to support both transitions: by surfacing relevant frameworks at moments when learners might otherwise fail to recognize that a framework applies (Stage 1 → 2), and by providing scaffolding for deliberate execution once recognition occurs (Stage 2 → 3).

---

## 3. Deliberate practice

Ericsson, Krampe, and Tesch-Römer (1993) and subsequent work argue that expert performance in any domain develops primarily through *deliberate practice* — sustained, effortful activity specifically designed to improve performance, with feedback, on tasks just beyond current capability. The implication for software engineering education is that exposure to expert content (lectures, books) is insufficient; learners must repeatedly perform the relevant activities with attention to improvement.

The methodology presented here is designed to support deliberate practice rather than substitute for it. The skills do not perform the work; they provide structure (checklists, questions, frameworks) that learners then apply themselves. This is intentional: a skill that performed the engineering task would interrupt the very practice loop that produces competence.

---

## 4. Scaffolding and the Zone of Proximal Development

The pedagogical mechanism the project relies on is *scaffolding*, originally articulated by Wood, Bruner, and Ross (1976) and grounded in Vygotsky's earlier *Zone of Proximal Development* (Vygotsky, 1978). Scaffolding refers to temporary structural support that enables a learner to perform a task at the edge of their capability — support that is gradually withdrawn ("faded") as the learner internalizes the task.

The project's first design principle — *prompt the thinking, do not replace it* — is a direct application of scaffolding theory. Each skill is intended to be a temporary structure. The explicit goal, stated in multiple skill bodies, is that **the skill should become unnecessary as the learner internalizes the practice.** A skill that the learner remains permanently dependent on is, in scaffolding terms, a failed scaffold.

This design choice distinguishes the methodology from alternatives that aim for permanent AI assistance with the underlying work.

### 4.1 Marking critical features — the warrant for proactive prompting

Wood, Bruner, and Ross decompose scaffolding into six tutoring functions. One of them, **marking critical features**, is the tutor's act of drawing the learner's attention to aspects of a task that are relevant but that the learner has not noticed. It is not a supplement to scaffolding; it is constitutive of it.

This function supplies the theoretical warrant for a property the methodology requires of every skill at runtime (see [`METHODOLOGY.md`](./METHODOLOGY.md), Section 10.7): skills surface adjacent concerns the situation implies **even when the user has not asked about them**.

The argument is a direct consequence of the competence model in Section 2. A learner in unconscious incompetence cannot formulate a request about a gap they are unable to perceive; the request presupposes the awareness that is precisely what is missing. A system that responds only to what is asked is therefore structurally incapable of serving the stage 1 → stage 2 transition, which this project identifies as the highest-leverage one. Reactive help can support a learner who already knows what to ask; it cannot create that knowledge.

Two constraints bound the function, and both matter for it to remain scaffolding rather than instruction:

1. **Volume.** Marking is selective by definition — a tutor who marks every feature has marked none, and merely relocated the learner's problem from ignorance to triage. The protocol accordingly limits proactive surfacing to one or two items ranked by consequence.
2. **Expertise sensitivity.** Kalyuga's (2007) expertise-reversal effect predicts that guidance which benefits novices degrades expert performance, because redundant guidance imposes extraneous cognitive load on a learner who already holds the relevant schema. Proactive prompting must therefore attenuate as demonstrated expertise rises — the same calibration the methodology already applies to diagnostic depth.

The distinction that keeps this compatible with Design Principle 1 (*prompt the thinking; do not replace it*) is between **surfacing a consideration** and **supplying a conclusion**. Naming an unexamined stakeholder, consequence, or artifact hands the learner something to reason about. Naming the answer removes the reasoning. The first is scaffolding; the second is the substitution the methodology exists to avoid.

### 4.2 Perry's scheme — the warrant for preserving disagreement

Perry's (1970) scheme of intellectual and ethical development describes a progression through nine positions, conventionally grouped into four stages:

1. **Dualism** — the belief that every problem has a right answer, that the learner's task is to acquire those answers, and that authorities possess them.
2. **Multiplicity** — recognition that authorities disagree, initially experienced as all opinions being equally valid.
3. **Relativism** — the capacity to weigh positions using evidence, and to see knowledge as contextual.
4. **Commitment within relativism** — making reasoned choices and holding them, while accepting that they were made under uncertainty.

The scheme supplies the warrant for a property the methodology requires of every skill in contested territory (see [`METHODOLOGY.md`](./METHODOLOGY.md), Section 3.6): **where practitioners genuinely disagree, a skill presents the disagreement rather than resolving it.**

The argument runs directly from the project's stated goal. This methodology exists to move practitioners toward independent judgment. A skill that always supplies a single answer trains the reader to expect one — which is the defining feature of dualism, the stage the project is trying to move people out of. **Consistently resolving contested questions on the learner's behalf is therefore not merely unhelpful; it is actively counter-developmental**, however correct each individual answer happens to be.

Two constraints keep this from collapsing into false balance:

1. **The disagreement must be real.** Perry's progression is not served by presenting settled questions as open. A learner taught that input validation is a matter of taste has been misinformed, not developed. The principle applies where the correct answer depends on circumstances the skill cannot know — team, scale, domain, risk tolerance — not where evidence favours one side and the author is reluctant to say so.
2. **The conditions must be supplied.** Stage 2 (multiplicity) — *"everyone disagrees, so nothing can be known"* — is a worse destination than dualism for practical purposes. Naming a disagreement without naming what determines the answer leaves the learner there. The skill's contribution is the **conditions**, not the controversy.

This also explains why the repository's most useful passages tend to be conditional rather than prescriptive: the schemaless-is-sometimes-right conditions in `evolvable-data`, the complexity-transfer table in `managing-complexity`, the inertia matrix that makes *leave it alone* a legitimate answer. Each presents a genuine disagreement together with the circumstances that settle it.

---

## 5. Situated cognition and just-in-time learning

Brown, Collins, and Duguid (1989) argue that knowledge is fundamentally situated — knowledge learned in the context of authentic activity is more transferable and more useful than knowledge taught in abstraction. This finding underlies the project's second design principle: *trigger on situations, not on topics*.

A skill that activates only when the user is *about to take a specific action* (write a commit message, review a PR, prepare for a 1:1) presents its content at the moment of authentic activity. A skill that activates on topical mention ("tell me about code reviews") provides decontextualized information — what the literature characterizes as inert knowledge (Whitehead, 1929).

The situation-trigger mechanism, supported by the underlying LLM's pattern-matching against the skill's `description` field, is a technical implementation of just-in-time learning theory.

---

## 6. Cognitive load theory

Sweller's (1988) cognitive load theory distinguishes intrinsic load (the inherent difficulty of the material), extraneous load (load imposed by the presentation), and germane load (load that contributes to schema construction). Effective instructional design minimizes extraneous load and maximizes germane load.

The methodology applies this in two ways. First, by surfacing only the skill relevant to the user's current situation, it reduces extraneous load from material the learner is not currently in a position to use. Second, the consistent skill body structure (Source, Pillars, Mindset, How to Run, Output Style, When NOT to Use) reduces the load of orienting to each new skill — once one skill is understood, the structure transfers.

---

## 7. Apprenticeship patterns and the software craftsmanship tradition

Hoover and Oshineye's *Apprenticeship Patterns* (2009) articulates the modern software-craftsmanship view of skill development: practice is acquired through deliberate work alongside more experienced practitioners, structured by recognizable patterns (e.g., *Expose Your Ignorance*, *Kindred Spirits*, *Practice, Practice, Practice*).

The skill format used by this project can be understood as a partial mechanization of apprenticeship: capturing the situation-pattern matching that experienced practitioners perform implicitly, and surfacing the relevant pattern at the moment a less experienced practitioner faces the situation. This is not a replacement for human mentorship (which the skills consistently route users toward) but a low-cost supplement to it, particularly at scale.

---

## 8. AI-augmented learning — emerging literature

The integration of AI tools into education is an active area of inquiry, and the literature is unsettled. Early empirical work suggests that the *manner* of AI use matters more than the *quantity*: learners who use AI as a tutor (asking for explanations, testing their understanding, soliciting feedback on their own work) develop competence; learners who use AI to produce answers may produce work without corresponding learning (Risko & Gilbert, 2016; Lee et al., 2025).

This project's design choice — to coach the user's thinking rather than perform the work — is a methodological commitment in a still-contested space. The literature does not yet provide settled empirical support for this commitment; the position is principled rather than evidenced. See [`LIMITATIONS.md`](./LIMITATIONS.md) for further discussion.

---

## 9. What the theoretical grounding does and does not establish

The theoretical foundations above support the *plausibility* of the methodology. They do not establish that the specific implementation in this repository is effective. Validating the implementation would require empirical study — controlled comparison with alternative approaches, measurement of learning outcomes over time, and replication across populations. None of that work has been done. The methodology is offered as a principled proposal supported by relevant educational and cognitive theory; the empirical question is open.

This is also why the specific skills in this repository are presented as *one author's implementation*, not as authoritative content. Faculty and other educators are explicitly invited to disagree with skill content, fork the implementation, build alternatives, and (ideally) study the results. The methodology is the proposed contribution; the skills are an existence proof of what the methodology produces.

---

## References

- Broadwell, M. M. (1969). *Teaching for Learning (XVI)*. The Gospel Guardian, 20(41).
- Brown, J. S., Collins, A., & Duguid, P. (1989). Situated cognition and the culture of learning. *Educational Researcher*, 18(1), 32–42.
- Ericsson, K. A., Krampe, R. T., & Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. *Psychological Review*, 100(3), 363–406.
- Gerlich, M. (2025). AI tools in society: Impacts on cognitive offloading and the future of critical thinking. *Societies*, 15(1).
- Hoover, D. H., & Oshineye, A. (2009). *Apprenticeship Patterns: Guidance for the Aspiring Software Craftsman*. O'Reilly Media.
- Perry, W. G., Jr. (1970). *Forms of Intellectual and Ethical Development in the College Years: A Scheme*. Holt, Rinehart and Winston.
- Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *Educational Psychology Review*, 19(4), 509–539.
- Lee, H. P., et al. (2025). The impact of generative AI on critical thinking. *Proceedings of CHI 2025*.
- Riccomini, C., & Ryaboy, D. (2021). *The Missing Readme: A Guide for the New Software Engineer*. No Starch Press.
- Risko, E. F., & Gilbert, S. J. (2016). Cognitive offloading. *Trends in Cognitive Sciences*, 20(9), 676–688.
- Ryle, G. (1949). *The Concept of Mind*. Hutchinson.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.
- Vygotsky, L. S. (1978). *Mind in Society: The Development of Higher Psychological Processes*. Harvard University Press.
- Whitehead, A. N. (1929). *The Aims of Education and Other Essays*. Macmillan.
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89–100.

---

*See also:* [`METHODOLOGY.md`](./METHODOLOGY.md) for the explicit method derived from these foundations; [`LIMITATIONS.md`](./LIMITATIONS.md) for what this grounding does and does not claim; [`FOR-EDUCATORS.md`](./FOR-EDUCATORS.md) for practical pedagogical use.
