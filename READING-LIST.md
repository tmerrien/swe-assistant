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
- **Relates to:** [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md)
- **Status:** To read
- **Why this matters here:** A book entirely on the practice of asking — for help, for advice, for what you need. The `asking-for-help` skill currently runs on one section of one chapter; this book is likely to deepen the framework substantially, especially around the social and cultural sides of asking.

### Apprenticeship Patterns: Guidance for the Aspiring Software Craftsman

- **Authors:** Dave Hoover, Adewale Oshineye (O'Reilly, 2009)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), possibly [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- **Status:** To read
- **Why this matters here:** A pattern language for the long climb to mastery — concrete practices like "expose your ignorance," "kindred spirits," "find mentors," "expand your bandwidth." Should sharpen the `learning-toolkit` framing and may surface new patterns worth packaging as their own skills.

### Building Secure & Reliable Systems

- **Authors:** Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield (Google, O'Reilly Media, 2020)
- **URL:** https://sre.google/books/building-secure-reliable-systems/ (free online)
- **Source:** *The Missing Readme*, Ch. 4 Level Up
- **Relates to:** [`input-validation`](./plugins/swe-assistant/skills/input-validation/SKILL.md) (security throughout), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md)
- **Status:** To read
- **Why this matters here:** The sequel to Google's *Site Reliability Engineering* book, focused specifically on the intersection of security and reliability — design principles, change management, incident response for security incidents, recovery, monitoring for both performance and attack signals. Available free online. Foundational reference for engineers building services that need to be both reliable and secure (which is most production services).

### Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation

- **Authors:** Jez Humble, David Farley (Addison-Wesley, 2010)
- **Source:** *The Missing Readme*, Ch. 8 Level Up
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (build pipelines, CI hygiene, releasing on every commit), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release cadence, publication automation), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md) (delivery pipeline framing), and the not-yet-written deploy/rollout skills
- **Status:** To read
- **Why this matters here:** The canonical practitioner text on modern delivery pipelines — the discipline of getting from a commit to a running production change quickly, safely, and reliably. Sources of much of the industry vocabulary around build pipelines, deployment pipelines, and the "release on every commit" ideal. Directly foundational for the CI hygiene material in `build-and-package` and the cadence material in `release-hygiene`; will further inform the deploy/rollout skills as they're written.

### Clean Code: A Handbook of Agile Software Craftsmanship

- **Author:** Robert C. Martin (Prentice Hall, 2008)
- **Source:** *The Missing Readme*, Ch. 4 Level Up
- **Relates to:** [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) (Boy Scout rule already attributed to Martin), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md)
- **Status:** To read
- **Why this matters here:** Canonical practitioner book on writing readable, maintainable code at the function and class level — naming, function size, comments, formatting, error handling. The Boy Scout Rule (*"leave the code cleaner than you found it"*) attributed to Martin is widely cited in this repository's skills. The full book covers much more than that one principle. Some of Martin's broader prescriptions are debated in the community; read critically.

### Code Complete (2nd edition)

- **Author:** Steve McConnell (Microsoft Press, 2004)
- **Source:** *The Missing Readme*, Ch. 4 Level Up
- **Relates to:** [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md) (extensive coverage), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md), [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md)
- **Status:** To read
- **Why this matters here:** Among the most comprehensive practitioner books on software construction. Covers defensive programming, naming, error handling, integration, testing, refactoring, debugging, code review, and project-management aspects of construction. 900+ pages; not a quick read, but referenced across an enormous range of working engineering contexts. Probably the single best book to read if you only get to read one foundational SWE text.

### Extreme Programming Explained: Embrace Change

- **Authors:** Kent Beck, Cynthia Andres (Addison-Wesley, 2nd ed. 2004)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md) (pair programming), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) (collective code ownership, taste-building), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md) (continuous integration, small releases)
- **Status:** To read
- **Why this matters here:** The foundational text for many modern engineering practices — pair programming, TDD, continuous integration, small releases, refactoring as discipline. Touches several skills. Probably the most cross-cutting book on this list.

### Git for Teams: A User-Centered Approach to Creating Efficient Workflows in Git

- **Author:** Emma Jane Hogbin Westby (O'Reilly, 2015)
- **Source:** *The Missing Readme*, Ch. 8 Level Up
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (team workflows shape what a good build looks like), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release-branch discipline, tagging conventions), [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md)
- **Status:** To read
- **Why this matters here:** Team-level version-control discipline — branching models, review workflows, release branches — that determines what CI is even asked to build. A team's Git conventions are effectively the contract the build pipeline enforces. Useful complement to `commit-and-pr-hygiene` (which is about individual-author discipline) at the team-workflow layer.

### The Legacy Code Programmer's Toolbox

- **Author:** Jonathan Boccara (2021)
- **Source:** *The Missing Readme*, Ch. 3 Level Up
- **Relates to:** [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md)
- **Status:** To read
- **Why this matters here:** A modern, pragmatic companion to Feathers' *Working Effectively with Legacy Code*. Covers practical techniques for understanding, navigating, and changing unfamiliar codebases — including material on reading code, refactoring under uncertainty, and the psychological side of legacy-code work that Feathers does not directly address. Likely to broaden `changing-legacy-code` with techniques beyond the original five-step algorithm.

### The Mythical Man-Month: Essays on Software Engineering

- **Author:** Frederick P. Brooks Jr. (Addison-Wesley, 1975; Anniversary Edition 1995)
- **Source:** *The Missing Readme*, Ch. 3 Level Up
- **Relates to:** [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md) (second-system effect, rewrites), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md) (project planning, Brooks's law), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md) (managing complexity)
- **Status:** To read
- **Why this matters here:** Foundational collection of essays on software engineering management. Two concepts in particular are directly applicable to existing-code work: **Brooks's law** (*"adding manpower to a late software project makes it later"*) and the **second-system effect** (the tendency to over-engineer the second version of a system once the first one's constraints are removed). The second-system effect is exactly the trap `change-discipline` warns about in its rewrite section. The Anniversary Edition adds the retrospective essay *"No Silver Bullet"* and its 1995 update, both worth reading.

### Presence: Bringing Your Boldest Self to Your Biggest Challenges

- **Author:** Amy Cuddy (Little, Brown Spark, 2015)
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md) (impostor syndrome)
- **Status:** To read
- **Why this matters here:** The embodied side of impostor syndrome — how posture, physical state, and small pre-game rituals can shift how you show up. *Note:* some of the power-pose research has had replication issues; the broader thesis about embodied self-trust still has supporting evidence and the book is worth reading critically.

### The Hard Thing About Hard Things: Building a Business When There Are No Easy Answers

- **Author:** Ben Horowitz (Harper Business, 2014)
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md) (not Level Up; cited within the chapter's main content)
- **Relates to:** [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md), [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** Source of the "10× better" rule used as the decision criterion across the change-discipline skills. The book is primarily about startup leadership but contains substantial material on engineering judgment, hard decisions, and the cost of switching — much of it directly applicable to technical decisions about rewrites, new technology adoption, and organizational change.

### Release It! Design and Deploy Production-Ready Software

- **Author:** Michael T. Nygard (Pragmatic Bookshelf, 2nd ed. 2018)
- **Source:** *The Missing Readme*, Ch. 8 Level Up
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (packaging for production; capacity and stability patterns start at the build), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release-repository choices and immutability), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md) (stability patterns), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md)
- **Status:** To read
- **Why this matters here:** The practitioner canon on making software survive contact with production — capacity patterns, stability patterns (circuit breaker, bulkhead, timeout, steady state), and the packaging/deployment/operations decisions that shape whether the software can be operated at all. The circuit-breaker pattern used in rollout skills traces to this book. The second edition (2018) is substantially updated for cloud-native and microservice architectures.

### Refactoring: Improving the Design of Existing Code

- **Author:** Martin Fowler (Addison-Wesley, 2nd ed. 2018)
- **Source:** *The Missing Readme*, Ch. 3 Level Up
- **Relates to:** [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) (refactoring catalog), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md) (code-smells vocabulary), [`software-entropy`](./plugins/swe-assistant/skills/software-entropy/SKILL.md) (recognizing patterns of decay)
- **Status:** To read
- **Why this matters here:** The canonical catalog of refactoring techniques. The second edition (2018) is updated to use JavaScript and modern tooling. Source of the "code smells" vocabulary — long method, duplicated code, feature envy, primitive obsession, and so on — that engineers use to recognize and discuss problems in existing code. Pairs naturally with Feathers' *Working Effectively with Legacy Code*: Fowler tells you *what* to refactor; Feathers tells you *how to do it safely when there are no tests*.

### Site Reliability Engineering: How Google Runs Production Systems

- **Editors:** Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (Google, O'Reilly 2016)
- **URL:** https://sre.google/sre-book/table-of-contents/ (free online)
- **Source:** *The Missing Readme*, Ch. 8 Level Up — also referenced from [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md)
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (release engineering), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release-engineering discipline as a formal role), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`metrics`](./plugins/swe-assistant/skills/metrics/SKILL.md), [`logging`](./plugins/swe-assistant/skills/logging/SKILL.md), [`tracing`](./plugins/swe-assistant/skills/tracing/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical text on running large-scale production systems. Chapter 8 (*"Release Engineering"*) formalizes release engineering as a discipline — reproducible builds, hermetic tooling, packaging and configuration policies, deployment. Also foundational for the three-pillars-of-observability framing used in `operator-playbook` and the dedicated observability skills. Free online; often the first book people recommend to engineers moving into operations.

### Explore It! Reduce Risk and Increase Confidence with Exploratory Testing

- **Author:** Elisabeth Hendrickson (Pragmatic Bookshelf, 2013)
- **Source:** *The Missing Readme*, Ch. 6 Level Up
- **Relates to:** [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md) (acceptance / exploratory test types), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md) (post-incident exploration), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) (exploratory thinking about edge cases)
- **Status:** To read
- **Why this matters here:** The canonical practitioner book on **exploratory testing** — the discipline of structured-but-improvisational testing that complements (rather than replaces) automated test suites. Hendrickson distinguishes exploration from ad-hoc poking around: it's chartered, time-boxed, and produces explicit findings. Important counterweight to the *"if it's not automated it doesn't count"* trap. Particularly useful for engineers who own a service and need to think about what could go wrong beyond what their unit tests already cover.

### The Pragmatic Programmer: Your Journey to Mastery

- **Authors:** Andrew Hunt, David Thomas (Addison-Wesley, 1999; 20th Anniversary Edition 2019)
- **Source:** *The Missing Readme*, Ch. 6 Level Up
- **Relates to:** [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md), [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md), [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md) — cross-cuts many skills
- **Status:** To read
- **Why this matters here:** One of the most-cited practitioner books in the field. Source of widely-used vocabulary (*"broken windows,"* *"DRY,"* *"orthogonality,"* *"tracer bullets,"* *"stone soup,"* *"prototypes,"* the *"pragmatic"* posture itself) that shows up across many of the skills in this repository. The 20th Anniversary Edition (2019) is the better starting point — substantially updated by the original authors, including modern material on testing, concurrency, and the engineer's relationship with their tools. Probably the second-most-cross-cutting book on this list, after *Code Complete*.

### Test-Driven Development: By Example

- **Author:** Kent Beck (Addison-Wesley, 2002)
- **Source:** *The Missing Readme*, Ch. 6 — primary citation in [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md) AND in the Ch. 6 Level Up reading list
- **Relates to:** [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md), [`mocking`](./plugins/swe-assistant/skills/mocking/SKILL.md) (TDD pressure on design naturally surfaces mocking decisions), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) (TDD discipline for bug fixes)
- **Status:** To read
- **Why this matters here:** The canonical text for test-driven development. Beck walks through TDD on two extended worked examples (a multi-currency money library, then the xUnit framework itself), demonstrating the red-green-refactor loop in enough detail to actually learn from. The book is short and focused; it is intended to be worked through, not just read. The `writing-tests` skill surfaces TDD as a useful default; this is the book to read to actually adopt the discipline.

### Thanks for the Feedback: The Science and Art of Receiving Feedback Well

- **Authors:** Douglas Stone, Sheila Heen (Penguin, 2014)
- **Source:** *The Missing Readme*, Ch. 7 Level Up
- **Relates to:** [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) (receive-side specifically), [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md) (the identity-trigger framing maps onto impostor-syndrome distortion), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md) (using feedback as data in self-assessment), [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md) (the related skill of asking for and metabolizing feedback)
- **Status:** To read
- **Why this matters here:** The companion volume to Stone & Heen's earlier *Difficult Conversations*, focused entirely on the receive side of feedback. The framework — three triggers that make feedback hard to hear (*truth* triggers: it's wrong; *relationship* triggers: from this person?; *identity* triggers: I'm not the kind of person who...) and concrete moves for hearing it well anyway — transfers directly to code review and to any growth-feedback context. The single most useful book on receiving feedback. The framing is well-known and frequently cited in performance-review and leadership-development contexts; less commonly cited in engineering-specific writing despite being directly applicable. Worth folding into the receive-side section of `code-review` once read.

### Unit Testing: Principles, Practices, and Patterns

- **Author:** Vladimir Khorikov (Manning, 2020)
- **Source:** *The Missing Readme*, Ch. 6 Level Up
- **Relates to:** [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md), [`mocking`](./plugins/swe-assistant/skills/mocking/SKILL.md), [`test-determinism`](./plugins/swe-assistant/skills/test-determinism/SKILL.md), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) (the book has substantial material on testing legacy code)
- **Status:** To read
- **Why this matters here:** A modern, opinionated practitioner book on unit testing that takes a strong position on the *style* of testing — preferring sociable tests over heavily-mocked solitary tests, emphasizing testing observable behavior rather than implementation details, and giving a rigorous treatment of the *"mock everything"* anti-pattern. Likely to sharpen all three Ch. 6 skills, especially `mocking` (Khorikov's treatment of test doubles is one of the most useful in the field) and `writing-tests` (the four-pillar test quality framework — protection against regressions, resistance to refactoring, fast feedback, maintainability). C#-flavored in code examples but conceptually language-agnostic.

### Working Effectively with Legacy Code

- **Author:** Michael C. Feathers (Prentice Hall, 2004)
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md) (cited within the chapter's main content) AND in the Ch. 3 Level Up reading list
- **Relates to:** [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical text on safely changing existing code. The five-step algorithm and dependency-breaking techniques captured in `changing-legacy-code` come from this book, but the book itself goes far deeper — many seam-introducing techniques the skill doesn't yet capture, plus extended worked examples. Worth reading cover-to-cover.

---

## Articles, Specs, and Talks

### Amazon Builder's Library

- **Publisher:** Amazon Web Services (ongoing collection)
- **URL:** https://aws.amazon.com/builders-library
- **Source:** *The Missing Readme*, Ch. 4 Level Up and Ch. 8 Level Up
- **Relates to:** [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md), [`metrics`](./plugins/swe-assistant/skills/metrics/SKILL.md), [`configuration`](./plugins/swe-assistant/skills/configuration/SKILL.md), [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md)
- **Status:** To read
- **Why this matters here:** A curated collection of essays by Amazon principal engineers on how AWS actually builds and operates production systems at scale. Notable essays include *"Timeouts, retries, and backoff with jitter"* (foundational for the `retry-and-backoff` skill — likely already informed industry practice that skill cites), *"Avoiding fallback in distributed systems,"* *"Avoiding insurmountable queue backlogs,"* *"Caching challenges and strategies,"* *"Making retries safe with idempotent APIs."* Free, frequently updated. Probably the best single web resource for learning how large-scale services are built and operated by people who do it for a living.

### Choose Boring Technology

- **Author:** Dan McKinley
- **URL:** http://boringtechnology.club/
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md) (not Level Up; cited within the chapter's main content)
- **Relates to:** [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md), [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md)
- **Status:** To read
- **Why this matters here:** Foundational essay/talk on technology adoption discipline in engineering teams. Source of the "innovation tokens" vocabulary used in `choose-boring-technology`. Short read; the essay form crystallizes the argument in a way the skill body doesn't fully capture. The talk version (linked from the site) covers additional ground.

### Google's Code Review Developer Guide

- **Publisher:** Google (open-sourced, ongoing)
- **URL:** https://google.github.io/eng-practices/review/
- **Source:** *The Missing Readme*, Ch. 7 Level Up — also a primary citation in [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md)
- **Relates to:** [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md), [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md), [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md) (the standards section maps onto design-review thinking)
- **Status:** To read
- **Why this matters here:** The most comprehensive public practitioner reference on running code reviews at scale, written from Google's experience reviewing hundreds of thousands of CLs per week. Split into two halves — *The Code Reviewer's Guide* and *The Change Author's Guide* — that map almost exactly onto Mode A / Mode B in `code-review`. The framing *"approve once the change improves code health, even if it isn't perfect"* (from https://google.github.io/eng-practices/review/reviewer/standard.html) is the single most useful disposition for resolving the chronic *"is this good enough to approve?"* tension. Free and short by book standards.

### How to Write a Git Commit Message

- **Author:** Chris Beams
- **URL:** https://chris.beams.io/posts/git-commit/
- **Source:** *The Missing Readme*, Ch. 3 — primary citation in [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) (not Level Up; cited within the chapter's main content)
- **Relates to:** [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical short essay on writing good commit messages. The seven rules embedded in `commit-and-pr-hygiene` come from this article. Beams' full argument has more nuance than the rules alone convey; worth reading in full at least once. Short — ~10 minutes.

### On Pair Programming

- **Authors:** Birgitta Böckeler, Nina Siessegger
- **URL:** https://www.martinfowler.com/articles/on-pair-programming.html
- **Source:** *The Missing Readme*, Ch. 2 Level Up
- **Relates to:** [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md) (pair programming technique)
- **Status:** To read
- **Why this matters here:** A focused, practical guide to doing pair programming well — much more depth than `learning-toolkit` currently has on this technique. Likely candidate for upgrading the pairing section of that skill, or for spinning out a focused `pair-programming` skill if it earns the volume.

### Semantic Versioning (SemVer) — the spec

- **Authors:** Tom Preston-Werner et al. (specification, currently at 2.0.0)
- **URL:** https://semver.org
- **Source:** *The Missing Readme*, Ch. 5 Level Up — and the primary citation in [`dependency-management`](./plugins/swe-assistant/skills/dependency-management/SKILL.md)
- **Relates to:** [`dependency-management`](./plugins/swe-assistant/skills/dependency-management/SKILL.md), [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md) (breaking changes are versioning events), [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md) (some teams tie commit conventions to SemVer bumps)
- **Status:** To read
- **Why this matters here:** The shared vocabulary the rest of the industry uses for versioning libraries: `MAJOR.MINOR.PATCH`, with strict rules about what each segment promises. Short, well-written, worth knowing by heart. Most package-manager conflict-resolution behavior assumes consumers understand SemVer; not knowing the spec is a quiet source of dependency-hell bugs.

### PEP 440 — Version Identification and Dependency Specification (Python)

- **Author:** Nick Coghlan, Donald Stufft (Python Software Foundation)
- **URL:** https://www.python.org/dev/peps/pep-0440/
- **Source:** *The Missing Readme*, Ch. 5 Level Up
- **Relates to:** [`dependency-management`](./plugins/swe-assistant/skills/dependency-management/SKILL.md) (Python ecosystem specifically)
- **Status:** To read
- **Why this matters here:** Python's authoritative versioning standard. Shares SemVer's basic shape (`MAJOR.MINOR.MICRO`) but adds Python-specific concepts: epochs (`1!2.0`), pre-releases (`1.0a1`, `1.0b1`, `1.0rc1`), post-releases (`1.0.post1`), and developmental releases (`1.0.dev1`). Required reading for anyone publishing to PyPI or pinning Python dependencies seriously.

---

## How references flow into skills

The intended pipeline:

1. **Surfaced** (here, with status "To read") — the reference is known and tagged to the relevant skill(s).
2. **Read** — status updated; Takeaways section added here with the 3–7 things that changed my thinking.
3. **Folded** — the relevant skill body is updated with the new material; the skill's `## Source` section adds this book to its citation list; status here is set to **Folded**.

The reason for keeping this separate from the skills (rather than padding skill bodies with unread references) is **honesty**: skills should reflect material that's actually shaped them, not material that *should* shape them eventually. Aspirational citations are a slow poison for trust in the skills — when the user goes back to a skill expecting depth and finds only what's been actually internalized, the skill stays trustworthy.
