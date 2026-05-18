# Methodology

This document specifies the method by which the skills in this repository were designed. It is intended as a generalizable framework, applicable by other educators, researchers, or practitioners who wish to construct their own situation-triggered AI-coaching skill sets from their own sources, for their own student populations, or in domains beyond early-career software engineering.

The methodology is the **primary intended contribution** of this project. The 18 skills currently in this repository are *one instance* of the methodology — one author's implementation, drawn from one author's reading. The methodology generalizes; the specific implementation does not.

---

## 1. The unit: a "skill"

A **skill** is a single Markdown document with YAML frontmatter (Anthropic's plugin skills format) that:

- Activates automatically when the user's conversational context matches the situation described in its `description` field.
- Provides a structured coaching protocol — frame, diagnostic question(s), surfaced content, action prompt, close — rather than performing the underlying engineering work for the user.
- Cites the sources from which its content is drawn.
- Names the situations in which it should *not* fire and routes the user elsewhere.

The skill is the atomic unit of the methodology. Each skill addresses one recurring engineering situation. Skills do not address topics in general; they address moments in which a learner is about to take a specific action.

---

## 2. The triggering mechanism

Anthropic's plugin runtime performs semantic matching between the user's message and the `description` field of every installed skill. If a match is found, the runtime loads the skill body and follows its instructions.

This mechanism has two methodological consequences:

1. **Skills are surfaced by situation, not by request.** The user does not need to know which skill (or whether any skill) exists. They describe their situation; the relevant skill activates.
2. **The description is the trigger.** Quality of skill activation depends primarily on the quality of the description — how precisely it captures the situations in which the skill should fire and the situations in which it should not. Description design is a first-class methodological concern, not an afterthought.

---

## 3. The five design principles

All skills in this repository are constructed to satisfy five principles. Adopting the methodology means adopting these principles; modifications are reasonable, but the principles function as a coherent system.

### 3.1 Prompt the thinking; do not replace it

A skill must scaffold the learner's own engagement with the task. It may provide frames, checklists, questions, decision criteria, or templates; it must not produce the finished engineering artifact. A skill that writes the design document, performs the code review, or composes the postmortem on the user's behalf interrupts the practice loop the methodology is designed to support.

**Theoretical basis:** scaffolding theory (Wood, Bruner, & Ross, 1976); deliberate practice (Ericsson et al., 1993). See [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md).

### 3.2 Trigger on situations, not on topics

A skill activates when the learner is *about to take a specific action* (write a commit message, scope a project, prepare for a 1:1), not when a topic is mentioned in passing. The trigger is the situation, not the keyword.

**Practical implication:** descriptions enumerate concrete user phrases ("I'm about to...", "should I..."), not abstract topic labels.

**Theoretical basis:** situated cognition (Brown, Collins, & Duguid, 1989).

### 3.3 Synthesize sources; do not enshrine them

A skill is the synthesis of multiple sources rather than a paraphrase of a single text. As new sources arrive that bear on the same situation, the skill is updated to incorporate them. No single source is treated as authoritative.

**Practical implication:** each skill includes a `## Source` section that grows over time. New sources are folded into the skill body rather than spawning new skills for the same situation.

### 3.4 Cite what informed the skill

Every framework, claim, or technique in a skill body must be traceable to a cited source. Sources may include published books and articles, widely-attested industry practice (explicitly labeled as such), or the author's own experience (also explicitly labeled).

**Practical implication:** unattributed paraphrasing of book content is treated as a methodological failure, not stylistic license.

### 3.5 Paraphrase; do not reproduce

Skill bodies are operational ("do X, then Y, check Z"), not literary excerpts. Source material is paraphrased into action-guiding instructions; the original prose is not reproduced. This serves both copyright and pedagogical purposes — the skill must work as instruction at the moment of use, not as a summary of someone else's writing.

---

## 4. Skill body structure

All skills in this repository conform to a consistent internal structure. Adopters may modify this structure, but its consistency reduces cognitive load on the user (once one skill is understood, the structure of others transfers — see Sweller, 1988).

```
---
name: <kebab-case identifier matching folder name>
description: <one paragraph, max 1024 characters, listing specific
              triggers and explicit non-triggers>
---

# <skill name>

## Source
[Citations to works that inform this skill.]

## Pillars this skill strengthens
[Mapping to the project's competence rubric — Technical Knowledge,
 Execution, Communication, Leadership. Adopters using a different
 rubric should substitute their own.]

## What this skill is for
[One paragraph describing the situation addressed.]

## The core mindset (lead with this)
[The single most important framing the skill should establish before
 giving any tactics. Often the most-quoted part of the skill.]

## How to run
[Step-by-step coaching protocol. Typically:
   Step 1 — Frame
   Step 2 — Diagnose / ask where they are
   Step 3 — Surface relevant content
   Step 4 — Pick one concrete action
   Step 5 — Close]

## Output style
[Tone, formatting, length guidance for skill activations.]

## When NOT to use this skill
[Explicit out-of-scope cases, routing to other skills where
 appropriate. Cross-links function as both navigation and
 scope-definition.]

## Further reading
[Sources surfaced as references but not yet folded into the
 skill body, with a pointer to READING-LIST.md.]
```

---

## 5. The construction process

Each skill in this repository was constructed by the following process. Adopters may compress or extend the steps; the sequence is what matters.

1. **Source identification.** Identify the source(s) that present a recurring engineering situation worth packaging. This may be one book chapter, one article, an aggregation of practitioner conversations, or a personal experience. Note the source explicitly.

2. **Situation extraction.** Distinguish *the situation in which a learner needs help* from *the topic the source addresses*. A book chapter may discuss code review as a topic; the situations are *"about to leave feedback on a PR"* and *"about to react to feedback I received."* Skills attach to situations, not topics.

3. **Description drafting.** Write the `description` field first, before the body. The description must list specific user phrases that should trigger the skill *and* phrases that should not. Drafting the description first forces clarity about scope.

4. **Body construction.** Write the body to the standard structure (Section 4 above). Lead with the mindset. Make the coaching protocol concrete (numbered steps with explicit questions).

5. **Trigger verification.** Generate 5–10 realistic user prompts (about half that *should* trigger the skill and about half that *should not*). Mentally simulate or test whether the description would correctly activate for each. Tighten the description until coverage is acceptable. This step is what distinguishes skills that work in practice from skills that look good on paper.

6. **Cross-link integration.** Identify the *other* skills in the set that may compete for the same trigger or that the user should be routed to. Add explicit cross-references in both the body ("for X, see [other skill]") and the *When NOT to use* section.

7. **Pillar / stage tagging.** Tag the skill with the competence dimension(s) it strengthens and the career stage(s) at which it's most useful. Adopters using their own rubric should substitute their own tags.

---

## 6. Verification

The verification step (5 above) deserves separate emphasis because it is the most under-practiced part of skill design.

A skill that does not activate when it should, or activates when it should not, fails as a piece of pedagogy regardless of how well its body is written. Verification is the discipline of checking that the description actually matches the situations the body addresses.

**Verification protocol:**

- Generate at least 5 prompts that represent realistic *positive* cases (user is genuinely in the target situation).
- Generate at least 3 prompts that represent *negative* cases (user is in an adjacent situation that should route to a different skill, or no skill at all).
- For each prompt, judge: does the description match? Does it match too loosely (false positive risk)? Does it match too narrowly (false negative risk)?
- Iterate the description until coverage is acceptable.
- Document any unresolved borderline cases in the body's *When NOT to use* section.

This verification is currently performed by the author. In a production research context, it could be conducted with crowd-sourced annotators or with held-out user logs.

---

## 7. The source-attribution discipline

Every skill carries a `## Source` section that lists the works informing it. This serves three purposes:

1. **Scholarly honesty.** Adopters of the skill (and learners reading it) can trace any claim back to its origin.
2. **Update discipline.** When a new source is read that bears on a skill, the skill body is updated *and* the new source is added to the `## Source` section. The trail of what shaped a skill is preserved over time.
3. **Status tracking.** The repository maintains a [`READING-LIST.md`](../READING-LIST.md) with status indicators (*to read* / *reading* / *read* / *folded*) for every source surfaced. Sources move from *to read* to *folded* through deliberate work, not passive accumulation.

This discipline addresses a common failure mode in informal pedagogical projects: aspirational citation, in which a work lists books that *should* inform its content but in fact do not. The status pipeline distinguishes intent from realization.

---

## 8. The maintenance model

The methodology assumes skills are living documents, not static publications. As an adopter reads new material, gains new experience, or receives feedback from learners, skills are expected to evolve:

- New sources are folded into existing skill bodies where the situation already exists.
- New skills are created only when the situation is genuinely new (rather than a variation of an existing one).
- Trigger descriptions are sharpened in response to observed misfires (skill fired when it shouldn't, or didn't fire when it should).
- The skill set's coverage gaps are tracked openly (in this repository, in the `Status` section of the README and the spin-out backlog noted in the project history).

A skill set that does not evolve is a skill set that does not benefit from the use it is put to.

---

## 9. What this methodology does not specify

The methodology specifies *how* to construct skills. It does not specify:

- **Which situations to cover.** Adopters choose based on their student population, domain, and pedagogical goals.
- **Which sources to draw from.** This is a function of what the adopter has read, who they want to credit, and which traditions they want to surface.
- **Which content to put in a skill.** Two adopters applying the same methodology to the same situation will produce different skill bodies, reflecting their different judgments.
- **Which competence rubric or career model to organize around.** This repository uses Riccomini and Ryaboy's four pillars and five stages; adopters may substitute their own.

The methodology is content-agnostic. It is a way of packaging engineering wisdom for AI-mediated coaching; it does not specify which wisdom to package or how to organize it.

---

## 10. Applying the methodology

An educator or researcher who wishes to build their own skill set should expect to:

1. Choose a domain and a student population.
2. Identify the recurring situations in that domain that learners need help with.
3. Identify the sources from which they draw — books, articles, practitioner experience.
4. For each situation, apply the construction process (Section 5) to produce a skill.
5. Verify each skill's trigger description against realistic prompts (Section 6).
6. Cross-link the skills into a coherent set, with explicit routing between them.
7. License the work openly (this repository uses CC BY 4.0) and preserve inline source attribution.
8. Maintain the set as a living artifact, adding sources, refining triggers, and tracking gaps over time.

The 18 skills in this repository can be read as a worked example of this process applied to early-career software engineering, with *The Missing Readme* (Riccomini & Ryaboy, 2021) as the primary anchor. They are not the right skills for every context. The methodology generalizes; the implementation is one author's interpretation.

---

*See also:* [`THEORETICAL-FOUNDATIONS.md`](./THEORETICAL-FOUNDATIONS.md) for the literature this methodology draws from; [`LIMITATIONS.md`](./LIMITATIONS.md) for what the methodology does not yet establish empirically; [`FOR-EDUCATORS.md`](./FOR-EDUCATORS.md) for practical use in teaching contexts; [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the contribution process if adapting *this* repository rather than building one's own.
