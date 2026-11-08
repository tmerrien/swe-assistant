#!/usr/bin/env python3
"""Ratchet: every trigger phrase a skill advertises should route to that skill.

Each skill's `description` quotes example phrasings ("our sprints never
finish"). The router is a separate regex table. Nothing kept the two in step,
so a description could promise a phrasing the router never matched: two
logged misfires (2026-08-17 agile-planning, the design-document entry) were
exactly that. Measured on 0.2.5: 96 of 222 quoted phrases did not route to
their own skill.

Fixing 96 regexes at once is not the point. This check stops the class from
growing. The current misses are recorded in a committed baseline; a miss NOT
in the baseline fails, and so does a baseline entry that now routes (so the
baseline only ever shrinks). Pay the baseline down at whatever pace suits.

This is a maintainer tool, not part of the plugin, and lives outside
plugins/ so changing it never cuts a release.

Usage:
  ./scripts/check-trigger-routing.py            # check against the baseline
  ./scripts/check-trigger-routing.py --update   # rewrite the baseline to current state
  ./scripts/check-trigger-routing.py --list     # print every miss, grouped by skill
"""
import argparse
import importlib.util
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(REPO, "plugins", "swe-assistant")
SKILLS_DIR = os.path.join(PLUGIN, "skills")
ROUTER = os.path.join(PLUGIN, "scripts", "swe-skill-router.py")
BASELINE = os.path.join(REPO, "scripts", "trigger-routing-baseline.json")

# Quoted runs in a description: straight or curly double quotes, 4+ chars.
QUOTED = re.compile(r"[\"“]([^\"”]{4,})[\"”]")
DESCRIPTION = re.compile(r"^description:\s*(.*)$", re.M)


def load_router():
    spec = importlib.util.spec_from_file_location("swe_skill_router", ROUTER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def trigger_phrases():
    """Yield (skill, phrase) for every quoted phrase in every description."""
    for name in sorted(os.listdir(SKILLS_DIR)):
        path = os.path.join(SKILLS_DIR, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as fh:
            parts = fh.read().split("---", 2)
        m = DESCRIPTION.search(parts[1]) if len(parts) > 2 else None
        if not m:
            continue
        for phrase in QUOTED.findall(m.group(1)):
            yield name, phrase


def current_misses(router):
    misses, total = {}, 0
    for skill, phrase in trigger_phrases():
        total += 1
        if skill not in router.find_matches(phrase):
            misses.setdefault(skill, []).append(phrase)
    return misses, total


def as_pairs(d):
    return {(s, p) for s, ps in d.items() for p in ps}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--update", action="store_true", help="rewrite the baseline")
    ap.add_argument("--list", action="store_true", help="print every current miss")
    args = ap.parse_args()

    misses, total = current_misses(load_router())
    n = sum(len(v) for v in misses.values())
    print(f"{n} of {total} advertised trigger phrases do not route to their own skill.")

    if args.list:
        for skill in sorted(misses):
            print(f"\n{skill}")
            for p in misses[skill]:
                print(f'  - "{p}"')

    if args.update:
        with open(BASELINE, "w", encoding="utf-8") as fh:
            json.dump({k: misses[k] for k in sorted(misses)}, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"Baseline written: {os.path.relpath(BASELINE, REPO)}")
        return 0

    try:
        with open(BASELINE, encoding="utf-8") as fh:
            baseline = json.load(fh)
    except FileNotFoundError:
        print("No baseline. Run with --update to create one.")
        return 1

    new = sorted(as_pairs(misses) - as_pairs(baseline))
    fixed = sorted(as_pairs(baseline) - as_pairs(misses))
    if new:
        print(f"\nFAIL: {len(new)} new miss(es). Widen the router pattern, or reword the description:")
        for s, p in new:
            print(f'  {s}: "{p}"')
    if fixed:
        print(f"\nFAIL: {len(fixed)} baseline entr(ies) now route. Run --update to shrink the baseline:")
        for s, p in fixed:
            print(f'  {s}: "{p}"')
    if new or fixed:
        return 1
    print("OK: no new misses; baseline is current.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
