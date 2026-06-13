# Split `professional-html-report` into two skills

**Date:** 2026-06-13
**Status:** Approved design, ready for implementation plan

## Problem

The `professional-html-report` skill produces very long-winded reports even when
the user explicitly asks for a 1–2 page document. The cause is not the visual
design system — it is the skill's mandatory **findings** structure. The skill is
shaped around security-assessment-with-many-findings output and repeatedly forces
heavy per-finding scaffolding regardless of report size, most notably:

> "Every finding card MUST contain all three sections... No exceptions. A finding
> without all three sections is incomplete."

When asked for a short general report, the model still dutifully expands every
point into three mandated blocks (Current State + Impact box + Remediation box),
adds a TOC, donut chart, severity coding, and cross-references. The skill fights
the brevity request by design.

Two parts of the skill are genuinely valuable and not reliably reproduced ad hoc:

1. **A consistent, opinionated visual identity** — warm editorial palette, exact
   font trio. Gives brand consistency across reports.
2. **Print/PDF gotchas** — `print-color-adjust: exact`, `break-inside: avoid`,
   section-head gluing. Models routinely forget these and emit PDFs with
   invisible white-on-white headers. This is the highest-value, least-replaceable
   part.

Removing the skill would throw out this durable design knowledge to fix what is
really a content-length problem.

## Decision

Split the single skill into two:

- **`professional-html-report`** (keeps the name) — the general, reusable design
  system, made brevity-aware. Owns the look + print rules + general components.
- **`security-findings-report`** (new) — the opt-in findings layer. Builds on
  `professional-html-report` and owns everything specific to severity-coded
  findings documents.

A normal "make me a 1-page report" request hits only the general skill (now
brevity-aware) → short output. A security assessment pulls in both skills → full
findings treatment.

### Why this shape

- **Keep the established name for the general skill.** `professional-html-report`
  already has strong trigger coverage for general client-facing reports; the
  general design system is the better fit for that trigger. The findings format
  becomes a deliberate add-on.
- **Findings skill references the design skill (no duplicated CSS).** Single
  source of truth for the palette and print rules; no drift. The harness loads
  relevant skills automatically, so chaining is reliable.

## Skill A — `professional-html-report` (general, brevity-aware)

The reusable design system. Keeps the look and the print knowledge; drops all
findings-specific mandates.

### Keeps (moved/retained content)
- Document structure (`<!DOCTYPE>` ... single-file shell)
- Typography (DM Serif Display / Manrope / JetBrains Mono) + Google Fonts link
- Color palette (CSS variables) — including the severity accent variables, since
  tables and callouts use them generally
- Layout (max-width 880px, body sizing, anti-alias, smooth scroll)
- **Report header** (dark banner)
- **Table of contents**
- **Section headers** (`.section-head` gluing)
- **Data tables** (`.fail` / `.warn` / `.ok` cell modifiers)
- **Bar charts** (generic, pure-CSS)
- **Code blocks** + **inline code**
- **Callout / questions section**
- **Footer**
- Full **Print & Responsive** block (verbatim — the highest-value part)

### New — Brevity section
Add an explicit section establishing that **structure scales to the requested
length**:
- When the user asks for 1–2 pages, "concise," "short," or "executive," prefer
  prose + compact tables; skip the TOC, donut/severity charts, and heavy
  scaffolding.
- Do not pad. Default to the minimum structure that communicates the content;
  add components (TOC, charts, collapsible sections) only when length/complexity
  justifies them.
- Length follows the request, not the template. The component library is a
  toolkit to draw from, not a checklist to fill.

This is the direct fix for the long-winded behavior.

### Drops (moves to Skill B)
- Finding cards, severity coding, the 3-section finding mandate
- Impact box, Remediation box
- Severity donut + severity bar + legend-with-finding-links
- Sequential finding numbering, cross-references
- Collapse/expand + anchor-auto-expand JavaScript
- Findings-related "Common Mistakes" rows

### JavaScript
The general skill keeps essentially no required JS (the keyboard-shortcut /
anchor-expand JS is findings-specific and moves to Skill B). If any general
interactivity remains it stays minimal; otherwise the JS section is removed from
Skill A.

## Skill B — `security-findings-report` (opt-in findings layer)

Builds on Skill A. Opens with a directive to apply the base skill first:

> "First apply `professional-html-report` for the base look, typography, palette,
> and print rules. This skill adds the findings-specific components below."

### Owns (moved from the original skill)
- **Finding card** (collapsible, 4px severity left-border;
  `severity-critical/high/medium`; `id="finding-N"`; default-open criticals)
- **3-section finding structure** — Current State (`<h4>`), Impact box,
  Remediation box — including the "MUST have all three / No exceptions" mandate,
  now scoped to findings reports only
- **Impact box** (`danger` / `warning` / `info` by severity)
- **Remediation box** (numbered `<ol>` steps, green accent)
- **Executive summary with charts** — **severity donut** (conic-gradient),
  **severity bar** (stacked), **donut legend with linked finding numbers**
- **Sequential finding numbering** (#1, #2, ... in document order)
- **Cross-references** between findings (`<a href="#finding-N">`)
- **JavaScript** — Alt+E / Alt+C expand-collapse and anchor auto-expand/scroll
- Findings-related **Common Mistakes** rows (wrong expand state, missing required
  sections, missing `id`, unlinked legend numbers, unlinked cross-references,
  non-sequential numbers, wrong impact-box class, prose instead of `<ol>`, etc.)

### Description / triggers
Targets security assessments, audit findings documents, infrastructure reviews,
and any severity-coded findings-with-remediation report. Should make clear it is
the heavy findings format that complements `professional-html-report`.

## Two judgment calls (confirmed)

1. **Severity donut → Skill B.** It is framed entirely around findings severity,
   so it lives with findings. Generic **bar charts stay in Skill A**.
2. **The "MUST have 3 sections / No exceptions" mandate** is retained but only in
   Skill B and scoped to findings reports, so it no longer forces verbosity onto
   a general one-page report.

## Repo integration

- Skills are flat directories under `skills/`, each with a `SKILL.md`. Create
  `skills/security-findings-report/SKILL.md`; edit
  `skills/professional-html-report/SKILL.md` in place.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` carry a
  free-text plugin description that enumerates the skills in prose. Update both
  descriptions to mention the new findings skill, and bump the plugin `version`
  (currently `1.6.0`) per the existing convention of version bumps on skill set
  changes.

## Out of scope

- No change to the visual design itself (palette, fonts, components render
  identically).
- No new build step, framework, or external dependency — output stays
  single-file HTML.
- No broad rewrite of unrelated skills.

## Success criteria

- A general "1–2 page report" request, using only `professional-html-report`,
  produces a short report without forced TOC/charts/3-section findings.
- A security-assessment request pulls in both skills and produces the full
  findings treatment identical in look to today's output.
- No palette or print CSS is duplicated between the two skills.
- Plugin manifests and version reflect the new skill.
