# Split professional-html-report Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the single `professional-html-report` skill into a general, brevity-aware design-system skill (keeps the name) plus a new opt-in `security-findings-report` skill, so short reports stop being forced into the heavy findings format.

**Architecture:** `professional-html-report` retains the look (typography, palette, layout), all general components, the full Print & Responsive block, and gains a new Brevity section. `security-findings-report` references `professional-html-report` for the base look and print rules, and owns all findings-specific components (finding cards, the 3-section mandate, impact/remediation boxes, severity donut + bar + linked legend, sequential numbering, cross-references, expand/collapse JS). No CSS is duplicated between them.

**Tech Stack:** Markdown skill files (`SKILL.md` with YAML frontmatter), two JSON plugin manifests. No code, no build step, no automated test framework — verification is via `grep`, frontmatter inspection, and visual review.

---

## Reference: current content map

All line numbers below refer to the **current** `skills/professional-html-report/SKILL.md` (421 lines) as it exists before this plan runs. Read it once at the start so you can copy blocks verbatim.

| Block | Current lines | Destination |
|-------|--------------|-------------|
| Frontmatter | 1–4 | A (edit description) |
| Overview | 6–16 | A (genericize) |
| When to Use | 12–16 | A (genericize) |
| Design System (typography/palette/layout) | 18–83 | A (verbatim) |
| Component 1 — Report Header | 87–93 | A |
| Component 2 — Table of Contents | 95–100 | A |
| Component 3 — Executive Summary with Charts (donut/legend/severity bar) | 102–132 | **B** |
| Component 4 — Section Headers | 134–147 | A |
| Component 5 — Finding Cards | 149–197 | **B** |
| Component 6 — Impact Box | 199–210 | **B** |
| Component 7 — Remediation Box | 212–223 | **B** |
| Component 8 — Data Tables | 225–234 | A |
| Component 9 — Bar Charts | 236–248 | A |
| Component 10 — Code Blocks | 250–255 | A |
| Component 11 — Inline Code | 257–262 | A |
| Component 12 — Questions / Callout | 264–272 | A |
| Component 13 — Footer | 274–282 | A |
| JavaScript (expand/collapse + anchor) | 284–309 | **B** |
| Print & Responsive | 311–369 | A (verbatim; keep findings selectors) |
| Document Structure | 371–396 | A (genericize) |
| Common Mistakes table | 398–420 | split (see Task 2 / Task 3) |

**Common Mistakes split:**
- Stay in A (general/print concerns): "Using a JS framework or build step", "Dark theme", "Generic fonts", "Purple/gradient color scheme", "Forgetting print styles", "Dark header / colored fills vanish in printed PDF", "Card/table/section split awkwardly across two printed pages", "Section heading stranded at page bottom", "Code block separated from the line that introduces it".
- Move to B (findings-specific): "Missing severity left border on cards", "Wrong default expand state", "Finding card missing required sections", "Impact box without 'Why this matters:'", "Remediation without numbered steps", "Wrong impact box class for severity", "Non-sequential finding numbers", "Finding cards without `id` attributes", "Legend item numbers not linked", "Unlinked cross-references".

---

## File Structure

- **Create:** `skills/security-findings-report/SKILL.md` — the opt-in findings layer.
- **Modify:** `skills/professional-html-report/SKILL.md` — strip findings content, genericize, add Brevity section.
- **Modify:** `.claude-plugin/plugin.json` — description + version bump.
- **Modify:** `.claude-plugin/marketplace.json` — description + version bump.

---

## Task 1: Create the `security-findings-report` skill

**Files:**
- Create: `skills/security-findings-report/SKILL.md`

This task copies the findings-specific blocks out of the current `professional-html-report/SKILL.md` into a new skill, prefixed with a directive to apply the base skill first. **Copy the HTML/CSS/JS code blocks verbatim** from the line ranges in the content map — do not retype or "improve" them.

- [ ] **Step 1: Create the new skill file with frontmatter + opening directive**

Create `skills/security-findings-report/SKILL.md` starting with:

```markdown
---
name: security-findings-report
description: Use when generating a security assessment, audit findings document, penetration test report, infrastructure review, or any client-facing report organized as severity-coded findings with remediation steps
---

# Security Findings Report

## Overview

The findings layer for professional reports: severity-coded finding cards, an executive summary with severity charts, and structured remediation. This skill builds on `professional-html-report`.

**First apply the `professional-html-report` skill** for the base look (typography, color palette, layout), the report header, table of contents, section headers, data tables, code blocks, footer, and the full Print & Responsive CSS. This skill adds only the findings-specific components below — it intentionally does NOT restate the palette or print rules, so there is a single source of truth for them.

## When to Use

- Client-facing security assessments, audit reports, penetration test results, infrastructure reviews
- Any report whose body is a set of severity-coded findings, each with impact and remediation
- When a report needs a severity breakdown chart, sequential finding numbering, and cross-references between findings

If the report is NOT findings-based (a general summary, brief, or one-pager), use `professional-html-report` alone and do not pull in this skill.
```

- [ ] **Step 2: Append the Executive Summary with Charts component**

From current `professional-html-report/SKILL.md` lines **102–132**, copy the entire "### 3. Executive Summary with Charts" block (donut chart CSS, donut legend with linked item numbers, severity bar). Paste under a new heading. Renumber it as component 1 in this skill:

```markdown
## Component Library

### 1. Executive Summary with Charts
```

…followed by the copied body (the donut `conic-gradient` CSS, the `.donut-legend a` CSS, the `donut-legend` HTML, and the severity-chart HTML) verbatim.

- [ ] **Step 3: Append the Finding Cards component**

From current lines **149–197**, copy the entire "### 5. Finding Cards (collapsible)" block verbatim — including the full `finding-card` HTML, the "Every finding card MUST contain all three sections" mandate, the "No exceptions" line, and the "Cross-references" guidance. Add it under:

```markdown
### 2. Finding Cards (collapsible)
```

- [ ] **Step 4: Append the Impact Box and Remediation Box components**

From current lines **199–210** copy "### 6. Impact Box" and from **212–223** copy "### 7. Remediation Box", verbatim. Renumber as:

```markdown
### 3. Impact Box
```
```markdown
### 4. Remediation Box
```

- [ ] **Step 5: Append the JavaScript section**

From current lines **284–309**, copy the entire "## JavaScript" block (Alt+E / Alt+C expand-collapse and anchor auto-expand) verbatim:

```markdown
## JavaScript

Minimal. Keyboard shortcuts for expand/collapse, plus auto-expand on anchor navigation:
```
…followed by the copied `<script>` body.

- [ ] **Step 6: Append the findings-specific Common Mistakes table**

Add this table verbatim (these are the findings rows lifted from the current Common Mistakes table):

```markdown
## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Missing severity left border on cards | Always include `severity-critical/high/medium` class on finding cards. |
| Wrong default expand state | All critical cards get `open` class. High and medium cards are collapsed. |
| Finding card missing required sections | Every card MUST have: Current State h4, impact box, and remediation box. No exceptions. |
| Impact box without "Why this matters:" | Always lead with `<strong>Why this matters:</strong>` in impact boxes. |
| Remediation without numbered steps | Use `<ol>` in remediation boxes, not prose paragraphs. |
| Wrong impact box class for severity | Use `danger` for critical findings, `warning` for high, `info` for medium. |
| Non-sequential finding numbers | Always number findings #1, #2, #3... in document order, regardless of source numbering. |
| Finding cards without `id` attributes | Every card needs `id="finding-N"` for anchor linking from summary and cross-references. |
| Legend item numbers not linked | Each number in the donut legend should be an `<a href="#finding-N">` link. |
| Unlinked cross-references | Any mention of another finding (e.g., "see #6") must be an `<a href="#finding-N">` link. |
```

- [ ] **Step 7: Verify the new skill has valid frontmatter and references the base skill**

Run: `head -4 skills/security-findings-report/SKILL.md`
Expected: shows `---`, `name: security-findings-report`, a `description:` line, `---`.

Run: `grep -c "professional-html-report" skills/security-findings-report/SKILL.md`
Expected: `1` or more (the opening directive references it).

- [ ] **Step 8: Verify NO palette or print CSS was duplicated into B**

Run: `grep -c -e "--bg-page" -e "print-color-adjust" -e "conic-gradient" skills/security-findings-report/SKILL.md`
Expected: the donut `conic-gradient` IS present, but `--bg-page` and `print-color-adjust` are NOT. Confirm by running each separately:

Run: `grep -c "print-color-adjust" skills/security-findings-report/SKILL.md`
Expected: `0`

Run: `grep -c -- "--bg-page" skills/security-findings-report/SKILL.md`
Expected: `0`

Run: `grep -c "conic-gradient" skills/security-findings-report/SKILL.md`
Expected: `1`

- [ ] **Step 9: Commit**

```bash
git add skills/security-findings-report/SKILL.md
git commit -m "Add security-findings-report skill (opt-in findings layer)"
```

---

## Task 2: Strip findings content from `professional-html-report` and genericize

**Files:**
- Modify: `skills/professional-html-report/SKILL.md`

Remove the blocks that moved to Task 1, renumber the remaining components, and genericize the Overview / When to Use / Document Structure so the skill reads as a general report design system. **Keep the Design System and the full Print & Responsive block verbatim.**

- [ ] **Step 1: Remove the three findings component blocks**

Delete these blocks from `skills/professional-html-report/SKILL.md`:
- "### 3. Executive Summary with Charts" (current lines 102–132)
- "### 5. Finding Cards (collapsible)" (current lines 149–197)
- "### 6. Impact Box" and "### 7. Remediation Box" (current lines 199–223)

- [ ] **Step 2: Remove the JavaScript section**

Delete the entire "## JavaScript" block (current lines 284–309). The general skill has no required JavaScript.

- [ ] **Step 3: Renumber the remaining components**

After deletion, the remaining components are, in order: Report Header, Table of Contents, Section Headers, Data Tables, Bar Charts, Code Blocks, Inline Code, Questions / Callout Section, Footer. Renumber their headings sequentially:

```markdown
### 1. Report Header (dark banner)
### 2. Table of Contents
### 3. Section Headers
### 4. Data Tables
### 5. Bar Charts (pure CSS)
### 6. Code Blocks
### 7. Inline Code
### 8. Questions / Callout Section
### 9. Footer
```

- [ ] **Step 4: Genericize the Overview**

Replace the current Overview body (lines 8–10) so it no longer centers on assessments. Use:

```markdown
## Overview

Generate self-contained, single-file HTML reports with a warm light-themed editorial aesthetic. Reports are print-friendly, responsive, and use only Google Fonts + CSS (no JS frameworks). The design is intentionally restrained and professional -- suitable for executive audiences, client deliverables, and compliance documentation.

For severity-coded **findings** reports (security assessments, audits, pen tests), also use the `security-findings-report` skill, which adds finding cards, severity charts, and remediation structure on top of this design system.
```

- [ ] **Step 5: Genericize the When to Use and add length guidance**

Replace the current "## When to Use" body (lines 12–16) with:

```markdown
## When to Use

- Client-facing reports, briefs, summaries, infrastructure reviews, and audit documents
- Any professional document that should look polished, on-brand, and print-ready
- Reports that will be printed, exported to PDF, or shared as standalone HTML files

Match the report's heft to the request: a one-pager and a 30-finding audit both use this design system, but at very different structural weight. See **Report Length & Restraint** below.
```

- [ ] **Step 6: Add the Report Length & Restraint section**

Insert this new section immediately after "## When to Use" and before "## Design System":

```markdown
## Report Length & Restraint

**Structure scales to the requested length. The component library is a toolkit to draw from, not a checklist to fill.**

- When the user asks for a 1-2 page, "short", "concise", "brief", or "executive" report, prefer plain prose and compact tables. Skip the table of contents, charts, and heavy scaffolding. A short report may be a header, a few sections, and a footer — nothing more.
- Do not pad. Default to the minimum structure that communicates the content clearly. Add components (TOC, charts, collapsible sections, callouts) only when the length and complexity genuinely justify them.
- Length follows the request, not the template. If asked for two pages, deliver two pages — do not expand every point into multi-part scaffolding to look thorough.
- Reach for the full apparatus (TOC, summary charts, many sections) only for genuinely long, complex documents where it aids navigation.
```

- [ ] **Step 7: Genericize the Document Structure block**

Replace the current "## Document Structure" body (the HTML skeleton at lines 373–396) with a version that does not assume findings:

```markdown
## Document Structure

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Report Title]</title>
  [Google Fonts link]
  <style>[CSS from design system + print block]</style>
</head>
<body>
  <header class="report-header">...</header>
  <div class="page-wrap">
    <!-- Include only what the report needs (see Report Length & Restraint): -->
    <nav class="toc">Table of contents</nav>          <!-- optional, longer reports -->
    <section class="section" id="...">Content sections</section>
    ...
    <section class="questions-section">Open questions</section>  <!-- optional -->
    <div class="report-footer">...</div>
  </div>
</body>
</html>
```
```

(Note: the closing fence above is part of the embedded code block — preserve the nested fencing exactly as written in the current file's Document Structure section.)

- [ ] **Step 8: Trim the Common Mistakes table to general rows only**

Replace the current Common Mistakes table (lines 398–420) so it contains ONLY these rows (the findings rows moved to Task 1):

```markdown
## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using a JS framework or build step | Keep it single-file HTML. No dependencies. |
| Dark theme | This is a light warm theme. Dark header only. |
| Generic fonts (Inter, Roboto, Arial) | Use DM Serif Display + Manrope + JetBrains Mono exactly. |
| Purple/gradient color scheme | Use the warm neutral palette with red/amber/blue severity coding. |
| Padding a short report into a long one | Match structure to the requested length; skip TOC/charts for 1-2 page reports. |
| Forgetting print styles | Always include `@media print` block. |
| Dark header / colored fills vanish in printed PDF (white text on white) | Add `print-color-adjust: exact` (and `-webkit-` prefix) with `!important` to `*` inside `@media print` so backgrounds render. |
| Card/table/section split awkwardly across two printed pages | Apply `break-inside: avoid` (+ legacy `page-break-inside: avoid`) to components in `@media print`; wrap custom groups in `<div class="avoid-break">`. |
| Section heading stranded at page bottom, its table/chart on the next page | Wrap the section's label+title+intro in `<div class="section-head">` so the intro stays glued to the content that follows it. |
| Code block separated from the line that introduces it (or split mid-block) | `.code-block` gets `break-inside: avoid`; for a guaranteed pairing wrap the intro line + code block in `<div class="avoid-break">` (e.g. numbered "step + code" lists). |
```

- [ ] **Step 9: Verify findings content is gone from A**

Run: `grep -c -e "finding-card" -e "Finding Cards" -e "remediation-box" -e "impact-box" -e "conic-gradient" -e "Why this matters" skills/professional-html-report/SKILL.md`
Expected: `0` (none of the findings-specific markers remain).

Run: `grep -c "Report Length" skills/professional-html-report/SKILL.md`
Expected: `1` (brevity section present).

- [ ] **Step 10: Verify the design system and print block survived intact**

Run: `grep -c -e "--bg-page" -e "print-color-adjust" -e "break-inside: avoid" -e "DM Serif Display" skills/professional-html-report/SKILL.md`
Expected: a non-zero count for each (run individually if needed) — the palette, print rules, and fonts are all still present.

Note: the Print & Responsive block legitimately still lists findings selectors (`.finding-card`, `.impact-box`, `.remediation-box`, etc.) in its `break-inside: avoid` rule. **Leave these** — `security-findings-report` relies on this block for print behavior, which is the whole point of not duplicating CSS.

- [ ] **Step 11: Commit**

```bash
git add skills/professional-html-report/SKILL.md
git commit -m "Genericize professional-html-report: drop findings layer, add brevity guidance"
```

---

## Task 3: Update plugin manifests and version

**Files:**
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`

- [ ] **Step 1: Update `plugin.json` description and version**

In `.claude-plugin/plugin.json`, replace the `description` value with one that mentions the new skill, and bump `version` from `1.6.0` to `1.7.0`:

```json
{
  "name": "ianneub-skills",
  "description": "Personal skill collection: README crafting, design elevation, professional HTML reports, security findings reports, itinerary-to-ICS calendar files, and Pushover notifications",
  "version": "1.7.0"
}
```

- [ ] **Step 2: Update `marketplace.json` description and version**

In `.claude-plugin/marketplace.json`, update the plugin entry's `description` to match and bump its `version` to `1.7.0`:

```json
{
  "name": "ianneub-claude-skills",
  "owner": {
    "name": "Ian Neubert"
  },
  "plugins": [
    {
      "name": "ianneub-skills",
      "source": "./",
      "description": "Personal skill collection: README crafting, design elevation, professional HTML reports, security findings reports, itinerary-to-ICS calendar files, and Pushover notifications",
      "version": "1.7.0",
      "author": {
        "name": "Ian Neubert"
      }
    }
  ]
}
```

- [ ] **Step 3: Verify both manifests are valid JSON and reference the new skill**

Run: `python3 -m json.tool .claude-plugin/plugin.json > /dev/null && python3 -m json.tool .claude-plugin/marketplace.json > /dev/null && echo OK`
Expected: `OK` (both parse).

Run: `grep -c "security findings" .claude-plugin/plugin.json .claude-plugin/marketplace.json`
Expected: each file reports `1`.

Run: `grep -c "1.7.0" .claude-plugin/plugin.json .claude-plugin/marketplace.json`
Expected: `plugin.json:1` and `marketplace.json:1`.

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json
git commit -m "Register security-findings-report skill, bump to 1.7.0"
```

---

## Task 4: Final cross-skill verification

**Files:** none modified — verification only.

- [ ] **Step 1: Confirm both skills exist with valid frontmatter**

Run: `for f in skills/professional-html-report/SKILL.md skills/security-findings-report/SKILL.md; do echo "== $f"; head -4 "$f"; done`
Expected: both show a `---` / `name:` / `description:` / `---` frontmatter block, with names `professional-html-report` and `security-findings-report` respectively.

- [ ] **Step 2: Confirm the no-duplication invariant holds across both skills**

Run: `grep -l "print-color-adjust" skills/*/SKILL.md`
Expected: only `skills/professional-html-report/SKILL.md` (print CSS lives in exactly one skill).

Run: `grep -l -- "--bg-page" skills/*/SKILL.md`
Expected: only `skills/professional-html-report/SKILL.md` (palette lives in exactly one skill).

- [ ] **Step 3: Confirm the findings skill owns the findings components**

Run: `grep -l "finding-card" skills/*/SKILL.md`
Expected: only `skills/security-findings-report/SKILL.md`.

- [ ] **Step 4: Read both skills top-to-bottom for coherence**

Open each `SKILL.md` and confirm: component numbering is sequential with no gaps, the Overview/When-to-Use cross-references between the two skills are correct, and no dangling reference to a removed/moved section remains. Fix any stragglers and amend the relevant commit.

- [ ] **Step 5: Final commit (only if Step 4 required fixes)**

```bash
git add skills/professional-html-report/SKILL.md skills/security-findings-report/SKILL.md
git commit -m "Fix cross-references and numbering after skill split"
```

---

## Self-Review notes (for the implementer)

- **Spec coverage:** Skill A keeps look + print + general components + new Brevity section (Tasks 2). Skill B owns finding cards, 3-section mandate, impact/remediation, donut+severity bar+legend, numbering, cross-refs, JS, findings mistakes (Task 1). Donut → B; bar charts → A (content map). No CSS duplicated (Task 1 Step 8, Task 4 Step 2). Manifests + version bump (Task 3). All spec sections map to a task.
- **No placeholders:** every new prose block (frontmatter, overview, brevity section, doc structure, both Common Mistakes tables, both JSON files) is given in full. Moved code blocks reference exact verbatim line ranges in the current file rather than being retyped, to avoid transcription drift.
- **Naming consistency:** the new skill is `security-findings-report` everywhere; the retained skill is `professional-html-report` everywhere; version is `1.7.0` in both manifests.
