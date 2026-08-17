#!/usr/bin/env python3
"""Move every version field that has to move, together.

The plugin's version is the update gate: Claude Code resolves a plugin version
from plugin.json first and uses it as the cache key for update detection, so a
version that does not move offers users no update. That is how this repository
spent 83 commits on a static 0.1.0 delivering nothing.

Three files carry a version and they drift by hand, so nothing here is left to
memory:

  plugins/swe-assistant/.claude-plugin/plugin.json   the update gate
  .claude-plugin/marketplace.json                    the catalog's own version
  CITATION.cff                                       the citable release

README.md's skill-count badge is maintained here too. It is not a version, but
it is the same kind of fact — stated in one place, derived from another, and
silently wrong the moment nobody remembers. It read 44 against a real count of
50 for five days on the repository's front page.

Usage:
  ./scripts/bump-version.py patch|minor|major   # bump, write, print new version
  ./scripts/bump-version.py --check             # exit 1 if a bump, badge, or archive is owed
  ./scripts/bump-version.py --sync-badge        # fix the badge without bumping
  ./scripts/bump-version.py --show              # print the current version

`--check` is the guard, and it tests three things that go wrong independently:

  the version did not move       -> installed users are offered nothing
  the badge disagrees with disk  -> the front page states something untrue
  a tag has no GitHub Release    -> Zenodo never deposited it, so no DOI

All three are reported rather than stopping at the first, because a release
that goes wrong tends to go wrong in more than one way at once. The release
check needs `gh` and network; without either it is skipped rather than failed,
so this stays usable offline. It compares against the last tag, so uncommitted
work is invisible to it.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date

# Windows consoles default to a legacy codepage, which mangles the em-dashes
# below into replacement characters. Harmless if unavailable.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_JSON = os.path.join(REPO, "plugins", "swe-assistant", ".claude-plugin", "plugin.json")
MARKETPLACE_JSON = os.path.join(REPO, ".claude-plugin", "marketplace.json")
CITATION = os.path.join(REPO, "CITATION.cff")
README = os.path.join(REPO, "README.md")
SKILLS_DIR = os.path.join(REPO, "plugins", "swe-assistant", "skills")
PLUGIN_DIR = "plugins/swe-assistant"


def git(*args):
    """Run a git command in the repo. Returns stripped stdout, or '' on failure."""
    try:
        out = subprocess.run(
            ["git", "-C", REPO, *args],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def current_version() -> str:
    with open(PLUGIN_JSON, encoding="utf-8") as fh:
        return json.load(fh)["version"]


def bump(version: str, level: str) -> str:
    try:
        major, minor, patch = (int(p) for p in version.split("."))
    except ValueError:
        raise SystemExit(f"version {version!r} is not MAJOR.MINOR.PATCH")
    if level == "major":
        return f"{major + 1}.0.0"
    if level == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def write_json_version(path: str, version: str) -> None:
    """Rewrite the version line in place.

    Deliberately textual rather than json.dump: these files are hand-maintained
    and reserialising them would reorder keys and reflow the whole file, turning
    a one-line change into an unreviewable diff.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    new, n = re.subn(r'("version"\s*:\s*")[^"]*(")', rf"\g<1>{version}\g<2>", text, count=1)
    if n != 1:
        raise SystemExit(f"no version field found in {path}")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)


def write_citation(version: str, released: str) -> None:
    with open(CITATION, encoding="utf-8") as fh:
        text = fh.read()
    text, n1 = re.subn(r"(?m)^version:.*$", f"version: {version}", text, count=1)
    text, n2 = re.subn(r'(?m)^date-released:.*$', f'date-released: "{released}"', text, count=1)
    if n1 != 1 or n2 != 1:
        raise SystemExit("CITATION.cff is missing version or date-released")
    with open(CITATION, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def count_skills() -> int:
    """The roster size, counted from disk rather than trusted from a badge."""
    try:
        return sum(
            1 for name in os.listdir(SKILLS_DIR)
            if os.path.isfile(os.path.join(SKILLS_DIR, name, "SKILL.md"))
        )
    except OSError:
        return -1


def badge_count() -> int:
    """What README.md currently claims. -1 if the badge is missing."""
    try:
        with open(README, encoding="utf-8") as fh:
            m = re.search(r"skills-(\d+)-blue", fh.read())
        return int(m.group(1)) if m else -1
    except OSError:
        return -1


def write_badge(count: int) -> bool:
    """Rewrite the skill-count badge. Returns True if it changed.

    The count appears twice — once as the image alt text and once inside the
    shields.io URL — and updating only one leaves the badge rendering a number
    that disagrees with its own label.
    """
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    new = re.sub(r"Skills: \d+", f"Skills: {count}", text)
    new = re.sub(r"skills-\d+-blue", f"skills-{count}-blue", new)
    if new == text:
        return False
    with open(README, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)
    return True


def tags_without_releases():
    """Version tags that have no published GitHub Release.

    A tag without a Release is never deposited to Zenodo and so has no DOI —
    the state 0.2.3 was left in when `gh release create` hit a transient 503.
    The job went red, but a red job does not look like "a released version is
    unarchived", so it is worth checking rather than reading logs.

    Returns None when the answer is unknown — no `gh`, not authenticated, or
    no network — so that this stays usable offline instead of failing loudly
    about something it cannot see.
    """
    if not shutil.which("gh"):
        return None
    try:
        out = subprocess.run(
            ["gh", "release", "list", "--limit", "200", "--json", "tagName", "--jq", ".[].tagName"],
            cwd=REPO, capture_output=True, text=True, check=True, timeout=30,
        )
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return None
    released = {t.strip() for t in out.stdout.split() if t.strip()}
    tags = {t.strip() for t in git("tag", "-l", "v*").splitlines() if t.strip()}
    return sorted(tags - released)


def last_tag() -> str:
    return git("describe", "--tags", "--abbrev=0", "--match", "v*")


def plugin_changed_since(ref: str) -> bool:
    """Did anything under the plugin directory change since `ref`?"""
    if not ref:
        return True  # no tag yet: treat as owing a release
    return bool(git("diff", "--name-only", f"{ref}..HEAD", "--", PLUGIN_DIR))


def version_moved_since(ref: str) -> bool:
    if not ref:
        return False
    before = git("show", f"{ref}:plugins/swe-assistant/.claude-plugin/plugin.json")
    if not before:
        return True  # cannot tell; do not block on it
    try:
        return json.loads(before)["version"] != current_version()
    except (ValueError, KeyError):
        return True


def check() -> int:
    """Fail when a release is owed, or a stated fact has drifted.

    Both are checked every time rather than short-circuiting on the first pass,
    because they fail independently: a version that did not move ships nothing,
    and a badge that did not move states something untrue on the front page.
    Neither failure is loud on its own — that is the whole reason for this.
    """
    ref = last_tag()
    version = current_version()
    problems = []

    if plugin_changed_since(ref) and not version_moved_since(ref):
        changed = git("diff", "--name-only", f"{ref}..HEAD", "--", PLUGIN_DIR).splitlines()
        lines = [
            f"BUMP OWED: {PLUGIN_DIR}/ changed since {ref} but the version is still {version}.",
            "  Users will receive none of this — the version is the update gate:",
        ]
        lines += [f"    {p}" for p in changed[:10]]
        if len(changed) > 10:
            lines.append(f"    ... and {len(changed) - 10} more")
        lines += [
            "",
            "    ./scripts/bump-version.py patch   # content revised, patterns tuned",
            "    ./scripts/bump-version.py minor   # skills added, or a new component",
            "    ./scripts/bump-version.py major   # a skill removed or renamed",
        ]
        problems.append("\n".join(lines))
    else:
        print(f"OK: version {version} is current for {PLUGIN_DIR}/.")

    actual, claimed = count_skills(), badge_count()
    if actual >= 0 and claimed >= 0 and actual != claimed:
        problems.append(
            f"BADGE STALE: README.md claims {claimed} skills; there are {actual}.\n"
            "    ./scripts/bump-version.py --sync-badge"
        )
    elif actual >= 0 and claimed == actual:
        print(f"OK: README badge and roster agree at {actual} skills.")

    unreleased = tags_without_releases()
    if unreleased is None:
        print("SKIP: cannot reach GitHub, so tags-versus-releases went unchecked.")
    elif unreleased:
        problems.append(
            "UNARCHIVED: these tags have no GitHub Release, so Zenodo never\n"
            "  deposited them and they have no DOI:\n"
            + "\n".join(f"    {t}" for t in unreleased)
            + "\n\n    gh release create <tag> --verify-tag --generate-notes --latest"
        )
    else:
        n = len(git("tag", "-l", "v*").split())
        print(f"OK: all {n} version tags have a published release.")

    for p in problems:
        print("\n" + p)
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("level", nargs="?", choices=["patch", "minor", "major"])
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if a bump is owed or the skill-count badge has drifted")
    ap.add_argument("--show", action="store_true", help="print the current version")
    ap.add_argument("--sync-badge", action="store_true",
                    help="rewrite the README skill count from the roster, without bumping")
    args = ap.parse_args()

    if args.show:
        print(current_version())
        return 0
    if args.check:
        return check()
    if args.sync_badge:
        n = count_skills()
        print(f"README skill count -> {n}" if write_badge(n)
              else f"README skill count already {n}")
        return 0
    if not args.level:
        ap.error("give a level (patch/minor/major), --check, --show, or --sync-badge")

    old = current_version()
    new = bump(old, args.level)
    released = date.today().isoformat()

    write_json_version(PLUGIN_JSON, new)
    write_json_version(MARKETPLACE_JSON, new)
    write_citation(new, released)

    print(f"{old} -> {new}  (released {released})")
    print("  plugins/swe-assistant/.claude-plugin/plugin.json")
    print("  .claude-plugin/marketplace.json")
    print("  CITATION.cff")

    # The roster only changes when the plugin changes, which is exactly when a
    # bump happens — so the badge is refreshed here rather than on its own
    # schedule. It sat at 44 for five days against a real count of 50.
    skills = count_skills()
    if skills >= 0 and write_badge(skills):
        print(f"  README.md (skill count -> {skills})")
    print(f"\nCHANGELOG.md is not touched — write the entry for {new} yourself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
