# Hooks

Optional Claude Code hooks that support the plugin. These are **not part of the plugin** — the plugin works without them. They live here so they are version-controlled rather than surviving only as a single untracked file in a user's home directory.

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

### Installing it

`scripts/sync-to-claude.sh` installs this file to `~/.claude/hooks/` alongside the plugin sync. It warns before overwriting a version that differs from the repo, so local tuning is not silently lost — if you have been editing the installed copy directly, copy it back here first.

Register it in `~/.claude/settings.json` as a `UserPromptSubmit` hook. It is a plain Python 3 script with no third-party dependencies.
