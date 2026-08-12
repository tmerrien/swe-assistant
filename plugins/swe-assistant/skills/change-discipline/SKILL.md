---
name: change-discipline
description: Use when the user is considering a meaningful change to the way things already work — rewriting a module or system, bypassing a team standard or convention, forking a library instead of contributing upstream, or swapping one technology for another. Triggers include "I want to rewrite this", "let me migrate us from X to Y", "I'm going to fork the library to fix this", or "I don't agree with our coding standards". Uses Horowitz's 10x-better rule as the decision criterion. For new-technology evaluation specifically, route to choose-boring-technology. Skip for small in-flight refactors, code reviews, or active incidents.
---

# change-discipline

## Source

*The Missing Readme*, Chapter 3, "Working with Existing Code" (Section: Avoiding Pitfalls). The 10x rule is from Ben Horowitz, *The Hard Thing About Hard Things* (Harper Business, 2014). The boring-technology framing is from Dan McKinley's *Choose Boring Technology* (http://boringtechnology.club/) — see also the dedicated [`choose-boring-technology`](../choose-boring-technology/SKILL.md) skill.

## Pillars this skill strengthens

- **Primary:** Leadership (judgment about when not to change things), Communication (proposing changes through proper channels)
- **Also:** Execution (working effectively within existing structure), Technical Knowledge (understanding the real costs of change)

## What this skill is for

Engineers — especially early- and mid-career — frequently feel the urge to change things in the codebases and stacks they inherit. "This should be rewritten." "This standard is dumb, I'll just bypass it." "Let me fork this and fix the bug." "We should switch to [new framework]."

These urges are often partly right — the existing thing *does* have problems. But changes have compound costs that the urge tends to obscure. This skill fires when the user is contemplating that kind of change, and helps them apply real cost/benefit discipline before they commit time and political capital to it.

## The core mindset (lead with this)

**Default to staying put. The cost of changing what already works is usually invisible until you start the change.**

Existing code, standards, and stacks come with accumulated context — bug fixes embedded in the implementation, documentation people have read, mental models teammates have built. Changing them resets that accumulation. The new thing has to be *meaningfully better*, not just "what I would have built."

The Horowitz test, applied to engineering decisions:

> *"The primary thing that any technology startup must do is build a product that's at least ten times better at doing something than the current prevailing way of doing that thing. Two or three times better will not be good enough to get people to switch to the new thing fast enough or in large enough volume to matter."*
> — Ben Horowitz, *The Hard Thing About Hard Things* (2014)

The rule transfers cleanly: **switching from one piece of working software, one convention, or one technology to another is also asking everyone to "switch."** Costs the asker forgets to count: retraining teammates, breaking other code that depended on the old thing, losing the embedded context, replacing all the surrounding tooling and integrations, migration time across many systems, debugging time in the new thing while you re-learn its failure modes. **If the new thing is only 2× or 3× better, the switch loses on net almost every time.** 10× is the threshold that makes the math actually work.

This isn't a literal *exactly-ten* requirement — it's a guard against romantic estimates of benefit. If you struggle to argue the change is dramatically better, it probably isn't.

---

## The four pitfalls

### 1. The urge to rewrite

The most common form: *"This module is a mess, I'm going to rewrite it from scratch."*

What the urge misses:
- The "mess" usually contains years of bug fixes and edge-case handling you can't see. (See [`software-entropy`](../software-entropy/SKILL.md) for the reframe — most code mess is the natural cost of evolution, not negligence.)
- A rewrite takes longer than its estimate, always. Often 3–10×.
- During the rewrite, the team can't ship features at the old rate. Rewrites come at the expense of new features, and that opportunity cost is usually invisible in the proposal.
- The rewrite reintroduces the bugs the old code already fixed. Some of those bugs will only be found in production.

Better moves, in roughly increasing order of intervention:

- **In-flight refactoring.** When you're already changing a piece of code, leave it slightly better than you found it. See [`changing-legacy-code`](../changing-legacy-code/SKILL.md).
- **Add tests around it first, then change incrementally.** Feathers' Legacy Code Change Algorithm — also in `changing-legacy-code`.
- **Propose specific named debt payoff** if the issue is structural and recurring. See [`technical-debt`](../technical-debt/SKILL.md) for the framework.
- **Rewrite only as a last resort,** when the cost of the rewrite is genuinely smaller than the cost of continuing — and when you can prove the 10× benefit. *"Migrations are awful"* is engineering folk wisdom for a reason.

### 2. Going rogue on standards

The urge: *"This linter rule is stupid, I'll just disable it for my PR."* Or *"Our naming convention is bad, I'll use the one I prefer."*

Why this fails even when you're right:

- **Standards are coordination devices.** Their value is that *everyone follows them*, not that they're optimal. Diverging makes the codebase harder for everyone to read, including future-you.
- **Bypassing makes you not-fit-the-team.** You might be technically correct and still socially expensive. That cost compounds.
- **Other people will copy what you do.** Now there are two conventions in the codebase, and the next engineer has to decide which to follow.

The right move: **change the standard through proper channels.** Concretely:

- **Write down what you want changed**, why, what the alternative is, and what the cost of the current standard is. (Same shape as a debt proposal — see [`technical-debt`](../technical-debt/SKILL.md), or [`design-doc`](../design-doc/SKILL.md) for larger changes.)
- **Find the owner.** Most standards have an owner or a team that "owns" them. Address the proposal to them, not into the void.
- **Argue priority, ownership, cost, implementation.** Those are the four dimensions standards conversations actually turn on. Be specific about all four.
- **Don't be distracted from daily work** while you advocate. Your credibility to propose change comes partly from being competent at your actual job.
- **Tell your manager you're spending time on this.** Time spent advocating for change should be visible, not hidden.

Side benefit of going through channels: you build cross-team relationships and become known as someone who proposes change constructively rather than someone who just diverges. That's how engineers become early adopters of *real* change later.

### 3. Forking without committing upstream

The urge: *"This library has a bug. I'll fork it, fix the bug, and use my fork."*

What happens next:
- You make the small fix in your fork. It works. You move on.
- The upstream library releases a new version. You can't easily take it because your fork has diverged.
- You make another small tweak. The divergence grows.
- Six months later, you're maintaining a substantially different piece of software, and you have no community supporting it. You own a fork.

Better moves:

- **Contribute the fix upstream.** Open a PR to the original library. Even if it takes weeks to merge, you've eliminated the long-term cost.
- **Use a temporary workaround** in your code that calls the library, and remove it when upstream fixes it.
- **If the fix can't go upstream** (rejected by maintainers, license issues, etc.), then yes, fork — but **only with the explicit understanding that you now own that fork forever.** Document it. Budget for its maintenance.

The rule: **don't fork without committing the fix upstream first, or accepting upfront that you're now maintaining a separate piece of software.**

### 4. Adding new technology to the stack

The urge: *"This new framework / language / database / tool is so much better, we should adopt it."*

This pitfall is significant enough that it has its own dedicated skill: see [`choose-boring-technology`](../choose-boring-technology/SKILL.md) for the full treatment of innovation tokens, ecosystem-maturity evaluation, and the decision framework. The short version:

- **New technology is less mature.** You don't yet know its failure modes; boring technology's failure modes are well-understood and survivable.
- **Every new technology costs an "innovation token."** Your team has a limited budget of these per quarter. Spending one on a tech swap is opportunity cost against innovative features.
- **Ecosystem maturity matters more than feature lists.** Packaging, IDE support, library ecosystem, test frameworks, engineer availability — these are what determine whether the new tech actually lives long enough to matter.

Route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md) for the full framework.

---

## How to run

### Step 1 — Diagnose the urge

Ask the user:

- *"What specifically are you trying to change — code, a convention, a library, or a piece of the stack?"*
- *"What's the trigger? Is something blocking you right now, or is this an urge to clean up something that bothers you?"*

The answer routes which of the four pitfalls to surface.

### Step 2 — Apply the 10× test honestly

Walk them through the Horowitz framing. Ask:

- *"What does the world look like after the change, specifically?"*
- *"What does it cost to get there — time, retraining, opportunity cost, risk of new bugs, lost context?"*
- *"Is the benefit 10× the cost, or are you romanticizing?"*

If they can't argue 10×, the change is probably not worth it. That's a useful conclusion on its own.

### Step 3 — Surface a smaller alternative

For most cases there's a smaller intervention that captures most of the benefit at much lower cost:

- Rewrite → incremental refactor + characterization tests ([`changing-legacy-code`](../changing-legacy-code/SKILL.md))
- Bypass standards → propose change through proper channels
- Fork → contribute upstream + temporary workaround
- New tech → see if existing stack can solve the underlying need ([`choose-boring-technology`](../choose-boring-technology/SKILL.md))

Help them find the smaller move.

### Step 4 — If the change still passes the bar, plan it

When the change *does* pass the 10× test — and sometimes it does — help them plan it as a real proposal:

- Write it down ([`design-doc`](../design-doc/SKILL.md) for technical changes; [`technical-debt`](../technical-debt/SKILL.md) for paydown proposals).
- Find the right owner/audience.
- Be explicit about costs, alternatives considered, and the criteria for success.
- Make sure their manager knows they're spending time on this.

### Step 5 — Close

Confirm the decision (do the smaller thing, or propose the bigger thing through channels) and the next concrete action. If they're going to propose a real change, offer to walk through the proposal with them.

## Output style

- **Validate the underlying frustration.** The urge to change usually points at a real pain. Don't dismiss it; redirect the energy toward a smaller or more strategic move.
- **Apply the 10× test concretely.** Don't just cite Horowitz — ask the actual question: *"What would the world look like after, specifically?"* Vague benefits don't survive the math.
- **Be honest when the change is worth it.** This skill is not a blanket "don't change anything." Sometimes the rewrite or the new tech is right. The discipline is reserving "yes" for those cases.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is doing an **in-flight refactor** as part of normal feature work (not a proposed rewrite) — route to [`changing-legacy-code`](../changing-legacy-code/SKILL.md).
- The user is **evaluating a specific new technology** rather than the broader "should we change?" question — route to [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- The user is **identifying technical debt** to pay down — route to [`technical-debt`](../technical-debt/SKILL.md). (Tech debt paydown is sometimes the right alternative to a rewrite — this skill helps them see the difference.)
- The user is in an **active incident** — route to [`incident-response`](../incident-response/SKILL.md). Discipline-about-change conversations are for calm afternoons.

## Further reading

Surfaced as primary references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md).

- *The Hard Thing About Hard Things* — Ben Horowitz (Harper Business, 2014). Source of the 10× rule used in this skill, with broader management/leadership context.
- *Choose Boring Technology* — Dan McKinley (http://boringtechnology.club/). Foundational for the new-tech discipline; covered in detail in [`choose-boring-technology`](../choose-boring-technology/SKILL.md).
- *The Mythical Man-Month* — Frederick P. Brooks Jr. (Addison-Wesley, 1975; Anniversary Edition 1995). Source of the **second-system effect** — exactly the trap behind the urge to rewrite — and **Brooks's law** (*"adding manpower to a late software project makes it later"*). Both directly relevant to the rewrites and standards sections of this skill.
