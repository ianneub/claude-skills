# Technique Catalog

Specific visual techniques organized by what they achieve. Select techniques that serve your design intent.

---

## Creating Visual Hierarchy

### Scale Contrast
Make important elements significantly larger than supporting content. Don't be timid—2x or 3x size difference creates clear hierarchy.
- Hero headlines: 48-72px (or larger)
- Section titles: 24-32px
- Body text: 16-18px
- Caption/meta: 12-14px

### Weight Contrast
Pair heavy and light font weights. Bold headings with regular body, or light display with medium body.
- Display: 700-900 weight
- Body: 400-500 weight
- Avoid: All medium weights (creates visual monotony)

### Color Weight
Use saturation and value to create hierarchy. Primary elements: full saturation. Secondary: reduced saturation. Tertiary: muted/gray.

### Position Dominance
Place primary content at optical center (slightly above mathematical center). Supporting content below or to sides.

### Isolation
Give important elements more whitespace. Crowded elements recede; isolated elements demand attention.

---

## Adding Sophistication

### Negative Space
Double or triple your instinctive margins. Professional work has more whitespace than amateur work.
- Page margins: 48-80px minimum
- Section padding: 64-120px vertical
- Element spacing: 24-48px

### Restraint
Remove elements that don't serve a purpose. If something can be removed without loss, remove it.

### Subtle Gradients
Instead of flat colors, use slight gradients (same hue, 5-10% value shift). Adds depth without calling attention.
```css
background: linear-gradient(180deg, #1a1a2e 0%, #16162a 100%);
```

### Refined Shadows
Multiple layered shadows feel more natural than single heavy shadows.
```css
box-shadow:
  0 1px 2px rgba(0,0,0,0.05),
  0 4px 8px rgba(0,0,0,0.05),
  0 16px 32px rgba(0,0,0,0.08);
```

### Border Subtlety
Replace visible borders with subtle separation: slight background color shifts, shadows, or spacing.

### Monochromatic Depth
Single color palette with varying shades creates sophistication. Add one accent color sparingly.

---

## Building Energy & Impact

### Diagonal Composition
Angle elements or content flow to create movement. Diagonal lines activate compositions.

### Bold Color Blocks
Large areas of saturated color create impact. Commit fully rather than using color tentatively.

### Contrast Extremes
High contrast (white on black, saturated on neutral) creates visual tension and energy.

### Asymmetric Balance
Off-center layouts with counterbalancing elements feel dynamic while remaining balanced.

### Scale Shock
One dramatically oversized element creates memorable impact.
- Oversized numbers: 120-200px for metrics
- Giant typography: Full-width headlines
- Large imagery: Full-bleed photos

### Unexpected Overlap
Elements that break grid boundaries and overlap create depth and interest.

---

## Establishing Trust & Professionalism

### Grid Discipline
Consistent column structure and alignment. Every element should align with something.
- 12-column grid for complex layouts
- 8-point baseline grid for vertical rhythm
- Consistent gutters throughout

### Consistent Spacing
Use a spacing scale (8, 16, 24, 32, 48, 64, 96). Never arbitrary values.

### Clean Typography
- Single typeface or well-matched pair
- Limited size variations (3-4 sizes)
- Consistent paragraph styling

### Neutral Foundations
Gray, white, and black foundations with color accents feel more professional than color-heavy palettes.

### Data Precision
Align decimal points. Use consistent precision. Format numbers appropriately (commas, units).

### Visual Consistency
Same corner radius everywhere. Same shadow depth. Same border weight. Same icon style.

---

## Creating Delight

### Unexpected Details
Small surprises reward attention:
- Custom cursors
- Hover state transformations
- Subtle background animations
- Easter eggs in empty states

### Micro-animations
Small movements that provide feedback:
- Button hover lifts
- Input focus transitions
- Loading state pulses
- Success celebrations

### Texture & Grain
Subtle texture adds warmth to digital surfaces:
```css
background-image: url("noise.png");
background-blend-mode: overlay;
opacity: 0.03;
```

### Custom Illustrations
Hand-drawn or stylized illustrations (not stock) create personality.

### Personality in Copy
Microcopy, empty states, and error messages as design opportunities.

### Generous Flourishes
One decorative element (gradient orb, geometric pattern, illustrated header) that doesn't serve function but adds character.

---

## Format-Specific Techniques

### Presentations / Slides
- One idea per slide
- Minimal text (30 words max)
- Full-bleed images or large whitespace
- Progressive disclosure (build slides)
- Consistent position for repeated elements
- Speaker notes for detail, slides for impact

### Spreadsheets / Tables
- Zebra striping (subtle, 2-3% color shift)
- Sticky headers with visual distinction
- Aligned decimal points
- Conditional formatting for data patterns
- Frozen rows/columns for context
- Grouped rows with visual hierarchy

### Dashboards
- Information hierarchy: KPIs → Trends → Details
- Sparklines for compact trend display
- Color coding with legend (not arbitrary colors)
- Consistent chart styles throughout
- Filtering controls clearly accessible
- Responsive card layouts

### PDFs / Reports
- Running headers/footers for navigation
- Consistent margins throughout
- Table of contents with page numbers
- Pull quotes for key insights
- Charts sized for reading context
- Appropriate image resolution (300dpi print, 72dpi screen)

### Data Visualizations
- Direct labeling over legends when possible
- Meaningful color encoding
- Axis labels with units
- Annotation for key data points
- Appropriate chart type for data relationship
- Avoid: 3D effects, pie charts for > 5 categories

### Email Templates
- Single column for mobile compatibility
- 600px max width
- System font stacks for reliability
- Bulletproof buttons (not image-based)
- Alt text for all images
- Preview text optimization

---

## Anti-Patterns to Avoid

### Generic Defaults
- System fonts without consideration
- Default blue links
- Bootstrap/Tailwind defaults unchanged
- Stock photography without curation

### Template Aesthetics
- Obvious template structure showing through
- Placeholder-looking content
- Generic icons and illustrations
- Cookie-cutter layouts

### Arbitrary Decisions
- Random padding values
- Inconsistent corner radii
- Mixed icon styles
- Colors without relationship

### Over-Decoration
- Gradients for gradient's sake
- Drop shadows on everything
- Excessive animation
- Decorative elements that obscure content

### Timid Execution
- Almost-but-not-quite bold
- Colors at 70% when they should be 100%
- Sizes that are "safe" rather than intentional
- Playing not to lose instead of playing to win
