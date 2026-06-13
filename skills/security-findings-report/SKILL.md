---
name: security-findings-report
description: Use when producing a security assessment, audit, penetration-test report, vulnerability writeup, or any client-facing document organized as severity-coded findings with impact and remediation.
---

# Security Findings Report

## Overview

This skill defines **what a security findings report must contain and how to organize it** — the reporting methodology. It is **not** a design skill: it specifies no colors, fonts, or CSS.

**Render with the `professional-html-report` skill.** That skill is the visual design language (warm paper aesthetic, Fraunces / Hanken Grotesk / JetBrains Mono, palette, and component library). This skill maps security content onto those components. For everything visual — tokens, styling, layout, print rules — use `professional-html-report`. Its `reference-report.html` is itself a security assessment and shows these components in use.

```
security-findings-report  →  WHAT to report (this skill: severity model, finding structure, numbering)
professional-html-report  →  HOW it looks   (design language: tokens + components)
```

## When to Use

- Security assessments, audits, penetration-test reports, infrastructure/security reviews
- Any report whose body is a set of severity-coded findings, each with impact and remediation

For a general report with no enumerated findings, use `professional-html-report` alone.

## Severity model

Use one consistent scale throughout — the index, the write-ups, and any overview must agree. A typical scale:

- **Critical** — actively exploitable, data exposure, or imminent outage; fix immediately.
- **High** — serious weakness, likely exploitable or high-impact; fix soon.
- **Medium** — meaningful risk requiring specific conditions; schedule a fix.
- **Low / Info** — hardening or hygiene; address opportunistically. (Include only if used.)

Render severity as **colored text** using `professional-html-report`'s severity tokens — Critical → `--critical` (rust), High → muted gold, Medium → `--ink-soft`. Never use the emerald accent for severity; emerald is the *positive* color.

## What every report contains (requirements)

1. **Executive verdict** — overall posture in 2–4 sentences plus the headline counts. → design skill's **verdict tab**.
2. **Severity overview** — counts by severity (plus any key metrics). → **snapshot grid** (a cell per severity + total) and/or a **findings table** used as an index.
3. **Findings** — the core (see below). Provide a **findings table** (No. / Finding / Severity / Effort) as an at-a-glance index, then a detailed write-up per finding.
4. **Remediation roadmap / next steps** — the prioritized actions. → **action list**.
5. **Scope & methodology** — what was reviewed, against which standards, over what window. → **footer** (and/or an opening section).

## What every finding contains (requirements)

Each finding is a numbered **section** (design skill's numbered section heading, with `id="finding-N"`) and MUST document all three parts:

1. **Current State** — the problem, with evidence: a data table, config excerpt, or inline code as needed.
2. **Impact** — why it matters: risk, blast radius, compliance exposure. Lead with the consequence. → design skill's **alert note** (`--alert` for the lead label).
3. **Remediation** — concrete, ordered steps to fix it. → design skill's **action list** (numbered).

A finding missing any of the three is incomplete. Show each finding's severity visibly (colored text), matching the index table.

## Numbering

Number findings **#1, #2, #3 …** in the order they appear in the report, independent of any source/tool/scanner numbering. The index table, the detailed write-ups, and every cross-reference use the same numbers.

## Cross-references

When one finding refers to another, link it: `<a href="#finding-N">#N</a>` (every finding section has `id="finding-N"`). This lets readers jump between related findings — e.g. "compounds with the short backup retention (see <a href="#finding-12">#12</a>)".

## Restraint (inherited from the design skill)

`professional-html-report`'s "components are a toolkit, not a checklist" principle applies to the **visuals**: scale the apparatus to the report. A three-finding review does not need a snapshot grid *and* a severity chart *and* comparison cards — pick what serves the reader.

This restraint is about visual scaffolding, **not** the content requirements above. The verdict, severity model, three-part findings, remediation, numbering, and scope are the *substance* of a security report and always apply, however large or small the engagement.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Defining colors / fonts / CSS in this skill | This skill is content only. Reference `professional-html-report` for all visuals. |
| Finding without an Impact section | Every finding states why it matters (the alert note), led by the consequence. |
| Remediation as vague prose | Concrete, ordered steps (the action list) — not "review and harden as appropriate." |
| Inconsistent severity | Apply the severity model uniformly; the same value appears in the index and the write-up. |
| Source / scanner numbering leaking through | Renumber #1..N in document order. |
| Emerald used for a severity level | Emerald is the positive accent; severity is rust / gold / ink-soft. |
| Unlinked cross-references | Link "see #6" as `<a href="#finding-6">#6</a>`. |
| Burying the verdict | Lead with the verdict tab — overall posture + headline counts at the top. |
| Re-implementing the warm-paper look by hand | Start from `professional-html-report`'s `reference-report.html` and its components. |
