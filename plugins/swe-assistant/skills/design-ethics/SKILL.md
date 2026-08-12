---
name: design-ethics
description: Use when a design decision may work against the person using it — a pre-checked consent box, an opt-in default, cancellation made harder than signup, an obscured price or recurring charge, urgency or scarcity that is not real, a quiet decline button beside a loud accept, bundled consents, or repeated nagging until a user relents. Also fires when the user asks whether something counts as a dark pattern, says a request feels wrong but cannot say why, or is weighing a growth or conversion tactic against user interest. Teaches transferable tests rather than a taxonomy to memorize, explains the habituation mechanism that makes these patterns work on attentive people, and covers raising the concern as consent validity and regulatory risk rather than morality. Should be raised unprompted when a design under discussion looks manipulative. Do not trigger for genuinely protective friction such as a confirmation before a destructive action (route to operational-tools), or for legitimate contested design calls like minimal versus rich (route to interface-tradeoffs) — treating every design disagreement as an ethical one devalues the times it matters.
---

# design-ethics

## Source

Pereyra, *Universal Principles of UX* (Rockport) — principles 5 (*Design is not neutral*) and 14 (*Friction isn't always bad*), which together supply the claim and the mechanism.

**Harry Brignull's deceptive patterns** work (https://www.deceptive.design/) is the origin of the *dark patterns* framing and the standard taxonomy. This skill treats it as a reference to look things up in, not a list to memorize — see the note on tests below.

The mechanism comes from **Rainer Böhme and Stefan Köpsell**, *Trained to Accept? A Field Experiment on Consent Dialogs* (CHI 2010) — a single consent dialog run in twelve variations across 80,000 live users.

Regulatory material is current as of early 2026 and is **jurisdiction-specific**; the Canadian position below is the maintainer's own and is offered as a worked example of how to locate yours, not as the answer.

## Pillars this skill strengthens

- **Primary:** Leadership, Communication
- **Also:** Technical Knowledge (consent validity is a compliance property, not only an ethical one)

## What this skill is for

The recurring moment: an engineer is handed a requirement that is technically trivial and quietly works against the person on the other side. Pre-check the box. Make the cancel flow four screens. Default it to opt-in. Nobody in the room describes it as deception, and the person implementing it is usually the last one positioned to object and the first one whose name is on the commit.

This skill fires there. It also fires **unprompted** — see the callout at the end, which is the most important paragraph in it.

## The core mindset (lead with this)

**If you shipped it, you own it.**

- There is no professional body that will stop you and no licence to lose. **Nobody takes a vow leaving a computer science programme.** That absence does not distribute the responsibility elsewhere; it concentrates it on the individual.
- **The specification is not a defence, and neither is the job title.** Whoever writes the code that pre-checks the box has pre-checked the box. Designers are engineers and engineers are designers; the person who ships the interface owns its consequences.
- The question is not *did I lie*. It is **did I arrange things so the user would decide against their own interest without noticing.**

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

### Step 1 — Get the specific pattern

Ask **one** question if it is not already clear:

- *"What exactly are you being asked to build, and what happens to a user who doesn't notice?"*

The second half is the diagnostic. Most deceptive patterns are defensible when described from the perspective of a user who is paying full attention, and indefensible from the perspective of one who is not.

### Step 2 — Apply the tests

Below. Do not reach for the taxonomy first; the tests catch patterns that have no name yet.

### Step 3 — If it fails, help them raise it

The hard part is rarely recognising the problem. It is saying something. See the escalation section — the framing that works is usually **risk**, not morality.

### Step 4 — Close

One concrete next step: the sentence they will say, or the person they will say it to.

---

## The three tests

Learn these rather than the pattern names. Novel deceptive patterns appear faster than taxonomies are updated, and all three of these catch things that do not have names yet.

### 1. The asymmetry test

**Is the friction where the consequence is, or where the revenue is?**

Friction that protects the user is safety. The identical mechanism, placed to protect the company's numbers, is a dark pattern. One click to subscribe and seven screens to cancel is a safety gate pointed backwards.

Run it in both directions: *absence* of friction where consequence is high is as much a decision as its presence where consequence is low. A one-click irreversible purchase and a seven-screen cancellation are the same design philosophy.

### 2. The informed-user test

**Would the user still choose this if they understood it as well as you do?**

If yes, the design is fine and possibly good. If no, you are relying on their not understanding — and a design that depends on the user's ignorance to function is the definition of the thing.

### 3. The disclosure test

**Could you explain this pattern to the user, in plain language, to their face?**

*"We made the decline button grey and small so fewer people would find it"* is a sentence that cannot be said out loud to the person it was done to. That reaction is reliable information. If the honest description is embarrassing, the design is the problem, not the description.

## Why these patterns work — and why "the information was there" fails as a defence

The standard defence is that nothing was hidden: the checkbox was visible, the terms were linked, the user could have read it.

**Böhme and Köpsell tested exactly this.** One consent dialog, twelve variations, 80,000 real users. Their finding was that people accept **more** readily the more a dialog resembles ones they have seen before — habituation, not laziness. Two further results are worth knowing:

- **Polite phrasing and buttons signalling a voluntary choice *decreased* consent**, contrary to what social psychology predicts.
- Response-latency data showed users were **not deciding at all**. They were pattern-matching and moving on.

The consequence: **these patterns do not work by fooling careless people. They work by exploiting a reflex that thousands of prior dialogs installed in careful ones.** Disclosure that relies on the user breaking that reflex is not disclosure. "It was on the screen" describes the pixels, not the consent.

The same finding is why generic confirmation dialogs fail as safety mechanisms — see [`operational-tools`](../operational-tools/SKILL.md), which uses it in the opposite direction.

## Where the actual obligation comes from

**Professional codes do less work here than people expect.** The [ACM Code of Ethics](https://www.acm.org/code-of-ethics) has relevant clauses — 1.2 *Avoid harm*, 1.3 *Be honest and trustworthy* — and it is **voluntary and unenforceable**. Membership is optional, software engineering is unlicensed in most jurisdictions, and no disciplinary consequence follows a violation. Contrast a P.Eng governed by a real regulator with a protected title. Cite the Code to frame an argument; do not present it as authority that settles one.

**Regulation does more work, and it is jurisdiction-specific.** The transferable instruction is: **find out what applies where your users are, before you need it.** Do not assume the regime you have read about online governs you.

> **Worked example — Canada / Ontario, as of early 2026.** Offered to show the shape of the answer, not as the answer.
>
> - **PIPEDA** — consent must not be obtained through deception; organisations must not mislead individuals in connection with obtaining consent.
> - **PHIPA** — for personal health information, consent must be *meaningful*. Consent obtained through a deceptive interface is plausibly not valid consent, which converts a design question into a compliance one.
> - A late-2024 **Office of the Privacy Commissioner** sweep reviewed **145 Canadian websites and apps** specifically for deceptive design.
> - In **November 2024**, the federal, provincial and territorial Information and Privacy Commissioners issued a **joint resolution** urging organisations to avoid designs that influence, manipulate, or coerce users into decisions against their privacy interests.
> - **Bill C-27 is not law.** It died on the Order Paper in January 2025 when Parliament was prorogued. Anyone citing it as binding is mistaken.
>
> Note what makes this argument strong: it is not *this is wrong*. It is **this may invalidate the consent we are relying on.**

## Raising it — the framing that lands

Most engineers recognise the problem and say nothing, because the available script is moral and moral scripts read as accusations.

**Reframe from ethics to risk.** These are the same objection and they are received completely differently:

| Instead of | Say |
|---|---|
| *"This is manipulative"* | *"If consent obtained this way isn't valid, does our lawful basis for the data hold?"* |
| *"This is a dark pattern"* | *"The privacy commissioner ran a sweep for this pattern in 2024 — has legal looked at it?"* |
| *"Users will hate this"* | *"What's our cancellation-complaint and chargeback rate after this ships? Can we agree a threshold to reverse it?"* |

Then, practically:

- **Put it in writing, once, without heat.** A design doc comment or a PR thread creates a dated record that the question was asked. See [`design-doc`](../design-doc/SKILL.md).
- **Ask, don't accuse.** *"What happens to a user who doesn't notice this?"* is harder to dismiss than an assertion and often produces the reconsideration by itself.
- **Name a reversal condition.** Agreeing in advance what result would undo the decision is a proposal rather than an objection, and it frequently gets accepted.
- **Know your own line before you are standing on it.** Decide in the calm moment what you will not build. That decision is much harder to make well under pressure with a deadline.

If it ships anyway, that is a legitimate outcome of raising it. The record exists and the argument was made.

## Callout — Raise this unprompted

**This is the highest-value application of Output Protocol 10.7 anywhere in this skill set.**

An engineer mid-implementation is precisely the person who will not think to ask whether the thing they were handed is manipulative. The requirement arrived as a ticket, it is technically trivial, and the ethical question was decided — if it was decided at all — in a meeting they were not in.

So: **when a design under discussion looks like it works against its user, say so, even when the conversation was about something else.** Once, briefly, without moralising, phrased as a question. Then return to what they asked about.

*"Before we go on — is that checkbox pre-checked on purpose? If consent is what it's for, that may be a problem worth flagging. Happy to keep going on the layout either way."*

That is the whole intervention. It costs one sentence and it is very often the only time anyone will raise it.

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **Do not moralise.** The user is usually the one person in the chain who noticed. Treat them as an ally, not a suspect.
- **Lead with the test, not the taxonomy.** Naming a pattern is satisfying and less useful than a test they keep.
- **Give them the sentence.** *"Raise it with your PM"* is not help. The exact words are.
- **Prefer the risk framing** when they have to say something to someone with more authority.
- **Do not overstate the law**, and do not assert a jurisdiction you have not established. Ask where their users are.
- **Do not overstate professional codes.** The ACM Code is rhetorical, not binding, and pretending otherwise damages the argument when someone checks.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The friction is **genuinely protective** — a confirmation before a destructive action, a deliberate delay on an irreversible operation. That is [`operational-tools`](../operational-tools/SKILL.md), and the asymmetry test above says why it is different.
- The question is a **legitimate contested design call** — minimal versus rich, familiar versus distinctive. Route to [`interface-tradeoffs`](../interface-tradeoffs/SKILL.md). Not every design disagreement is an ethical one, and treating them as such devalues the times it matters.
- The user needs **actual legal advice** for a specific product. This skill helps them ask the right question of someone qualified; it does not answer it.
- The concern is **security** rather than user manipulation. Route to [`input-validation`](../input-validation/SKILL.md) or [`defensive-programming`](../defensive-programming/SKILL.md).
- The user is describing **conduct toward colleagues** rather than users — credit, blame, a hostile review culture. Different domain; help them directly.
