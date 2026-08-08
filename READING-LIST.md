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

### An Elegant Puzzle: Systems of Engineering Management

- **Author:** Will Larson (Stripe Press, 2019)
- **Source:** *The Missing Readme*, Ch. 13 Level Up
- **Relates to:** [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md)
- **Status:** To read
- **Why this matters here:** How engineering organizations actually decide things — team sizing and shape, headcount, migrations, how work gets prioritized across groups. Written for managers, and useful to an individual contributor precisely for that reason: it makes legible the constraints your manager is operating inside, which is most of what turns "my manager said no" into a negotiable conversation. Larson's material on organizational debt is a good companion to `technical-debt`.

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

### A Philosophy of Software Design

- **Author:** John Ousterhout (Yaknyam Press, 2018; 2nd ed. 2021)
- **Source:** *The Missing Readme*, Ch. 11 — the chapter adopts this book's definition of complexity outright, and Ch. 11 Level Up
- **Relates to:** [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`software-entropy`](./plugins/swe-assistant/skills/software-entropy/SKILL.md), [`technical-debt`](./plugins/swe-assistant/skills/technical-debt/SKILL.md), [`changing-legacy-code`](./plugins/swe-assistant/skills/changing-legacy-code/SKILL.md)
- **Status:** To read
- **Why this matters here:** The definitional anchor for `managing-complexity`. Ousterhout defines complexity as *anything related to the structure of a system that makes it hard to understand and modify* — consequence-based rather than metric-based — and decomposes its symptoms into **dependency** and **obscurity**. Also the source of "deep modules" (simple interface, substantial implementation) and a sharp argument that comments are part of the design rather than an afterthought. Short, opinionated, and directly contradicts *Clean Code* in places, which makes reading both worthwhile. **Priority read** — a skill in this repository currently rests on a book that has not been read end to end.

### High Output Management

- **Author:** Andrew S. Grove (Random House, 1983; reissued 1995)
- **Source:** *The Missing Readme*, Ch. 13 Level Up — also cited in [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- **Relates to:** [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md), [`contributor-playbook`](./plugins/swe-assistant/skills/contributor-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** The origin of both practices `working-with-managers` is built on. Grove invented what became **OKRs** at Intel, and treats the **1:1** as the manager's single highest-leverage activity — worth reading for the argument that the meeting belongs to the *subordinate*, which is exactly the framing the skill takes. Also the source of the "managerial leverage" idea that explains why your manager behaves as they do. Forty years old and still the most-recommended management book in the industry.

### Building Evolutionary Architectures

- **Authors:** Neal Ford, Rebecca Parsons, Patrick Kua (O'Reilly, 2017; 2nd ed. 2022)
- **Source:** *The Missing Readme*, Ch. 11 Level Up
- **Relates to:** [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`evolvable-apis`](./plugins/swe-assistant/skills/evolvable-apis/SKILL.md), [`evolvable-data`](./plugins/swe-assistant/skills/evolvable-data/SKILL.md), [`change-discipline`](./plugins/swe-assistant/skills/change-discipline/SKILL.md)
- **Status:** To read
- **Why this matters here:** Architecture designed for continuous change rather than for a predicted end state — the book-length version of Ch. 11's premise. Notable contribution is the **fitness function**: an automated, executable check that guards an architectural property (coupling limits, latency budgets, compatibility) the way a test guards behaviour. That idea is missing from this repository's skills and would strengthen all three Ch. 11 skills if folded in.

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
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (build pipelines, CI hygiene, releasing on every commit), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release cadence, publication automation), [`deployment-discipline`](./plugins/swe-assistant/skills/deployment-discipline/SKILL.md) (automated deploy pipelines end-to-end), [`progressive-rollout`](./plugins/swe-assistant/skills/progressive-rollout/SKILL.md) (canary and blue/green ramps as extensions of the deployment pipeline), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md) (delivery pipeline framing)
- **Status:** To read
- **Why this matters here:** The canonical practitioner text on modern delivery pipelines — the discipline of getting from a commit to a running production change quickly, safely, and reliably. Sources of much of the industry vocabulary around build pipelines, deployment pipelines, and the "release on every commit" ideal. Foundational for the CI hygiene material in `build-and-package`, the cadence material in `release-hygiene`, the automation-first framing in `deployment-discipline`, and the canary/blue-green patterns in `progressive-rollout`.

### A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives

- **Editors:** Lorin W. Anderson, David R. Krathwohl (Eds.) (Longman, 2001)
- **Source:** Referenced in the [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) skill for the revised-taxonomy levels (evaluate, create) that Socratic dialogue exercises
- **Relates to:** [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical revision of Bloom's 1956 taxonomy. Distinguishes the *knowledge* dimension from the *cognitive process* dimension, and names the highest-order thinking levels (analyze, evaluate, create) that active-defense practices like Socratic dialogue exercise. Provides a defensible vocabulary for talking about *what kind of understanding* a skill is targeting.

### Data Mesh: Delivering Data-Driven Value at Scale

- **Author:** Zhamak Dehghani (O'Reilly, 2022)
- **Source:** *The Missing Readme*, Ch. 11 Level Up
- **Relates to:** [`evolvable-data`](./plugins/swe-assistant/skills/evolvable-data/SKILL.md)
- **Status:** To read
- **Why this matters here:** The full architectural treatment of the **data product** idea that `evolvable-data` uses as its answer to shared-database coupling — treating published data as a deliberately-designed, owned, versioned product with a contract, rather than a byproduct other teams scrape from your internal tables. Data mesh as a whole is an organisational proposal aimed at large companies and is genuinely contested; the data-product-as-contract concept is the portable part and is useful at any scale.

### The Manager's Path

- **Author:** Camille Fournier (O'Reilly, 2017)
- **Source:** *The Missing Readme*, Ch. 13 Level Up — also cited in [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- **Relates to:** [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md), [`contributor-playbook`](./plugins/swe-assistant/skills/contributor-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** Structured as a ladder from being managed through to senior leadership, which means **the first chapter is written directly for an individual contributor** — what to expect from a manager, what a good 1:1 looks like from the other side, what to ask for and when. The most useful single chapter an early-career engineer can read on this relationship, and the rest of the book explains where your manager's incentives come from.

### The Staff Engineer's Path

- **Author:** Tanya Reilly (O'Reilly, 2022)
- **Source:** Owned by the maintainer; selected to address the career-arc gap recorded in [`docs/LIMITATIONS.md`](./docs/LIMITATIONS.md), Section 7a
- **Relates to:** [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md), [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md)
- **Status:** To read — **next up**
- **Why this matters here:** The most direct fix available for this repository's largest structural gap. [`JOURNEY.md`](./JOURNEY.md) inherits a five-stage map from *The Missing Readme* that stops at roughly senior; Reilly's book is the staff-and-beyond arc, organised around three pillars — the big picture, execution, and levelling up others — that map onto territory `owner-playbook` currently only gestures at. Also covers the parts of staff-plus work that have no home here at all: influence without authority, choosing what *not* to work on, and the shift from doing the work to setting technical direction.

### Designing Interfaces

- **Authors:** Jenifer Tidwell, Charles Brewer, Aynne Valencia (O'Reilly, 3rd ed. 2020)
- **Source:** Owned by the maintainer
- **Relates to:** speculative — no current skill covers interface design. Nearest neighbours are [`operational-tools`](./plugins/swe-assistant/skills/operational-tools/SKILL.md) (developer- and operator-facing UX) and [`evolvable-apis`](./plugins/swe-assistant/skills/evolvable-apis/SKILL.md) (API surface as an interface)
- **Status:** To read
- **Why this matters here:** A catalogue of UI patterns with the reasoning behind each. **Folding it in would be a deliberate scope change**, not an extension — [`docs/LIMITATIONS.md`](./docs/LIMITATIONS.md) Section 8 currently states the project's scope as software engineering only. Worth reading regardless for anyone building product surfaces; worth noting that McKinsey's 2025 PDLC analysis argues UI-pattern knowledge in isolation is the *depreciating* half of design skill while UX judgment appreciates, so read it as vocabulary rather than as the durable core.

### Universal Principles of UX

- **Author:** Irene Pereyra (Rockport, 2023)
- **Source:** Owned by the maintainer
- **Relates to:** speculative — same scope question as *Designing Interfaces*, but the better first read of the two
- **Status:** To read
- **Why this matters here:** One hundred UX principles, each presented atomically with an example. **Structurally, that is almost exactly this repository's skill format** — a principle, the situation it applies to, and why — which makes it the most fold-able of the design books by some distance. If the project ever extends into product surfaces, this is the entry point: principles before patterns, and per the McKinsey analysis the more durable half of the discipline.

### Code Crafted — Generative Design in Branding

- **Author:** *(entry incomplete — publisher and author not yet confirmed)*
- **Source:** Owned by the maintainer
- **Relates to:** speculative — furthest from the current scope of any book on this list
- **Status:** To read
- **Why this matters here:** Generative and computational approaches to brand systems. The honest assessment is that this is the least likely of the four to fold into a software-engineering skill set, and the most likely to be worth reading for its own sake. If a connection emerges it is probably methodological rather than topical — generative design and situation-triggered skills are both attempts to encode judgment as a system that produces variation rather than a fixed output. That is a thin thread and should not be forced.

### The Creative Act: A Way of Being

- **Author:** Rick Rubin (Penguin, 2023)
- **Source:** Recommended to the maintainer personally; added here with the fit deliberately marked uncertain
- **Relates to:** possibly [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md) (the *give it time* material), possibly [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- **Status:** To read
- **Why this matters here:** **Uncertain, and recorded as uncertain on purpose.** Rubin's book is aphoristic and deliberately non-prescriptive, which sits badly against this repository's Design Principle 3.5 (*skill bodies are operational, not literary*) and its requirement that every claim trace to something actionable. It is unlikely to fold cleanly and should not be forced. The one place it plausibly touches is the conditions for creative work — protected time, unhurried thinking, the tolerance for not-knowing — which `technical-design-process` already covers via Graham's *Maker's Schedule* and Hickey's *Hammock Driven Development*. Read for its own sake; fold only if something specific and operational actually lands.

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

### The Elements of Style

- **Authors:** William Strunk Jr., E. B. White (4th ed., Longman, 1999; first published 1918)
- **Source:** *The Missing Readme*, Ch. 10 Level Up
- **Relates to:** [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md)
- **Status:** To read
- **Why this matters here:** The shortest respectable book on English prose style — under 100 pages, and the source of *"omit needless words."* Its value for engineers is concision: design documents fail more often from being too long to read than from being too short. Some of its grammatical prescriptions are dated and contested by linguists; read it for the editing instinct, not as law.

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

### On Writing Well: The Classic Guide to Writing Nonfiction

- **Author:** William Zinsser (30th Anniversary Edition, HarperCollins, 2006; first published 1976)
- **Source:** *The Missing Readme*, Ch. 10 Level Up
- **Relates to:** [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md)
- **Status:** To read
- **Why this matters here:** The standard book on nonfiction writing, and a warmer, more practical companion to Strunk & White. Zinsser's central themes — clarity, simplicity, ruthless removal of clutter, and writing for a reader rather than to impress — map almost directly onto what makes a design document actually get read. Includes a chapter on writing about science and technology specifically, aimed at exactly the engineer who thinks they can't write.

### Managing Up: How to Move Up, Win at Work, and Succeed with Any Type of Boss

- **Author:** Mary Abbajay (Wiley, 2018)
- **Source:** *The Missing Readme*, Ch. 13 Level Up
- **Relates to:** [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md), [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md)
- **Status:** To read
- **Why this matters here:** A full treatment of the managing-up material `working-with-managers` compresses into one step. Organized around adapting to *types* of manager — absent, micromanaging, indecisive — which is the practical question an engineer actually faces, since you rarely get to choose. Read critically: the genre tends toward the anecdotal, and the advice is strongest where it is most concrete.

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
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (packaging for production; capacity and stability patterns start at the build), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release-repository choices and immutability), [`deployment-discipline`](./plugins/swe-assistant/skills/deployment-discipline/SKILL.md) (cloud-native deploy topologies and stability patterns at deploy time), [`progressive-rollout`](./plugins/swe-assistant/skills/progressive-rollout/SKILL.md) (the canonical modern treatment of the circuit-breaker pattern), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md) (stability patterns), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md)
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
- **Source:** *The Missing Readme*, Ch. 8 Level Up **and Ch. 9 Level Up** (which points specifically at SRE chapters 4, 11, 13, 14, and 15) — also referenced from [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md)
- **Relates to:** [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md) (release engineering), [`release-hygiene`](./plugins/swe-assistant/skills/release-hygiene/SKILL.md) (release-engineering discipline as a formal role), [`deployment-discipline`](./plugins/swe-assistant/skills/deployment-discipline/SKILL.md) (automated, atomic, independent deploys), [`progressive-rollout`](./plugins/swe-assistant/skills/progressive-rollout/SKILL.md) (SLIs as the rollout-monitoring signal), [`on-call-shift`](./plugins/swe-assistant/skills/on-call-shift/SKILL.md) (Ch. 4 for SLI/SLO/SLA, Ch. 11 for on-call as a discipline), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md) (Ch. 13–15 for emergency response, incident management, postmortem culture), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`metrics`](./plugins/swe-assistant/skills/metrics/SKILL.md), [`logging`](./plugins/swe-assistant/skills/logging/SKILL.md), [`tracing`](./plugins/swe-assistant/skills/tracing/SKILL.md)
- **Status:** To read
- **Why this matters here:** The canonical text on running large-scale production systems. Chapter 8 (*"Release Engineering"*) formalizes release engineering as a discipline — reproducible builds, hermetic tooling, packaging and configuration policies, deployment. Chapter 4 (*"Service Level Objectives"*) is the authoritative treatment of the SLI/SLO/SLA distinction; Chapter 11 (*"Being On-Call"*) is the best single treatment of on-call as a discipline in print; Chapters 13–15 (*Emergency Response*, *Managing Incidents*, *Postmortem Culture*) cover the incident lifecycle end-to-end. Also foundational for the three-pillars-of-observability framing used in `operator-playbook`. Free online; often the first book people recommend to engineers moving into operations. **Priority read** — it is now the most-cited unread source in this repository.

### Domain-Driven Design / Implementing Domain-Driven Design

- **Authors:** Eric Evans (Addison-Wesley, 2003); Vaughn Vernon (Addison-Wesley, 2013)
- **Source:** *The Missing Readme*, Ch. 11 — Evans cited in-chapter, Vernon in Ch. 11 Level Up
- **Relates to:** [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md), [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md)
- **Status:** To read
- **Why this matters here:** The architectural approach behind "encapsulate domain knowledge" — mapping software boundaries onto business domains. Evans (the "blue book") is the original and is dense; **Vernon is the more practical entry point** and is the one the chapter's Level Up list points to. The chapter's own position is worth preserving: full DDD is warranted only for genuinely complex domains, but the core vocabulary — bounded contexts, ubiquitous language, aggregates — sharpens boundary decisions long before anyone adopts the whole methodology.

### Designing Data-Intensive Applications

- **Author:** Martin Kleppmann (O'Reilly, 2017)
- **Source:** *The Missing Readme*, Ch. 11 Level Up
- **Relates to:** [`evolvable-data`](./plugins/swe-assistant/skills/evolvable-data/SKILL.md), [`evolvable-apis`](./plugins/swe-assistant/skills/evolvable-apis/SKILL.md), [`idempotency`](./plugins/swe-assistant/skills/idempotency/SKILL.md), [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md), [`configuration`](./plugins/swe-assistant/skills/configuration/SKILL.md)
- **Status:** To read
- **Why this matters here:** The standard modern reference on data systems. **Chapter 4, "Encoding and Evolution,"** is the direct anchor for both Ch. 11 skills: it works through backward and forward compatibility across Avro, Protocol Buffers, and Thrift, and makes explicit the point those two skills are built on — that **stored data and service APIs are the same evolution problem**. The rest of the book (replication, partitioning, transactions, consistency, stream processing) is the best available grounding for anyone whose systems outgrow a single database. **Priority read**, alongside the SRE book.

### Elements of Clojure

- **Author:** Zachary Tellman (self-published, 2019)
- **Source:** *The Missing Readme*, Ch. 11 Level Up
- **Relates to:** [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md)
- **Status:** To read
- **Why this matters here:** Despite the title, largely a book about naming, indirection, and abstraction as tools for managing complexity — the Clojure is a vehicle rather than the subject. Unusually rigorous on *why* a name is good or bad and on when indirection earns its cost, which is exactly the judgment `managing-complexity` tries to scaffold. Worth reading by engineers who will never write Clojure.

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
- **Relates to:** [`code-review`](./plugins/swe-assistant/skills/code-review/SKILL.md) (receive-side specifically), [`working-with-managers`](./plugins/swe-assistant/skills/working-with-managers/SKILL.md) (performance reviews), [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md) (the identity-trigger framing maps onto impostor-syndrome distortion), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md) (using feedback as data in self-assessment), [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md) (the related skill of asking for and metabolizing feedback)
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

### The Agile Manifesto (and the twelve principles behind it)

- **Authors:** Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin Fowler, et al. (2001)
- **URLs:** https://agilemanifesto.org · principles: https://agilemanifesto.org/principles.html
- **Source:** *The Missing Readme*, Ch. 12 — quoted in-chapter and in Ch. 12 Level Up
- **Relates to:** [`agile-planning`](./plugins/swe-assistant/skills/agile-planning/SKILL.md), [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md), [`contributor-playbook`](./plugins/swe-assistant/skills/contributor-playbook/SKILL.md), [`owner-playbook`](./plugins/swe-assistant/skills/owner-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** Four value statements and twelve supporting principles, together shorter than a page. The **principles page is the more useful document and the far less read one** — it is the source of the retrospective principle used in `team-rituals`, and several principles describe things teams claim to believe and do not practice. Worth reading for the closing qualifier alone: *while there is value in the items on the right, we value the items on the left more* — the right-hand items are not dismissed, which is precisely how the manifesto is most often misused. Ten minutes total.

### Atlassian Agile Coach

- **Publisher:** Atlassian (ongoing documentation)
- **URL:** https://www.atlassian.com/agile
- **Source:** *The Missing Readme*, Ch. 12 Level Up
- **Relates to:** [`agile-planning`](./plugins/swe-assistant/skills/agile-planning/SKILL.md), [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md)
- **Status:** To read
- **Why this matters here:** The most accessible free practical reference on Scrum and Kanban mechanics — how to run each ceremony, how boards and WIP limits work, how backlogs are groomed. The **Kanban material is particularly good** and is the recommended starting point for a team moving that way. Vendor documentation, so read the tooling recommendations with the obvious caveat; the process explanations are sound and vendor-neutral. The chapter's own note is worth keeping: most agile *books* are overkill for an individual engineer, being exhaustive across variants and written for project and program managers.

### Agile Retrospectives: Making Good Teams Great

- **Authors:** Esther Derby, Diana Larsen (Pragmatic Bookshelf, 2006)
- **Source:** Cited in [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md) and [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md) for the retrospective/individual-growth boundary
- **Relates to:** [`team-rituals`](./plugins/swe-assistant/skills/team-rituals/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md) (postmortems are a related but distinct ritual)
- **Status:** To read
- **Why this matters here:** The standard reference on facilitating retrospectives. Source of the five-stage structure (set the stage, gather data, generate insights, decide what to do, close) and a catalogue of activities worth rotating through when a team's retro has gone stale and everyone is bored of the same three columns. Also the clearest statement of the boundary both skills above enforce: retrospectives address **team process**, not individual performance.

### Valve Handbook for New Employees

- **Publisher:** Valve Corporation (2012)
- **URL:** widely mirrored; commonly cited from https://www.valvesoftware.com/en/publications
- **Source:** *The Missing Readme*, Ch. 14 — the T-shaped skills frame
- **Relates to:** [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), [`contributor-playbook`](./plugins/swe-assistant/skills/contributor-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** Source of the **T-shaped** frame folded into `growth-self-check` — breadth across many valuable skills (the bar) plus expert depth in one narrow discipline (the stem), with Valve naming the failure mode for each half. Worth reading in full and critically: it is a recruiting and culture document for one unusually structured company (flat, no managers, desks on wheels), so its claims about how work should be organized do not transfer to most employers. The T-shape itself does. Note the internal tension the skill preserves — Valve also states that collaboration traits matter *more* than deep domain knowledge, which sits awkwardly beside the vertical stem.

### Amazon Builder's Library

- **Publisher:** Amazon Web Services (ongoing collection)
- **URL:** https://aws.amazon.com/builders-library
- **Source:** *The Missing Readme*, Ch. 4 Level Up and Ch. 8 Level Up
- **Relates to:** [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md), [`retry-and-backoff`](./plugins/swe-assistant/skills/retry-and-backoff/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`defensive-programming`](./plugins/swe-assistant/skills/defensive-programming/SKILL.md), [`metrics`](./plugins/swe-assistant/skills/metrics/SKILL.md), [`configuration`](./plugins/swe-assistant/skills/configuration/SKILL.md), [`build-and-package`](./plugins/swe-assistant/skills/build-and-package/SKILL.md), [`deployment-discipline`](./plugins/swe-assistant/skills/deployment-discipline/SKILL.md), [`progressive-rollout`](./plugins/swe-assistant/skills/progressive-rollout/SKILL.md)
- **Status:** To read
- **Why this matters here:** A curated collection of essays by Amazon principal engineers on how AWS actually builds and operates production systems at scale. Notable essays include *"Timeouts, retries, and backoff with jitter"* (foundational for the `retry-and-backoff` skill — likely already informed industry practice that skill cites), *"Avoiding fallback in distributed systems,"* *"Avoiding insurmountable queue backlogs,"* *"Caching challenges and strategies,"* *"Making retries safe with idempotent APIs."* Free, frequently updated. Probably the best single web resource for learning how large-scale services are built and operated by people who do it for a living.

### What Happens When the Pager Goes Off?

- **Publisher:** *Increment* magazine (Stripe), on-call issue
- **URL:** https://increment.com/on-call/when-the-pager-goes-off/
- **Source:** *The Missing Readme*, Ch. 9 Level Up
- **Relates to:** [`on-call-shift`](./plugins/swe-assistant/skills/on-call-shift/SKILL.md), [`incident-response`](./plugins/swe-assistant/skills/incident-response/SKILL.md), [`operator-playbook`](./plugins/swe-assistant/skills/operator-playbook/SKILL.md)
- **Status:** To read
- **Why this matters here:** Practitioner accounts of what being paged actually feels like and what teams actually do in the first minutes, gathered across several companies with different scales and cultures. Valuable precisely because it is descriptive rather than prescriptive — it shows the *variance* in real on-call practice, which is a useful corrective to reading any single company's playbook (including Google's) as the universal standard. Short; a good first read before the SRE book's on-call chapters.

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

### Public design-proposal archives — PEPs, KIPs, and Rust RFCs

- **Publishers:** Python Software Foundation; Apache Kafka; the Rust project (all ongoing)
- **URLs:** https://peps.python.org/ · https://cwiki.apache.org/confluence/display/KAFKA/Kafka+Improvement+Proposals · https://github.com/rust-lang/rfcs
- **Source:** *The Missing Readme*, Ch. 10 — surfaced as worked examples of design documents
- **Relates to:** [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md)
- **Status:** To read
- **Why this matters here:** Three large archives of real design documents written in the open, by communities that conduct technical design publicly. Unlike a template, these show *finished* proposals at varying quality, and — because the discussion threads are preserved — the objections each one survived. That makes them the best available calibration for depth, tone, and how much detail a section actually needs. Rust RFCs are notable for requiring explicit *Drawbacks* and *Rationale and alternatives* sections in every proposal; KIPs for their attention to compatibility and migration; PEPs for house-style discipline across decades. Reading three or four, discussion included, is worth more than reading another article about how to write design docs.

### Hammock Driven Development

- **Author:** Rich Hickey (2010, talk)
- **URL:** https://youtu.be/f84n5oFoZBc
- **Source:** *The Missing Readme*, Ch. 10 Level Up — which points specifically at the *"Field Report"* portion
- **Relates to:** [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md)
- **Status:** To read
- **Why this matters here:** Hickey's talk on deliberately thinking a problem through before writing code — gathering facts, surveying prior art, identifying what you don't know, and then letting the problem sit (the "hammock") so the background mind can work on it. The single best available argument that unhurried thinking is *engineering work* rather than the absence of it, which is precisely the case an early-career engineer struggles to make to themselves and to their manager. Pairs naturally with Graham's *Maker's Schedule*.

### How an AI-Enabled Software Product Development Life Cycle Will Fuel Innovation

- **Authors:** Chandra Gnanasambandam, Martin Harrysson, Rikki Singh, with Aditi Chawla (McKinsey & Company, February 2025)
- **URL:** https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/how-an-ai-enabled-software-product-development-life-cycle-will-fuel-innovation
- **Source:** Surfaced in conversation; PDF saved locally
- **Relates to:** [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md) (which skills appreciate), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md), [`writing-tests`](./plugins/swe-assistant/skills/writing-tests/SKILL.md) and [`on-call-shift`](./plugins/swe-assistant/skills/on-call-shift/SKILL.md) (roles the article predicts will change)
- **Status:** Read
- **Why this matters here:** Consultancy analysis of how AI reshapes the software product development life cycle. Useful for calibrating what to learn, with one important correction to how it is usually summarised: **the role convergence it describes runs toward product managers, not engineers.** It predicts the PM role subsuming product marketing, product owner, technical product manager, and UI/UX positions, with PMs building technical POCs directly. For engineers it predicts something narrower — rising demand for senior/staff judgment able to review AI-generated code, a push toward full-stack plus business literacy, declining demand for UI-only skills alongside rising demand for UX research, and SDET and some SRE work being absorbed elsewhere. Read critically: it is vendor-adjacent thought leadership built on interviews rather than measurement, and it openly leaves the biggest question open — if AI absorbs junior work, how the next generation of senior engineers gets trained is "still to be determined."

### Maker's Schedule, Manager's Schedule

- **Author:** Paul Graham (2009)
- **URL:** http://www.paulgraham.com/makersschedule.html
- **Source:** *The Missing Readme*, Ch. 10 — cited within the chapter's *Give it Time* section, and a primary citation in [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md)
- **Relates to:** [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md), [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- **Status:** To read
- **Why this matters here:** Short, widely-cited essay distinguishing two incompatible ways of using a calendar: the *manager's schedule* (hour-long slots, context-switching is cheap) and the *maker's schedule* (half-day units, where a single meeting dropped in the middle can destroy the entire afternoon). Source of the vocabulary engineers use to explain — to managers, and to themselves — why design and deep work need protected blocks rather than gaps between meetings. Ten-minute read; unusually high ratio of usefulness to length.

### Simple Made Easy

- **Author:** Rich Hickey (2011, talk — Strange Loop)
- **URL:** https://www.youtube.com/watch?v=SxdOUGdseq4
- **Source:** *The Missing Readme*, Ch. 11 Level Up
- **Relates to:** [`managing-complexity`](./plugins/swe-assistant/skills/managing-complexity/SKILL.md), [`choose-boring-technology`](./plugins/swe-assistant/skills/choose-boring-technology/SKILL.md), [`software-entropy`](./plugins/swe-assistant/skills/software-entropy/SKILL.md)
- **Status:** To read
- **Why this matters here:** The talk that separates **simple** (not intertwined — an objective property of a thing) from **easy** (familiar, near at hand — relative to the person). The distinction matters because teams routinely choose easy over simple and then pay for the complecting later, and because "this is simple" is usually a claim about familiarity rather than structure. Directly sharpens what `managing-complexity` means by its central term. Pairs with Hickey's *Hammock Driven Development*, already listed. Widely regarded as one of the best conference talks in the field.

### How to Write Usefully / Write Like You Talk

- **Author:** Paul Graham (2020 and 2015 respectively)
- **URLs:** http://paulgraham.com/useful.html · http://paulgraham.com/talk.html
- **Source:** *The Missing Readme*, Ch. 10 Level Up
- **Relates to:** [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`commit-and-pr-hygiene`](./plugins/swe-assistant/skills/commit-and-pr-hygiene/SKILL.md), [`asking-for-help`](./plugins/swe-assistant/skills/asking-for-help/SKILL.md)
- **Status:** To read
- **Why this matters here:** Two short companion essays, grouped because they're read together in ten minutes. *How to Write Usefully* argues that useful writing is important, correct, novel, and clear — a usable checklist for whether a design document is worth anyone's time. *Write Like You Talk* is the more immediately actionable of the pair for engineers: formal writing voice makes documents harder to read and is usually adopted to sound authoritative, at direct cost to being understood. If a design doc reads as stiff and nobody engages with it, this is the essay to read.

### Effective Software Design Documents (WePay)

- **Publisher:** WePay engineering blog
- **URLs:** https://wecode.wepay.com/posts/effective-software-design-documents · template: https://github.com/wepay/design_doc_template
- **Source:** *The Missing Readme*, Ch. 10 Level Up
- **Relates to:** [`design-doc`](./plugins/swe-assistant/skills/design-doc/SKILL.md), [`technical-design-process`](./plugins/swe-assistant/skills/technical-design-process/SKILL.md)
- **Status:** To read
- **Why this matters here:** A company-scale account of adopting a design-document practice, with the actual template published as an open repository. Useful as a second data point against the template in `design-doc` — seeing where an independent team's structure agrees and diverges is a good check on which sections are genuinely load-bearing versus conventional. Note: one of the book's authors was at WePay, so this is close to a primary source for the chapter's template rather than an independent corroboration of it.

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

### Self-Explanations: How Students Study and Use Examples in Learning to Solve Problems (Chi et al., 1989)

- **Authors:** Michelene T. H. Chi, Miriam Bassok, Matthew W. Lewis, Peter Reimann, Robert Glaser
- **Publication:** *Cognitive Science* 13(2), 145–182 (1989)
- **Source:** Cited in the [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) skill as the empirical grounding for the self-explanation effect
- **Relates to:** [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- **Status:** Folded
- **Why this matters here:** The foundational empirical treatment of the **self-explanation effect** — the finding that learners who articulate *to themselves* why an example works learn substantially more than those who read the same example passively. Directly grounds why the `stress-test-understanding` skill works: forcing the user to explain their own model is itself the pedagogical mechanism, not just a diagnostic. Widely cited across the learning-science literature.

### Metacognition and Cognitive Monitoring: A New Area of Cognitive-Developmental Inquiry (Flavell, 1979)

- **Author:** John H. Flavell
- **Publication:** *American Psychologist* 34(10), 906–911 (1979)
- **Source:** Cited in the [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) skill as the grounding for the "know what you know" calibration close
- **Relates to:** [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md), [`growth-self-check`](./plugins/swe-assistant/skills/growth-self-check/SKILL.md), [`growth-obstacles`](./plugins/swe-assistant/skills/growth-obstacles/SKILL.md)
- **Status:** Folded
- **Why this matters here:** The canonical article that named and framed **metacognition** — the knowledge and monitoring of one's own cognitive processes. Grounds the *"what you can now defend vs. what's still fuzzy"* close in the `stress-test-understanding` skill: calibrating self-knowledge is a distinct skill from producing knowledge, and it's what a well-run stress-test session actually produces. Short, foundational, cited across the entire self-regulated-learning literature.

### Test-Enhanced Learning: Taking Memory Tests Improves Long-Term Retention (Roediger & Karpicke, 2006)

- **Authors:** Henry L. Roediger III, Jeffrey D. Karpicke
- **Publication:** *Psychological Science* 17(3), 249–255 (2006)
- **Source:** Referenced in the [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) skill as an adjacent empirically-supported active-learning technique
- **Relates to:** [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- **Status:** To read
- **Why this matters here:** A landmark demonstration of the **testing effect** (also called retrieval practice): being tested on material produces better long-term retention than an equivalent time spent re-studying it. Adjacent to the mechanism `stress-test-understanding` exercises — retrieval under adversarial questioning is a stronger form of retrieval practice than reading with a highlighter. Worth folding into `learning-toolkit` and `stress-test-understanding` more deeply on a second pass.

### Elaborative Interrogation and Facilitation of Fact Learning (Pressley et al., 1988)

- **Authors:** Michael Pressley, Mark A. McDaniel, James E. Turnure, Eileen Wood, Maheen Ahmad
- **Publication:** *Journal of Educational Psychology* 80(3), 268–278 (1988)
- **Source:** Referenced in the [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md) skill as adjacent empirical grounding for the "why questions during learning" mechanism
- **Relates to:** [`stress-test-understanding`](./plugins/swe-assistant/skills/stress-test-understanding/SKILL.md), [`learning-toolkit`](./plugins/swe-assistant/skills/learning-toolkit/SKILL.md)
- **Status:** To read
- **Why this matters here:** The foundational study on **elaborative interrogation** — the practice of asking *"why is this true?"* / *"why does this fact make sense given what I already know?"* during study, and the empirical demonstration that this substantially improves learning of factual material. Closely related to the self-explanation effect (Chi et al., 1989) and directly relevant to why the Socratic probing in `stress-test-understanding` produces retention, not just performance-in-the-moment.

---

## How references flow into skills

The intended pipeline:

1. **Surfaced** (here, with status "To read") — the reference is known and tagged to the relevant skill(s).
2. **Read** — status updated; Takeaways section added here with the 3–7 things that changed my thinking.
3. **Folded** — the relevant skill body is updated with the new material; the skill's `## Source` section adds this book to its citation list; status here is set to **Folded**.

The reason for keeping this separate from the skills (rather than padding skill bodies with unread references) is **honesty**: skills should reflect material that's actually shaped them, not material that *should* shape them eventually. Aspirational citations are a slow poison for trust in the skills — when the user goes back to a skill expecting depth and finds only what's been actually internalized, the skill stays trustworthy.
