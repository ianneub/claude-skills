---
name: professional-html-report
description: Use when generating a client-facing HTML report, executive brief, assessment, decision brief, or any polished, print-ready single-file document that should look professionally designed rather than like default HTML.
---

# Professional HTML Report

## Overview

Generate self-contained, single-file HTML reports in a **warm paper editorial** aesthetic — a centered "sheet" on warm off-white, set in Fraunces (serif display), Hanken Grotesk (body), and JetBrains Mono (labels/figures), with a single emerald accent and rust/amber severity coding. Restrained, print-ready, and suitable for executive and client audiences. No JS, no frameworks, no build step.

**`reference-report.html` (in this skill's folder) is the canonical implementation.** The fastest, most consistent way to produce a new report is to **start from that file**: keep its `<style>` block and structure, swap in your content, and drop the components you don't need. Everything below explains the system so you can adapt it well.

## When to Use

- Client-facing reports, assessments, audits, infrastructure/security reviews, decision briefs
- Executive summaries and one- to several-page documents that should look designed
- Anything destined for PDF/print or sharing as a standalone `.html` file

This skill is the general house style. For the heavier collapsible **findings-card** format (severity cards with mandatory Current-State / Impact / Remediation blocks, severity donut), see the `security-findings-report` skill, which layers on top of this one.

## Components are a toolkit, not a checklist

**Reach for the components a given report actually needs — never all of them by default.** The component library below is a palette to draw from, not a required sequence. A short decision brief might be just *masthead → verdict → two or three sections → footer*. A longer assessment might add the snapshot grid, comparison cards, a findings table, and an alert note.

- Don't force a snapshot grid, comparison cards, or a findings table where the content doesn't call for them.
- Don't pad a report to "look thorough." Length and which components appear are judgment calls that follow the content and the request.
- The reward for restraint is a document that looks intentional. The reward for dumping every component in is a document that looks like a template.

See **Report Length & Restraint** for how this interacts with requested length.

## Report Length & Restraint

**Structure scales to the requested length.**

- For a 1–2 page, "short", "concise", "brief", or "executive" report: prefer prose and a couple of compact components. A header, a verdict, a few sections, and a footer is a complete report.
- For a long, complex document: add the navigational/visual apparatus (more sections, snapshot grid, comparison cards, tables) where it genuinely aids the reader.
- Length follows the request, not the template. If asked for two pages, deliver two pages.

## Design Tokens

### Fonts (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,560;0,9..144,600;0,9..144,620;1,9..144,300;1,9..144,400;1,9..144,560&family=Hanken+Grotesk:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

- **Fraunces** — display: h1 title (with one italic accent word), section headings, large metric values, the italic deck. Use weights 560–620; the italic optical sizing gives it character.
- **Hanken Grotesk** — all running body text, paragraphs, list and row labels (400–600).
- **JetBrains Mono** — the kicker, every label, all figures/values, table headers, footer (use `font-variant-numeric: tabular-nums`).

### Palette (CSS variables)

```css
:root {
  --paper:#f6f2e9;        /* sheet background — warm off-white */
  --paper-deep:#ede7d8;   /* table row dividers, deeper warm tint */
  --paper-light:#fffdf6;  /* cards, snapshot/grid cell backgrounds */
  --ink:#20271f;          /* primary text, masthead/footer rules */
  --ink-soft:#51594b;     /* labels, captions, secondary text, Medium severity */
  --hairline:#c9c0ab;     /* cell borders, hairline rules */
  --accent:#1e7a4e;       /* EMERALD — accent word, section numbers, positive figures, "good" state, action numerals */
  --accent-soft:#e3ece5;  /* verdict-tab gradient, positive tint */
  --critical:#9a4a1e;     /* rust — Critical severity, "bad"/current state */
  --alert:#8c2f1b;        /* deeper red — blast-radius / alert note rule + lead */
}
/* High severity: #7a6020 (muted gold). html page behind the sheet: #dcd5c4 */
```

Emerald is the **positive/accent** color (good outcomes, the hardened state, the accent word) — never use it for a severity level. Severity runs rust (Critical) → muted gold (High) → ink-soft (Medium).

### Layout

- Body is a centered **sheet**: `max-width:880px; margin:48px auto 64px; padding:56px 64px 72px;` on `--paper` with a soft top radial highlight and a drop shadow, over an `html` background of `#dcd5c4`.
- Body text Hanken Grotesk `15px`/`1.55`, `-webkit-font-smoothing:antialiased`.

(Exact rules for all of the above are in `reference-report.html`.)

## Component Library

Each component is shown as a small usage snippet; copy the matching CSS from `reference-report.html`. Use the ones the report needs.

### Kicker masthead
A mono, uppercase, letter-spaced row split left/right with an ink underline — firm/confidentiality on the left, date on the right. Good on nearly every report.
```html
<div class="kicker"><span>EndeavorOps · Confidential Assessment</span><span>June 13, 2026</span></div>
```

### Title, accent word, client line
Fraunces h1 with exactly **one** word wrapped in `<em>` for the emerald italic accent; an optional mono client/subject line beneath.
```html
<h1>Cloud Security &amp; <em>Reliability</em> Assessment</h1>
<div class="h1-client">Brightwater Logistics</div>
```

### Deck
One italic Fraunces sentence framing the report. Skip it if the title is self-explanatory.
```html
<p class="deck">AWS production environment, reviewed against the CIS Benchmark and 90 days of telemetry.</p>
```

### Verdict tab ("The Bottom Line")
A bordered box with an overlapping mono tab and a gradient toward `--accent-soft`; bold the key phrases, color the positive figure with `class="pos"`. Ideal as the lead takeaway — strong on briefs and assessments.
```html
<div class="verdict"><div class="verdict-tab">The Bottom Line</div>
  <p>…<strong>three critical exposures</strong>… cost recovery (<span class="pos">~$11.4k/mo</span>)…</p></div>
```

### Numbered section heading
Fraunces heading with a mono emerald number and a hairline rule that fills the remaining width. Numbering is optional — drop `.sec-num` for an unnumbered report.
```html
<h2><span class="sec-num">01</span> Where things stand</h2>
```

### Snapshot grid (metric cells)
A 4-up grid of `mono label → Fraunces value → italic sub`. Use when a few headline numbers orient the reader; color one value with `.accent` (emerald) or `--critical` to draw the eye. Skip for reports without key metrics.

### Comparison cards (e.g. current vs target)
Two side-by-side cards with colored headers (rust `current`, emerald `hardened`) and dotted-divider rows of `label → mono value`. Use for before/after, current/target, option-A/option-B. Not every report has a comparison — omit when there isn't one.

### Findings / data table
Full-width table: mono uppercase headers, hairline dividers, right-aligned mono final column, severity as **colored text** (`.sev-critical` / `.sev-high` / `.sev-medium`), optional faint tint on `tr.row-critical`, italic `<caption>` for notes. Use colored text, **not** pill badges.

### Alert / callout note
A left-ruled tinted note with a mono lead label — for a blast-radius warning, caveat, or "read this first." `--alert` red for warnings; reskin with `--accent` for a positive/info note.
```html
<div class="note-alert"><div class="note-lead">Blast Radius</div><p>…</p></div>
```

### Action items
An ordered list with mono `decimal-leading-zero` emerald numerals and dotted dividers. Use for recommendations/next steps.
```html
<ol class="actions"><li>Revoke the public snapshot — today.</li>…</ol>
```

### Footer
Ink top rule, mono, split sources (left) / attribution (right).
```html
<div class="report-footer"><span>Sources: …</span><span class="footer-right">EndeavorOps · Prepared for Brightwater Logistics</span></div>
```

## Print & Responsive

Always include the print and responsive blocks from `reference-report.html`. The essentials:

```css
@media print {
  html { background: white; }
  body { box-shadow: none; max-width: 100%; padding: 24px 36px; font-size: 13px; margin: 0; }
  /* REQUIRED: browsers drop background fills in print/PDF by default. Without this the
     colored path-card headers, tinted cells, verdict, and alert note lose their fills. */
  *, *::before, *::after { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
  section { break-inside: avoid; }
  h2, h3 { break-after: avoid; page-break-after: avoid; }
}
@media (max-width: 720px) {
  body { padding: 32px 28px 48px; }
  .snapshot { grid-template-columns: repeat(2, 1fr); }
  .paths { grid-template-columns: 1fr; }
}
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using a JS framework or build step | Single-file HTML. No dependencies, no script. |
| Generic fonts (Inter, Roboto, Arial, system) | Use Fraunces + Hanken Grotesk + JetBrains Mono exactly. |
| Dark theme | This is a warm light paper theme. Colored fills are only the path-card headers, verdict, tinted cells, and the alert note. |
| Emerald used for a severity level | Emerald is the positive/accent color. Severity = rust (Critical) → gold (High) → ink-soft (Medium). |
| Severity as loud pill badges | Severity is colored **text** (`.sev-*`), not filled pills. |
| Forcing every component into every report | Components are a toolkit — use only what the content needs (see "Components are a toolkit"). |
| Padding a short report to look thorough | Match structure and length to the request. |
| More than one italic accent word in the h1 | Exactly one `<em>` accent word in the title. |
| Colored fills vanish in printed PDF | Keep the `print-color-adjust: exact !important` rule on `*` in `@media print`. |
| Table/section split awkwardly across printed pages | Keep `section { break-inside: avoid; }` and the heading `break-after: avoid` rules. |
