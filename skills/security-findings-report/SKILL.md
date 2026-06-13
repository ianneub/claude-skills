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

## Component Library

### 1. Executive Summary with Charts

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

### 2. Finding Cards (collapsible)

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

### 3. Impact Box

```html
<div class="impact-box danger">  <!-- or warning, info -->
  <strong>Why this matters:</strong> Explanation text...
</div>
```
- `danger` = red accent (critical)
- `warning` = amber accent (high)
- `info` = blue accent (medium/informational)

Styling: 14px 18px padding, 6px border-radius, 13px font, colored background + border + text.

### 4. Remediation Box

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
