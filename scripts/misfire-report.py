#!/usr/bin/env python3
"""Turn the captured routing events into misfire candidates for triage.

This is a maintainer tool, not part of the plugin. It reads the event log the
two hooks write (`~/.claude/swe-assistant/events.jsonl`) and reports where the
router's suggestion and Claude's actual skill choice disagreed.

It does NOT write MISFIRE-LOG.md. The log's value is the diagnosis — "the
alternation ends in `design\\s+doc` followed by `\\b`, so the boundary falls
between `c` and `u`" — and no amount of event capture produces that. What this
replaces is the part that depended on remembering: noticing the misfire at all.
Run it at triage time, read the candidates, write up the ones that turn out to
be real.

Usage:
  ./scripts/misfire-report.py             # full report
  ./scripts/misfire-report.py --verify    # health check only: is capture working?
  ./scripts/misfire-report.py --days 30   # limit to recent events
"""
import argparse
import json
import os
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO, "plugins", "swe-assistant", "skills")

# Windows consoles default to a legacy codepage, which mangles the em-dashes
# and section marks below into replacement characters. Harmless if unavailable.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass


def log_path() -> str:
    d = os.environ.get("SWE_ASSISTANT_LOG_DIR") or "~/.claude/swe-assistant"
    return os.path.join(os.path.expanduser(d), "events.jsonl")


def known_skills() -> set:
    """The skill roster, read from the repo rather than hardcoded."""
    try:
        return {
            name for name in os.listdir(SKILLS_DIR)
            if os.path.isfile(os.path.join(SKILLS_DIR, name, "SKILL.md"))
        }
    except OSError:
        return set()


def bare(skill: str) -> str:
    """Strip a `plugin:` namespace prefix, if present."""
    return skill.split(":", 1)[1] if ":" in skill else skill


def read_events(path, days):  # `days` may be None; unannotated to keep the 3.8 floor
    if not os.path.exists(path):
        return []
    cutoff = None
    if days:
        cutoff = datetime.now().astimezone() - timedelta(days=days)

    events = []
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                continue  # a torn line from a concurrent append; skip it
            if cutoff:
                try:
                    if datetime.strptime(ev["ts"], "%Y-%m-%dT%H:%M:%S%z") < cutoff:
                        continue
                except (KeyError, ValueError):
                    pass
            events.append(ev)
    return events


def build_windows(events: list) -> list:
    """Pair each `route` with the skills invoked before the next route.

    A window is one routing decision and its outcome. Invocations arriving
    before any route in a session are dropped — there is no decision to judge
    them against.
    """
    by_session = defaultdict(list)
    for ev in events:
        by_session[ev.get("session_id")].append(ev)

    windows = []
    for session, evs in by_session.items():
        current = None
        for ev in evs:
            if ev.get("event") == "route":
                if current is not None:
                    windows.append(current)
                current = {
                    "session": session,
                    "ts": ev.get("ts"),
                    "suggested": [bare(s) for s in ev.get("suggested") or []],
                    "prompt": ev.get("prompt"),
                    "invoked": [],
                }
            elif ev.get("event") == "invoke" and current is not None:
                current["invoked"].append(bare(ev.get("skill") or ""))
        if current is not None:
            windows.append(current)
    return windows


def verify(events: list) -> int:
    """Health check. Silent capture failure is the thing worth catching."""
    routes = [e for e in events if e.get("event") == "route"]
    invokes = [e for e in events if e.get("event") == "invoke"]

    print(f"log file      : {log_path()}")
    print(f"route events  : {len(routes)}")
    print(f"invoke events : {len(invokes)}")
    if events:
        print(f"first / last  : {events[0].get('ts')}  ..  {events[-1].get('ts')}")

    if not routes:
        print("\nFAIL: no routing events captured — the UserPromptSubmit hook is not running.")
        print("\nInterpreters visible from THIS shell:")
        for name in ("py", "python3", "python"):
            found = shutil.which(name)
            if not found:
                print(f"  {name:<8} not found")
            elif "WindowsApps" in found:
                print(f"  {name:<8} {found}")
                print(f"  {'':<8} ^ Microsoft Store alias stub, NOT a real interpreter.")
                print(f"  {'':<8}   Disable it under Settings > Apps > Advanced app")
                print(f"  {'':<8}   settings > App execution aliases, or install Python.")
            else:
                print(f"  {name:<8} {found}")
        print("\n  Careful: the hook runs under Claude Code's environment, not this")
        print("  shell's. A terminal that finds Python proves nothing about the hook.")
        print("  If the names above look correct but capture is still zero, Claude Code")
        print("  has most likely inherited a stale PATH from whatever launched it —")
        print("  the usual state on Windows right after installing Python, because")
        print("  relaunching from the same Explorer session reuses the old environment.")
        print("  Sign out and back in (or reboot), then start Claude Code fresh.")
        print("\n  Then confirm the plugin is installed and enabled: /plugins")
        return 1
    if not invokes:
        print("\nWARN: routing is captured but no skill invocations are.")
        print("  Either no skill has been invoked yet, or the PostToolUse matcher")
        print('  ("Skill" in hooks/hooks.json) no longer matches the tool name.')
        print("  Invoke any skill once, then re-run. If it stays zero, the matcher")
        print("  is stale — that is the failure this check exists to surface.")
        return 1

    tool_names = Counter(e.get("tool_name") for e in invokes)
    print(f"\nOK: capture is working. Tool names seen: {dict(tool_names)}")
    return 0


def report(events: list) -> int:
    roster = known_skills()
    windows = build_windows(events)
    if not windows:
        print("No routing decisions captured yet. Run with --verify for a health check.")
        return 0

    under = Counter()      # invoked but not suggested — the router missed it
    under_examples = defaultdict(list)
    over = Counter()       # suggested, nothing of ours invoked in the window
    used = Counter()

    for w in windows:
        ours = [s for s in w["invoked"] if s in roster]
        for s in ours:
            used[s] += 1
            if s not in w["suggested"]:
                under[s] += 1
                if w.get("prompt"):
                    under_examples[s].append(w["prompt"])
        if w["suggested"] and not ours:
            for s in w["suggested"]:
                over[s] += 1

    print(f"{len(windows)} routing decisions, {sum(used.values())} skill invocations, "
          f"{len(roster)} skills in roster\n")

    print("UNDER-FIRE candidates — invoked without the router naming it")
    print("(the highest-signal category: these were previously invisible)")
    if under:
        for skill, n in under.most_common(15):
            total = used[skill]
            print(f"  {n:4d} / {total:<4d}  {skill}")
            for ex in under_examples[skill][:1]:
                print(f"              e.g. {ex[:100].replace(chr(10), ' ')!r}")
    else:
        print("  none")

    print("\nOVER-FIRE candidates — suggested, but no skill of ours was used")
    print("(noisy by design: most prompts legitimately need no skill. Look for")
    print(" a name that dominates this list while rarely appearing above.)")
    if over:
        for skill, n in over.most_common(15):
            print(f"  {n:4d}  {skill}  (actually used {used[skill]}x)")
    else:
        print("  none")

    never = sorted(roster - set(used))
    print(f"\nNEVER INVOKED ({len(never)} of {len(roster)})")
    print("(not necessarily broken — the situation may simply not have come up)")
    print("  " + (", ".join(never) if never else "none"))

    print("\nNext: read docs/METHODOLOGY.md §6, diagnose the ones that look real,")
    print("and write them up in MISFIRE-LOG.md. This tool finds candidates; it")
    print("does not diagnose them.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verify", action="store_true",
                    help="health check only: confirm both hooks are capturing")
    ap.add_argument("--days", type=int, default=None,
                    help="only consider events from the last N days")
    args = ap.parse_args()

    events = read_events(log_path(), args.days)
    if args.verify:
        return verify(events)
    if not events:
        print(f"No events at {log_path()}.")
        print("Run --verify for what to check.")
        return 0
    return report(events)


if __name__ == "__main__":
    sys.exit(main())
