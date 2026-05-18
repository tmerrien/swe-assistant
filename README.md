# SWE Assistant

A curated collection of Claude AI skills for software engineers, organized by recurring engineering situations and informed by established engineering literature.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Skills: 16](https://img.shields.io/badge/skills-16-blue.svg)](#skills)
[![Plugin: Claude](https://img.shields.io/badge/plugin-Claude-purple.svg)](https://docs.claude.com/en/docs/claude-code)

---

## Overview

This repository provides a working set of AI **skills** — situation-triggered coaching prompts — for software engineers in early and mid-career. Each skill activates when the user is in (or about to enter) a specific engineering situation, and surfaces a checklist, frame, or question drawn from established engineering practice rather than producing the work for the user.

**Intended audience:** computer science students, junior and mid-level software engineers, engineering educators, and curriculum designers.

**Scope.** This is a *coaching framework*, not a code-generation toolkit. The skills aim to make practitioners better at the underlying engineering work, not to perform that work for them. They will not write code, design systems, or compose documents on the user's behalf; they will prompt the user through frameworks for doing those things deliberately.

**Format.** Each skill is a Markdown file with YAML frontmatter (Anthropic skills format), installable as a Claude plugin (Claude Code CLI or Claude Cowork desktop). The skills can also be read directly as standalone reference material, independent of any AI tool.

## Background

The design rests on three theoretical anchors, drawn from the engineering literature:

1. **A four-pillar model of engineering competence** — Technical Knowledge, Execution, Communication, Leadership — adapted from Riccomini and Ryaboy (*The Missing Readme*, 2021, Ch. 1). Every skill in this repository declares which pillar(s) it strengthens.
2. **A five-stage career progression** — Newcomer → Ramp-Up → Contributor → Operator → Owner — also adapted from Riccomini and Ryaboy. Skills are tagged with the stage(s) they most apply to.
3. **Broadwell's Four Stages of Competence** (unconscious incompetence → conscious incompetence → conscious competence → unconscious competence). The skills are designed to accelerate the climb from Stage 1 to Stage 3, where deliberate practice is teachable; Stage 4 (automaticity) is left to time on task.

Further theoretical references — including Fowler's Technical Debt Quadrant, Feathers' *Working Effectively with Legacy Code*, Beams' commit-message conventions, and others — are cited inline in the relevant skill bodies and tracked in [`READING-LIST.md`](./READING-LIST.md).

## Repository Contents

```
swe-assistant/
├── .claude-plugin/plugin.json      Plugin manifest (Anthropic plugin format)
├── README.md                       This file
├── OBJECTIVES.md                   Four-pillar competence rubric
├── JOURNEY.md                      Five-stage career-progression map
├── READING-LIST.md                 Source-material tracker (status: to read / read / folded)
├── LICENSE                         Creative Commons Attribution 4.0
└── skills/                         One subdirectory per skill, each containing SKILL.md
```

Each `SKILL.md` includes a description (which determines when the skill triggers in conversation), the source materials that inform it, the engineering pillar(s) it strengthens, and a structured coaching protocol.

## Skills

| Skill | Stage(s) | Pillar(s) strengthened | Triggering situation |
|---|---|---|---|
| [`growth-self-check`](./skills/growth-self-check/SKILL.md) | Any | Leadership, Communication (meta) | Reflecting on growth: prepping for a 1:1 or review, asking how one is doing, doing a retrospective |
| [`new-team-onboarding`](./skills/new-team-onboarding/SKILL.md) | Newcomer | Execution, Communication, Technical Knowledge | First weeks at a new company, team, or role |
| [`ramp-up-playbook`](./skills/ramp-up-playbook/SKILL.md) | Ramp-Up | Communication, Execution, Technical Knowledge | Past first weeks but not yet productive — building codebase context and manager relationship |
| [`contributor-playbook`](./skills/contributor-playbook/SKILL.md) | Contributor | Execution, Communication, Technical Knowledge | Trusted with larger work; owning a feature end-to-end; OKR / quarterly goals |
| [`code-review`](./skills/code-review/SKILL.md) | Ramp-Up onward | Communication, Execution, Technical Knowledge | Giving or receiving feedback on a pull request |
| [`operator-playbook`](./skills/operator-playbook/SKILL.md) | Operator | Technical Knowledge, Execution, Communication | Taking responsibility post-merge: delivery pipeline, observability, on-call preparation |
| [`incident-response`](./skills/incident-response/SKILL.md) | Operator (any if on-call) | Execution, Communication, Technical Knowledge | An active production incident, or preparing for first on-call shift |
| [`owner-playbook`](./skills/owner-playbook/SKILL.md) | Owner | Execution, Communication, Leadership | Driving a small project; balancing maintenance and new work; longer-term career planning |
| [`design-doc`](./skills/design-doc/SKILL.md) | Contributor onward | Communication, Execution, Technical Knowledge | Writing or reviewing a technical design document, RFC, or ADR |
| [`learning-toolkit`](./skills/learning-toolkit/SKILL.md) | Any | Technical Knowledge, Execution (meta) | Deliberately learning a codebase, system, tool, or domain |
| [`asking-for-help`](./skills/asking-for-help/SKILL.md) | Any | Communication, Execution | Drafting a question for a colleague; deciding whether and how to ask |
| [`growth-obstacles`](./skills/growth-obstacles/SKILL.md) | Any | Leadership, Communication (meta) | Expressing impostor-syndrome distortion, or showing potential Dunning-Kruger overconfidence |
| [`software-entropy`](./skills/software-entropy/SKILL.md) | Any | Communication, Leadership | Frustration with code mess, before blame culture sets in |
| [`technical-debt`](./skills/technical-debt/SKILL.md) | Any (Contributor+ most common) | Communication, Leadership, Execution | Identifying, prioritizing, or proposing the payoff of specific technical debt |
| [`changing-legacy-code`](./skills/changing-legacy-code/SKILL.md) | Any | Execution, Technical Knowledge | About to modify unfamiliar, untested, or complex existing code |
| [`commit-and-pr-hygiene`](./skills/commit-and-pr-hygiene/SKILL.md) | Any | Communication, Execution | Writing commit messages or preparing a pull request for review |

## How to Use

### Direct reading

The skills can be read as standalone reference material — each `SKILL.md` is a self-contained Markdown document. Educators may use individual skills as discussion prompts, reading-group material, or supplementary content. No AI tool is required for this mode of use.

### As a Claude plugin

The intended primary mode of use is as an installed Claude plugin. Once installed, the skills auto-trigger when a user describes a matching situation in conversation with Claude.

**Installation (Claude Code CLI):**

```
claude plugin add tmerrien/swe-assistant
```

**Installation (Claude Cowork desktop):**

Settings → Plugins → Add Plugin → paste the repository URL:

```
https://github.com/tmerrien/swe-assistant
```

Once installed, no further action is required from the user. Skills activate based on the descriptions in their YAML frontmatter; users describe their situation in natural language and the appropriate skill (if any) is loaded automatically. A single skill may also be invoked manually with `/<skill-name>`.

## Design Principles

The skills in this repository follow five principles. New contributions are expected to follow them as well.

1. **Prompt the thinking, do not replace it.** Skills surface checklists and questions, not finished answers. The user performs the engineering work; the skill provides scaffolding.
2. **Trigger on situations, not on topics.** A skill activates when the user is about to take a specific action, not when a topic is mentioned in passing.
3. **Synthesize sources, do not enshrine them.** Each skill's `Sources` section accumulates references over time as new materials inform the practice. No single source is treated as authoritative.
4. **Cite the literature that shaped the skill.** Every source that informed a skill is named inline, preserving the path back to the original work.
5. **Paraphrase, do not reproduce.** Skill bodies are operational ("do X, then Y"), not literary excerpts. Underlying source materials retain their own copyrights and are credited but not reproduced.

## How to Cite

If you reference, adapt, or build on this work, please cite it as follows:

> Merrien, T. (2026). *SWE Assistant: A curated collection of Claude AI skills for software engineers* (Version 0.1.0) [Software]. https://github.com/tmerrien/swe-assistant

A machine-readable citation is also available in [`CITATION.cff`](./CITATION.cff), which GitHub renders as a *Cite this repository* button at the top of the project page.

For inline attribution in derived works, the suggested string is:

> *Based on the SWE Assistant by T. Merrien (CC BY 4.0). https://github.com/tmerrien/swe-assistant*

## Contributing

Contributions are welcome. Areas of particular interest include:

- **New skills** for situations not yet covered, following the five design principles above.
- **Source integration** — folding wisdom from books on the [`READING-LIST.md`](./READING-LIST.md) into the relevant skills, updating Sources sections, and marking entries as **Folded**.
- **Trigger-description refinements** based on real-world use — cases where a skill should have activated and did not, or activated when it should not have.
- **Translation** of skills into other languages.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details on the contribution process, skill style conventions, and review expectations.

## License

This work is licensed under the **Creative Commons Attribution 4.0 International License** (CC BY 4.0). See [`LICENSE`](./LICENSE) for the full text.

You are free to share and adapt the material for any purpose, including academic and commercial use, provided that appropriate credit is given, a link to the license is provided, and changes are indicated.

The underlying ideas paraphrased in the skills (from *The Missing Readme*, *Working Effectively with Legacy Code*, Fowler's writing, Beams' article, and other cited works) remain the intellectual property of their respective authors and are not relicensed by this work. Forks and adaptations must preserve both this license and the inline source attributions within each skill body.

## Acknowledgements & Source Materials

This work is informed by, and gratefully acknowledges, the following primary sources:

- Riccomini, C., & Ryaboy, D. (2021). *The Missing Readme: A Guide for the New Software Engineer*. No Starch Press. — Source of the four-pillar competence model, the five-stage journey, and several individual skill frameworks.
- Feathers, M. C. (2004). *Working Effectively with Legacy Code*. Prentice Hall. — Source of the Legacy Code Change Algorithm and dependency-breaking techniques used in `changing-legacy-code`.
- Fowler, M. *Technical Debt Quadrant*. https://martinfowler.com/bliki/TechnicalDebtQuadrant.html — Used in `technical-debt`.
- Beams, C. *How to Write a Git Commit Message*. https://chris.beams.io/posts/git-commit/ — Source of the seven commit-message rules used in `commit-and-pr-hygiene`.
- Broadwell, M. M. (1969). *Teaching for Learning*. — Source of the Four Stages of Competence framework underlying Chapter 2 skills.

Additional sources are tracked in [`READING-LIST.md`](./READING-LIST.md), with status indicators showing which have been read and folded into the skills.

## Maintainer

Tanguy Merrien — `tmerrien@outlook.com`

Issues and pull requests are welcome through the GitHub repository at https://github.com/tmerrien/swe-assistant.
