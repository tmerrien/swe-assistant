---
name: progressive-rollout
description: Use when the user has deployed new code and now must decide how to expose it — gradually, safely, and with a way back. Triggers include phrases like "how should we roll this out", "canary vs blue/green", "how much traffic for the canary", "feature flag vs canary", "feature toggle", "our feature flags are out of control", "flag cleanup", "circuit breaker", "dark launch", "traffic shadowing", "how do I know the rollout is safe", "what should we monitor during rollout", "A/B test with a flag", or "we ramped to 100% too fast". Walks through the rollout phase from The Missing Readme (Ch. 8) — monitoring against pre-declared expectations, ramping with feature flags, protecting code with circuit breakers, parallel version ramps (canary, blue/green), and dark-mode / traffic-shadowing launches. Also covers flag hygiene. For build, publish, or deploy machinery upstream, route to build-and-package / release-hygiene / deployment-discipline. For an active incident, route to incident-response.
---

# progressive-rollout

## Source

*The Missing Readme* (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 8, "Delivering Software"** — the **Rollout** section. The five moves that structure this skill — monitor against pre-declared expectations, ramp with feature flags, protect with circuit breakers, parallel version ramps (canary / blue-green), and dark-mode launches — come from the book. The "hold the champagne" phrasing, the caution against A/B testing with plain feature flags, and the specific naming of Istio/Gloo/Diffy for traffic shadowing are also from the book.

The framing of SLIs (service level indicators) as the health metrics to watch is widely-attested industry practice, canonically documented in *Site Reliability Engineering* (Beyer et al., Google/O'Reilly 2016; free online at https://sre.google/sre-book/), which is surfaced in this repository's [`READING-LIST.md`](../../../../READING-LIST.md).

Two related skills already exist and are cross-linked below rather than duplicated: [`operator-playbook`](../operator-playbook/SKILL.md) gives the higher-level Operator-stage framing (this skill provides the rollout depth it points to), and [`metrics`](../metrics/SKILL.md) / [`logging`](../logging/SKILL.md) / [`tracing`](../tracing/SKILL.md) cover the observability instruments that make rollouts monitorable in the first place.

## Pillars this skill strengthens

- **Primary:** Execution, Technical Knowledge
- **Also:** Communication (a rollout plan is what you tell the team, ops, and support so they know what to watch)
- **Builds:** Leadership (rollout discipline is a team norm senior engineers set)

## What this skill is for

Deployment installed the new code onto the machines. Rollout is where you decide **who actually gets it**, **how quickly**, and **how you'll know it's working before you commit to it fully**. Skip the rollout discipline and every deploy is a coin flip against every user at once; do it well and most bad changes are caught by a small blast radius before anyone big notices.

This skill fires when the user is planning how to expose a new change, choosing between rollout strategies, cleaning up an out-of-control feature-flag jungle, or trying to figure out what "the rollout looks healthy" would even mean. It does not fire before the code is deployed (that's [`deployment-discipline`](../deployment-discipline/SKILL.md)) or once an incident is already in progress (that's [`incident-response`](../incident-response/SKILL.md)).

## The core mindset (lead with this)

**Hold the champagne until the metrics say so.**

- A rollout that isn't monitored isn't a rollout; it's a coin flip with extra steps.
- Decide *before* the flip what "healthy" looks like — which SLIs, which error signature, which log line. If you're inventing the criterion after traffic is on it, you're rationalizing, not verifying.
- Start narrow. A 1% blast radius that reveals a bug is a good day; a 100% blast radius that reveals the same bug is a postmortem.
- **Sophistication is a cost, not a feature.** Blue/green plus canary plus dark-launch is overkill for most changes. Keep the fancy tools in the toolbox for the changes that need them.

---

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the user's actual rollout if they share one, skip diagnosis when the first message already tells you what they need.**

### Step 1 — Frame the moment

One or two sentences. Name that the deploy is done and the rollout is about controlling *who sees it and when*, with a way to see whether it's working. Skip if the user already has a specific decision on the table.

### Step 2 — Diagnose (one question, only if needed)

The situation usually falls into one of these shapes:

- **Planning a specific rollout** — a new feature or service change goes live next week and they're picking the strategy.
- **Choosing between strategies** — canary vs. blue/green vs. dark launch, or "do we even need this?"
- **Feature-flag hygiene** — the codebase has hundreds of stale flags and nobody knows which are safe to remove.
- **Monitoring the rollout itself** — what do we watch, how do we automate the "roll back if X" trigger, what does "healthy" mean?

If the message is ambiguous, ask **one** question — for example: *"What's the situation — planning a specific rollout, choosing between strategies, or cleaning up flag debt?"*

### Step 3 — Declare what "healthy" means, then monitor for it

Before any traffic hits the new code, the rollout plan must include **the specific signals that will say it's working (or not)**.

- **Pre-declare the SLIs.** Which metrics matter for *this* rollout? Latency (which percentile?), error rate (which endpoints?), throughput, resource use, business signals (signups completing, payments succeeding). If you have to invent these mid-rollout, the rollout is already in trouble.
- **Say what you expect to see.** *"After enabling the new pricing path for 5% of traffic, I expect `pricing_lookup_latency_p99` to stay under 200ms and the `pricing_error_total` counter to grow at less than 0.1% of `pricing_request_total`."* If reality diverges, that's the automatic signal to pause or roll back.
- **Watch logs and traces too**, not just metrics. The new code path should be visible — with a distinguishing marker, feature-flag tag, or version label — so you can pull just its logs and traces.
- **Automate the rollback trigger when the change is big enough.** For smaller changes, humans-watching-dashboards is enough. For anything with a wide blast radius, wire the SLI thresholds to the rollout tooling so it pauses or reverses on its own.
- **Hold the champagne.** Don't call the rollout done until the signals confirm what you expected. "Nothing paged" is not the same as "it works."

Depth on picking what to measure belongs in [`metrics`](../metrics/SKILL.md); the log-hygiene side lives in [`logging`](../logging/SKILL.md).

### Step 4 — Ramp with feature flags

**Feature flags decouple deploy from release.** The code is out there; only the flag decides whether it runs.

- **Shapes.** On/off booleans, allow-lists (specific users/tenants), percentage ramps (0% → 1% → 10% → 50% → 100%), function-based (arbitrary logic per request). Pick the simplest shape that fits.
- **The killer app** is the ability to disable a feature without redeploying. First time you have to flip a flag at 2am you never ship a risky change without one again.
- **Flagged code that mutates state needs extra care.** State written under the new code path doesn't magically disappear when you turn the flag off. If the flag flips to off, old code sees rows the new code wrote — those rows must still be readable. See *Callout — Feature flag hygiene* below and the compatibility guidance in [`deployment-discipline`](../deployment-discipline/SKILL.md).
- **Databases are not usually behind flags.** New and old code hit the same tables. Schema changes must be forward and backward compatible across the ramp; two-phase migrations (add column → dual-write → backfill → dual-read → cut over → drop column) are the standard pattern.
- **A/B testing is not the same as flagging.** A percentage ramp on a plain flag does *not* give you statistically meaningful buckets. If the goal is to measure impact, use a flagging system that assigns users to consistent test buckets (e.g., LaunchDarkly experiments, Statsig, split.io, Unleash variants), and involve a data scientist before drawing conclusions.

### Step 5 — Protect code with circuit breakers

**A circuit breaker is a feature flag controlled by the system, not by a human.**

- **Trigger:** an operational signal — error-rate spike, latency spike, exception burst, log-volume anomaly, downstream saturation.
- **Behavior:** binary, automated, and (usually) permanent until a human resets it. When the breaker trips, the risky path stops being called and the code falls back to a safe alternative (return cached data, return a default, refuse cleanly, or shed load).
- **Use it for irrecoverable side effects.** Sending email, transferring money, publishing to external partners, sending SMS — anything that can't be undone by re-running the request. A breaker on those paths turns a bad rollout into "we didn't send the double-charge" instead of "we sent 40,000 duplicate payments."
- **Databases can protect themselves.** Flip to read-only when disk corruption is detected, when a replica lag threshold is exceeded, when the pool is exhausted. The database's own breaker is often the last honest line of defense.

Libraries: Netflix Hystrix (deprecated but conceptually canonical), Resilience4j, Polly (.NET), envoy/istio circuit-breaker filters, cloud-native mesh implementations. Pick what your platform supports natively.

### Step 6 — Ramp service versions in parallel

For services that carry real traffic, deploy the new version **alongside** the old one and shift traffic gradually. A switch at the entry point (load balancer, service mesh, API gateway, reverse proxy) decides which version each request hits.

**Canary deployments** — the new version runs on a small slice of instances (or a small percentage of traffic). Malfunction impacts a small fraction of users, and any of them can be routed back to the stable version the moment errors show up. Good for high-traffic services where a broken change would page everyone at once. See *Callout — Canary vs. blue/green vs. dark* below.

**Blue/green deployments** — two full environments run in parallel: one active (blue), one passive (green). When green is verified healthy against real or synthetic traffic, flip the router. If issues appear, flip back. In cloud environments, the passive side is torn down once the new version has soaked. Good when traffic can't be cleanly subset, when the change touches many services at once, or when the ability to flip back near-instantly matters more than a gradual ramp.

Both approaches share the same failure modes as feature-flag ramps: **shared state (databases, queues, caches) has both old and new code hitting it at once.** Backward and forward compatibility must hold across the entire ramp window. Any time you can't guarantee both, don't ramp — ship dark, feature-flag on, and cut over deliberately.

### Step 7 — Launch in dark mode (traffic shadowing)

**Dark mode = real production traffic hits the new code path, but users never see its responses.**

- The pattern: a proxy sits between users and the app; every real request is also **duplicated** to the new code path. Responses from both are compared and any differences are logged. Only the old path's response is returned to the user.
- **Best use case:** complex migrations. New serialization format, new pricing engine, new fraud model, new storage backend. You get real production traffic hitting the new path with zero user-facing risk.
- **Watch the side effects.** Anything with a real-world consequence (billing, emails, external API calls, database writes) must be suppressed or routed to a sandbox on the shadowed path — otherwise you double-bill, double-email, double-write.
- **Exclude shadow traffic from user analytics.** Mark shadow requests with a header (or the service mesh convention for it) so downstream systems can filter them out.
- **Tooling.** Service meshes (Istio, Linkerd) and API gateways (Gloo, Envoy filters) have built-in support. The open-source **Diffy** was designed specifically for this pattern.

Dark mode is powerful and expensive. Reach for it when the risk of getting the change wrong justifies the operational cost; don't reach for it as a matter of routine.

### Step 8 — Pick one action, then close

Ask: *"What's the one rollout move you'll make for this change?"* Push for concreteness.

- *"Roll it out gradually"* → too vague.
- *"Ramp behind a percentage flag: 1% → 10% → 50% → 100%, holding at each step for 24 hours, watching p99 latency and error rate for the pricing endpoint; auto-pause if p99 > 250ms or error rate > 0.5%"* → the action.
- *"Ship dark for a week, compare responses via Diffy, then cut over"* → the action.

Close in one or two sentences. Confirm the plan. If the change is turning out to need bigger surgery (schema migration, protocol change) than the rollout can absorb, name that and route back to [`deployment-discipline`](../deployment-discipline/SKILL.md) for the compatibility work first.

---

## Callout — Feature flag hygiene

Flags are cheap to add and expensive to keep. A codebase littered with stale flags is harder to read, harder to test (every flag doubles the paths), and a source of real bugs (flag-A-on + flag-B-off + old-user-tier = crash).

**Discipline:**

- **Every new flag ships with a removal ticket.** The ticket has a due date and the name of the owner. Not adding the ticket is the norm to break.
- **Kill flags after full ramp.** Once a boolean flag has been 100% on (or off) in production for two release cycles with no issues, delete the flag and the dead branch. Same for percentage ramps that have hit 100%.
- **Do the cleanup incrementally.** Like technical debt in [`technical-debt`](../technical-debt/SKILL.md), flag cleanup is opportunistic — every touch of a file with a stale flag is a chance to delete it.
- **Categorize flags.** *Release* flags (temporary, delete after ramp) vs. *operational* flags (permanent kill switches — circuit breakers, feature-disable levers) vs. *permission* flags (user/tenant entitlements — often belong in a real entitlements system, not a flag system).
- **Audit periodically.** Once a quarter, dump the list of flags and their last-changed date. Anything older than six months with no changes is either dead code or a load-bearing kill switch nobody documented.

**A/B testing caveat** (worth repeating): a percentage-ramp flag is *not* a randomized experiment. Users may end up in inconsistent buckets across sessions, downstream systems may bias the split, and the flag system may not preserve blindness. If you're measuring impact, use a flagging system that offers real experiment buckets and involve a data scientist for the statistics.

---

## Callout — Canary vs. blue/green vs. dark

Three parallel-version patterns, each with its own use case. Pick by the shape of the risk, not by which is the newest thing you read about.

### Canary

- **Shape:** small slice of production traffic hits the new version; rest goes to old. Slice grows over time if healthy.
- **Best for:** high-traffic services where a bad change would page everyone at once. Bugs surface early, on a small user set.
- **Watch out for:** the canary needs enough traffic to be statistically meaningful — a 0.1% canary on a low-traffic service may take days to reveal a subtle bug. Also, shared state means both versions can affect each other.

### Blue/green

- **Shape:** two full environments; one live, one dark-but-warm. Flip the router when green is verified.
- **Best for:** changes that touch many services at once, changes where subsetting traffic is hard or impossible, environments where the ability to *instantly* flip back matters more than a gradual ramp.
- **Watch out for:** the cost of running two full environments (mitigated in cloud by tearing down the old one after soak). Also, database state is shared unless you go to extreme lengths — the compatibility rules still apply.

### Dark mode / traffic shadowing

- **Shape:** the new version runs in parallel and processes real traffic, but its responses are never returned to users; instead they're diffed against the old version's responses and logged.
- **Best for:** complex behavior migrations where the *correctness* of the new path is the risk (new pricing engine, new fraud model, new serialization). Also useful for validating capacity headroom under real load.
- **Watch out for:** side effects (must be suppressed on the shadow path), analytics contamination (mark shadow traffic and filter it), and cost (running everything twice).

**The one that usually wins for a routine change:** a feature flag ramp on the existing service. Reach for canary / blue/green / dark when the change earns it.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't fire the Step 2 menu as a wall.
- **Work on their actual change.** If they describe the specific feature going out, walk through *its* rollout — its SLIs, its blast radius, its rollback path. Don't stay generic if you can stay concrete.
- **Name real tools.** LaunchDarkly, Statsig, Unleash, Flagsmith, split.io for flags; Istio, Linkerd, Envoy, Gloo, ArgoCD Rollouts, Flagger for traffic shaping; Diffy for response diffing. Say what they'll actually reach for.
- **Don't over-engineer.** Small internal service with a boolean toggle doesn't need blue/green plus canary. Match sophistication to risk.
- **When the rollout is already going sideways in real time**, route to [`incident-response`](../incident-response/SKILL.md); roll back first, tighten the rollout plan later.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is designing the build, choosing a package registry, or writing release notes. Route to [`build-and-package`](../build-and-package/SKILL.md) or [`release-hygiene`](../release-hygiene/SKILL.md).
- The user is designing the deploy machinery itself — automation, atomicity, ordering. Route to [`deployment-discipline`](../deployment-discipline/SKILL.md).
- There's an active production incident from a rollout that's already broken. Route to [`incident-response`](../incident-response/SKILL.md).
- The user is designing the observability instruments themselves (which metrics to emit, log structure, tracing propagation). Route to [`metrics`](../metrics/SKILL.md), [`logging`](../logging/SKILL.md), [`tracing`](../tracing/SKILL.md).
- The user is asking about the statistics of A/B testing — significance, power, sample size. Out of scope; recommend a data scientist.
- The user is designing configuration itself (schema, defaults, validation). Route to [`configuration`](../configuration/SKILL.md).

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- ***Continuous Delivery*** — Jez Humble & David Farley (Addison-Wesley, 2010). The deployment-pipeline discipline that continues into rollout. Chapter on canary/blue-green patterns is foundational.
- ***Release It!*** — Michael T. Nygard (Pragmatic Bookshelf, 2nd ed. 2018). Stability patterns; the canonical modern treatment of the circuit-breaker pattern used in Step 5 above.
- ***Site Reliability Engineering*** — Beyer, Jones, Petoff, Murphy (Google, O'Reilly 2016). Free online at https://sre.google/sre-book/. The SLI/SLO framework that anchors Step 3's "declare what healthy means" discipline.
- ***Amazon Builder's Library*** (https://aws.amazon.com/builders-library). Several essays on deployment safety, progressive delivery, and canary analysis from AWS principal engineers.
