---
name: growth-obstacles
description: Use when the user is expressing self-doubt about their competence (impostor syndrome territory) or showing signs of overconfidence about something they may not fully understand (Dunning-Kruger territory), or asking for help calibrating their self-assessment. Triggers include phrases like "I feel like a fraud", "everyone else seems to know more", "I shouldn't be here", "I'm going to be found out", "I'm not ready for this", "I got here by luck", "I'm an impostor", "this is easy I can do it in a day" (when scope is large), "I don't need to check with anyone, I know this" (in unfamiliar territory), or directly asking about impostor syndrome, the Dunning-Kruger effect, or how to know whether they're over- or under-estimating their own competence. Walks through both growth obstacles from The Missing Readme (Chapter 2) — impostor syndrome (under-estimation) and Dunning-Kruger (over-estimation) — with concrete calibration practices. Goal — see yourself accurately so you can actually climb through the four stages of competence. Do not trigger for general growth reflection (use growth-self-check) or tactical engineering questions.
---

# growth-obstacles

## Source

*The Missing Readme*, Chapter 2, "Getting to Conscious Competence" (Section: Overcoming Growth Obstacles). The two named obstacles — impostor syndrome and the Dunning-Kruger effect — are well-established outside the book; the book frames them as the two main self-perception traps that block the climb through Broadwell's stages.

## Pillars this skill strengthens

- **Primary:** Leadership (self-awareness is the foundation), Communication (soliciting honest feedback)
- **Builds:** Technical Knowledge (DK antidotes drive deeper learning)
- **Meta:** Touches all four pillars by improving the accuracy of self-assessment that drives growth in every dimension

## What this skill is for

Both impostor syndrome and Dunning-Kruger are distortions of the same thing: **your view of your own competence.** And that view is what determines whether you climb through the four stages. If you think you know less than you do (impostor), you stall in Stage 2, paralyzed. If you think you know more than you do (DK), you skip Stage 2 entirely, miss what you don't know, and make confident mistakes.

This skill fires when the user is in either trap, or asking how to tell which one they're in. The work is **fixing the lens** before doing the assessment. After the lens is right, [`growth-self-check`](../growth-self-check/SKILL.md) is the structured rubric for the assessment itself.

## The core mindset (lead with this)

**The goal is to see yourself clearly — not to feel good, and not to feel humble.**

- Calibration is the practice. Confidence and humility both need to track reality, not feeling.
- Impostor syndrome is not modesty. It is a *false* report. Treating it as truth is a mistake.
- Dunning-Kruger is not arrogance. It is a *blind spot*. Treating it as truth is a different mistake.
- Both traps run in the background unless you actively check.

---

## The two obstacles (mirror images)

### Impostor syndrome — *the under-estimation trap*

**What it is:** the persistent feeling that you don't really belong, that everyone else is more competent, that you've made it this far by luck and you'll soon be found out. Common in engineering because the surface area of "things you could know" is vast, and there's always someone who knows more about any given thing than you do.

**Where it comes from:** comparing your inside (uncertain, full of internal monologue, aware of your gaps) to others' outside (confident, polished, gap-hidden). The comparison is structurally rigged against you.

**How it shows up:**

- *"Everyone else seems to know more than me."*
- *"I'm going to be found out."*
- *"I got here by luck / by accident."*
- *"I shouldn't speak up — I'm not qualified to have an opinion."*
- *"I don't deserve this role / this team / this promotion."*
- *"I can't take that opportunity — I'm not ready yet."*

**Why it's a growth obstacle:**

- Stops you from asking questions (afraid to look dumb). Note: this is exactly the failure mode [`asking-for-help`](../asking-for-help/SKILL.md) calls "martyr."
- Stops you from taking opportunities you'd grow from (don't feel ready).
- Stops you from claiming credit for what you've done.
- Stops you from giving feedback or pushing back (who am I to say?).
- Stops you from speaking up about real problems you've noticed.

**The brutal irony:** impostor syndrome is most acute in the *competent* engineers, because they have a more accurate map of how much they don't know. The actual frauds rarely feel like frauds. (See Dunning-Kruger, opposite side.)

### Dunning-Kruger — *the over-estimation trap*

**What it is:** the cognitive bias that, in domains where you have *limited* knowledge, you also have limited knowledge of the *limits of your knowledge* — so you overestimate your competence. The curve goes: tiny bit of knowledge → peak of confidence ("Mount Stupid") → realization of how much you don't know → crash → slow climb back up to actual competence.

**Where it comes from:** the same cognitive machinery that produces competence — knowing the gaps — only develops *with* competence. So at the start, you can't see the gaps. Everything looks simpler than it is.

**How it shows up:**

- *"This is easy — I can do it in a day"* (about something that's actually two weeks).
- *"I don't need to check with anyone, I know this domain"* (after a week of exposure).
- *"This obviously won't break"* (about something with edge cases you haven't seen).
- *"My approach is clearly better than what they're doing"* (about a system whose history you don't know).
- *"The feedback I got is wrong"* (without engaging with why a thoughtful reviewer said it).
- Strong, fast opinions on a topic just-encountered.

**Why it's a growth obstacle:**

- Stops you from learning more on a topic you think you already understand.
- Stops you from asking questions — you think you have the answer.
- Stops you from listening to feedback — you assume the feedback is wrong.
- Leads to bad decisions made with confidence — which are much harder to recover from than uncertain ones.
- Note: this is exactly the failure mode [`asking-for-help`](../asking-for-help/SKILL.md) calls "drain" — except the drain doesn't know they're being one.

**The brutal irony:** by definition, you can't easily see when you're in Dunning-Kruger. The cure has to be installed in advance, as a *habit of doubt* you keep running even when you feel certain.

---

## Self-check — which one am I in right now?

Most people have both, at different times, for different topics. Some patterns to watch for:

| You feel… | About… | Likely trap |
|---|---|---|
| Anxious, inadequate, "everyone else gets it" | A topic you've actually been studying for months | Impostor |
| Confident, dismissive of complications | A topic you just learned about a week ago | Dunning-Kruger |
| Hesitant to claim credit for shipped work | Work you actually did | Impostor |
| Sure the senior engineer's caution is overblown | A system you don't yet know the history of | Dunning-Kruger |
| Reluctant to apply for / accept a stretch opportunity | A role that's a step up from your current scope | Impostor |
| Quick to dismiss feedback as "they don't get it" | Code you wrote recently | Dunning-Kruger |

**Junior tendency:** impostor on big things you've been doing for a while (the real work), DK on small things you just learned (the shiny thing).

**Senior tendency:** more accurate calibration overall, but cycles back to impostor when changing domains, companies, or roles. Even senior engineers feel like newcomers when newly senior somewhere else.

---

## Calibration practices (both obstacles, same toolkit)

These work on either trap because both come from the same problem: *not enough comparison to external reality.*

### 1. Keep a brag doc

A running list of:

- Things you've shipped (with rough scope and impact).
- Times you taught someone else something they didn't know.
- Times someone explicitly thanked you for help.
- Positive feedback you've received (from PRs, 1:1s, slack messages — anywhere).

**Why this works:** the impostor brain forgets evidence. The brag doc is external evidence you can re-read when the feeling lies to you. The DK brain over-weights recent wins; the brag doc shows you the full picture and what's *not* on it.

**Note:** "brag doc" is a useful internal term — you don't have to share it. It's calibration material, not a marketing artifact. Though it's also great for performance reviews — see [`growth-self-check`](../growth-self-check/SKILL.md) for that use.

### 2. Track predictions vs. outcomes

When you're about to do something — estimate a project, ship a PR, predict an incident's severity, predict how a meeting will go — **write down your prediction first.** Then check it later.

**Why this works:** the gap between prediction and outcome is the most honest measure of competence you have. Over time, it tells you which domains you're well-calibrated in and which you're not. The DK brain insists you're calibrated; the data tells the truth. The impostor brain insists you're not; the data also tells the truth.

Heuristic: aim for "right 70–80% of the time, wrong in proportionate ways." Right 99% of the time means you're not predicting confidently enough. Right 30% of the time means you're not learning from your mistakes.

### 3. Ask for specific feedback from people who would know

Not *"how am I doing?"* (impossible to answer, useless). Instead:

- *"On the X project, was my scoping accurate? Where did I miss things?"*
- *"In the design review yesterday, did I push back on the right things, or did I miss something obvious?"*
- *"You've seen me write a lot of code now. What's the one habit I should change?"*

**Why this works:** specific questions get specific answers. And the answer often surprises both directions — impostor folks find out they're more solid than they thought; DK folks find out there's a habit they didn't know about.

### 4. The "explain it back" test (DK-specific)

When you feel confident about something, try to:

- Explain it out loud to a teammate.
- Defend it against thoughtful questioning.
- Predict 3 edge cases that would break the simple version.

**Why this works:** DK collapses fast under the requirement to *generate explanation under questioning.* The gap between "I can use this" and "I can teach this" is enormous, and reaching for the explanation reveals which side you're on.

### 5. Notice "comparing inside to outside" (impostor-specific)

When you find yourself thinking *"everyone else seems to get this,"* pause and check:

- Did you actually *see inside* their thinking, or are you inferring from their outside?
- If you talked to that person privately and asked "do you also feel lost sometimes?" — what's the most likely answer? (Almost always: yes.)
- Are you comparing your worst day to their best day?

The comparison is structurally unfair. Once you see it, the feeling loses some of its grip.

---

## Callout — How AI tools can exacerbate both

This assistant is itself worth flagging in this context. AI tools can deepen *either* trap:

- **Impostor amplifier:** *"The AI does it better than me. I'm useless. Why am I even here?"* This is structurally wrong — the AI is a tool, not a peer. You wouldn't compare yourself to a hammer. The relevant question is whether *you with the AI* are better than *you without it*, and whether your judgment about when to use it is improving.

- **Dunning-Kruger amplifier:** *"I generated code that compiled and shipped. I clearly understand this domain."* This is the most dangerous trap of AI-accelerated work — you can produce competent-looking output without building competence. The test is whether you could write it yourself, or maintain it, or debug it when it breaks. If no, the AI is doing the work; *you're* still in unconscious incompetence about that domain.

The antidote in both directions is the same: **calibrate to what *you* can do, not to what *you-plus-AI* can do.** That distinction matters because the AI isn't there when production is on fire at 2am, when the design review is happening live, when the interview asks you to explain your reasoning.

---

## How to run

### Step 1 — Frame

Two sentences. Surface the mindset (see clearly, not feel good/humble), and signal you'll diagnose which trap they might be in.

### Step 2 — Diagnose (one question at a time)

Per the [Output Protocol](../../docs/METHODOLOGY.md#10-output-protocol), ask **one** question per turn. The second one (if needed) waits for a later turn.

Start with: *"What's the situation — what specifically are you doubting (or confident about)?"*

If the user's answer to the first question doesn't make the trap obvious, ask a second one in the next turn — typically: *"What's the evidence on either side of how you're seeing it?"*

Often the user's first message already names the trap (e.g., *"I feel like a fraud"* — impostor; *"this should be easy"* on something large — possible DK). In those cases, skip the diagnostic and go to Step 3.

### Step 3 — Surface the relevant trap and antidote

Pull the relevant section above. Don't dump both unless they're explicitly asking about both.

### Step 4 — Suggest one calibration practice to try this week

Pick the one most likely to bite for their specific case:

- Impostor + project anxiety → brag doc (cheap to start, instant calibration)
- Impostor + opportunity hesitation → specific feedback solicitation
- DK + scope estimation → prediction tracking
- DK + strong opinions → explain-it-back test

### Step 5 — Close

One or two sentences. Confirm the practice, and offer to come back to do a [`growth-self-check`](../growth-self-check/SKILL.md) once the lens feels clearer.

## Output style

- For impostor cases, be warm — the feeling is real even when the report is false. Lead with empathy before tactics.
- For potential DK cases, be careful. *Don't* tell them they're being overconfident; ask questions that let them notice. *"What would change your mind about this?"* and *"Can you teach me what makes the simple approach wrong here?"* are useful prompts.
- Don't lecture about the framework. Use it as the engine, not the surface.

## When NOT to use this skill

- The user wants a structured self-assessment (am I solid on the four pillars?) without the lens-fixing — route to [`growth-self-check`](../growth-self-check/SKILL.md).
- The user is asking a tactical engineering question. Skip — those need real help.
- The user is in distress about their job that goes beyond competence concerns (burnout, bullying, real performance issues). Acknowledge first; this skill isn't designed for those situations.
- The user is asking about *someone else's* impostor syndrome or DK. The frameworks apply but this skill is designed for first-person work.

## Further reading

Surfaced as a reference but not yet folded in — see [`READING-LIST.md`](../../READING-LIST.md) for the full entry.

- *Presence: Bringing Your Boldest Self to Your Biggest Challenges* — Amy Cuddy. The embodied side of impostor syndrome — posture, physical state, pre-game rituals. (Read critically: some of the power-pose research has had replication issues; the broader thesis about embodied self-trust still has support.)
