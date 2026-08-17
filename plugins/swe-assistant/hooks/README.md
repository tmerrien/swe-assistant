# Hooks

Claude Code hooks that ship **as part of the plugin**. `hooks.json` is auto-loaded when the plugin is installed — no `settings.json` editing, no separate install step.

Both hooks are optional in the sense that matters: the 50 skills work without them. What the hooks add is a routing floor and the evidence to tune it.

| File | Event | What it does |
|---|---|---|
| `../scripts/swe-skill-router.py` | `UserPromptSubmit` | Suggests skills that plausibly apply, and records what it suggested |
| `../scripts/swe-skill-invocations.py` | `PostToolUse` (matcher `Skill`) | Records which skill was actually invoked |

Both write to `~/.claude/swe-assistant/events.jsonl`. Override the directory with `SWE_ASSISTANT_LOG_DIR`.

## `swe-skill-router.py`

A `UserPromptSubmit` hook that pattern-matches the user's prompt against every skill in this repository and injects the names of the ones that plausibly apply.

### What problem it solves

Skills in this plugin are triggered by the runtime's semantic match against each skill's `description` field. That match is good but not exhaustive — it can miss situations that are described obliquely, and it competes for attention with everything else in the context.

The router is a **cheap regex floor** underneath that semantic match. It does not decide anything; it surfaces candidate skill names so they are visible at the moment the user's situation arises.

### Design stance: it is tuned to over-fire

This is deliberate, and it is the opposite of how most routers are tuned.

A skill that fires when it shouldn't costs one visible false positive, which the user can see and correct. A skill that *silently* fails to fire costs the user the help they needed, and produces **no signal at all** that anything went wrong. The asymmetry favours over-firing, so the patterns are broad and the injected text tells the model to skip a suggestion in one clause if it plainly does not fit.

Treat the router's output as **a floor, not a ceiling.** If a skill applies and the router did not name it, it should still be invoked.

### Pattern maintenance — the two bugs that keep recurring

Both have been introduced and fixed more than once. Check for them when adding patterns:

1. **Trailing `\b` after a stem.** `backward.?compat\b` fails on *"backward compatible"*, because `\b` cannot match between `t` and `i`. Use `compat\w*` instead of `compat\b` whenever the pattern ends on a word stem.

2. **Rigid adjacency in multi-word patterns.** `everything\s+looks\s+important` fails on *"everything on this dashboard looks equally important"*. Real prompts put words in the middle. Use a bounded gap — `everything.{0,30}?\b(looks|is)\s+important` — and allow both orderings when either reads naturally.

**Always test a new pattern against a sentence you did not write it from.** Both bugs above survived review because they were tested against their own source phrasing.

## Event capture

The design stance above has a gap it cannot close on its own: the router says what it *thinks* applies, and nothing recorded what actually happened next. A silent non-fire produced "no signal at all" — which is exactly why misfires only got written down when someone remembered to write them down.

The two hooks close that. The router logs every prompt it routed, **including the ones it matched nothing on**; the `PostToolUse` hook logs every skill invocation. Within a session, one routing decision plus the skills invoked before the next routing decision is a window, and disagreement inside that window is a misfire candidate:

- **invoked but not suggested** → the router missed it (under-fire). Previously invisible; now the highest-signal row in the report.
- **suggested but nothing used** → possible over-fire. Noisy by design, since most prompts legitimately need no skill.

Read the candidates with `scripts/misfire-report.py` in the repository root. That tool finds candidates; it does not diagnose them — diagnosis still goes in `MISFIRE-LOG.md` by hand, because the useful part of an entry is the root cause, and no hook produces that.

### Prompt text is opt-in

Skill names, counts, and timestamps are always recorded. The **user's prompt text is not**, unless `SWE_ASSISTANT_LOG_PROMPTS=1` is set. An installed plugin should not write someone's words to disk uninvited; the maintainer opts in on their own machine, where diagnosing a bad pattern needs the actual sentence.

### Failure behaviour

Both scripts exit 0 unconditionally and swallow every logging error. A hook that breaks a prompt or a tool call is worse than no hook, and a gap in the log is the cheaper failure.

That safety has one consequence worth knowing: because the scripts always exit 0, the `python3 … || python …` fallback in `hooks.json` never runs the script twice. The fallback fires only when the interpreter itself is missing.

### Requirements

Python 3, on `PATH` as `py`, `python3`, or `python` — the command tries all three in that order. No third-party dependencies.

If none resolves, the skills continue to work; you lose only the routing floor.

**Two Windows failure modes, both observed:**

1. **Store alias stubs.** `python` and `python3` in `%LOCALAPPDATA%\Microsoft\WindowsApps` are Microsoft Store shortcuts, not interpreters. They print an install advert and exit 49. The `||` chain treats that nonzero exit as a miss and moves on, which is why the chain exists — but if the stubs are the *only* thing on `PATH`, every link fails. Disable them under **Settings → Apps → Advanced app settings → App execution aliases**.

2. **A stale inherited `PATH`.** Installing Python updates the registry `PATH`, but a running process keeps the environment it was started with — and relaunching Claude Code from the same Explorer session inherits that same stale copy. The symptom is confusing: a terminal finds Python perfectly while the hook cannot, because they have different environments. Sign out and back in (or reboot) so the new `PATH` actually propagates.

The second one is the nastier of the two, because every check you can run *from a terminal* passes. Confirm capture is actually running with:

```
./scripts/misfire-report.py --verify
```

That check exists specifically to catch the two silent failures: the hook never running, and the `PostToolUse` matcher going stale if the `Skill` tool is ever renamed.
