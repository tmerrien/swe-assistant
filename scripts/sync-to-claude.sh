#!/usr/bin/env bash
#
# sync-to-claude.sh — push the local plugin into Claude's plugin cache so local
# skill edits go live without a GitHub round-trip.
#
# Usage:  ./scripts/sync-to-claude.sh
# Then:   run /reload-plugins in Claude (or restart the app).
#
# Why this exists: the installed plugin normally comes from GitHub, so editing a
# SKILL.md locally has no effect until you commit, push, and update the
# marketplace. This script copies the local plugin directly into the cache
# instead. It writes a real directory (not a symlink) so that normal plugin
# operations can't break in confusing ways — if a future `/plugin marketplace
# update` overwrites it, you simply get the published version back.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO/plugins/swe-assistant"
CACHE_ROOT="$HOME/.claude/plugins/cache/swe-assistant/swe-assistant"

if [[ ! -d "$SRC/skills" ]]; then
  echo "error: no skills dir at $SRC/skills" >&2
  exit 1
fi

# Find the installed version dir (e.g. 0.1.0). If several, take the newest.
DEST="$(find "$CACHE_ROOT" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | sort -V | tail -1 || true)"

if [[ -z "$DEST" ]]; then
  echo "error: plugin does not appear to be installed." >&2
  echo "       expected a version dir under: $CACHE_ROOT" >&2
  echo "       install it first in Claude:" >&2
  echo "         /plugin marketplace add tmerrien/swe-assistant" >&2
  echo "         /plugin install swe-assistant@swe-assistant" >&2
  exit 1
fi

# Refuse to clobber a symlink — that would be someone else's setup, not ours.
if [[ -L "$DEST" ]]; then
  echo "error: $DEST is a symlink; not touching it." >&2
  echo "       remove it first if you want the copy-based sync." >&2
  exit 1
fi

SRC_COUNT=$(find "$SRC/skills" -maxdepth 1 -mindepth 1 -type d | wc -l)

# Mirror one directory exactly, removing anything the source no longer has.
# rsync is the obvious tool but is not present in a default Git Bash install on
# Windows, where this script would otherwise fail outright — so fall back to a
# remove-then-copy, which has the same delete semantics.
mirror() {
  local src="$1" dest="$2"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a --delete "$src/" "$dest/"
  else
    rm -rf "$dest"
    mkdir -p "$dest"
    cp -R "$src/." "$dest/"
  fi
}

# Stale copies must actually disappear: a removed skill left behind still loads,
# and a stale router would route against the previous skill roster. hooks/ and
# scripts/ are part of the plugin now, so they travel with it.
mirror "$SRC/skills" "$DEST/skills"
for sub in .claude-plugin hooks scripts; do
  if [[ -d "$SRC/$sub" ]]; then
    mirror "$SRC/$sub" "$DEST/$sub"
  fi
done

DEST_COUNT=$(find "$DEST/skills" -maxdepth 1 -mindepth 1 -type d | wc -l)

echo "synced $SRC_COUNT skills -> $DEST"
if [[ "$SRC_COUNT" != "$DEST_COUNT" ]]; then
  echo "warning: destination now reports $DEST_COUNT skills (expected $SRC_COUNT)" >&2
fi

# --- stale standalone hook --------------------------------------------------
# The router used to be installed by hand into ~/.claude/hooks and registered in
# settings.json. It now ships inside the plugin (hooks/hooks.json, auto-loaded),
# so an old copy left behind would route twice against a stale skill roster.
# Flag it rather than delete it — removing a file someone may have tuned is not
# this script's call to make.
LEGACY_HOOK="$HOME/.claude/hooks/swe-skill-router.py"
if [[ -f "$LEGACY_HOOK" ]]; then
  echo
  echo "note: found a pre-plugin router at $LEGACY_HOOK"
  echo "      the router now ships with the plugin. that copy is stale and will"
  echo "      double-fire. remove it, and drop its UserPromptSubmit entry from"
  echo "      ~/.claude/settings.json:"
  echo "        rm \"$LEGACY_HOOK\""
fi

# Honesty check: if the repo is dirty or unpushed, the skills now loaded are not
# what anyone else would get. That matters when logging trigger misfires.
cd "$REPO"
DIRTY="$(git status --porcelain 2>/dev/null || true)"
UNPUSHED="$(git log --oneline @{upstream}..HEAD 2>/dev/null | wc -l || echo 0)"

if [[ -n "$DIRTY" ]]; then
  echo "note: repo has uncommitted changes — you are testing unpublished skills."
fi
if [[ "$UNPUSHED" -gt 0 ]]; then
  echo "note: $UNPUSHED commit(s) not pushed to origin."
fi

echo
echo "next: run /reload-plugins in Claude to pick this up."
