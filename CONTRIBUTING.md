# Contributing to SWE Assistant

Thank you for considering contributing. This document describes how to propose new skills, refine existing ones, fold sources from the reading list, and translate the content.

## Scope of Contributions

Contributions of greatest value:

1. **New skills** for recurring engineering situations not yet covered.
2. **Source integration** — reading items from [`READING-LIST.md`](./READING-LIST.md), folding the insights into the relevant skills, and updating the status accordingly.
3. **Trigger-description refinements** based on real-world use of the plugin — cases where a skill should have activated and did not, or activated when it should not have.
4. **Translation** of skills into other languages.
5. **Bug fixes** in skill bodies (broken links, factual errors, outdated references).

Out of scope for this repository:

- Skills unrelated to software engineering practice (this is a focused project).
- AI-generated skill bodies without human review and source attribution.
- Promotional content for specific products, vendors, or services.

## Skill Design Principles

All new skills must adhere to the five principles stated in the main [`README.md`](./README.md):

1. **Prompt the thinking, do not replace it.**
2. **Trigger on situations, not on topics.**
3. **Synthesize sources, do not enshrine them.**
4. **Cite the literature that shaped the skill.**
5. **Paraphrase, do not reproduce.**

A skill that does not follow these principles will not be merged.

## Skill File Format

Each skill lives in `plugins/swe-assistant/skills/<skill-name>/SKILL.md`. The required structure:

```markdown
---
name: skill-name-in-kebab-case
description: One paragraph (max 1024 characters) describing when this skill
  should trigger — specific situations, example phrases the user might use,
  and explicit do-not-trigger cases.
---

# skill-name

## Source

[Citations to the works that inform this skill — books, articles, talks,
or "common practice with attribution".]

## Pillars this skill strengthens

[Which of the four pillars from `OBJECTIVES.md` this skill primarily and
secondarily strengthens.]

## What this skill is for

[Brief description of the situation the skill addresses.]

## The core mindset (lead with this)

[The single most important framing the skill should establish before
giving any tactics.]

## How to run

[Step-by-step coaching protocol: Step 1 — Frame; Step 2 — Diagnose; ...]

## Output style

[Tone, formatting, length guidance for skill activations.]

## When NOT to use this skill

[Explicit out-of-scope cases, with routes to other skills where
appropriate.]
```

### Description guidelines

The `description` field is the trigger mechanism. Claude reads this field across all installed skills and decides which (if any) matches the user's message. Quality of the description directly determines quality of skill activation.

- Lead with the situation (*"Use when the user is..."*).
- List explicit example phrases the user might say.
- State explicit do-not-trigger cases (route to other skills where appropriate).
- Avoid generic language ("helps with code") — specificity is what makes triggers work.

Verify a new description by drafting 5–10 realistic prompts and checking that the description would correctly activate for matching prompts and not activate for non-matching ones.

## Source Attribution

Every claim, framework, or technique in a skill body must trace to a cited source. Acceptable sources:

- Books and articles, cited inline with author, title, and (where relevant) year.
- Widely-attested industry practice, labeled as such (*"informed by common SRE practice"*).
- The contributor's own experience, labeled as such.

Unattributed paraphrasing of book content is unacceptable. If you read something that changes how a skill should work, fold the insight into the skill body **and** add the source to the skill's `## Source` section **and** update the entry in [`READING-LIST.md`](./READING-LIST.md) to status **Folded**.

## Submission Process

1. **For new skills:** open a GitHub issue first with the proposed skill name, the situation it addresses, and the source(s) that inform it. This gives space for discussion before significant writing effort.
2. **For refinements and folds:** open a pull request directly. Reference the source materials in the PR description.
3. **PR contents:** the SKILL.md (or other file change), an updated skills table row in the main `README.md` if relevant, and an updated entry in `READING-LIST.md` if a source was folded.
4. **Review:** the maintainer (or designated reviewers) will check that the contribution adheres to the design principles, that sources are properly attributed, and that the trigger description is sound. Expect at least one round of revision on substantive contributions.
5. **License:** by submitting a contribution, you agree that it will be licensed under CC BY 4.0, in line with the rest of the repository.

## Style Conventions

- Skill file and folder names: kebab-case, lowercase, hyphens only.
- Markdown: standard CommonMark, with no skill-internal HTML.
- Citations: prefer inline citations in the skill body, plus a consolidated `## Source` section at the top.
- Voice: instructive and coaching-oriented, in the second person ("you") when addressing the user, in the third person when describing the skill's design rationale.
- Avoid jargon without definition. If a term is used (OKR, SRE, RFC), define it on first use or link to its definition.

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) version 2.1. By contributing, you agree to abide by its terms. See [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

## Contact

For questions about contributing, open an issue on the GitHub repository or contact the maintainer at `tmerrien@outlook.com`.
