---
name: professional-html-report
description: Use when generating a client-facing HTML report, security assessment, audit findings document, or any professional single-file report that needs to look polished and print-ready
---

# Professional HTML Report

## Overview

Generate self-contained, single-file HTML reports with a warm light-themed editorial aesthetic. Reports are print-friendly, responsive, and use only Google Fonts + CSS (no JS frameworks). The design is intentionally restrained and professional -- suitable for executive audiences and compliance documentation.

## When to Use

- Client-facing security assessments, audit reports, infrastructure reviews
- Any professional document that needs severity-coded findings with remediation
- Reports that will be printed, exported to PDF, or shared as standalone HTML files

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

### 3. Executive Summary with Charts

**Donut chart** (pure CSS `conic-gradient`):
```css
.donut {
  width: 120px; height: 120px; border-radius: 50%;
  background: conic-gradient(var(--accent-red) 0deg Xdeg, var(--accent-amber) Xdeg Ydeg, var(--accent-blue) Ydeg 360deg);
}
```
Center overlay: absolute positioned circle with count + label.

**Donut legend with linked item numbers:** Each item number in the legend is an `<a href="#finding-N">` link to the corresponding finding card. Style the links to inherit text color with a subtle underline:
```css
.donut-legend a { color: inherit; text-decoration: underline; text-decoration-color: var(--border-mid); text-underline-offset: 2px; transition: color 0.15s; }
.donut-legend a:hover { color: var(--accent-blue); text-decoration-color: var(--accent-blue); }
```
```html
<div class="donut-legend">
  <div><span class="ldot" style="background:var(--accent-red)"></span><strong>Critical</strong> &mdash; Must fix immediately (items <a href="#finding-1">1</a>, <a href="#finding-3">3</a>, ...)</div>
  <div><span class="ldot" style="background:var(--accent-amber)"></span><strong>High</strong> &mdash; Fix this month (items <a href="#finding-2">2</a>, <a href="#finding-4">4</a>, ...)</div>
</div>
```

**Severity bar** (stacked):
```html
<div class="severity-chart"> <!-- flex, 10px height, 5px border-radius, overflow hidden -->
  <div class="sev-bar crit" style="width:45%"></div>
  <div class="sev-bar high" style="width:45%"></div>
  <div class="sev-bar med" style="width:10%"></div>
</div>
```

### 4. Section Headers

```html
<section class="section" id="section-id">
  <div class="section-label">Section N</div>       <!-- 11px, uppercase, 2.5px letter-spacing -->
  <h2 class="section-title">Section Name</h2>      <!-- var(--serif), 28px -->
  <p class="section-desc">Description text</p>     <!-- 14px, max-width 720px -->
</section>
```

### 5. Finding Cards (collapsible)

Core component. Severity indicated by left border (4px solid).

The card-header is `display: flex` with `gap: 16px`. The first child `<div>` (title wrapper) gets `flex: 1; min-width: 0` so it fills available space, pushing the severity badge and chevron to a consistent right-aligned position regardless of title length.

Every finding card gets an `id="finding-N"` attribute for anchor linking from the summary, TOC, and cross-references. Number findings sequentially (#1, #2, #3...) in the order they appear in the report, regardless of any source document numbering.

```html
<div class="finding-card severity-critical open" id="finding-1">  <!-- or severity-high, severity-medium -->
  <div class="card-header" onclick="this.parentElement.classList.toggle('open')">
    <div>                                          <!-- flex:1, min-width:0 -->
      <div class="card-num">#1</div>               <!-- var(--mono), 12px, sequential -->
      <div class="card-title">Title</div>          <!-- 16px, weight 700 -->
    </div>
    <span class="card-severity critical">Critical</span>  <!-- badge, right-aligned -->
    <span class="card-chevron">&#9662;</span>              <!-- rotates 180deg when open -->
  </div>
  <div class="card-body">
    <!-- REQUIRED: Every finding card MUST have all three sections below -->
    <h4>Current State</h4>
    <p>Description of the current problem with supporting data/tables...</p>

    <div class="impact-box danger">  <!-- danger for critical, warning for high, info for medium -->
      <strong>Why this matters:</strong> Explanation of risk and compliance impact...
    </div>

    <div class="remediation-box">
      <div class="rem-label">How to fix</div>
      <ol>
        <li>Numbered remediation steps...</li>
      </ol>
    </div>
  </div>
</div>
```

Add `open` class to all critical-severity cards by default. High and medium cards should be collapsed.

**Every finding card MUST contain all three sections:**
1. **Current State** (`<h4>Current State</h4>`) -- description of the problem with supporting data, tables, or charts
2. **Impact box** -- explains why this matters and the risk/compliance impact. Use `danger` class for critical, `warning` for high, `info` for medium
3. **Remediation box** -- numbered steps to fix the issue

No exceptions. A finding without all three sections is incomplete.

**Cross-references:** When a finding's description or remediation refers to another finding, always link it using `<a href="#finding-N">#N</a>`. This lets readers jump directly to the related finding (and auto-expands it). Examples:
- Remediation step: `see VPC finding <a href="#finding-6">#6</a>`
- Impact text: `Combined with the short backup retention (see finding <a href="#finding-12">#12</a>)`

### 6. Impact Box

```html
<div class="impact-box danger">  <!-- or warning, info -->
  <strong>Why this matters:</strong> Explanation text...
</div>
```
- `danger` = red accent (critical)
- `warning` = amber accent (high)
- `info` = blue accent (medium/informational)

Styling: 14px 18px padding, 6px border-radius, 13px font, colored background + border + text.

### 7. Remediation Box

```html
<div class="remediation-box">
  <div class="rem-label">How to fix</div>  <!-- green, uppercase -->
  <ol>
    <li>Step one</li>
    <li>Step two with <span class="inline-code">code reference</span></li>
  </ol>
</div>
```
Green accent: `--accent-green-bg` background, `#bce4cc` border.

### 8. Data Tables

```html
<table>
  <tr><th>Column</th><th>Column</th></tr>
  <tr><td>Value</td><td class="fail">FAILING VALUE</td></tr>
  <tr><td>Value</td><td class="ok">Passing</td></tr>
</table>
```
Cell modifiers: `.fail` (red, weight 600), `.warn` (amber), `.ok` (green).

### 9. Bar Charts (pure CSS)

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

### 10. Code Blocks

```html
<div class="code-block">aws cli command here</div>
```
Dark background (`--text-heading`), green text (`#a8e6a1`), monospace, 12px.

### 11. Inline Code

```html
<span class="inline-code">variable_name</span>
```
Warm code background, light border, 12px monospace, 2px 7px padding.

### 12. Questions / Callout Section

```html
<section class="questions-section" id="questions">
  <h3>Open Questions</h3>
  <p>Question text...</p>
</section>
```
Blue accent: `--accent-blue-bg` background, `--accent-blue-border`, 28px 32px padding, serif h3.

### 13. Footer

```html
<div class="report-footer">
  <p>Assessment methodology and scope...</p>
  <p style="margin-top:12px"><strong>Prepared by:</strong> Company Name</p>
</div>
```
Top border, 12px text, dim color.

## JavaScript

Minimal. Keyboard shortcuts for expand/collapse, plus auto-expand on anchor navigation:
```js
// Expand all (Alt+E) / Collapse all (Alt+C)
document.addEventListener('keydown', function(e) {
  if (e.key === 'e' && e.altKey) {
    document.querySelectorAll('.finding-card').forEach(f => f.classList.add('open'));
  }
  if (e.key === 'c' && e.altKey) {
    document.querySelectorAll('.finding-card').forEach(f => f.classList.remove('open'));
  }
});

// Auto-expand and scroll to finding card when clicking an anchor link
document.addEventListener('click', function(e) {
  var link = e.target.closest('a[href^="#finding-"]');
  if (!link) return;
  e.preventDefault();
  var el = document.querySelector(link.getAttribute('href'));
  if (el && el.classList.contains('finding-card')) {
    el.classList.add('open');
    el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
});
```

## Print & Responsive

Always include:
```css
@media print {
  .report-header { padding: 32px 0; }
  .card-body { display: block !important; }
  .finding-card { break-inside: avoid; }
  body { font-size: 12px; }
}

@media (max-width: 680px) {
  .report-header h1 { font-size: 28px; }
  .toc-list { grid-template-columns: 1fr; }
  .donut-wrap { flex-direction: column; align-items: flex-start; }
  .bar-label { width: 100px; font-size: 11px; }
}
```

## Document Structure

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Report Title]</title>
  [Google Fonts link]
  <style>[Full CSS from design system]</style>
</head>
<body>
  <header class="report-header">...</header>
  <div class="page-wrap">
    <section id="summary">Executive summary + charts</section>
    <nav class="toc">Table of contents</nav>
    <section class="section" id="...">Grouped findings</section>
    ...
    <section class="questions-section">Open questions</section>
    <div class="report-footer">...</div>
  </div>
  <script>Keyboard shortcuts</script>
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
| Missing severity left border on cards | Always include `severity-critical/high/medium` class on finding cards. |
| Forgetting print styles | Always include `@media print` block. |
| Wrong default expand state | All critical cards get `open` class. High and medium cards are collapsed. |
| Finding card missing required sections | Every card MUST have: Current State h4, impact box, and remediation box. No exceptions. |
| Impact box without "Why this matters:" | Always lead with `<strong>Why this matters:</strong>` in impact boxes. |
| Remediation without numbered steps | Use `<ol>` in remediation boxes, not prose paragraphs. |
| Wrong impact box class for severity | Use `danger` for critical findings, `warning` for high, `info` for medium. |
| Non-sequential finding numbers | Always number findings #1, #2, #3... in document order, regardless of source numbering. |
| Finding cards without `id` attributes | Every card needs `id="finding-N"` for anchor linking from summary and cross-references. |
| Legend item numbers not linked | Each number in the donut legend should be an `<a href="#finding-N">` link. |
| Unlinked cross-references | Any mention of another finding (e.g., "see #6") must be an `<a href="#finding-N">` link. |
