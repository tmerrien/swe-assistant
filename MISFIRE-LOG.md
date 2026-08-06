# Misfire Log

A running record of skills firing when they shouldn't have, and skills that should have fired but didn't. This is the feedback data that lets trigger descriptions tighten over time — the empirical version of the verification step described in [`docs/METHODOLOGY.md`](./docs/METHODOLOGY.md#6-verification).

**This file is not academic material.** It's an operational log. Terse entries, one per incident, dated. Don't optimize prose — optimize how easy it is to jot an entry the moment a misfire happens.

---

## How to log an entry

Add a new entry at the top under **Log**. Use this shape:

```
### YYYY-MM-DD — <skill-that-fired-or-should-have> — over-fire | under-fire | wrong-skill

**What I said (paraphrase OK):** …
**What actually happened:** … (which skill fired, if any)
**What should have happened:** …
**Guess at fix:** description tweak / new skill / no fix (I was ambiguous) / …
```

Three failure categories:

- **over-fire** — a skill fired when the situation didn't actually warrant it.
- **under-fire** — no skill fired but one should have. Include which skill you expected.
- **wrong-skill** — a skill fired but the wrong one; another skill in the set was a better match.

Don't worry about being right about the fix. The pattern that emerges across many entries matters more than any single diagnosis.

---

## Triage rhythm

Roughly monthly (or when the log grows past ~15 unresolved entries):

1. Scan the log for repeated patterns — same skill under-firing, same phrasing over-firing.
2. Open a PR that adjusts the affected `description` field(s), citing the relevant log entries.
3. Once shipped, strike through (or move to the *Resolved* section below) the entries that motivated the change.

Do not iterate on descriptions from a single entry. One data point is not a pattern; two or three consistent ones are.

---

## Log

<!-- Newest first. Add entries here as they happen. -->

### 2026-08-01 — design-doc — under-fire + over-fire (router) — **PATTERN CONFIRMED**

**What I said (paraphrase):** Pasted Chapter 10's design-document template section — the full section list (Introduction, Current State, Motivation, Requirements, Potential Solutions, Proposed Solution, Design and Architecture with API/schema/UI subsections, Test Plan, Rollout Plan, Unresolved Questions, Appendix) with per-section guidance.

**What actually happened:** Router matched `defensive-programming`, `input-validation`, `mocking`, `dependency-management`, `deployment-discipline` (+1 more). It did **not** match `design-doc` — despite the prompt being explicitly and entirely about a design document template.

**What should have happened:** `design-doc`. None of the five that fired were relevant.

**Diagnosis:** Same shape as the entry below, and now confirmed as a pattern rather than a one-off:

- **Over-fire cause:** keyword collisions with section *names* in the template — "API Changes" → `input-validation`, "dependencies" → `dependency-management`, "Rollout Plan" → `deployment-discipline`, "mock-ups" → `mocking` (likely a substring hit on *mock*), "error handling" → `defensive-programming`. A document *describing* sections about these topics is not a request for help *with* them.
- **Under-fire cause:** the `design-doc` pattern appears not to match on strong signals like "design document", "design doc template", or the literal section names of a design document. This is the second consecutive prompt where the single most obviously correct skill was missed.

**ROOT CAUSE — confirmed bug, not a tuning issue.** The router pattern was:

```
"design-doc": r"\b(design\s+doc|RFC\b|ADR\b|...)\b"
```

The alternation ends in `design\s+doc`, and the group is followed by `\b`. So after matching `design doc` inside "design **doc**ument", the required word boundary falls between `c` and `u` — both word characters — and the match fails. The same breaks *every* suffix:

| input | matched |
|---|---|
| `design doc` | yes |
| `design docs` | **no** |
| `design document` | **no** |
| `design documents` | **no** |

Only the exact bare string "design doc" ever matched. The plural — arguably the more common phrasing — never did. This skill had been effectively unroutable for most real phrasings since the router was written.

**FIXED** — three changes applied to `~/.claude/hooks/swe-skill-router.py`:

1. `design\s+doc` → `design\s+doc(ument)?s?`. Verified: all four variants above now match; "designer" still correctly does not.
2. **`technical-design-process` was missing from the router entirely** (found while investigating — the skill was created the same day and never added). Pattern added covering *define the problem*, *problem statement*, *where do I start*, *prototype/spike*, *maker's schedule*, *deep work*, *prior art*, *throwaway code*. Router now covers all 38 skills.
3. `mocking` — `mock\b` matched "mock-up" (the hyphen is a word boundary), which is common design-document vocabulary. Added negative lookahead `(?!-?ups?\b)`. Verified: "I need mock-ups for the UI" no longer fires it; "should I mock the database in this test" still does.

Backup of the pre-fix router: `scratchpad/swe-skill-router.py.bak`.

**Not fixed, deliberately:** the `input-validation` / `dependency-management` / `deployment-discipline` / `defensive-programming` over-fires. Those keywords ("API", "dependencies", "rollout", "error handling") are legitimately broad and over-firing on them is the intended bias.

**Caveat retained:** both logged entries are *authoring* prompts (writing the skills) rather than *usage* prompts (being coached), so the over-fire half may not reproduce in ordinary work. The `design-doc` under-fire needed no such caveat — it was a bug that would equally have broken a genuine "help me write this design doc" request.

---

### 2026-08-01 — design-doc / technical-design-process — under-fire + over-fire (router)

**What I said (paraphrase):** Pasted Chapter 10 notes on the technical design process — the design spiral, defining the problem with stakeholders, doing research, running prototypes, protecting deep-work time, and writing/maintaining design documents.

**What actually happened:** The `swe-skill-router.py` hook matched `code-review`, `input-validation`, and `writing-tests`. It did **not** match `design-doc`, which was plainly the closest existing skill.

**What should have happened:** `design-doc` matched. The three that fired did not.

**Diagnosis:** All three false positives are keyword collisions with incidental words in the text — *"code review"* (mentioned once, as the place to enforce doc updates), *"validate"* (*"prototypes to validate your designs"*), and *"tests"* (*"performance tests"*, *"A/B tests"*). None of these describe the situation; they're vocabulary that happens to appear.

The under-fire is the more interesting half. This was a repo-authoring prompt *about* the design process rather than a request for help *in* it, so it was described obliquely — exactly the blind spot `CLAUDE.md` predicts for a keyword matcher. Notably the *word* "design" appears repeatedly, so the router's `design-doc` pattern is likely narrower than a bare `design` keyword (probably requires "design doc"/"RFC"/"ADR").

**Guess at fix:** Two candidates, neither urgent on one data point —
1. Router: loosen the `design-doc` pattern to catch bare *design*-adjacent phrasing, and/or require a stronger signal than a single incidental keyword for `code-review` / `writing-tests` / `input-validation`.
2. No fix: this was an authoring prompt, not a real usage situation. Worth waiting to see whether the same three over-fire during ordinary work before touching anything.

Leaning (2) for now — per the triage rule below, one data point is not a pattern.

---

## Resolved

<!-- Move entries here once the underlying description has been tightened and shipped.
     Keep the entry, add a resolution line: "Fixed by <commit-hash>: <what changed>". -->

*(No entries yet.)*
