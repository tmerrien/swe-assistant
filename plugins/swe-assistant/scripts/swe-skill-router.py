#!/usr/bin/env python3
"""UserPromptSubmit hook: surface relevant swe-assistant skills.

Matches the submitted prompt against topic patterns and injects a note naming
the skills that apply. Topic-based on purpose, not situation-based: "write a
doc about incident response" should fire just as "prod is down" does, because
guidance written about a practice should be grounded in the skill too.

Tuned to OVER-fire. Per ~/.claude/CLAUDE.md, false positives are the signal
the author wants — they reveal trigger descriptions that need tightening.

Also records what it suggested to the event log, so the routing decision can be
compared later against the skill that actually got invoked. See
`hooks/README.md` and `scripts/misfire-report.py` in the repository.

Exits 0 unconditionally. A router that blocks a prompt is worse than no router.
"""
import json
import os
import re
import sys
import time

# Keys must match directory names in the plugin's skills/ directory
# (../skills/ relative to this file).
PATTERNS = {
    "first-run-experience": r"(README\b|quick.?start|getting.?started|onboarding\s+docs?|setup\s+(guide|doc|instructions)|first.?run\s+experience|time.?to.?first|nobody\s+uses\s+our|new\s+(users?|hires?)\s+(get|keep)\s+(stuck|asking)|same\s+setup\s+question|document\s+(this|our)\s+(service|library|API|package))",

    "interface-decisions": r"\b(UI|UX|user\s+interface|user\s+experience|mock.?up|wireframe|user.?facing|design\s+the\s+(screen|page|flow|form)|onboarding\s+flow|polish(ed)?\s+later)\b",
    "rationing-attention": r"(too\s+much\s+on\s+(this|the)|everything.{0,30}?\b(looks|feels|is|seems)\s+(equally\s+)?important|what\s+(should\s+i|to)\s+(emphasi[sz]|highlight)\w*|visual\s+hierarch\w*|primary\s+action|cluttered|information\s+overload|make\s+\w+\s+stand\s+out)",
    "interface-tradeoffs": r"(minimal(ism|ist)?\s+(vs|versus|or)|too\s+(plain|busy|boring)|which\s+direction\s+(should|do)|break\s+(the\s+)?(\w+\s+){0,3}pattern|deviate\s+from\s+(the\s+)?(design\s+system|pattern|convention)|design\s+system\s+default|less\s+is\s+(more|a\s+bore))",
    "interface-copy": r"(button\s+label|error\s+message|empty\s+state|microcopy|tooltip|placeholder\s+text|confirmation\s+(dialog|message|copy)|helper\s+text|UI\s+(copy|text|string)|what\s+should\s+(it|this|the\s+\w+)\s+say)",
    "design-ethics": r"(dark\s+pattern|deceptive\s+(design|pattern)|pre.?check\w*|opt.?out\s+by\s+default|confirmsham\w*|harder\s+to\s+cancel|roach\s+motel|nag\s+screen|false\s+urgency|(cancel|decline|opt.?out|unsubscribe|no\s+thanks).{0,40}?(grey|gray)(ed)?\s+out|(grey|gray)(ed)?\s+out.{0,40}?(cancel|decline|opt.?out|unsubscribe)|decline\s+button|bury\s+the\s+(cancel|opt.?out|unsubscribe)|manipulat\w*\s+(design|UI|UX|user)|feels\s+(wrong|sketchy|scummy))",

    # --- incidents & operations -------------------------------------------
    # NB: trailing \b after a singular noun blocks the plural — "incidents"
    # does not match \bincident\b. Every noun here takes an explicit s?.
    "incident-response": r"\b(incidents?|outages?|prod(uction)?\s+(is\s+)?down|got\s+paged|on\s+fire|postmortems?|post-mortems?|broke\s+in\s+prod|sev\s?\d)\b",
    "on-call-shift": r"\b(on[-\s]?call|pagers?|paging|support\s+(requests?|rotation)|P[0-4]\b|escalation\s+path)",
    "operator-playbook": r"\b(runbooks?|production\s+readiness|operat(e|ing)\s+(it|this|the\s+system)|keep\s+it\s+running)\b",
    "operational-tools": r"\b(ops\s+tools?|admin\s+(tool|panel|console)s?|internal\s+tools?|back\s?office)\b",
    "metrics": r"\b(metrics?|SLIs?|SLOs?|SLAs?|dashboards?|instrument(ation|ing|ed)?|observab|vanity\s+metric|what\s+(should|do)\s+(we|i)\s+(measure|track))\b",
    "tracing": r"\b(traces?|tracing|spans?|distributed\s+trac|correlation\s+ids?)\b",
    "logging": r"\b(log(ging|s)?)\b.{0,40}\b(level|structur|redact|aggregat|verbose|what\s+to\s+log)|\bstructured\s+log",

    # --- writing & reviewing code -----------------------------------------
    "code-review": r"\b(code\s+review|review(ing)?\s+(a|this|my|the)\s+(PR|pull\s+request|code|diff)|PR\s+feedback|rubber.?stamp|approve\s+the\s+PR)\b",
    "commit-and-pr-hygiene": r"\b(commit\s+message|squash|rebase|PR\s+(description|template)|branch(ing)?\s+strateg|conventional\s+commit)\b",
    "changing-legacy-code": r"\b(legacy|refactor\s+safely|scared\s+to\s+(change|touch)|no\s+tests?\s+(for|on)|inherited\s+(this\s+)?code|seams?\b)",
    "defensive-programming": r"\b(defensive|harden(ing)?|more\s+robust|null\s+(check|safety)|what\s+can\s+go\s+wrong|fail\s+safe|error\s+handling)\b",
    "input-validation": r"\b(validat(e|ion|ing)|sanitiz|injections?|XSS|CSRF|OWASP|untrusted|user\s+input|escap(e|ing)|trust\s+boundary)\b",
    "idempotency": r"\b(idempoten|exactly.?once|de-?dup|double.?(charge|submit)|replay|webhook\s+twice|retry\s+safe)\b",
    "retry-and-backoff": r"\b(retry|retries|retrying|backoff|jitter|exponential\s+back)\b",
    "configuration": r"\b(config(uration|s)?\b|env(ironment)?\s+var|dotenv|\.env\b|12.?factor|feature\s+config|settings\s+file)",

    # --- testing -----------------------------------------------------------
    "writing-tests": r"\b(writ(e|ing)\s+tests?|test\s+(coverage|strategy|suite|pyramid)|unit\s+test|integration\s+test|e2e\s+test|TDD)\b",
    "test-determinism": r"\b(flaky|flakiness|intermittent(ly)?\s+fail|non.?deterministic|passes\s+locally|test\s+is\s+unreliable)\b",
    "mocking": r"\b(mock(ing|s)?\b(?!-?ups?\b)|stub(bing|s)?\b|test\s+doubles?|fixtures?|fake\s+(the|a)\s)",

    # --- build, release, deploy -------------------------------------------
    "build-and-package": r"\b(build\s+(pipeline|system|step)|packag(e|ing)\b|artifacts?|reproducible\s+build|monorepo\s+build)\b",
    "dependency-management": r"\b(dependenc(y|ies)|semver|semantic\s+version|version\s+conflict|lockfiles?|transitive|vendoring|upgrade\s+the\s+(lib|package))\b",
    "deployment-discipline": r"\b(deploy(ment|ing|s)?\b|roll\s?back|atomic\s+(deploy|release)|ship\s+to\s+prod|release\s+process)",
    "release-hygiene": r"\b(release\s+notes|changelogs?|cut\s+a\s+release|version(ing)?\s+scheme|tag\s+a\s+release)\b",
    "progressive-rollout": r"\b(canar(y|ies)|feature\s+flags?|gradual\s+roll|staged\s+roll|blue.?green|dark\s+launch|percentage\s+roll)\b",

    # --- decisions & judgement --------------------------------------------
    "design-doc": r"\b(design\s+doc(ument)?s?|RFC\b|ADR\b|architecture\s+decision|tech(nical)?\s+spec|one.?pager|write\s+up\s+the\s+design)\b",
    "technical-design-process": r"\b(define\s+the\s+problem|problem\s+statement|where\s+do\s+i\s+(even\s+)?start|scope\s+(this|the\s+project)|prototyp(e|ing)|spike\b|maker.?s\s+schedule|deep\s+work|design\s+process|prior\s+art|throwaway\s+code)\b",
    "managing-complexity": r"\b(over.?engineer\w*|premature\s+optimi[sz]\w*|YAGNI|too\s+coupled|tightly\s+coupled|change\s+amplification|add\s+an?\s+abstraction|extensible|least\s+astonishment|domain.?driven|bounded\s+context|high\s+cohesion|too\s+complex|touched\s+\w+\s+files)\b",
    "evolvable-apis": r"\b(breaking\s+change|backward\w*.?compat\w*|forward\w*.?compat\w*|version\s+(the\s+)?API|API\s+version|deprecat\w*|OpenAPI|protobuf|protocol\s+buffers?|gRPC|thrift\b|break\s+(our|the|my)\s+clients?)\b",
    "evolvable-data": r"\b(schema\s+(change|migration|evolution)|migrat(e|ing|ion)\s+(the\s+)?(database|schema|data)|backfill|add\s+a\s+column|drop\s+a\s+column|rename\s+a\s+column|schema.?less|shared\s+database|gh-?ost|pt-online|flyway|liquibase|change\s+data\s+capture|expand\s+and\s+contract)\b",
    "choose-boring-technology": r"\b(should\s+(we|i)\s+(use|adopt|switch)|evaluat(e|ing)\s+\w+|innovation\s+tokens?|boring\s+techno|new\s+(framework|language|database|stack)|pick\s+a\s+(library|framework|database))\b",
    "change-discipline": r"\b(rewrite|re-?write|fork\s+the|bypass\s+the\s+(linter|standard|rule)|replace\s+\w+\s+with|migrate\s+(us|off|from))\b",
    "technical-debt": r"\b(tech(nical)?\s+debt|cruft|shortcuts?|clean\s?up\s+later|pay\s+(it|this)\s+down|quick\s+and\s+dirty)\b",
    "software-entropy": r"\b(entropy|code\s+rot|degrad(ing|ed|ation)|hard\s+to\s+maintain|getting\s+messy|broken\s+windows?)\b",
    "stress-test-understanding": r"\b(do\s+i\s+(really\s+)?understand|check\s+my\s+understanding|poke\s+holes|am\s+i\s+missing|sanity.?check\s+(my|this))\b",

    # --- planning & team process ------------------------------------------
    "agile-planning": r"\b(story\s+points?|user\s+stor(y|ies)|sprint\s+(planning|capacity)|backlog\s+(groom|triage|refine)\w*|acceptance\s+criteria|scrum\b|kanban|scrumban|estimat\w*\s+(this|the\s+(work|story|ticket))|planning\s+poker|roadmaps?|velocity|overcommit\w*|spike\s+stor|sprints?\s+\w*\s*(never|didn.?t|don.?t|keep)\w*\s*(finish|complete|end)\w*|sprints?\b.{0,40}?\b(slip|over(run|ran)|spill|carr(y|ied|ying)\s+over)\w*|(slip|over(run|ran)|spill|carr(y|ied|ying)\s+over)\w*.{0,40}?\bsprints?)\b",
    "team-rituals": r"\b(stand.?ups?|daily\s+scrum|retros?\b|retrospectives?|sprint\s+reviews?|demo\s+(day|meeting)|parking\s+lot|scrum\s+of\s+scrums)\b",

    # --- joining, growing, working with people ----------------------------
    "new-team-onboarding": r"\b(join(ing)?\s+(a|the|this)?\s*(new\s+)?(team|company|job)|new\s+(job|team|role|company)|first\s+(week|day|month)|onboard(ing)?|starting\s+at)\b",
    "ramp-up-playbook": r"\b(ramp(ing)?[-\s]?up|get(ting)?\s+up\s+to\s+speed|unfamiliar\s+codebase|new\s+codebase|first\s+90\s+days)\b",
    "contributor-playbook": r"\b(own(ing)?\s+(a|my|this)\s+feature|scope\s+(a|this|the)\s+work|OKRs?|quarterly\s+goal|end.to.end\s+feature)\b",
    "owner-playbook": r"\b(tech(nical)?\s+lead|owning\s+(the|a)\s+system|mentor(ing|ship)?|lead\s+the\s+(project|team))\b",
    "working-with-managers": r"\b(1:1s?|one.on.ones?|my\s+manager|PPPs?\b|progress[,\s]+plans[,\s]+problems|status\s+updates?|OKRs?\b|key\s+results?|self.?review|performance\s+reviews?|managing\s+up|feedback\s+(to|for)\s+my\s+manager|SBI\b)\b",
    "growth-self-check": r"\b(1:1|one.on.one|performance\s+review|promotions?|next\s+level|am\s+i\s+(growing|improving)|career\s+(growth|development))\b",
    "growth-obstacles": r"\b(imposter|impostor|feel\s+like\s+a\s+fraud|not\s+(good\s+)?(ready|enough)|out\s+of\s+my\s+depth|found\s+out|everyone\s+else\s+knows)\b",
    "learning-toolkit": r"\b(how\s+(do|should)\s+i\s+learn|get(ting)?\s+good\s+at|learn(ing)?\s+(a\s+)?(new\s+)?(language|framework|codebase)|side\s+project)\b",
    "asking-for-help": r"\b(ask(ing)?\s+for\s+help|stuck\s+(for|on)|don'?t\s+want\s+to\s+(bother|interrupt)|should\s+i\s+ask|been\s+stuck)\b",
}

MAX_NAMED = 5

# How many recent human turns to consider when the current prompt is a bare
# continuation ("do doc 3", "yes", "carry on"). Measured need: on a real
# working session, 0 of 17 prompts carried a topic keyword — the topic lived
# in the conversation, not the prompt. Prompt-only matching is close to
# useless mid-session, which is exactly when it is needed most.
# Kept deliberately small. At 12 turns a long engineering conversation matched
# 36 of the 37 skills that existed when this was measured — exactly as useless
# as matching none, and worse now that there are more. Context hits are ranked
# newest-turn-first and capped hard (MAX_CONTEXT).
CONTEXT_TURNS = 4
MAX_CONTEXT = 2

# User-role transcript entries that were not typed by the human: skill
# payloads, tool results, system reminders, slash-command plumbing. Matching
# these would make the router fire on its own output.
NOT_HUMAN = re.compile(
    r"Base directory for this skill|<system-reminder>|<command-name>|"
    r"<local-command-stdout>|ARGUMENTS:|tool_use_id|Result of calling|"
    # Background-task notifications arrive through the same channel as prompts
    # and are dense with engineering vocabulary — they fired the router on
    # every subagent completion until this line existed.
    r"<task-notification>|\[SYSTEM NOTIFICATION|automated background-task event",
    re.I,
)


def log_dir() -> str:
    """Where event records go. Outside the repo — this is the user's data."""
    override = os.environ.get("SWE_ASSISTANT_LOG_DIR")
    if override:
        return os.path.expanduser(override)
    return os.path.expanduser("~/.claude/swe-assistant")


def log_event(record: dict) -> None:
    """Append one JSON line to the event log. Never raises.

    A logging failure must not cost the user their prompt, so every error here
    is swallowed. The cost of silence is a gap in the log; the cost of raising
    is a broken session.
    """
    try:
        record["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        d = log_dir()
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "events.jsonl"), "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except Exception:
        pass


def find_matches(text: str) -> list:
    try:
        return [n for n, p in PATTERNS.items() if re.search(p, text, re.I)]
    except re.error:
        return []


def recent_human_text(payload: dict) -> list:
    """Best-effort read of recent human turns, newest first. Failure -> []."""
    path = payload.get("transcript_path")
    if not path:
        sid = payload.get("session_id")
        if not sid:
            return []
        import glob
        hits = glob.glob(os.path.expanduser(f"~/.claude/projects/*/{sid}.jsonl"))
        if not hits:
            return []
        path = hits[0]
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()[-400:]
    except OSError:
        return []

    texts = []
    for line in reversed(lines):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") != "user":
            continue
        content = (d.get("message") or {}).get("content")
        parts = []
        if isinstance(content, str):
            parts = [content]
        elif isinstance(content, list):
            parts = [b.get("text", "") for b in content
                     if isinstance(b, dict) and b.get("type") == "text"]
        for t in parts:
            if t and not NOT_HUMAN.search(t):
                texts.append(t)
        if len(texts) >= CONTEXT_TURNS:
            break
    return texts  # newest first


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    if not isinstance(payload, dict):
        return 0

    prompt = payload.get("prompt") or ""
    if not prompt.strip():
        return 0

    # Background-task notifications and other machine-generated turns arrive in
    # the same `prompt` field a human types into. Routing on them fires the
    # skill nag on every subagent completion, which is pure noise.
    if NOT_HUMAN.search(prompt):
        return 0

    hits = find_matches(prompt)
    source = "This prompt matches"
    matched_from = "prompt"

    # Continuation prompts ("do doc 3", "yes") carry no topic. Fall back to the
    # recent conversation, ranked newest-turn-first so the live thread wins over
    # something mentioned four turns ago, and capped tight.
    if not hits:
        seen = []
        for turn in recent_human_text(payload):  # newest first
            for name in find_matches(turn):
                if name not in seen:
                    seen.append(name)
            if len(seen) >= MAX_CONTEXT:
                break
        hits = seen[:MAX_CONTEXT]
        source = "The recent conversation is about"
        matched_from = "context"

    # Log every routed prompt, INCLUDING the no-match case. A prompt the router
    # said nothing about is exactly the under-fire evidence that was previously
    # invisible: if a skill gets invoked after one of these, the router missed it.
    record = {
        "event": "route",
        "session_id": payload.get("session_id"),
        "suggested": hits,
        "matched_from": matched_from if hits else "none",
        "prompt_chars": len(prompt),
    }
    # Prompt text is the user's own words. Off by default so an installed plugin
    # never writes them to disk uninvited; the maintainer opts in on their own
    # machine, where diagnosing a bad pattern needs the actual sentence.
    if os.environ.get("SWE_ASSISTANT_LOG_PROMPTS") not in (None, "", "0"):
        record["prompt"] = prompt
    log_event(record)

    if not hits:
        return 0

    named = hits[:MAX_NAMED]
    listed = ", ".join(f"swe-assistant:{h}" for h in named)
    extra = f" (+{len(hits) - MAX_NAMED} more)" if len(hits) > MAX_NAMED else ""

    context = (
        f"[swe-skill-router] {source}: {listed}{extra}.\n"
        "Invoke the relevant one(s) with the Skill tool BEFORE answering — including "
        "when you are writing documentation or guidance ABOUT the practice rather than "
        "doing it, since that guidance should be grounded in the skill rather than "
        "improvised. Skip only if you already loaded it this session, it plainly does "
        "not fit, or this is an active incident; if you skip, say so in one clause and why."
    )

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        },
        "suppressOutput": True,
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
