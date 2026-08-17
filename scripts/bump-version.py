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

Usage:
  ./scripts/bump-version.py patch|minor|major   # bump, write, print new version
  ./scripts/bump-version.py --check             # exit 1 if a bump is owed
  ./scripts/bump-version.py --show              # print the current version

`--check` is the guard: it fails when plugins/swe-assistant/ has changed since
the last tag without the version moving. Run it locally or in CI.
"""
import argparse
import json
import os
import re
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
    """Fail when a release is owed. This is the guard that replaces remembering."""
    ref = last_tag()
    version = current_version()
    if not plugin_changed_since(ref):
        print(f"OK: {PLUGIN_DIR}/ unchanged since {ref or 'the beginning'}; "
              f"version {version} needs no bump.")
        return 0
    if version_moved_since(ref):
        print(f"OK: {PLUGIN_DIR}/ changed and the version moved to {version}.")
        return 0

    changed = git("diff", "--name-only", f"{ref}..HEAD", "--", PLUGIN_DIR).splitlines()
    print(f"BUMP OWED: {PLUGIN_DIR}/ changed since {ref} but the version is still {version}.")
    print("\nUsers will receive none of this — the version is the update gate:")
    for path in changed[:10]:
        print(f"  {path}")
    if len(changed) > 10:
        print(f"  ... and {len(changed) - 10} more")
    print("\n  ./scripts/bump-version.py patch   # content revised, patterns tuned")
    print("  ./scripts/bump-version.py minor   # skills added, or a new component")
    print("  ./scripts/bump-version.py major   # a skill removed or renamed")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("level", nargs="?", choices=["patch", "minor", "major"])
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if the plugin changed since the last tag without a bump")
    ap.add_argument("--show", action="store_true", help="print the current version")
    args = ap.parse_args()

    if args.show:
        print(current_version())
        return 0
    if args.check:
        return check()
    if not args.level:
        ap.error("give a level (patch/minor/major), or --check / --show")

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
    print(f"\nCHANGELOG.md is not touched — write the entry for {new} yourself.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
