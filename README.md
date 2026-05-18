# SWE Assistant

Tanguy's growing software engineering assistant — a coherent set of Claude skills that surface at the moment they're needed, distilled from everything I'm reading, doing, and learning along the way.

## Why this exists

You read the book. You highlight the good parts. You agree with everything. Then you go back to work and you write the same code review you would have written before reading it. The lessons live in your highlights, not in your hands.

The other half of the problem: AI is getting good enough to do the work for you. That makes you faster, but it can also let you skip the struggle that produces understanding — you ship the code without building the model. So the question isn't *should I use AI*, it's *how do I use AI in a way that prompts the thinking instead of replacing it?*

## The idea

A single coherent assistant, organized by **situation**, not by source. When the situation arises — opening a PR, getting paged, prepping for a 1:1, debugging, joining a new team — the relevant skill fires and surfaces a coaching prompt: a frame, a checklist, a question.

Each skill is a living distillation. When I read something new and it changes how I think about a situation, the corresponding skill gets updated; the new source goes into that skill's `Sources` section. Over time each skill becomes the synthesis of many inputs rather than the echo of one — the way a senior engineer's instincts actually work.

Skills here are designed to **coach, not replace your thinking**. A skill should give you a frame, a checklist, or a question — never do the work for you. Over enough reps, the skill becomes unnecessary because you've internalized the practice. That's the whole point.

## What's in here

```
swe-assistant/
├── .claude-plugin/
│   └── plugin.json             # Plugin manifest
├── OBJECTIVES.md               # The four pillars — the rubric for "strong player"
├── JOURNEY.md                  # The stage map — Newcomer → strong player
├── READING-LIST.md             # Books/articles/talks to read; what they'd shape
├── README.md
└── skills/                     # one folder per skill
    ├── asking-for-help/
    ├── changing-legacy-code/
    ├── code-review/
    ├── commit-and-pr-hygiene/
    ├── contributor-playbook/
    ├── design-doc/
    ├── growth-obstacles/
    ├── growth-self-check/
    ├── incident-response/
    ├── learning-toolkit/
    ├── new-team-onboarding/
    ├── operator-playbook/
    ├── owner-playbook/
    ├── ramp-up-playbook/
    ├── software-entropy/
    └── technical-debt/
```

`OBJECTIVES.md` defines *what* good looks like (the four pillars). `JOURNEY.md` defines *the path* you walk to get there (stages from Newcomer onward). Together they're the design rubric every skill is built against.

`READING-LIST.md` tracks books, articles, and talks surfaced (mostly from each chapter's "Level Up" section) that should eventually inform the skills. Entries stay honest about status — *to read* / *reading* / *read* / *folded* — so the skill bodies only ever cite material that's actually shaped them.

## Skills

| Skill | Stage(s) | Pillar(s) strengthened | Fires when… |
|---|---|---|---|
| [`growth-self-check`](./skills/growth-self-check/SKILL.md) | Any | Leadership, Communication (meta — touches all four) | You're reflecting on your own growth: prepping for a 1:1 or review, asking "how am I doing", planning what to learn, doing a retro |
| [`new-team-onboarding`](./skills/new-team-onboarding/SKILL.md) | Newcomer | Execution, Communication (also Technical Knowledge) | You're in (or about to enter) the first weeks at a new company, team, or role |
| [`ramp-up-playbook`](./skills/ramp-up-playbook/SKILL.md) | Ramp-Up | Communication, Execution (also Technical Knowledge) | You're past first weeks but not yet productive — learning the codebase, putting up first PRs, building the manager relationship, figuring out status updates |
| [`contributor-playbook`](./skills/contributor-playbook/SKILL.md) | Contributor | Execution, Communication (also Technical Knowledge, emerging Leadership) | You're trusted with bigger work — owning a feature end-to-end, helping teammates, scoping, OKRs/quarterly goals |
| [`code-review`](./skills/code-review/SKILL.md) | Ramp-Up onward | Communication, Execution (also Technical Knowledge) | You're about to leave (or are reacting to) feedback on a pull request |
| [`operator-playbook`](./skills/operator-playbook/SKILL.md) | Operator | Technical Knowledge, Execution (also Communication, building Leadership) | You're taking responsibility for what happens after merge — delivery pipeline, observability, on-call prep, defending software |
| [`incident-response`](./skills/incident-response/SKILL.md) | Operator (any-stage if on-call) | Execution, Communication (also Technical Knowledge) | The pager fired, prod is on fire, or you're prepping for first on-call shift |
| [`owner-playbook`](./skills/owner-playbook/SKILL.md) | Owner | Execution, Communication, Leadership (also Technical Knowledge) | You're driving a small project, designing software, balancing maintenance vs new work, thinking about team process or longer-term career |
| [`design-doc`](./skills/design-doc/SKILL.md) | Contributor onward | Communication, Execution (also Technical Knowledge) | You're writing or reviewing a technical design document, RFC, or ADR |
| [`learning-toolkit`](./skills/learning-toolkit/SKILL.md) | Any | Technical Knowledge, Execution (meta — builds all four over time) | You're trying to learn something deliberately — a codebase, a system, a tool, a domain — rather than just shipping a specific thing |
| [`asking-for-help`](./skills/asking-for-help/SKILL.md) | Any | Communication, Execution (builds Leadership) | You're about to ask a colleague for help, hesitating to ask, drafting a question, stuck and wondering whether to ask, or reflecting on whether you ask too much or too little |
| [`growth-obstacles`](./skills/growth-obstacles/SKILL.md) | Any | Leadership, Communication (meta — improves accuracy of self-assessment across all four) | You feel like a fraud or like everyone knows more than you (impostor) — or you're moving fast and confident on something you might not fully understand (Dunning-Kruger) |
| [`software-entropy`](./skills/software-entropy/SKILL.md) | Any | Communication, Leadership (also Technical Knowledge) | You're frustrated with a messy codebase and starting to blame "whoever wrote this" — needs the reframe before blame culture sets in |
| [`technical-debt`](./skills/technical-debt/SKILL.md) | Any (Contributor+ most common) | Communication, Leadership (also Execution, Technical Knowledge) | You're identifying, prioritizing, or proposing the payoff of specific tech debt — and need to communicate about it with your team or manager |
| [`changing-legacy-code`](./skills/changing-legacy-code/SKILL.md) | Any | Execution, Technical Knowledge (also Communication) | You're about to modify existing code — especially code that's unfamiliar, untested, or scary — and want to do it safely |
| [`commit-and-pr-hygiene`](./skills/commit-and-pr-hygiene/SKILL.md) | Any | Communication, Execution | You're writing a commit message, preparing a PR, or cleaning up your commit history before review |

## Install

Clone or add this repo as a Claude plugin source.

```
/plugin install tmerrien/swe-assistant
```

Or in Cowork, paste the GitHub URL into Settings → Plugins → Add Plugin:

```
https://github.com/tmerrien/swe-assistant
```

## Design principles

1. **Prompt the thinking, don't replace it.** Skills give checklists and questions, not finished answers.
2. **Trigger on situations, not topics.** A skill fires when you're *about to do something*, not when a topic is mentioned.
3. **Synthesize sources, don't enshrine them.** Each skill carries a `Sources` section that grows as new inputs arrive — books, articles, talks, lessons learned.
4. **Cite what informed you.** Every source that shaped a skill gets named, so the trail back to the original is preserved.
5. **Paraphrase, don't copy.** Skill bodies are operational ("do X, then Y"), not literary excerpts.

## Sources informing the current skills

- *The Missing Readme: A Guide for the New Software Engineer* — Chris Riccomini & Dmitriy Ryaboy (No Starch Press, 2021). [Buy it.](https://nostarch.com/missing-readme)

(More sources will appear here as the assistant grows.)

## Status

Chapter 1 fully mapped: nine skills covering all five stages of the journey (Newcomer → Ramp-Up → Contributor → Operator → Owner). Chapter 2 ("Getting to Conscious Competence") produced three meta-skills on the practice of learning itself — `learning-toolkit`, `asking-for-help`, `growth-obstacles`. Chapter 3 ("Working with Existing Code") in progress — four skills so far: `software-entropy` (reframe for natural mess), `technical-debt` (discipline for named debt), `changing-legacy-code` (Feathers' algorithm for safely modifying existing code), `commit-and-pr-hygiene` (the communication artifacts around changes). 16 skills total.

## License & attribution

This work is licensed under [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](./LICENSE).

You're free to share, adapt, and build on it — for academic use, professional learning, or anything else — as long as you give appropriate credit and link to the license.

The underlying ideas in the skills come from books, articles, and other sources that retain their original copyrights — credited inline in each skill's `## Source` section and tracked in [`READING-LIST.md`](./READING-LIST.md). When you fork or adapt this work, **please preserve those inline attributions as well as the top-level license.** And if a skill helps you, please support the original authors by buying the source books.
