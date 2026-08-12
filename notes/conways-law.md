# Conway's Law — research note

Not book reading. Compiled to answer a gap noticed while logging *Universal Principles of UX* principle 17: **Conway's Law appeared nowhere in this repository.** Recorded so the citations do not have to be re-found.

**Outcome: folded, not built as a skill.** Reasoning at the end.

---

## The source

**Melvin E. Conway, *How Do Committees Invent?*, Datamation, April 1968.** ([PDF](https://www.melconway.com/Home/pdf/committees.pdf))

> organizations which design systems … are constrained to produce designs which are copies of the communication structures of these organizations.

Two details worth carrying:

- **It was rejected by *Harvard Business Review* in 1967 on the grounds that Conway had not proved his thesis.** Datamation published it instead. The most-cited claim in socio-technical architecture reached print only after being turned down for insufficient evidence — and the proof arrived forty years later, from other people.
- The thesis sits in the **third-to-last paragraph**. It was not presented as a law; the "law" framing came later, from readers.

## The evidence — stronger than most citations suggest

**Nagappan, Murphy & Basili, *The Influence of Organizational Structure on Software Quality* (ICSE 2008, 521–530).** ([PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2008-11.pdf))

Eight organisational-complexity metrics tested against **Windows Vista**. They predicted failure-proneness at **86.2% precision and 84% recall**, significantly outperforming code churn, complexity, coverage, dependencies, and pre-release bug counts. The headline: **who worked on the code predicted defects better than any property of the code.** Motivated explicitly by Brooks asserting this in *The Mythical Man-Month* without evidence.

**MacCormack, Rusnak & Baldwin, *Exploring the Duality Between Product and Organizational Architectures* (*Research Policy* 41(8), 2012, 1309–1324).** ([PDF](https://www.hbs.edu/ris/Publication%20Files/08-039_1861e507-1dc1-4602-85b8-90d71559d85b.pdf))

Matched pairs of products doing the same job, one from a tightly-coupled commercial firm and one from a loosely-coupled open-source community. In **every pair** the loosely-coupled organisation's product was more modular — **up to a factor of eight** in how far a design change propagates.

## The limits — the part that gets dropped

**Colfer & Baldwin, *The Mirroring Hypothesis: Theory, Evidence and Exceptions* (*Industrial and Corporate Change*, 2016).** ([PDF](https://www.hbs.edu/ris/Publication%20Files/Colfer%20Baldwin%20Mirroring%20Hypothesis%20Ind%20Corp%20Change-2016_8aa320ff-6aa6-42ef-b259-d139012faaf6.pdf))

Review of **142 empirical studies**, split into industry, firm, and open collaborative projects.

- Mirroring is **prevalent but not universal** in industry and firm studies.
- **Studies of open collaborative projects were not supportive of the hypothesis.**
- **Partial mirroring** — knowledge boundaries drawn wider than operational ones — is likely superior in technologically dynamic industries.
- Firms deliberately **"break the mirror"**: modular partitions inside their own boundaries, or relational contracts supporting interdependency across them.

**So it is a strong tendency under specific conditions, deliberately breakable, and absent in open collaboration.** Conway's HBR reviewers were right about the proof and wrong about the conclusion. Anything derived from this should say *tendency*, not *law*.

## The Inverse Conway Maneuver — deliberately left out

Restructure teams to produce the architecture you want; central to *Team Topologies* (Skelton & Pais). Excluded from the folds for two reasons.

**Audience.** It is a staff-plus or management decision. This repository serves early- to mid-career engineers, who are *subject to* a reorg rather than deciding one — see [`LIMITATIONS.md`](../docs/LIMITATIONS.md) Section 7a on where the career model stops.

**And the honest version is a warning, not a technique.** Against an existing rigid architecture it is not an instant fix; breaking working groups costs morale and productivity; and without genuine buy-in people revert to established paths and **further solidify the architecture the maneuver was meant to change.** A failed attempt leaves the system more entrenched than before.

## Why this folded rather than becoming a skill

[`METHODOLOGY.md`](../docs/METHODOLOGY.md) Design Principle 3.2: **trigger on situations, not topics.** Conway's Law is a topic — a lens that explains things, not a moment anyone is in. Strip out the reorg material as out-of-audience and what remains is diagnostic, and every situation it clarifies already has a skill:

| Fold | Where | What it adds |
|---|---|---|
| [`managing-complexity`](../plugins/swe-assistant/skills/managing-complexity/SKILL.md) | Step 4, plus the transfers callout | **Organisational inertia** — a boundary that doesn't match the communication structure regenerates after you move it. Diagnostic: *can this boundary move, or would the org rebuild it?* |
| [`software-entropy`](../plugins/swe-assistant/skills/software-entropy/SKILL.md) | New callout after the four drivers | A **fifth answer that isn't decay**. The other four are degradation; mirroring is present at birth. Another non-blame explanation, which is that skill's whole job. |
| [`evolvable-apis`](../plugins/swe-assistant/skills/evolvable-apis/SKILL.md) | The *internal, other teams* consumer class | Cross-team APIs are **negotiated treaties**, and the negotiation shows in the surface. |

**Open question.** Colfer & Baldwin's finding that mirroring fails for open collaborative projects is not folded anywhere, because no current skill is about contributing to or running open source. If that ever becomes a topic here, it is the first thing to check — the repository's implicit model of team-shaped software may not transfer.
