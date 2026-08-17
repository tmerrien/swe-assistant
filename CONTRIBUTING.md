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

All new skills must adhere to the six principles stated in the main [`README.md`](./README.md):

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
description: One paragraph (see length guidance below) describing when this skill
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

### Description length

Two separate constraints apply, and only one is imposed by the platform:

- **Hard limit — 1,536 characters.** Claude Code truncates the combined description text at 1,536 characters *in the skill listing*, which is the surface the runtime matches against when deciding whether to activate a skill. Exceeding this silently cuts the tail of the description — typically the non-trigger and routing clauses, which is the worst part to lose. Configurable via `skillListingMaxDescChars`, but do not rely on a non-default setting.
- **Repository convention — 1,024 characters.** Stricter than the platform requires, and deliberately so. The skill listing shares a context budget (roughly 1% by default) across *every* installed skill. With 50 skills in this plugin, verbose descriptions crowd each other out. Keeping each under 1,024 keeps the whole set affordable.

If a description will not fit in 1,024 characters, that is usually a signal that the skill's scope is too broad and it may want splitting, rather than a reason to raise the limit.

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

## Local Development

### Setting up on a new machine

Everything this repository needs is tracked in it, with three exceptions that cannot be — they are machine state, not project state.

1. **Git author identity.** Git deliberately refuses to let a repository set this, so it never travels with a clone. Without it the first commit fails with *"Author identity unknown."*

   ```bash
   git config user.name "Your Name" && git config user.email "you@example.com"
   ```

2. **Python 3**, for the hooks and the maintenance scripts. It must be a real interpreter on `PATH` as `py`, `python3`, or `python`. **On Windows, `python` and `python3` are frequently Microsoft Store alias stubs** that print an install advert and exit 49 — a real install is needed, and after installing it you must sign out and back in, because a relaunched app inherits the environment of the process that started it rather than the updated `PATH`.

3. **The plugin install itself**, if you want to exercise the skills rather than only edit them — `/plugin marketplace add tmerrien/swe-assistant`, then install, then use the sync script below for local edits.

Confirm the first two took:

```bash
python scripts/bump-version.py --show && python scripts/misfire-report.py --verify
```

The routing event log at `~/.claude/swe-assistant/` is also machine-local, and deliberately so — it is your own prompt-routing data. It does not travel between machines, so misfire evidence gathered on one machine is not visible on another.

### Iterating on a skill

Skills are normally installed from GitHub, which means an edit to a `SKILL.md` in your working copy has no effect on your running Claude until it is committed, pushed, and the marketplace is updated. That round-trip is fine for occasional changes and is the more faithful test — what loads is what users actually get.

When iterating on a skill's content or trigger description, that round-trip gets in the way. Two supported options:

**Claude Code CLI** — the documented approach. Loads live from the filesystem and shadows the installed plugin for that session:

```bash
claude --plugin-dir /path/to/swe-assistant/plugins/swe-assistant
```

Then `/reload-plugins` inside the session picks up further edits without restarting.

**Claude desktop** — the `--plugin-dir` flag is not available. Use the sync script instead, which copies the local plugin into Claude's plugin cache:

```bash
./scripts/sync-to-claude.sh
```

Then run `/reload-plugins` in Claude. The script mirrors `skills/`, `hooks/`, and `scripts/` exactly (including deletions), warns if the repository has uncommitted or unpushed changes — so you know when the loaded skills differ from the published ones — and writes a real directory rather than a symlink, so a later `/plugin marketplace update` simply restores the published version instead of breaking in a way that is hard to diagnose. It also flags a pre-plugin router left in `~/.claude/hooks`, which would now double-fire.

It falls back to `cp` when `rsync` is unavailable, which is the default state of Git Bash on Windows.

Re-run the script after every edit; it is not a live mount.

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
