---
name: code-review
description: Use when the user is about to review someone else's pull request or merge request, has been asked to review code, is in the middle of leaving feedback on a PR, is on the receiving end of code review feedback (especially feedback that feels confusing, harsh, or unclear), or is asking how to give or receive code reviews well. Walks through how to give a good review — order of priorities (correctness, security, maintainability, clarity, then style), tone (questions over commands, suggest don't dictate), what to label as blocking vs nit, what to skip if a linter handles it, and when to praise. Also covers receiving reviews well — separating the code from the self, asking for clarification, when to push back with reasoning. Useful at any stage from Ramp-Up onward; central to the Contributor stage. Do not trigger for general engineering questions, debugging, or asks about how to *write* code from scratch — only when the situation is reviewing or being reviewed.
---

# code-review

## Source

Informed by *The Missing Readme*, Chapter 1, "The Journey Ahead" (Contributor stage). The book's pointer is brief; this skill expands on it because code review is one of the most frequent recurring situations in any engineer's week.

## Pillars this skill strengthens

- **Primary:** Communication, Execution
- **Also:** Technical Knowledge (spotting issues requires knowing what good code looks like)
- **Builds:** Leadership (over time, your reviews shape the team's standards)

## What this skill is for

Code review is where a team's actual standards live. Docs say one thing; what gets approved says another. This skill fires whenever the user is on either side of that conversation — about to leave feedback, or about to react to feedback they received.

## The core mindset (lead with this)

**Code review is about the code, not the person.** You are a co-author of quality, not a gatekeeper.

- **As reviewer:** your job is to make the code better and to help your teammate grow. It is not to prove you spotted something they missed.
- **As author:** the reviewer is critiquing the code, not your worth. Even feedback that lands badly usually contains useful data.

Two failure modes to avoid: harshness that makes people afraid to ship, and rubber-stamping that ships bad code. Aim for the middle: candid, specific, kind.

---

## How to give a good code review

### 1. Read the PR description first

If there isn't one, **stop and ask for one** before reviewing. *"Hey, can you add a short description of what this changes and why? It'll make the review faster for me and better for you."* A reviewer with no context will either review badly or annoy the author with avoidable questions.

### 2. Read the diff in context

A diff in isolation is misleading. Click into the surrounding code if anything is non-obvious. If you don't understand what the function above the change does, your feedback on the change itself is suspect.

### 3. Review in priority order

Look at things in roughly this order. Don't get stuck on style before you've looked at correctness.

1. **Correctness.** Does it do what the description says it does? Edge cases, off-by-ones, error handling, data integrity.
2. **Security.** Is anything user-controlled flowing into a place it shouldn't? Auth, input validation, secrets, injection vectors.
3. **Maintainability.** Will the next person who touches this understand it? Is the naming honest? Are the abstractions earned?
4. **Tests.** Do they exercise the contract or the implementation? Would they catch a regression?
5. **Style / nits.** Only if a linter doesn't already handle it. If your team uses a formatter, never review style.

### 4. Use the right tone

- **Questions over commands.** *"What do you think about pulling this into a helper?"* beats *"Pull this into a helper."* The first invites a conversation; the second issues an order.
- **Suggest, don't dictate**, unless it's actually a blocking issue.
- **Explain why.** *"This could be a problem because..."* teaches; *"change this"* doesn't.
- **Praise good things.** Code review isn't only deficit-finding. *"Nice — this is much cleaner than the version we had"* costs nothing and builds trust.

### 5. Label severity

Many teams use prefixes so the author knows what they have to address vs. what's optional:

- `Blocking:` — must change before merge
- `Suggestion:` — worth considering, author's call
- `Nit:` — small/stylistic, ignore if you want
- `Question:` — I want to understand, not asking you to change anything
- `Praise:` — this is good

If your team doesn't use these, you can still adopt them yourself. Authors love the clarity.

### 6. Don't pile on

If three reviewers have already left the same comment, you don't need to add a fourth. Add a thumbs-up if you want the author to know it's a real concern; otherwise move on.

### 7. When you're uncertain, frame as a question

*"I'm not sure about this — can you walk me through why X?"* is honest, useful, and protects the author from defending against a confident wrong opinion.

---

## How to receive a code review well

### 1. Separate the code from yourself

The reviewer didn't say *you* are bad. They said the *code* could be better. This is the single hardest skill in receiving reviews. It gets easier with reps.

### 2. Treat all feedback as data

Even feedback that feels wrong usually points at something — maybe the code is fine but the intent isn't clear, or the docstring is misleading, or the abstraction surprised the reader. The feedback is data about how the code lands; what you do with it is your call.

### 3. Ask for clarification when you don't understand

*"Can you say more about why you'd prefer Y? I want to make sure I'm getting your point."* Better than guessing and re-doing the wrong thing.

### 4. Push back when you disagree — but with reasoning, not defensiveness

*"I considered Y but went with X because of Z — does that change your view?"* That's a productive disagreement.

What's not productive: *"This is fine."* / *"I disagree."* / silently ignoring the comment.

### 5. Resolve, don't ghost

Every comment deserves a reply, even if the reply is *"good catch, fixed."* Unresolved comments make reviewers feel ignored and slow down future reviews.

### 6. Thank the careful reviewers

Especially the ones who left thoughtful or hard-but-fair feedback. They spent their time. A small thanks now buys you better reviews next time.

---

## When to escalate vs. let go

- **Escalate (block the PR or pull a senior in):** correctness bugs, security issues, decisions that will be hard to reverse, anything that violates a team norm in a way that matters.
- **Let go:** style things you personally don't like but the team accepts, micro-optimizations that don't measurably matter, naming preferences when the existing name is fine just not your favorite.

A simple test: *"Will this matter in six months?"* If no, let it go.

---

## Output style

Follow the [Output Protocol](../../docs/METHODOLOGY.md#10-output-protocol). Specifically for this skill:

- **One question per turn.** If you need clarification, ask the most useful question first; don't list options.
- **If they share a draft comment or response, work on the draft directly.** Don't restart with abstract framework.
- **If the user is about to give a review,** walk them through the priority order and the tone guidance, one section at a time. Ask if they want a second pair of eyes on a specific comment they're drafting.
- **If the user is receiving a review** and feeling stung, lead with the mindset (separate code from self) before tactics. Ask one question about what specifically landed badly.
- Keep it conversational. One section per response. Don't dump the whole skill body.

## When NOT to use this skill

- The user is asking how to *write* code, not how to review it. Skip.
- The user is debugging, not reviewing. Skip.
- The user is asking general questions about engineering practice not tied to a specific review situation. Route to [`growth-self-check`](../growth-self-check/SKILL.md) or [`contributor-playbook`](../contributor-playbook/SKILL.md) as appropriate.
