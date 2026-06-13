---
name: professional-html-report
description: Use when generating a client-facing HTML report, executive brief, summary, or any polished, print-ready single-file report. For severity-coded findings reports (security assessments, audits, pen tests), use the security-findings-report skill instead.
---

# Professional HTML Report

## Overview

Generate self-contained, single-file HTML reports with a warm light-themed editorial aesthetic. Reports are print-friendly, responsive, and use only Google Fonts + CSS (no JS frameworks). The design is intentionally restrained and professional -- suitable for executive audiences, client deliverables, and compliance documentation.

For severity-coded **findings** reports (security assessments, audits, pen tests), also use the `security-findings-report` skill, which adds finding cards, severity charts, and remediation structure on top of this design system.

## When to Use

- Client-facing reports, briefs, summaries, infrastructure reviews, and audit documents
- Any professional document that should look polished, on-brand, and print-ready
- Reports that will be printed, exported to PDF, or shared as standalone HTML files

Match the report's heft to the request: a one-pager and a 30-finding audit both use this design system, but at very different structural weight. See **Report Length & Restraint** below.

## Report Length & Restraint

**Structure scales to the requested length. The component library is a toolkit to draw from, not a checklist to fill.**

- When the user asks for a 1-2 page, "short", "concise", "brief", or "executive" report, prefer plain prose and compact tables. Skip the table of contents, charts, and heavy scaffolding. A short report may be a header, a few sections, and a footer — nothing more.
- Do not pad. Default to the minimum structure that communicates the content clearly. Add components (TOC, charts, collapsible sections, callouts) only when the length and complexity genuinely justify them.
- Length follows the request, not the template. If asked for two pages, deliver two pages — do not expand every point into multi-part scaffolding to look thorough.
- Reach for the full apparatus (TOC, summary charts, many sections) only for genuinely long, complex documents where it aids navigation.

## Design System

### Typography (Google Fonts)

```
DM Serif Display  -- Headings (h1, h2, section titles). Weight 400 only.
Manrope            -- Body text, UI elements. Weights 300-800.
JetBrains Mono     -- Code, numbers, labels. Weights 400-600.
```

Font link:
```html
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Manrope:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### Color Palette (CSS Variables)

```css
:root {
  /* Backgrounds */
  --bg-page: #fafaf8;        /* Page background -- warm off-white */
  --bg-white: #ffffff;        /* Card/container backgrounds */
  --bg-warm: #f5f3ef;         /* Subtle warm highlight, table headers */
  --bg-code: #f0eeea;         /* Inline code background */

  /* Borders */
  --border-light: #e8e5df;    /* Card borders, table rows */
  --border-mid: #d4d0c8;      /* Table header border */

  /* Text */
  --text-body: #2c2a26;       /* Primary body text */
  --text-secondary: #5c5850;  /* Descriptions, table cells */
  --text-dim: #8a857c;        /* Labels, meta text, legends */
  --text-heading: #1a1816;    /* Headings, header background */

  /* Severity Accents */
  --accent-red: #c0392b;            /* Critical severity */
  --accent-red-bg: #fdf2f1;
  --accent-red-border: #f0c4bf;

  --accent-amber: #d4850a;          /* High severity */
  --accent-amber-bg: #fef8ed;
  --accent-amber-border: #f0d9a8;

  --accent-blue: #1a6bb5;           /* Medium severity / informational */
  --accent-blue-bg: #eef5fc;
  --accent-blue-border: #b8d4ef;

  --accent-green: #1a7a4c;          /* Remediation / success */
  --accent-green-bg: #eef8f2;

  --accent-teal: #0d7377;           /* Optional accent */

  /* Font stacks */
  --serif: 'DM Serif Display', Georgia, serif;
  --sans: 'Manrope', -apple-system, sans-serif;
  --mono: 'JetBrains Mono', monospace;
}
```

### Layout

- Max width: `880px`, centered with `margin: 0 auto; padding: 0 24px`
- Body: `font-size: 15px; line-height: 1.7`
- Anti-aliased: `-webkit-font-smoothing: antialiased`
- Smooth scroll: `scroll-behavior: smooth; scroll-padding-top: 80px`

## Component Library

### 1. Report Header (dark banner)

Dark `--text-heading` background with white text. Contains:
- Company label: 12px, 3px letter-spacing, uppercase, 45% white opacity
- Title: `var(--serif)`, 38px, weight 400
- Subtitle: 16px, 60% white opacity, max-width 600px
- Meta row: flex with 32px gap, separated by 1px white/10% border-top. Each item has a `meta-label` (10px, uppercase, 35% opacity) and `meta-value` (14px, 85% opacity)

### 2. Table of Contents

White card with 8px border-radius. Uses CSS grid `1fr 1fr` for two columns. Each entry has:
- Monospace number (11px, right-aligned, 22px wide)
- Link text (14px, weight 500)
- Optional severity badge (auto margin-left): 10px, weight 700, 2px 8px padding, 3px border-radius

### 3. Section Headers

Wrap the label + title + intro in a `.section-head` so they stay together AND stay glued to the first content block when printing (see Print & Responsive). Put a section's introductory `section-desc` INSIDE `.section-head`; a `section-desc` used as a trailing note after a table stays outside it.

```html
<section class="section" id="section-id">
  <div class="section-head">                         <!-- keeps intro with following content in print -->
    <div class="section-label">Section N</div>       <!-- 11px, uppercase, 2.5px letter-spacing -->
    <h2 class="section-title">Section Name</h2>      <!-- var(--serif), 28px -->
    <p class="section-desc">Description text</p>     <!-- 14px, max-width 720px -->
  </div>
  <table>...</table>                                 <!-- content; intro is glued to this -->
</section>
```

### 4. Data Tables

```html
<table>
  <tr><th>Column</th><th>Column</th></tr>
  <tr><td>Value</td><td class="fail">FAILING VALUE</td></tr>
  <tr><td>Value</td><td class="ok">Passing</td></tr>
</table>
```
Cell modifiers: `.fail` (red, weight 600), `.warn` (amber), `.ok` (green).

### 5. Bar Charts (pure CSS)

```html
<div class="bar-chart">
  <div class="bar-row">
    <span class="bar-label">Label</span>           <!-- 160px, right-aligned -->
    <div class="bar-track">                         <!-- flex:1, 24px height, warm bg -->
      <div class="bar-fill red" style="width:75%">75%</div>
    </div>
  </div>
</div>
```
Fill colors: `.red`, `.amber`, `.blue`, `.green`, `.gray`.

### 6. Code Blocks

```html
<div class="code-block">aws cli command here</div>
```
Dark background (`--text-heading`), green text (`#a8e6a1`), monospace, 12px.

### 7. Inline Code

```html
<span class="inline-code">variable_name</span>
```
Warm code background, light border, 12px monospace, 2px 7px padding.

### 8. Questions / Callout Section

```html
<section class="questions-section" id="questions">
  <h3>Open Questions</h3>
  <p>Question text...</p>
</section>
```
Blue accent: `--accent-blue-bg` background, `--accent-blue-border`, 28px 32px padding, serif h3.

### 9. Footer

```html
<div class="report-footer">
  <p>Assessment methodology and scope...</p>
  <p style="margin-top:12px"><strong>Prepared by:</strong> Company Name</p>
</div>
```
Top border, 12px text, dim color.

## Print & Responsive

Always include:
```css
@media print {
  /* REQUIRED: browsers strip background-color and gradients from print/PDF by
     default. Without this, the dark report-header prints as invisible white text
     on white, and tinted callouts/table headers lose their fills. This forces
     all backgrounds to render. Keep the !important and the -webkit- prefix. */
  *, *::before, *::after {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  .report-header { padding: 32px 0; }
  .card-body { display: block !important; }
  body { font-size: 12px; }

  /* Keep self-contained blocks from being split across pages. break-inside is
     modern; page-break-inside is the legacy alias some PDF engines still need. */
  .finding-card, .summary-card, .stat-card, table, .toc,
  .impact-box, .remediation-box, .questions-section, .bar-chart, .verdict, .code-block,
  .report-footer {
    break-inside: avoid;
    page-break-inside: avoid;
  }
  /* Never strand a heading at the bottom of a page, separated from its content. */
  h2, h3, h4 { break-after: avoid; page-break-after: avoid; }
  /* Keep a code block glued to the line that introduces it. Best-effort (engines
     support break-before: avoid imperfectly); for a guaranteed result wrap the
     intro line + code block together in <div class="avoid-break">. */
  .code-block { break-before: avoid; page-break-before: avoid; }

  /* A section's intro block (label + title + description, wrapped in
     .section-head) stays intact AND glued to the content that follows, so a
     "SECTION N / Title / intro" never strands alone at a page bottom while its
     table or chart spills to the next page. break-inside keeps the intro from
     splitting (reliable); break-after requests no break before the content
     (best-effort -- engines support it imperfectly, and it cannot help when the
     intro + first content together exceed one page). */
  .section-head { break-inside: avoid; break-after: avoid;
                  page-break-inside: avoid; page-break-after: avoid; }

  /* Opt-in: wrap any group of elements in <div class="avoid-break"> to force
     them onto a single page (e.g. a chart + its caption, or a short section).
     NOTE: only works for content shorter than one page. A block taller than the
     page will still break -- there is no way to fit it on one page. For long
     sections, rely on the heading rule above instead of wrapping the whole thing. */
  .avoid-break { break-inside: avoid; page-break-inside: avoid; }
}

@media (max-width: 680px) {
  .report-header h1 { font-size: 28px; }
  .toc-list { grid-template-columns: 1fr; }
  .donut-wrap { flex-direction: column; align-items: flex-start; }
  .bar-label { width: 100px; font-size: 11px; }
}
```

**Keeping content on one page:** small components (cards, tables, callouts, charts) avoid page breaks automatically via the rules above. To force an arbitrary group onto a single page, wrap it in `<div class="avoid-break">...</div>`. This only works for groups shorter than one page — a block taller than the page will still break, since it physically cannot fit. For a long section, don't wrap the whole thing; the `break-after: avoid` heading rule already keeps each heading attached to the content that follows it.

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
