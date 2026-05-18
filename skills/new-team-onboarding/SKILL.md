---
name: new-team-onboarding
description: Use when the user is in or about to enter the early days at a new company, team, or role — for example, about to start a new job, just had their first day or first week, in their first month, asking how to onboard well, asking what to focus on in their first 30 or 90 days, transferring between teams, or expressing that they feel lost as a new hire. Walks them through the Newcomer-stage playbook from The Missing Readme (Chapter 1, "The Journey Ahead") — set up the environment, attend the right meetings, build relationships, learn the codebase by making small low-stakes changes, document what you learn so the next new hire has it easier. Always leads with the core mindset for this stage — understand the system and the people, not to impress. Do not trigger for general career questions or for tactical engineering help unrelated to onboarding.
---

# new-team-onboarding

## Source

*The Missing Readme*, Chapter 1, "The Journey Ahead" — the **Newcomer** stage (the book calls this "Peak Newb"). See [`JOURNEY.md`](../../JOURNEY.md) for the full stage map.

## Pillars this skill strengthens

- **Primary:** Execution, Communication
- **Also:** Technical Knowledge (setting up your environment, learning the codebase)

## What this skill is for

Onboarding well in the first weeks at a new company, team, or role. The skill fires when the user is in (or about to enter) that situation. It helps them get the right setup, the right relationships, and — most importantly — the right mindset.

## The core mindset (lead with this)

**In the first weeks, the goal is to understand the system and the people, not to impress.**

- Speed matters less than learning the steps.
- Asking many "obvious" questions early is an asset, not a liability — that window closes fast, so use it.
- Take notes on everything. They serve you twice: once now, and once as the gift you leave for the next new hire.
- The first PR you ship matters less than the conversations you have in the first month.

If the user seems anxious about being impressive, performing, or "proving themselves" — surface the mindset first, before any of the tactical advice.

## How to run the playbook

### Step 1 — Frame the moment

Two or three sentences. Welcome them. Name the mindset (above). Tell them you'll tailor the rest to where they are in the timeline.

### Step 2 — Ask where they are

One question, options:

- Haven't started yet (next week, next month)?
- First few days?
- Week 2–4?
- Month 2–3?
- Transferring to a new team within the same company?

Wait for the answer. Use it to prioritize which sections of the playbook to surface in Step 3.

### Step 3 — Surface the relevant moves

Don't dump the whole list. Pick the 3–5 items most relevant to where they are. Group by area. Keep prose short.

#### Setup *(week 1)*

- Set up the dev environment and system access. **Write down every step as you go** — this becomes the gift you leave for the next new hire (and your own reference when you forget it in two months).
- Set up the IDE. Ask what code formatting conventions the team uses; configure them locally so your first PRs don't churn on style.
- Confirm you have access to: source repos, code review tooling, CI, internal docs, monitoring, on-call paging, shared drives, calendars, group emails, the relevant Slack/Teams channels.

#### Meetings & rhythms *(week 1–2)*

- Confirm with your manager that you're on every meeting that matters: standup, sprint planning, retro, demos, all-hands. If something feels missing, ask.
- Identify the recurring rhythms: when does the team plan? when do they ship? when do they review? **Watch a full cycle before forming opinions.**

#### People & org *(week 1–3)*

- If there's a new hire program, use it fully.
- If there isn't, ask your manager for: the org chart (who is in charge of what), the relationships between departments, and who you should report what to. Take notes. Refer back to them.
- Schedule short intro 1:1s with everyone on your immediate team. A useful question to bring to each: *"What do you wish you'd known when you started?"*

#### Codebase *(week 2–4)*

- Read the docs. All of them. Yes really.
- Capture the gaps in the docs as you read them — those become your first contributions.
- Ask for one or two minor, low-stakes changes to make in the codebase. **The goal is to learn the workflow** (clone, branch, change, test, review, merge, deploy) **— not to impress.**
- Have discussions with teammates about the code. *"Why is this structured this way?"* is the most useful question of your first month.

#### Documentation *(continuous)*

- Document what you do as you set up. If your company has no formal onboarding process, you are now creating one — write it down.
- Fill in gaps in existing documentation as you find them. **Small PRs that improve docs are a great way to start contributing** — low risk, real value, and they show you're paying attention.

### Step 4 — Pick one move for this week

Ask: *"Out of everything we just covered, what's one thing you'll do this week? Be specific — give me the action and the day."*

Push for concreteness:

- *"Read the docs"* is too vague.
- *"Read the architecture overview by Wednesday and write down 3 questions to bring to my 1:1 with [manager] on Friday"* is the action.

If they're stuck, offer 2–3 small options tied to where they are in the timeline. Let them pick.

### Step 5 — Close

Two sentences: confirm the action, and offer to come back when they have questions or want to debrief after the first week. Don't lecture; don't add bonus advice.

## Output style

- Conversational. Surface the relevant section based on where they are; do not dump the whole playbook.
- Always lead with the mindset if they sound worried about being impressive, slow, or behind.
- If they have a specific blocker (e.g., can't get access to a tool, awkward 1:1 with manager), help with that and skip the rest of the playbook for now.

## When NOT to use this skill

- The user has been at the company/team for more than ~3 months. They've moved past the Newcomer stage; route to other skills.
- The user is asking about onboarding *others* (writing onboarding docs for a new hire they'll receive). The content is reusable but the framing is different.
- The user has a tactical engineering question with no onboarding context. Skip — those need real help, not a checklist.
