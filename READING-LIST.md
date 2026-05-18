# Reading List

Books, articles, talks, and papers that inform (or should inform) this assistant. Collected primarily from each book chapter's **"Level Up"** section, plus other sources as they surface.

The list is honest about status. Most entries are *to read*, not yet absorbed. When something gets read and it changes how a skill should work, the entry gets a **Takeaways** section here and the relevant skill body gets updated — with this source properly cited there.

---

## How this list works

Each entry shows:

- **Title + author(s) / year** — the citation
- **Source** — where this reference came from (which chapter of which book, which conversation, which article)
- **Relates to** — which skill(s) in this assistant it would shape
- **Status** — one of:
  - **To read** — surfaced but not yet started
  - **Reading** — currently working through it
  - **Read** — finished; takeaways noted, but skill bodies not yet updated
  - **Folded** — read and integrated; the relevant skill body has been updated and cites this source
- **Why this matters here** — a sentence or two on what this is likely to contribute
- **Takeaways** (added once read) — the 3–7 things that changed my thinking

---

## Books

### All You Have to Do is Ask: How to Master the Most Important Skill for Success

- **Author:** Wayne Baker (2020)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`asking-for-help`](./skills/asking-for-help/SKILL.md)
- **Status:** To read
- **Why this matters here:** A book entirely on the practice of asking — for help, for advice, for what you need. The `asking-for-help` skill currently runs on one section of one chapter; this book is likely to deepen the framework substantially, especially around the social and cultural sides of asking.

### Apprenticeship Patterns: Guidance for the Aspiring Software Craftsman

- **Authors:** Dave Hoover, Adewale Oshineye (O'Reilly, 2009)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./skills/learning-toolkit/SKILL.md), possibly [`growth-self-check`](./skills/growth-self-check/SKILL.md)
- **Status:** To read
- **Why this matters here:** A pattern language for the long climb to mastery — concrete practices like "expose your ignorance," "kindred spirits," "find mentors," "expand your bandwidth." Should sharpen the `learning-toolkit` framing and may surface new patterns worth packaging as their own skills.

### Extreme Programming Explained: Embrace Change

- **Authors:** Kent Beck, Cynthia Andres (Addison-Wesley, 2nd ed. 2004)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./skills/learning-toolkit/SKILL.md) (pair programming), [`code-review`](./skills/code-review/SKILL.md) (collective code ownership, taste-building), [`operator-playbook`](./skills/operator-playbook/SKILL.md) (continuous integration, small releases)
- **Status:** To read
- **Why this matters here:** The foundational text for many modern engineering practices — pair programming, TDD, continuous integration, small releases, refactoring as discipline. Touches several skills. Probably the most cross-cutting book on this list.

### Presence: Bringing Your Boldest Self to Your Biggest Challenges

- **Author:** Amy Cuddy (Little, Brown Spark, 2015)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`growth-obstacles`](./skills/growth-obstacles/SKILL.md) (impostor syndrome)
- **Status:** To read
- **Why this matters here:** The embodied side of impostor syndrome — how posture, physical state, and small pre-game rituals can shift how you show up. *Note:* some of the power-pose research has had replication issues; the broader thesis about embodied self-trust still has supporting evidence and the book is worth reading critically.

### Working Effectively with Legacy Code

- **Author:** Michael C. Feathers (Prentice Hall, 2004)
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`changing-legacy-code`](./skills/changing-legacy-code/SKILL.md) (not Level Up; cited within the chapter's main content)
- **Relates to:** [`changing-legacy-code`](./skills/changing-legacy-code/SKILL.md), [`technical-debt`](./skills/technical-debt/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical text on safely changing existing code. The five-step algorithm and dependency-breaking techniques captured in `changing-legacy-code` come from this book, but the book itself goes far deeper — many seam-introducing techniques the skill doesn't yet capture, plus extended worked examples. Worth reading cover-to-cover.

---

## Articles

### How to Write a Git Commit Message

- **Author:** Chris Beams
- **URL:** https://chris.beams.io/posts/git-commit/
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`commit-and-pr-hygiene`](./skills/commit-and-pr-hygiene/SKILL.md) (not Level Up; cited within the chapter's main content)
- **Relates to:** [`commit-and-pr-hygiene`](./skills/commit-and-pr-hygiene/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical short essay on writing good commit messages. The seven rules embedded in `commit-and-pr-hygiene` come from this article. Beams' full argument has more nuance than the rules alone convey; worth reading in full at least once. Short — ~10 minutes.

### On Pair Programming

- **Authors:** Birgitta Böckeler, Nina Siessegger
- **URL:** https://www.martinfowler.com/articles/on-pair-programming.html
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./skills/learning-toolkit/SKILL.md) (pair programming technique)
- **Status:** To read
- **Why this matters here:** A focused, practical guide to doing pair programming well — much more depth than `learning-toolkit` currently has on this technique. Likely candidate for upgrading the pairing section of that skill, or for spinning out a focused `pair-programming` skill if it earns the volume.

---

## How references flow into skills

The intended pipeline:

1. **Surfaced** (here, with status "To read") — the reference is known and tagged to the relevant skill(s).
2. **Read** — status updated; Takeaways section added here with the 3–7 things that changed my thinking.
3. **Folded** — the relevant skill body is updated with the new material; the skill's `## Source` section adds this book to its citation list; status here is set to **Folded**.

The reason for keeping this separate from the skills (rather than padding skill bodies with unread references) is **honesty**: skills should reflect material that's actually shaped them, not material that *should* shape them eventually. Aspirational citations are a slow poison for trust in the skills — when the user goes back to a skill expecting depth and finds only what's been actually internalized, the skill stays trustworthy.
