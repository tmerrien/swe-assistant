---
name: deployment-discipline
description: Use when the user is designing, automating, hardening, or debugging how built and published packages get installed onto the machines that run them. Triggers include "how should we deploy this", "our deploys are manual", "our deploy broke halfway through", "we can't roll back cleanly", "deploy A before B", or "make deploys atomic". Covers automating deploys, making them atomic via install-and-flip, and designing applications to deploy independently — backward and forward compatibility, no ordering dependencies. For the build that produces the package, route to build-and-package. For release repos or release notes, route to release-hygiene. For gradual traffic shifting after deploy, route to progressive-rollout.
---

# deployment-discipline

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 8, "Delivering Software"** — the **Deployment** section. The three moves that structure this skill (automate, atomic, independent) come from the book. The install-side-by-side + symlink-flip pattern for atomicity, the "deploy with changes off, turn on in order later" pattern for handling unavoidable dependencies, and the backward/forward-compatibility posture all come from here.

The named tools (Puppet, Salt, Ansible, Terraform) are the book's examples. In addition, container orchestration (Kubernetes, Nomad, ECS), GitOps controllers (ArgoCD, Flux), and platform PaaS deployment models (Cloud Foundry, Heroku, Vercel/Netlify, Fly.io, Railway) are widely-attested current practice for the same discipline — they implement the same principles the book articulates.

## Pillars this skill strengthens

- **Primary:** Execution, Technical Knowledge
- **Also:** Communication (a deploy plan is a communication artifact for the operators who will run it)
- **Builds:** Leadership (deploy safety is a norm senior engineers set for the team)

## What this skill is for

Deployment is the moment the software actually meets the environment it will run in. Build produced the package; release published it; deployment installs it onto the machines (or clusters, or edge nodes, or user devices) that will run it. Get this wrong and the failure mode is loud and expensive: half-deployed services, mystery-machine-only bugs, deploys that can't be rolled back, and 3am pages that start with *"we tried to push a fix and now nothing works."*

This skill fires when the user is designing how deployments happen, automating a currently-manual process, hardening a deploy that keeps failing partway through, or untangling deploy-order dependencies between services. It does not fire once the software is installed and the question shifts to *how gradually to expose it* — that's rollout territory (feature flags, canaries, blue/green), covered for now in [`operator-playbook`](../operator-playbook/SKILL.md).

## The core mindset (lead with this)

**Every deploy should be automated, atomic, and independent. If it's any of those but not all three, the next deploy is a coin flip.**

- **Automated** — a human clicking buttons is a manual step that will be forgotten, mistyped, or done in the wrong order.
- **Atomic** — the deploy either fully succeeds or the environment is unchanged. There is no half-deployed state.
- **Independent** — no other team's deploy needs to happen first, in the right order, at the right time, for yours to work.

A deploy that violates any of these looks fine on Tuesday and fails on Thursday when the person who knew the trick is on vacation.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual pipeline if shared, skip diagnosis when the first message tells you what's needed.**

### Step 1 — Frame the moment

One or two sentences. Name that the deploy's job is to get the package onto its runtime with zero surprises — and that the three properties above are what "zero surprises" actually means. Skip if the user is already on a specific decision.

### Step 2 — Diagnose (one question, only if needed)

The situation usually falls into one of these shapes:

- **Automating** an existing manual deploy — replacing a runbook with a script/tool.
- **Hardening** — the deploy fails partway through and leaves things broken; needs to be made atomic.
- **Untangling ordering** — service A's deploy requires service B first, or database migrations must precede code, or the team can't ship on their own schedule.
- **Choosing the tool** — Ansible vs. Terraform vs. Kubernetes/ArgoCD vs. platform PaaS, etc.

If the message is ambiguous, ask **one** question — for example: *"What's the situation — automating a manual deploy, dealing with deploys that break partway, or untangling ordering between services?"*

### Step 3 — Automate deployments

Manual steps are the failure vector. **Use scripts (or purpose-built tools) for everything you do to get software from the release repo onto its runtime.**

- **Off-the-shelf tools are almost always the right starting point.** Ansible, Salt, Puppet, and Terraform are the book's examples; Kubernetes + ArgoCD/Flux, Nomad, and platform PaaS (Heroku, Fly.io, Vercel/Netlify, Railway, Cloud Foundry) are equally valid depending on the runtime. Pick one, don't roll your own until you've genuinely outgrown the tools.
- **Automate on both sides of the blockers.** Some steps may genuinely resist automation — a signed compliance review, a physical device attach, a human sign-off. That's okay; wrap script around everything else and shrink the manual boundary to just the step that has to be human.
- **Continuous delivery is the long-term target** for teams whose users can absorb frequent changes: every green commit becomes a candidate deploy, executed automatically. Prerequisites are strong automated testing and observability that surfaces problems fast. It's not a starting point for most teams; it's what mature automation grows into.
- **Idempotency at the deploy layer.** A deploy script re-run on an already-deployed environment should end in the same state, not error out or drift. Route depth on operation-level idempotency to [`idempotency`](../idempotency/SKILL.md).

Ask: *"What's the manual step that always trips you up?"* — start there.

### Step 4 — Make deployments atomic

**All-or-nothing.** A deploy either fully succeeds or the environment stays exactly as it was. Half-deployed is a failure mode you never want to see.

The classic pattern (from the book, still widely used):

1. Install the new version to a **different location** on disk. Don't touch the old one.
2. Do whatever verification you can — the binary starts, health checks pass, schema is valid.
3. **Flip a single symlink** (or shortcut, or config pointer, or load-balancer target) from the old location to the new. This is the atomic step.
4. If anything goes wrong before the flip, tear down the new install; the old version is still serving.
5. Rollback is the same flip in reverse.

See *Callout — Atomic install-and-flip* below for the pattern in more concrete form.

Container-image deploys inherit this property somewhat naturally (the old container keeps running until the new one is healthy, then traffic swaps), but the discipline still applies: don't mutate the running container in place, replace it. Kubernetes rolling updates and platform PaaS deploys implement variants of the same idea.

### Step 5 — Deploy applications independently

**No deploy should require another team's deploy to happen first, in the right order, at the right time.** Ordering dependencies are the number-one cause of deploys that can't ship without a coordination meeting.

Three moves that make independence possible:

- **Backward compatibility.** New code must handle old data, old messages, old callers. If the API changes shape, both shapes work during the transition.
- **Forward compatibility.** Old code must tolerate the new world — new fields it doesn't understand, new message types it ignores, new endpoints it doesn't call. The classic pattern: additive changes only during the transition, deprecation later.
- **Ship dark, turn on later.** When a dependency between changes is genuinely unavoidable, deploy the code with the new behavior *turned off* (feature flag, config, or explicit branch), then turn it on across services in the right order. Turning a flag on is much cheaper than coordinating a deploy order. Depth on feature-flag mechanics belongs in the rollout skill; until it exists, see [`operator-playbook`](../operator-playbook/SKILL.md).

See *Callout — Backward and forward compatibility across a deploy* below.

The failure mode this prevents: two services get out of sync for thirty seconds during a rolling deploy, something crashes, everyone rolls back and holds a retrospective about why the deploy order was documented in a Slack message from six months ago.

### Step 6 — Pick one action, then close

Ask: *"What's the one deploy-discipline move you'll make this week?"* Push for concreteness.

- *"Automate our deploys"* → too vague.
- *"Wrap the current manual deploy in an Ansible playbook by Friday and run it end-to-end against staging"* → the action.
- *"Change the API endpoint so `POST /users` accepts both the old and new payload shape starting next deploy"* → the action.

Close in one or two sentences. Confirm the move. If the next question is "how do I gradually shift traffic onto the new version" (canaries, blue/green, feature flags at the user level), route to [`operator-playbook`](../operator-playbook/SKILL.md); that skill covers rollout at a high level until a dedicated one lands.

---

## Callout — Atomic install-and-flip

The pattern in one page. Adaptable to almost every runtime.

**Setup — on-disk layout:**

```
/opt/myapp/
  releases/
    2024-11-01-abcdef/    ← previous version
    2024-11-08-123456/    ← new version, just installed
  current -> releases/2024-11-08-123456/
```

**Deploy steps:**

1. `mkdir /opt/myapp/releases/<new-version>` and unpack the release package there. The old install is untouched.
2. Run any per-install setup that's local to the new tree — generate configs, create empty log/cache dirs, warm the JIT if applicable.
3. **Verify** — run health checks against the new install without swapping traffic to it. Startup succeeds, the binary responds, config is valid.
4. **Flip:** `ln -sfn /opt/myapp/releases/<new-version> /opt/myapp/current` (atomic on POSIX filesystems), then restart or `reload` the service so it picks up the new `current`.
5. If verification fails before the flip, `rm -rf /opt/myapp/releases/<new-version>`. Old install is still serving; nobody noticed.
6. **Rollback:** `ln -sfn /opt/myapp/releases/<previous-version> /opt/myapp/current` and reload. Whole rollback in one flip.

**Retention:** keep the last N releases on disk so rollback is instant. Cheap on disk, priceless at 2am.

**Variants:**

- **Containers.** New image runs alongside old; orchestrator flips traffic when the new one is healthy. Old container gets torn down after a soak period. Kubernetes `Deployment`, Nomad `service` update strategy, ECS blue/green implement this natively.
- **Serverless / PaaS.** New version deployed as a separate revision; the platform's router flips traffic. Google Cloud Run, AWS Lambda aliases, Heroku slugs, Fly.io machines all work this way.
- **Client-installed software.** New version installed to a version-suffixed directory; a launcher or shortcut points at the current version. Updater flips the pointer atomically.

The unifying principle: **the switch from old to new is a single, cheap, reversible operation.** Anything else, and half your deploys will be partial-failure recoveries.

---

## Callout — Backward and forward compatibility across a deploy

During any non-trivial deploy — rolling update, canary, blue/green — old code and new code run **at the same time.** For minutes, hours, or during a paused rollout, for days.

This means every change to a shared surface has to work in **both directions**:

- **Backward compatible.** New code handles anything old code or old data can send it. New API accepts old request shapes. New service still reads old-shaped messages from the queue. New schema still readable by old workers.
- **Forward compatible.** Old code tolerates anything new code produces. Old API accepts unknown fields without crashing. Old workers ignore new message types. Old readers ignore new schema columns.

Concrete patterns:

- **Additive-only during transition.** Add the new field/endpoint/message-type first; migrate readers/writers to use it; only then remove the old one. Never rename in one step; rename is *add new + migrate + remove old.*
- **Two-phase schema changes.** Migration 1 adds the new column, defaulted or nullable; deploy the code that writes both old and new; backfill; deploy the code that reads only new; migration 2 drops old column.
- **Message-format evolution.** Protobuf, Avro, JSON with `additionalProperties` — pick a format that tolerates unknown fields. Never break wire compatibility in one release.
- **Feature-flag the switchover.** Ship the new code path in place, off by default, turn it on with a flag after every service has the new code deployed. Deploy order and code-behavior order are now decoupled.

Rule of thumb: **any single deploy should be safe to pause halfway through indefinitely.** If pausing at 50% would break things, the change isn't compat-safe yet — split it.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't dump Step 2's diagnostic menu.
- **Work on their actual runtime.** VMs, containers, serverless, PaaS, client-installed software — the pattern is the same but the concrete moves differ. If they share the deploy script, playbook, `Dockerfile`, `Deployment` manifest, or Terraform config, walk through *theirs*.
- **Name real tools.** `ansible-playbook`, `terraform apply`, `argocd sync`, `kubectl rollout`, `helm upgrade`, `fly deploy`, `gh workflow run` — say what they'll type.
- **Don't over-engineer.** A small internal service does not need blue/green plus canary plus dark-launch. It needs an atomic install-and-flip and a script.
- **When they're mid-outage from a bad deploy**, help them roll back and stabilize before proposing structural fixes. Route to [`incident-response`](../incident-response/SKILL.md) if that's the shape.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is designing the build that produces the package. Route to [`build-and-package`](../build-and-package/SKILL.md).
- The user is choosing a package repository or writing release notes/changelogs. Route to [`release-hygiene`](../release-hygiene/SKILL.md).
- The user is asking about gradually shifting user traffic to a new deploy — feature flags at the user level, canaries, blue/green traffic splitting, dark launches / traffic shadowing. Route to [`operator-playbook`](../operator-playbook/SKILL.md); a dedicated rollout skill is planned.
- The user is dealing with an active production incident from a bad deploy. Route to [`incident-response`](../incident-response/SKILL.md); roll back first, tighten the deploy discipline later.
- The user is designing configuration itself (schema, defaults, validation, secret handling). Route to [`configuration`](../configuration/SKILL.md).
- The user is asking about idempotent request handling in application code (webhooks, RPC handlers). Route to [`idempotency`](../idempotency/SKILL.md).

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- ***Continuous Delivery*** — Jez Humble & David Farley (Addison-Wesley, 2010). Foundational text on automated deployment pipelines — the discipline this skill's Step 3 is a distillation of.
- ***Release It!*** — Michael T. Nygard (Pragmatic Bookshelf, 2nd ed. 2018). Stability patterns and capacity thinking for deployed systems; the second edition has extensive material on cloud-native deploy topologies.
- ***Site Reliability Engineering*** — Beyer, Jones, Petoff, Murphy (Google, O'Reilly 2016). Free online at https://sre.google/sre-book/. Ch. 8 (*"Release Engineering"*) is the closest institutional treatment of the discipline; the book's operational chapters cover the deploy → operate handoff.
- ***Amazon Builder's Library*** (https://aws.amazon.com/builders-library). Multiple essays on deployment safety, atomicity, and progressive delivery from AWS principal engineers.
- ***Git for Teams*** — Emma Jane Hogbin Westby (O'Reilly, 2015). Team-level Git workflows that shape what a deploy pipeline is being asked to consume.
