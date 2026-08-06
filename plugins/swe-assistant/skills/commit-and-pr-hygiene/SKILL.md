---
name: commit-and-pr-hygiene
description: Use when the user is writing a commit message, preparing a pull request, restructuring their commit history before submitting for review, or asking about version control practices (rebase, squash, branching, commit conventions). Triggers include phrases like "how should I write this commit message", "my commits are messy", "should I squash these commits", "about to open a PR", "how do I structure this PR", "what's a good commit message", "help me write a PR description", "should I rebase or merge", or asking about commit-message conventions. Walks through commit hygiene from The Missing Readme (Chapter 3) — commit early and often during development, rebase and squash before review, issue ID prefixes for traceability, the seven rules of good commit messages (per Chris Beams), and how to structure the PR so reviewers can actually follow your thinking. Useful at any stage from Newcomer onward. Do not trigger for active code reviews (route to code-review) or tactical Git command questions.
---

# commit-and-pr-hygiene

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code" (Section: Use version control system best practices). The seven commit-message rules come from **Chris Beams, "How to Write a Git Commit Message"**: https://chris.beams.io/posts/git-commit/. See [`READING-LIST.md`](../../../../READING-LIST.md).

## Pillars this skill strengthens

- **Primary:** Communication (commits and PRs are messages to humans)
- **Also:** Execution (cleaner history = faster reviews = faster shipping)
- **Builds:** Leadership (modeling good commit culture lifts the whole team)

## What this skill is for

Commits and PRs are **communication artifacts**, not just code transport. The reviewers who'll see your PR today, and the future engineer (often you) doing `git blame` in three years, both depend on commit messages and PR descriptions that tell them *what changed, why it changed, and what to know.*

This skill fires when the user is producing those artifacts and wants to do it well — or when their first instinct is to type *"fix"* and click submit.

## The core mindset (lead with this)

**Commit messages are for humans. PR descriptions are for humans. Optimize accordingly.**

- The cost of a good commit message is two minutes. The cost of a bad one shows up months or years later when someone — including you — needs to understand a change and can't.
- Reviewers can only review well if they can follow your thinking. A messy commit history forces them to read your diff as a single blob; a clean history lets them read it as a story.

## The two-mode rhythm

There are two distinct modes for commits, with different rules:

### Mode 1 — While cracking out code (private to you)

- **Commit early, commit often.** Don't try to land a perfect commit on the first try.
- **Shorthand messages are fine.** *"wip"*, *"trying X"*, *"this almost works"* are all acceptable while you're heads-down.
- Your local history is a working space, not a final artifact.

### Mode 2 — Before submitting for review (public to your team)

- **Rebase and clean up.** Use `git rebase -i` (interactive rebase) to reorder, combine, and split commits.
- **Squash work-in-progress commits** into meaningful units. A reviewer should see the change as you'd *want* to present it, not as you *built* it.
- **Write proper messages.** See the seven rules below.
- **Each commit should make sense on its own.** A reviewer reading just the commit messages should understand the story of the change.

The transition between Mode 1 and Mode 2 is a habit worth building. Most engineers' commit messages are bad because they never make the switch.

---

## Issue ID prefixes (or whatever your team uses)

If your team uses issue tracking (Jira, Linear, GitHub Issues), it's common — and useful — to prefix commit messages with the issue ID:

```
[MYPROJ-123] Make the backend work with Postgres
```

**Why it pays:**

- Connects the commit to the broader context (the issue's discussion, requirements, related work).
- Makes scripting and tooling possible — many teams auto-link commits to issues, generate changelogs, build deploy notifications.
- Future-you trying to understand a change can read the issue for the *why* the commit message couldn't fit.

Different teams use different conventions: `[MYPROJ-123]`, `MYPROJ-123:`, `fix(auth): MYPROJ-123 ...`, conventional commits (`feat:`, `fix:`, `chore:`). **Use whatever your team uses.** Consistency is the value, not the specific format.

---

## Callout — Chris Beams' seven rules of a great commit message

If your team has no formal rules, this is the most widely-adopted default. Source: https://chris.beams.io/posts/git-commit/

1. **Separate subject from body with a blank line.**
2. **Limit the subject line to 50 characters.** (72 is the absolute max; aim for 50.)
3. **Capitalize the subject line.**
4. **Do not end the subject line with a period.**
5. **Use the imperative mood in the subject line.** *"Add login flow"* — not *"Added login flow"* or *"Adds login flow"*. Read it as "If applied, this commit will... `<subject>`."
6. **Wrap the body at 72 characters.**
7. **Use the body to explain *what* and *why* versus *how*.** The diff already shows *how*. The reader needs the motivation and the constraints.

### A worked example

**Bad:**

```
fixed bug
```

**Mediocre:**

```
Fix the auth bug that was happening
```

**Good:**

```
[AUTH-481] Refresh the user token before expiry, not after

The previous implementation refreshed the token in response to a
401 from a downstream service. This caused a ~200ms latency hit on
every request that happened to be near the expiry boundary, since
the refresh round-trip blocked the user's request.

Now the token refresh runs in a background task triggered 60 seconds
before expiry. The user-facing request always uses a valid token
and doesn't pay the refresh latency.

Tested by simulating clock skew (see auth_test.py). The 60-second
buffer assumes our clock skew tolerance is <30s, which the SRE team
confirmed today.
```

The body teaches the reviewer (and future-you) what was going on without making them re-derive it from the diff.

---

## PR-level discipline (briefly)

This skill mostly lives at the commit level. The PR description deserves the same care but has its own shape:

- **Title:** as if it were a commit subject. Imperative, ≤50 chars, no period.
- **Description:** at minimum, *what* and *why* (same as the commit body). For non-trivial PRs, also: *how to test*, *any deploy/rollout considerations*, *links to issue or design doc*.
- **Keep the PR diff readable.** Many small focused PRs beat one giant PR. See [`changing-legacy-code`](../changing-legacy-code/SKILL.md) for the incremental-PR rhythm.
- **Tag specific reviewers and say what you want from them.** *"@Alice — I'd love your eye on the migration. @Bob — the API change is the part I'm least sure about."*

For receiving review feedback on the PR, route to [`code-review`](../code-review/SKILL.md).

---

## How to run

### Step 1 — Diagnose what they're producing

Ask:

- *"Are you writing a commit message right now, cleaning up your history before a PR, or writing the PR description?"*

Different answers want different sections of this skill.

### Step 2 — Surface the relevant guidance

- **Mid-development sloppy commits:** *"That's fine. Save the cleanup for before review."*
- **About to submit for review:** Walk through the Mode 2 checklist — rebase, squash, write proper messages. Get them to do `git log --oneline` and see if the story reads.
- **Writing a specific commit message:** Apply Beams' seven rules to their draft. If they don't have a draft, ask them to write *what changed and why* in their own words first.
- **Writing a PR description:** Title rules + what/why minimum + test/deploy notes if non-trivial.

### Step 3 — Work on the actual artifact

Like with [`design-doc`](../design-doc/SKILL.md) and [`technical-debt`](../technical-debt/SKILL.md), apply the framework to their specific draft. *"Show me the message you're about to write."* Edit together. The rules teach faster when applied to real text.

### Step 4 — Close

If they're submitting for review, remind them to route to [`code-review`](../code-review/SKILL.md) when feedback comes back.

## Output style

- **Don't be precious about the rules.** If their team uses a different convention, the team's convention wins. The skill teaches a sensible default; the user lives with their team's reality.
- **Show, then tell.** If they share a draft, edit it before lecturing. Concrete fix > abstract rule.
- **Don't add complexity if they're already doing it well.** A clean three-commit history with imperative-mood messages doesn't need a PR description framework lecture.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is in an active code review (giving or receiving feedback on a PR) — route to [`code-review`](../code-review/SKILL.md).
- The user has a tactical Git command question (*"how do I undo my last commit?"*, *"what does `git rebase --onto` do?"*) — this skill is about hygiene, not Git mechanics. Help directly.
- The user is asking about a specific complex VCS workflow (Git submodules, monorepos, release branches) — those are bigger topics than this skill.

## Further reading

Surfaced as a primary reference but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for the full entry.

- *How to Write a Git Commit Message* — Chris Beams (https://chris.beams.io/posts/git-commit/). The canonical short essay on the seven rules. Worth reading in full once; it's brief and well-argued.
