---
name: configuration
description: Use when the user is designing, adding, or modifying application or service configuration — choosing a format, setting defaults, validating at startup, grouping related settings, or weighing dynamic against static config. Triggers include "how should I configure this", "YAML or env vars", "where should these settings live", "config validation", "should this be config or hardcoded", or "I'm hand-editing config in production". Covers boring-is-better, logging and validating all config at startup, sensible defaults, treating config as code, and not editing deployed config. Do not trigger for build configuration, feature-flag tooling, or code reviews.
---

# configuration

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Configuration). The 12-Factor App's Config principle (https://12factor.net/config) is referenced as the canonical practitioner anchor for the env-var-centric view.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (configuration is a contract between developers and operators)
- **Builds:** Leadership (boring, well-validated config raises the team's operational bar)

## What this skill is for

Configuration is the seam between code and operations — what an engineer can change about a running service *without re-deploying*. Good configuration saves more incidents than features add. Bad configuration takes services down silently because nobody noticed the env var was wrong, or fast and loudly because the wrong YAML format crashed at startup.

This skill fires when the user is designing config for a new service, adding settings to an existing one, choosing a format, or trying to decide whether something should be configurable at all.

## The core mindset (lead with this)

**Configuration should be boring. Use the simplest possible approach that will work; don't get creative.**

- A static configuration file in a single standard format is almost always the right answer.
- Dynamic configuration (changeable while the application is running, without restart) introduces real complexity. Most of the time it isn't worth it. The clearest exceptions: log verbosity, feature flags for *operational* features (kill switches), and rate-limit thresholds.
- Boring config is debuggable config. Clever config systems become the source of incidents you didn't expect.
- **If something needs to change between environments, it's configuration. If it only changes between releases, it's probably code.**

---

## The format options

Five common shapes, with rough use-cases.

### Plain-text config files (INI, JSON, YAML, TOML)

- **When:** the primary mechanism for any non-trivial service. Human-readable, version-controllable, reviewable.
- **YAML** allows nesting (good for grouping related config) but has notorious type-coercion quirks (`yes` becomes `true`, leading zeros become octal). Use a schema validator.
- **JSON** is unambiguous and machine-friendly but unfriendly to write (no comments, no trailing commas in most parsers).
- **TOML** is increasingly popular for application config — explicit types, comments, less footgun than YAML.
- **INI** is fine for flat, small configs. Limited nesting support.

### Environment variables

- **When:** values that are environment-specific (dev/staging/prod), values you don't want in version control (secrets, but use a secret manager for serious cases), values you want to inject without modifying the deployed artifact.
- The **12-Factor App** view: store *all* config in the environment. Many modern frameworks default to this pattern (Kubernetes, Docker, Heroku, most cloud platforms).
- Limitations: flat namespace (use `MYAPP_SECTION_KEY` convention to fake nesting), values are always strings (parse and validate), no comments or grouping at the env layer.

### Command-line flags

- **When:** values the operator chooses at invocation. Most useful for CLIs and short-lived processes; less common for long-running services.
- Combine well with config files: flag overrides file, file overrides env vars, env vars override defaults (or any other consistent precedence rule).

### Custom DSL

- **When:** the configuration genuinely needs programmable logic — conditionals, loops, dynamic generation. Sometimes the right answer for routing rules, complex policies, or sophisticated alerting rules.
- **Cost:** harder to parse with standard tools, harder for operators unfamiliar with the DSL, harder to validate, harder to integrate with other systems. Interoperability is the main cost.
- **Most teams who reach for a DSL underestimate this cost.** If the alternative is data with a small amount of declarative structure, prefer the data.

### The language the app is written in

- **When:** internal-only services where the operator is always a developer; rapid prototypes.
- **Cost:** changes require redeploying; non-developers can't operate the service; config becomes inseparable from code review of behavior changes.
- **Most production services should not use this approach.**

---

## The seven practices

### 1. Don't get creative

Configuration should be the simplest thing that works. A static file in a standard format, loaded once at startup, is the default. Reach for anything more complex only when there's a concrete reason.

Resist:

- Custom config DSLs when YAML/TOML would do.
- Multi-source config layering with elaborate precedence rules when one file would do.
- Dynamic reload-on-change when restart-on-config-change would do.
- Distributed config stores (Consul, Etcd, ZooKeeper) for small services when a file would do.

Each of these has a use case. Most services don't have it.

### 2. Log and validate all config at startup

- **Log every non-secret config value** as the application starts. The operator should be able to read the startup log and confirm the application is seeing the values they expect.
- **Never log secrets** — see [`logging`](../logging/SKILL.md) for the redaction discipline. Log secret values as `[REDACTED]` so the operator knows it was set but not what it was.
- **Validate every value when loaded.** Check types, value bounds, valid enum values, string length, URL format, port range (1024+ for non-root), required-field presence.
- **Fail fast on invalid config.** Refuse to start rather than starting and failing later with a confusing error. A clean startup-time validation message ("config error: SERVER_PORT must be between 1024 and 65535, got 80") is much better than mid-runtime confusion.

### 3. Provide sensible defaults

The application should work out of the box for the most common use case. Operators should only have to configure what's actually different about their environment.

- **Network ports above 1024** (avoid requiring root).
- **Use the system's temp directory** if a path isn't specified.
- **Use the user's home directory** for user-specific data when reasonable.
- **Sensible timeouts** — not zero (= forever), not absurdly low.

A configuration with no required values is the friendliest possible interface for a new user; if every parameter requires a decision, the application is hostile.

### 4. Group related configuration

Use a format that allows nesting (YAML, TOML, JSON). Bundle tightly-coupled parameters together so the relationship is visible and so the operator changes them as a set:

```yaml
database:
  host: db.internal
  port: 5432
  pool_size: 20
  pool_timeout_seconds: 30
  ssl: true
```

Better than:

```yaml
db_host: db.internal
db_port: 5432
db_pool_size: 20
db_pool_timeout_seconds: 30
db_ssl: true
```

The first reads as a unit. The second reads as five unrelated keys that happen to share a prefix.

### 5. Treat configuration as code (CaC)

The same rigor applied to source code should apply to configuration files.

- **Version control** — config lives in Git (or your team's VCS), tracked alongside or near the code.
- **Code review** — config changes go through the same review process as code changes. A bad config push has the same blast radius as a bad code push.
- **Validation in CI** — schema-check config files automatically. Catch missing required keys, wrong types, broken YAML before deploy.
- **Build and publish** — config gets packaged and deployed through the same pipeline as code. No hand-copying files into production.
- **Track changes** — every config change has an author, a reason (commit message), and a rollback path. Same as code.

This discipline is the difference between *"who changed the config and why?"* being a quick Git query versus a six-hour investigation.

### 6. Keep configuration files clean

- **Standard formatting and spacing.** If your team has a YAML/TOML formatter, use it.
- **Don't blindly copy from other files.** Inherited config carries inherited assumptions and dead settings. Copy intentionally; remove what doesn't apply.
- **Comments where the value isn't obvious.** A `timeout_seconds: 30` is fine; a `timeout_seconds: 47` deserves a comment explaining why 47 specifically.
- **Group related sections, separate unrelated ones with blank lines** for readability.
- **Delete dead config.** Settings that no code reads anymore are confusing and dangerous. Audit periodically.

### 7. Don't edit deployed config by hand

- **Avoid hand-editing config on a running machine.** It bypasses every guardrail above (review, validation, version control, rollback).
- **If you must during an active incident** (a real emergency), document what you changed and **commit the change to the source of truth as soon as the fire is out.** The undocumented hand-edit is one of the most common causes of *"why is this server behaving differently from the others?"* and *"why did this come back after the next deploy?"*
- For incidents specifically, see [`incident-response`](../incident-response/SKILL.md) — emergency hand-edits are valid mitigation, but the postmortem must include the config-sync action item.

---

## Callout — The 12-Factor App view on configuration

The **12-Factor App** (https://12factor.net) is a widely-adopted methodology for building modern cloud-native services. Its **Factor III: Config** says:

> *"An app's config is everything that is likely to vary between deploys (staging, production, developer environments, etc.). … Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires strict separation of config from code. … The twelve-factor app stores config in environment variables."*

The methodology is opinionated toward env vars as the primary mechanism, on the argument that they're language-agnostic, OS-managed, hard to accidentally commit, and easy to inject differently per environment. Most cloud-native services and platforms (Kubernetes, Heroku, Docker, AWS ECS) assume and support this pattern.

This view is not the only valid one — file-based config is fine, especially for self-hosted services and when grouping matters. But the 12-Factor methodology is the most widely-cited reference, and any team designing config from scratch should know its argument before choosing a different path.

---

## Callout — Configuration vs feature flags

These are often confused. The distinction:

- **Configuration** = operational settings. *"What database does this service talk to? What port does it listen on? How long are timeouts? What's the log level?"* Lives in config files / env vars; changes between environments and deploys; managed by ops.
- **Feature flags** = which application behaviors are enabled at runtime. *"Show new checkout UI to 10% of users. Enable beta payment provider for these customers. Kill-switch this experimental code path."* Lives in a feature flag service (LaunchDarkly, Unleash, Statsig, in-house) or a database; changes constantly; managed by product and engineering jointly.

Both can be "dynamic" (changeable without redeploy), but they're managed differently and serve different needs.

**The risk in conflating them:** putting feature flags in your YAML config means every flag change is a deploy. Putting operational settings in a feature-flag service couples your runtime behavior to a third-party service. Pick the right tool for each.

The `configuration` skill is about operational config. For product feature-flagging, the patterns are different and largely beyond this skill's scope.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Diagnose

If the user shared a config file or named a specific decision, work on that. Otherwise ask **one** question:

- *"What are you configuring, and how is it set today (file? env vars? hardcoded?)?"*

### Step 2 — Identify the actual question

Most configuration questions fall into one of these:

- **Format choice** (YAML vs env vars vs flags) → format-options section.
- **Should this be configurable at all?** → "boring is better" mindset; "if it varies between environments, it's config."
- **How do I validate this?** → practice 2 (log + validate at startup).
- **How do I handle defaults?** → practice 3.
- **How do I organize many settings?** → practice 4 (group).
- **Workflow for changing config in production safely** → practices 5 and 7.
- **Config vs feature flags** → the disambiguation callout.

### Step 3 — Surface only the relevant practice

Don't dump all seven. Pick the one or two that fit the user's question.

### Step 4 — One concrete change

Ask for a specific commitment: change this format, add this validation, rename this key, set this default, etc.

### Step 5 — Close

One sentence. If they're new to the 12-Factor framing, mention it briefly.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about format, defaults, and validation in one message.
- **Default to recommending the boring option.** Engineers reaching for a custom DSL or distributed config store almost always benefit from being asked *"would a file work?"*
- **Push hard on validation-at-startup.** Many production issues trace back to invalid config that loaded silently and failed later. The skill should make this practice non-negotiable.
- **Match the user's stack.** YAML conventions in Python differ from YAML conventions in Go; env-var conventions in Kubernetes differ from env-var conventions in bare-metal systemd. Tailor to context.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is asking about **build configuration** (Webpack, Vite, Maven, Gradle, package.json scripts) — that's build tooling, not application config. Skip.
- The user is asking about **product feature flags** (A/B testing, gradual rollout to user cohorts) — the patterns are different; see the disambiguation callout but don't run this skill's protocol.
- The user is reviewing a PR with config changes — route to [`code-review`](../code-review/SKILL.md).
- The user is in an active incident — route to [`incident-response`](../incident-response/SKILL.md). The "don't edit deployed config" practice has an explicit exception for active mitigation.

## Further reading

Surfaced as a primary reference but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md).

- **The 12-Factor App** (https://12factor.net) — the canonical practitioner methodology for cloud-native services. Factor III (Config) specifically addresses configuration; the other 11 factors are also worth reading.
