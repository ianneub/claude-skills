# Elevation Protocol

Systematic process for transforming functional output into polished design. Work through each pass in order, completing one before moving to the next.

---

## Overview

```
Functional Draft → Typography → Color → Layout → Detail → Interrogation → Deliver
```

Each pass focuses on one dimension. This prevents overwhelming choices and ensures nothing is missed.

---

## Pass 1: Functional Draft

**Goal**: Content-complete, structurally sound, works correctly.

### Actions
- All content present and accurate
- Correct structure (headings, sections, hierarchy)
- Functional elements work (links, interactions, calculations)
- Placeholder content replaced with real content

### Not Yet
- Don't worry about visual appeal
- Default fonts and colors are fine
- Spacing can be rough

### Checkpoint
Can someone use this to accomplish their goal? If yes, proceed.

---

## Pass 2: Typography

**Goal**: Intentional type choices that create hierarchy and set tone.

### Actions

**1. Select fonts**
- Choose display font (headings, titles)
- Choose body font (paragraphs, content)
- Verify pairing works (contrast + harmony)
- Avoid: Arial, Roboto, system defaults

**2. Establish hierarchy**
- Set heading sizes (H1 > H2 > H3)
- Ensure clear visual distinction between levels
- Headlines should be significantly larger than body

**3. Refine details**
- Line height: 1.4-1.6 for body, tighter for headings
- Line length: aim for 45-75 characters
- Letter spacing: tighten large headings, default or slight open for body
- Font weights: use contrast (300 + 700, not 400 + 500)

**4. Check readability**
- Sufficient contrast (text on background)
- Appropriate size for viewing context
- Comfortable reading flow

### Checkpoint
Read through the content. Does typography enhance comprehension and set the right tone?

---

## Pass 3: Color

**Goal**: Cohesive palette that reinforces message and guides attention.

### Actions

**1. Define palette**
- Primary: dominant brand/mood color
- Secondary: supporting color (optional)
- Accent: call-to-action, emphasis
- Neutrals: backgrounds, text, borders

**2. Apply systematically**
- Background colors (hierarchy of surfaces)
- Text colors (primary, secondary, muted)
- Interactive elements (buttons, links)
- Status colors (success, warning, error)

**3. Create variables/tokens**
```css
--color-primary: #...;
--color-accent: #...;
--color-bg: #...;
--color-text: #...;
--color-text-muted: #...;
```

**4. Verify contrast**
- Text on backgrounds: 4.5:1 minimum
- Interactive elements distinguishable
- Color not sole indicator of meaning

### Checkpoint
Screenshot and squint. Is there clear color hierarchy? Does palette feel cohesive?

---

## Pass 4: Layout & Spacing

**Goal**: Intentional arrangement that guides the eye and groups related content.

### Actions

**1. Establish grid**
- Define column structure
- Set consistent gutters
- Align elements to grid lines

**2. Create spacing scale**
- Use consistent values: 8, 16, 24, 32, 48, 64, 96
- Never arbitrary spacing
- Larger space = more separation in meaning

**3. Apply whitespace**
- Generous margins (more than instinct)
- Breathing room around important elements
- Visual grouping through proximity

**4. Consider flow**
- Where does eye go first?
- Clear path through content
- Logical progression

**5. Check alignment**
- Nothing floating randomly
- Consistent edge alignment
- Baseline alignment for text

### Checkpoint
Draw lines connecting aligned elements. Is there an underlying structure?

---

## Pass 5: Detail & Polish

**Goal**: The finishing touches that separate amateur from professional.

### Actions

**1. Borders & dividers**
- Consistent weight throughout
- Subtle colors (not heavy black)
- Consider: do I need this divider? (spacing may be enough)

**2. Shadows & depth**
- Layered, subtle shadows
- Consistent depth language
- Purpose: hierarchy, not decoration

**3. Corner radius**
- Pick one value and use everywhere (or 2: small, large)
- Consistency is more important than the specific value

**4. Icons & images**
- Consistent style (outline, filled, thickness)
- Appropriate resolution
- Intentional sizing

**5. Micro-interactions (if applicable)**
- Hover states
- Focus indicators
- Transitions (200-300ms, ease-out)

**6. Empty/edge states**
- Loading states designed
- Empty states have personality
- Error states are helpful

### Checkpoint
Zoom to 200%. Are details consistent and polished? Zoom to 50%. Does overall composition work?

---

## Pass 6: Final Interrogation

**Goal**: Verify output meets professional standards.

### Actions
Run through design-interrogation.md checklist completely.

### Key questions
1. Would a design director approve this?
2. Does it look hand-crafted, not template-based?
3. What's the one memorable element?
4. Is every choice intentional?

### If gaps found
Return to relevant pass and address. Then re-run interrogation.

---

## Delivery

### Standard delivery
Present polished output only. No discussion of process unless asked.

### If user asks about process
"I applied systematic design elevation: establishing typography hierarchy, defining a cohesive color palette, refining layout and spacing, then adding polish and detail. Happy to walk through specific choices."

### If user asks for changes
Return to relevant pass, make adjustment, verify with interrogation.

---

## Quick Reference

| Pass | Focus | Time Investment |
|------|-------|-----------------|
| 1. Draft | Content, function | 40% |
| 2. Typography | Fonts, hierarchy | 15% |
| 3. Color | Palette, application | 10% |
| 4. Layout | Spacing, alignment | 15% |
| 5. Detail | Polish, consistency | 15% |
| 6. Interrogation | Verification | 5% |

The draft takes longest. Elevation passes are faster because each has narrow focus.
