---
name: code-review
description: Use when the user is about to give or is in the middle of giving a code review, about to submit their own code for review, on the receiving end of code-review feedback (especially feedback that feels confusing, harsh, or unclear), preparing a draft / WIP PR, planning a code walkthrough for a large change, triaging a backlog of review requests, or asking how to give or receive code reviews well. Triggers include phrases like "I'm reviewing a PR", "asked to review", "leaving feedback on", "my PR is ready for review", "got harsh review feedback", "should I push to trigger CI", "draft PR", "WIP review", "code walkthrough", "I have a huge review backlog", "how do I structure a code review comment", "what's the priority order for code review", "am I being too nitpicky", "how do I push back on review feedback I disagree with". Walks through the discipline from The Missing Readme (Chapter 7) — why reviews exist (teaching tool, shared awareness, decision archive, security/compliance record), Mode A (you are reviewing) vs Mode B (you are being reviewed), the giving priorities (correctness → security → maintainability → tests → style), the tone discipline (questions over commands, label severity), how to handle large changes via walkthroughs, the don't-rubber-stamp rule, and the receive-side discipline (separate code from self, prepare PRs well, use draft reviews honestly, be proactive on response speed). Cross-links to growth-obstacles for the impostor / Dunning-Kruger feelings that code review reliably triggers. Useful at any stage from Ramp-Up onward; central to the Contributor stage. Do not trigger for general engineering questions, debugging, or asks about how to *write* code from scratch — only when the situation is reviewing or being reviewed.
---

# code-review

## Source

Informed by:

- ***The Missing Readme*** (Riccomini & Ryaboy, No Starch Press 2021), **Chapter 7** ("Code Review") and Chapter 1 (the Contributor stage's expectation to participate in reviews). The bulk of the discipline below — prepare reviews, draft-review etiquette, the don't-trigger-CI anti-pattern, walk-throughs for large changes, triage, block time, comprehensive feedback, don't rubber-stamp, drive to conclusion — comes from Chapter 7.
- **Google's *Code Review Developer Guide*** (https://google.github.io/eng-practices/review/) — the "favor approving once code health is improved even if the CL isn't perfect" framing comes from here.
- **Severity-label conventions** (Blocking / Suggestion / Nit / Question / Praise) are widely-attested practitioner conventions across many companies, popularized in part by Google's guide above.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (spotting issues requires knowing what good code looks like)
- **Builds:** Leadership (over time, your reviews shape the team's standards)

## What this skill is for

Code review is where a team's actual standards live. Docs say one thing; what gets approved says another. This skill fires whenever the user is on either side of that conversation — about to leave feedback, about to submit their own code, planning a walkthrough for a large change, or stuck reacting to feedback that landed badly.

## The core mindset (lead with this)

**Code review is about the code, not the person.** You are a co-author of quality, not a gatekeeper.

- **As reviewer:** your job is to make the code better and to help your teammate grow. It is not to prove you spotted something they missed.
- **As author:** the reviewer is critiquing the code, not your worth. Even feedback that lands badly usually contains useful data.

Two failure modes to avoid: harshness that makes people afraid to ship, and rubber-stamping that ships bad code. Aim for the middle: candid, specific, kind.

---

## Why code review exists (frame for skeptics)

If the user is questioning *whether* code review is worth the time (their own or the team's), surface these four reasons before getting tactical:

1. **It's a teaching tool, both ways.** You learn from feedback on your code; you learn by reading senior teammates' reviews; you learn by being asked to review code you don't yet understand. Code review is one of the highest-bandwidth ways an engineer absorbs the team's standards.
2. **It spreads awareness.** More than one person becomes familiar with every line of production code. This makes the team able to evolve the code cohesively, not as a bunch of personal fiefdoms.
3. **It documents implementation decisions.** *"Why is this done this way?"* often has its answer in the review thread on the PR that introduced it. The review is part of the change's permanent record.
4. **It's a security and compliance control.** Required review means no single developer can unilaterally modify production code — important for both honest mistakes and (rarer but more serious) bad-faith changes. Many regulated industries require this by policy.

---

## How to run — diagnose the mode first

This skill serves two genuinely different users. Diagnose before you respond.

### Step 1 — Ask one question if it isn't obvious

- *"Are you about to **leave a review** on someone else's PR, or are you on the receiving end of feedback / preparing your own PR for review?"*

Three rough modes:

- **Mode A: Reviewing** (you are leaving feedback on a teammate's change) → use the *How to give a good code review* section.
- **Mode B: Being reviewed** (you are submitting code or reacting to feedback) → use the *Getting your code reviewed* section.
- **Mode C: Walkthrough** (you have or are preparing for a large change that needs an in-person walk-through before formal review) → use the *Code walkthroughs* callout.

Many conversations involve both A and B — the same engineer is reviewer on some PRs and author on others. Switch modes as the conversation moves.

---

## Mode A — How to give a good code review

### A0. Triage the review queue

Don't drop everything every time a review request lands. That kills focus and rarely produces a good review.

- **Triage by urgency, size, and complexity.** A one-line fix gets a fast read; a 500-line refactor gets scheduled.
- **On high-velocity teams, you don't have to review every change.** Focus on changes that touch code you're familiar with or that you can learn from.
- **Block off time for reviews.** A dedicated 30–60 minute slot — once or twice a day — beats reactive context-switching. Tell the team your rhythm so they know when to expect you.
- **If a review will take more than 1–2 hours, treat it as work.** Create an issue / task to track it; ask in sprint planning for the time. Large reviews squeezed into the cracks of a day get rubber-stamped.

### A1. Read the PR description first

If there isn't one, **stop and ask for one** before reviewing. *"Hey, can you add a short description of what this changes and why? It'll make the review faster for me and better for you."* A reviewer with no context will either review badly or annoy the author with avoidable questions.

### A2. Read the diff in context

A diff in isolation is misleading. Click into the surrounding code if anything is non-obvious. If you don't understand what the function above the change does, your feedback on the change itself is suspect.

For large or unfamiliar changes, **don't limit yourself to the web-based review tool.** Check out the branch locally, open it in your IDE, run the tests, attach a debugger, trigger the failure scenarios the change is meant to handle. Comments grounded in *"I ran this locally and saw X"* are far more useful than comments grounded in *"I read the diff and wondered if X."*

### A3. Aim to understand the change

Before commenting, make sure you understand:

- **Why is the change being made?** What's the user-visible / business-visible motivation?
- **How did the code behave before?** What changes in behavior?
- **What are the long-term implications?** API surface, data structures, public interfaces — these are the decisions that are hard to reverse.

Ask questions when something isn't clear, *before* leaving prescriptive feedback.

### A4. Review in priority order

Look at things in roughly this order. Don't get stuck on style before you've looked at correctness.

1. **Correctness.** Does it do what the description says it does? Edge cases, off-by-ones, error handling, data integrity.
2. **Security.** Is anything user-controlled flowing into a place it shouldn't? Auth, input validation, secrets, injection vectors. Watch for OWASP Top Ten violations specifically — see [`input-validation`](../input-validation/SKILL.md).
3. **Maintainability.** Will the next person who touches this understand it? Is the naming honest? Are the abstractions earned? How might a future programmer misuse or misunderstand this?
4. **Alternative approaches.** *"How would I have implemented this?"* — not as a gotcha, but to trigger conversation about trade-offs you'd otherwise miss.
5. **Available libraries / services.** Anything the team already has that does what this PR is reinventing?
6. **Tests.** Do they exercise the contract or the implementation? Would they catch a regression? **Read the tests like you read the code** — they document how the code is meant to be used, and they're often where the cleanest reading of the change lives. Easy entry point: *start with the tests*.
7. **Style / nits.** Only if a linter doesn't already handle it. If your team uses a formatter, never review style.

### A5. Use the right tone

- **Questions over commands.** *"What do you think about pulling this into a helper?"* beats *"Pull this into a helper."* The first invites a conversation; the second issues an order.
- **Suggest, don't dictate**, unless it's actually a blocking issue.
- **Explain both the *what* and the *why*.** *"This could be a problem because..."* teaches; *"change this"* doesn't.
- **Write comments the way you'd say them sitting side by side.** Read each comment back to yourself — if it would land badly in person, it lands badly in writing.
- **Acknowledge the good stuff.** Code review isn't only deficit-finding. *"Nice — this is much cleaner than the version we had"* costs nothing and builds trust. Even a change you dislike usually has something worth noting positively.

### A6. Distinguish issues, suggestions, and nitpicks (label severity)

Many teams use prefixes so the author knows what they have to address vs. what's optional:

- `Blocking:` — must change before merge.
- `Suggestion:` (or `Optional:` / `Take it or leave it:` / `Nonblocking:`) — worth considering, author's call.
- `Nit:` — small/stylistic, ignore if you want.
- `Question:` — I want to understand, not asking you to change anything.
- `Praise:` — this is good.

If your team doesn't use these, you can still adopt them yourself. Authors love the clarity.

**Two corrections to the nitpick pattern:**

- **If the same style issue occurs repeatedly, don't keep harping on it.** Say it once with *"applies across the file"* and move on.
- **If you keep nitpicking style, ask whether the team's linter is good enough.** Repetitive style nits are a tooling problem disguised as a review problem. Surface it to the team rather than re-litigating it on every PR.

If your reviews are *all* nits with little substance, **slow down and do a deeper reading.** Surface-level reviews are easy to write but they're not what the team needs from you.

### A7. Don't pile on

If three reviewers have already left the same comment, you don't need to add a fourth. Add a thumbs-up if you want the author to know it's a real concern; otherwise move on.

### A8. Don't rubber-stamp

The temptation is real, especially with a senior author or a long backlog: skim, approve, move on. Resist it. You might be held responsible later, the change might have issues a careful reading would catch, and rubber-stamping degrades the whole team's review standard.

**If you can't prioritize the review adequately, don't review it at all** — say so and let someone else pick it up. That's better than a low-effort approval.

If the temptation comes from the review being *too large*, ask the author to split it into smaller sequential chunks, or to give you a walk-through (see callout below).

### A9. Drive to a conclusion

Reviews shouldn't drift. Conclude with an explicit verdict — *Request Changes* or *Approved* in your tool.

The Google guideline (https://google.github.io/eng-practices/review/reviewer/standard.html) is worth installing as a default: *"reviews should favor approving a CL once it is in a state where it definitely improves the overall code health of the system being worked on even if the CL isn't perfect."*

- **Respect the scope of the change.** If you spot something adjacent that's also worth fixing, **open a ticket** rather than blocking the PR on it.
- **Keep scope tight.** Long PRs that grow during review become impossible to merge.
- **If there's significant disagreement** between you and the author that you can't resolve together, **proactively propose escalation** to another senior or to a tech-lead who can adjudicate. Don't let it stalemate.

---

## Mode B — Getting your code reviewed

### B1. Prepare the review

The single highest-leverage thing you can do for your reviewers — and for your future self when you have to rebase or debug — is prepare the PR well.

- **Keep individual changes small.** Separate feature work and refactoring work into different PRs. A single PR that adds a feature *and* rewrites three unrelated modules is unreviewable.
- **Write descriptive commit messages.** See [`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md) for the seven-rule baseline.
- **Include comments and tests.** Both are part of the review, not afterthoughts.
- **Don't get attached to the code you submit.** Expect it to change. The team owns the code now.
- **Title + description matters.** The PR title and description are *not* the commit message. They should add:
  - Context the commit message doesn't carry (links to issues, design docs, conversations)
  - How the change was tested (locally, in staging, with what data)
  - Open questions or specific things you want feedback on
  - Implementation details a reviewer would otherwise have to deduce

A well-prepared PR gets reviewed faster, gets better feedback, and avoids the most common cause of slow reviews (reviewer context-loading).

### B2. Use draft reviews honestly

A **draft / WIP PR** is an informal request intended to get quick, cheap feedback from a teammate before you go further. Used well, they de-risk big changes.

- **Be explicit when it's a draft.** Prepend `[Draft]` or `[WIP]` to the title; many platforms (GitHub, GitLab) have a built-in "Draft" status — use it.
- **Be equally explicit when it's *ready*.** Convert the draft to a real review, update the description, ping reviewers. Reviewers won't engage seriously with something marked Draft, so leaving it Draft after you're done is the same as never asking.

### B3. Don't submit reviews just to trigger CI tests

This is a real anti-pattern that wastes the team's time:

- It fills the test queue and blocks reviews that actually need their results.
- Teammates see the review request and may waste time looking at code you didn't intend for review yet.
- The fix: **invest in running tests locally.** Make your coding-and-testing loop fast enough that you know within seconds whether you broke something, not within a CI cycle.

If your only way to run tests is to push, that's a tooling problem worth surfacing to the team — not a free pass to spam reviews.

### B4. Don't get attached to your code

This is the hardest receive-side skill. The reviewer is critiquing the code, not you.

- **Separate the code from yourself.** The reviewer didn't say *you* are bad. They said the *code* could be better. This is the single hardest skill in receiving reviews. It gets easier with reps.
- **Treat all feedback as data.** Even feedback that feels wrong usually points at something — maybe the code is fine but the intent isn't clear, or the docstring is misleading, or the abstraction surprised the reader.
- **Whole team owns the code from this point on.** Once it merges, "your" code is the team's code. The reviewer is a co-author.

### B5. Practice empathy, but don't tolerate rudeness

- **Empathy:** the reviewer is doing this in addition to their own work. They're going to miss things, occasionally word things badly, sometimes be wrong. Default to charitable reading.
- **Don't tolerate actual rudeness.** Reviews that target the person, not the code, or that are dismissive in a way that wouldn't fly in person, are worth pushing back on calmly — and if that doesn't resolve it, talking to your manager. Follow team conventions for escalation.

### B6. Respond well

- **Ask for clarification when you don't understand.** *"Can you say more about why you'd prefer Y? I want to make sure I'm getting your point."* Better than guessing and redoing the wrong thing.
- **Push back when you disagree — but with reasoning, not defensiveness.** *"I considered Y but went with X because of Z — does that change your view?"* That's productive disagreement. Not productive: *"This is fine."* / *"I disagree."* / silently ignoring the comment.
- **Resolve, don't ghost.** Every comment deserves a reply, even if it's *"good catch, fixed."* Unresolved comments make reviewers feel ignored and slow down future reviews.
- **Thank careful reviewers.** Especially the ones who left thoughtful or hard-but-fair feedback. They spent their time. A small thanks now buys you better reviews next time.

### B7. Be proactive — and merge promptly

- **If you don't get feedback within a reasonable window, check in.** Without being pushy: *"Hey, when you get a chance, would love your eye on PR-1234 — no rush, just flagging."*
- **Respond to comments promptly.** A review that takes days to round-trip every comment becomes weeks of work for nobody's benefit.
- **Merge promptly after approval.** Leaving an approved PR dangling is inconsiderate. If you wait too long, the code may need to be rebased — and rebases sometimes break logic and trigger another round of review. *Approved* should mean *merging this week* at the latest.

---

## Callout — Code walkthroughs (for large changes)

When a change is genuinely large — a major refactor, a new subsystem, a non-trivial API redesign — the right unit of review may be *human conversation before code comments.*

A **walkthrough** is an in-person (or video) meeting where the author shares their screen and walks teammates through the change. It's not a review meeting; it's an *understanding* meeting. The actual review happens afterward.

**How to run one well:**

- **Circulate the design doc and the code in advance.** Ask teammates to take a look before the meeting. Give adequate time — *not* one hour before the meeting.
- **Start with background.** Why is this change being made? Reviewing the design doc together for 5 minutes is often well-spent.
- **Navigate the code in your IDE as you narrate.** Follow the code flow from a real entry point — page load, API call, application startup — through to where execution terminates. Use the IDE's jump-to-definition; don't try to read code top-to-bottom.
- **Explain the concepts behind any new models or abstractions** — what they're for, how they're meant to be used, how they fit into the larger system.
- **Don't try to get the team to review the code in the walkthrough itself.** Save substantive comments for the actual review. The walkthrough's job is to give people a working mental model so the formal review goes much faster.

When the walkthrough is the right move:

- The change is too large to absorb from a diff alone.
- The change introduces new abstractions the team hasn't seen.
- A reviewer asks for a walkthrough rather than rubber-stamping a huge PR.

A 30-minute walkthrough often saves multiple days of confused review back-and-forth.

---

## Callout — Code review and the impostor / Dunning-Kruger feelings it triggers

Code review is the situation that most reliably surfaces both **impostor syndrome** (*"my code is bad; the reviewer will see right through me"*) and **Dunning-Kruger** (*"this reviewer is obviously wrong, my code is fine"*). Both are normal. Both are also distortion fields that make you act worse than you want to.

If the user is showing signs of either — flinching pre-emptively at feedback, getting defensive in ways that block them from hearing valid comments, or being dismissive of feedback from less-senior teammates — route to [`growth-obstacles`](../growth-obstacles/SKILL.md) for the calibration first, then come back here to handle the specific review situation.

The mindset to install before reading any review:

- **They are critiquing the code, not you.** Even if the wording landed badly.
- **You are critiquing the code, not them.** Even if you're sure you're right.
- **The reviewer might be wrong.** Push back with reasoning. But check yourself first — the certainty that you're right is often the loudest when you're wrong (that's the Dunning-Kruger half of the pattern).

---

## When to escalate vs. let go (as reviewer)

- **Escalate (block the PR or pull a senior in):** correctness bugs, security issues, decisions that will be hard to reverse, anything that violates a team norm in a way that matters.
- **Let go:** style things you personally don't like but the team accepts, micro-optimizations that don't measurably matter, naming preferences when the existing name is fine just not your favorite.

A simple test: *"Will this matter in six months?"* If no, let it go.

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol). Specifically for this skill:

- **Always diagnose the mode first** unless the user's first message makes it obvious. Don't surface review-giving guidance to someone receiving a review, or vice versa.
- **One question per turn.** If you need clarification, ask the most useful question first; don't list options.
- **If they share a draft comment or response, work on the draft directly.** Don't restart with abstract framework.
- **If they're showing impostor / Dunning-Kruger signs, surface the callout above** before the tactical content.
- **In Mode A (reviewing):** walk them through the priority order and the tone guidance, one section at a time. Ask if they want a second pair of eyes on a specific comment they're drafting.
- **In Mode B (being reviewed):** if they're feeling stung, lead with the mindset (separate code from self) before tactics. Ask one question about what specifically landed badly.
- Keep it conversational. One section per response. Don't dump the whole skill body.

## When NOT to use this skill

- The user is asking how to *write* code, not how to review it. Skip.
- The user is debugging, not reviewing. Skip.
- The user is preparing a commit or a PR description as a craft (not the broader review situation). Route to [`commit-and-pr-hygiene`](../commit-and-pr-hygiene/SKILL.md).
- The user is asking general questions about engineering practice not tied to a specific review situation. Route to [`growth-self-check`](../growth-self-check/SKILL.md) or [`contributor-playbook`](../contributor-playbook/SKILL.md) as appropriate.
- The user is showing impostor / Dunning-Kruger signs *and* there is no specific review in front of them. Route to [`growth-obstacles`](../growth-obstacles/SKILL.md) directly.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for full entries.

- **Google's *Code Review Developer Guide*** — https://google.github.io/eng-practices/review/ — the most comprehensive public practitioner reference on running code reviews at scale. Source of the *"favor approving once it improves code health"* framing surfaced above.
- ***Thanks for the Feedback: The Science and Art of Receiving Feedback Well*** — Douglas Stone & Sheila Heen (Penguin, 2014). Receive-side companion to this skill. The three triggers (truth / relationship / identity) that make feedback hard to hear, and the practical moves for hearing it well anyway, transfer directly to code review.
- ***Clean Code*** — Robert C. Martin. Function- and class-level criteria for what *good* code looks like, which translates directly into what to look for during review.
- ***Code Complete*** (2nd ed.) — Steve McConnell. The chapter on collaborative construction (including code reviews and pair programming) is one of the more thorough treatments in the practitioner literature.
