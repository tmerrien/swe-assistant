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

# Mirror skills/ exactly (--delete so removed skills actually disappear), and
# refresh the plugin manifest.
rsync -a --delete "$SRC/skills/" "$DEST/skills/"
if [[ -d "$SRC/.claude-plugin" ]]; then
  rsync -a "$SRC/.claude-plugin/" "$DEST/.claude-plugin/"
fi

DEST_COUNT=$(find "$DEST/skills" -maxdepth 1 -mindepth 1 -type d | wc -l)

echo "synced $SRC_COUNT skills -> $DEST"
if [[ "$SRC_COUNT" != "$DEST_COUNT" ]]; then
  echo "warning: destination now reports $DEST_COUNT skills (expected $SRC_COUNT)" >&2
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
