# For Educators

This document describes how *SWE Assistant* can be used in software-engineering and computer-science teaching contexts. It is intended for faculty members evaluating the project for course adoption, for adaptation, or as a worked example of an AI-mediated coaching approach to professional skill development.

The project is offered as a **proposition** — a particular methodology for supporting students in the age of AI-assisted work, accompanied by one author's worked example. Faculty are explicitly invited to disagree with specific skills, fork the repository, replace content, build alternative implementations for their student populations, or use the project as discussion material precisely *because* they disagree with parts of it. The methodology generalizes; the current content does not claim authority.

---

## 1. What the project offers an instructor

Three distinct affordances, separable from each other:

1. **A methodology to adopt or adapt.** The [`METHODOLOGY.md`](./METHODOLOGY.md) document specifies how skills are constructed. Faculty can apply the same method to their own student population, domain, source materials, and pedagogical goals — producing a different skill set tailored to their course.

2. **A reference implementation to use, fork, or critique.** The 31 skills currently in this repository are immediately usable as reading material, discussion prompts, or installed AI tooling. They can also be forked and modified, or used as material for student critique.

3. **A set of design artifacts to teach with.** The skills themselves, the trigger descriptions, the four-pillar rubric, the five-stage journey map, and the supporting documentation can serve as teaching material *about* how engineering practice is structured and how AI-augmented learning tools are designed.

These three affordances correspond to three different intensities of adoption — from light (assign individual skills as readings) to heavy (build a parallel implementation as a course project).

---

## 2. Modes of use

### 2.1 As supplementary reading

Each `SKILL.md` is a standalone document that can be assigned as preparation for class discussion. The bodies are written in instructional prose accessible to early-career students. Suggested uses:

- Assign a relevant skill as preparation for a project milestone (e.g., assign `design-doc` before students draft their project design documents).
- Use a skill as the basis for a class discussion comparing the skill's framework with alternative approaches.
- Pair a skill with a primary source (e.g., assign `changing-legacy-code` alongside excerpts from Feathers, 2004) to compare the skill's distillation with the original.

### 2.2 As an installable AI tool for students

Students can install the plugin in their own Claude environments and use the skills as in-context coaching during project work. Practical considerations:

- Students need access to Claude (institutional or personal). Some institutions have organizational agreements; others do not.
- The methodology assumes students using the skills *as scaffolding for their own work*, not as a substitute for it. Course expectations should reinforce this — see [`LIMITATIONS.md`](./LIMITATIONS.md), Section 2 on the gap between the principled commitment and empirical validation.

### 2.3 As curriculum scaffolding

The structure of the skill set itself — five career stages, four competence pillars, situation-triggered tactical skills — can serve as a backbone for organizing a software engineering course. The mapping between skills and course modules is something the instructor controls (see Section 3 below).

### 2.4 As critical material

The skills can be used in seminars or upper-level courses as material to evaluate critically. Students can:

- Read several skills and identify the design principles in action.
- Critique skills for content they disagree with, gaps in coverage, or instances of overclaim.
- Compare the project's approach with alternative pedagogical tools.
- Propose improvements, write their own skills, or build a domain-specific spinoff.

This mode treats the project as a primary source about how AI-mediated pedagogy can be designed, rather than as a settled authority on engineering practice.

---

## 3. Suggested course integrations

These are starting points, not prescriptions. Adapt to your students, your course structure, and your institutional context.

### 3.1 Introductory software engineering course

A first-year or second-year SE course addressing the basic professional practices of working as a software engineer.

**Suggested skill cluster:**
- [`new-team-onboarding`](../plugins/swe-assistant/skills/new-team-onboarding/SKILL.md) — joining a team
- [`ramp-up-playbook`](../plugins/swe-assistant/skills/ramp-up-playbook/SKILL.md) — building productive context
- [`code-review`](../plugins/swe-assistant/skills/code-review/SKILL.md) — the most frequent professional communication
- [`commit-and-pr-hygiene`](../plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) — basic communication artifacts around code
- [`asking-for-help`](../plugins/swe-assistant/skills/asking-for-help/SKILL.md) — a skill students at this level explicitly need

**Suggested anchor reading:** *The Missing Readme* (Riccomini & Ryaboy, 2021), Chapters 1–3.

### 3.2 Intermediate / project-based software engineering course

Typically a junior- or senior-year course in which students work in teams on a substantive project.

**Suggested skill cluster:**
- [`contributor-playbook`](../plugins/swe-assistant/skills/contributor-playbook/SKILL.md) — owning a piece of work end-to-end
- [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) — the design artifact for project work
- [`technical-debt`](../plugins/swe-assistant/skills/technical-debt/SKILL.md) — recognizing and proposing payoff
- [`change-discipline`](../plugins/swe-assistant/skills/change-discipline/SKILL.md) — judgment about when to change things
- [`choose-boring-technology`](../plugins/swe-assistant/skills/choose-boring-technology/SKILL.md) — stack-selection discipline
- [`changing-legacy-code`](../plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) — working with code they didn't write

**Suggested anchor reading:** Feathers, *Working Effectively with Legacy Code* (2004); Fowler, *Refactoring* (2018).

### 3.3 Capstone or practicum

Senior project, industry partnership, or open-source contribution course.

**Suggested skill cluster:**
- [`operator-playbook`](../plugins/swe-assistant/skills/operator-playbook/SKILL.md) — production responsibility
- [`incident-response`](../plugins/swe-assistant/skills/incident-response/SKILL.md) — handling things that break
- [`owner-playbook`](../plugins/swe-assistant/skills/owner-playbook/SKILL.md) — driving a project at the level expected of seniors
- [`learning-toolkit`](../plugins/swe-assistant/skills/learning-toolkit/SKILL.md) — building sustainable learning habits
- [`growth-self-check`](../plugins/swe-assistant/skills/growth-self-check/SKILL.md) — reflective self-assessment
- [`growth-obstacles`](../plugins/swe-assistant/skills/growth-obstacles/SKILL.md) — impostor syndrome and Dunning-Kruger calibration

### 3.4 Professional development / career-focused course

For programs that include explicit career-development modules.

**Suggested skill cluster:**
- [`growth-self-check`](../plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- [`growth-obstacles`](../plugins/swe-assistant/skills/growth-obstacles/SKILL.md)
- [`learning-toolkit`](../plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- [`asking-for-help`](../plugins/swe-assistant/skills/asking-for-help/SKILL.md)

**Suggested anchor reading:** Hoover & Oshineye, *Apprenticeship Patterns* (2009).

---

## 4. Sample assignments

### 4.1 Apply a skill to current project work

> "Using the [`design-doc`](../plugins/swe-assistant/skills/design-doc/SKILL.md) skill as a structural guide, write a 2-page design document for the current state of your project. Submit both the document and a 1-page reflection on which sections were hardest to write and why."

### 4.2 Critique a skill

> "Pick any one skill from the SWE Assistant repository. Write a 750-word critique addressing: (a) one piece of advice in the skill you agree with and why; (b) one piece of advice you disagree with or would qualify and why; (c) one situation the skill does not address that you believe it should. Cite at least one outside source."

### 4.3 Apply the legacy-code algorithm

> "Identify a section of an open-source codebase (or our course codebase) that is unfamiliar to you and that lacks tests. Working through the [`changing-legacy-code`](../plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) skill's five-step algorithm, make a small documented change to that code. Submit a PR plus a 500-word reflection on the experience of working through the algorithm."

### 4.4 Reflective self-assessment

> "Using the four-pillar rubric in [`OBJECTIVES.md`](../OBJECTIVES.md) and the [`growth-self-check`](../plugins/swe-assistant/skills/growth-self-check/SKILL.md) skill as a frame, write a 1,500-word self-assessment of where you currently sit across the four pillars, with specific examples from the past semester's work. Identify one concrete move you will make this semester to strengthen your weakest pillar."

### 4.5 Build a new skill

> "Working in pairs, identify a recurring software-engineering situation not currently covered by SWE Assistant. Following the methodology described in [`METHODOLOGY.md`](./METHODOLOGY.md), construct a new `SKILL.md` for that situation. Submit the skill, a 1-page rationale, and an analysis of how you verified the trigger description."

### 4.6 Compare with the source

> "Read Chapter 1 of *The Missing Readme* (Riccomini & Ryaboy, 2021). Then read the skills in this repository that derive from that chapter ([`growth-self-check`](../plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`new-team-onboarding`](../plugins/swe-assistant/skills/new-team-onboarding/SKILL.md), [`ramp-up-playbook`](../plugins/swe-assistant/skills/ramp-up-playbook/SKILL.md), [`contributor-playbook`](../plugins/swe-assistant/skills/contributor-playbook/SKILL.md), [`operator-playbook`](../plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`owner-playbook`](../plugins/swe-assistant/skills/owner-playbook/SKILL.md)). Write a 1,000-word analysis of what was preserved, what was reframed, and what was lost in translation from the source to the skills."

---

## 5. Discussion prompts

For seminar-style classes or as supplementary discussion material:

- **On the AI tension.** The project takes the position that AI tools can support competence development if they prompt thinking rather than replace it. Is this principled distinction empirically defensible? Where might the line genuinely fail?
- **On situation-triggered learning.** The skills activate when a specific situation arises rather than when a topic is discussed. What does this design choice gain? What does it lose?
- **On the four-pillar rubric.** The project uses Riccomini and Ryaboy's framing (Technical Knowledge, Execution, Communication, Leadership). What alternative rubrics exist? What would each surface that this one obscures?
- **On the boundary between scaffolding and substitution.** The project's first design principle is "prompt the thinking, do not replace it." Where in the current skills is this most successful? Where does the skill come closest to violating it?
- **On the limits of paraphrased wisdom.** The skills paraphrase source material rather than reproducing it. What is lost in this compression? What is gained?

---

## 6. Adapting the project for your context

Faculty wishing to adopt the project beyond use of the current 31 skills have several paths:

### 6.1 Fork and modify

Fork the repository (CC BY 4.0 license), modify individual skills to reflect your own framing, your students' context, or your institutional norms. Preserve attribution to the original work and to the underlying sources.

### 6.2 Build a parallel implementation

Apply the methodology (see [`METHODOLOGY.md`](./METHODOLOGY.md)) to construct a new skill set drawn from your own sources, addressing situations specific to your domain or student population. The methodology is content-agnostic; the implementation is entirely yours.

### 6.3 Use as a worked example in coursework

Use the project itself — its methodology, design choices, and limitations — as a primary source in a course on instructional design, AI in education, or software engineering pedagogy. The [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) and [`METHODOLOGY.md`](./METHODOLOGY.md) documents are written to support this use.

### 6.4 Collaborate on extensions

The project is actively maintained. Faculty interested in proposing new skills, building domain-specific spinoffs, conducting empirical research on the methodology, or co-authoring future work are invited to open issues on the GitHub repository or contact the maintainer directly.

---

## 7. What this project is not

For honest framing:

- It is **not a complete software-engineering curriculum.** It addresses specific recurring situations within professional practice; many topics (algorithms, theory, specific stacks, specialized domains) are out of scope.
- It is **not an authority on engineering practice.** It is one author's distillation. Faculty are expected to bring their own judgment and to disagree where they have evidence or experience that conflicts.
- It is **not a substitute for human mentorship.** The skills explicitly route users toward human help (managers, teammates, instructors). They are designed to complement, not replace, the human relationships that make professional development work.
- It is **not empirically validated.** See [`LIMITATIONS.md`](./LIMITATIONS.md) for the full discussion. The methodology rests on theoretical principles, not measured outcomes.
- It is **not platform-neutral.** Primary intended use requires Claude. The standalone reading mode works without any AI tool.

---

## 8. Contact

For questions about course adoption, research collaboration, or proposed extensions, please open an issue on the GitHub repository (https://github.com/tmerrien/swe-assistant) or contact the maintainer at `tmerrien@outlook.com`.

The project is most useful to the field when educators engage with it critically and contribute back what they find. Disagreement, alternative implementations, and empirical study are all welcomed.

---

*See also:* [`METHODOLOGY.md`](./METHODOLOGY.md) for the construction method; [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) for the literature this is grounded in; [`LIMITATIONS.md`](./LIMITATIONS.md) for the honest scope of what is and is not claimed; [`OBJECTIVES.md`](../OBJECTIVES.md) for the four-pillar rubric; [`JOURNEY.md`](../JOURNEY.md) for the five-stage career map; [`READING-LIST.md`](../READING-LIST.md) for the source-material tracker.
