# Misfire Log

A running record of skills firing when they shouldn't have, and skills that should have fired but didn't. This is the feedback data that lets trigger descriptions tighten over time — the empirical version of the verification step described in [`docs/METHODOLOGY.md`](./docs/METHODOLOGY.md#6-verification).

**This file is not academic material.** It's an operational log. Terse entries, one per incident, dated. Don't optimize prose — optimize how easy it is to write up a misfire once you have one.

## Detection is automatic; diagnosis is not

Misfires used to be recorded only when someone noticed one and remembered to write it down. That is a bad capture mechanism for a rare, easy-to-miss event, and it under-recorded badly.

The plugin's two hooks now record every routing decision and every skill invocation (see [`plugins/swe-assistant/hooks/README.md`](./plugins/swe-assistant/hooks/README.md)). At triage time, surface the disagreements:

```bash
./scripts/misfire-report.py            # candidates, ranked
./scripts/misfire-report.py --verify   # is capture actually running?
```

**That tool finds candidates. It does not diagnose them.** The value of an entry below is the root cause — *"the alternation ends in `design\s+doc` and the group is followed by `\b`, so the boundary falls between `c` and `u`"* — and no amount of event capture produces that sentence. The report tells you where to look; the write-up is still yours.

So the workflow is now: run the report → pick the candidates that look real → diagnose → write the entry here.

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

1. Run `./scripts/misfire-report.py`. Start with the **under-fire** section — a skill invoked without the router naming it is the category that was previously invisible, and the one most likely to be a real bug rather than noise.
2. Diagnose the candidates that look real, and write them up below. Ignore the rest; the over-fire column is noisy on purpose.
3. Scan the log for repeated patterns — same skill under-firing, same phrasing over-firing.
4. Open a PR that adjusts the affected `description` field(s) or router pattern, citing the relevant log entries.
5. Once shipped, strike through (or move to the *Resolved* section below) the entries that motivated the change.

Do not iterate on descriptions from a single entry. One data point is not a pattern; two or three consistent ones are. The report makes it cheap to wait for the second and third.

---

## Log

<!-- Newest first. Add entries here as they happen. -->

### 2026-11-08 — triage run (2026-08-25 .. 2026-11-08) — notes

`misfire-report.py`: 4925 routes, 67 invocations, 24 under-fire misses in 21 windows. Prompts were recovered from session transcripts by `session_id` + timestamp because **`SWE_ASSISTANT_LOG_PROMPTS` is not set on this machine**. Every route event carries `prompt_chars` only, so the report printed no `e.g.` lines. Set it before the next triage.

**Noise (4 windows, no entry):**
- *"run design-doc against DESIGN.md"*: the user named the skill by its slug, so no routing was needed. (`design\s+doc` does not accept the hyphen, but that is irrelevant when the user names the skill.)
- *"yes go ahead with the messages"* → `interface-copy`: a bare continuation. The context fallback (cap 2) surfaced `design-doc` from "ADR" and `build-and-package` from an `<artifact-view-context>` block (see 2026-09-25).
- 2026-09-18 `release-hygiene` and 2026-09-30 `rationing-attention`/`interface-tradeoffs`/`interface-copy`/`operational-tools`: **attribution artifacts.** Those invocations came from subagents (`subagents/agent-*.jsonl`) but were logged under the parent `session_id`, which put them in the parent's window. Neither route's prompt exists in the main transcript. Report-side fix, not yet done: record an agent identifier on `invoke` events and exclude subagent invocations from windows.

**Over-fire leads (not diagnosable without prompt text):** `build-and-package` 347/1, `metrics` 302/2, `new-team-onboarding` 201/1. Partial causes: `artifacts?` matching Artifact plumbing (fixed below), `dashboards?` matching product dashboards (2026-09-21, 2026-10-28), and bare `onboard(ing)?` (2026-08-28, 2026-09-02). Over-firing is the intended bias, so only the Artifact plumbing is fixed. It is not a topic word at all.

---

### 2026-10-28 — configuration — wrong-skill (router)

**What I said:** *"make sure we have space in the code for those business decisions so if any of those decisions change we don't need to rebuild … have some things set as settings in the dashboard"*
**What actually happened:** router named `metrics` (`dashboards?`). `configuration` was invoked anyway.
**What should have happened:** `configuration`. Its description covers "should this be config or hardcoded" and dynamic vs static config.
**Diagnosis — vocabulary gap.** The pattern needs `config…`, `env var`, `.env`, or `settings file`. Bare *settings*, *hardcoded*, *don't need to rebuild*, and *change without a deploy* are not covered. The `metrics` hit is a `dashboards?` collision: the user meant an admin UI, not monitoring.
**Guess at fix:** add `settings\b`, `hard.?coded`, `without\s+(a\s+)?(rebuild|redeploy)`. **Waiting** (one data point).

### 2026-09-30 — metrics — wrong-skill (router)

**What I said:** *"I want to have a look at adding the LGTM stack also to the api, you know about it?"*
**What actually happened:** router named `mocking` from context. `metrics` was invoked.
**What should have happened:** `metrics`, and arguably `tracing`/`logging`. LGTM is Loki, Grafana, Tempo, Mimir.
**Diagnosis — vocabulary gap (tool names).** The pattern has concept words (`metrics`, `SLO`, `observab…`) but no product names. *LGTM*, *Grafana*, *Prometheus*, *OpenTelemetry/OTel*, *Loki*, and *Tempo* all miss.
**Guess at fix:** add a tool-name alternation shared by `metrics`/`tracing`/`logging`. **Waiting** (one data point).

### 2026-09-25 — code-review — under-fire (router) — **FIX PROPOSED**

**What I said:** *"can we take a pause on this work quickly and have a look at pr 405 on webapp, steven asked for a review."* The desktop app prefixed an `<artifact-view-context>` block.
**What actually happened:** router named `build-and-package` only. `code-review` was invoked.
**What should have happened:** `code-review`.
**Diagnosis — fixed word order + machine text.** (1) `review(ing)?\s+(a|this|my|the)\s+(PR|…)` needs *review* first and a determiner next. Here the PR comes first and *review* comes 40 characters later. (2) `build-and-package` came entirely from the artifact block's boilerplate ("…live state in the **artifact**…"). With the block stripped, the prompt matched nothing. The same block fed the context fallback for the 2026-09-25 *"yes go ahead with the messages"* window.
**Fix proposed:** bidirectional *review* ↔ PR/branch/diff within 60 chars. Strip `<artifact-view-context>…</artifact-view-context>` before matching. Stripping is right here, not adding the block to `NOT_HUMAN`, because the user's words follow the block.

### 2026-09-24 — code-review — under-fire (router) — **FIX PROPOSED**

**What I said:** *"review 376"*
**What actually happened:** nothing matched. `code-review` was invoked.
**What should have happened:** `code-review`.
**Diagnosis — wrong alternation.** Every alternative needs a noun after *review* (`PR`, `code`, `diff`). A bare PR number is the shortest and most common phrasing, and nothing covers it.
**Fix proposed:** `review\w*\s+(of\s+)?((PR|pull\s+request|MR)\s*)?#?\d{2,}`.

### 2026-09-21 — interface-decisions — wrong-skill (router) — **FIX PROPOSED**

**What I said:** *"I mean the mock frontend with fake data. The same way the chore/review-fronted-first-draft is set up."*
**What actually happened:** router named `mocking`. `interface-decisions` was invoked.
**What should have happened:** `interface-decisions`. A mock frontend is a UI prototype, not a test double.
**Diagnosis — keyword collision, second instance.** `mock\b(?!-?ups?\b)` excluded only *mock-up*, the case from 2026-08-01. *Mock frontend*, *mock UI*, and *mock screens* use the same UI-prototype sense and still hit `mocking`. `interface-decisions` matches `mock.?up` but not `mock` + a UI noun.
**Fix proposed:** add `mock\s+(front.?end|UI|screens?|pages?|app)|front.?end\s+mocks?` to `interface-decisions`, and extend the `mocking` lookahead to exclude those nouns. This agrees with the 2026-08-01 entry.

### 2026-09-21 — interface-tradeoffs — wrong-skill (router)

**What I said:** a long design message: add a Slack-ID step to sign-up ("idk what you think with your HIG mind"), what the attendant dashboard must resolve, and cancellation flow.
**What actually happened:** router named `metrics` (`dashboards?`). `interface-tradeoffs` was invoked.
**What should have happened:** an interface skill, `interface-decisions` at minimum.
**Diagnosis — vocabulary gap.** `interface-decisions` keys on meta-words (`UI`, `UX`, `wireframe`) and misses the objects users actually name: *sign-up step/process*, *the dashboard needs to…*, *HIG*. `metrics` then wins on *dashboard*, which here means a product screen.
**Guess at fix:** add `HIG\b` and `sign.?up\s+(flow|process|step)` to `interface-decisions`. **Waiting** (one data point. The `dashboards?` collision has two, see 2026-10-28, but over-firing is the intended bias).

### 2026-09-18 — code-review — under-fire (router) — **FIX PROPOSED**

**What I said:** *"could you pull aqsa's branch on the attendant app, let's do some review."*
**What actually happened:** nothing matched. `code-review` was invoked.
**What should have happened:** `code-review`.
**Diagnosis — fixed word order.** The object (*branch*) comes 35 characters before *review*, and *review* has no determiner after it. No alternative allows object-then-verb.
**Fix proposed:** covered by the bidirectional clause (see 2026-09-25).

### 2026-09-17 — choose-boring-technology — wrong-skill (router) — **FIX PROPOSED**

**What I said:** *"…our technical advisor said we should create a separate backend … stick with something similar to our tech stack … Do you know in the world of TypeScript a good tool that we could use…"*
**What actually happened:** router named `design-doc` from context. `choose-boring-technology` was invoked.
**What should have happened:** `choose-boring-technology`.
**Diagnosis — fixed word order.** `should\s+(we|i)\s+(use|adopt|switch)` is question order only. *"a good tool that we could use"* puts the noun first and uses *could*. *Tech stack* is not covered either (only `new … stack`).
**Fix proposed:** `(good|best|right)\s+(tool|framework|library|ORM|database)s?\s+(for|that|to)`, plus both noun-first and verb-first orderings. This agrees with 2026-08-26.

### 2026-09-17 — release-hygiene — under-fire (router) — **FIX PROPOSED**

**What I said:** *"…the Release PR that needs to start introducing releases with GitHub Release, and the patch template…"*
**What actually happened:** router named `commit-and-pr-hygiene` (correct, PR template). `release-hygiene` was also invoked.
**What should have happened:** both.
**Diagnosis — vocabulary gap.** The pattern is five fixed phrases (`release notes`, `changelog`, `cut a release`, `versioning scheme`, `tag a release`). *GitHub Release(s)* and *release PR* are missing. This is the third of three diagnosable `release-hygiene` misses. The skill went 4/4 under-fire: the router never once named it when it was used.
**Fix proposed:** add `(github|gh)\s+releases?`, `release\s+(skills?|PRs?|branch(es)?|tags?)`, `versioning`.

### 2026-09-04 — code-review — under-fire (router) — **FIX PROPOSED**

**What I said:** *"One last thing, let's do a review of pr 287"*
**What actually happened:** router named `interface-decisions` from context. `code-review` was invoked.
**What should have happened:** `code-review`.
**Diagnosis — wrong alternation.** The determiner list is `(a|this|my|the)` directly after *review*. *Review **of** PR* is not in it.
**Fix proposed:** `review\w*\s+(of\s+)?…#?\d{2,}` and the bidirectional clause.

### 2026-09-04 — agile-planning — wrong-skill (router)

**What I said:** *"we're working on epics organization"*
**What actually happened:** router named `interface-decisions` and `dependency-management` from context. `agile-planning` was invoked.
**What should have happened:** `agile-planning`.
**Diagnosis — vocabulary gap.** The pattern has `user stor(y|ies)`, `backlog`, and `roadmap`, but not *epic(s)*, the level above stories.
**Guess at fix:** add `epics?\b`. **Waiting.** This is the third `agile-planning` vocabulary gap (with 2026-09-02 and 2026-08-17), but no two share a missing word.

### 2026-09-02 — agile-planning — wrong-skill (router)

**What I said:** *"in the coming week aqsa will do mostly onboarding, she won't be able to do much code/actual app tasks"*
**What actually happened:** router named `new-team-onboarding` (bare `onboard(ing)?`). `agile-planning` was invoked.
**What should have happened:** `agile-planning`. This is capacity planning for the week.
**Diagnosis — vocabulary gap + keyword collision.** Capacity is only matched as `sprint\s+capacity`. *Coming week* and *won't be able to do much* have no planning words at all. `new-team-onboarding` fired on a third party's onboarding, not the user joining a team.
**Guess at fix:** none yet. It is hard to match without over-firing. `onboard(ing)?` also misrouted 2026-08-28, but narrowing it trades against the over-fire bias. **Waiting.**

### 2026-09-01 — release-hygiene — under-fire (router) — **FIX PROPOSED**

**What I said:** *"Next thing I think we should set up is versioning. I want to use GitHub releases and I want strong versioning. There is a skill set up for that."*
**What actually happened:** router named `interface-decisions` and `interface-tradeoffs` from context. `release-hygiene` was invoked.
**What should have happened:** `release-hygiene`.
**Diagnosis — vocabulary gap.** `version(ing)?\s+scheme` needs the word *scheme*. Bare *versioning* and *GitHub releases* miss.
**Fix proposed:** see 2026-09-17.

### 2026-09-01 — commit-and-pr-hygiene — under-fire (router)

**What I said:** *"look at the git management skill to see what would be the best way and how people should work around the development branch."*
**What actually happened:** nothing matched. `commit-and-pr-hygiene` was invoked.
**What should have happened:** `commit-and-pr-hygiene`.
**Diagnosis — vocabulary gap.** Only `branch(ing)?\s+strateg` covers branching. *Development branch*, *git workflow/management*, and *gitflow* miss.
**Guess at fix:** `(develop(ment)?|main|release|feature)\s+branch`, `git\s+(workflow|management|flow)`. **Waiting** (one data point).

### 2026-08-31 — release-hygiene — under-fire (router) — **FIX PROPOSED**

**What I said:** *"…load the release skills from the swe assistant because CI/CD is also maintaining gh actions and gh release, we should start on this too."*
**What actually happened:** router named `mocking` and `operational-tools` from context. `release-hygiene` was invoked.
**What should have happened:** `release-hygiene`. The user asked for it almost by name.
**Diagnosis — vocabulary gap.** Neither *release skills* nor *gh release* is in the alternation.
**Fix proposed:** see 2026-09-17.

### 2026-08-28 — first-run-experience — wrong-skill (router)

**What I said:** *"We can probably document my onboarding experience as the base process for developers."*
**What actually happened:** router named `new-team-onboarding`. `first-run-experience` was invoked.
**What should have happened:** `first-run-experience`, which covers onboarding material for the new hires you will receive.
**Diagnosis — fixed word order.** `onboarding\s+docs?` needs noun-then-doc. *Document … onboarding* is verb-first with words in between.
**Guess at fix:** `document\w*\s+(\w+\s+){0,3}onboarding`, `onboarding\s+(guide|material|process)`. **Waiting** (one data point).

### 2026-08-26 — choose-boring-technology — under-fire (router) — **FIX PROPOSED**

**What I said:** *"We need to check if we should actually pull a whole framework to support the webapp or something like an ORM just to get the seed data going … measure the various options."*
**What actually happened:** nothing matched. `choose-boring-technology` was invoked.
**What should have happened:** `choose-boring-technology`.
**Diagnosis — fixed adjacency + vocabulary gap.** *"we should **actually** pull"* breaks `should\s+(we|i)\s+(use|adopt|switch)` twice: the order is reversed and there is an adverb. *Pull in a framework* and *ORM* are not covered.
**Fix proposed:** `(pull|bring)(ing)?\s+in\s+(an?\s+)?…`, `pull\s+(a\s+)?whole\s+(framework|ORM|library)`, plus the clauses in 2026-09-17.

---


### 2026-08-17 — agile-planning — under-fire (router) — **FIXED**

**What I said (paraphrase):** *"our sprint keeps slipping"* — typed as a throwaway test prompt while verifying the new event capture, not as a real request for help.

**What actually happened:** the router matched nothing at all. Logged as a `route` event with `suggested: []`, which is the first time an under-fire has been visible without someone noticing it by hand.

**What should have happened:** `agile-planning`. The skill's own description lists *"our sprints never finish"* as a trigger, and this is the same complaint in different words.

**Diagnosis — a vocabulary gap, not a regex-mechanics bug.** The clause was:

```
sprints?\s+\w*\s*(never|didn.?t|don.?t|keep)\w*\s*(finish|complete|end)\w*
```

It requires a completion verb from `(finish|complete|end)`. *Slipping*, *overrunning*, *spilling*, and *carrying over* are at least as common for the same complaint and none were covered. It also fixed the order — sprint first, verb second — so *"work keeps carrying over from the sprint"* could not match either. That is the second of the two recurring bugs listed in [`hooks/README.md`](./plugins/swe-assistant/hooks/README.md), and the clause was written from the one phrasing its author had in mind.

**FIXED** — added a bidirectional clause covering `slip`, `overrun`/`overran`, `spill`, and `carry over`, in both orderings. Verified against six phrasings not used to write it, and against four negatives that must not match: *"I sprinted to the finish line"*, *"the deploy slipped past the window"*, *"we had a slip in the release date"*, *"the release overran its window"* — none fire.

**Note on the one-data-point rule.** The triage rule below says not to iterate from a single entry, and this was fixed on one. The exemption is the same one the 2026-08-01 entry used: this is a phrasing the skill's own description already claims to trigger on, so it is a defect against stated behaviour rather than a judgement call about breadth. Tuning still waits for a pattern.

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
