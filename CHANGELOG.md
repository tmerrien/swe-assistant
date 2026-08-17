# Changelog

Notable changes to the `swe-assistant` plugin. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Not every released version appears below, and that is deliberate.** Releases
are cut automatically — any push touching `plugins/swe-assistant/` bumps and
tags itself — so versions are produced faster than prose is worth writing. A
description tweak does not merit a paragraph, and inventing one for every patch
is how a changelog turns into a commit log nobody reads.

Entries here cover releases worth describing. **The complete record is the tags
and the git history**, which are exhaustive by construction; this file is the
edited version. If a version is missing below, `git log v0.2.0..v0.2.1` is the
authoritative answer to what changed in it.

## Versioning rules for this repository

The `version` field in `plugins/swe-assistant/.claude-plugin/plugin.json` is not
decoration. Claude Code resolves a plugin's version from the first of
`plugin.json` → the marketplace entry → the git commit SHA, and uses the result
as the cache key that decides whether an update is available. **If the version
does not move, installed users receive nothing**, however many commits land.

**This is enforced rather than remembered**, because remembering is what failed
the first time. [`.github/workflows/release.yml`](./.github/workflows/release.yml)
runs on any push touching `plugins/swe-assistant/`, calls
[`scripts/bump-version.py`](./scripts/bump-version.py) to move all three version
fields together, then commits and tags. Reading notes, `docs/`, `READING-LIST.md`,
and `MISFIRE-LOG.md` sit outside that path and never cut a release.

- **Patch** — the default. Skill content revised, router patterns tuned, docs
  corrected.
- **Minor** — skills added, or the plugin gains a component or a requirement.
  Opt in with `[minor]` in the commit message.
- **Major** — a skill removed or renamed, which breaks `/<skill-name>`, the
  router's `PATTERNS` keys, and anyone's habits. Opt in with `[major]`.

Major and minor stay manual because only the author knows whether a rename
happened; patch is safe to assume. `./scripts/bump-version.py --check` fails
when a committed plugin change has no bump behind it — note it compares against
the last tag, so uncommitted work is invisible to it.

Three files carry a version, and they mean different things:

| File | Meaning | When it moves |
|---|---|---|
| `plugins/swe-assistant/.claude-plugin/plugin.json` | What ships. The update gate. | Every plugin change, per the rules above |
| `.claude-plugin/marketplace.json` | The catalog's own version | When the catalog changes. Kept aligned here because this marketplace hosts one plugin and divergence would only confuse |
| `CITATION.cff` | The citable release | At each tagged release, with `date-released` |

---

## [0.2.0] — 2026-08-17

The plugin gains its own hooks, and an optional dependency on Python 3.

**If you were on 0.1.0, this is the first update you have ever received.**
`plugin.json` sat at `0.1.0` from the first commit to this release, so the
version never moved and no update was ever offered. Everything added across that
period arrives now, including roughly a dozen skills beyond the original set and
a router fix that had made `design-doc` unroutable for most phrasings.

### Added

- The skill router ships **inside the plugin**, registered in
  `hooks/hooks.json` and auto-loaded on install. No `settings.json` entry and no
  manual copy into `~/.claude/hooks` — both previously required.
- **Routing event capture.** The router records every prompt it routes,
  including ones it matched nothing on, and a `PostToolUse` hook records which
  skill actually ran. Disagreement between the two is a misfire candidate.
  Events land in `~/.claude/swe-assistant/events.jsonl`
  (`SWE_ASSISTANT_LOG_DIR` overrides).
- `scripts/misfire-report.py` ranks misfire candidates and offers `--verify`,
  a health check for the two silent failures worth catching: the hook never
  running, and the `PostToolUse` matcher going stale.

### Changed

- `MISFIRE-LOG.md` is now written from the report at triage time rather than
  from memory. Detection is automatic; diagnosis stays manual, because the value
  of an entry is the root cause and no hook produces that.
- `scripts/sync-to-claude.sh` mirrors `hooks/` and `scripts/` into the plugin
  cache alongside `skills/`, and flags a stale hand-installed router that would
  now double-fire.

### Fixed

- `scripts/sync-to-claude.sh` no longer requires `rsync`, which is absent from a
  default Git Bash install and made the script fail outright on Windows.

### Requirements

Python 3 on `PATH` as `py`, `python3`, or `python` — tried in that order. The
skills all work without it; only the routing floor is lost. On Windows, note
that `python`/`python3` are frequently Microsoft Store alias stubs rather than
real interpreters. See
[`plugins/swe-assistant/hooks/README.md`](./plugins/swe-assistant/hooks/README.md).

---

## [0.1.0] — 2026-08-06

Initial published version: the skill collection, the four-pillar rubric in
`OBJECTIVES.md`, the five-stage map in `JOURNEY.md`, and the academic
documentation under `docs/`.

Content continued to change substantially after this tag without the version
moving, so `0.1.0` does not name a single tree. Consult the git history for what
a particular install actually contained; the install manifest records the commit
SHA under `~/.claude/plugins/.install-manifests/`.
