---
name: learning-toolkit
description: Use when the user is trying to learn something deliberately — a codebase, a system, a language, a tool, a domain — rather than just trying to ship a specific thing. Triggers include asking how to learn an unfamiliar codebase, how to get good at debugging or a particular tool, how to read code effectively, how to set up a sustainable learning habit, whether to do a side project to learn X, how to make sense of a complex system, expressing they don't feel like they're learning enough, or asking how to build the practice of learning itself. Walks through the learning toolkit from The Missing Readme (Chapter 2) — front-loading learning at the start, learning by doing, experimenting with code, reading widely (code, tickets, docs, books, papers), watching presentations, attending meetups and conferences, pairing and shadowing, side projects. Goal — get the user to conscious competence (Broadwell's stage 3) as quickly as possible. Do not trigger for tactical engineering questions or when the user just wants the answer to ship something.
---

# learning-toolkit

## Source

*The Missing Readme*, Chapter 2, "Getting to Conscious Competence" (Section A: Learning to Learn). The chapter's frame is Broadwell's *Four Stages of Competence*. See [`JOURNEY.md`](../../JOURNEY.md) for the career stage map (different framework, complementary).

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (pair programming, reading-group participation)
- **Builds:** All four pillars over time — this is meta-skill work

## What this skill is for

The chapter's goal is the right one: **get to conscious competence as quickly as possible.** This skill fires when the user is in *learning mode* — deliberately building competence in something — and gives them a toolkit to choose from. Different things you're learning call for different techniques; the skill helps you pick.

## The core mindset (lead with this)

**Learning is something you do, not something you're given.**

- Reading the answer is not the same as building the model. The understanding lives in your hands and your head, not in the page you read.
- The most expensive stage of learning is the one where you don't know there's anything to learn. Catching gaps early is the highest-leverage move you have.
- Learning is bursty by nature. Some weeks you'll absorb a lot; some weeks you'll consolidate. Both are necessary.

---

## Callout — Broadwell's four stages of competence

The chapter's organizing frame. Worth reading once and remembering.

1. **Unconscious incompetence** — *you don't know what you don't know.* The most expensive stage, because you can't ask for help with a gap you can't see. Most of "wasted time" early in a job lives here.
2. **Conscious incompetence** — *you know there's something to learn.* Uncomfortable but productive. The gap is visible; you can act on it.
3. **Conscious competence** — *you can do it, with effort and attention.* You think hard, and you get the right answer.
4. **Unconscious competence** — *you can do it without thinking.* Reps got you here; no shortcut.

The chapter's argument: **Stage 1 → 3 is teachable. Stage 3 → 4 is just time on task.** So the leverage is all in moving fast through the first three stages — noticing what you don't know, then deliberately closing the gap. This skill is about how to do that.

---

## How to run the skill

### Step 1 — Frame

Two or three sentences. Surface the mindset, mention the four stages if relevant, and tell the user you'll tailor what you suggest based on what they're actually trying to learn.

### Step 2 — If their first message isn't already specific enough, ask ONE question

Often the user's first message tells you what they want to learn, and you can skip straight to Step 3. If it does not, ask **one** of the following — not both, not a list. Pick the most useful one for the situation:

- *"What specifically are you trying to learn?"* — when the goal is vague (*"I want to be better at engineering"* needs sharpening).
- *"What have you tried already, if anything?"* — when the goal is clear but you need to know which stage they're at.

Ask one. Wait for the answer. The second question, if needed, comes in a later turn — never in the same message.

Many users will include both pieces of context in their first message unprompted. When they do, **do not re-ask.**

### Step 3 — Surface 2–4 relevant techniques

Don't dump all eight. Pick the ones that fit *what they're learning* and *what they've tried*. Reference the toolkit below as a menu.

### Step 4 — Pick one move for this week

Concrete. Verb + deadline. *"Read the docs"* is too vague. *"Trace one user request through the auth service end-to-end by Wednesday and write down every file it touches"* is the action.

### Step 5 — Close

Two sentences. Confirm the action, offer to come back when they want a debrief or hit something they don't understand.

---

## The toolkit (the eight techniques)

### A. Front-load your learning

Spend your first few months on the job *intentionally* learning how everything works. It feels uncomfortable because you want to be shipping; but the time invested early compounds for years. The engineer who front-loads context is the engineer who, six months in, can scope a project correctly because they understand the constraints. The engineer who skipped the investment is still hitting walls they didn't know existed.

This pairs well with [`new-team-onboarding`](../new-team-onboarding/SKILL.md) and [`ramp-up-playbook`](../ramp-up-playbook/SKILL.md) — those are stage skills; this is the meta-principle behind them.

### B. Learn by doing

Write code, ship code. Reading about how something works will only take you so far; doing it builds the model.

- Understand the **impact** of your work. Who is affected if this breaks? How quickly?
- Act with **appropriate caution** — small reversible changes for risky things, less ceremony for safe things.
- **Learn when you fail**, then move on. The failure is data; the wallowing isn't.

### C. Experiment with code

Run experiments to see how code *actually* works, not how you think it works.

- Throw an exception in a test. See where it propagates.
- Add a print statement and watch what happens.
- Print a stack trace at a suspicious spot.
- **Attach a debugger** and step through. Pause running code, see live threads, stack traces, variable values. If there's multithreading, watch how the threads interleave (or don't).
- Read what the standard library actually does instead of guessing.

These are tiny investments that pay back enormously. The engineers who experiment freely are the engineers who become unconsciously competent fastest.

### D. Read

Spend a portion of every week reading. Not occasionally — weekly. Sources, in rough priority for early career:

- **Team documentation** — the thing your team has written down about itself.
- **Design documents** — past and current. They show how decisions get made.
- **Code** — your codebase, *and* open-source code (especially libraries you use).
- **Ticket backlogs** — surprisingly rich. See below.
- **Books** — for going deep into a subject.
- **Papers** — when you want depth that books don't have, or current research.
- **Technical sites and blogs** — for trends and practitioner perspectives.

When you read, **pay attention to discussions of trade-offs and context.** Almost no engineering decision is "right" in the abstract — it's right for a context. Train your eye on which contexts make which choices reasonable.

#### Reading code (don't read it like a novel)

> *"Code never lies. Comments sometimes do."*

Code is the source of truth — comments and docs drift. Reading code is an active skill:

- **Use your IDE to navigate.** "Find usages," "go to definition," "find in repo" — these are how senior engineers move through a codebase. Click through, don't scroll.
- **Diagram control flow and states** for key operations. A pen-and-paper sketch of "what happens when a user clicks Submit" beats reading 30 files in your head.
- **Dig into data structures and algorithms.** When you hit something you don't recognize, pause and learn it.
- **Pay attention to edge case handling.** What does this code do when the input is empty? when the network fails? Edge cases reveal what the original author worried about.
- **Learn the local dialect.** Every codebase has idioms and style choices. Read a lot of code in one codebase before you write much, and your code will fit better.

Read open-source code too — particularly the libraries you use. You'll discover that most libraries are smaller and more readable than they look from the outside.

#### Reading tickets

Old tickets generally fall into three categories:

1. **No longer relevant** — close them or label them so.
2. **Useful but minor** — easy wins; great for a quiet afternoon.
3. **Important but too large to tackle right now** — the seeds of future projects. Read these for the *context* even if you can't act on them. They tell you what the team has been worried about.

#### Books vs. online resources

- **Books** are great for going deep into a subject. Slower to write, more carefully edited, longer-shelf-life ideas.
- **Online resources** are less trustworthy individually but great for keeping up with trends.
- Sometimes, **"it's good to be boring"** — the boring technology, the boring approach, the well-established way. Boring tools have known failure modes and big communities. Resist the pull to chase every shiny new framework.

Joining a **reading group** is one of the highest-leverage things you can do for keeping up with research in academia and industry. The discussion does as much teaching as the reading.

### E. Watch presentations

Tutorials, conference talks, internal tech talks, brown bags. Use them to:

- Get oriented in a new area faster than reading would.
- Hear a topic explained by someone who already understands it.
- Discover what "good" looks like in a domain.

Two practices that multiply the value:

- **Take notes** for retention.
- **Follow up on unfamiliar concepts or terms** — don't let them slip past unexamined. Each one is a candidate for the next thing to learn.

Go to internal **brown bags** if your company has them. The cost is one lunch; the network and learning compound.

### F. Attend meetups and conferences

Good for networking and discovering new ideas. **Don't overdo it** — conference attendance is fun but it's not the same as building competence.

- **Academic conferences** can have great content, but reading the papers and going to smaller, more focused gatherings is usually a better return.
- **Interest-based conferences** (a community around a language, framework, or practice) are great for practical tips and meeting experienced practitioners.
- **Vendor conferences** are the biggest and most visible — fun to attend but not really for learning. Calibrate expectations.

### G. Shadow and pair with experienced engineers

The fastest way to install someone else's instincts in your own head.

- **Shadowing** — watch them work. Ask them to narrate what they're thinking. (You'll be surprised how much is invisible until they say it out loud.)
- **Reverse shadowing** — they watch *you* work. They'll catch habits and gaps you can't see in yourself.
- **Pair programming** — actively code together, swap who's typing every 20–30 minutes. Done well, it's the highest-density learning available in engineering. Done poorly (one person types, the other watches), it's just a slow standup.

Don't be shy about asking for shadowing time. Most senior engineers are flattered to be asked and underused for this.

### H. Experiment with side projects

Build things on your own. Contribute to open source.

- **Find a problem you actually care about**, then solve it using the tools you want to learn. The "real" problem keeps you motivated through the boring middle of learning the tool.
- **Open source contributions** teach you to read other people's code, work async with strangers, and write at a higher quality bar than you might internally.

Two cautions worth taking seriously:

- **Don't use company resources or company time** for side projects. This is both an ethical line and a contractual one in most jobs.
- **Avoid side projects that compete with your company's product.** Even if you think it's fine, it can become a real legal mess later.

#### Important — IP ownership of side projects

Many employment contracts contain **IP assignment clauses** that quietly claim ownership of *anything you build*, even on your own time and machine, unless specifically carved out. This is a career-relevant detail most early engineers don't know to look for.

Before you put real effort into a side project:

- **Read your employment contract.** Look for "intellectual property," "inventions," or "work-for-hire" sections.
- If your contract is broad, **ask HR or your manager in writing** whether a specific side project is okay. Get the answer in writing too.
- If you're in a US state with a relevant statute (California has Labor Code 2870, Washington has similar), you may have more protection than the contract suggests — but check.
- For anything that might become valuable, **getting clarity up front is worth the slightly awkward conversation.**

This isn't paranoia — it's how engineers have lost ownership of years of work. Five minutes of contract-reading is cheap insurance.

---

## Callout — Using AI as a learning aid (not a replacement)

This assistant exists to make you a better engineer, not to do the engineering for you. The same principle applies to any AI tool you use — they can either accelerate your climb to conscious competence or trap you in unconscious incompetence with shipped code. The difference is in *how you prompt.*

A few moves that bias toward learning rather than shortcutting:

- **Ask "why," not just "what."** *"Why does this approach work and the other one doesn't?"* teaches; *"give me code that does X"* doesn't.
- **Ask for the trade-offs, not the answer.** *"What are the options here and what are the trade-offs of each?"* makes you the decider.
- **Ask it to explain back to you.** After you've written code, paste it and ask: *"What would break this in production?"* Cheaper than a postmortem.
- **Pair with it like a teammate**, not a vending machine. Tell it what you're trying to learn, not just what you want done.
- **Don't accept code you don't understand.** If the AI gives you something you couldn't write or maintain yourself, treat that as a signal you have something to learn — not as a finished answer.
- **Notice when you're cheating yourself.** If you find yourself copying answers without engaging, that's exactly the trap. Step away, do it the slow way once, come back.

The test: in six months, can you do what the AI helped you with today, *without* the AI? If yes, you used it for learning. If no, you used it for shortcutting.

---

## Output style

Follow the [Output Protocol](../../docs/METHODOLOGY.md#10-output-protocol). Specifically for this skill:

- **One question per turn.** Never ask the *what-are-you-learning* and *what-have-you-tried* questions in the same message.
- **Skip the diagnostic if the first message already answers it.** Many users give you the context unprompted; don't re-ask.
- **Surface 2–4 techniques** based on what they're trying to learn — don't dump the whole toolkit.
- **If they've tried things already, lean into techniques they haven't tried** rather than re-suggesting what they tried.
- For specific learning targets (e.g., "learn the codebase"), pull the most relevant subset of *Read*, *Experiment*, and *Pair* — skip side projects unless they bring it up.
- The four-stages callout fires when the user is genuinely unsure where they are in their learning, or when *"I don't know what I don't know"* is the actual problem.

## When NOT to use this skill

- The user has a tactical question — *help me write this code*, *debug this stack trace*. They want help finishing something, not a lecture about how to learn. Skip.
- The user is in active onboarding — route to [`new-team-onboarding`](../new-team-onboarding/SKILL.md), which has stage-specific advice.
- The user is mid-incident. Definitely skip; route to [`incident-response`](../incident-response/SKILL.md). Learning happens *after* the fire is out.
- The user is reflecting on growth in the four-pillars sense (am I getting better as an engineer overall) — route to [`growth-self-check`](../growth-self-check/SKILL.md). This skill is about *how to learn a thing*; that one is about *am I getting stronger*.

## Further reading

Surfaced as references but not yet folded in — see [`READING-LIST.md`](../../READING-LIST.md) for full entries.

- *Apprenticeship Patterns* — Hoover & Oshineye. Pattern language for the long climb to mastery.
- *Extreme Programming Explained* — Beck & Andres. Foundational on pair programming and many cross-cutting practices.
- *On Pair Programming* — Böckeler & Siessegger (martinfowler.com). Focused, practical guide to pairing well.
