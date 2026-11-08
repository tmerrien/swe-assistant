#!/usr/bin/env python3
"""PostToolUse hook: record which skill actually got invoked.

The router (`swe-skill-router.py`) records what it *suggested*. This records
what Claude actually *did*. Comparing the two within a session is what turns a
routing miss from an invisible event into a logged one — the asymmetry the
router's design stance rests on (see hooks/README.md).

Records every skill invocation, not just this plugin's. A prompt where
`swe-assistant:incident-response` was suggested but some other skill fired is
the `wrong-skill` category from MISFIRE-LOG.md, and it is only visible if the
other skill is recorded too.

Exits 0 unconditionally and swallows every error. A logger that breaks a tool
call is worse than no logger.
"""
import json
import os
import re
import socket
import sys
import time


def log_dir() -> str:
    """Where event records go. Must match swe-skill-router.py."""
    override = os.environ.get("SWE_ASSISTANT_LOG_DIR")
    if override:
        return os.path.expanduser(override)
    return os.path.expanduser("~/.claude/swe-assistant")


def log_file() -> str:
    """This machine's event file. Must match the other hook.

    One file per machine, so SWE_ASSISTANT_LOG_DIR can point at a synced folder
    (OneDrive, iCloud) shared by several machines without two of them appending
    to the same file, which sync clients resolve by forking it into conflict
    copies. misfire-report.py reads every events*.jsonl in the directory.
    """
    host = re.sub(r"[^A-Za-z0-9_-]", "_", socket.gethostname().split(".")[0]) or "unknown"
    return os.path.join(log_dir(), f"events-{host}.jsonl")


def log_event(record: dict) -> None:
    """Append one JSON line to the event log. Never raises."""
    try:
        record["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        d = log_dir()
        os.makedirs(d, exist_ok=True)
        with open(log_file(), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if not isinstance(payload, dict):
        return 0

    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        tool_input = {}

    # The Skill tool takes the skill name in `skill`. Recorded verbatim,
    # including any `plugin:skill` namespace prefix — the report splits it.
    skill = tool_input.get("skill")
    if not isinstance(skill, str) or not skill.strip():
        return 0

    record = {
        "event": "invoke",
        "session_id": payload.get("session_id"),
        "skill": skill.strip(),
        # Recorded so a rename of the Skill tool shows up in the data rather
        # than silently emptying the log.
        "tool_name": payload.get("tool_name"),
    }
    # Claude Code includes agent_id only when the hook fires inside a subagent.
    # Subagent invocations share the parent's session_id, so without this they
    # land in the parent's routing window and read as false under-fires
    # (MISFIRE-LOG, 2026-11-08 triage notes). The report excludes them.
    if payload.get("agent_id"):
        record["agent_id"] = payload.get("agent_id")
        record["agent_type"] = payload.get("agent_type")
    log_event(record)
    return 0


if __name__ == "__main__":
    sys.exit(main())
