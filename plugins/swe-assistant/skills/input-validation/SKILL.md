---
name: input-validation
description: Use when the user is writing code that handles input from outside the trust boundary — user input, network requests, file uploads, environment variables, query parameters, request bodies, message queue payloads, third-party API responses, command-line arguments, or any other data the code did not produce itself. Triggers include phrases like "I'm validating user input", "this takes a request body", "how do I sanitize this", "is this SQL injection safe", "preventing XSS", "how do I validate this form", "checking input from", "the user can submit", "this endpoint accepts", "should I escape this", "what are the security considerations", or asking about OWASP, input sanitization, or preconditions on a function that crosses a trust boundary. Walks through the validation discipline from The Missing Readme (Chapter 4) — never trust input, reject bad input early, validate format and range, escape for the downstream context (SQL, HTML, shell), use mature libraries rather than rolling your own, and the OWASP Top 10 categories that catch the most common production security failures. Do not trigger for purely internal data flow within a trust boundary, for code reviews (route to code-review), or for general "make this safer" requests (route to defensive-programming).
---

# input-validation

## Source

*The Missing Readme*, Chapter 4, "Writing Operable Code" (Section: Defensive Programming, subsection on validating inputs). The OWASP material is anchored by the **OWASP Top 10**: https://owasp.org/www-project-top-ten/ — *the* essential reference for early-career engineers on what security failures actually happen in production.

## Pillars this skill strengthens

- **Primary:** Technical Knowledge, Execution
- **Also:** Communication (validation logic is most readable when it's at the boundary, not scattered)
- **Builds:** Leadership (security failures hurt teams; modeling the discipline raises the bar)

## What this skill is for

Input validation is where the most consequential bugs live. SQL injection, cross-site scripting, buffer overflows, command injection, and most data-corruption bugs all start at a boundary where untrusted input was treated as trusted.

This skill fires when the user is writing code that handles input from outside the trust boundary — anywhere data enters their system from the network, the user, the filesystem, or a third party. Internal data passing between functions within the same trust boundary is *not* this skill's domain.

## The core mindset (lead with this)

**Never trust input. Reject bad input at the boundary, as early as possible.**

- **Validate at the door.** The further untrusted data gets into the system before being checked, the more places a missing check becomes a bug.
- **Be as constrained as possible.** If the field can only be a phone number, validate that format. If it can only be in a range, validate the range. If it can only be one of three values, validate the enum. *"Looks like a string"* is not validation.
- **Bad input is the common case, not the edge case.** Real systems get malformed data, malicious data, and accidentally-wrong data constantly. Code that assumes input is well-formed will be wrong in production within days.

## How to run

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol): **one question per turn, work on the actual code if shared, route to focused content the user needs.**

### Step 1 — Diagnose

If the user has specific code in mind, work on that. Otherwise ask **one** question:

- *"What input are you validating, and where does it come from?"* (form? API request? file upload? message queue?)

Skip if obvious from the user's first message.

### Step 2 — Identify the trust boundary

What separates trusted from untrusted code in their system? The validation belongs *at* that boundary, not deeper. Common boundaries:

- HTTP request handlers / route handlers
- Message queue consumers
- File upload handlers
- CLI argument parsers
- Third-party webhook handlers
- Database query results from untrusted sources

### Step 3 — Walk through the validation layers

Pick the layers that apply, based on the input type and the downstream context.

#### Format and shape

- **Structural shape.** Is it valid JSON / XML / whatever? Use a parser; don't regex.
- **Required fields present?** Missing fields should fail loudly, not silently default.
- **Field types correct?** A string that should be an integer is not "obviously close enough."
- **String format if structured?** Email regex / phone format / ISO date — use battle-tested libraries.
- **Whitespace?** Leading and trailing whitespace are a near-universal validation gotcha. Trim or reject explicitly.

#### Range and constraints

- **Numbers in range?** A "quantity" of -1 or 10,000,000 should be rejected, not stored.
- **String length bounds?** Both minimum and maximum. Unbounded strings are a DoS vector.
- **Enumerated values?** Reject anything not in the allowed set.
- **Cross-field constraints?** *Start date before end date*, *amount ≤ available balance*, etc.

#### Escape for the downstream context

Each downstream destination has its own escaping rules. Use the right one:

- **SQL** → parameterized queries. *Always.* String concatenation into SQL is the original sin of input handling. If your language/library makes parameterized queries hard, switch libraries.
- **HTML** → context-aware escaping (different rules for HTML content, attributes, URLs, JavaScript context). Use your framework's escaping; don't roll your own.
- **Shell** → avoid shell-out entirely if you can. If you must, use the API form that takes argv arrays rather than the string form (`exec(['ls', '-la', path])` not `exec(f'ls -la {path}')`).
- **Logging** → escape control characters before logging untrusted input. Log injection is real.
- **File paths** → reject absolute paths and `..` traversal; resolve against an explicit base directory.

### Step 4 — Use libraries

Most languages have well-known validation libraries that encode the right behaviors. Use them:

- Java / Kotlin: Hibernate Validator (Bean Validation), with annotations like `@Size(min=0, max=100)`, `@NotNull`, `@Email`, `@Pattern`.
- Python: Pydantic, marshmallow, Cerberus.
- JavaScript / TypeScript: Zod, Yup, Joi.
- Go: validator/v10.
- Rust: validator crate.

These libraries handle whitespace, format checking, and most of the patterns above. They also produce useful error messages.

For cryptography or auth: **use mature libraries**, never roll your own. AES, bcrypt, JWT — use the library, read the docs, follow the conventions.

### Step 5 — Use preconditions and postconditions

For internal functions called from a validated boundary, lightweight preconditions document and enforce assumptions:

- Most languages have `assert` or library helpers like `Preconditions.checkNotNull(x)` / `requireNonNull(x)` / `check_that(...)`.
- Postconditions check the function honored its contract.
- These are cheap, they document the function's expectations, and they fail loudly at the right line.

### Step 6 — For durability-critical data: checksums

If you need strong guarantees that data hasn't been corrupted in transit or storage, use checksums (CRC32, SHA-256, etc.). The application or library validates the checksum on read; corruption fails the read, doesn't silently produce wrong results.

---

## Callout — OWASP Top 10

The **OWASP Top 10** (https://owasp.org/www-project-top-ten/) is the most useful security reference for working engineers. It's a periodically-updated list of the most common security failure categories in production web applications.

Categories (as of the most recent OWASP Top 10) include:

- **Broken Access Control** — most common single category. Users accessing things they shouldn't.
- **Cryptographic Failures** — exposed secrets, weak encryption, plaintext storage.
- **Injection** — SQL, command, log, NoSQL, LDAP, XPath injection. Pure input-validation failures.
- **Insecure Design** — design-time security failures (not just coding failures).
- **Security Misconfiguration** — default credentials, exposed admin panels, missing security headers.
- **Vulnerable and Outdated Components** — using libraries with known CVEs.
- **Identification and Authentication Failures** — weak passwords, missing MFA, predictable session tokens.
- **Software and Data Integrity Failures** — unverified deserialization, insecure deploy pipelines.
- **Security Logging and Monitoring Failures** — can't detect attacks because nothing was logged.
- **Server-Side Request Forgery (SSRF)** — coerced server-side requests to internal resources.

**For every input-handling situation, ask yourself:**

- Could this be an injection vector? (Look at OWASP A03.)
- Am I making an access-control assumption I haven't checked? (A01.)
- Am I logging sensitive data? Am I logging *enough* to detect attacks? (A09.)

Reading the OWASP Top 10 once a year and re-reading the new release when it comes out is one of the highest-leverage hours a working engineer can spend.

---

## Common pitfalls — concrete

A short catalog of the bugs this skill is designed to prevent. Each maps to a real production incident pattern.

| Pitfall | Example | Fix |
|---|---|---|
| String concatenation into SQL | `f"SELECT * FROM users WHERE id={user_id}"` | Parameterized: `cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))` |
| Echoing user input into HTML | `<div>${userMessage}</div>` | Context-aware HTML escaping via framework |
| `strcpy` without size limit (C) | `strcpy(dest, src);` | `strncpy(dest, src, sizeof(dest)-1); dest[sizeof(dest)-1] = '\0';` (and prefer safer string types) |
| Shell-out with string interpolation | `exec(f"convert {input_file} out.png")` | `exec(["convert", input_file, "out.png"])` |
| Path traversal in file upload | `open(f"/uploads/{filename}", "wb")` | Resolve against base directory, reject `..` and absolute paths |
| Trusting Content-Type from the client | Assume "image/png" means it really is | Re-derive type from file magic bytes |
| No bounds on collection size | Accept arbitrarily large request bodies | Set explicit size limits at the boundary |
| Rolling your own crypto | Hand-rolled "hash" or token signing | Use `bcrypt`, `argon2`, `jwt` libraries; read the docs |

---

## Output style

Follow the [Output Protocol](../../../../docs/METHODOLOGY.md#10-output-protocol).

- **One question per turn.** Don't ask about all six validation layers at once; diagnose first, then surface what fits.
- **Work on the user's actual code.** If they shared a function, apply the validation discipline to that function specifically.
- **Surface the right downstream-context escape rule for their situation.** SQL injection advice for code that builds HTML is wasted.
- **Mention OWASP early if security is the user's concern.** It's the most useful single reference they can bookmark.
- **Don't lecture if they're already validating.** Senior practitioners often want a sanity check, not a tutorial.
- **Close by surfacing one thing they haven't raised** that the situation implies — a person who should be told, an artifact that needs updating, a step they haven't planned for. One, chosen by consequence; skip it if they've already covered it or clearly know (Output Protocol 10.7).

## When NOT to use this skill

- The user is working with purely internal data flow within a trust boundary. Skip; defensive practices apply but input-validation specifically doesn't.
- The user is asking for general defensive practices, not input-specific. Route to [`defensive-programming`](../defensive-programming/SKILL.md).
- The user is reviewing a PR for security issues. Route to [`code-review`](../code-review/SKILL.md) with security as the lens.
- The user is responding to an active security incident. Route to [`incident-response`](../incident-response/SKILL.md).

## Further reading

Surfaced as a primary reference but not yet folded in — see [`READING-LIST.md`](../../../../READING-LIST.md) for the full entry.

- **OWASP Top 10** (https://owasp.org/www-project-top-ten/) — the canonical practitioner reference for application security failure categories.
- *Building Secure & Reliable Systems* — Adkins, Beyer, et al. (Google, O'Reilly 2020). Free online at https://sre.google/books/building-secure-reliable-systems/. The intersection of security and reliability at scale, including design-time security thinking that complements OWASP's catalog of failure modes.
